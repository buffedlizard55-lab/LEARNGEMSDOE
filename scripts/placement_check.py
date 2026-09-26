#!/usr/bin/env python3
"""Metric-aware placement check: dense emission vs. spaced nodes, under our own DTI.

Research / analysis tooling ONLY.
-----------------------------------
* Uses `scripts/metrics.py` (the verified distance-weighted Tversky implementation,
  alpha=0.2, beta=0.8, R=300 m) to measure a claim made by the sibling "Pindrop"
  experiment page: that emitting hard pixels at a spacing of ~4-5 pixels beats a
  dense one-pixel ridge at the same pixel budget, because each ground-truth pixel
  is credited from its single best prediction within the kernel.
* It writes no GeoTIFF and touches no competition data. Everything below is
  synthetic geometry on small tiles (pure-python backend, no numpy needed).

What is being verified, and what is not
----------------------------------------
Verified (locally, with our metric):
  1. When the truth trace is longer than the dense budget can cover, a spaced
     schedule out-scores the dense prefix at the same budget (coverage beats width).
  2. On an axis-aligned straight trace, spacing s <= 5 keeps every covered truth
     pixel inside the kernel (worst-case gap s/2 < R = 3 px) -- the published
     derivation. Spacing 4 leaves a margin of one pixel.
  3. The same square-suppression rule (Chebyshev distance >= s between nodes) does
     NOT preserve coverage on a diagonal trace: nodes end up s*sqrt(2) px apart,
     so for s=4 the midpoint sits 2.83 px from the nearest node and earns
     k = 1 - 283/300 = 0.057 -- a near-miss inside the kernel. The published
     "worst-case gap 2.0 px" figure holds only for 4-connected geometry.

Not verified here: the sibling sites' emitted files, budgets, or suppressions --
no sibling repository is checked out from this one, by design. This script checks
the geometry of the method, not a specific artifact.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import metrics  # noqa: E402

TILE = 80   # square tile side, pixels (small: pure-python backend)
BUDGET = 40  # emitted prediction pixels per policy


def trace_cells(kind: str, start=(8, 8), length=200):
    """Ordered (y, x) cells of a synthetic 1-px trace, clipped to the tile."""
    y0, x0 = start
    cells, seen = [], set()
    for i in range(length):
        if kind == "axis":            # E-W line
            y, x = y0, x0 + i
        elif kind == "diag":          # exact 45-degree staircase (Chebyshev steps of 1)
            y, x = y0 + i, x0 + i
        elif kind == "slope12":       # oblique: +1 row every 2 cols (Bresenham-ish)
            y, x = y0 + i // 2, x0 + i
        else:
            raise ValueError(kind)
        if 0 <= y < TILE and 0 <= x < TILE and (y, x) not in seen:
            seen.add((y, x))
            cells.append((y, x))
    return cells


def dense_policy(truth, budget):
    """First `budget` pixels of the trace -- what a confidence floor emits."""
    return set(truth[:budget])


def nodes_policy(truth, budget, spacing):
    """Greedy square suppression: accept a trace pixel only if no accepted node is
    within a square of half-width spacing-1 (Chebyshev distance < spacing).
    This mirrors the rule documented on the sibling experiment page."""
    acc = []
    for (y, x) in truth:
        if all(max(abs(y - ay), abs(x - ax)) >= spacing for ay, ax in acc):
            acc.append((y, x))
            if len(acc) >= budget:
                break
    return set(acc)


def disc_policy(truth, budget, spacing):
    """Greedy disc suppression: accept only if no accepted node is within Euclidean
    distance < spacing. Arc-length worst case is then spacing/2 px on ANY
    orientation (the isotropic fix for the diagonal failure mode)."""
    acc = []
    for (y, x) in truth:
        if all((y - ay) ** 2 + (x - ax) ** 2 >= spacing * spacing for ay, ax in acc):
            acc.append((y, x))
            if len(acc) >= budget:
                break
    return set(acc)


def grid_from(cells, h, w):
    g = [[0.0] * w for _ in range(h)]
    for (y, x) in cells:
        g[y][x] = 1.0
    return g


def run(kind, truth_len, budget, spacings):
    truth = trace_cells(kind, length=truth_len)
    gt = grid_from(truth, TILE, TILE)
    out = {"trace": kind, "truth_px": len(truth), "budget": budget, "policies": {}}
    for name, cells in [("dense", dense_policy(truth, budget))] + [
        (f"nodes_s{s}", nodes_policy(truth, budget, s)) for s in spacings
    ] + [
        (f"disc_s{s}", disc_policy(truth, budget, s)) for s in spacings if s > 1
    ]:
        res = metrics.distance_weighted_tversky(grid_from(cells, TILE, TILE), gt)
        out["policies"][name] = {
            "emitted_px": len(cells),
            "on_supplied_convention": "all pixels at 1.0, all on the truth trace",
            "TPw": round(res["TPw"], 3),
            "FPw": round(res["FPw"], 3),
            "FNw": round(res["FNw"], 3),
            "dti": round(res["dti"], 4),
            "tpw_per_emitted": round(res["TPw"] / max(1, len(cells)), 4),
        }
    return out


def main() -> int:
    report = {
        "constants": {
            "alpha": metrics.ALPHA, "beta": metrics.BETA,
            "R_meters": metrics.R_METERS, "pixel_meters": metrics.PIXEL_SIZE_M,
            "note": "hard emission (1.0); DTI here is the full-coverage form, "
                    "known-mask irrelevant because every prediction sits on the synthetic trace",
        },
        "cases": [],
    }
    # Coverage-constrained regime: truth is 4x the dense budget (the regime the
    # sibling page argues from). Also the budget-matched regime L == budget, where
    # dense wins by construction.
    for kind in ("axis", "diag", "slope12"):
        for L in (BUDGET, 4 * BUDGET):
            report["cases"].append(run(kind, L, BUDGET, (1, 4, 5, 6)))

    # Diagonal-coverage decomposition: mean credit per covered truth pixel for
    # nodes_s4 on a diagonal trace (the square-suppression caveat).
    truth = trace_cells("diag", length=4 * BUDGET)
    gt = grid_from(truth, TILE, TILE)
    nodes = nodes_policy(truth, BUDGET, 4)
    pred = grid_from(nodes, TILE, TILE)
    # per-truth-pixel best credit, reusing metrics' kernel machinery
    import math
    offs = metrics._offsets(metrics.R_METERS / metrics.PIXEL_SIZE_M)
    credits = []
    for (gy, gx) in truth:
        best = 0.0
        for dy, dx, d in offs:
            y, x = gy + dy, gx + dx
            if 0 <= y < TILE and 0 <= x < TILE and pred[y][x] > 0.0:
                k = metrics.kernel(d * metrics.PIXEL_SIZE_M)
                if k > best:
                    best = k
        credits.append(best)
    hit = [c for c in credits if c > 0.0]
    report["diagonal_decomposition_s4"] = {
        "truth_px": len(truth),
        "node_px": len(nodes),
        "mean_credit_all_truth_px": round(sum(credits) / len(credits), 4),
        "mean_credit_covered_truth_px": round(sum(hit) / len(hit), 4) if hit else None,
        "share_truth_px_below_0_1": round(sum(1 for c in credits if c < 0.1) / len(credits), 4),
        "min_gap_to_node_px": None,
        "worst_case_note": (
            "nodes are Chebyshev-spaced 4 -> euclidian 4*sqrt(2)=5.66 px on a 45-degree "
            "trace; midpoint distance 2.83 px -> kernel credit "
            f"{metrics.kernel(2 * 2 ** 0.5 * metrics.PIXEL_SIZE_M):.4f}"
        ),
        "axis_worst_case_note": (
            "axis-aligned s=4: worst-case gap 2.0 px -> kernel credit "
            f"{metrics.kernel(2.0 * metrics.PIXEL_SIZE_M):.4f}; s=5 gives "
            f"{metrics.kernel(2.5 * metrics.PIXEL_SIZE_M):.4f}; s=6 gives "
            f"{metrics.kernel(3.0 * metrics.PIXEL_SIZE_M):.4f}"
        ),
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
