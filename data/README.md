# Data placement (training blocker)

Competition rasters are **not** in this repository. They require a registered DrivenData account on the GEMS Prize challenge and are behind login.

## Official download (manual review)

1. Enroll at the competition hub: [https://www.drivendata.org/competitions/306/competition-doe-gems/](https://www.drivendata.org/competitions/306/competition-doe-gems/)
2. Open the data tab: [https://www.drivendata.org/competitions/306/competition-doe-gems/data/](https://www.drivendata.org/competitions/306/competition-doe-gems/data/) (redirects to login if unauthenticated — verified 2026-09-26).
3. Place files under `data/` as expected by `scripts/prepare_data.py`.

The official problem description lists:

| File | What it is | Source |
| --- | --- | --- |
| `training_features.tif` | Multiband GeoTIFF, UTM 11N (EPSG:32611), 100 m | [Problem description — Provided features](https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#provided-features) |
| Training labels (vector + raster) | USGS Quaternary faults / INGENIOUS | [Problem description — Labels](https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#labels) |
| `1m_DEM_links.csv` | URLs for 1 m DEM tiles | Same page |
| Sample submission GeoTIFF | All-absence template | [Submission format](https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#submission-format) |

The DrivenData **reference solution** notebook uses different local names (`data/numeric_features.tif`, `data/labels.tif`) and reports **19 feature bands**, raster size **3730 × 3292**, CRS **EPSG:32611**, 100 m pixels ([notebook](https://github.com/drivendataorg/gems-prize-reference-solution/blob/main/unet-mc-cv-reference-solution.ipynb)). Treat those names as the reference-solution convention, not as a second official filename list.

## What this repo will not do

This knowledge-base agent **does not** generate, validate-for-score, or submit prediction GeoTIFFs. After data are placed, `python scripts/prepare_data.py` only inspects rasters and writes a local inventory. Submission generation stays a separate, gated process.

## Public source rasters (no DrivenData login)

These are independently published and may be used for catalogue-gap research (external-data license still applies if used in a prize submission):

- GeoDAWN magnetic/radiometric surveys — Glen & Earney, 2024, [https://doi.org/10.5066/P93LGLVQ](https://doi.org/10.5066/P93LGLVQ)
- INGENIOUS Great Basin compilation — Ayling et al., 2022, [https://doi.org/10.15121/1881483](https://doi.org/10.15121/1881483)
- USGS Quaternary Fault and Fold Database — [https://www.usgs.gov/programs/earthquake-hazards/faults](https://www.usgs.gov/programs/earthquake-hazards/faults) · citation DOI [https://doi.org/10.5066/P9BCVRCK](https://doi.org/10.5066/P9BCVRCK)
