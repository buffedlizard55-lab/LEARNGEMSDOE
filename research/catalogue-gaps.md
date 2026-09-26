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
- **Confidence:** verified for the GDR descriptions, the Hart-Wagoner abstract (read) and the project page (read). **Unverified** — the field-definition document inside the v2 archive has not been unpacked. **Update 2026-09-26:** now read — see CG-12.

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
- **Confidence:** verified for the counts. **Update 2026-09-26:** the field-definition README was read (CG-12) — it defines 24, 63, 100, 250, 316, 500 as scale denominators; `10`, `50`, `60`, `62.5`, `125`, `155`, `700` and `1:10,000` remain **undocumented** (flagged).

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
     class 4. **Inference** from two verified counts; the footprint clip is still pending. **Update 2026-09-26:** done — CG-12.
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
- **Scale codes — confirmed from the primary field-definition file**
  (`README_fielddefinitions_qfaults_ingenious_nad83conus117_2023-06-27.txt` inside the GDR v2 zip; 112 lines, sha256
  `94bda0c28a98475285047e97644d732cb2a4322ed218d6c442709edb89716cec`; printed verbatim in [run 36276864491](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/actions/runs/36276864491)):
  - `250` — "1:250,000, fault could be more discontinuous than continuous and mapping is accurate at >1:125,000 scale."
  - `100` — "1:100,000, fault could be more discontinuous than continuous and mapping is accurate at >50,000 scale."
  - The same table defines `24`, `63`, `316`, `500`. `FCODE2023` values 1–2 say mapping "is accurate at given
    \"MAPSCALE\" value".
- **Irregularity flagged — undocumented codes.** The README's `MAPSCALE` table lists only 24, 63, 100, 250, 316, 500. The
  regionally dominant code **`10` (11,334 traces)** and codes `50`, `60`, `62.5`, `125`, `155`, `700` and the literal
  `1:10,000` (requirements page) are **not defined** there; conversely 63, 316 and 500 do not appear in the service
  counts. The footprint is unaffected (only 250/100 occur), but nobody should guess what `10` means regionally.
- **Why it matters for the scored target.** The entire GeoDAWN catalogue is compiled at 1:100,000–1:250,000 — the
  coarsest codes present in the footprint's compilation — and the compilers state such traces "could be more
  discontinuous than continuous" (verified quote). The gap-class reasoning that follows is **inference**. That predicts two specific gap classes: (a) short or low-relief scarps below the resolution
  of a 1:250k source, and (b) positional misfit of mapped traces large enough to leave true fault pixels outside the
  300 m kernel — the H1 "newly mapped geometry" class staff confirmed is scored. It also reframes CG-9's "comparatively
  well mapped" reading: `FTYPE_` says *constrained*, `MAPSCALE` says *coarse*. Those are different properties.
- **Caveats.** (1) Still the 2023-06-27 compilation, not the rasterised labels on the data tab — they may differ.
  (2) "Intersecting" counts a trace once even if only partly inside; the length column is the clipped length.
  (3) The USGS data page states the survey covers **51,857 km²**; the extent shapefile's own attribute says
  **51,695.2 km²** (0.3% lower). Small, but a real discrepancy between two official artefacts — **flagged, not
  resolved.**
- **Confidence:** verified (computed from primary files, reproducible by re-running the workflow); scale-code meaning
  verified from the field-definition README. The gap-class predictions are **inference**.

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

## CG-13 · Only *published* evidence can enter the compilation at all

- **Source:** <https://www.usgs.gov/programs/earthquake-hazards/faults> — "Reference Materials" section (read 2026-09-26)
- **Citation:** U.S. Geological Survey, 2020, Quaternary Fault and Fold Database for the Nation, <https://doi.org/10.5066/P9BCVRCK>
- **Claim (verbatim):**
  > "For this compilation, we have limited our compilation to synthesis of published literature relevant to the United
  > States. Our definition of published literature includes typical sources (journals and maps), as well as M.S. theses
  > and Ph.D. dissertations, governmental contract reports (which includes many NEHRP-sponsored studies), abstracts, and
  > open-file (preliminary) reports. **We generally do not cite unpublished field mapping, field notes, and other
  > gray-literature reports that are not generally available to the public.**"
  >
  > "These data are compiled from thousands of journal articles, maps, theses, and other documents, as referenced herein."
- **Relevance:** this is the strongest single sentence in the whole library for gap class 4 (CG-7). It is not our
  inference that publication history gates inclusion — the database says so itself. A scarp that is visible in lidar,
  recognisable in the field, and never written up has no route into the compilation. The named exclusions ("unpublished
  field mapping, field notes") are exactly the evidence a field campaign produces before publication, and the named
  inclusions ("abstracts, open-file (preliminary) reports") set a floor on how weak admissible evidence may be.
- **Confidence:** verified — quoted verbatim from the official USGS page this session.

## CG-14 · The catalogue's own fault classes A–D — and every section inside the footprint is Class A

- **Source:** same USGS page, "Fault Classes" table. The page attributes the classes to Crone and Wheeler, 2000; **no URL for that reference is given on the page, and none is asserted here.**
 
- **Claim (verbatim):**
  - **Class A** — "Geologic evidence demonstrates the existence of a Quaternary fault of tectonic origin, whether the
    fault is exposed for mapping or inferred from liquefaction or other deformational features."
  - **Class B** — "Geologic evidence demonstrates the existence of a fault or suggests Quaternary deformation, but either
    (1) the fault might not extend deeply enough to be a potential source of significant earthquakes, or (2) the
    currently available geologic evidence is too strong to confidently assign the feature to Class C but not strong
    enough to assign it to Class A."
  - **Class C** — "Geologic evidence is insufficient to demonstrate (1) the existence of tectonic fault, or (2)
    Quaternary slip or deformation associated with the feature."
  - **Class D** — "Geologic evidence demonstrates that the feature is not a tectonic fault or feature; this category
    includes features such as demonstrated joints or joint zones, landslides, erosional or fluvial scarps, or landforms
    resembling fault scarps, but of demonstrable non-tectonic origin."
- **Measured this session (CG-15/CG-16):** every one of the **5,570** USGS sections intersecting the GeoDAWN data
  extent carries `class = A`. There is no Class B, C or D section inside the footprint.
- **Relevance:** two consequences. (1) The USGS catalogue inside the GeoDAWN footprint contains **no** entries that the
  database itself considered uncertain or non-tectonic — so "the catalogue here is poorly constrained" is *false* as
  stated, and any argument that leans on it should be dropped. (2) Class D is the catalogue's own name for the confuser
  set: erosional and fluvial scarps and "landforms resembling fault scarps, but of demonstrable non-tectonic origin".
  That is the same list Hermant et al. measured their models firing on (GM-8, GM-10) — paleo-shorelines, canyon and
  stream boundaries, the Rec Area scarp. The database resolved those questions with field evidence a model does not
  have; a detector cannot, so it must price them rather than delete them (H11).
- **Confidence:** verified for the class definitions and for the measured `class` counts.

## CG-15 · Measured side by side: USGS QFFD vs INGENIOUS inside the footprint

Closes the question CG-12 could not: how much fault is actually catalogued inside the GeoDAWN footprint, and do the two
compilations the problem description names as label sources agree?

- **Inputs (primary, both public):** `Qfaults_GIS.zip` — 32,371,696 bytes, sha256
  `447eadc5926256710d988c30e5996ba540604caa0154f9746c48bad637926893` — from
  <https://earthquake.usgs.gov/static/lfs/nshm/qfaults/Qfaults_GIS.zip>, the "GIS files" link on the USGS faults page
  (<https://www.usgs.gov/programs/earthquake-hazards/faults>); and INGENIOUS Qfaults v2 from
  [GDR 1391](https://gdr.openei.org/submissions/1391), <https://doi.org/10.15121/1881483>.
- **How it was run:** GitHub Actions runner in *this* repository (sandbox TLS is blocked) — workflow
  [`public-data.yml`](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/blob/main/.github/workflows/public-data.yml),
  script [`public_census.py`](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/blob/main/scripts/public_census.py),
  run [36277952393](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/actions/runs/36277952393). Results were read back
  from the check-run annotations; the full JSON is the `public-census` run artifact. No competition raster was touched;
  no prediction was produced.
- **What the USGS zip contains:** three shapefiles, all EPSG:4326 —
  `Qfaults_GIS/SHP/Qfaults_US_Database.shp` (112,809 records), `fault_areas.shp` (37 records, fault *zones* as polygons),
  `ca_offshore.shp` (1,093 records, offshore California). Inside the GeoDAWN data extent polygon:
  **5,570** sections from `Qfaults_US_Database`, **0** from `fault_areas`, **0** from `ca_offshore`.
- **Measured inside the same polygon (the GeoDAWN data extent, EPSG:32611, computed area 51,678.8 km²):**

| | USGS QFFD (`Qfaults_US_Database`) | INGENIOUS Qfaults v2 (2023-06-27) |
| --- | --- | --- |
| Records, whole dataset | 112,809 | 22,956 |
| Traces intersecting the footprint | **5,570** (all distinct geometries) | **413** |
| Clipped length inside the footprint | **6,241.3 km** (6,241,293.3 m) | **6,230.2 km** (6,230,216.8 m) |
| Mean trace length (arithmetic) | 1,120.5 m | 15,084.3 m |

- **Mutual agreement (distances computed in the INGENIOUS layer's NAD83 Contiguous USA Albers equal-area projection, in
  metres — not geodesic):**
  - Each of the 413 INGENIOUS footprint traces to its nearest USGS section: **0.0 m for all 413** (they intersect).
  - Each of the 5,570 USGS sections inside the footprint to its nearest INGENIOUS trace: min 0.0 m, median 0.0 m,
    **max 31.6 m**; 100% within 100 m.
  - Length difference between the two compilations inside the footprint: 11.1 km of 6,230.2 km = **0.18%**
    (arithmetic on the two measured values).
- **Reading.** The two compilations carry the *same fault network* inside the footprint — the same total length to
  within 0.18%, and mutually within 31.6 m. The 13.5× difference in record count is **granularity**: the USGS database
  distributes ~1.1 km fault *sections*, INGENIOUS distributes ~15 km *traces*. **This corrects a statement this
  knowledge base previously made.** CG-12 reported "413 traces inside the data extent" and several pages read that as
  the catalogue's content in the GeoDAWN area. It is not: it is one compilation's record count. The content is
  ~6,230 km of mapped fault, however it is segmented. Any future sentence of the form "the catalogue holds only N
  traces here" is wrong unless it names the compilation and the granularity.
- **Caveats.** (1) The USGS zip was downloaded 2026-09-26; the INGENIOUS compilation is dated 2023-06-27, so part of
  any difference could be three years of USGS updates rather than compilation practice. (2) Neither is the rasterised
  label file on the data tab; that reconciliation is still outstanding (CG-12 caveat 1). (3) "Intersecting" counts a
  trace once even if only partly inside; the length column is the clipped length. (4) `fault_areas` and `ca_offshore`
  do not intersect the footprint, so nothing is claimed about fault *zones* inside it.
- **Confidence:** verified — computed from the two primary files on a public runner, reproducible by re-running the
  workflow. The interpretation is labelled as such.

## CG-16 · Who compiled the footprint, at what scale, and how certain — the mapping-history evidence

The USGS `Qfaults_US_Database` layer carries the compilation's own provenance attributes. Counted inside the GeoDAWN
data extent (5,570 sections; every count is one re-runnable measurement, CG-15):

| Attribute | Values inside the footprint | Share |
| --- | --- | --- |
| `cooperator` | Piedmont Geosciences, Inc. **4,052** · U.S. Geological Survey **951** · California Geological Survey **567** | 72.7% / 17.1% / 10.2% |
| `scale` | 1:250,000 **4,890** · 1:62,500 **389** · 1:100,000 **274** · unspecified **14** · 1:24,000 **3** | 87.8% / 7.0% / 4.9% / 0.3% / 0.05% |
| `linetype` | Well Constrained **4,896** · Moderately Constrained **592** · Inferred **82** | 87.9% / 10.6% / 1.5% |
| `certainty` | Good **5,567** · blank **3** | 99.95% / 0.05% |
| `class` | A **5,570** | 100% |
| `age` | undifferentiated Quaternary **2,335** · latest Quaternary **1,928** · historic **715** · late Quaternary **562** · middle and late Quaternary **30** | 41.9% / 34.6% / 12.8% / 10.1% / 0.5% |
| `slip_sense` | Normal **3,786** · Right lateral **1,417** · Left lateral **364** · Unspecified **3** | 68.0% / 25.4% / 6.5% / 0.05% |
| `Location` | Nevada **5,167** · California **403** | 92.8% / 7.2% |

- **Relevance — four things this settles or changes.**
  1. **Gap class 4 is now measurable, and it is a compiler statement.** 72.7% of the sections inside the footprint were
     compiled by one contractor (Piedmont Geosciences, Inc.), 17.1% by USGS, 10.2% by the California Geological Survey.
     CG-11's argument — that where the Nevada catalogue is thin is partly a statement about who was funded to map what,
     and when — is no longer rhetorical inside this footprint: the compiler is an attribute on almost every section.
  2. **H12 is corroborated on the USGS side.** 87.8% of the sections inside the footprint are `scale = 1:250,000`, and
     only 3 of 5,570 are 1:24,000. The INGENIOUS-side measurement (every footprint trace `MAPSCALE` 250 or 100, CG-12)
     and the USGS-side measurement now agree: the GeoDAWN catalogue is a coarse-scale compilation. Two independent
     compilations, same conclusion.
  3. **H12's *mechanism* is weakened.** H12 argued that at 1:250,000 "1 mm on the source map is 250 m on the ground, so
     digitising and generalisation error alone is of the order of the 300 m kernel". The measured mutual agreement
     between two independent compilations is **≤ 31.6 m** — an order of magnitude smaller than that arithmetic. The
     naive scale argument over-predicts positional error. H12's class (b) (a scarp offset from a mapped trace by more
     than the kernel) therefore cannot be sized from compilation-to-compilation offsets; it must come from expert
     re-mapping at higher resolution (H10, GM-7's >150 m and CG-5's 400 m). H12 class (a) — short or low-relief scarps
     below the resolution of a 1:250k source — is untouched by this measurement.
  4. **The "poorly constrained catalogue" framing is dead inside this footprint.** `linetype` is 87.9% Well
     Constrained, `certainty` is 99.95% Good, `class` is 100% A, and Inferred is 1.5% of sections. This independently
     re-confirms the H8 rejection on the USGS side: the poorly-constrained stock that H8 wanted to exploit is not here.
- **Why the age column matters for H14.** 12.8% of the sections have `age = historic` and 34.6% `latest Quaternary` —
  nearly half the footprint's catalogue records rupture within the Holocene, i.e. the best-studied material.
  41.9% are only "undifferentiated Quaternary". That asymmetry is the basis of hypothesis H14.
- **Confidence:** verified for all counts (computed from the primary shapefile on a public runner). The four
  interpretations are labelled **inference** where they go beyond the counts.
- **Flagged irregularity.** The USGS faults page describes this file as "GIS files (16 MB ZIP file)". The file served
  at that URL on 2026-09-26 is **32,371,696 bytes** (≈ 32.4 MB decimal, ≈ 30.9 MiB) — roughly twice the stated size.
  Both the URL and the size were read from the same official page the same day; the discrepancy is recorded, not
  resolved.

## Next actions

1. ~~Clip CG-8 to the GeoDAWN outline polygon.~~ **Done 2026-09-26 — CG-12** (413 INGENIOUS traces, via GitHub Actions).
2. ~~Read the field-definition text in the v2 zip.~~ **Done 2026-09-26 (CG-12)** — 250 = 1:250,000, 100 = 1:100,000;
   code `10` is undocumented (flagged).
3. ~~Measure the USGS side of the catalogue inside the footprint.~~ **Done 2026-09-26 — CG-15/CG-16**: 5,570 sections,
   6,241.3 km, ≤ 31.6 m from the INGENIOUS traces. Corrects the "413 traces is the catalogue" reading.
4. Once rasters are placed: distance-to-nearest-label for high-strain / high-seismicity / high-gradient pixels.
5. Reconcile the label raster against **both** public compilations — the INGENIOUS 413-trace clip (CG-12) and the USGS
   5,570-section clip (CG-15). If the shipped labels carry materially more or less mapped length than ~6,230 km inside
   the same polygon, that is a provenance discrepancy worth recording, not smoothing over.
6. Split the USGS 5,570 footprint sections by `cooperator` and by `scale` on a map, and ask whether catalogue density
   tracks the compiler rather than the geology (CG-16, H14). This needs no competition data and is the next
   measurement that could move a hypothesis.

### Arithmetic, stated so it can be checked

6,230.2 km of catalogue trace at 100 m pixels is at least **62,302** one-pixel-wide fault pixels. The prediction grid is
3292 × 3730 = **12,279,160** pixels. So the known-fault class occupies **≥ 0.51%** of the grid — arithmetic from two
verified numbers, assuming a one-pixel-wide rasterisation. Compare Hermant et al.'s 6.5% positive fraction at 10 m with a
50 m buffer (GM-3): the imbalance here is worse by more than an order of magnitude, and the buffer that produced their
6.5% is not available to us because the mask is pixel-exact (GV-5).
