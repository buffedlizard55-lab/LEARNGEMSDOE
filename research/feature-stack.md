# Feature stack

Canonical HTML: [`docs/feature-stack.html`](../docs/feature-stack.html)

**Provenance caveat stated up front.** Band names and data categories below are the `description` and `data_category`
tags read out of `training_features.tif` by the official
[reference-solution notebook](https://github.com/drivendataorg/gems-prize-reference-solution/blob/main/unet-mc-cv-reference-solution.ipynb).
The competition pages do **not** state which public release each band came from, what processing was applied, at what
native resolution, or how nodata was propagated. Anything beyond the band tag is labelled inference.

## Raster geometry (from the reference notebook output)

| Property | Features | Labels |
| --- | --- | --- |
| Width | 3292 | 3292 |
| Height | 3730 | 3730 |
| CRS | EPSG:32611 | EPSG:32611 |
| Resolution | 100.0 × 100.0 m | 100.0 × 100.0 m |
| Data type | float32 | int32 |
| nodata | −3.4028234663852886e+38 | −1.0 |
| Bands | 19 | 1 |

The "19 bands" printed for the *label* file is a display bug, not a real band count —
[staff confirmation, forum 11529](https://community.drivendata.org/t/why-does-the-training-fault-labels-file-in-the-data-tab-have-a-single-band-while-the-labels-in-the-reference-solution-repo-have-19-bands/11529).

## The 19 bands

| # | Official description | Category |
| --- | --- | --- |
| 1 | Magnetic anomaly — deviation from expected Earth's magnetic field | magnetic_data |
| 2 | Reduced to pole magnetic data — magnetic anomaly corrected for latitude effects | magnetic_data |
| 3 | Total magnetic intensity horizontal gradient | magnetic_data |
| 4 | Geodetic second invariant — measure of strain rate tensor magnitude | geodetic_strain |
| 5 | Isostatic gravity anomaly slope | gravity_data |
| 6 | Tilt angle or total curvature — magnetic field derivative for edge detection | magnetic_data |
| 7 | Geodetic shear rate — rate of angular deformation from GPS/InSAR | geodetic_strain |
| 8 | Geodetic dilatation rate — rate of volumetric strain | geodetic_strain |
| 9 | Total magnetic intensity vertical gradient | magnetic_data |
| 10 | Distance to earthquake (n=100km radius, a=15° azimuth parameters) | seismic |
| 11 | Isostatic gravity anomaly vertical gradient | gravity_data |
| 12 | Detrended elevation — topography with regional trends removed | topographic |
| 13 | Isostatic gravity anomaly | gravity_data |
| 14 | Total magnetic intensity | magnetic_data |
| 15 | Depth to basement surface — thickness of sedimentary cover | subsurface |
| 16 | Earthquake intensity or density (n=100km radius, a=15° parameters) | seismic |
| 17 | Conductivity surface — electrical conductivity of subsurface | subsurface |
| 18 | Isostatic gravity anomaly horizontal gradient | gravity_data |
| 19 | Detrended elevation slope | topographic |

**By family:** magnetic 1, 2, 3, 6, 9, 14 · gravity 5, 11, 13, 18 · geodetic strain 4, 7, 8 · topographic 12, 19 ·
seismic 10, 16 · subsurface 15, 17.

Only two of nineteen bands are topographic, and both derive from a 100 m detrended surface.

## GeoDAWN acquisition (USGS data page, CC0 1.0)

|  | Area 1 | Area 2 |
| --- | --- | --- |
| Purpose | Clayton Valley — Li-clay and brine | Remainder — geothermal |
| Flight-line spacing | 200 m | 400 m |
| Tie-line spacing | 2,000 m | 4,000 m |
| Line / tie azimuth | 90° / 180° | 90° / 180° |
| Nominal clearance | 100 m low relief / 150 m mountainous | 150 m low relief / 200 m mountainous |
| Rank | Rank 1 (EarthMRI) | Between rank 1 and 2 |

- Total: **149,030 line-km** over **51,857 km²**; flown 1 Nov 2021 – 20 Nov 2022 by EDCON-PRJ under USGS contract.
- Tonopah block (Area 1 + southern Area 2) by Precision GeoSurveys, Bell Jet Ranger; remainder by Cloudstreet Flying
  Service, Cessna 180 and Turbo 206.
- Four blocks north to south: **Winnemucca, Fallon, Hawthorne, Tonopah**.
- Magnetic processing: diurnal, aircraft-field, tie-line levelling, micro-levelling, IGRF removal.
- Deliverables include **Esri shapefiles of flight paths and survey outlines** — what H7 needs.
- Licence **CC0 1.0**, so no external-data licence obstacle.

Sources: <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and> ·
<https://doi.org/10.5066/P93LGLVQ> · <https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7>

### Derived observation: the prediction grid is larger than the survey area

3292 × 3730 px at 100 m = 329.2 km × 373.0 km ≈ **122,800 km²** of bounding box, versus **51,857 km²** surveyed —
roughly 2.4×. **Inference.** Both inputs are verified; no one has measured how much of the grid lies inside the
footprint. If it holds, much of the scoring grid is served by regional geophysics rather than GeoDAWN. Check first:
overlay the survey-outline shapefile on the raster bounds.

## What is not in the stack (absence-of-evidence argument — **inference**, re-check against the file)

| Layer | Public source | Licence |
| --- | --- | --- |
| Radiometric (K/eU/eTh, total count) | <https://doi.org/10.5066/P93LGLVQ> | CC0 1.0 |
| 1 m lidar DEM (3DEP) | `1m_DEM_links.csv` on the data tab | USGS public domain |
| Heat flow | <https://doi.org/10.5066/P9BZPVUC> | USGS |
| MT conductance, 5 depth ranges 2–200 km | <https://doi.org/10.5066/P9TWT2LU> | USGS |
| Slip and dilation tendency | <https://doi.org/10.5066/P9YL58W6> | USGS |
| Paleogeothermal features (sinter, tufa) | <https://gdr.openei.org/submissions/1391> | CC BY 4.0 |
| 2 m temperature probes | <https://gdr.openei.org/submissions/1391> | CC BY 4.0 |
| Elevation trend / detrended elevation (native) | <https://doi.org/10.5066/P9MQRCBY> | USGS |

External data are allowed provided the licence permits use in the challenge **and** sharing with the sponsor
([problem description](https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#external-datasets);
staff reaffirmation in [forum 11528](https://community.drivendata.org/t/paid-for-external-data-license/11528)).
Both licences above satisfy that.

## Known processing pitfalls

- **Nodata sentinel:** features use −3.4028234663852886e+38; the reference notebook masks anything below −1e38 to NaN
  before normalising. Any local preprocessing must do the same.
- **Per-band min-max normalisation** is applied across the whole raster over non-NaN values, and is outlier-sensitive.
- **The label raster is int32 with nodata −1.0** — treat −1 as nodata, not background.
- **Resampled provenance is undocumented.** Gradients computed on an already-resampled grid inherit its smoothing;
  the GeoDAWN line spacing is the lower bound on resolvable wavelength in the magnetic bands.
- **Bands 10 and 16 share parameters** (n=100 km, a=15°), so they are not independent evidence.

## Reproduce the inventory

```bash
bash scripts/download_competition_data.sh   # on an enrolled machine, into data/
python scripts/prepare_data.py              # writes data/inventory.json — inspection only
```

Compare `data/inventory.json` against this page after data placement. If they disagree, this page is wrong and should be
corrected.
