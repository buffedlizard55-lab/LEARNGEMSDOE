# Catalogue-gap reasoning

Canonical HTML: [`docs/research/catalogue-gaps.html`](../docs/research/catalogue-gaps.html)

Highest-leverage domain. The scored target is "what the catalogue does not contain", so the catalogues' own
methodology is the most valuable document in the project: if you know how a fault had to be evidenced to get into
the database, you know which faults were structurally incapable of getting in.

## CG-1 · The database is defined by surface rupture

- **Source:** <https://www.usgs.gov/programs/earthquake-hazards/faults>
- **Citation:** U.S. Geological Survey, 2020, Quaternary Fault and Fold Database for the Nation, <https://doi.org/10.5066/P9BCVRCK>
- **Claim (verbatim):** "This database contains information on faults and associated folds in the United States that demonstrate geological evidence of **coseismic surface deformation** in large earthquakes during the past 1.6 million years (Ma)." The 1.6 Ma cutoff is inherited from the 1983 Geologic Time Scale in use when the database was established in 1993.
- **Relevance:** A buried structure with no demonstrable surface deformation is out of scope by construction, not merely unmapped. Combined with the About page — "many are hidden below the surface, requiring geophysical data to detect" (<https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/>) — this is the strongest argument for H2.
- **Confidence:** verified.

## CG-2 · 1993 compilation rules

- **Source:** <https://pubs.usgs.gov/of/1993/0338/report.pdf> — Haller, Machette & Dart, USGS OF 93-338
- **Claim (verbatim):** compilers were told to "give preference to (1) fault-related topical studies over general studies …, (2) more recent studies, and (3) more detailed scale of work (i.e., 1:24,000-scale over 1:250,000-scale mapping)". And: "suspected or inferred Quaternary faults (and folds) will be shown as dotted Quaternary structures (age category 5), whereas structures with known late Tertiary (or older) movement will not be shown unless there is compelling evidence of Quaternary movement (geomorphology, offset surficial deposits, etc.)". The compiler "is forced to select a slip rate and age even when no data may exist". Segmentation requires study "in a paleoseismologic sense (trenching and dating)".
- **Relevance:** Three exclusion mechanisms: evidence must be published; inferred structures are down-weighted or dropped; scale heterogeneity is baked in.
- **Confidence:** verified — quotations read from the PDF.

## CG-3 · Reduced maintenance since 2017

- **Source:** <https://www.usgs.gov/programs/earthquake-hazards/faults>
- **Claim (verbatim):** "effective January 12, 2017, the USGS will maintain a limited number of metadata fields … Archived reports are accessible from the abbreviated record." Also: as of **26 February 2026** the Database Search function is retired; legacy reports are reachable through the interactive fault map <https://doi.org/10.5066/F7S75FJM>. GIS: <https://earthquake.usgs.gov/static/lfs/nshm/qfaults/Qfaults_GIS.zip> (16 MB).
- **Relevance:** Maintenance capacity is deliberately reduced, consistent with completeness tracking publication history rather than geology. Also a time-sensitive note for anyone pulling per-fault metadata.
- **Confidence:** verified.

## CG-4 · INGENIOUS Qfaults: an attribute update, not a new mapping

- **Source:** <https://gdr.openei.org/submissions/1391> · DOI <https://doi.org/10.15121/1881483> · CC BY 4.0
- **Citation:** Ayling, B., Faulds, J., Morales Rivera, A., Koehler, R., Kreemer, C., Mlawsky, E., Coolbaugh, M., Micander, R., dePolo, C., Kraal, K., Wagoner, N., Siler, D., DeAngelo, J., Glen, J., Peacock, J., Batir, J., Gentry, E., Berti, C., Lifton, Z., Clark, A., Kirby, S., Hardwick, C., and Kleber, E. (2022).
- **Claim:** Qfaults **v1** = "updated quaternary fault traces, ages, and slip rates … Attributes conform to USGS Qfault Database s[tandards]". Qfaults **v2** "contains an updated version … and text document with field definitions. It supersedes [v1]". Whole compilation: 9 files, 116.98 MB.
- **Relevance:** These are the training labels the scorer masks out (rules §3.3). It is an attribute update, so it inherits USGS inclusion criteria rather than fixing them. v2 supersedes v1 — check versions.
- **Corroboration from the project's own team:** Hart-Wagoner, Coolbaugh, Faulds & Mlawsky (GBCGE / NBMG, University of Nevada, Reno), <https://publications.mygeoenergynow.org/grc/1034813.pdf>: "A Quaternary fault database for the INGENIOUS GBR was collated in Phase I of the INGENIOUS project and included **updated fault locations** and updated fault attributes of **recency** (i.e., age of most recent rupture) and **slip rates**." Independent, project-internal confirmation that the compilation updated locations and attributes rather than re-mapping from new evidence.
- **Project context** (<https://gbcge.org/current-projects/ingenious/>): PI Bridget Ayling, Co-PI James Faulds; 1 Feb 2021 – 30 Jun 2025; $10,000,000; DOE GTO award DE-EE0009254.
- **Confidence:** verified for the GDR descriptions, the Hart-Wagoner abstract (read) and the project page (read). **Unverified** — the field-definition document inside the v2 archive has not been unpacked.

## CG-5 · Measured heterogeneity, up to 400 m misfit

- **Source:** <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf> (cited by the competition About page)
- **Citation:** Hermant, B., Kiersnowski, L., & Bellanger, M. (2025). Proc. 50th Workshop on Geothermal Reservoir Engineering, Stanford.
- **Claim (figure 2 caption):** "Local discrepancy observed in North Central Nevada: distance between USGS Quaternary faults and TLS fault label can be up to 400 m." Heterogeneity attributed to "the aggregation of different mapping sources or scales in this database".
- **Relevance:** 400 m > the 300 m metric kernel. This is the quantitative core of H1, and a warning that "stay near the known line" is not a safe prior.
- **Confidence:** verified. Measured in north-central Nevada — regional, not area-specific.

## CG-6 · Who labelled the new faults, and what they will say

- **Sources:** rules §2 <https://www.nlr.gov/docs/fy26osti/96647.pdf>; forum 11527 post 7 <https://community.drivendata.org/t/how-were-the-new-test-faults-identified-data-sources-and-fault-types/11527/7>
- **Claim (verbatim, rules §2):** "The labels for this prize come from the USGS Quaternary Fault and Fold Database and from a set of newly identified faults labeled by geology experts at the National Laboratory of the Rockies (NLR) and USGS."
- **Claim (verbatim, staff):** "We're not sharing details about the data sources, fault types, or coverage behind the test faults beyond what's in the problem description."
- **Relevance:** We know the institutions, not the protocol. The Phase 2 redirection is an official hint about where value sits.
- **Confidence:** verified for both quotations. Any inference from the labellers' identity is **unverified**.

## CG-7 · The four gap classes (derived)

**Inference — reasoning, not sourced fact.** Written to be argued with.

1. **Corrections to known traces** — tip extensions, splays, parallel strands, positional errors up to ~400 m. Staff-confirmed to count.
2. **Post-compilation visibility** — scarps mappable only with 3DEP/GeoDAWN-era elevation, i.e. after the topical literature compilers were told to prefer.
3. **Cover-masked structures** — outside the QFFD definition entirely (CG-1).
4. **Low-publication terrain** — no topical detailed-scale study ever published, so nothing for a compiler to prefer.

Mapping to signals: classes 1–2 → topography (bands 12, 19, 1 m lidar); class 3 → gravity/magnetics under thick cover (5, 11, 13, 15, 18); class 4 → independent evidence (4, 7, 8, 10, 16, 17).

## Falsification tests

- If private labels are dominated by long, obvious, unmapped range fronts, the corrections/subtle-scarps framing is wrong.
- If distance-to-known-fault is a *positive* predictor of new labels, the gap is diffuse and H1 should be demoted.
- If the INGENIOUS v2 field definitions carry provenance or mapping-scale attributes, class 4 becomes measurable.

## Next actions

1. Download <https://gdr.openei.org/files/1391/qfaults_ingenious_nad83conus117_2023-06-27.zip> and read the field-definition text.
2. Pull Qfaults GIS zip and the GeoDAWN survey outlines (<https://www.sciencebase.gov/catalog/item/657e1d85d34e23d3533209f7>); build catalogue-density and lidar-coverage surfaces.
3. Once rasters are placed: distribution of distance-to-nearest-label for high-strain / high-seismicity / high-gradient pixels.
