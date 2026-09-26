#!/usr/bin/env bash
# Placement helper for GEMS Prize research data.
# Does not log in to DrivenData, does not store credentials, does not write predictions.
# Competition rasters stay behind the data-tab login. Public USGS / GDR files are attempted
# only so catalogue-gap research can proceed without a second account.
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data"
RAW="$DATA/raw"
mkdir -p "$DATA" "$RAW"

HUB="https://www.drivendata.org/competitions/306/competition-doe-gems/"
DATA_TAB="https://www.drivendata.org/competitions/306/competition-doe-gems/data/"
PROBLEM="https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#provided-features"

echo "GEMSDOE data placement"
echo "======================"
echo "Official hub:     $HUB"
echo "Data tab (login): $DATA_TAB"
echo "Feature list:     $PROBLEM"
echo
echo "This script will NOT log in to DrivenData and will NOT create an account."
echo

# Probe the data tab. A login redirect is the expected official behaviour.
echo "-- data-tab probe --"
probe_file="$RAW/data-tab-probe.txt"
if curl -fsSL --max-time 25 -o "$probe_file" -w "http_code=%{http_code} redirect=%{url_effective}\n" "$DATA_TAB"; then
  echo "data-tab fetch wrote $probe_file"
else
  echo "data-tab fetch failed (curl exit $?). Exit 35 is a TLS failure, not a login redirect."
  echo "A separate fetch of the same URL on 2026-09-26 did reach the login page. Do not conflate the two."
fi
echo

# Small public files verified from the ScienceBase item JSON on 2026-09-26.
# Sizes and MD5s are from that JSON, not from a local download.
# https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7?format=json
# The USGS QFFD GIS zip URL and 16 MB size were read off the official USGS faults page
# https://www.usgs.gov/programs/earthquake-hazards/faults on 2026-09-26.
echo "-- public outline attempt (no DrivenData login) --"
declare -A PUBLIC
PUBLIC[GeoDAWN_area1_outline.zip]="https://www.sciencebase.gov/catalog/file/get/657e1d85d34e23d3533209f7?f=__disk__09%2Ff1%2Fa5%2F09f1a519280068416e999b331e3596b7e38e8a93"
PUBLIC[GeoDAWN_area2_outline.zip]="https://www.sciencebase.gov/catalog/file/get/657e1d85d34e23d3533209f7?f=__disk__30%2Fc6%2Ff0%2F30c6f052098f41629e63c31e0f9526d9765f4258"
PUBLIC[GeoDAWN_data_extent.zip]="https://www.sciencebase.gov/catalog/file/get/657e1d85d34e23d3533209f7?f=__disk__2d%2F0e%2F73%2F2d0e73bd2517f5bcc9dfc5dd3271fe302ed66537"
PUBLIC[qfaults_v2.zip]="https://gdr.openei.org/files/1391/qfaults_ingenious_nad83conus117_2023-06-27.zip"
PUBLIC[Qfaults_GIS.zip]="https://earthquake.usgs.gov/static/lfs/nshm/qfaults/Qfaults_GIS.zip"

public_ok=0
for name in GeoDAWN_area1_outline.zip GeoDAWN_area2_outline.zip GeoDAWN_data_extent.zip qfaults_v2.zip Qfaults_GIS.zip; do
  dest="$RAW/$name"
  if [[ -s "$dest" ]]; then
    echo "already present: $dest"
    public_ok=1
    continue
  fi
  echo "GET $name"
  if curl -fL --retry 2 --max-time 60 -o "$dest" "${PUBLIC[$name]}"; then
    echo "saved: $dest ($(wc -c < "$dest") bytes)"
    public_ok=1
  else
    echo "FAILED: $name (curl exit $?)"
    rm -f "$dest"
  fi
done
echo

echo "Expected competition names from the problem description:"
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
for f in "$DATA"/*.tif "$DATA"/*.tiff "$DATA"/*.csv "$DATA"/raw/*.tif "$DATA"/raw/*.tiff "$DATA"/raw/*.csv; do
  echo "found: $f"
  found=1
done

if [[ "$found" -eq 0 ]]; then
  echo "STATUS: no competition GeoTIFF/CSV in data/ — training remains blocked."
  echo "Public-outline attempt ok=$public_ok (1 means at least one public file landed)."
  echo "After placing competition files, run: python scripts/prepare_data.py"
  exit 2
fi

echo "STATUS: some files present. Run: python scripts/prepare_data.py"
exit 0
