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

## GM-7 · The premise is demonstrated, not assumed: experts confirmed model-found faults

- **Source:** Hermant et al. (2025), §6 and the Figure 9 caption — <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf>, read this session.
- **Claim (verbatim):** "New faults are also detected (Figure 9, area A), mainly by FaultSEG and later confirmed by
  experts looking at the LIDAR data." Same section: "some discrepancies > 150 m are observed with a clear offset between
  the USGS fault line and the topographic break visible on the slope data (Figure 9, area B)."
- **Location check.** Figure 9 is the Leach Hot Springs area, printed with 40°36′N and longitudes 117°36′–117°42′W;
  Figure 8 (Rye Patch, western Humboldt Range) prints 40°30′–40°33′N. Both fall inside the GeoDAWN bounding box
  (−120.0024 to −116.1415 E, 37.3641 to 40.7247 N — CG-9). "Inside the box" is **not** "inside the flight footprint";
  the footprint is irregular and that has not been tested.
- **Why it matters.** The entire project rests on one premise: that faults exist which the catalogue lacks and which a
  geologist will confirm. Hermant et al. report exactly that outcome in this region, from lidar, using a U-Net-family
  model. It also supplies a local scale for catalogue error: >150 m positional discrepancy is half the 300 m scoring
  kernel, which is the same order as Hermant's 400 m figure in CG-5.
- **Confidence:** verified for both quotations and for the coordinates as printed in the figures. The bounding-box
  containment is arithmetic on a verified box. Footprint containment is **unverified**.

## GM-8 · The confuser list is observed, not invented

- **Source:** Hermant et al. (2025), Figures 8–9 and §7, read this session.
- **Claim (verbatim):** "both siUNET and FaultSEG models detect non faulted objects described by Silver et al. (2011),
  such as the paleo-shoreline or the Rec Area scarp"; "the detection of a canyon boundary (Figure 9, area B) and stream
  boundary (Figure 9, area A) raises questions as they are aligned with USGS Quaternary faults"; and on a possible fix:
  "we know that in some cases, faults can be co-located with a paleo-shoreline … or with a canyon boundary … An approach
  to differentiate between them may therefore miss some of these co-located structures."
- **Also (verbatim, §7):** "It has been decided to take the risk of predicting too many faults, even if this means
  deleting them manually afterwards with an expert analysis, rather than missing or incorrectly mapping certain faults."
- **Why it matters.** Paleo-shorelines, canyon and stream boundaries are *measured* false positives in this terrain, and
  the authors warn that a dedicated confuser class can delete real faults because the two co-occur. That is an argument
  for soft suppression channels over hard negative classes (H11). Their deliberate over-prediction is also the right
  posture under α=0.2 / β=0.8.
- **Confidence:** verified.

## GM-9 · The rules call the 1 m DEM *feature data* — and describe GeoDAWN differently from the data release

- **Source:** rules §2 — <https://www.nlr.gov/docs/fy26osti/96647.pdf> (redirects to `docs.nlr.gov`), read this session.
- **Claim (verbatim):** "The feature data for this prize come from the recently released Geoscience Data Acquisition for
  Western Nevada (GeoDAWN) dataset, a high-resolution lidar, magnetic, and radiometric study of western Nevada and
  eastern California … In addition, the feature data also contain U.S. Geological Survey (USGS) Digital Elevation Model
  (DEM) elevation data at 1-m resolution."
- **Why it matters.** The 1 m DEM is described as **feature data**, i.e. in scope and officially provided — not external
  data requiring a licence judgement. That strengthens H3 and removes the main objection to spending on lidar.
- **Irregularity flagged, not smoothed.** The rules call GeoDAWN a "lidar, magnetic, and radiometric study"; the data
  release (Glen & Earney, 2024, <https://doi.org/10.5066/P93LGLVQ>) is titled "Airborne magnetic and radiometric
  surveys" and describes the lidar as a **separate, coordinated** 3DEP collection over "a similar extent". Two official
  DOE/USGS documents describe the same programme differently. No scoring consequence is known. Recorded so that nobody
  later cites the rules as evidence that GeoDAWN itself distributed lidar.
- **Confidence:** verified for both texts.

## GM-10 · What an expert actually looks for, in the authors' own words

- **Source:** Hermant et al. (2025) §3.3, read this session — <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf>
- **Claim (verbatim):**
  > "As the USGS Quaternary fault mapping is sometimes inaccurate at small scales or of variable precision, we created a
  > new manual mapping of faults over the eastern half of the study area using elevation and slope data, and satellite
  > imagery. The remaining half was reserved for prediction."
- **The four visual criteria they list (verbatim):**
  1. "A fault often appears as a generally straight line on the image, creating a strong visual contrast with the
     surrounding areas"
  2. "Active or recent faults can affect the topography: the areas on either side of the fault will have a different
     elevation and the fault zone itself will have a steeper slope."
  3. "Faults can affect the surrounding vegetation, creating a noticeable variation in vegetation on different parts of
     the Earth's surface."
  4. "Geological features can also be associated with the presence of faults in the area, such as areas of weathered rock
     or fractures along hillsides or mountains."
- **Also (verbatim):** "Using these criteria, we created a fault label dataset containing 1100 faults with a cumulative
  length of 264 km." And on the label raster: "a buffer value of 50 m was used, implying a thickness of the fault
  signature in the data 100 m."
- **Why it matters here.** Three things. (1) This is a published, worked statement of why a team would discard the
  catalogue as a training target and build its own — the same conclusion as H5 and H9, reached independently, in this
  region, from this data. (2) Criterion 3 (vegetation) is a modality the 19-band stack does not contain at all (PA-1);
  criterion 4 (weathered rock, hillside fractures) is what the conductivity and magnetic bands weakly proxy. (3) Criterion
  1 — a generally straight line with strong visual contrast — is the confuser generator: ditches, roads, shorelines and
  channel margins are all straight, high-contrast lines. The catalogue resolved that ambiguity with field evidence and
  put the non-tectonic ones in **Class D** (CG-14); a model cannot, which is why H11 prices confusers instead of deleting
  them.
- **Note on the quotation.** The sentence quoted above is where the shorter phrase quoted in PA-2 ("the USGS Quaternary
  fault mapping is sometimes inaccurate at small scales or of variable precision") comes from. It was read verbatim from
  §3.3 this session, so PA-2's quotation is confirmed rather than inferred.
- **Confidence:** verified — read from the PDF this session.

## Blocked-on

1. Read `1m_DEM_links.csv` — count tiles, coverage, volume.
2. Build a lidar-coverage mask and intersect with the GeoDAWN outline; test whether catalogue completeness jumps at coverage boundaries.
3. Check whether bands 12/19 match 10.5066/P9MQRCBY once resampled.
4. **Do not compute slope from non-lidar 3DEP** — Hermant et al. found it artefact-ridden. A published negative result, free to respect.
