#!/usr/bin/env python3
"""Clip the public INGENIOUS Qfaults v2 layer to the public GeoDAWN outline polygons.

Research-only. Reads public files placed in data/raw/ by scripts/download_competition_data.sh
(or by the `public-data` GitHub Actions workflow). Writes data/raw/public_census.json.
Does NOT touch competition rasters and does NOT produce any prediction or submission file.

Every number it prints is computed from the downloaded files; nothing is hard-coded.
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
    prj = shp.with_suffix(".prj")
    crs = CRS.from_wkt(prj.read_text()) if prj.exists() else None
    r = shapefile.Reader(str(shp))
    fields = [f[0] for f in r.fields[1:]]
    geoms, recs = [], []
    for sr in r.iterShapeRecords():
        if sr.shape.points:
            geoms.append(shape(sr.shape.__geo_interface__))
            recs.append(dict(zip(fields, sr.record)))
    return geoms, crs, len(r), fields, members, shp.name, recs


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
    report = {"files": {}, "layers": {}, "clip": {}}
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
        ftype, mapscale = {}, {}
        for i in idx:
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
        }
    report["qfaults_total_records"] = len(fault_geoms)
    OUT.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
