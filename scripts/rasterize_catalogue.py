#!/usr/bin/env python3
"""Rasterise the two public fault compilations onto the competition grid.

Research-only. Reads public files placed in data/raw/ (see
`scripts/download_competition_data.sh` / the `public-data` workflow) and writes:

* `data/raw/catalogue_grid.json`  -- counts and cross-checks (printed to stdout too)
* `data/raw/catalogue_grid.bin`   -- zlib-compressed uint8 bitmap, row-major,
                                     3730 x 3292: 1 = INGENIOUS, 2 = USGS, 3 = both

It produces NO prediction and NOTHING submittable. The point is provenance: once
the competition label raster is placed on an enrolled machine, it can be reconciled
against ~6,230 km of public catalogue trace on the exact grid the submission uses.

Grid geometry (documented sources):
  shape (3730, 3292), EPSG:32611, 100 m, origin (243350.0, 4508550.0) --
  as printed by the reference-solution notebook's rasterio profile read (see
  docs/feature-stack.html) and as re-published in the 13-check format gate output
  on the sibling entry site (2026-09-26). If `data/inventory.json` ever disagrees,
  that file wins and this script's defaults must be corrected.

Stamping convention: each polyline is densified at 25 m intervals and every pixel
containing a sample point is set. That is an "all-touched, quarter-pixel sampling"
convention -- closer to GDAL ALL_TOUCHED than to centroid rasterisation. It is
documented here so the later reconciliation diff can be interpreted correctly.
Distances are computed in EPSG:32611 metres, not geodesically.
"""
import json
import math
import sys
import zipfile
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT_JSON = RAW / "catalogue_grid.json"
OUT_BIN = RAW / "catalogue_grid.bin"

GRID = {
    "crs": "EPSG:32611",
    "width": 3292,
    "height": 3730,
    "res": 100.0,
    "origin_x": 243350.0,   # upper-left corner, per the documented geotransform
    "origin_y": 4508550.0,
    "densify_m": 25.0,
}

try:
    import shapefile  # pyshp
    from pyproj import CRS, Transformer
    from shapely.geometry import shape
    from shapely.ops import transform
except ImportError as exc:  # pragma: no cover
    print(f"missing dependency: {exc}. pip install pyshp shapely pyproj", file=sys.stderr)
    sys.exit(3)


def load_shp(shp: Path):
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


def unzip_shps(zp: Path, workdir: Path):
    d = workdir / zp.stem
    d.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zp) as z:
        z.extractall(d)
    return sorted(d.rglob("*.shp"))


def pixel_of(x, y):
    c = int((x - GRID["origin_x"]) // GRID["res"])
    r = int((GRID["origin_y"] - y) // GRID["res"])
    if 0 <= r < GRID["height"] and 0 <= c < GRID["width"]:
        return r, c
    return None


def stamp(geom_utm, bitmap, value, per_value_counts):
    """Densify a (Multi)LineString at GRID['densify_m'] metres and stamp pixels."""
    lines = []
    if geom_utm.geom_type == "LineString":
        lines = [geom_utm]
    elif geom_utm.geom_type == "MultiLineString":
        lines = list(geom_utm.geoms)
    else:
        return 0
    stamped = 0
    for ln in lines:
        n = max(2, int(math.ceil(ln.length / GRID["densify_m"])) + 1)
        for i in range(n):
            pt = ln.interpolate(i / (n - 1), normalized=True)
            px = pixel_of(pt.x, pt.y)
            if px is None:
                continue
            r, c = px
            off = r * GRID["width"] + c
            old = bitmap[off]
            if old != value:
                bitmap[off] = 3 if (old and old != value) else value
                stamped += 1
    per_value_counts["stamped_pixel_touches"] += stamped
    return stamped


GRID_BBOX = (GRID["origin_x"], GRID["origin_y"] - GRID["height"] * GRID["res"],
             GRID["origin_x"] + GRID["width"] * GRID["res"], GRID["origin_y"])


def rasterise_layer(shp_path, bitmap, value, to_utm_cache):
    geoms, crs, n, fields, recs = load_shp(shp_path)
    if crs is None:
        return {"shapefile": str(shp_path), "status": "no .prj — skipped"}
    key = crs.to_string()
    if key not in to_utm_cache:
        to_utm_cache[key] = Transformer.from_crs(crs, "EPSG:32611", always_xy=True).transform
    utm = [transform(to_utm_cache[key], g) for g in geoms]
    x0, y0, x1, y1 = GRID_BBOX
    margin = 1000.0
    near = [g for g in utm
            if g.bounds[0] <= x1 + margin and g.bounds[2] >= x0 - margin
            and g.bounds[1] <= y1 + margin and g.bounds[3] >= y0 - margin]
    counts = {"stamped_pixel_touches": 0}
    for g in near:
        stamp(g, bitmap, value, counts)
    touched = sum(1 for i in range(len(bitmap)) if bitmap[i] in (value, 3))
    return {
        "shapefile": shp_path.name,
        "crs": key,
        "records": n,
        "records_within_grid_bbox_margin_1km": len(near),
        "stamp_convention": f"densify {GRID['densify_m']} m, all-touched",
        "pixels_with_this_value_after_merge": touched,
    }


def main() -> int:
    need = {"ingenious": RAW / "qfaults_v2.zip", "usgs": RAW / "Qfaults_GIS.zip",
            "extent": RAW / "GeoDAWN_data_extent.zip"}
    missing = [k for k, p in need.items() if not p.exists()]
    if missing:
        print(f"blocked: missing public files {missing} in {RAW}", file=sys.stderr)
        return 2

    npix = GRID["width"] * GRID["height"]
    bitmap = bytearray(npix)
    work = RAW / "_unzipped"
    cache = {}
    report = {"grid": GRID, "layers": {}}

    for shp in unzip_shps(need["ingenious"], work)[:1]:
        report["layers"]["ingenious_qfaults_v2"] = rasterise_layer(shp, bitmap, 1, cache)
    for shp in unzip_shps(need["usgs"], work):
        if shp.stem == "Qfaults_US_Database":
            report["layers"]["usgs_qffd"] = rasterise_layer(shp, bitmap, 2, cache)

    ing = sum(1 for b in bitmap if b in (1, 3))
    usgs = sum(1 for b in bitmap if b in (2, 3))
    both = sum(1 for b in bitmap if b == 3)
    report["grid"]["pixels"] = {
        "total": npix,
        "ingenious_stamped": ing,
        "usgs_stamped": usgs,
        "union": sum(1 for b in bitmap if b),
        "intersection": both,
        "intersection_share_of_union": round(both / max(1, sum(1 for b in bitmap if b)), 4),
        "reference_figure_label_raster_catalogue_px": 60988,
        "reference_figure_source": "published sibling-site baseline table + site header (2026-09), "
                                   "NOT measured here — competition labels are not in this repository",
    }

    OUT_JSON.write_text(json.dumps(report, indent=2))
    OUT_BIN.write_bytes(zlib.compress(bytes(bitmap), 9))
    print(json.dumps(report, indent=2))
    print(f"bitmap: {npix} px -> {OUT_BIN} ({OUT_BIN.stat().st_size} bytes zlib)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
