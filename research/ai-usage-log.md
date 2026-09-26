# AI-usage log

Canonical HTML: [`docs/ai-usage.html`](../docs/ai-usage.html)

Required by Official Rules §3.2: <https://www.nlr.gov/docs/fy26osti/96647.pdf>

> "Using generative AI technology in the development of your prize submission is allowed. However, you must indicate
> in the narrative (not included in the word count) the extent to which, if any, you used generative AI technology and
> how you used it to develop your submission … You are responsible for the accuracy, authenticity, and authorship
> representations of your submission under consideration, including content developed with generative AI tools.
> Relying on generative AI may introduce significant risks, including but not limited to, research misconduct
> resulting from fabrication, falsification, or plagiarism…"

This log is built incrementally, session by session, so the §3.2 narrative can be assembled from a contemporaneous
record rather than reconstructed at the deadline.

---

## 2026-09-26 · session `arena/01a0df88-learngemsdoe`

**Tool.** Arena.ai Agent Mode — a coding agent with web fetch, web search, file read/write and shell execution in this
repository. No other generative-AI service was called. No image, audio or video generation. No prediction GeoTIFF was
produced, scored or submitted, and no weekly submission slot was used.

**Did — source verification (fetched and read, not recalled).** Competition hub; problem description page 967 (both
chunks); About page 968; the official rules PDF (Preface, §1.1–§1.4, §2, §3.1–§3.2); the forum category JSON (both
chunks); the ScienceBase GeoDAWN item including its `fields=spatial` bounding box; six NBMG ArcGIS count queries plus
the layer metadata; the USGS Quaternary Fault and Fold Database page including its History section; the USGS GeoDAWN
data page; Hermant et al. (2025) PDF chunks 4–6; Drenth & Grauch (2019) Table 1; and the reference-solution README via
the GitHub API. Two DOIs discovered in Hermant's reference list were resolved before being cited
(10.1130/GES00673.1 → Geosphere 7(6):1357; 10.1029/2019EO120449 → Eos).

**Did — measurement.** Counted the INGENIOUS fault compilation inside the published GeoDAWN bounding box by attribute
class (CG-9): 1,179 traces — 739 Well Constrained, 351 Moderately Constrained, 89 Inferred, 0 Poor/Other/blank. Every
count is reproducible from a linked query URL. No total fault length is asserted because the service reports
`supportsStatistics: false` and refuses the sum.

**Did — writing.** Added 15 numbered research entries and three hypothesis cards; added the search page, its generated
index, a two-tier navigation, a reading order and a verification section; added CI and footer/explainer-gate links;
corrected PA-2 in favour of PA-6's prose-sourced figures; made Pass 2–3 review corrections to coordinates, citation
form, counts, and markup; and appended this log and the changelog entry in the same session. Existing entries were
extended, not duplicated.

**Did — code.** Wrote `scripts/check_site.py` (offline link, anchor, asset, source-allowlist, and count verification)
and `scripts/build_search_index.py` (search-index generator with a `--check` drift mode); added
`.github/workflows/verify.yml`; extended `check_site.py` during review to cover overview cards and domain-meta counts;
re-ran `scripts/metrics.py --selftest` (11 checks pass) and both data-placement scripts (still blocked).

**Did not.** Create or use a DrivenData account or credentials. Generate, validate or submit a prediction raster. Ask
the forum anything — this agent does not post. Create a second site, repository, account or registration, including for
staging. Transcribe a number from a source whose labels were not legible — the Figure 7 table was left untranscribed
for exactly that reason.

**Human review still required.** Open every linked primary URL and confirm the quotations; confirm the eligibility
position against rules §1.3 if team composition or affiliations change; decide whether to raise GV-12 (submission
extent) and GV-13 (GeoDAWN contents) on the official forum; place the competition rasters and run the six CG-9 queries
against the outline polygons.

---

## 2026-09-26 · session `arena/01a0df77-learngemsdoe`

**Tool.** Arena.ai Agent Mode — coding agent with web fetch, file read/write and shell. No other generative-AI
service. No image/audio generation. No prediction files.

**Did — source verification.** Fetched hub, problem 967 (both chunks), About 968, forum category JSON and
threads 11540, 11526, 11543, USGS QFFD page, INGENIOUS GDR 1391, NBMG count query (`22956`).

**Did — writing.** Added `docs/forum.html`, GV-10, mobile navigation, library filter, changelog and this log
entry. Extended existing pages; did not duplicate CG-1…CG-8 or H1–H8.

**Did not.** Generate or submit a prediction GeoTIFF. Create a DrivenData account. Invent forum answers.
Create a second site, repo, or registration.

**Human review still required.** Open every linked primary URL. Four forum threads remain unanswered.

---

## 2026-09-26 · session `arena/01a0df46-learngemsdoe`

**Tool.** Arena.ai Agent Mode — coding agent with web fetch, web search, file read/write and shell execution. No other
generative-AI service was called from this repository. No image, audio or video generation was used.

**Did — source verification.** Fetched and read: competition hub, problem description (both chunks), About page, data
tab (login redirect), page 966, rules PDF sections §1.3, §2, §3.2–§3.4 and §A.1, forum category JSON and threads
11499, 11526, 11540 and 11543, ScienceBase item JSON file list, INGENIOUS GDR submission 1391, the NBMG INGENIOUS
Qfaults MapServer (layer schema and `returnCountOnly` queries), the USGS faults page, and the USGS FAQ “What is a
Quaternary fault?”. Reference-solution README was read via the GitHub API. The reference notebook was not re-read.

**Did — measurement.** Counted INGENIOUS constraint class and mapping-scale codes from the public map service. Each
count is tied to a query URL on `docs/requirements.html`. The service ignored `returnDistinctValues`. Counts that
could not be completed (`REC2023` value list; GeoDAWN clip) are marked unverified, not estimated.

**Did — writing.** Added the requirements checklist, CG-8, H8, watch-list rows, and this log entry. Extended the
irregularity list. Did not rewrite earlier changelog entries.

**Did — code and runs.** Updated `scripts/download_competition_data.sh` so it attempts small public files and still
refuses to log in. Ran that script, `scripts/prepare_data.py`, and `scripts/metrics.py --selftest`. Competition
rasters were not obtained. No prediction file was written.

**Did not.**

- Generate, score or write a prediction GeoTIFF, and add no code capable of doing so.
- Use a DrivenData weekly submission slot, or touch the submission API.
- Create a DrivenData account, or store credentials.
- Create a second site, repository, or registration.
- Invent a count. Where a partition was incomplete, the page says so.
- Translate `MAPSCALE` short codes into map scales. That translation is labelled inference and is not used as a fact.

**Human review still required.**

- Open each query link on the requirements page and confirm the JSON count before a prize narrative quotes it.
- The field-definition text inside the Qfaults v2 zip is unread.
- Hermant 2025 chunks 4–7 and the body of Mattéo et al. 2021 remain unread.
- Four forum threads remain unanswered: 11540, 11526, 11543, 11499.

**Fabrication controls used.**

- Quoted rules sentences were copied from the PDF chunks fetched this session.
- Attribute counts were copied from `{"count": N}` responses, then added and checked against 22,956. The addition is
  labelled arithmetic.
- A `returnDistinctValues` response that repeated rows was discarded and not used as a histogram.
- Empty-string and single-space `MAPSCALE` queries returned the same count. They were not summed.
- East Cache and Joes Valley names were copied from feature attributes. Their position relative to GeoDAWN was not
  asserted.

---

## 2026-09-26 · session `arena/01a0df14-learngemsdoe`

**Tool.** Arena.ai Agent Mode — coding agent with web fetch, web search, file read/write and shell execution. No other
generative-AI service was called from this repository. No image, audio or video generation was used.

**Did — source verification.** Re-fetched and read, in full or in part: the NLR official rules PDF (all 7 chunks),
DrivenData hub, problem page 967 (both chunks), about page 968, the forum category index and eleven individual threads,
the USGS GeoDAWN data page, the USGS Quaternary Fault and Fold Database page, the INGENIOUS GDR record, the Hermant 2025
workshop PDF (4 of 8 chunks), the Mattéo 2021 publisher record, the reference-solution README and notebook, and
corroborating records for Miller & Singh 1994, Verduzco et al. 2004 and Kreemer & Young 2022; plus the HeroX rules
resource, the USGS ScienceBase item for GeoDAWN, the GBCGE INGENIOUS project page, and the Hart-Wagoner et al. GRC
paper.

**Did — correction.** Resolved the previous session's open question about the scoring mask by reading staff post 4 of
forum thread 11516 (2026-09-21): "The mask is indeed pixel-exact — it is identical to the provided set of training fault
labels." Removed the earlier hedge from four pages and quoted the full post.

**Did — writing.** Rebuilt the site (stylesheet, sticky nav, per-page TOC, client-side filters), added the feature-stack
page, expanded all six library domains to 40 numbered entries, rewrote the seven hypothesis cards against the corrected
mask behaviour, rewrote the overview and explainer, rebuilt the source index with per-source verification status.

**Did — code.** Wrote `scripts/metrics.py` — distance-weighted Tversky index, Tversky loss, a pixel-exact masked variant,
and 11 self-tests. Ran the self-tests; all pass on CPU with the Python standard library alone.

**Did not.**
- Generate, score or write a prediction GeoTIFF, and add no code capable of doing so.
- Use a DrivenData weekly submission slot, or touch the submission API.
- Handle, request or store DrivenData credentials; no attempt to bypass the data-tab login.
- Create a second site, repository, account or competition registration.
- Invent a source, DOI, number or quotation. Three items not traceable to content actually read are marked
  `unverified` or `inference` where they appear.

**Human review still required.**
- Every URL on the source index should be opened by a person before any prize narrative quotes it.
- Miller & Singh 1994 (<https://doi.org/10.1016/0926-9851(94)90022-1>) and Verduzco et al. 2004
  (<https://doi.org/10.1190/1.1651454>) are cited by bibliographic record only; their method summaries are conventional
  descriptions, not quotations, and are labelled as such.
- Hermant 2025 PDF chunks 4–7 and the body of Mattéo et al. 2021 are unread.
- The INGENIOUS Qfaults v2 field-definition document inside the archive has not been opened.
- The reference notebook is 198 chunks; only the first was read. Claims about later cells are withheld.
- Four unanswered forum threads need re-checking: 11540, 11526, 11543, and the eligibility reply in 11499.

**Fabrication controls used.**
- Every quoted sentence was copied from a page fetched during the session. Nothing quoted from memory.
- Numbers — α=0.2, β=0.8, R=300 m, prize splits, 3292×3730, 19 bands, 149,030 line-km, 51,857 km², 200 m/400 m line
  spacing, 1,100 faults, 264 km, 50 m buffer, 6.5% positives, 1.6 Ma — were each copied from the document named beside
  them.
- Derived quantities show their inputs and are marked arithmetic or inference. The grid-area comparison (≈122,800 km²
  bounding box versus 51,857 km² surveyed) is arithmetic from two verified numbers, in a collapsible note, with the
  conclusion labelled an inference.
- Absence-of-evidence arguments, notably "what is not in the 19-band stack", are labelled inference.
- One source that had been listed with no verified content was moved out of the citation index; the PDF was then
  opened, found to be a real GBCGE / NBMG paper with a directly relevant statement about how the INGENIOUS fault
  database was collated, and reinstated as *abstract and introduction read*. Both the demotion and the reinstatement
  are recorded on the sources page and in the changelog rather than silently reversed.
- Two author lists were corrected (Kreemer & Young; Siler D.L.) against the INGENIOUS project page's own publication
  list.
- A claim inherited from a previous session — that a complete train/inference/validate pipeline was ready to run — was
  checked against the repository, found false, and flagged.

---

## 2026-09-26 · session `arena/01a0df09-learngemsdoe`

- **Tool:** Arena.ai Agent Mode (web fetch/search + file writes). Same repository, separate branch from 01a0def8.
- **Did:** re-fetched and line-by-line verified the rules PDF, DrivenData hub/967/968, USGS QFFD page, GeoDAWN
  ScienceBase item, INGENIOUS GDR record, Hermant 2025 PDF, Mattéo 2021 (JGR), Kreemer & Young 2022 (SRL), and forum
  threads 11516 / 11527-7 / 11536. Corrected an overclaim (staff 11516 confirms the known-fault mask but did not then
  state it is pixel-exact; re-labelled as an inference). Fixed a weekly-cap citation. Upgraded several confidence notes
  to "verified".
- **Did not:** generate or submit a prediction GeoTIFF; use weekly submission slots; invent citations.
- **Human review still needed:** forum 11527 post bodies; NLR PDF appendix remainder; Mattéo 2021 full methods.
  *Partly resolved by the session above.*

---

## 2026-09-26 · session `arena/01a0def8-learngemsdoe`

- **Tool:** Arena.ai Agent Mode (coding agent with web fetch/search). No other generative-AI APIs were called from this
  repository.
- **Did:** fetched official competition pages, NLR rules PDF, forum threads, USGS/INGENIOUS/GeoDAWN landing pages,
  Hermant 2025 PDF, reference-solution README and notebook. Wrote the GitHub Pages research library, hypothesis backlog,
  changelog, this log, and the inspect-only data scripts.
- **Did not:** generate a prediction GeoTIFF; call DrivenData submit; invent citations.
- **Human-owned checks still required:** every URL in the source index should be opened by a person before a prize
  narrative quotes it. NLR PDF §A.14–A.17 not fully extracted at the time — *resolved by the 01a0df14 session*.
- **Fabrication controls used:** claims tied to fetched URLs; numbers copied from those pages, not estimated; missing
  content labelled unverified.

---

## Standing controls

1. **No unsourced number.** If a figure cannot be pointed at in a fetched document, it is not written down.
2. **Quote, do not paraphrase.** Where a rule or clarification matters, the sentence is copied verbatim with a citation.
3. **Label the inference.** Reasoning built on verified inputs is marked `inference` so a reader knows it is arguable.
4. **Distinguish record from content.** A confirmed DOI means the work exists, not that a claim from it has been read.
5. **Log the negative.** Corrections, demotions and rejected hypotheses are recorded and kept, not deleted.
6. **Gate the submission.** No prediction artefact is produced by this agent; submission generation is a separate,
   explicitly authorised process, and this log is the record that the separation was maintained.
