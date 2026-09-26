# Prior art

Canonical HTML: [`docs/research/prior-art.html`](../docs/research/prior-art.html)

## PA-1 · Mattéo et al. (2021)

- **Source:** <https://doi.org/10.1029/2020JB021269>, listed first on the competition About page
- **Citation:** Mattéo, L., Manighetti, I., Tarabalka, Y., Gaucel, J.-M., van den Ende, M., Mercier, A., Tasar, O., Girard, N., Leclerc, F., Giampetro, T., Dominguez, S., & Malavieille, J. (2021). Automatic fault mapping in remote optical images and topographic data with deep learning. *JGR: Solid Earth*, 126(4), e2020JB021269.
- **Verified:** full author list, journal, volume, article number, DOI; **open access under CC BY-NC-ND 4.0**; corresponding author L. Mattéo (Université Côte d'Azur, Géoazur).
- **Relevance:** The organisers' first citation uses optical imagery + topography. **The 19-band stack has no optical band at all** — the modality the organisers point at first is the one this competition does not provide. Argument for Sentinel-2 as external data (cf. Hermant's B8A use, GM-3).
- **Confidence:** verified for the record. **Unverified:** methods and results have *not* been extracted; nothing about architecture, resolution, training set or scores is asserted.

## PA-2 · Hermant et al. (2025)

- **Source:** <https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf>
- **Verified design:** two U-Net-family models — **siUNET** (487,297 parameters) and a deeper in-house **FaultSEG** (~100× parameters). Three-channel input (elevation, slope, Sentinel-2 B8A) at 10 m, 128 × 128 tiles. Labels: 1,100 faults / 264 km, 50 m buffer, eastern half of the study area, western half reserved for prediction. 7,692 tiles → split 64/16/20 (4,920 / 1,232 / 1,540) → augmented to 20,000 / 4,000 / 4,000. Fault pixels 6.5%. Focal Binary Cross Entropy, α = 0.065, γ = 2.0. Metrics: PR-AUC and weighted Focal IoU. Learning curves reach PR-AUC ≈ 0.88 train / ≈ 0.59 validation for FaultSEG at epoch 17.5; siUNET ≈ 0.56 / 0.47.
- **Relevance:** Three lessons. (1) The generalisation gap is the story — on a *geographic* split they still report train 0.88 vs validation 0.59; a random-patch split will look better than it is. (2) They trained on their own labels, not the USGS catalogue, because "the USGS Quaternary fault mapping is sometimes inaccurate at small scales or of variable precision" — a published endorsement of H5. (3) Their output is a fault map, not a gap map.
- **Confidence:** verified — all numbers read from the PDF. The overfitting reading is our interpretation of their reported curves.

## PA-3 · The official reference solution (Lipor)

- **Source:** <https://github.com/drivendataorg/gems-prize-reference-solution> — README and `unet-mc-cv-reference-solution.ipynb`
- **Verified (from the notebook's own approach summary):** "an ensemble of U-Net models trained across multiple train/test splits"; (1) load and pre-process multi-channel features and fault labels; (2) split into patches; (3) train with data augmentation, applying **random train/test splits** for cross-validation, using a **Tversky loss function weighted to penalize false negatives more than false positives**; (4) average predictions from the best model across each iteration. Uses `segmentation_models_pytorch` and `torchvision.transforms.v2`; device CUDA → MPS → CPU. Local filenames `data/numeric_features.tif` and `data/labels.tif`. Preprocessing: values < −1e38 → NaN, then per-channel min-max normalisation to [0, 1].
- **Confidence:** verified for all of the above. **Unverified:** the notebook is 198 chunks and only the first was read — no claim is made about patch size, epochs, model depth, ensemble size or reported scores.

## PA-4 · Where the reference likely falls short

**Inference, built on verified inputs.** Four structural mismatches:

1. **It is trained to reproduce the labels scoring removes.** Staff: the mask "is identical to the provided set of training fault labels" (11516 post 4). A perfect reproduction scores *zero*.
2. **Random splits leak spatially.** The notebook states random splits. Neighbouring patches share edges, noise and acquisition artefacts; reported CV performance overstates generalisation — cf. Hermant's 0.88 vs 0.59 on a proper geographic split.
3. **The 1 m DEM is unused.** The reference reads `numeric_features.tif` only. The officially provided 1 m DEM — the layer at scarp resolution — is absent. *(Depends on the unread notebook cells; strike if later cells load DEM tiles.)*
4. **Nothing is conditioned on cover thickness.** Band 15 is in the stack, but a single uniform model cannot express that "no scarp" means different things under fill versus on bedrock.

## PA-5 · The organisers' own menu of methods

- **Source:** <https://www.drivendata.org/competitions/306/competition-doe-gems/page/968/>
- **Verified quotations:** "modern computational methods including **edge detection, Hough transforms, and deep learning** on seismic or topographic datasets further enhance automated fault mapping"; and "**Most faults in the GeoDAWN region of Nevada are more subtle, and many are hidden below the surface, requiring geophysical data to detect.**"
- **Relevance:** Classical lineament methods are explicitly in scope, and the interesting faults are stated to be subtle and hidden. A classical edge-detection pass is cheap, explainable to a geologist reviewer, and targets the hidden half directly.

## PA-6 · Hermant et al. (2025): the numbers the paper states, read this session

Everything below is stated in the paper's prose (§6), not read off a chart. Source:
<https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2025/Hermant.pdf>.

- **Training setup (verbatim):** "The siUNET and FaultSEG models were both trained on the same augmented dataset with
  the same hyperparameters (Adam optimizer, 20 epochs and a learning rate of 10⁻⁵)."
- **PR-AUC — FaultSEG:** 0.902 train / 0.610 validation / 0.595 test. **siUNET:** 0.574 / 0.463 / 0.449.
- **Weighted Focal IoU (verbatim):** "a threshold ≤ 0.3 should be considered as good performance for FaultSEG (≥ 0.879,
  ≥ 0.594 and ≥ 0.580 for training, validation and test respectively) and ≤ 0.2 for siUNET (0.600, 0.498 and 0.453 …)".
- **Overfitting (verbatim):** "the loss and metrics show a clear deviation between the values for training and the
  validation datasets **after 7 epochs** … This overfitting is also present but to a lesser extent for siUNET **after 12
  epochs**." They add that "FaultSEG after 7 epochs outperforms siUNET [at] 12 epochs".
- **Refines PA-2.** The epoch-resolved figures recorded in PA-2 (PR-AUC ≈ 0.88 / ≈ 0.59 for FaultSEG; ≈ 0.56 / ≈ 0.47 for
  siUNET) were approximations taken from a figure whose axis labels were truncated in our extraction. They are
  consistent with the prose values above but are **not** the paper's stated numbers, and PA-2 cites them as
  "epoch 17.5", which the prose does not support. **Use the values in this entry.** Figure 7's per-epoch table has not
  been transcribed, because its column headers did not survive extraction and transcribing half a header row is how
  wrong numbers enter a knowledge base.
- **Why it matters.** The generalisation gap is the whole story: 0.902 train against 0.595 test on a model the authors
  call the better of the two. Any project score quoted on a random-patch split is not comparable to this. Also note the
  absolute level: PR-AUC ~0.6 out of sample for a purpose-built fault detector on 10 m lidar-derived inputs. That is the
  realistic ceiling to plan around, not a floor to beat on the first try.
- **Confidence:** verified for all quotations and figures in this entry.

## PA-7 · Published design advice for exactly our problem: incomplete labels

- **Source:** Hermant et al. (2025) §7, read this session.
- **Verbatim — the problem:** "the fault labels used for training are inherently uncertain as manual fault maps are
  never exhaustive." **Verbatim — the proposed fix:** "This highlights the need to inform the model that any part of the
  study area may contain some faults, even if they are not present in the fault label. This could be done by including
  an adversarial loss term (Goodfellow et al., 2015) or by introducing noise in the true label (Mnih and Hinton, 2012),
  which will be the subject of further work." **Verbatim — the operating posture:** "It has been decided to take the
  risk of predicting too many faults … rather than missing or incorrectly mapping certain faults." **Verbatim — the
  loop:** "iterative learning … using faults predicted by the model and validated by an expert as fault label, can
  improve the qualitative and quantitative detection performance."
- **Why it matters.** This is peer-reviewed-adjacent, region-specific endorsement of three things this project already
  assumes: (1) the catalogue is an incomplete sample, so training to reproduce it encodes the wrong target; (2) given
  α=0.2 / β=0.8, over-prediction is the correct posture; (3) expert re-labelling of model output is the improvement
  mechanism — which is precisely the Phase 2 structure described on the problem page. It is the strongest outside
  support for H9.
- **Caveat to carry.** Their own models overfit after 7 epochs on 20,000 augmented tiles at 10 m. Transferring their
  recipe to 100 m inputs with an even smaller positive fraction is not free.
- **Confidence:** verified.

## PA-8 · An independent lidar-mapped fault set exists inside the GeoDAWN box

- **Citation:** Silver, E., MacKnight, R., Male, E., Pickles, W., Cocks, P., & Waibel, A. (2011). *LiDAR and
  hyperspectral analysis of mineral alteration and faulting on the west side of the Humboldt Range, Nevada.*
  **Geosphere**, 7(6), 1357–1368. <https://doi.org/10.1130/GES00673.1>
- **Verified:** the DOI resolves to that title in Geosphere vol. 7 no. 6, p. 1357 (checked 2026-09-26). The full
  citation is printed in Hermant et al. (2025)'s reference list, which is where it was found.
- **Why it matters.** Hermant et al. use it as the reference fault mapping for the Rye Patch / western Humboldt Range
  area, and their models' false positives include features "described by Silver et al. (2011), such as the
  paleo-shoreline or the Rec Area scarp". If that mapping can be obtained, it is an **independent** lidar-derived fault
  set inside the GeoDAWN bounding box — a local truth set for asking "does this detector find faults the catalogue
  lacks?" without spending a submission slot or touching the private labels.
- **Confidence:** verified for the citation and DOI resolution. **Unverified:** the paper's contents have not been read
  and it is **not established** that its fault mapping is distributed as data. Treat as a lead, not as an asset.

## Synthesis — what a better design looks like

1. Change the **split** before changing the model: contiguous geographic blocks, not random patches.
2. Score with the real metric on the real mask — `scripts/metrics.py` implements the DTI with a pixel-exact known-fault mask.
3. Define **positives** by something other than the catalogue.
4. Keep one **classical, explainable** branch alive (tilt-derivative / gradient-magnitude lineaments).
5. Report **conditioned on cover thickness and lidar coverage**.
