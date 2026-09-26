#!/usr/bin/env python3
"""Inspect competition rasters if present. Never writes a prediction GeoTIFF."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "inventory.json"

# Official / reference names documented in the knowledge base.
CANDIDATES = [
    "training_features.tif",
    "numeric_features.tif",
    "labels.tif",
    "training_labels.tif",
    "1m_DEM_links.csv",
]


def inspect_tif(path: Path) -> dict:
    try:
        import rasterio  # type: ignore
    except ImportError:
        return {
            "path": str(path),
            "error": "rasterio not installed; file present but not opened",
            "size_bytes": path.stat().st_size,
        }
    info: dict = {"path": str(path), "size_bytes": path.stat().st_size}
    with rasterio.open(path) as src:
        info.update(
            {
                "width": src.width,
                "height": src.height,
                "count": src.count,
                "crs": str(src.crs) if src.crs else None,
                "transform": list(src.transform),
                "res": list(src.res),
                "dtypes": list(src.dtypes),
                "nodata": src.nodata,
                "bounds": {
                    "left": src.bounds.left,
                    "bottom": src.bounds.bottom,
                    "right": src.bounds.right,
                    "top": src.bounds.top,
                },
                "band_tags": [src.tags(i) for i in range(1, src.count + 1)],
            }
        )
    return info


def main() -> int:
    DATA.mkdir(exist_ok=True)
    report: dict = {
        "note": "Inspection only. This script does not generate or validate a prize submission.",
        "data_dir": str(DATA),
        "files": [],
        "missing_documented_names": [],
    }
    for name in CANDIDATES:
        p = DATA / name
        if not p.exists():
            report["missing_documented_names"].append(name)
    extras = sorted(
        {
            *DATA.glob("*.tif"),
            *DATA.glob("*.tiff"),
            *DATA.glob("*.csv"),
        }
    )
    if not extras:
        report["status"] = "blocked_no_data"
        OUT.write_text(json.dumps(report, indent=2))
        print(json.dumps(report, indent=2))
        print("\nNo rasters in data/. Download from the DrivenData data tab after login.", file=sys.stderr)
        return 2
    for p in extras:
        if p.suffix.lower() in {".tif", ".tiff"}:
            report["files"].append(inspect_tif(p))
        else:
            report["files"].append(
                {
                    "path": str(p),
                    "size_bytes": p.stat().st_size,
                    "kind": "csv",
                    "head": p.read_text(errors="replace").splitlines()[:8],
                }
            )
    report["status"] = "inspected"
    OUT.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
