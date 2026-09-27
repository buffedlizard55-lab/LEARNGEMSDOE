# GEMSDOE — GEMS Prize research library

Knowledge base and hypothesis backlog for the
[Geologic Enhanced Mapping System (GEMS) Prize](https://www.drivendata.org/competitions/306/competition-doe-gems/),
maintained under **one** registered DrivenData entity and **this** repository only.

The scored target is faults that are **absent** from the USGS / INGENIOUS catalogue in the GeoDAWN area — not a replay of
known traces. This repository **researches and documents**. It does **not** generate, score-validate, or submit
prediction GeoTIFFs, and it does **not** use weekly submission slots.

## Site

GitHub Pages is published at <https://buffedlizard55-lab.github.io/LEARNGEMSDOE/>.

**Two deploy paths are configured, and that is worth knowing.** `.github/workflows/pages.yml` uploads `docs/` on every
push to `main`, while the repository's Pages setting is still the legacy "build from the `main` branch, path `/`" — which
is the one currently serving, so live URLs carry a `/docs/` segment (the root `index.html` redirects there). Both work,
because every link in the site is relative. If you would rather the site be served at the bare subpath, switch
**Settings → Pages → Source** to **GitHub Actions**; that is a repository-owner action (an integration token cannot
change it) and it is the one manual step left in the site setup.

| Page | File | What it holds |
| --- | --- | --- |
| Overview | [docs/index.html](docs/index.html) | Reading order, competition facts table, what is scored, domain index, flagged irregularities, how the site checks itself |
| Search | [docs/search.html](docs/search.html) | One box over every research entry, hypothesis card and page; generated index |
| Explainer | [docs/executive-summary.html](docs/executive-summary.html) | Geologist-facing narrative of the problem |
| Requirements | [docs/requirements.html](docs/requirements.html) | Full checklist: constraints, re-read facts, counted catalogue attributes, open items |
| Research library | [docs/research/](docs/research/) | Six domains, 79 numbered entries, each with source / citation / claim / relevance / confidence |
| Feature stack | [docs/feature-stack.html](docs/feature-stack.html) | All 19 bands, raster geometry, GeoDAWN acquisition, missing layers, pitfalls |
| Hypothesis backlog | [docs/hypotheses.html](docs/hypotheses.html) | H1–H15 cards (H8 and H13 rejected; H15 partially validated on synthetic tiles) with layers, signature, gap reasoning, expected DTI impact, cost, validation, rejection |
| Sources | [docs/sources.html](docs/sources.html) | Every source, with what was read and what remains unverified |
| Pipeline | [docs/pipeline.html](docs/pipeline.html) | Data-placement blocker, what runs today, the submission gate |
| Governance | [docs/research/governance.html](docs/research/governance.html) | Rules section by section, staff clarifications, open questions |
| Forum watch | [docs/forum.html](docs/forum.html) | Unanswered threads with JSON links, re-read each session |
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
python3 scripts/public_census.py            # footprint clip of public INGENIOUS faults (needs pyshp shapely pyproj)
```

Competition rasters require a DrivenData login, so they are not in this repository and cannot be fetched from here.
After files are in `data/`, reconcile `data/inventory.json` against [docs/feature-stack.html](docs/feature-stack.html)
and correct that page if they disagree.

## What runs today, with no competition data

```bash
python3 scripts/metrics.py --selftest            # 11 numeric checks, CPU, standard library only
python3 scripts/metrics.py --demo                # worked example as JSON
python3 scripts/placement_check.py               # dense vs node emission under our metric — synthetic, prints JSON
python3 scripts/rasterize_catalogue.py           # stamps public catalogues onto the 100 m grid (needs pyshp shapely pyproj + public files)
python3 scripts/check_site.py                    # links, anchors, assets, source allowlist — offline
python3 scripts/build_search_index.py            # regenerate the search index
python3 scripts/build_search_index.py --check    # fail if the committed index is stale
```

**Public data via GitHub Actions.** `.github/workflows/public-data.yml` downloads the *public* GeoDAWN outlines and
INGENIOUS Qfaults v2 on a GitHub runner (manual `workflow_dispatch`, or on push to `arena/**` when the census files
change) and publishes the footprint census as run annotations. It never touches the login-gated competition data and
uses no secrets. Results: `docs/research/catalogue-gaps.html#cg12`.

`scripts/check_site.py` enforces part of the no-hallucinated-sources rule mechanically: every external link anywhere on
the site must also appear on [docs/sources.html](docs/sources.html), or the check fails. It fetches nothing.
`scripts/build_search_index.py` regenerates `docs/assets/search-index.js` from the markdown mirrors, and its `--check`
mode fails if the committed index has drifted. Both run in CI on every push and pull request.

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
