# Hypothesis backlog

Canonical HTML (full cards): [`docs/hypotheses.html`](../docs/hypotheses.html)

Every card states layers, physical signature, why it catches a *catalogue gap* rather than a known fault, expected
DTI impact, cost, validation protocol and rejection criterion. Written for a Phase 2 geologic reviewer.
Negative results stay in this table.

| ID | Status | Summary | Cost | Blocks on |
| --- | --- | --- | --- | --- |
| H1 | untested | New geometry of known systems — tip extensions, splays, parallel strands, positional corrections | Low–med | Rasters |
| H2 | untested | Buried intra-basin structures from gravity/magnetic edges under cover | Low | Rasters |
| H3 | blocked | 1 m lidar scarps too subtle for the compiled catalogue | High | Rasters + DEM |
| H4 | untested | Kinematic orphans — strain/seismicity highs with no catalogue trace | Low | Rasters |
| H5 | untested | Do not train to reproduce the label raster the scorer masks out | Med | Rasters + GPU |
| H6 | untested | Conductivity as corroboration only, never as a detector | Low | Rasters |
| H7 | untested | Control: GeoDAWN Area 1 / Area 2 flight-spec mosaic as a false-structure test | Low | Public shapefiles |
| H8 | untested | Inferred and blank-scale traces mark the edge of the map — not a positive class | Low | GeoDAWN clip |

**All are untested because the competition rasters are not placed in `data/`.** "Untested" means not measured, not
unexamined.

## H1 — Newly mapped geometry of existing systems

- **Layers:** label raster as mask only; bands 12, 19; bands 3, 6; 1 m lidar if placed.
- **Signature:** slope break or potential-field edge continuing past a digitised endpoint, running parallel within a few hundred metres, or diverging as a splay.
- **Why a gap:** staff 11536 — "new fault" means any pixel not already captured, and "can include newly mapped geometry of an existing fault system". Staff 11516 post 4 — new-fault ground truth can lie within 300 m of a known trace and "identifying these corrections is one outcome we are aiming for". Hermant et al. measure up to **400 m** catalogue misfit in north-central Nevada — larger than the 300 m kernel.
- **Expected DTI impact:** potentially highest of any card; but the mask is pixel-exact, so near-known-trace predictions far from new labels are **fully** penalised. Thickening range fronts is pure cost, not a hedge.
- **Validation:** contiguous-block spatial holdout. Baseline = the mask itself (zero by construction). Control = same probability mass at random azimuths along strike.
- **Rejection:** reject if the added corridor is dominated by ditches, irrigation lines, fan-channel margins or road embankments — i.e. if random-azimuth placement scores the same.

## H2 — Buried intra-basin structures under cover

- **Layers:** bands 13, 18, 11, 5; bands 2, 3, 6, 9; **band 15** as the stratifying variable. Not the label raster.
- **Signature:** linear gravity and/or magnetic gradient maxima beneath basins where depth-to-basement is large and surface slope is low.
- **Why a gap:** QFFD is defined by "coseismic surface deformation" in the past 1.6 Ma (USGS faults page); OF 93-338 says structures without Quaternary movement "will not be shown unless there is compelling evidence". A buried structure with no surface rupture is out of scope by design. About page: "many are hidden below the surface, requiring geophysical data to detect".
- **Expected DTI impact:** high if private labels include geophysical faults, harmful if lidar scarps only. Staff declined to say (11527 post 7) — size as a component, not the whole submission.
- **Validation:** condition every candidate on band 15; require gravity + magnetic conjunction; cross-check against H7.
- **Rejection:** reject where candidates align with survey or block boundaries (H7), or where a magnetic edge has no gravity counterpart over thin cover.

## H3 — 1 m lidar scarps absent from the compiled map

- **Status:** **blocked** — needs the data-tab CSV and the rasters.
- **Layers:** 1 m DEM from `1m_DEM_links.csv` (officially provided, not external); bands 12, 19 as coarse priors; label raster as mask.
- **Signature:** linear breaks-in-slope and curvature maxima, 1–10 m relief, persistent along strike, on piedmonts and playa margins; often invisible at 100 m.
- **Why a gap:** OF 93-338 preferred published topical studies at detailed scale. A scarp mappable only after 3DEP lidar could not have been compiled at the time. Hermant et al. built a new 1,100-fault label set for exactly this reason.
- **Expected DTI impact:** high if expert labels used lidar — likely, since the About page says 3DEP lidar was collected over a similar extent — but **unverified**. Confusers: ditches, shorelines, fan-channel margins, lithologic benches, fence/road lines, playa edges.
- **Extra constraint:** Hermant et al. found clean slope is only obtainable where the DEM is **lidar-derived**. Build a lidar-coverage mask first.
- **Rejection:** reject if candidates correlate better with drainage and road networks than with the catalogue's orientation distribution.

## H4 — Kinematic orphans

- **Layers:** bands 4, 7, 8, 16, 10; label raster as mask.
- **Signature:** elevated strain-rate invariant and/or earthquake density whose nearest catalogue pixel is > 300 m away.
- **Why a gap:** geodetic strain and seismicity are measured independently of publication. INGENIOUS compiled them as separate evidence layers; Kreemer & Young (2022) examine strain-versus-earthquake rates in the western US.
- **Expected DTI impact:** low standalone — smooth regional fields will spray false positives (α=0.2 is cheap but not free). Use as a spatial prior re-weighting H1–H3.
- **Cost:** low; everything is in the stack. Bands 10 and 16 share parameters (n=100 km, a=15°) — use one.
- **Validation:** quantile-bin 4, 7, 8, 10, 16; distance-to-nearest-label per bin. Monotonic decrease is the test.
- **Rejection:** reject as a standalone detector if distance-to-label does not decrease with strain quantile.

## H5 — Do not train to reproduce the raster the scorer removes

- **Layers:** all 19 bands; labels used only as the scoring mask and a near-trace hard-negative sampler.
- **Why a gap:** the reference solution trains a U-Net to reproduce the USGS/INGENIOUS raster; staff confirmed the scoring mask is identical to those labels, so perfect reproduction scores zero. Hermant et al. reached the same conclusion and built their own labels.
- **Expected DTI impact:** a necessary precondition, not a gain.
- **Cost:** medium — retraining. GPU recommended; the reference ships CPU and Apple-Silicon environments.
- **Validation:** two models identical except for the positive-class definition, evaluated on held-out geographic blocks with the pixel-exact mask. Also switch from the reference's random patch splits to contiguous spatial blocks.
- **Rejection:** reject the reformulation only if it scores no better than the catalogue-reproduction baseline on a spatial holdout.

## H6 — Conductivity as corroboration, not detection

- **Layers:** band 17; optionally the five depth-sliced conductance maps from <https://doi.org/10.5066/P9TWT2LU>.
- **Signature:** conductive lineament or shallow conductive base coincident with an H1–H4 candidate.
- **Why a gap:** fluids/clays/alteration along an unmapped structure raise conductance with no QFFD entry — but conductance is equally sensitive to basin fill, salinity and geothermal outflow.
- **Expected DTI impact:** small and positive as a multiplier; expected negative as a primary map (it lights up basin centres, exactly where Hermant et al. warn predictions are unreliable).
- **Validation:** candidate precision at matched recall with and without the multiplier, on a spatial holdout.
- **Rejection:** reject as a primary detector; reject as a multiplier if precision at matched recall does not improve.

## H7 — Control: the GeoDAWN flight-spec mosaic

- **Layers:** bands 3, 6, 9, 18; GeoDAWN survey-outline and flight-path shapefiles from <https://doi.org/10.5066/P93LGLVQ>.
- **Signature:** step change in apparent lineament density or gradient amplitude at the Area 1 / Area 2 boundary, or lineaments paralleling block boundaries, with no counterpart in gravity, DEM or catalogue.
- **Why a control:** Area 1 at 200 m lines versus Area 2 at 400 m, different clearances, four blocks, different contractors and aircraft. The USGS page warns that in steep terrain "variable terrain clearance should be considered when modeling and interpreting these data".
- **Cost:** low, and the only card startable without competition rasters — the shapefiles are public and CC0.
- **Validation:** overlay outlines on the gradient bands; test whether maxima cluster along boundary geometry more than under a random-orientation null.
- **Rejection:** if no boundary association is found, keep it as a passing control and stop spending on it. A clean result is a result.

## H8 — Inferred and blank-scale traces mark the edge of the map

- **Status:** untested. Regional counts are measured (CG-8). The GeoDAWN clip is not.
- **Layers:** `FTYPE_`, `MAPSCALE` on the NBMG 2023-06-27 service. Label raster as mask only, once placed.
- **Why a gap, not a known fault:** Inferred (5,280), Poor (100), Other (27) and blank FTYPE (447) traces are already in the compilation the scorer masks. Predicting them scores nothing. The gap is where those traces end, and where the survey has no trace. Not yet known to lie inside GeoDAWN.
- **Expected DTI impact:** harmful as a positive class. Useful only as a prior for H1 after the clip.
- **Rejection:** reject as a detector now. Reject as a prior if the clip shows negligible Inferred length inside the survey.

## Negative results

None yet — nothing has been run. This section exists so the first negative result has somewhere to live. Rejected
hypotheses stay on the page with their rejection reason and date, marked `rejected`. They are not deleted: "we tried
this and it did not work, here is the measurement" is evidence a Phase 2 reviewer respects.

## Recommended order once data land

1. **H7** — public shapefiles only; de-risks everything magnetic that follows. Can start today.
2. **H5's split fix** — contiguous spatial blocks before believing any score.
3. **H4 measurement** — one quantile-versus-distance table; half a day.
4. **H2 with band-15 conditioning** — highest-upside geophysical card; conditioning is free.
5. **H1** — highest expected value, and staff-endorsed; after mask behaviour is confirmed locally.
6. **H3** — highest cost, gated on lidar-coverage mapping.
