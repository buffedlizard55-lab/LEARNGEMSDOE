# Competition governance

Canonical HTML: [`docs/research/governance.html`](../docs/research/governance.html)

The rules PDF was read in full this session — all seven chunks, §1.1 through §A.17.

Primary: <https://www.nlr.gov/docs/fy26osti/96647.pdf> (September 2026)

## GV-1 · Eligibility: the homepage is shorter than the rules

**Homepage:** individual competitors must be US citizens or permanent residents; team captain must be a US citizen or
permanent resident; private entities must be US-incorporated with a US primary place of business; federal entities and
federal employees ineligible.

**Rules §1.3 adds:**
- "Individuals competing as part of a team are eligible to participate if they are **legally authorized to work in the United States**."
- "Academic institutions must be based in the United States and accredited by a nationally recognized accrediting agency or association."
- FFRDCs may not compete; individual FFRDC researchers may compete in their individual capacities if no FFRDC resources are used, but "may receive an honorable mention [and] are not eligible to receive any cash prizes".
- Ineligible: non-DOE federal entities and federal employees; DrivenData officers, employees, judges and their households; DOE employees and support contractors; debarred parties; under-18s; individuals in a Malign Foreign Talent Recruitment Program of a foreign country of concern; entities owned or controlled by such a government. DOE defines foreign countries of concern as including Iran, North Korea, Russia, Belarus and China, "subject to change".
- Registration requires certifying under penalty of perjury (18 U.S.C. §1001 and §287; 31 U.S.C. §§3729–3733 and 3801–3812).

**Open questions (all unanswered at 2026-09-26):**
- 11540 <https://community.drivendata.org/t/team-member-eligibility-competition-homepage-vs-official-rules/11540> — must non-captain members be US-work-authorised?
- 11526 <https://community.drivendata.org/t/institutional-limit/11526> — one final submission per team or per organisation / UEI?
- 11499 <https://community.drivendata.org/t/about-the-gems-prize-challenge-category/11499> — may a team mix one US resident and one non-US resident?

**Action:** re-confirm against §1.3 before any change in team composition or affiliation. Conservative reading: §1.3
governs.

## GV-2 · Generative AI must be disclosed (§3.2)

Verbatim: "Using generative AI technology in the development of your prize submission is allowed. However, you must
**indicate in the narrative** (not included in the word count) the extent to which, if any, you used generative AI
technology and how you used it to develop your submission … You are responsible for the accuracy, authenticity, and
authorship representations of your submission … Relying on generative AI may introduce significant risks, including but
not limited to, research misconduct resulting from **fabrication, falsification, or plagiarism**…"

Also from §3.2: finalists must submit complete code assets and documentation, including the resources required to build
and run the solution, sufficient to reproduce the winning results, consistent with DrivenData's Winning Model
Documentation Template.

## GV-3 · Submission mechanics

- Three scored submissions per week (§3.2, §3.4); allowance resets on a **rolling window**, not a calendar week (11524).
- One final submission for both rounds; multiple finalised submissions not allowed; team members may not submit separately (§3.4).
- You choose blind: "You must make your decision without knowledge of your scores on the private test set" (§3.6.2).
- Public leaderboard scores "may not be the same as the final scores"; the public/private fault weighting is set by the organisers before the competition (§3.2, §3.6.2).
- Winners notified ~60 days after close (§3.6.5); optional DOE interviews (§3.6.3); a DOE Federal employee is the judge (§3.6.4, A.15).

## GV-4 · External data

Verbatim: "Participants are allowed to use any additional data sources, provided that the participants possess a
license that permits the data to be used in this challenge **and shared with the sponsor for evaluation purposes**."
Staff reaffirmed this in 11528 in answer to a question about subscription-only data. GeoDAWN is CC0 1.0; INGENIOUS is
CC BY 4.0 — both satisfy the condition.

## GV-5 · The scoring mask is pixel-exact (**corrected this session**)

Staff post 4 of 11516, 2026-09-21 — <https://community.drivendata.org/t/scoring-clarification-are-known-usgs-ingenious-faults-masked-when-scoring-and-are-they-in-the-final-round-label-set/11516/4>:

1. "The mask is indeed **pixel-exact** — it is identical to the provided set of training fault labels."
2. "Only new-fault ground truth is considered for scoring purposes. A predicted pixel that is near a known fault trace but far from a new-fault ground truth pixel will be **fully penalized**, i.e., the buffer does not apply to known faults."
3. "A new-fault ground truth pixel **can indeed lie within 300m of a known fault trace**. Such pixels would constitute corrections or modifications to existing fault traces. Identifying these corrections is one outcome we are aiming for as part of this competition."

Earlier, post 2: known-fault pixels are masked in both rounds, and "for scoring purposes it should not matter whether
these known faults are included with predictions or not".

**Previous session's hedge ("pixel-exactness not stated by staff") is now resolved and removed.**

## GV-6 · What counts as a new fault

Verbatim (11536): "For the purposes of this competition, 'new fault' means 'any fault pixel not already captured by
USGS/INGENIOUS' and can include newly mapped geometry of an existing fault system." Covers continuations past mapped
endpoints, splays and parallel strands.

## GV-7 · Test-fault provenance will not be published

Verbatim (11527 post 7): "We're not sharing details about the data sources, fault types, or coverage behind the test
faults beyond what's in the problem description. Note that the largest prize pool (Phase 2) will use a test set that is
updated by expert review of all Phase 1 submissions, so your fault predictions have an impact on final evaluation even
if they are not the most performant in Phase 1."

Rules §2 does state *who* labelled them: "geology experts at the National Laboratory of the Rockies (NLR) and USGS".

## GV-8 · Deadline conflict

- Hub: "Dec. 3, 2026, 11:59 p.m. UTC"
- Rules §A.1: "by **5:00 p.m. ET** on the prize submission deadline date"; also "Late submissions or any other form of submission may be rejected".
- Rules §1.2 punts to the competition website for "the most current timeline".

**Flagged, not resolved.** No forum thread found. Operate on the earlier instant. The rules PDF's own change-log table
was empty when read.

## GV-9 · Other provisions worth knowing

- §A.4: public elements must not contain trade secrets or confidential information; DOE gets an unlimited licence to display and use them; confidential material needs the prescribed notice on every page and double brackets around every line.
- §A.10: submission materials become DOE records subject to FOIA; competitors notified under 29 C.F.R. §70.26.
- §A.2: winners must return an NLR ACH form and IRS W-9 within 30 days of notice; failure can mean no funds. §A.3: a single amount goes to the designated primary submitter, who allocates it; DOE will not arbitrate.
- §A.13 program policy factors (alongside reviewer scores): DOE/administration policy priorities; geographic diversity and economic impact; non-duplication with existing DOE funding; technological or programmatic diversity; likely US employment/manufacturing benefit; acceleration of advances industry would not undertake alone; support for complementary DOE-funded efforts; expanding to new recipients; enabling new market segments.
- §A.12: "DOE may conduct a risk review … for potential risks of foreign interference … An elimination based on a risk review is not appealable." And: "If, in DOE's determination, no competitors are likely to achieve the goals of the program, DOE will select no competitors to be winners and will award no prize money."
- §1.1: Phase 1 $50,000 split equally among the top five; Phase 2 $100,000 / $70,000 / $40,000 / $25,000 / $15,000; "up to 10 awards".
- §2: competitors "are strongly encouraged to form multidisciplinary teams that include expertise in data science and geosciences".

## Watch list

| Item | Thread | State at 2026-09-26 |
| --- | --- | --- |
| Non-captain work authorisation | 11540 | unanswered |
| One submission per team vs per organisation / UEI | 11526 | unanswered |
| Teammate interpretation as training labels | 11543 | unanswered |
| Team mixing US and non-US residents | 11499 | unanswered |
| Deadline conflict | §A.1 vs hub | no thread found |
| Test-fault provenance | 11527 post 7 | declined by staff |
| Rules change-log table | PDF Preface | empty when read; **re-read 2026-09-26, still empty** |
| Staff about-post links to page 966 | https://www.drivendata.org/competitions/306/competition-doe-gems/page/966/ | duplicate of the hub welcome, not page 967 |
| Rules PDF host | https://www.nlr.gov/docs/fy26osti/96647.pdf | redirects to docs.nlr.gov (re-fetched 2026-09-26) |
| §1.2 key dates | rules PDF vs hub | PDF defers to the website; **cite the hub for the deadline, not the PDF** (GV-11) |
| Submission extent | §3.2 vs problem description | "entirety of the GeoDAWN study area" vs "same bounds as the training data" — **unresolved until the raster is placed** (GV-12) |
| GeoDAWN contents | §2 vs Glen & Earney 2024 | rules call it a "lidar, magnetic, and radiometric study"; the release is magnetic/radiometric with 3DEP lidar as a separate coordinated collection (GV-13) |
| USGS vs INGENIOUS trace counts | CG-15 / CG-16 | 5,570 USGS sections vs 413 INGENIOUS traces for the same ~6,230 km inside the footprint — granularity, not content. Do not quote "413 traces" as the catalogue |
| USGS QFFD GIS file size | <https://www.usgs.gov/programs/earthquake-hazards/faults> | page says 16 MB; the file served is 32,371,696 bytes (measured 2026-09-26). Unresolved |
| Problem-description feature list vs band tags | GV-17 | two layers named in the description have no band tag; two band tags are absent from the description |

## GV-11 · Rules and forum re-read, 2026-09-26 (session `arena/01a0df88`)

- **Source:** rules PDF <https://www.nlr.gov/docs/fy26osti/96647.pdf> (served from `docs.nlr.gov` after redirect),
  chunks covering the Preface, §1.1–§1.4, §2 and §3.1–§3.2; forum category JSON
  <https://community.drivendata.org/c/gems-prize-challenge/111.json> (both chunks).
- **Claim — nothing has changed.** The Preface change-log table still has five empty rows: no recorded amendment since
  the September 2026 version was published. The forum holds **11 topics**; the newest is **11543 (2026-09-25)**, i.e.
  no new topic since the previous session's re-read a few hours earlier. `posts_count` is unchanged at 1 for 11543,
  11540 and 11526, and 2 for 11499 (the pinned "About" post plus one unanswered eligibility question).
- **Newly recorded — §1.2 does not restate the deadline (verbatim):** "Please see the competition website
  gems.drivendata.org for the most current timeline and important dates." Consequence: the **3 December 2026,
  11:59 p.m. UTC** deadline must be cited to the
  [DrivenData hub](https://www.drivendata.org/competitions/306/competition-doe-gems/), **not** to the rules PDF. The
  prize amounts in §1.1 and the hub agree, so the PDF is still the authority for money, not for dates.
- **Newly recorded — §3.2 restates the submission cap and the AI disclosure in the same section (verbatim):** "You can
  make multiple submissions, subject to the limits specified on the competition website (three submissions per week)."
- **Eligibility re-confirmed against the text (§1.3).** The eligible-entity list, the FFRDC carve-out, the federal
  employee exclusion, the MFTRP / FCOC exclusions and the perjury certification statement were all re-read this session
  and are unchanged. **No team-composition or affiliation change was recorded**, so this is a re-confirmation against
  the rules text only, not a verification of any particular team. It must be re-run the moment membership or
  affiliation changes.
- **Confidence:** verified for all of the above, read this session.

## GV-12 · Open wording difference: "the entirety of the GeoDAWN study area" vs "the same bounds as the training data"

- **Sources:** rules §3.2 <https://www.nlr.gov/docs/fy26osti/96647.pdf>; problem description
  <https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#submission-format>.
- **Claim (both verbatim).** Rules §3.2: "You must submit a single GeoTIFF with a single raster layer at 100-meter
  resolution containing your model's predictions of fault locations **for the entirety of the GeoDAWN study area**."
  Problem description: "Your submission has **the same bounds as the training data**, and data outside the bounds is
  null or nan."
- **Why it is a live question, not pedantry.** The prediction grid (3292 × 3730 px at 100 m ≈ 122,800 km² bounding box)
  is roughly 2.4× the surveyed area (51,857 km² — see the feature-stack page). If the training raster's bounds are that
  bounding box, then "the entirety of the GeoDAWN study area" and "the same bounds as the training data" are **two
  different instructions** (the second is larger). If the training raster is clipped to the footprint, they coincide.
  This cannot be settled without the file.
- **Action:** once `training_features.tif` is placed, compare its bounds against the GeoDAWN bounding box from
  ScienceBase (−120.0024, 37.3641, −116.1415, 40.7247) and record the answer here. If they differ, the safe submission
  is the training-data bounds (the problem description governs format, and staff have confirmed the mask is derived from
  the provided labels). Until then this stays on the watch list.
- **Confidence:** verified for both quotations. The size mismatch is the derived observation recorded on the
  feature-stack page, itself **inference** from two verified numbers.

## GV-13 · The two official documents describe GeoDAWN's contents differently

Recorded in full at **GM-9** and tracked here because it is a governance-grade discrepancy between two official
sources: rules §2 calls GeoDAWN "a high-resolution lidar, magnetic, and radiometric study", while the data release
(Glen & Earney, 2024, <https://doi.org/10.5066/P93LGLVQ>) is titled "Airborne magnetic and radiometric surveys" and
describes lidar as a separate, coordinated 3DEP collection. **No scoring consequence is known.** Not raised on the
forum — this agent does not post. Flagged for a human to raise if it ever matters.

## GV-14 · Re-verification pass 2026-09-26 session arena/01a0dfc9 — no new forum topics, no rules change, site audit clean

- **Source:** hub <https://www.drivendata.org/competitions/306/competition-doe-gems/>; problem 967 both chunks; about 968; rules PDF <https://docs.nlr.gov/docs/fy26osti/96647.pdf> (redirect from nlr.gov) all 7 chunks; forum category JSON <https://community.drivendata.org/c/gems-prize-challenge/111.json> both chunks; threads 11516/4, 11536, 11527/7, 11524, 11528, 11529; USGS GeoDAWN data page; ScienceBase item JSON + fields=spatial; INGENIOUS GDR 1391; USGS QFFD page; NBMG layer 0 JSON.
- **Claim:** Same as GV-11 — Preface change-log table still 5 empty rows, no amendment since September 2026 version; forum still 11 topics newest 11543 (2026-09-25) no new topic since previous session; posts_count unchanged 1 for 11543/11540/11526, 2 for 11499 (pinned + 1 unanswered eligibility), 4 for 11516, 2 for 11536/11529/11528/11524, 10 for 11527, 1 for 11531/11526; rules PDF now served from docs.nlr.gov after redirect, both URLs same content; deadline still Dec 3 2026 11:59 p.m. UTC on hub vs 5 p.m. ET on §A.1 — flagged irregularity remains; eligibility §1.3 re-read no change no team-composition change recorded; metric α=0.2 β=0.8 R=300 m worked example 0.60 re-confirmed; submission format EPSG:32611 100 m float32 [0,1] same bounds null/nan re-confirmed; mask pixel-exact identical to training labels + near-known fully penalized + new-fault can lie within 300 m correction outcome re-confirmed from staff posts 11516/4 and 11536; test-fault provenance declined 11527/7 re-confirmed; weekly rolling window 11524 re-confirmed; external data licence must permit use + sharing 11528 re-confirmed; band-19 bug 11529 re-confirmed; GeoDAWN 149,030 line-km 51,857 km² Area1 200 m/2,000 m 100/150 m Area2 400 m/4,000 m 150/200 m 4 blocks Winnemucca/Fallon/Hawthorne/Tonopah CC0 1.0 variable clearance warning re-confirmed; ScienceBase bbox -120.0024,37.3641,-116.1415,40.7247 re-confirmed; INGENIOUS 22,956 traces re-confirmed.
- **Relevance:** Time-sensitive governance — confirms no official errata or new staff answers since previous session. Any decision based on previous reads remains valid today.
- **Confidence:** verified — all items fetched and read this session via fetch_page, not recalled.

## GV-15 · Re-verification pass — 2026-09-26, session `arena/01a0dfe6-learngemsdoe`

- **Sources, each fetched and read this session (not recalled):** competition hub; problem description page 967 (both
  chunks); About page 968; official rules PDF <https://www.nlr.gov/docs/fy26osti/96647.pdf> (served from `docs.nlr.gov`)
  chunks covering the Preface, §1.1–§1.4, §2 and §3.1–§3.2; forum category JSON (both chunks); thread
  [11516](https://community.drivendata.org/t/scoring-clarification-are-known-usgs-ingenious-faults-masked-when-scoring-and-are-they-in-the-final-round-label-set/11516.json)
  (all four posts) and thread
  [11536](https://community.drivendata.org/t/where-do-you-draw-the-line/11536.json) (both posts); NBMG layer-0 JSON and a
  `returnCountOnly` query; ScienceBase item `?format=json&fields=spatial`; INGENIOUS GDR 1391 resource list; the USGS
  faults page (chunks 0–2, including the sections not previously read); the USGS GeoDAWN data page (read in full);
  Hermant et al. (2025) (all eight chunks); the reference-solution README.
- **Claim — nothing has changed.** The Preface change-log table still has five empty rows: no recorded amendment since
  the September 2026 version. The forum still holds **11 topics**, the newest still **11543 (2026-09-25)**, with
  `posts_count` unchanged (11516: 4, last post 2026-09-21; 11536: 2, 2026-09-23; 11527: 10, 2026-09-23; 11528, 11529,
  11524: 2 each; 11531, 11526, 11540, 11543: 1 each; 11499 pinned: 2). No staff reply has appeared on 11540, 11526,
  11543, or the eligibility question inside 11499.
- **Newly recorded verbatim — the complete staff answer in 11516 post 4 (2026-09-21):**
  1. "The mask is indeed pixel-exact - it is identical to the provided set of training fault labels."
  2. "Only new-fault ground truth is considered for scoring purposes. A predicted pixel that is near a known fault trace
     but far from a new-fault ground truth pixel will be fully penalized, i.e., the buffer does not apply to known
     faults."
  3. "A new-fault ground truth pixel can indeed lie within 300m of a known fault trace. Such pixels would constitute
     corrections or modifications to existing fault traces. Identifying these corrections is one outcome we are aiming
     for as part of this competition. **Such corrections may already exist in the new-fault set, and may also exist in
     the final round evaluation set.**"
  The final sentence was not previously captured in this library. It matters for H1 and H12: corrections are not only an
  Initial-Round phenomenon — staff say they may also be in the Final-Round evaluation set, so near-trace geometry can pay
  twice.
- **Also newly recorded from the rules PDF this session:** §1.1 states "There will be two phases of prize awards", with
  Phase 1 "$50,000 … distributed equally among the top five competitors, as judged by their performance on the private
  test set of fault labels" and Phase 2 "$250,000 … among the top five competitors, as judged by their performance on all
  fault labels in this updated label set", and "a total of up to 10 awards"; §3 states the prize "is part of the
  American-Made program … administered by NLR"; §1.2 again defers dates to `gems.drivendata.org`; and footnote 3 cites
  GeoDAWN as "Accessed December 22, 2025".
- **Confidence:** verified — everything above was fetched and read this session.

## GV-16 · The official escalation channel for the two open discrepancies

- **Source:** <https://www.drivendata.org/competitions/306/competition-doe-gems/> (read 2026-09-26)
- **Claim (verbatim):** "If you are ever unsure whether your solution meets the competition rules, ask the challenge
  organizers in the competition forum or send an email to gemsprize@nlr.gov."
- **Relevance.** GV-12 (submission extent) and GV-13 (what GeoDAWN contains) are cases of two official documents
  disagreeing with each other. This agent does not post to the forum — that constraint is recorded in every
  AI-usage-log entry — so the escalation path belongs to a human: a new forum thread, or that mailbox. Recorded here so
  the decision is not lost between sessions. Neither question blocks research; both could block a submission.
- **Confidence:** verified for the quotation.

## GV-17 · The problem description's feature list and the notebook's 19 band tags do not line up

- **Sources:** <https://www.drivendata.org/competitions/306/competition-doe-gems/page/967/#provided-features> (read
  2026-09-26); band tags as printed by the reference-solution notebook (see the [feature stack](../feature-stack.html)).
- **Claim — problem description, verbatim:** "The GeoTIFF has many layers: Surface conductivity and depth to conductive
  base surface · Detrended elevation and the slope of detrended elevation · Dilatation rate, shear strain rate, and the
  second invariant of the strain rate tensor · Isostatic gravity anomaly and the slope of the isostatic gravity anomaly ·
  Magnetics including reduced-to-pole magnetic anomaly, total magnetic intensity, the vertical and horizontal slope of
  total magnetic intensity, and the top-of-crustal magnetic source depth estimate · Density of earthquakes."
- **Claim — band tags, verbatim examples:** band 6 "Tilt angle or total curvature — magnetic field derivative for edge
  detection"; band 10 "Distance to earthquake (n=100km radius, a=15° azimuth parameters)"; band 15 "Depth to basement
  surface — thickness of sedimentary cover".
- **The mismatch, stated precisely.** The problem description names a **"depth to conductive base surface"** and a
  **"top-of-crustal magnetic source depth estimate"**; no band tag matches either name. Conversely, band 6 (tilt angle /
  total curvature) and band 10 (distance to earthquake) have no counterpart in the problem description's list. The
  remaining items map onto bands plausibly but not provably (e.g. "surface conductivity" ↔ band 17).
- **Why it is not pedantry.** Band 6 is already an edge detector, so whether it exists changes what H2 must build; the
  two unnamed depth surfaces would change the cover-conditioning argument (PF-6); and if the problem description's list
  is the authoritative inventory, the notebook's tags are a display convention and the band numbering used across this
  site could be shifted by the position of the unlisted layers.
- **Action:** resolve by comparing `data/inventory.json` (written by `scripts/prepare_data.py`) against the
  [feature-stack page](../feature-stack.html) once the rasters are placed. Until then, every band number on this site is
  cited as "the tag printed by the reference notebook", which is what the feature-stack page states up front.
- **Confidence:** verified for both texts. The mismatch is arithmetic on them; the consequences are **inference**.

## GV-10 · Forum re-read 2026-09-26 (session arena/01a0df77)

- **Source:** category JSON <https://community.drivendata.org/c/gems-prize-challenge/111.json>; thread JSON 11540, 11526, 11543.
- **Claim:** No new topic since 11543 (created 2026-09-25). `posts_count` remains 1 for 11540, 11526, 11543. NBMG Qfaults layer 0 `returnCountOnly` still returns `{"count":22956}` — same as CG-8.
- **Relevance:** Time-sensitive governance. An unanswered eligibility question is not an answer.
- **Confidence:** verified for the JSON fields named above. HTML pages: [`docs/forum.html`](../docs/forum.html).
