#!/usr/bin/env bash
# Download helper for GEMS Prize rasters.
# Does not scrape DrivenData, does not store credentials, does not write predictions.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data"
mkdir -p "$DATA"

HUB="https://www.drivendata.org/competitions/306/competition-doe-gems/"
DATA_TAB="https://www.drivendata.org/competitions/306/competition-doe-gems/data/"
PROBLEM="https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#provided-features"

echo "GEMSDOE data placement"
echo "======================"
echo "Official hub:     $HUB"
echo "Data tab (login): $DATA_TAB"
echo "Feature list:     $PROBLEM"
echo
echo "This script will NOT log in to DrivenData."
echo "On an enrolled machine, download the competition files into:"
echo "  $DATA"
echo
echo "Expected names from the problem description:"
echo "  training_features.tif"
echo "  1m_DEM_links.csv"
echo "  training labels (vector and/or raster; names as given on the data tab)"
echo "  sample submission GeoTIFF"
echo
echo "Reference-solution local names (may be copies/renames of the same rasters):"
echo "  numeric_features.tif"
echo "  labels.tif"
echo "  See https://github.com/drivendataorg/gems-prize-reference-solution"
echo

found=0
shopt -s nullglob
for f in "$DATA"/*.tif "$DATA"/*.tiff "$DATA"/*.csv; do
  echo "found: $f"
  found=1
done

if [[ "$found" -eq 0 ]]; then
  echo "STATUS: no GeoTIFF/CSV yet in data/ — training remains blocked."
  echo "After placing files, run: python scripts/prepare_data.py"
  exit 2
fi

echo "STATUS: some files present. Run: python scripts/prepare_data.py"
exit 0
