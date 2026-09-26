# GEMSDOE — GEMS Prize research library

Knowledge base and hypothesis backlog for the
[Geologic Enhanced Mapping System (GEMS) Prize](https://www.drivendata.org/competitions/306/competition-doe-gems/),
maintained under **one** registered DrivenData entity and **this** repository only.

The scored target is faults that are **absent** from the USGS / INGENIOUS catalogue in the GeoDAWN area — not a replay of
known traces. This repository **researches and documents**. It does **not** generate, score-validate, or submit
prediction GeoTIFFs, and it does **not** use weekly submission slots.

## Site

GitHub Pages is served from `docs/` (the workflow deploys on push to `main`).

| Page | File | What it holds |
| --- | --- | --- |
| Overview | [docs/index.html](docs/index.html) | Competition facts table, what is scored, domain index, flagged irregularities |
| Explainer | [docs/executive-summary.html](docs/executive-summary.html) | Geologist-facing narrative of the problem |
| Research library | [docs/research/](docs/research/) | Six domains, 40 numbered entries, each with source / citation / claim / relevance / confidence |
| Feature stack | [docs/feature-stack.html](docs/feature-stack.html) | All 19 bands, raster geometry, GeoDAWN acquisition, missing layers, pitfalls |
| Hypothesis backlog | [docs/hypotheses.html](docs/hypotheses.html) | H1–H7 cards with layers, signature, gap reasoning, expected DTI impact, cost, validation, rejection |
| Sources | [docs/sources.html](docs/sources.html) | Every source, with what was read and what remains unverified |
| Pipeline | [docs/pipeline.html](docs/pipeline.html) | Data-placement blocker, what runs today, the submission gate |
| Governance | [docs/research/governance.html](docs/research/governance.html) | Rules section by section, staff clarifications, open questions |
| Changelog | [docs/changelog.html](docs/changelog.html) | Dated, append-only |
| AI-usage log | [docs/ai-usage.html](docs/ai-usage.html) | Rules §3.2 compliance record |

Markdown mirrors (for git review and agent continuity): [`research/`](research/).

## Official anchors — open these to check the work

- Competition hub — <https://www.drivendata.org/competitions/306/competition-doe-gems/>
- Problem description — <https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/>
- About / resources — <https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/>
- Rules page — <https://www.drivendata.org/competitions/306/competition-doe-gems/rules/>
- Official rules PDF (NLR, September 2026) — <https://www.nlr.gov/docs/fy26osti/96647.pdf>
- Reference solution — <https://github.com/drivendataorg/gems-prize-reference-solution>
- Forum — <https://community.drivendata.org/c/gems-prize-challenge/111>
- GeoDAWN — <https://doi.org/10.5066/P93LGLVQ> · <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and>
- INGENIOUS — <https://doi.org/10.15121/1881483> · <https://gdr.openei.org/submissions/1391>
- USGS QFFD — <https://www.usgs.gov/programs/earthquake-hazards/faults> · <https://doi.org/10.5066/P9BCVRCK>

## Data placement — the training blocker

```bash
bash scripts/download_competition_data.sh   # prints official URLs, checks data/, never logs in
python scripts/prepare_data.py              # writes data/inventory.json — inspection only
```

Competition rasters require a DrivenData login, so they are not in this repository and cannot be fetched from here.
After files are in `data/`, reconcile `data/inventory.json` against [docs/feature-stack.html](docs/feature-stack.html)
and correct that page if they disagree.

## What runs today, with no competition data

```bash
python3 scripts/metrics.py --selftest   # 11 numeric checks, CPU, standard library only
python3 scripts/metrics.py --demo       # worked example as JSON
```

`scripts/metrics.py` implements the official distance-weighted Tversky index (α=0.2, β=0.8, R=300 m), a Tversky loss,
and a pixel-exact masked variant matching the staff-confirmed scoring mask. It has one documented assumption: distances
are measured **centre-to-centre** in metres, the only convention under which "3 pixels at 100 m" equals 300 m.

There is deliberately **no** training script and **no** inference script that emits a submission GeoTIFF — see
[docs/pipeline.html](docs/pipeline.html) for the gate and for why a previous handoff claim about a complete pipeline was
flagged as inaccurate.

## Constraints

- One entity, one repository, one site. No second site, repo, account or registration, including for staging.
- No hallucinated sources, numbers or citations. Anything not traceable to a primary or clearly authoritative source is
  marked `unverified` or `inference` where it appears.
- Irregularities are flagged, not smoothed over — see the list on the overview page.
- Re-confirm eligibility against [rules §1.3](https://www.nlr.gov/docs/fy26osti/96647.pdf) if team composition or
  affiliations change.
- Extend research entries on re-run; never duplicate them. Append to the changelog and the AI-usage log every session.
