#!/usr/bin/env python3
"""Distance-weighted Tversky index (DTI) and Tversky loss for the GEMS Prize.

Research / validation tooling ONLY.
-----------------------------------
* This module scores a probability raster against a ground-truth raster.
* It never writes a GeoTIFF and never produces anything that can be submitted.

Why it exists
-------------
The hypothesis backlog (docs/hypotheses.html) needs hypotheses to move from
"untested" to "validated on spatial holdout". That requires the competition
metric. Nothing in this repository may generate a submission, but scoring
candidate maps on a held-out spatial block is research, not submission.

Metric definition (verbatim from the official problem description,
https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#performance-metric):

    k(d)  = (1 - d/R)+   with R = 300 m  (3 pixels at 100 m)
    TPw   = sum_{g in G}          max_{x : d(x,g) <= R} p(x) k(d(x,g))
    FPw   = sum_{x : p(x) > 0}    p(x) [ 1 - max_{g in G} k(d(x,g)) ]
    FNw   = sum_{g in G}        [ 1 - max_{x : d(x,g) <= R} p(x) k(d(x,g)) ]
    DTI   = TPw / (TPw + alpha*FPw + beta*FNw + eps)

with alpha = 0.2 (false-positive weight) and beta = 0.8 (false-negative weight).

Reading of "d": distance between pixel centres, in metres. The problem
description does not state whether d is centre-to-centre or edge-to-edge; this
implementation uses centre-to-centre Euclidean distance in metres, which is the
conventional choice and matches the "R = 300 m (i.e., 3 pixels at 100 m
resolution)" statement only under the centre-to-centre convention (a pixel 3
cells away has centre-to-centre distance 300 m). Flagged as an assumption.

Dependencies
------------
Pure standard library by default, so `--selftest` runs anywhere. NumPy is used
automatically when importable, which is what you want for a full
3730 x 3292 raster (see docs/feature-stack.html for those dimensions).
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from typing import Iterable, List, Sequence, Tuple

# Official competition constants (problem description, page 967).
ALPHA = 0.2   # false-positive penalty
BETA = 0.8    # false-negative penalty
R_METERS = 300.0
PIXEL_SIZE_M = 100.0
EPS = 1e-12

try:  # optional acceleration, not required for correctness
    import numpy as _np  # type: ignore
except Exception:  # pragma: no cover
    _np = None


# --------------------------------------------------------------------------
# kernel
# --------------------------------------------------------------------------
def kernel(d_meters: float, r: float = R_METERS) -> float:
    """Triangular kernel k(d) = max(1 - d/R, 0)."""
    if d_meters is None:
        return 0.0
    v = 1.0 - (float(d_meters) / float(r))
    return v if v > 0.0 else 0.0


# --------------------------------------------------------------------------
# offsets used by the pure-python path
# --------------------------------------------------------------------------
def _offsets(r_pixels: float) -> List[Tuple[int, int, float]]:
    """(dy, dx, distance_in_pixels) for every cell whose centre is within r."""
    rad = int(math.floor(r_pixels + 1e-9))
    out: List[Tuple[int, int, float]] = []
    for dy in range(-rad, rad + 1):
        for dx in range(-rad, rad + 1):
            d = math.hypot(dy, dx)
            if d <= r_pixels + 1e-9:
                out.append((dy, dx, d))
    out.sort(key=lambda t: t[2])
    return out


# --------------------------------------------------------------------------
# numpy implementation
# --------------------------------------------------------------------------
def _dti_numpy(pred, gt, r, pixel, alpha, beta, eps):
    p = _np.asarray(pred, dtype=_np.float64)
    g = _np.asarray(gt, dtype=_np.float64)
    if p.shape != g.shape:
        raise ValueError(f"shape mismatch: pred {p.shape} vs gt {g.shape}")
    p = _np.where(_np.isfinite(p), p, 0.0)
    p = _np.clip(p, 0.0, 1.0)
    g = (g > 0.5)

    r_px = r / pixel
    offs = _offsets(r_px)
    rad = int(math.floor(r_px + 1e-9))
    pad = ((rad, rad), (rad, rad))

    # --- TPw / FNw: for each ground-truth pixel, max over predicted pixels
    # within R of p(x) * k(d).  Do it with shifted slices.
    gp = _np.pad(g, pad, mode="constant", constant_values=False)
    pp = _np.pad(p, pad, mode="constant", constant_values=0.0)
    h, w = g.shape
    best = _np.zeros((h, w), dtype=_np.float64)
    for dy, dx, d in offs:
        k = kernel(d * pixel, r)
        if k <= 0.0:
            continue
        cand = pp[rad + dy: rad + dy + h, rad + dx: rad + dx + w] * k
        _np.maximum(best, cand, out=best)
    tp_w = float(best[g].sum())
    fn_w = float(g.sum()) - tp_w

    # --- FPw: for each predicted pixel, k at the distance to the nearest
    # ground-truth pixel.  Same shifted-slice trick, keeping the max kernel.
    kg = _np.zeros((h, w), dtype=_np.float64)
    for dy, dx, d in offs:
        k = kernel(d * pixel, r)
        if k <= 0.0:
            continue
        hit = gp[rad + dy: rad + dy + h, rad + dx: rad + dx + w]
        _np.maximum(kg, _np.where(hit, k, 0.0), out=kg)
    fp_w = float((p * (1.0 - kg)).sum())

    return _finish(tp_w, fp_w, fn_w, alpha, beta, eps)


# --------------------------------------------------------------------------
# pure-python implementation (small tiles / self-tests only)
# --------------------------------------------------------------------------
def _dti_python(pred: Sequence[Sequence[float]],
                gt: Sequence[Sequence[float]],
                r: float, pixel: float, alpha: float, beta: float, eps: float):
    h = len(gt)
    if h == 0:
        raise ValueError("empty raster")
    w = len(gt[0])
    for row in gt:
        if len(row) != w:
            raise ValueError("gt is not rectangular")
    if len(pred) != h or any(len(row) != w for row in pred):
        raise ValueError("pred/gt shape mismatch")

    r_px = r / pixel
    offs = _offsets(r_px)

    gset = [(y, x) for y in range(h) for x in range(w) if gt[y][x] > 0.5]

    # nearest ground-truth kernel value for every cell
    tp_w = 0.0
    for (gy, gx) in gset:
        best = 0.0
        for dy, dx, d in offs:
            y, x = gy + dy, gx + dx
            if 0 <= y < h and 0 <= x < w:
                pv = pred[y][x]
                if not math.isfinite(pv):
                    pv = 0.0
                pv = min(1.0, max(0.0, pv))
                if pv > 0.0:
                    v = pv * kernel(d * pixel, r)
                    if v > best:
                        best = v
        tp_w += best
    fn_w = float(len(gset)) - tp_w

    fp_w = 0.0
    for y in range(h):
        prow = pred[y]
        for x in range(w):
            pv = prow[x]
            if not math.isfinite(pv):
                pv = 0.0
            pv = min(1.0, max(0.0, pv))
            if pv <= 0.0:
                continue
            best_k = 0.0
            for dy, dx, d in offs:
                yy, xx = y + dy, x + dx
                if 0 <= yy < h and 0 <= xx < w and gt[yy][xx] > 0.5:
                    k = kernel(d * pixel, r)
                    if k > best_k:
                        best_k = k
                    break  # offsets are distance-sorted; first hit is nearest
            fp_w += pv * (1.0 - best_k)

    return _finish(tp_w, fp_w, fn_w, alpha, beta, eps)


def _finish(tp_w: float, fp_w: float, fn_w: float, alpha: float, beta: float, eps: float) -> dict:
    denom = tp_w + alpha * fp_w + beta * fn_w
    dti = tp_w / (denom + eps) if denom > 0 else 0.0
    return {
        "dti": dti,
        "TPw": tp_w,
        "FPw": fp_w,
        "FNw": fn_w,
        "alpha": alpha,
        "beta": beta,
        "R_meters": R_METERS,
        "denominator": denom,
        "eps": eps,
    }


# --------------------------------------------------------------------------
# public entry point
# --------------------------------------------------------------------------
def distance_weighted_tversky(pred, gt, r: float = R_METERS, pixel: float = PIXEL_SIZE_M,
                              alpha: float = ALPHA, beta: float = BETA,
                              eps: float = EPS) -> dict:
    """Score `pred` (float probability grid, 0..1) against `gt` (0/1 grid).

    Returns a dict with keys dti, TPw, FPw, FNw, alpha, beta, R_meters.
    """
    if _np is not None and hasattr(pred, "shape") and hasattr(gt, "shape"):
        return _dti_numpy(pred, gt, r, pixel, alpha, beta, eps)
    if _np is not None:
        try:
            return _dti_numpy(_np.asarray(pred), _np.asarray(gt), r, pixel, alpha, beta, eps)
        except Exception:
            pass
    return _dti_python(pred, gt, r, pixel, alpha, beta, eps)


def tversky_index(tp: float, fp: float, fn: float,
                  alpha: float = ALPHA, beta: float = BETA, eps: float = EPS) -> float:
    """Undistance-weighted Tversky index, TI = TP / (TP + a*FP + b*FN)."""
    denom = tp + alpha * fp + beta * fn
    return tp / (denom + eps) if denom > 0 else 0.0


def tversky_loss(tp: float, fp: float, fn: float,
                 alpha: float = ALPHA, beta: float = BETA, eps: float = EPS) -> float:
    """1 - Tversky index. Matches the reference solution's `smp.TverskyLoss`
    family of losses (alpha/beta weighting) but computed from counts."""
    return 1.0 - tversky_index(tp, fp, fn, alpha, beta, eps)


def masked_dti(pred, gt, known_mask, **kwargs) -> dict:
    """DTI with known USGS/INGENIOUS pixels excluded from *both* sides.

    DrivenData staff confirmed the official scoring mask is **pixel-exact** and
    identical to the provided training-fault labels
    (forum 11516, post 4, 2026-09-21). Pixels that are not masked but sit
    near a known fault are still fully penalised. This helper reproduces that
    so local holdouts behave like the real scorer.
    """
    if _np is None:
        raise RuntimeError("masked_dti needs numpy; install numpy or mask the arrays yourself")
    pred = _np.asarray(pred, dtype=_np.float64)
    gt = _np.asarray(gt, dtype=_np.float64)
    known = _np.asarray(known_mask) > 0.5
    p = _np.where(known, 0.0, pred)
    g = _np.where(known, 0.0, gt)
    out = distance_weighted_tversky(p, g, **kwargs)
    out["masked_pixels"] = int(known.sum())
    return out


# --------------------------------------------------------------------------
# self-tests
# --------------------------------------------------------------------------
def _grid(h: int, w: int, cells: Iterable[Tuple[int, int, float]]) -> List[List[float]]:
    g = [[0.0] * w for _ in range(h)]
    for y, x, v in cells:
        g[y][x] = float(v)
    return g


def selftest(verbose: bool = True) -> int:
    failures = 0

    def check(name: str, got: float, want: float, tol: float = 1e-9) -> None:
        nonlocal failures
        ok = abs(got - want) <= tol
        if not ok:
            failures += 1
        if verbose:
            print(f"  [{'PASS' if ok else 'FAIL'}] {name}: got {got:.10f} want {want:.10f}")

    print("distance-weighted Tversky index — self-tests")
    print(f"  backend: {'numpy' if _np is not None else 'pure python'}")

    # 1. perfect binary prediction on a single ground-truth pixel
    gt = _grid(7, 7, [(3, 3, 1.0)])
    pr = _grid(7, 7, [(3, 3, 1.0)])
    check("exact hit -> DTI 1.0", distance_weighted_tversky(pr, gt)["dti"], 1.0)

    # 2. prediction offset by 2 px = 200 m: k = 1 - 200/300 = 1/3
    #    TPw = 1/3, FPw = 2/3, FNw = 2/3 -> DTI = (1/3) / (1/3 + 0.2*2/3 + 0.8*2/3) = 1/3
    pr = _grid(7, 7, [(3, 5, 1.0)])
    check("200 m miss -> DTI 1/3", distance_weighted_tversky(pr, gt)["dti"], 1.0 / 3.0)

    # 3. no prediction at all -> complete false negative -> 0
    pr = _grid(7, 7, [])
    check("empty prediction -> 0", distance_weighted_tversky(pr, gt)["dti"], 0.0)

    # 4. prediction outside the 300 m support -> pure false positive -> 0
    gt2 = _grid(7, 7, [(0, 0, 1.0)])
    pr2 = _grid(7, 7, [(6, 6, 1.0)])
    check("beyond R -> 0", distance_weighted_tversky(pr2, gt2)["dti"], 0.0)

    # 5. probabilistic: p=0.5 exact plus p=0.25 one pixel away.
    #    TPw = max(0.5*1, 0.25*(1-1/3)) = 0.5
    #    FPw = 0.5*(1-1) + 0.25*(1/3)    = 1/12
    #    FNw = 1 - 0.5                   = 0.5
    #    DTI = 0.5 / (0.5 + 0.2/12 + 0.4) = 0.5 / (11/12 + 1/60)
    pr = _grid(7, 7, [(3, 3, 0.5), (3, 4, 0.25)])
    want = 0.5 / (0.5 + 0.2 * (1.0 / 12.0) + 0.8 * 0.5)
    check("probabilistic mix", distance_weighted_tversky(pr, gt)["dti"], want)

    # 6. kernel shape
    check("k(0) = 1", kernel(0.0), 1.0)
    check("k(150) = 0.5", kernel(150.0), 0.5)
    check("k(300) = 0", kernel(300.0), 0.0)
    check("k(400) = 0 (clipped)", kernel(400.0), 0.0)

    # 7. plain Tversky loss
    check("tversky_loss(1,0,0) = 0", tversky_loss(1.0, 0.0, 0.0), 0.0)
    check("tversky_loss(0,0,1) = 1", tversky_loss(0.0, 0.0, 1.0), 1.0)

    # 8. numpy and pure-python paths must agree (regression guard)
    if _np is not None:
        a = _np.zeros((9, 9), dtype=_np.float64)
        a[4, 4] = 1.0
        b = _np.zeros((9, 9), dtype=_np.float64)
        b[4, 5] = 0.7
        b[2, 2] = 0.3
        fast = _dti_numpy(b, a, R_METERS, PIXEL_SIZE_M, ALPHA, BETA, EPS)["dti"]
        slow = _dti_python(b.tolist(), a.tolist(), R_METERS, PIXEL_SIZE_M, ALPHA, BETA, EPS)["dti"]
        check("numpy == pure python", fast, slow, tol=1e-9)

    print(f"  {'ALL TESTS PASSED' if failures == 0 else str(failures) + ' FAILURE(S)'}")
    return 1 if failures else 0


def main(argv: List[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true",
                    help="run the built-in numeric checks (no data required)")
    ap.add_argument("--demo", action="store_true",
                    help="print a worked example as JSON")
    args = ap.parse_args(argv)

    if args.selftest or not (args.demo):
        rc = selftest()
        if args.selftest:
            return rc

    if args.demo:
        gt = _grid(9, 9, [(4, 3, 1.0), (4, 4, 1.0), (4, 5, 1.0)])
        pr = _grid(9, 9, [(4, 3, 0.9), (4, 4, 0.9), (4, 5, 0.9), (6, 4, 0.4)])
        res = distance_weighted_tversky(pr, gt)
        res["note"] = "worked example; not from the official scoring figure"
        print(json.dumps(res, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
