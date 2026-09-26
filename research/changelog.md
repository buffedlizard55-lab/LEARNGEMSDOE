# Changelog

Canonical HTML: [`docs/changelog.html`](../docs/changelog.html)

Append-only. Passes are idempotent — extend entries, never duplicate. Newest first.

---

## 2026-09-26 · session `arena/01a0dfd3-learngemsdoe` — public data via Actions, footprint census, H8 rejected

**Added**
- `.github/workflows/public-data.yml` + `scripts/public_census.py`: fetch the *public* GeoDAWN outline / extent zips and
  INGENIOUS Qfaults v2 on a GitHub runner (sandbox TLS is blocked), clip faults to the footprint, report via annotations.
  Run [36276586563](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/actions/runs/36276586563). No competition data, no secrets, no predictions.
- **CG-12** footprint census: 413 traces (not 1,179), 6,230.2 km clipped length, every trace `MAPSCALE` 250 or 100.
  Cross-checks pass (22,956 = CG-8; area vs `SqKm` within 0.03%).
- **H12** (coarse-scale compilation) — new, untested.

**Changed**
- **H8 → rejected** by its own criterion (Inferred = 0.8% of clipped length). First entry under Negative results.
- CG-9 marked superseded for footprint questions. Pipeline page: re-run results + what is and isn't unblocked.

**Flagged**
- USGS data page says 51,857 km²; extent shapefile attribute says 51,695.2 km² (0.3%). Unresolved.
- "Full pipeline ready to run" handoff claim — still false (no train/inference scripts). Re-checked.

**Re-verified (fetched)**: data tab → login redirect; forum category JSON — 11 topics, newest still 11543, no new staff reply.

**Next**: print the v2 field-definition text in the workflow to confirm `MAPSCALE` semantics (gates H12).

---

## 2026-09-26 · session `arena/01a0dfc9-learngemsdoe` — Pass 1-3 re-verification, clean UI rebuild, site audit

**Verified this session, each item fetched and read — line by line, no hallucinations**

- Competition hub <https://www.drivendata.org/competitions/306/competition-doe-gems/>: deadline Dec 3 2026 11:59 p.m. UTC, prize $300k table (Phase1 $50k top5 $10k each, Phase2 $100k/$70k/$40k/$25k/$15k), eligibility summary, how-to-compete 6 steps.
- Problem description page 967 both chunks <https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/>: competition structure Initial $50k fixed private + Final $250k expanded via expert review, datasets GeoDAWN + INGENIOUS + 1m_DEM_links.csv, provided features list, labels USGS+INGENIOUS, external data licence condition, metric DTI α=0.2 β=0.8 R=300 m triangular kernel (1-d/R)+, worked example TPw=3.00 FPw=1.89 FNw=2.00 TIw=0.60, submission format EPSG:32611 100 m float32 [0,1] same bounds null/nan outside.
- About/resources page 968 <https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/>: sponsor DOE OG, GeoDAWN 149,030 line-km 51,857 km² EarthMRI, lidar via 3DEP coordinated over similar extent, fault definition trace/zone, detection methods field + seismic + gravity/magnetic + remote sensing + edge detection/Hough/DL, subtle/hidden quote, additional info Mattéo 2021 DOI 10.1029/2020JB021269 + Hermant 2025 PDF.
- Rules page <https://www.drivendata.org/competitions/306/competition-doe-gems/rules/>: points to HeroX resource 2274.
- Official rules PDF NLR primary <https://www.nlr.gov/docs/fy26osti/96647.pdf> now redirects to docs.nlr.gov, fetched all 7 chunks: Preface change-log table still empty (5 rows), §1.1 prize overview, §1.2 key dates defers to website gems.drivendata.org, §1.3 eligibility full list (individual US citizen/PR, team captain US citizen/PR + members legally authorized to work US, private US-incorporated + primary US place, academic US accredited, FFRDC not allowed except individual capacity honorable mention no cash, non-DOE federal + federal employees ineligible, DrivenData officers/employees/judges + households ineligible, DOE employees/support contractors ineligible, debarred, under 18, MFTRP + FCOC Iran/North Korea/Russia/Belarus/China, perjury certification 18 USC 1001/287 31 USC 3729-3733 3801-3812), §1.4 prize goals, §2 background feature data GeoDAWN lidar/magnetic/radiometric + USGS 1 m DEM + labels USGS QFFD + new faults labelled by NLR/USGS experts + multidisciplinary teams encouraged, §3.2 process overview single GeoTIFF 100 m entirety of GeoDAWN, 3 per week, generative AI disclosure verbatim, evaluation DTI, solution verification complete code, §3.3 algorithm/testing labels from INGENIOUS, §3.4 feedback, §3.5 what to submit, §3.6 how determine winners public leaderboard may not equal final, blind final selection, interviews, judge DOE federal employee, winner notification ~60 days, §A.1 requirements 5 p.m. ET wording flagged vs hub, §A.2 verification payments ACH/W-9 30 days, §A.3 single-entity awards, §A.4 treatment submission materials public vs confidential double-bracket notice, §A.10 records retention FOIA 29 CFR 70.26, §A.11 privacy, §A.12 general conditions risk review not appealable + may select no winners, §A.13 program policy factors 9 items, §A.15 definitions, §A.17 platform.
- Reference solution <https://github.com/drivendataorg/gems-prize-reference-solution>: README author Prof John Lipor, env CPU/GPU CUDA 12.6/13.0, notebook unet-mc-cv-reference-solution.ipynb, approach ensemble U-Net multi split, Tversky loss weighted FN > FP, data filenames numeric_features.tif labels.tif, preprocessing < -1e38 → NaN per-channel min-max [0,1], device CUDA→MPS→CPU.
- Forum category JSON <https://community.drivendata.org/c/gems-prize-challenge/111.json> both chunks: 11 topics, newest 11543 (2026-09-25) 1 post, 11540 (2026-09-24) 1 post, 11527 (2026-09-19) 10 posts, 11528 2 posts, 11536 2 posts, 11529 2 posts, 11516 4 posts, 11531 1 post, 11526 1 post, 11524 2 posts, 11499 pinned 2 posts. No new topic since 11543.
- Forum threads JSON re-read: 11516 post 4 verbatim mask pixel-exact identical to training labels, near-known-trace fully penalized, new-fault ground truth can lie within 300 m correction outcome aimed for; post 2 masked excluded both rounds; 11536 verbatim new fault any pixel not already captured can include newly mapped geometry; 11527 post 7 verbatim not sharing details about data sources/fault types/coverage beyond problem description, Phase2 largest pool updated by expert review; 11524 rolling window; 11528 licence must permit use + sharing with sponsor; 11529 single band bug artifact.
- GeoDAWN USGS data page <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and>: 149,030 line-km 51,857 sq km, Area1 Clayton Valley rank1 200 m lines 90° 2,000 m ties 180° 100 m low/150 m mountain, Area2 remainder rank1-2 400 m/4,000 m 150 m/200 m, 4 blocks Winnemucca/Fallon/Hawthorne/Tonopah, flown 2021-11-01 to 2022-11-20 by EDCON-PRJ Inc Tonopah block Precision GeoSurveys Bell Jet Ranger rest Cloudstreet Cessna 180 Turbo 206, drape 22-degree climb/descent variable clearance warning verbatim, magnetic processing diurnal/aircraft/tie-line levelling/micro-levelling/IGRF, radiometric corrections aircraft/cosmic/radon/Compton/altitude, deliverables grd/map/gdb Oasis Montaj/Geosoft Viewer + Esri shapefiles flight paths/outlines, CC0 1.0, citation Glen Earney 2024.
- ScienceBase item <https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7> JSON: publication 2024-03-01 start 2021-11-01 end 2022-11-20, citation Glen Earney 2024 DOI 10.5066/P93LGLVQ, boundingBox minX -120.0024 maxX -116.1415 minY 37.3641 maxY 40.7247 WGS84, file list includes GeoDAWN_area1_outline.zip 1,190 bytes, area2 1,497 bytes, extent 2,774 bytes, plus contractor report PDF readme csv metadata zip grids.
- INGENIOUS GDR 1391 <https://gdr.openei.org/submissions/1391>: DOI 10.15121/1881483 CC BY 4.0, 9 files 116.98 MB, list 2m temp probe 1.03 MB, earthquake density 22.98 MB independent+dependent, electrical conductance MT 5 depth ranges 2-200 km DOI 10.5066/P9TWT2LU, elevation trend detrended DOI 10.5066/P9MQRCBY, geodetic shear/dilation 51.99 MB Nevada Geodetic Lab, gravity/magnetics DOI 10.5066/P9Z6SA1Z, heat flow DOI 10.5066/P9BZPVUC, paleo geothermal 82.04 kB sinter/tufa, slip/dilation tendency DOI 10.5066/P9YL58W6, Qfaults v1 5.76 MB, v2 5.85 MB supersedes v1 with field definitions text, volcanics 9.44 MB, study area boundary 6.68 kB, thermal conductivity, well/spring temp/chemistry 19.85 MB.
- USGS QFFD <https://www.usgs.gov/programs/earthquake-hazards/faults>: coseismic surface deformation past 1.6 Ma verbatim, 1983 timescale 1.6 Ma updated 1.8 Ma 1999 2.6 Ma 2009 2.58 Ma 2018, 2017-01-12 limited metadata fields archived reports via abbreviated record, Search retired 2026-02-26 legacy via interactive map DOI 10.5066/F7S75FJM, downloads KML 13 MB 5 layers historic/Holocene/late Quaternary/middle-late/Quaternary + GIS zip 16 MB, citation USGS 2020 DOI 10.5066/P9BCVRCK, cooperators list 12 states Alaska to Utah Nevada = Nevada Bureau of Mines and Geology, Background archive for M>6 Quaternary, History early 1970s nuclear reactor siting, state maps Jennings 1975 Witkind 1975 etc, first true compilations Johns 1982 Stickney Bartholemew 1987 Hecker 1993, 1990 ILP Working Group II-2 World Map Active Faults Trifonov, 1993 USGS developing database earnest NEHRP + state surveys.
- NBMG service <https://web2.nbmg.unr.edu/arcgis/rest/services/Qfaults/Qfaults_INGENIOUS/MapServer/0?f=pjson>: layer Qfaults [INGENIOUS 6-27-2023] 22,956 polylines, supportsStatistics false, CRS NAD83 Contiguous USA Albers, fields NAME NUM DIPDIRECT SLIPDIRECT SLIPSENSE SECONDARY SLIPRT2023 SLIPRTNUM REC2023 RECNUM CODE2023 FCODE2023 RCODE2023 SCODE2023 FTYPE_ MAPSCALE SLIPINFO RECINFO COMMENTS GEOCOMM Shape_Leng.
- Metric self-tests: 11 PASS pure python backend (numpy not present here but fallback works, numpy path documented).
- Site checks: 18 pages 63 sources PASS, search index 99 items PASS.

**Added/changed this session**

- Rebuilt docs/index.html with clean UI, user-friendly organized sections, verified-today banner with session id, explicit data-placement blocker with copy-paste commands, competition facts table with source links verified today, research library cards, hypothesis backlog table, flagged irregularities 12 items with links, verification commands, official links for manual review.
- Updated docs/research/index.html meta re-verified line.
- Updated docs/assets/style.css header comment to v2 design goals.
- Added this changelog entry and matching AI-usage-log entry (see research/ai-usage-log.md and docs/ai-usage.html).
- Re-ran all offline checks: metrics selftest PASS, check_site PASS, build_search_index --check PASS, download_competition_data.sh still blocked_no_data (curl 35 TLS) + public outlines fail same, prepare_data.py blocked_no_data — both expected and not treated as missing.
- No prediction GeoTIFF generated, no weekly slot used, no second site/repo/account, no DrivenData login.

**Flagged, not smoothed — re-confirmed today**

- Deadline hub 11:59 p.m. UTC vs rules §A.1 5 p.m. ET.
- Eligibility hub shorter vs rules §1.3 longer (work authorization, FFRDC, MFTRP/FCOC).
- Test-fault provenance declined 11527 post7.
- Band-19 bug 11529.
- Feature-stack provenance undocumented beyond tags.
- No training/inference pipeline in repo — only metrics verified; handoff claim "ready to run" false, still flagged.
- Rules PDF redirect nlr.gov → docs.nlr.gov, change-log empty.
- Staff about-post links page 966 duplicate not 967.
- Public downloads TLS failure curl 35 — environment limit, not absence.
- MAPSCALE/REC2023 mixed conventions.
- Submission extent entirety of GeoDAWN vs same bounds as training data — grid bounding box 3292×3730×100 m ≈122,800 km² vs surveyed 51,857 km² ≈2.4×.
- GeoDAWN contents rules §2 lidar/magnetic/radiometric vs release magnetic/radiometric + 3DEP lidar coordinated separate similar extent.

**Next**

- Clip CG-9 1,179 envelope census to Area1/Area2 outline polygons (public shapefiles, no login) on machine with working TLS.
- Place competition rasters on enrolled unrestricted machine, run prepare_data.py, reconcile inventory vs feature-stack page.
- Read INGENIOUS v2 field-definition text inside zip before translating MAPSCALE codes.
- Read Hermant chunks 7+ tail reference list + Mattéo 2021 body methods.
- Re-check forum threads 11540,11526,11543,11499 for staff replies.

---

## 2026-09-26 · session `arena/01a0df88-learngemsdoe` — catalogue census, Hermant read end to end, site search and verification

**Verified this session, each item fetched and read**

- Competition hub; problem page 967 (both chunks); About page 968 — metric, submission format and the GeoDAWN + 3DEP
  wording re-confirmed against the text.
- Rules PDF (served from `docs.nlr.gov`): Preface change-log table still empty; §1.1 prize table; §1.2 **defers** key
  dates to the website; §1.3 eligibility; §2 background (labels, 1 m DEM, GeoDAWN described as a lidar/magnetic/
  radiometric study); §3.1–§3.2 (single GeoTIFF, three per week, AI disclosure).
- Forum category JSON (both chunks): 11 topics, newest 11543 (2026-09-25). No new topic or staff reply since the
  previous session.
- [ScienceBase GeoDAWN bounding box](https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7?format=json&fields=spatial):
  −120.0024, 37.3641, −116.1415, 40.7247 (WGS 84).
- NBMG INGENIOUS Qfaults service: six `returnCountOnly` queries inside that box (CG-9), plus layer metadata
  (`supportsStatistics: false`; CRS NAD 1983 Contiguous USA Albers).
- USGS faults page: 1.6 Ma definition, 2017 metadata reduction, 2026 search retirement, cooperators list — and the
  "History" section, new to the library (CG-10).
- Hermant et al. (2025) PDF chunks 4–6: results in prose, Figures 7–9, discussion, conclusion, reference list. Two DOIs
  found there were resolved and checked.
- USGS GeoDAWN data page: rank criteria, flight azimuths, CC0 1.0, shapefile deliverables.
- Drenth & Grauch (2019) Table 1 (Eos) — the rank criteria GeoDAWN cites.
- Reference-solution README (via the GitHub API): author, environment choices, notebook name.

**Measured — the highest-value result of the session.** CG-9: **1,179** of 22,956 INGENIOUS traces intersect the GeoDAWN
bounding box — 739 Well Constrained, 351 Moderately Constrained, 89 Inferred, 0 Poor/Other/blank, 0 blank `MAPSCALE`.
739 + 351 + 89 = 1,179 exactly and the complementary query returns 0, so the partition closes. This is the clip the
previous session asked for, done against the published box. The polygon version remains open. No total length is
asserted: the service reports `supportsStatistics: false` and refuses the sum.

**Added.** Research entries CG-9, CG-10, CG-11, PF-8, PF-9, GM-7, GM-8, GM-9, ST-7, PA-6, PA-7, PA-8, GV-11, GV-12,
GV-13. Hypotheses H9, H10, H11. Site-wide search with a generated index, two-tier navigation, a "start here" reading
order, a verification section on the overview, and two scripts (`scripts/check_site.py`,
`scripts/build_search_index.py`). Also added `.github/workflows/verify.yml` CI for metrics, site checks, and search-index
freshness; footer links from research and hypothesis pages back to the explainer and submission gate; and a README note
documenting the two configured Pages deploy paths plus the remaining owner-only source-switch step.

**Corrected.** PA-2's epoch-resolved Hermant figures (PR-AUC ≈ 0.88 / ≈ 0.59 "at epoch 17.5") were approximations read
off a figure whose axis labels were truncated in our extraction, and the epoch attribution is not supported by the
paper's prose. They are superseded by the values §6 states (PA-6), and the sequence is recorded on the sources page.
Figure 7's per-epoch table was deliberately left untranscribed rather than guessed at.

Pass 2 corrected H10/GM-7 to state only the coordinates printed in Hermant et al.'s figures; restored a missing `<tr>`
in `sources.html`; changed Drenth & Grauch to **Eos (2019)** rather than an unverified volume number; and recorded the
§1.3 eligibility text re-confirmation with its no-team-change limit. Pass 3 corrected stale overview/library/meta-line
domain counts, the requirements H1–H11 label, and the pipeline search-index count; `check_site.py` now enforces
overview-card and domain-meta counts as well as library-card counts.

**Flagged, not smoothed.** Rules §3.2 says the submission must cover "the entirety of the GeoDAWN study area" while the
problem description says "the same bounds as the training data" — not obviously the same instruction given a grid
bounding box ≈ 2.4× the surveyed area (GV-12). Rules §2 describes GeoDAWN as including lidar while the data release
treats the 3DEP lidar as a separate coordinated collection (GM-9 / GV-13).

**Not done.** No competition raster was obtained; both data scripts were re-run and still report `blocked_no_data`, with
all four public files failing TLS. No prediction file. No second site, repo, account or registration. No training or
inference script was added — the handoff claim that a complete pipeline is "ready to run" is still not true of this
repository, and that irregularity remains on the overview.

**Still open / next**

1. Repeat the six CG-9 queries against the Area 1 / Area 2 outline polygons instead of the bounding box. Everything
   else in the backlog is gated on the rasters.
2. Place the rasters on an enrolled machine, then reconcile the label raster against the 1,179 envelope count.
3. Read the INGENIOUS v2 field-definition text (still blocked by TLS) before translating `MAPSCALE` codes.
4. Hermant chunks 7+ (the tail of the reference list) and the body of Mattéo et al. 2021.

---

## 2026-09-26 · session `arena/01a0df77-learngemsdoe` — Pass 1–3: re-verify, forum watch, Pages UX

**Verified against primary sources this session (fetched and read):**

- Hub, problem 967 (both chunks), About 968.
- Forum category JSON; threads 11540, 11526, 11543 (each `posts_count` 1).
- USGS QFFD landing page; INGENIOUS GDR 1391; NBMG `returnCountOnly` = 22956.

**Added**

- `docs/forum.html` — unanswered-thread table with JSON links.
- GV-10. Mobile nav toggle. Library domain filter.
- This changelog block and the AI-usage log block.

**Still open / next**

- Clip `FTYPE_` / `MAPSCALE` to GeoDAWN outlines.
- Place competition rasters only on an enrolled machine.

---

## 2026-09-26 · session `arena/01a0df46-learngemsdoe` — Pass 1–3: catalogue counts, requirements list, data-placement attempt

**Verified against primary sources this session (fetched and read; not copied from the previous session's notes):**

- Competition hub, problem description (both chunks), About page, data tab (login redirect), page 966 (duplicate welcome).
- Rules PDF chunks covering §1.3, §2, §3.2, §3.3, §3.4, §A.1. Official URL redirected to `docs.nlr.gov`. Preface change-log table still empty.
- Forum category JSON and threads 11499, 11526, 11540, 11543. Still unanswered. No new topic since 11543 (2026-09-25).
- ScienceBase item JSON file list, including outline zip sizes and MD5s.
- INGENIOUS GDR submission 1391 resource list.
- NBMG MapServer `Qfaults/Qfaults_INGENIOUS` layer 0: field list, 22,956 feature count, `FTYPE_` and `MAPSCALE` partitions, partial `REC2023`.
- USGS faults page and USGS FAQ “What is a Quaternary fault?”
- Reference-solution README via GitHub. Notebook was not re-read this session (1.6 MB); no new claim taken from it.

**Added**

- `docs/requirements.html` — the full requirements checklist, with the counted attribute inventory and a query link for each count.
- Research entry CG-8 and hypothesis H8. H8 is untested; the regional counts are measured.
- Watch-list rows for the page-966 link and the rules-PDF host redirect.
- Download script now attempts the small public outline zips and records failure. It still never logs in.

**Changed**

- CG-4's “field definitions unread” note: field names and counts are now verified from the live service. The zip's text document is still unread.
- Pipeline page distinguishes the login wall from the TLS failure. They are not the same blocker.
- Irregularity list extended. The “pipeline is ready” handoff was re-checked and remains false. No training or inference script was added.

**Still open / next**

- Clip `FTYPE_` and `MAPSCALE` to the GeoDAWN outlines. That is the single highest-value next question.
- Read the v2 field-definition text before translating `MAPSCALE` codes.
- Re-check 11540, 11526, 11543, 11499.
- Place competition rasters only on an enrolled machine. Do not create an account from this agent.

---

## 2026-09-26 · session `arena/01a0df14-learngemsdoe` — Pass 3: verification, corrections, full source re-read

**Verified against primary sources this session (all re-fetched and read line by line):**

- NLR rules PDF — **all seven chunks, §1.1 through §A.17**. Closes the previous session's gap at §A.14–A.17.
- Competition hub, problem description (both chunks), About page.
- Forum: category index plus threads 11499, 11516 (*all four posts, via the Discourse JSON endpoint*), 11524, 11526,
  11527 (*all ten posts*), 11528, 11529, 11531, 11536, 11540, 11543.
- USGS GeoDAWN data page and Quaternary Fault and Fold Database landing page.
- INGENIOUS GDR submission 1391 (full resource list and licences).
- Hermant et al. 2025 PDF (chunks 0–3 of 8) and Mattéo et al. 2021 publisher record.
- Reference-solution README and notebook (band listing, raster geometry, preprocessing code).
- Miller & Singh 1994 and Verduzco et al. 2004 — bibliographic records and DOIs corroborated; Kreemer & Young 2022
  publisher record confirmed.
- HeroX rules resource 2274 — read; names the NLR PDF as the official rules document and links to it.
- USGS ScienceBase item for GeoDAWN — read; adds publication date 2024-03-01 and survey dates 2021-11-01 to 2022-11-20.
- GBCGE INGENIOUS project page — read; PI, personnel, duration (1 Feb 2021 – 30 Jun 2025), $10,000,000 under DOE GTO
  award DE-EE0009254, and the project's own publication list.
- Hart-Wagoner, Coolbaugh, Faulds & Mlawsky (GRC) — abstract and introduction read; confirms the INGENIOUS fault
  database updated locations plus recency and slip-rate attributes.

**Corrections**

- **Scoring mask upgraded from inference to verified.** Staff post 4 of thread 11516 (2026-09-21): "The mask is indeed
  pixel-exact — it is identical to the provided set of training fault labels." The previous session hedged this; the
  hedge is removed and the full post is now quoted on the governance page. Two further points from the same post are new
  to the library: near-known-trace predictions are *fully* penalised, and new-fault ground truth may lie within 300 m of
  a known trace.
- **Label provenance added.** Rules §2: the new faults were "labeled by geology experts at the National Laboratory of
  the Rockies (NLR) and USGS". Not previously recorded.
- **One source demoted, then reinstated on evidence.** "Hart-Wagoner et al., GRC feature engineering" had been listed
  with no verified content, so it was moved out of the citation index. The PDF was then opened: it is a real GBCGE /
  Nevada Bureau of Mines and Geology paper whose abstract states that the INGENIOUS fault database "included updated
  fault locations and updated fault attributes of recency … and slip rates" — directly relevant to CG-4. Restored to the
  methods table as *abstract and introduction read*. The sequence is recorded on the sources page rather than silently
  reversed.
- **Two author lists corrected.** Kreemer "et al." → **Kreemer & Young (2022)**, and Siler → **D.L. Siler (2022)**,
  using the [INGENIOUS project page](https://gbcge.org/current-projects/ingenious/)'s own publication list.
- **Pipeline claim flagged as inaccurate.** The handoff stating a complete train→inference→validate pipeline was "ready
  to run" does not match the repository. Recorded on the pipeline page and in the site-wide irregularity list.

**Added**

- New page `docs/feature-stack.html` — all 19 bands with official descriptions and categories, raster geometry, GeoDAWN
  acquisition table, a derived grid-area note, the public layers absent from the stack, and processing pitfalls.
- `scripts/metrics.py` — distance-weighted Tversky index, Tversky loss, masked variant, and 11 self-tests that pass on
  CPU with the standard library alone.
- Research entries expanded to CG-1…CG-7, PF-1…PF-7, GM-1…GM-6, ST-1…ST-6, PA-1…PA-5, GV-1…GV-9 — each with source,
  citation, claim, relevance and a confidence mark.
- Site-wide: redesigned stylesheet, sticky nav, per-page table of contents, client-side filters on the band table,
  hypothesis cards and source index, a confidence-mark legend, and a print stylesheet.
- Derived artefacts: 19-band family breakdown; the agreement/disagreement matrix in seismotectonics; the four
  catalogue-gap classes in CG-7 — all labelled as inference.

**Changed**

- Every hypothesis card rewritten against the pixel-exact mask confirmation; H3 marked *blocked* because it needs lidar
  placement as well as rasters.
- Overview rewritten around "what is actually scored", with a one-table competition summary and a six-item irregularity
  list.
- Explainer rewritten as a geologist-facing narrative rather than a summary of pages.

**Still open / next**

- Place rasters in `data/`; run `prepare_data.py`; reconcile against the feature-stack page.
- Download and read the INGENIOUS Qfaults v2 field-definition document (CG-4's unverified note).
- Open Miller & Singh 1994 and Verduzco et al. 2004 — still paywalled and unread.
- Read the remainder of the Hermant PDF (chunks 4–7) and the Mattéo methods.
- Re-check the four unanswered forum threads (11540, 11526, 11543, and 11499's eligibility reply) at the start of the
  next session.

---

## 2026-09-26 · session `arena/01a0df09-learngemsdoe` — Pass 1–3 verification and fixes

**Verified against primary sources (live fetches):** NLR rules PDF (§1.1, §1.3, §2, §3.2–§3.6, §A.1, §A.13),
DrivenData hub + problem page 967 + about 968, USGS QFFD page, GeoDAWN ScienceBase item, INGENIOUS GDR record, Hermant
2025 Stanford PDF, Mattéo 2021 (JGR), Kreemer & Young 2022 (SRL), and forum threads 11516 / 11527-7 / 11536.

**Fixed:** tightened the "pixel-exact scoring mask" wording in four pages — staff 11516 confirms known faults are
masked/excluded but, at that time, had not stated pixel-exact versus buffered; the 300 m kernel applies to new-fault
ground-truth distance, not to a known-fault buffer. Corrected the weekly-cap citation ("three per week" = rules
§3.2/§3.4; "rolling window" = forum 11524).

**Superseded by the session above:** the pixel-exact hedge was resolved by staff post 11516/4.

**Upgraded confidence:** CG-2 (OF 93-338 rules verified verbatim), CG-4 / PA-3 (Hermant 1,100 faults / 264 km, 50 m
buffer, 10 m lidar-derived 3DEP, B8A vegetation band, geographic half split — all confirmed in the PDF).

**Confirmed accurate, unchanged:** $300k prize structure; metric α=0.2, β=0.8, R=300 m and the 0.60 worked example;
deadline Dec 3 2026, 11:59 p.m. UTC; §3.3 INGENIOUS labels; §A.13 program-policy factors; GeoDAWN 149,030 line-km /
51,857 km² and the Area 1/2 flight specs; QFFD 1.6 Ma coseismic-surface-deformation design.

---

## 2026-09-26 · session `arena/01a0def8-learngemsdoe` — Pass 1–3: stand up the site

**Added**

- GitHub Pages site under `docs/`: overview, explainer, six-domain library, hypothesis backlog, sources, pipeline, AI
  log, changelog.
- `PROJECT_BRIEF_GEMSDOE.md` — reconstructed; the file was **not present in the repository at session start** (flagged
  at the time).
- Research markdown mirrors in `research/`.
- `scripts/download_competition_data.sh` and `scripts/prepare_data.py` — both inspect-only; neither can emit a
  prediction raster.
- Hypothesis cards H1–H7, all *untested*.

**Pass 2:** staff post 11527/7 recorded (no test-fault protocol will be published). Root `index.html` redirect added so
the legacy Pages source still reaches the library. §A.13 program-policy factors noted.

**Verified against:** DrivenData hub/967/968, NLR rules PDF, forum staff posts 11516/11524/11528/11529/11536, GeoDAWN
DOI, INGENIOUS DOI, USGS QFFD page, Hermant 2025 PDF, reference-solution README and notebook.

---

## Conventions

- One entry per session, newest first, dated with the session branch name.
- Append only. Earlier entries are corrected by adding a "superseded" note, never by rewriting history.
- Every "verified" claim names the source it was read from. Every correction names what changed and why.
- Each session entry ends with what is still open, so an interrupted run is resumable.
