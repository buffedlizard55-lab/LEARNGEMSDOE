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
| Rules change-log table | PDF Preface | empty when read |
| Staff about-post links to page 966 | https://www.drivendata.org/competitions/306/competition-doe-gems/page/966/ | duplicate of the hub welcome, not page 967 |
| Rules PDF host | https://www.nlr.gov/docs/fy26osti/96647.pdf | redirects to docs.nlr.gov (re-fetched 2026-09-26) |

## GV-10 · Forum re-read 2026-09-26 (session arena/01a0df77)

- **Source:** category JSON <https://community.drivendata.org/c/gems-prize-challenge/111.json>; thread JSON 11540, 11526, 11543.
- **Claim:** No new topic since 11543 (created 2026-09-25). `posts_count` remains 1 for 11540, 11526, 11543. NBMG Qfaults layer 0 `returnCountOnly` still returns `{"count":22956}` — same as CG-8.
- **Relevance:** Time-sensitive governance. An unanswered eligibility question is not an answer.
- **Confidence:** verified for the JSON fields named above. HTML pages: [`docs/forum.html`](../docs/forum.html).
