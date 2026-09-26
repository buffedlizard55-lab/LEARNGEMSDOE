#!/usr/bin/env python3
"""Clip the public INGENIOUS Qfaults v2 layer to the public GeoDAWN outline polygons,
and measure the positional offset between the USGS QFFD traces and the INGENIOUS traces.

Research-only. Reads public files placed in data/raw/ by scripts/download_competition_data.sh
(or by the `public-data` GitHub Actions workflow). Writes data/raw/public_census.json.
Does NOT touch competition rasters and does NOT produce any prediction or submission file.

Every number it prints is computed from the downloaded files; nothing is hard-coded.
Distances are computed in the INGENIOUS layer's own projected CRS (NAD83 Contiguous USA Albers,
metres), not geodesically.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = RAW / "public_census.json"

try:
    import shapefile  # pyshp
    from pyproj import CRS, Transformer
    from shapely.geometry import shape
    from shapely.ops import transform, unary_union
except ImportError as exc:  # pragma: no cover
    print(f"missing dependency: {exc}. pip install pyshp shapely pyproj", file=sys.stderr)
    sys.exit(3)


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def load_shp(shp: Path):
    """Return (geoms, crs, record_count, field_names, records) for one .shp."""
    prj = shp.with_suffix(".prj")
    crs = CRS.from_wkt(prj.read_text()) if prj.exists() else None
    r = shapefile.Reader(str(shp))
    fields = [f[0] for f in r.fields[1:]]
    geoms, recs = [], []
    for sr in r.iterShapeRecords():
        if sr.shape.points:
            geoms.append(shape(sr.shape.__geo_interface__))
            recs.append(dict(zip(fields, sr.record)))
    return geoms, crs, len(r), fields, recs


def load_zip(zp: Path, workdir: Path):
    """Return (list of shapely geoms, CRS, record count, field names) for the first .shp in zp."""
    d = workdir / zp.stem
    d.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zp) as z:
        z.extractall(d)
        members = z.namelist()
    shps = sorted(d.rglob("*.shp"))
    if not shps:
        raise RuntimeError(f"{zp.name}: no .shp inside (members: {members})")
    shp = shps[0]
    geoms, crs, n, fields, recs = load_shp(shp)
    return geoms, crs, n, fields, members, shp.name, recs


def unzip_all_shps(zp: Path, workdir: Path):
    """Extract zp and return [(shp path, members)] for every .shp it contains."""
    d = workdir / zp.stem
    d.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zp) as z:
        z.extractall(d)
        members = z.namelist()
    return [(s, members) for s in sorted(d.rglob("*.shp"))]


def nearest_distances(sources, targets):
    """For each target geometry, the distance to the nearest source geometry.

    Uses shapely's STRtree when available (shapely >= 2.0); otherwise falls back to a
    brute-force scan so the script still runs on older installs.
    """
    out = []
    if not sources or not targets:
        return out
    try:
        from shapely.strtree import STRtree

        tree = STRtree(sources)
        if hasattr(tree, "query_nearest"):
            for g in targets:
                idx = tree.query_nearest(g)
                if len(idx):
                    out.append(float(g.distance(sources[int(idx[0])])))
            return out
    except Exception:  # pragma: no cover - fall through to brute force
        pass
    for g in targets:
        out.append(min(g.distance(s) for s in sources))
    return out


def distance_stats(values):
    """Percentiles and tail shares, in metres, from a list of distances."""
    if not values:
        return {"n": 0}
    v = sorted(values)
    n = len(v)

    def pct(q):
        if n == 1:
            return round(v[0], 1)
        k = min(n - 1, max(0, int(round(q * (n - 1)))))
        return round(v[k], 1)

    def share(limit):
        return round(sum(1 for x in v if x <= limit) / n, 4)

    return {
        "n": n,
        "min_m": round(v[0], 1),
        "p25_m": pct(0.25),
        "median_m": pct(0.50),
        "p75_m": pct(0.75),
        "p90_m": pct(0.90),
        "p95_m": pct(0.95),
        "p99_m": pct(0.99),
        "max_m": round(v[-1], 1),
        "share_le_50m": share(50),
        "share_le_100m": share(100),
        "share_le_300m": share(300),
        "share_le_400m": share(400),
        "share_gt_1000m": round(sum(1 for x in v if x > 1000) / n, 4),
    }


def main() -> int:
    need = {
        "area1": RAW / "GeoDAWN_area1_outline.zip",
        "area2": RAW / "GeoDAWN_area2_outline.zip",
        "extent": RAW / "GeoDAWN_data_extent.zip",
        "qfaults": RAW / "qfaults_v2.zip",
    }
    missing = [k for k, p in need.items() if not p.exists()]
    if missing:
        print(f"blocked: missing public files {missing} in {RAW}", file=sys.stderr)
        return 2

    work = RAW / "_unzipped"
    report = {"files": {}, "layers": {}, "clip": {}, "offsets": {}}
    loaded = {}
    for k, p in need.items():
        geoms, crs, n, fields, members, shp, recs = load_zip(p, work)
        loaded[k] = (geoms, crs, recs)
        report["files"][k] = {"name": p.name, "bytes": p.stat().st_size, "sha256": sha256(p), "members": members}
        report["layers"][k] = {
            "shapefile": shp,
            "records": n,
            "crs": crs.to_string() if crs else None,
            "fields": fields,
        }
        if k != "qfaults":  # polygon attribute values are tiny; keep them for cross-checks
            report["layers"][k]["attributes"] = [{a: str(b) for a, b in rec.items()} for rec in recs]

    fault_geoms, fault_crs, fault_recs = loaded["qfaults"]
    if fault_crs is None:
        print("qfaults has no .prj; refusing to guess a CRS", file=sys.stderr)
        return 4
    for k in ("area1", "area2", "extent"):
        geoms, crs, _ = loaded[k]
        if crs is None:
            report["clip"][k] = "no .prj — skipped rather than guessing a CRS"
            continue
        tf = Transformer.from_crs(crs, fault_crs, always_xy=True).transform
        poly = unary_union([transform(tf, g) for g in geoms])
        idx = [i for i, g in enumerate(fault_geoms) if g.intersects(poly)]
        inter = [fault_geoms[i] for i in idx]
        inside_len = sum(g.intersection(poly).length for g in inter)
        ftype, mapscale, ftype_len = {}, {}, {}
        for i in idx:
            fl = str(fault_recs[i].get("FTYPE_", "")).strip() or "(blank)"
            ftype_len[fl] = ftype_len.get(fl, 0.0) + fault_geoms[i].intersection(poly).length
            f = str(fault_recs[i].get("FTYPE_", "")).strip() or "(blank)"
            m = str(fault_recs[i].get("MAPSCALE", "")).strip() or "(blank)"
            ftype[f] = ftype.get(f, 0) + 1
            mapscale[m] = mapscale.get(m, 0) + 1
        report["clip"][k] = {
            "traces_intersecting": len(inter),
            "clipped_length_in_fault_crs_units": round(inside_len, 1),
            "fault_crs_units": fault_crs.axis_info[0].unit_name if fault_crs.axis_info else None,
            "polygon_area_in_fault_crs_units2": round(poly.area, 1),
            "ftype_counts": dict(sorted(ftype.items())),
            "mapscale_counts": dict(sorted(mapscale.items())),
            "ftype_clipped_length_m": {a: round(b, 1) for a, b in sorted(ftype_len.items())},
        }
    report["qfaults_total_records"] = len(fault_geoms)

    # ------------------------------------------------------------------ offsets
    # Compare the USGS QFFD GIS distribution against the INGENIOUS compilation inside the
    # GeoDAWN data extent. This is a proxy for the "corrections to existing traces" class the
    # organisers say they are aiming for: two independent compilations of the same faults.
    extent_zip = RAW / "GeoDAWN_data_extent.zip"
    usgs_zip = RAW / "Qfaults_GIS.zip"
    if not usgs_zip.exists():
        report["offsets"] = {
            "status": "blocked_no_usgs_qfaults_gis",
            "expected_url": "https://earthquake.usgs.gov/static/lfs/nshm/qfaults/Qfaults_GIS.zip",
        }
    else:
        report["files"]["usgs_qfaults_gis"] = {
            "name": usgs_zip.name,
            "bytes": usgs_zip.stat().st_size,
            "sha256": sha256(usgs_zip),
        }
        geoms, crs, _ = loaded["extent"]
        tf = Transformer.from_crs(crs, fault_crs, always_xy=True).transform
        poly = unary_union([transform(tf, g) for g in geoms])
        footprint_idx = [i for i, g in enumerate(fault_geoms) if g.intersects(poly)]
        footprint_geoms = [fault_geoms[i] for i in footprint_idx]
        layers = {}
        for shp, members in unzip_all_shps(usgs_zip, work):
            ugeoms, ucrs, n, ufields, _ = load_shp(shp)
            entry = {
                "shapefile": str(shp.relative_to(work)),
                "records": n,
                "crs": ucrs.to_string() if ucrs else None,
                "fields": ufields[:14],
            }
            if ucrs is None:
                entry["status"] = "no .prj — skipped rather than guessing a CRS"
                layers[shp.stem] = entry
                continue
            ut = Transformer.from_crs(ucrs, fault_crs, always_xy=True).transform
            ugeoms_fc = [transform(ut, g) for g in ugeoms]
            u_in = [g for g in ugeoms_fc if g.intersects(poly)]
            entry["traces_intersecting_extent"] = len(u_in)
            entry["ingenious_footprint_trace_to_nearest_usgs"] = distance_stats(
                nearest_distances(ugeoms_fc, footprint_geoms)
            )
            entry["usgs_extent_trace_to_nearest_ingenious"] = distance_stats(
                nearest_distances(fault_geoms, u_in)
            )
            layers[shp.stem] = entry
        report["offsets"] = {
            "status": "measured",
            "distance_crs": fault_crs.to_string(),
            "distance_note": "computed in the INGENIOUS layer's Albers equal-area projection (metres), not geodesically",
            "ingenious_footprint_traces": len(footprint_geoms),
            "usgs_layers": layers,
        }

    OUT.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
