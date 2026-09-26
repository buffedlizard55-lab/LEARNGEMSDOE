# PROJECT_BRIEF — GEMSDOE research & knowledge base

**Status.** This file was **not present** in the repository when the first session started (2026-09-26). It is
reconstructed from the session mission and extended each session so later passes are resumable. It is **not** an
official DrivenData or DOE document.

**Entity.** One existing GitHub repository (`buffedlizard55-lab/LEARNGEMSDOE`) and one registered DrivenData competitor.
Do **not** create a second site, repo, account, or registration — including for staging.

## What this project is

A research library and hypothesis engine for the
[Geologic Enhanced Mapping System (GEMS) Prize](https://www.drivendata.org/competitions/306/competition-doe-gems/).
The scored target is **faults absent from the existing USGS / INGENIOUS catalogue** in the GeoDAWN area — not a replay of
known traces.

This work **researches and documents**. It does **not** generate, score-validate, or submit prediction files. Weekly
submission slots are not used by this agent. Submission generation remains a separate, explicitly gated process.

## Verified source anchors

| Role | URL |
| --- | --- |
| Competition hub | https://www.drivendata.org/competitions/306/competition-doe-gems/ |
| Problem description | https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/ |
| About / resources | https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/ |
| Data tab (login required) | https://www.drivendata.org/competitions/306/competition-doe-gems/data/ |
| DrivenData rules page | https://www.drivendata.org/competitions/306/competition-doe-gems/rules/ |
| Official rules PDF (NLR primary) | https://www.nlr.gov/docs/fy26osti/96647.pdf |
| HeroX rules resource | https://www.herox.com/GEMSPrize/resource/2274 |
| Reference solution | https://github.com/drivendataorg/gems-prize-reference-solution |
| Forum | https://community.drivendata.org/c/gems-prize-challenge/111 |
| Feature-data citation | Glen & Earney, 2024 — https://doi.org/10.5066/P93LGLVQ |
| GeoDAWN USGS data page | https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and |
| GeoDAWN ScienceBase item | https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7 |
| Label citation | Ayling et al., 2022 — https://doi.org/10.15121/1881483 |
| INGENIOUS GDR record | https://gdr.openei.org/submissions/1391 |
| USGS QFFD (current official page) | https://www.usgs.gov/programs/earthquake-hazards/faults |
| USGS QFFD citation DOI | https://doi.org/10.5066/P9BCVRCK |
| USGS QFFD interactive map | https://doi.org/10.5066/F7S75FJM |
| QFFD 1993 compilation guidelines | https://pubs.usgs.gov/of/1993/0338/report.pdf |
| Hermant et al., 2025 | https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf |
| Mattéo et al., 2021 | https://doi.org/10.1029/2020JB021269 |
| Kreemer et al., 2022 | https://doi.org/10.1785/0220220153 |
| Miller & Singh, 1994 (tilt) | https://doi.org/10.1016/0926-9851(94)90022-1 |
| Verduzco et al., 2004 (THDR) | https://doi.org/10.1190/1.1651454 |

## Mission

Continuously research, organise and document everything relevant to identifying faults absent from the existing
USGS / INGENIOUS catalogue in the GeoDAWN area, and turn that into a rich, navigable, source-linked section of the
existing site. A knowledge-and-hypothesis engine that makes the next modelling decision smarter — not a submission
generator.

## Research domains

1. **Potential-field geophysics** — magnetic (RTP, TMI, gradients), isostatic gravity, gradient magnitude and
   tilt-derivative methods for lineament / edge detection, and what they imply about buried structural contrasts.
2. **DEM-based structural geomorphology** — curvature and breaks-in-slope for scarp detection; what a subtle or
   partially-buried scarp looks like in this terrain specifically.
3. **Seismotectonics and strain** — strain-rate tensor invariants, earthquake density, conductivity anomalies; where
   independent signals agree versus disagree.
4. **Catalogue-gap reasoning** — the highest-leverage domain. Read the INGENIOUS compilation's and USGS database's own
   *methodology*, not just their output rasters: how were existing faults actually mapped (field campaigns,
   remote-sensing passes, terrain and access constraints)? Reason about where the catalogue is structurally likely to be
   incomplete — sparse historical fieldwork, younger cover masking scarps, remote terrain — rather than only asking what
   looks fault-like. This is the actual scored target.
5. **Prior art** — published fault / lineament-extraction ML work applicable to this feature stack; the reference
   solution's specific design choices and where they likely fall short.
6. **Competition governance** — rules PDF, forum threads, official errata, anything time-sensitive.

## Entry standard

Every research entry needs: source link, direct citation (prefer the primary DOIs above over secondary summaries), what
it claims, why it is relevant here, and a confidence note. Anything that cannot be traced to a primary or clearly
authoritative source is marked `unverified` or `inference` — never presented as fact.

## Hypothesis backlog

Per hypothesis: layer(s), physical signature, specific reasoning for why it should catch a catalogue gap rather than a
known fault, expected DTI impact, cost, and status (untested / validated on spatial holdout / rejected + why). Negative
results are included. Phase 2 is scored by geologists reading exactly this reasoning — write it for that reader.

## Compliance logging

Rules §3.2 requires disclosing, in the submission narrative, the extent generative AI was used, and flags fabrication,
falsification and plagiarism as AI-specific risks the competitor owns. `research/ai-usage-log.md` and
`docs/ai-usage.html` are maintained incrementally, session by session, as first-class site artefacts — never
reconstructed at deadline time.

## Site build

GitHub Pages from `docs/`: a research library by domain, a hypothesis backlog with visible status, a dated changelog,
the AI-usage log, a feature-stack inventory, and links back to the executive-summary / submission-explainer pages. Depth
and traceability over decoration.

## Hard constraints

- No hallucinated sources, numbers, or citations, ever.
- No submission generation or weekly-slot use from this agent.
- No second site, repo, account, or registration, including for staging.
- Flag irregularities rather than smoothing over them.
- Re-confirm eligibility against rules §1.3 if team composition or affiliations change.

## Operating model

Designed for unattended, resumable operation. Checkpoint after each pass — commit plus a short structured log entry
(added / changed / what's next) — so an interrupted run leaves a clean, resumable state. Each pass is idempotent:
re-running extends existing entries rather than duplicating them.

End of each session, report: what was added and where, hypothesis backlog and status, what is still unverified, what is
blocking progress, and the single highest-value next research question.

## Current blockers (as of 2026-09-26, session arena/01a0df77)

1. **Competition rasters are not in `data/`** — the data tab requires a DrivenData login (re-confirmed redirect).
   No hypothesis can move from `untested` until they are placed and `prepare_data.py` is run. No account was created.
2. **Public binary downloads also failed from this machine** — TLS handshake to sciencebase.gov, gdr.openei.org and
   usgs.gov returned `SSL_ERROR_SYSCALL`. The files are listed; they were not fetched. Do not treat that as absence.
3. **No training or inference code** — deliberately. A prior handoff claimed a complete train→inference→validate
   pipeline was ready to run; it is not present, and the discrepancy is flagged on `docs/pipeline.html`. Re-checked.
4. **Unanswered forum questions** — re-read 2026-09-26, still unanswered: 11540, 11526, 11543, and 11499's eligibility
   question.
5. **Unread sources** — the INGENIOUS Qfaults v2 field-definition *text* (field names and counts were read from the
   NBMG MapServer instead; see CG-8); Hermant 2025 PDF chunks 4–7; the body of Mattéo et al. 2021; two paywalled
   potential-field methods papers.
6. **GeoDAWN clip not run** — the highest-value next measurement. Outline zips are on ScienceBase (1,190 and 1,497
   bytes) but were not downloaded.
