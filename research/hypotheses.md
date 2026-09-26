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
| H8 | untested | Inferred and blank-scale traces mark the edge of the map — not a positive class | Low | GeoDAWN clip (envelope version done: CG-9) |
| H9 | untested | Train against label *incompleteness*, not just label position | Med | Rasters + GPU |
| H10 | blocked | Rye Patch / western Humboldt Range as an independent lidar validation anchor | Low–med | Silver et al. 2011 mapping |
| H11 | untested | Soft confuser channels instead of hard negative classes | Low–med | External public layers |

**All are untested because the competition rasters are not placed in `data/`.** "Untested" means not measured, not
unexamined. Two cards are additionally **blocked** on their own inputs: H3 (needs the 1 m DEM links as well as the
rasters) and H10 (needs an external lidar fault mapping, independent of the competition data).

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

- **Status:** untested. Regional counts are measured (CG-8). **The envelope-clipped counts are now measured too (CG-9,
  2026-09-26):** inside the GeoDAWN bounding box the compilation holds 1,179 traces — Well Constrained 739, Moderately
  Constrained 351, Inferred 89, and **zero** Poor / Other / blank. The polygon clip is still missing.
- **Layers:** `FTYPE_`, `MAPSCALE` on the NBMG 2023-06-27 service. Label raster as mask only, once placed.
- **Why a gap, not a known fault:** Inferred (5,280 regionally, 89 in the box), Poor (100), Other (27) and blank FTYPE
  (447) traces are already in the compilation the scorer masks. Predicting them scores nothing. The gap is where those
  traces end, and where the survey has no trace.
- **What the census changed (inference, from CG-9's verified counts):** inside the box, Inferred is 7.5% of traces
  versus 23.0% regionally. If that survives the polygon clip, the GeoDAWN area is *better* mapped than the region as a
  whole, and H8's value shifts: it is less "here is a stock of poorly-constrained traces to extend" and more "the
  well-constrained traces here are the ones to trust positionally; the search should concentrate on geometry they do not
  contain at all" — i.e. cover-masked and subtle-scarps classes (CG-7 classes 2–3) over class 4.
- **Expected DTI impact:** harmful as a positive class. Useful only as a prior for H1 after the polygon clip.
- **Rejection:** reject as a detector now. Reject as a prior if the polygon clip shows negligible Inferred length inside
  the survey.

## H9 — Train against label incompleteness, not only label position

- **Status:** untested. Design hypothesis, so it can be specified now and measured as soon as rasters exist.
- **Layers:** all 19 bands; label raster used as the scoring **mask** and as a *noisy* positive set; no new external data.
- **Physical signature:** none — this is a training-target hypothesis, and it should be written as one.
- **Why it catches a gap rather than a known fault.** The QFFD is defined by demonstrable coseismic surface deformation
  in the past 1.6 Ma (CG-1); its compilers were told to prefer published, recent, detailed-scale studies (CG-2); and
  Hermant et al. report model-found faults in this region that experts then confirmed on lidar (GM-7). The label raster
  is therefore a *biased, incomplete sample* of the fault population, not the population. A model trained to reproduce
  it learns the catalogue's accessibility and publication biases — the inverse of the scored target. Hermant et al.
  propose exactly the countermeasures we propose here: "inform the model that any part of the study area may contain
  some faults, even if they are not present in the fault label", via an adversarial loss term or label noise (PA-7).
- **Expected DTI impact:** not measurable alone; it is the mechanism that lets H1–H3 candidates carry probability mass
  outside catalogue corridors. The asymmetry helps: α=0.2 prices a false positive at a quarter of a false negative, so
  the error this introduces is the cheap kind. Risk: label noise degrades the near-known-trace corrections that staff
  said they are aiming for (11516 post 4), which are the most valuable pixels there are.
- **Cost:** medium — one retrain, and a hyperparameter (noise rate or adversarial weight) that cannot be read off the
  data statistics.
- **Validation:** two models identical except for the incompleteness term, scored with `scripts/metrics.py` (α=0.2,
  β=0.8, R=300 m, pixel-exact mask) on **contiguous geographic blocks** held out. Because no private labels exist
  locally, measure three proxies: (1) share of predicted mass outside the 300 m corridor of known traces; (2) a
  hand-audit of 50 random high-probability non-catalogue pixels against 1 m lidar and imagery; (3) recall on
  deliberately withheld catalogue traces as a check that noise has not destroyed the ability to find faults at all.
- **Rejection:** reject if the added out-of-corridor mass is dominated by survey/block-boundary geometry (H7) or by
  GM-8's confuser list. Reject specifically as a *noise* method if withheld-trace recall falls faster than
  out-of-corridor precision rises.

## H10 — An independent lidar validation anchor at Rye Patch / western Humboldt Range

- **Status:** **blocked** — on obtaining the Silver et al. (2011) mapping, not on competition data.
- **Layers:** Silver et al. (2011) lidar-derived fault mapping (<https://doi.org/10.1130/GES00673.1>); bands 12, 19; the
  officially provided 1 m DEM; label raster as mask only.
- **Physical signature:** faults mapped from lidar in that study that are absent from, or displaced relative to, the
  USGS catalogue.
- **Why it catches a gap rather than a known fault.** It is an *independent* expert lidar mapping that predates this
  competition, inside the GeoDAWN bounding box — Figure 9 prints 40°36′ N and 117°36′–117°42′ W, Figure 8 prints
  40°30′–40°33′ N, and both sit inside the box recorded in CG-9. Running a
  candidate detector there and asking "did it recover faults the catalogue lacks?" is a genuine out-of-sample test of
  gap-finding behaviour that costs no submission slot and touches no private label.
- **Expected DTI impact:** none directly. Its job is to de-risk H1 and H3 by giving them a local truth set before any
  scoring budget is spent.
- **Cost:** low to medium, entirely gated on whether the mapping is distributed.
- **Validation:** treat Silver et al.'s lidar faults as truth; score detectors with `scripts/metrics.py` under two
  masks — the catalogue (what we have) and the catalogue plus Silver (what a better catalogue looks like). A detector
  whose score improves sharply under the second mask is finding real un-catalogued faults, not artefacts.
- **Rejection:** reject as an anchor if the mapping is not obtainable, or if its footprint falls outside the actual
  GeoDAWN flight lines rather than merely outside the bounding box.
- **Open risk:** neither the paper nor any accompanying data has been obtained. It is a lead (PA-8), not an asset.

## H11 — Soft confuser channels, not hard negative classes

- **Status:** untested.
- **Layers:** drainage/channel network and pluvial-shoreline elevations as continuous channels (external, public);
  bands 12, 19 for the candidate set; label raster as mask only.
- **Physical signature:** a candidate lineament that coincides with a channel margin or with a paleo-shoreline elevation
  contour.
- **Why it catches a gap rather than a known fault.** Hermant et al. measured paleo-shorelines, canyon boundaries and
  stream boundaries being detected *as* faults in this terrain — and warned that a dedicated confuser class "may
  therefore miss some of these co-located structures", because "faults can be co-located with a paleo-shoreline … or
  with a canyon boundary" (GM-8). A soft channel suppresses the confuser without deleting the fault that happens to run
  along it, which is the case a geologist would most want kept.
- **Expected DTI impact:** small and positive — precision at matched recall, with the false-positive term priced at
  α=0.2. Not a headline gain; a way to spend less of the audit budget on ditches.
- **Cost:** low to medium; the layers are public, the engineering is a channel concatenation.
- **Validation:** precision at matched recall on a contiguous-block holdout, with and without the channels; plus an
  explicit check that candidates co-located with mapped faults are *not* suppressed (that is the failure mode Hermant
  et al. warn about).
- **Rejection:** reject if precision at matched recall does not improve, or if it removes H1 near-trace correction
  candidates — the most valuable pixels in the whole submission.

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
7. **H10 in parallel, from day one** — it needs no competition data. If Silver et al. (2011)'s mapping is obtainable, it
   converts every later "is this a real gap?" argument into a measurement.
8. **H9 with the first real train** — it is a flag on the training run, not a separate project. Do it while the GPU is
   already warm for H5.
9. **H11 last** — a precision tidy-up, only worth doing once there is something worth tidying.
