# Potential-field geophysics

Canonical HTML: [`docs/research/potential-field.html`](../docs/research/potential-field.html)

Ten of nineteen bands are potential-field or derived from them (six magnetic, four gravity). This is the only family
that responds to structure *under* cover.

## PF-1 · What GeoDAWN can resolve

- **Source:** <https://www.usgs.gov/data/geodawn-airborne-magnetic-and-radiometric-surveys-northwestern-great-basin-nevada-and> · <https://doi.org/10.5066/P93LGLVQ>
- **Citation:** Glen, J.M.G., and Earney, T.E. (2024). CC0 1.0.
- **Claim:** 149,030 line-km over 51,857 km²; flown 1 Nov 2021 – 20 Nov 2022. Area 1 (Clayton Valley, Li-brine): rank 1 EarthMRI, 200 m flight lines, 2,000 m tie lines, 100 m clearance over low relief. Area 2 (geothermal, between rank 1 and 2): 400 m flight lines, 4,000 m tie lines, 150 m clearance. Four blocks north to south: Winnemucca, Fallon, Hawthorne, Tonopah. Magnetic processing: diurnal, aircraft-field, tie-line levelling, micro-levelling, IGRF.
- **Relevance:** Line spacing sets the shortest sampled wavelength. A "lineament" found at 100 m may be interpolation between lines 400 m apart → H7 control.
- **Confidence:** verified for acquisition numbers; the aliasing implication is **inference**.

## PF-2 · The magnetic bands

- **Source:** band `description` / `data_category` tags printed by the reference notebook; see [`docs/feature-stack.html`](../docs/feature-stack.html)
- **Claim:** 1 magnetic anomaly · 2 reduced-to-pole · 3 TMI horizontal gradient · 6 "tilt angle or total curvature — magnetic field derivative for edge detection" · 9 TMI vertical gradient · 14 TMI.
- **Relevance:** Band 6 is already an edge detector, but the tag is genuinely ambiguous about which one — check numerically. Bands 3 + 9 + 14 give gradient magnitude and analytic signal. Prefer RTP (2) for anything geometric: unreduced anomaly peaks are displaced from their sources at this latitude.
- **Confidence:** verified for band tags; the tilt-vs-curvature identification and the RTP recommendation are **inference**.

## PF-3 · Miller & Singh (1994), tilt derivative

- **Citation:** Miller, H.G., & Singh, V. (1994). Potential field tilt — a new concept for location of potential field sources. *Journal of Applied Geophysics*, 32, 213–217. <https://doi.org/10.1016/0926-9851(94)90022-1>
- **Claim:** Tilt angle = arctan(vertical derivative / horizontal gradient magnitude). Bounded, balances shallow and deep source amplitudes, zero contour sits over source edges.
- **Relevance:** Amplitude balancing is exactly what a basin-and-range setting needs, where a deep basement step under fill gives a weak broad gradient.
- **Confidence:** bibliographic record **verified**; the method summary is the standard textbook form — **the paywalled article has not been opened**. Do not quote it as the authors' own wording.

## PF-4 · Verduzco et al. (2004), THDR

- **Citation:** Verduzco, B., Fairhead, J.D., Green, C.M., & MacKenzie, C. (2004). New insights into magnetic derivatives for structural mapping. *The Leading Edge*, 23(2), 116–119. <https://doi.org/10.1190/1.1651454>
- **Claim:** Extends the tilt by taking its total horizontal derivative, giving sharper, better-localised maxima over source edges; discusses analytic-signal amplitude alongside.
- **Relevance:** The cheapest H2 experiment available — a few gradient operations on grids that already exist.
- **Confidence:** bibliographic record **verified**; article **not opened**.

## PF-5 · The gravity family

- **Sources:** band tags; <https://doi.org/10.5066/P9Z6SA1Z> (Glen et al. 2022, regional Great Basin gravity and magnetic maps); <https://gdr.openei.org/submissions/1391>
- **Claim:** 13 isostatic gravity anomaly · 5 its slope · 11 its vertical gradient · 18 its horizontal gradient. The source release is described as "generated from new and existing sources to support ongoing efforts to characterize geothermal resource potential".
- **Relevance:** Gravity is independent evidence from magnetics. A lineament in both band 18 and band 3/6 is hard to explain away.
- **Confidence:** verified for band tags and the release description. **Unverified:** that the competition's gravity bands derive from that specific release — band provenance is undocumented beyond the tags.

## PF-6 · Band 15, depth to basement

- **Claim:** "Depth to basement surface — thickness of sedimentary cover", category `subsurface`.
- **Relevance:** The stratifying variable for the whole argument. Under thick cover, a missing scarp is uninformative; over thin cover it is meaningful negative evidence. Report every H2 candidate **conditioned on band 15**.
- **Confidence:** verified for the band tag; the conditioning strategy is **inference**.

## PF-7 · Artefacts that fake structure

1. **Mosaic discontinuity** — Area 1 (200 m lines) abuts Area 2 (400 m lines).
2. **Block boundaries** — four blocks, different contractors and aircraft; levelling joins become straight "structures" once gradient-filtered.
3. **Terrain clearance** — verbatim from the USGS page: in steep terrain "the aircraft may have required deviating from the planned drape surface, and therefore **variable terrain clearance should be considered when modeling and interpreting these data**".

- **Relevance:** All three produce linear, fault-shaped features, and β=0.8 makes over-prediction cheap enough to hide the mistake. The control is public: the GeoDAWN release ships Esri shapefiles of flight paths and survey outlines.
- **Confidence:** verified for the facts and the quotation; that the artefacts appear in the derived bands is **inference**.

## Cheapest next experiments

1. Confirm numerically what band 6 is, from bands 3, 9, 14.
2. Overlay the GeoDAWN survey-outline shapefile; test whether band-3/6 maxima cluster along Area 1/2 and block boundaries (H7).
3. Stratify every edge candidate by band 15 and report detection statistics per cover class.
4. Compute analytic-signal amplitude and THDR; test whether either adds information over band 6 alone.
