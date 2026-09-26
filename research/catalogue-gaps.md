# Catalogue-gap reasoning

Canonical HTML: [`docs/research/catalogue-gaps.html`](../docs/research/catalogue-gaps.html)

Highest-leverage domain. The scored target is "what the catalogue does not contain", so the catalogues' own
methodology is the most valuable document in the project: if you know how a fault had to be evidenced to get into
the database, you know which faults were structurally incapable of getting in.

## CG-1 · The database is defined by surface rupture

- **Source:** <https://www.usgs.gov/programs/earthquake-hazards/faults>
- **Citation:** U.S. Geological Survey, 2020, Quaternary Fault and Fold Database for the Nation, <https://doi.org/10.5066/P9BCVRCK>
- **Claim (verbatim):** "This database contains information on faults and associated folds in the United States that demonstrate geological evidence of **coseismic surface deformation** in large earthquakes during the past 1.6 million years (Ma)." The 1.6 Ma cutoff is inherited from the 1983 Geologic Time Scale in use when the database was established in 1993.
- **Relevance:** A buried structure with no demonstrable surface deformation is out of scope by construction, not merely unmapped. Combined with the About page — "many are hidden below the surface, requiring geophysical data to detect" (<https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/>) — this is the strongest argument for H2.
- **Corroboration (2026-09-26):** USGS FAQ, https://www.usgs.gov/faqs/what-a-quaternary-fault — "A Quaternary fault is one that has been recognized at the surface and that has moved in the past 1,600,000 years (1.6 million years)."
- **Confidence:** verified.

## CG-2 · 1993 compilation rules

- **Source:** <https://pubs.usgs.gov/of/1993/0338/report.pdf> — Haller, Machette & Dart, USGS OF 93-338
- **Claim (verbatim):** compilers were told to "give preference to (1) fault-related topical studies over general studies …, (2) more recent studies, and (3) more detailed scale of work (i.e., 1:24,000-scale over 1:250,000-scale mapping)". And: "suspected or inferred Quaternary faults (and folds) will be shown as dotted Quaternary structures (age category 5), whereas structures with known late Tertiary (or older) movement will not be shown unless there is compelling evidence of Quaternary movement (geomorphology, offset surficial deposits, etc.)". The compiler "is forced to select a slip rate and age even when no data may exist". Segmentation requires study "in a paleoseismologic sense (trenching and dating)".
- **Relevance:** Three exclusion mechanisms: evidence must be published; inferred structures are down-weighted or dropped; scale heterogeneity is baked in.
- **Confidence:** verified — quotations read from the PDF.

## CG-3 · Reduced maintenance since 2017

- **Source:** <https://www.usgs.gov/programs/earthquake-hazards/faults>
- **Claim (verbatim):** "effective January 12, 2017, the USGS will maintain a limited number of metadata fields … Archived reports are accessible from the abbreviated record." Also: as of **26 February 2026** the Database Search function is retired; legacy reports are reachable through the interactive fault map <https://doi.org/10.5066/F7S75FJM>. GIS: <https://earthquake.usgs.gov/static/lfs/nshm/qfaults/Qfaults_GIS.zip> (16 MB).
- **Relevance:** Maintenance capacity is deliberately reduced, consistent with completeness tracking publication history rather than geology. Also a time-sensitive note for anyone pulling per-fault metadata.
- **Confidence:** verified.

## CG-4 · INGENIOUS Qfaults: an attribute update, not a new mapping

- **Source:** <https://gdr.openei.org/submissions/1391> · DOI <https://doi.org/10.15121/1881483> · CC BY 4.0
- **Citation:** Ayling, B., Faulds, J., Morales Rivera, A., Koehler, R., Kreemer, C., Mlawsky, E., Coolbaugh, M., Micander, R., dePolo, C., Kraal, K., Wagoner, N., Siler, D., DeAngelo, J., Glen, J., Peacock, J., Batir, J., Gentry, E., Berti, C., Lifton, Z., Clark, A., Kirby, S., Hardwick, C., and Kleber, E. (2022).
- **Claim:** Qfaults **v1** = "updated quaternary fault traces, ages, and slip rates … Attributes conform to USGS Qfault Database s[tandards]". Qfaults **v2** "contains an updated version … and text document with field definitions. It supersedes [v1]". Whole compilation: 9 files, 116.98 MB.
- **Relevance:** These are the training labels the scorer masks out (rules §3.3). It is an attribute update, so it inherits USGS inclusion criteria rather than fixing them. v2 supersedes v1 — check versions.
- **Corroboration from the project's own team:** Hart-Wagoner, Coolbaugh, Faulds & Mlawsky (GBCGE / NBMG, University of Nevada, Reno), <https://publications.mygeoenergynow.org/grc/1034813.pdf>: "A Quaternary fault database for the INGENIOUS GBR was collated in Phase I of the INGENIOUS project and included **updated fault locations** and updated fault attributes of **recency** (i.e., age of most recent rupture) and **slip rates**." Independent, project-internal confirmation that the compilation updated locations and attributes rather than re-mapping from new evidence.
- **Project context** (<https://gbcge.org/current-projects/ingenious/>): PI Bridget Ayling, Co-PI James Faulds; 1 Feb 2021 – 30 Jun 2025; $10,000,000; DOE GTO award DE-EE0009254.
- **Confidence:** verified for the GDR descriptions, the Hart-Wagoner abstract (read) and the project page (read). **Unverified** — the field-definition document inside the v2 archive has not been unpacked.

## CG-5 · Measured heterogeneity, up to 400 m misfit

- **Source:** <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf> (cited by the competition About page)
- **Citation:** Hermant, B., Kiersnowski, L., & Bellanger, M. (2025). Proc. 50th Workshop on Geothermal Reservoir Engineering, Stanford.
- **Claim (figure 2 caption):** "Local discrepancy observed in North Central Nevada: distance between USGS Quaternary faults and TLS fault label can be up to 400 m." Heterogeneity attributed to "the aggregation of different mapping sources or scales in this database".
- **Relevance:** 400 m > the 300 m metric kernel. This is the quantitative core of H1, and a warning that "stay near the known line" is not a safe prior.
- **Confidence:** verified. Measured in north-central Nevada — regional, not area-specific.

## CG-6 · Who labelled the new faults, and what they will say

- **Sources:** rules §2 <https://www.nlr.gov/docs/fy26osti/96647.pdf>; forum 11527 post 7 <https://community.drivendata.org/t/how-were-the-new-test-faults-identified-data-sources-and-fault-types/11527/7>
- **Claim (verbatim, rules §2):** "The labels for this prize come from the USGS Quaternary Fault and Fold Database and from a set of newly identified faults labeled by geology experts at the National Laboratory of the Rockies (NLR) and USGS."
- **Claim (verbatim, staff):** "We're not sharing details about the data sources, fault types, or coverage behind the test faults beyond what's in the problem description."
- **Relevance:** We know the institutions, not the protocol. The Phase 2 redirection is an official hint about where value sits.
- **Confidence:** verified for both quotations. Any inference from the labellers' identity is **unverified**.

## CG-7 · The four gap classes (derived)

**Inference — reasoning, not sourced fact.** Written to be argued with.

1. **Corrections to known traces** — tip extensions, splays, parallel strands, positional errors up to ~400 m. Staff-confirmed to count.
2. **Post-compilation visibility** — scarps mappable only with 3DEP/GeoDAWN-era elevation, i.e. after the topical literature compilers were told to prefer.
3. **Cover-masked structures** — outside the QFFD definition entirely (CG-1).
4. **Low-publication terrain** — no topical detailed-scale study ever published, so nothing for a compiler to prefer.

Mapping to signals: classes 1–2 → topography (bands 12, 19, 1 m lidar); class 3 → gravity/magnetics under thick cover (5, 11, 13, 15, 18); class 4 → independent evidence (4, 7, 8, 10, 16, 17).

## Falsification tests

- If private labels are dominated by long, obvious, unmapped range fronts, the corrections/subtle-scarps framing is wrong.
- If distance-to-known-fault is a *positive* predictor of new labels, the gap is diffuse and H1 should be demoted.
- If the INGENIOUS v2 field definitions carry provenance or mapping-scale attributes, class 4 becomes measurable.

## CG-8 · Constraint codes counted on the live service (2026-09-26)

- **Source:** <https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0?f=pjson>
- **Citation:** same DOI as CG-4, service updated 2023-06-27. Counts and query links: [`docs/requirements.html`](../docs/requirements.html#catalogue).
- **Claim:** 22,956 polylines. `FTYPE_` partitions into Well Constrained 12,048 / Moderately Constrained 5,054 / Inferred 5,280 / Poor 100 / Other 27 / blank 447. `MAPSCALE` partitions into the codes on the requirements page, including 4,059 blank and 12 literal `1:10,000`.
- **Relevance:** this is the measurement CG-7 class 4 was waiting for, at regional scale. It is not the GeoDAWN label raster. Do not predict Inferred traces; they are already in the compilation the scorer masks.
- **Confidence:** verified for the counts. Unverified for what the short `MAPSCALE` codes mean. The zip's field-definition text is still unread (TLS).

## CG-9 · The GeoDAWN-box catalogue census, measured (2026-09-26)

> **Superseded for footprint questions by CG-12** (413 traces inside the actual data extent). Kept for provenance.

This is the clip CG-8 was waiting for, done against the published bounding box rather than the outline polygon.

- **Extent source (primary):** <https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7?format=json&fields=spatial>
  → `"boundingBox":{"minX":-120.0024,"maxX":-116.1415,"minY":37.3641,"maxY":40.7247}` (WGS 84).
- **Fault source:** NBMG `Qfaults [INGENIOUS 6-27-2023]` layer 0 — the INGENIOUS compilation cited by rules §3.3,
  DOI <https://doi.org/10.15121/1881483>.
- **Measured — every number below is one re-runnable query:**

| What | Count in the GeoDAWN box | Query |
| --- | --- | --- |
| All traces | **1,179** | [count](https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0/query?where=1%3D1&geometry=-120.0024%2C37.3641%2C-116.1415%2C40.7247&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json) |
| `FTYPE_` Well Constrained | **739** | [count](https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0/query?where=FTYPE_%3D%27Well%20Constrained%27&geometry=-120.0024%2C37.3641%2C-116.1415%2C40.7247&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json) |
| `FTYPE_` Moderately Constrained | **351** | [count](https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0/query?where=FTYPE_%3D%27Moderately%20Constrained%27&geometry=-120.0024%2C37.3641%2C-116.1415%2C40.7247&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json) |
| `FTYPE_` Inferred | **89** | [count](https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0/query?where=FTYPE_%3D%27Inferred%27&geometry=-120.0024%2C37.3641%2C-116.1415%2C40.7247&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json) |
| Any other `FTYPE_` (Poor / Other / blank) | **0** | [count](https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0/query?where=FTYPE_%20NOT%20IN%20%28%27Well%20Constrained%27%2C%27Moderately%20Constrained%27%2C%27Inferred%27%29&geometry=-120.0024%2C37.3641%2C-116.1415%2C40.7247&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json) |
| `MAPSCALE` blank or null | **0** | [count](https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0/query?where=MAPSCALE%3D%27%27&geometry=-120.0024%2C37.3641%2C-116.1415%2C40.7247&geometryType=esriGeometryEnvelope&inSR=4326&spatialRel=esriSpatialRelIntersects&returnCountOnly=true&f=json) |

739 + 351 + 89 = 1,179 exactly, and the `NOT IN` query independently returns 0, so the partition closes.

- **Why it matters.** Two readings, both relevant to the scored target:
  1. The GeoDAWN box holds **1,179 of 22,956** traces — **5.1%** of the regional compilation. Whatever the label raster
     contains, it is a small, spatially concentrated sample.
  2. The *quality mix* inside the box is better than the regional mix: **Inferred is 89/1,179 = 7.5%** here versus
     5,280/22,956 = **23.0%** regionally (CG-8). Read plainly: the GeoDAWN area is comparatively *well* mapped. If that
     holds inside the actual footprint, the remaining gaps are less likely to be obvious unmapped range fronts and more
     likely to be subtle, cover-masked, or outside the range-front template — which is the CG-7 class 2/3 argument, not
     class 4. **Inference** from two verified counts; the footprint clip is still pending.
- **Three caveats, stated before anyone quotes these numbers.**
  1. The envelope is a **rectangle**, not the flight footprint. The footprint is irregular and covers 51,857 km² inside a
     grid bounding box of roughly 122,800 km² (see the feature-stack page). Envelope counts are an **upper bound**:
     counted traces may lie outside the flown area.
  2. This is the **NBMG service snapshot dated 2023-06-27**, not the rasterised labels on the data tab. The two may
     differ.
  3. The service reports `supportsStatistics: false`, so `groupByFieldsForStatistics` / `outStatistics` return
     HTTP 400 — every class had to be counted with its own `where` clause. Total trace *length* could not be summed for
     the same reason; no length figure is asserted anywhere on this site.
- **Confidence:** <span>verified</span> for the bounding box, the query results and the closure arithmetic. **Inference**
  for the "comparatively well mapped" reading and for anything about the footprint interior.

## CG-12 · The GeoDAWN *footprint* census, measured from the public files (2026-09-26)

Closes the open item from CG-9: the clip is now against the published outline polygons, not the bounding box.

- **How it was run.** The Arena sandbox cannot complete TLS to sciencebase.gov / gdr.openei.org, so the public files
  were fetched on a GitHub Actions runner in *this* repository (no new account, no secrets, no DrivenData login):
  workflow [`public-data.yml`](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/blob/main/.github/workflows/public-data.yml), script [`public_census.py`](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/blob/main/scripts/public_census.py), run [36276586563](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/actions/runs/36276586563). Results were read back
  as run annotations. No competition raster was touched; no prediction was produced.
- **Inputs (primary):** `GeoDAWN_area1_outline.zip`, `GeoDAWN_area2_outline.zip`, `GeoDAWN_data_extent.zip` from
  ScienceBase item [657e1d85d34e23d3533209f7](https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7) (Glen & Earney 2024, <https://doi.org/10.5066/P93LGLVQ>);
  `qfaults_ingenious_nad83conus117_2023-06-27.zip` from [GDR 1391](https://gdr.openei.org/submissions/1391) (Ayling et al. 2022,
  <https://doi.org/10.15121/1881483>).
- **File checks (measured on the runner):**

| File | Bytes | Matches listing? | SHA-256 |
| --- | --- | --- | --- |
| GeoDAWN_area1_outline.zip | 1,190 | yes (ScienceBase 1,190) | `6a63cccdd7ebe51bc009eca5cc7ac83c959bf4876385813e73cebe442f850131` |
| GeoDAWN_area2_outline.zip | 1,497 | yes (ScienceBase 1,497) | `20916d6c2f74039254dc8d134cb79d380aee5ab66e5de89209ab4a8f4e0d2c27` |
| GeoDAWN_data_extent.zip | 2,774 | yes (ScienceBase 2,774) | `a27b484332fd1b75345cc63a0fa5353861db5812c5c846a494c566938c0c2ddb` |
| qfaults_v2.zip | 6,131,182 | yes (= 5.85 MiB, GDR page "5.85 MB") | `c7b091c9ac8bca140ad89ee6bb2bd63dd3ac12e3013acbfd8373d11c9faee59d` |

  The outlines are EPSG:32611; the faults are `NAD_1983_Contiguous_USA_Albers_117`
  (an equal-area projection, metres), so the area figures below are valid areas.
- **Independent cross-checks (all pass):**
  1. The GDR zip holds **22,956** records — exactly CG-8's count from the NBMG MapServer. Two distribution channels, one
     dataset.
  2. Computed extent-polygon area **51,678.8 km²** vs the shapefile's own `SqKm` attribute **51,695.2 km²** (0.03% apart).
  3. Computed Area 1 area **2,413.4 km²** vs its `ENCLOSED_A` attribute **"2411.7 sq km"**.
- **Measured (traces intersecting each polygon):**

| Polygon | Traces | Well / Moderately / Inferred | Clipped length | Inferred length | `MAPSCALE` codes |
| --- | --- | --- | --- | --- | --- |
| Data extent | **413** | 276 / 129 / 8 | 6,230.2 km | 51.0 km (0.8%) | `250`: 393 · `100`: 20 |
| Area 2 | 405 | 271 / 127 / 7 | 5,974.1 km | 46.7 km | `250`: 385 · `100`: 20 |
| Area 1 (Clayton Valley) | 19 | 12 / 6 / 1 | 311.6 km | 4.3 km | `250`: 19 |

  Partitions close: 276+129+8 = 413; 393+20 = 413; per-class lengths sum to the total. No Poor / Other / blank `FTYPE_`
  and no blank `MAPSCALE` inside the footprint.
- **What changed versus CG-9.**
  1. **The box over-counted by ~2.9×** (1,179 → 413). CG-9 had already labelled its figure an upper bound; this is the
     measured value. The 1,179 figure must not be quoted as "traces in the GeoDAWN area".
  2. Trace density inside the extent is 6,230 km / 51,679 km² ≈ **0.12 km of mapped trace per km²** (arithmetic on the
     measured values).
  3. **Mapping scale is the striking result.** Regionally the dominant `MAPSCALE` code is `10` (11,334 traces, CG-8 /
     requirements page), with `24` next (3,025). **Inside the footprint there are zero traces with code `10` or `24`**;
     every trace carries `250` or `100`. Regionally `250` is only 2,229 of 22,956 traces (9.7%); the footprint alone holds
     393 of those 2,229 (17.6%).
- **Why it matters for the scored target (inference — labelled as such).** Reading the codes as map-scale denominators
  in thousands (1:250,000 / 1:100,000) is the natural interpretation but is *not yet confirmed* against the v2 field-
  definition text (see Next actions). If it holds, the entire GeoDAWN catalogue was compiled from the coarsest source
  maps in the compilation. That predicts two specific gap classes: (a) short or low-relief scarps below the resolution
  of a 1:250k source, and (b) positional misfit of mapped traces large enough to leave true fault pixels outside the
  300 m kernel — the H1 "newly mapped geometry" class staff confirmed is scored. It also reframes CG-9's "comparatively
  well mapped" reading: `FTYPE_` says *constrained*, `MAPSCALE` says *coarse*. Those are different properties.
- **Caveats.** (1) Still the 2023-06-27 compilation, not the rasterised labels on the data tab — they may differ.
  (2) "Intersecting" counts a trace once even if only partly inside; the length column is the clipped length.
  (3) The USGS data page states the survey covers **51,857 km²**; the extent shapefile's own attribute says
  **51,695.2 km²** (0.3% lower). Small, but a real discrepancy between two official artefacts — **flagged, not
  resolved.**
- **Confidence:** verified (computed from primary files, reproducible by re-running the workflow). The scale-code
  interpretation and the gap-class predictions are **inference**.

## CG-10 · The catalogue is a literature compilation, not a survey

- **Source:** <https://www.usgs.gov/programs/earthquake-hazards/faults> — "Background" and "History".
- **Claim (verbatim):** "This database was used to create the fault-source characterization in the National Seismic
  Hazard Maps … For the hazard maps, both the fault surface trace and the metadata are simplified representations of the
  geometry and behavior of the fault, based on geologic interpretation." History: "Starting in the early 1970s, mainly
  in response to national concerns about the siting of nuclear reactors, scientists needed to locate active and
  Quaternary faults and document their characteristics." "These map compilations, however, did not provide much
  supporting data. Subsequent state-scale compilations, such as those by Johns and others, (1982), Stickney and
  Bartholemew (1987), and Hecker (1993) provided some supporting database and were the first true fault compilations."
  And: "In 1993, the U.S. Geological Survey began developing a database for Quaternary faults and folds for the United
  States in earnest, largely supported by NEHRP but with significant support from many State surveys."
- **Why it matters.** Completeness tracks **what was published and which state survey had capacity**, not the actual
  fault population. Joined to CG-2 — compilers were told to prefer published, recent, detailed-scale topical studies —
  this is the mechanism that produces CG-7 class 4. A fault in an unfashionable quadrangle is absent for reasons that
  have nothing to do with whether it exists.
- **Confidence:** verified — read from the USGS page this session.

## CG-11 · Nevada's contribution runs through one state agency

- **Source:** same USGS page, "List of cooperators": "Nevada - Nevada Bureau of Mines and Geology". Service host for the
  INGENIOUS update: <https://web2.nbmg.unr.edu/> (University of Nevada, Reno).
- **Claim:** the QFFD is a cooperative federal–state compilation with one named cooperator per participating state; for
  Nevada that is NBMG, which also hosts the INGENIOUS Qfaults update used as training labels.
- **Why it matters.** Where the Nevada catalogue is thin is partly a statement about NBMG's mapping history — which
  programmes were funded, which quadrangles were prioritised, and when. That makes gap class 4 *measurable* rather than
  rhetorical, provided someone measures it.
- **Next measurement (not done):** intersect trace density with NBMG's published geologic-map coverage per quadrangle.
  The map index has **not** been read this session, so no statement is made about what it contains.
- **Confidence:** verified for the cooperator listing and the service host. The mapping-history argument is
  **inference**.

## Next actions

1. ~~Clip CG-8 to the GeoDAWN outline polygon.~~ **Done 2026-09-26 — CG-12** (413 traces, via GitHub Actions).
2. Read the field-definition text in the v2 zip before translating `MAPSCALE` codes. **Now the top item** — CG-12's
   strongest finding depends on it. The zip downloads fine on the runner; extend `public_census.py` to print its text.
3. Once rasters are placed: distance-to-nearest-label for high-strain / high-seismicity / high-gradient pixels.
4. Reconcile the 413 footprint count (CG-12; the 1,179 envelope count is superseded) against the actual label raster. If the shipped labels contain materially more or
   fewer traces than the 2023-06-27 service inside the same box, that is a provenance discrepancy worth recording, not
   smoothing over.
