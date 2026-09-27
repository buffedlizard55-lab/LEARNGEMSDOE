# Potential-field geophysics

Canonical HTML: [`docs/research/potential-field.html`](../docs/research/potential-field.html)

Ten of nineteen bands are potential-field or derived from them (six magnetic, four gravity). This is the only family
that responds to structure *under* cover.

## PF-1 · What GeoDAWN can resolve

- **Source:** <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and> · <https://doi.org/10.5066/P93LGLVQ>
- **Citation:** Glen, J.M.G., and Earney, T.E. (2024). CC0 1.0.
- **Claim:** 149,030 line-km over 51,857 km²; flown 1 Nov 2021 – 20 Nov 2022. Area 1 (Clayton Valley, Li-brine): rank 1 EarthMRI, 200 m flight lines, 2,000 m tie lines, 100 m clearance over low relief. Area 2 (geothermal, between rank 1 and 2): 400 m flight lines, 4,000 m tie lines, 150 m clearance. Four blocks north to south: Winnemucca, Fallon, Hawthorne, Tonopah. Magnetic processing: diurnal, aircraft-field, tie-line levelling, micro-levelling, IGRF.
- **Relevance:** Line spacing sets the shortest sampled wavelength. A "lineament" found at 100 m may be interpolation between lines 400 m apart → H7 control.
- **Confidence:** verified for acquisition numbers; the aliasing implication is **inference**.

## PF-2 · The magnetic bands

- **Source:** band `description` / `data_category` tags printed by the reference notebook; see [`docs/feature-stack.html`](../docs/feature-stack.html)
- **Claim:** 1 magnetic anomaly · 2 reduced-to-pole · 3 TMI horizontal gradient · 6 "tilt angle or total curvature — magnetic field derivative for edge detection" · 9 TMI vertical gradient · 14 TMI.
- **Relevance:** Band 6 is already an edge detector, but the tag is genuinely ambiguous about which one — check numerically. Bands 3 + 9 + 14 give gradient magnitude and analytic signal. Prefer RTP (2) for anything geometric: unreduced anomaly peaks are displaced from their sources at this latitude.
- **Confidence:** verified for band tags; the tilt-vs-curvature identification and the RTP recommendation are **inference**.

## PF-3 · Miller & Singh (1994), tilt derivative

- **Citation:** Miller, H.G., & Singh, V. (1994). Potential field tilt — a new concept for location of potential field sources. *Journal of Applied Geophysics*, 32, 213–217. <https://doi.org/10.1016/0926-9851(94)90022-1>
- **Claim:** Tilt angle = arctan(vertical derivative / horizontal gradient magnitude). Bounded, balances shallow and deep source amplitudes, zero contour sits over source edges.
- **Relevance:** Amplitude balancing is exactly what a basin-and-range setting needs, where a deep basement step under fill gives a weak broad gradient.
- **Confidence:** bibliographic record **verified**; the method summary is the standard textbook form — **the paywalled article has not been opened**. Do not quote it as the authors' own wording.

## PF-4 · Verduzco et al. (2004), THDR

- **Citation:** Verduzco, B., Fairhead, J.D., Green, C.M., & MacKenzie, C. (2004). New insights into magnetic derivatives for structural mapping. *The Leading Edge*, 23(2), 116–119. <https://doi.org/10.1190/1.1651454>
- **Claim:** Extends the tilt by taking its total horizontal derivative, giving sharper, better-localised maxima over source edges; discusses analytic-signal amplitude alongside.
- **Relevance:** The cheapest H2 experiment available — a few gradient operations on grids that already exist.
- **Confidence:** bibliographic record **verified**; article **not opened**.

## PF-5 · The gravity family

- **Sources:** band tags; <https://doi.org/10.5066/P9Z6SA1Z> (Glen et al. 2022, regional Great Basin gravity and magnetic maps); <https://gdr.openei.org/submissions/1391>
- **Claim:** 13 isostatic gravity anomaly · 5 its slope · 11 its vertical gradient · 18 its horizontal gradient. The source release is described as "generated from new and existing sources to support ongoing efforts to characterize geothermal resource potential".
- **Relevance:** Gravity is independent evidence from magnetics. A lineament in both band 18 and band 3/6 is hard to explain away.
- **Confidence:** verified for band tags and the release description. **Unverified:** that the competition's gravity bands derive from that specific release — band provenance is undocumented beyond the tags.

## PF-6 · Band 15, depth to basement

- **Claim:** "Depth to basement surface — thickness of sedimentary cover", category `subsurface`.
- **Relevance:** The stratifying variable for the whole argument. Under thick cover, a missing scarp is uninformative; over thin cover it is meaningful negative evidence. Report every H2 candidate **conditioned on band 15**.
- **Confidence:** verified for the band tag; the conditioning strategy is **inference**.

## PF-7 · Artefacts that fake structure

1. **Mosaic discontinuity** — Area 1 (200 m lines) abuts Area 2 (400 m lines).
2. **Block boundaries** — four blocks, different contractors and aircraft; levelling joins become straight "structures" once gradient-filtered.
3. **Terrain clearance** — verbatim from the USGS page: in steep terrain "the aircraft may have required deviating from the planned drape surface, and therefore **variable terrain clearance should be considered when modeling and interpreting these data**".

- **Relevance:** All three produce linear, fault-shaped features, and β=0.8 makes over-prediction cheap enough to hide the mistake. The control is public: the GeoDAWN release ships Esri shapefiles of flight paths and survey outlines.
- **Confidence:** verified for the facts and the quotation; that the artefacts appear in the derived bands is **inference**.

## PF-8 · What "rank 1" actually certifies — and what it does not

- **Sources:** GeoDAWN text naming the criteria —
  <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and> and
  <https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7>; the criteria themselves —
  Drenth, B.J., & Grauch, V.J.S. (2019), *Finding the Gaps in America's Magnetic Maps*, **Eos** (2019),
  <https://doi.org/10.1029/2019EO120449> (Table 1 verified); the criteria as re-stated by USGS for the national survey
  inventory — <https://data.usgs.gov/datacatalog/metadata/USGS.5d38aac0e4b01d82ce8b940a.xml>.
- **Claim (verbatim, GeoDAWN):** Area 1 "was flown with rank 1 specifications (following criteria outlined by Drenth and
  Grauch, 2019) that met EarthMRI survey requirements"; Area 2 used "lower resolution flight specifications …
  (falling between rank 1 and 2)".
- **What rank 1 requires (verbatim from Table 1, survey-specifications row):** "TC < 152 meters and ratio ≤ 2", where
  TC is terrain clearance and the ratio is "of flight line spacing to typical distance above shallowest magnetic sources
  in the survey area". Ranks run 1 (best) to 5 (worst), and the overall rank is the worst of three categories (data
  type, survey specifications, data issues).
- **Why it matters.** GeoDAWN Area 1 is 200 m line spacing at ~100 m clearance; rank 1 therefore certifies that the
  spacing-to-source-distance ratio is ≤ 2 — i.e. the survey is designed to image sources no shallower than about half
  the line spacing. Area 2, at 400 m spacing, is explicitly *below* that standard. Two consequences for H2:
  (a) a "buried structure" expressed only in the shallowest magnetic layer may be undersampled in Area 2 by design;
  (b) gridding to 100 m does not create information the 400 m sampling never captured — the 100 m product grid
  oversamples Area 2 in the across-strike direction. (a) is a documented specification; (b) is the standard sampling
  argument, labelled **inference**.
- **Confidence:** verified for the GeoDAWN wording, the Table 1 criteria, and the Eos DOI (title and figure/table read).
  **Unverified:** the exact byline of the Eos article (the USGS survey-inventory metadata credits the ranking to Drenth
  and Grauch, 2019; the article credits "coauthor Tien Grauch" and an image to Benjamin J. Drenth — the full author
  list was not captured). The resolution consequences are **inference**.

## PF-9 · Acquisition geometry has an azimuth, and Basin-and-Range structures do too

- **Source:** GeoDAWN text (same two URLs as PF-8).
- **Claim (verbatim):** Area 1 "Flight lines were spaced 200 m apart at an azimuth of 90 degrees, and tie lines were
  spaced 2000 m apart at an azimuth of 180 degrees." Area 2: "flight lines spaced 400 m apart at an azimuth of 90
  degrees, and tie lines spaced 4000 m apart at an azimuth of 180 degrees."
- **Why it matters.** Flight lines run **E–W (090°)** and tie lines **N–S (180°)**. Sampling is therefore anisotropic by
  a factor of 10 (200 m vs 2,000 m in Area 1; 400 m vs 4,000 m in Area 2). A N–S-trending structure is crossed every
  200–400 m; an E–W-trending one is crossed by tie lines only every 2–4 km. Basin-and-Range normal faults trend
  broadly N–NE (well sampled); Walker Lane dextral structures and many range-front splays trend NW to WNW (obliquely to
  poorly sampled). Any comparison of "how strong does a lineament look" across orientations is comparing different
  sampling densities unless this is corrected for.
- **Confidence:** verified for the azimuths and spacings. The orientation-specific sampling consequence and the regional
  trend generalisation are **inference** — the trend claim should be checked against the actual trace orientations in
  the label raster once data are placed, which is a half-hour measurement.

## PF-10 · The GeoDAWN release ships geoTIFF grids, a contractor report and flight-path shapefiles

- **Source:** <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and>
  (read in full 2026-09-26) · <https://doi.org/10.5066/P93LGLVQ> · CC0 1.0
- **Claim (verbatim, deliverables):** "Included with this publication are: PDF files of the contractor's report and readme
  file (describing the surveys, field operations, equipment, data, and processing procedures), a .csv file of the
  contractor's metadata, and compressed .zip files containing deliverable products \[consisting of binary grid (.grd),
  map (.map), and database (.gdb) files of magnetic and radiometric grids and line data …\]; and Esri shapefiles (.shp)
  and associated projection (.prj), index (.shx) and dBASE (.dbf) files of the flight paths and survey outlines. Also
  included in this report are compressed .zip files containing .csv files of flight line data for magnetic and
  radiometric surveys, a PDF of the radiometric ternary map, and **geoTIFF images of geophysical grids**."
- **Also verified verbatim from the same page:** "The GeoDAWN surveys were performed by EDCON-PRJ, Inc., under contract
  with the USGS from November 1, 2021 to November 20, 2022"; the four acquisition blocks "from north to south: Winnemucca,
  Fallon, Hawthorne, and Tonopah"; and on the drape surface, "Nominal flight heights for both surveys were based on a best
  fit, pre-planned, three-dimensional draped surface designed with a maximum 22-degree climb/descent angle".
- **Relevance.** The last clause is the important one for provenance. PF-5 and the feature-stack page both record that
  the competition never says which public release each of the 19 bands came from. The GeoDAWN release itself ships
  **geoTIFF images of the geophysical grids**, plus a contractor report and readme that describe the processing
  procedures. That gives a concrete, licence-clean (CC0 1.0) route to resolving band provenance *without* the
  competition rasters: download the public grids, resample to the 100 m EPSG:32611 grid, and compare against the 19
  bands once the training raster is placed. The radiometric channels — the one GeoDAWN product with a direct
  surface-geology signal — are in that release and are **not** in the 19-band stack (feature-stack page), which is an
  external-data opportunity under rules §3.2/GV-4 rather than a gap in the survey.
- **Confidence:** verified for the deliverables list, the acquisition dates and the drape-surface wording, all read from
  the official page this session. **Unverified:** nothing was downloaded from ScienceBase this session (TLS to that host
  fails from this sandbox), so no claim is made about the contents, resolution or nodata handling of any file inside the
  release.

## Cheapest next experiments

1. Confirm numerically what band 6 is, from bands 3, 9, 14.
2. Overlay the GeoDAWN survey-outline shapefile; test whether band-3/6 maxima cluster along Area 1/2 and block boundaries (H7).
3. Stratify every edge candidate by band 15 and report detection statistics per cover class.
4. Compute analytic-signal amplitude and THDR; test whether either adds information over band 6 alone.

## PF-11 · Horizontal-gradient and tilt derivatives: the priority list vs. what the stack already has

- **Sources:** band tags as printed by the reference notebook (feature-stack page, verified); Miller &amp; Singh (1994),
  DOI <https://doi.org/10.1016/0926-9851(94)90022-1> (bibliographic record verified, paper still unread — paywalled);
  Verduzco et al. (2004), DOI <https://doi.org/10.1190/1.1651454> (likewise qualified); 6GEMSDOE public site
  methodology note (site claim, read 2026-09-26).
- **What the research priority asks.** Derivative layers on the magnetic and gravity grids: horizontal gradient
  magnitude (HGM), tilt derivative (TDR), and by extension the analytic-signal amplitude. These are the standard
  source-edge transforms: HGM maxima sit over contrasts in susceptibility (magnetics) or density (gravity), the tilt
  angle normalises the vertical derivative by the horizontal gradient so shallow and deep edges plot at comparable
  amplitude — the forms introduced for edges by Miller &amp; Singh (1994) and popularised for display by Verduzco et
  al. (2004). The formula-level details are deliberately not reproduced here from memory; both papers are on the
  unread-source list and the definitions above are marked **inference from the citations' scope**, not from the texts.
- **What already exists, verified from the band tags.** Band 6 is tagged "Tilt angle or total curvature — magnetic
  field derivative for edge detection" and band 15 is a depth-to-basement surface; there is also a band carrying the
  "vertical slope of total magnetic intensity" (feature-stack page). So the stack already ships exactly one magnetic
  edge derivative and no gravity edge derivative — the isostatic gravity anomaly appears only raw and as its slope.
- **What the sibling field implements (site claims, not re-run here).** The 6GEMSDOE methodology note advertises
  "derived horizontal-gradient magnitude, analytic-signal amplitude, tilt derivative, multi-scale curvature,
  break-in-slope and structure-tensor lineament features" over "the 19 official GeoDAWN/USGS bands", 88 channels in
  total; GEMSDOE4 describes 63 lineament features (multi-scale Sato ridgeness, structure-tensor coherence) on the six
  bands it judged edge-bearing. Published as text on their sites; this repository holds neither build.
- **The open, score-relevant questions.**
  1. **Does derived HGM/TDR add anything over band 6?** If band 6 is the tilt derivative of TMI, then re-deriving TDR
     is redundant by construction and the marginal channel is *gravity* HGM/TDR (basement density edges under cover)
     and the analytic signal (less dependent on magnetisation direction). "Cheapest next experiments" item 4 on this
     page already anticipated this; it is unmeasured because the rasters are unplaced.
  2. **Cross-layer edge coincidence.** A magnetic edge and a gravity edge at the same line are two independent
     physical contrasts supporting one buried structure (see ST-6's agreement matrix). Confluence is the discriminator
     between a fault and a lithologic contact, and it cannot be faked by a single-band edge detector.
  3. **Acquisition orientation leakage** (PF-9): derivative operators amplify along-track noise anisotropically —
     HGM computed on an anisotropically sampled grid is not isotropic, and line-parallel artefacts survive every
     derivative. Any HGM/TDR feature list needs the H7 artefact screen applied *after* derivation, not before.
- **Confidence:** verified for the band tags' existence as printed by the notebook, the two DOIs, and the sibling
  sites' published wording. Derivative-definition characterisations are **inference** until Miller &amp; Singh and
  Verduzco et al. are read; the redundancy and confluence arguments are **inference** pending the rasters.
