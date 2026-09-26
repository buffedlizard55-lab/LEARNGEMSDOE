# DEM structural geomorphology

Canonical HTML: [`docs/research/geomorphology.html`](../docs/research/geomorphology.html)

Two of nineteen bands are topographic, both derived from a 100 m detrended surface. The scarps an expert would map
are 1–10 m features — an order of magnitude finer than the only topographic layers provided.

## GM-1 · What the two 100 m bands can see

- **Source:** band tags — **12** "Detrended elevation — topography with regional trends removed", **19** "Detrended elevation slope — gradient of elevation after detrending".
- **Relevance:** Detrending is right for scarp work, but a 100 m pixel averages 10,000 m² of ground; a 2 m scarp 20 m wide is diluted roughly fifty-fold. Bands 12/19 resolve range fronts and large piedmont lineaments and miss small recent scarps.
- **Confidence:** verified for band tags; the dilution reasoning is **inference**.

## GM-2 · The 1 m DEM is official, provided as links

- **Sources:** <https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#provided-features> · rules §3.3 <https://www.nlr.gov/docs/fy26osti/96647.pdf> · About page <https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/>
- **Claim (verbatim):** "you will find a CSV file called `1m_DEM_links.csv` that contains links where DEM data at 1m resolution can be downloaded." Rules §3.3: "instructions will be provided for downloading USGS DEM elevation data at 1-m resolution for the GeoDAWN region". About page: airborne lidar collected through USGS 3DEP "over a similar extent spanned by the geophysical surveys".
- **Relevance:** Sanctioned, not external — no licence question. But it is a CSV of *links*, and lidar covers an extent "similar to" rather than identical to the geophysical surveys, so coverage is itself a spatial variable.
- **Confidence:** verified.

## GM-3 · Hermant et al. (2025) scarp protocol — worked, in this region

- **Source:** <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf>
- **Verified numbers read from the PDF:**
  - 3DEP **1/3 arc-second** (~10 m N–S; E–W varies with meridian convergence); chosen as the highest-resolution seamless DEM with full CONUS coverage and lighter than 1 m.
  - "**Clean slope raster data can only be calculated where elevation data is derived from LIDAR data.**" They used the 1/3 arc-second DEM *only where lidar-derived*, in northern central Nevada.
  - Own manual labels: **1,100 faults, 264 km cumulative**, eastern half of the study area; western half reserved for prediction.
  - **50 m buffer** → 100 m fault signature. 7,692 tiles retained after filtering; split 64/16/20 → 4,920 / 1,232 / 1,540; augmented to 20,000 / 4,000 / 4,000.
  - Tiles **128 × 128 px at 10 m = 1,280 m**.
  - Fault pixels **6.5%** after buffering. Focal Binary Cross Entropy, **α = 0.065**, **γ = 2.0**.
  - Sentinel-2 **B8A** (20 m → 10 m, 865 nm, 20 nm bandwidth) for vegetation/biomass: "in areas of very flat topography where faults are not necessarily highlighted by elevation data but sometimes by vegetation orientation".
  - Caveat: in flat areas (basin centre, playa) their processing vertically exaggerates relief — "Prediction results in flat areas should therefore be treated with caution."
- **Relevance:** Lidar provenance gates slope quality (hard constraint on H3). 1,100 faults / 264 km is a realistic prior for how much new fault length a manual expert pass adds here. 6.5% positives at 10 m implies far worse imbalance at 100 m. No optical/vegetation band exists in the 19-band stack — a genuine external-data opportunity.
- **Confidence:** verified.

## GM-4 · Geomorphic expression is admissible evidence

- **Sources:** <https://pubs.usgs.gov/of/1993/0338/report.pdf>; About page 968
- **Claim (verbatim, OF 93-338):** structures with pre-Quaternary movement "will not be shown unless there is compelling evidence of Quaternary movement (**geomorphology, offset surficial deposits, etc.**)". About page: field searches for "surface expressions such as fault scarps, offset rock layers, and polished slickensides"; remote sensing reveals "linear features and subtle ground movements indicative of fault activity".
- **Relevance:** Geomorphology is a valid route in — but only once a human has published the interpretation. A lidar-visible scarp with no publication is gap class 2 (CG-7), the target of H3.
- **Confidence:** verified.

## GM-5 · The native detrended-elevation release

- **Source:** <https://doi.org/10.5066/P9MQRCBY>, listed in <https://gdr.openei.org/submissions/1391>
- **Claim:** "Provided are maps of elevation trend and detrended elevation for the Great Basin, USA. The detrended elevation map … emphasizes local relative topogra[phy]."
- **Relevance:** If bands 12/19 were resampled from this, the detrending method and native resolution become knowable — and detrending wavelength determines which scarp heights survive.
- **Confidence:** verified for the release and description. **Unverified:** that the competition bands derive from it.

## GM-6 · What a subtle scarp looks like here (operational picture)

**Inference, assembled from GM-1…GM-5.** A low-offset, basin-facing scarp on a piedmont or playa margin: a few metres
of relief over tens of metres width, continuous for hundreds of metres to a few km along strike, often dissected by
alluvial channels, sometimes expressed only as a vegetation or tonal line.

- At **1 m lidar**: break-in-slope / curvature maximum traceable along strike, possibly with a tonal line.
- At **10 m 3DEP**: visible only if lidar-derived; otherwise artefacts.
- At **100 m**: invisible individually; a persistent along-strike run of slightly elevated slope may still register. Detection must be directional and multi-pixel.

Named confusers: irrigation and drainage ditches, pluvial shorelines and wave-cut benches, alluvial-fan channel
margins, lithologic benches, road and fence lines, playa edges.

## Blocked-on

1. Read `1m_DEM_links.csv` — count tiles, coverage, volume.
2. Build a lidar-coverage mask and intersect with the GeoDAWN outline; test whether catalogue completeness jumps at coverage boundaries.
3. Check whether bands 12/19 match 10.5066/P9MQRCBY once resampled.
4. **Do not compute slope from non-lidar 3DEP** — Hermant et al. found it artefact-ridden. A published negative result, free to respect.
