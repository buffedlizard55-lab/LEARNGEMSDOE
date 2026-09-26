# GEMSDOE research library

Knowledge base for the [Geologic Enhanced Mapping System (GEMS) Prize](https://www.drivendata.org/competitions/306/competition-doe-gems/) on **one** DrivenData entity and **this** GitHub repository.

This repository **researches and documents**. It does **not** generate, score-validate, or submit prediction GeoTIFFs.

## Site

GitHub Pages is served from `docs/`.

| Page | File |
| --- | --- |
| Overview | [docs/index.html](docs/index.html) |
| Explainer | [docs/executive-summary.html](docs/executive-summary.html) |
| Research library | [docs/research/](docs/research/) |
| Hypothesis backlog | [docs/hypotheses.html](docs/hypotheses.html) |
| Sources | [docs/sources.html](docs/sources.html) |
| AI-usage log (rules §3.2) | [docs/ai-usage.html](docs/ai-usage.html) |
| Changelog | [docs/changelog.html](docs/changelog.html) |

Markdown mirrors for later agents: [`research/`](research/).

## Official anchors (manual review)

- Hub: https://www.drivendata.org/competitions/306/competition-doe-gems/
- Problem: https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/
- About: https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/
- Rules PDF: https://www.nlr.gov/docs/fy26osti/96647.pdf
- Reference solution: https://github.com/drivendataorg/gems-prize-reference-solution
- Forum: https://community.drivendata.org/c/gems-prize-challenge/111
- GeoDAWN: https://doi.org/10.5066/P93LGLVQ
- INGENIOUS: https://doi.org/10.15121/1881483
- USGS QFFD: https://www.usgs.gov/programs/earthquake-hazards/faults · https://doi.org/10.5066/P9BCVRCK

## Data placement (training blocker)

```bash
bash scripts/download_competition_data.sh
python scripts/prepare_data.py
```

Competition rasters require DrivenData login. This environment cannot complete that download. After files are in `data/`, `prepare_data.py` only inventories them.

## Constraints

- No second site, repo, or DrivenData account.
- Re-confirm eligibility against [rules §1.3](https://www.nlr.gov/docs/fy26osti/96647.pdf) if the team changes.
- Extend research entries on re-run; do not duplicate.
