# Seismotectonics and strain

Canonical HTML: [`docs/research/seismotectonics.html`](../docs/research/seismotectonics.html)

Seven bands in this family (three geodetic, two seismic, one conductivity, plus depth-to-basement shared with
potential-field). None is a fault detector. All are independent of the published fault map, which is why they can
point at places where the crust is doing something and the catalogue says nothing.

**Disciplining rule:** strain and seismicity fields are smooth and regional; faults are thin and local. Use these as
spatial priors that re-weight candidates produced elsewhere, never as a standalone probability map (H4).

## ST-1 · The three geodetic strain bands

- **Source:** band tags — **4** "Geodetic second invariant — measure of strain rate tensor magnitude", **7** "Geodetic shear rate — rate of angular deformation from GPS/InSAR", **8** "Geodetic dilatation rate — rate of volumetric strain (expansion/contraction)".
- **Relevance:** The only provided bands measuring present-day deformation directly. Deformation does not require a published scarp. Dilatation (8) is the extensional signal, relevant to permeability as well as structure.
- **Confidence:** verified for band tags. **Unverified:** the underlying velocity field, station density, smoothing and reference frame are undocumented in the competition materials.

## ST-2 · The two seismic bands are parameterised and not independent

- **Source:** band tags — **10** "Distance to earthquake (n=100km radius, a=15° azimuth parameters)", **16** "Earthquake intensity or density (n=100km radius, a=15° parameters)".
- **Relevance:** Same catalogue, same parameters — counting them as two confirmations is double counting. And a 100 km smoothing radius cannot localise a fault to within the 300 m scoring kernel.
- **Confidence:** verified for the tags; the non-independence and over-smoothing conclusions are **inference**.

## ST-3 · Strain rate versus earthquake rate

- **Source:** <https://doi.org/10.1785/0220220153>
- **Citation:** Kreemer, C., & Young, Z.M. (2022). *Crustal Strain Rates in the Western United States and Their Relationship with Earthquake Rates.* Seismological Research Letters, 93(6), November 2022. First author: Nevada Bureau of Mines and Geology and Seismological Laboratory, University of Nevada, Reno. Author list confirmed from the [INGENIOUS project page](https://gbcge.org/current-projects/ingenious/).
- **Relevance:** The correlation is imperfect, and the imperfection is informative. Where strain and seismicity agree, two independent lines of evidence favour an unmapped structure. Where they disagree — high strain, low seismicity — possible aseismic creep, a short window, or strain distributed across structures too small or slow to appear in either record. The last case is the gap. Kreemer is a co-author on the INGENIOUS compilation supplying the training labels.
- **Confidence:** publisher record **verified** (title, journal, volume, date, DOI, affiliation); author list confirmed by the INGENIOUS project page. **Unverified:** the abstract body has not been read, so no quantitative claim from the paper is reproduced. The lineage suggestion is **inference**.

## ST-4 · Native geodetic and seismic products

- **Source:** <https://gdr.openei.org/submissions/1391>, CC BY 4.0
- **Claim:** *Geodetic Shear and Dilation Models* (51.99 MB) — "GeoTIFFs and accompanying ASCII, .csv, and metadata … developed at the Nevada Geodetic Labo[ratory]". *Earthquake Density Models* (22.98 MB) — "… describe **independent and dependent** earthquake density … developed at the Nevada Geo[dettic Laboratory]".
- **Relevance:** The archives ship metadata, so the smoothing and network become knowable. The earthquake release distinguishes declustered ("independent") from raw ("dependent") density — the declustered field is the right one for locating structures rather than aftershock clouds.
- **Confidence:** verified for the descriptions. **Unverified:** archives not downloaded; nothing asserted about internal files.

## ST-5 · Conductivity

- **Source:** band **17** "Conductivity surface — electrical conductivity of subsurface"; <https://doi.org/10.5066/P9TWT2LU>
- **Citation:** Peacock, J.R., & Bedrosian, P.A. (2022). Electrical conductance maps estimated from a 3D model of the Great Basin, USA, at **five depth ranges spanning 2 to 200 km**.
- **Relevance:** Sensitive to fluids, clays and alteration along structures — but equally to basin fill, salinity and geothermal outflow. Used as a primary detector it lights up exactly the flat, sedimentary areas Hermant et al. warn about. The depth slicing is the improvement worth having: a conductor at 2 km means something different from one at 50 km.
- **Confidence:** verified for the band tag and release description. **Unverified:** that band 17 derives from that release.

## ST-6 · Slip and dilation tendency

- **Source:** <https://doi.org/10.5066/P9YL58W6>, listed in GDR 1391
- **Citation:** Siler, D.L. (2022). *Shapefile for slip tendency and dilation tendency calculated for Quaternary faults in the Great Basin.* USGS data release.
- **Claim:** "results of slip tendency and dilation tendency analysis of Quaternary faults in the Great Basin region".
- **Relevance:** Computed **for known faults**, so it cannot discover. Its value is as a plausibility filter on candidates: is a proposed strand oriented such that the regional stress field would activate it? That is a geological argument a Phase 2 reviewer can engage with.
- **Confidence:** verified for the description. **Unverified:** not downloaded; no field-level claim.

## ST-7 · A native strain-rate-tensor source for the geodetic bands (citation located; paper not read)

- **Source of the citation:** Hermant et al. (2025) reference list, read this session —
  <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf>.
- **Citation as printed there:** Kreemer, C., Blewitt, G., Hammond, W.C., Oldow, J., & Cashman, P. (2009). *Geodetic
  constraints on contemporary deformation in the northern Walker Lane: 2. Velocity and strain rate tensor analysis.*
  In: Late Cenozoic Structure and Evolution of the Great Basin–Sierra Nevada Transition, **GSA Special Paper 447**,
  17–31. No DOI is printed in that reference list and none is asserted here.
- **Why it matters.** Bands 4, 7 and 8 are strain-rate quantities whose provenance the competition never documents. If
  they derive from a Walker Lane velocity/strain-rate tensor analysis, then the station density, smoothing and reference
  frame behind them are knowable — and the northern Walker Lane sits inside the GeoDAWN bounding box (CG-9). Kreemer is
  also a co-author of the INGENIOUS compilation that supplies the labels (ST-3), so the same group's products appear on
  both sides of the model.
- **Confidence:** the citation is **verified as printed** in a read source. The paper itself has **not been read**; no
  claim from it is reproduced. The suggestion that it underlies the competition's geodetic bands is **unverified
  inference** — it is a place to look, not a finding.

## Agreement / disagreement matrix (working tool, not a sourced claim)

| Signal combination | Reading | Action |
| --- | --- | --- |
| Strain high + seismicity high + no catalogue fault | Active deformation, silent catalogue | Prioritise for H1/H3 inspection |
| Strain high + seismicity low | Aseismic, or short catalogue window | Lower priority; note in Phase 2 narrative |
| Strain low + seismicity high | Localised release below geodetic resolution, or an aftershock cluster | Check clustering; use declustered density |
| Magnetic edge + gravity edge + thick cover | Two independent physical contrasts under cover | H2 candidate, report conditioned on cover |
| Edge + no gravity counterpart + thin cover | Probably lithology | Demote |
| Edge parallel to a survey or block boundary | Acquisition artefact until proven otherwise | Reject (H7) |
| Conductivity high + no structural evidence | Basin fill, salinity, outflow | Do not promote (H6) |

## First measurements

1. Quantile-bin bands 4, 7, 8, 10, 16; distance-to-nearest-label per bin. No monotonic decrease → H4 is dead as stated.
2. Check correlation between bands 10 and 16; if high, use one.
3. Overlay the declustered grid from <https://gdr.openei.org/files/1391/seismicity_INGENIOUS_regional_data.zip> on band 16.
4. Build the matrix as a raster stack; measure label density per cell on a spatial holdout.
