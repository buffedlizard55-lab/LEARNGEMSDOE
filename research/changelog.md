# Changelog

Canonical HTML: [`docs/changelog.html`](../docs/changelog.html)

## 2026-09-26

**Added:** GitHub Pages research site (`docs/`), `PROJECT_BRIEF_GEMSDOE.md`, domain entries, hypotheses H1–H7 (all untested), `scripts/download_competition_data.sh`, `scripts/prepare_data.py`.

**Changed:** replaced stub README.

**Next:** read forum 11527 in a browser; place DrivenData rasters; unpack INGENIOUS Qfaults v2 field definitions; finish NLR PDF appendix.

## 2026-09-26 (session arena/01a0df09-learngemsdoe) — Pass 1–3 verification + fixes

**Verified against primary sources (live fetches):** NLR rules PDF (§1.1, §1.3, §2, §3.2–§3.6, §A.1, §A.13), DrivenData hub + problem page 967 + about 968, USGS QFFD page, GeoDAWN ScienceBase item, INGENIOUS GDR record, Hermant 2025 Stanford PDF, Mattéo 2021 (JGR), Kreemer & Young 2022 (SRL), and forum threads 11516 / 11527-7 / 11536.

**Fixed:**
- Tightened the "pixel-exact scoring mask" wording (index, executive-summary, governance GV-5, catalogue-gaps banner): staff 11516 confirms known faults are masked/excluded, but did not explicitly state pixel-exact vs. buffered; the 300 m kernel is for new-fault ground-truth distance, not a known-fault buffer. "Pixel-exact" is now labeled an inference.
- Corrected the weekly-cap citation: "three per week" is the rules (§3.2/§3.4); "rolling window" is forum 11524.

**Upgraded confidence:** CG-2 (OF 93-338 rules verified verbatim), CG-4 / PA-3 (Hermant 1,100 faults / 264 km, 50 m buffer, 10 m lidar 3DEP, B8A vegetation band, geographic half split all confirmed in the PDF).

**Confirmed accurate, no change:** $300k prize structure; metric α=0.2, β=0.8, R=300 m and the 0.60 worked example; deadline Dec 3 2026, 11:59 p.m. UTC; §3.3 INGENIOUS labels; §A.13 program-policy factors; GeoDAWN 149,030 line-km / 51,857 km² and Area 1/2 flight specs; QFFD 1.6 Ma coseismic-surface-deformation design.

**What's next:** place competition rasters + run `prepare_data.py`; unpack INGENIOUS Qfaults v2 field-definition readme; open Miller 1994 / Verduzco 2004 PDFs (cited, not yet read); watch unanswered eligibility threads 11540 / 11526 / 11543.
