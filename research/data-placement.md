# Data placement attempt — 2026-09-26

Session `arena/01a0df46-learngemsdoe`. This file records what was run. It is not a claim that rasters are present.

## Commands

```text
bash scripts/download_competition_data.sh   # exit 2
python3 scripts/prepare_data.py             # exit 2, status blocked_no_data
python3 scripts/metrics.py --selftest       # exit 0, 11 checks passed, pure Python
```

## Two blockers, not one

1. **Login wall (verified by page fetch, not by curl).**  
   `https://www.drivendata.org/competitions/306/competition-doe-gems/data/` redirected to the DrivenData login page. No account was created. No credentials were stored.

2. **TLS failure from this machine (verified by curl).**  
   `curl` to `www.drivendata.org`, `www.sciencebase.gov`, and `gdr.openei.org` exited 35 (`SSL_ERROR_SYSCALL`) before any HTTP response. The download script therefore could not observe the login redirect itself. That does not erase the page-fetch result in item 1, and it does not mean the public files are missing.

## Public files attempted and not saved

| File | Listed size | Result |
| --- | --- | --- |
| `GeoDAWN_area1_outline.zip` | 1,190 bytes (ScienceBase JSON) | curl exit 35 |
| `GeoDAWN_area2_outline.zip` | 1,497 bytes | curl exit 35 |
| `GeoDAWN_data_extent.zip` | 2,774 bytes | curl exit 35 |
| `qfaults_ingenious_nad83conus117_2023-06-27.zip` | 5.85 MB (GDR page) | curl exit 35 |

`prepare_data.py` wrote `data/inventory.json` with `status: blocked_no_data` and the five documented names missing. That file is gitignored. No GeoTIFF was created.

## What was measured without those files

The NBMG map service was queried through a fetch path that can read JSON even when curl cannot complete TLS. Counts are on [docs/requirements.html](../docs/requirements.html#catalogue). They are not a substitute for the competition rasters.

## Re-run — 2026-09-26, session `arena/01a0dfd3`

- Sandbox: `download_competition_data.sh` → curl exit 35 on all four public files; `prepare_data.py` → exit 2,
  `blocked_no_data`. Data tab re-fetched → login redirect.
- **GitHub Actions runner** ([run](https://github.com/buffedlizard55-lab/LEARNGEMSDOE/actions/runs/36276586563)): all four public files downloaded — 1,190 / 1,497 / 2,774 / 6,131,182 bytes,
  matching the ScienceBase and GDR listings. Footprint census in CG-12. Files are not committed (gitignored, runner-only).
- Competition rasters: still require the registered account's login. Not attempted beyond the probe.
