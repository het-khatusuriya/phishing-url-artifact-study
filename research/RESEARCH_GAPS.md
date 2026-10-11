# Research Gaps, Hypotheses and Selected Direction

Version 1 — 2026-10-11, written after the literature collection (`paper_metadata_L1–L3.csv`, `reading_notes/`) and the repository and dataset audits. Citekeys refer to `references.bib`. Each gap states whether it is **acknowledged by prior authors** (A) or **inferred by us from comparing studies** (I).

## 0. What the audits established (our own evidence, not literature)

- The baseline ensemble's two most influential features are `https_usage` and a `www.`-driven subdomain count; it labels `https://google.com/` malicious with 88 % confidence (`REPOSITORY_AUDIT.md` §7).
- In PhiUSIIL, the closest public analogue of the project's data, **100 %** of benign URLs are `https://www.<domain>` homepages with an empty path, while phishing URLs are 48 % https / 42 % `www.` / 72 % homepage (`DATASET_AUDIT.md` §3). The `www.` and length artifacts point in opposite directions in different public corpora (AUC 0.21 vs 0.71 for `www.`).
- A 20k-row smoke experiment: lexical models reach ROC-AUC 0.999 on a grouped PhiUSIIL split and then flag **98–99 % of legitimate Hannousse-2021 URLs** as phishing (`results/runs` smoke, to be replaced by the full runs).

## 1. Candidate gap G1 — Collection artifacts and shortcut learning in URL benchmarks (A + I)

**Supporting literature.** General security-ML pitfalls: sampling bias → spurious correlations → base-rate fallacy chain [arp2022dosdonts]; closed-world evaluation [sommer2010closedworld]; base rates [axelsson2000baserate]. Phishing-specific: Alexa index pages vs full phishing URLs "creates a bias in the data" [sabir2022reliability]; findings "dataset dependent and far away from generalization", do not use Alexa lists directly [hannousse2021benchmark]; balanced data and domain-only benign sets criticised [elaassal2020benchmarking, das2020sokphishing, marchal2018designing]; cross-dataset accuracy near chance with SHAP sign flips [mia2024featurestrust]; detectors "work effectively only when the test sets are split from the same training dataset", with URL recording format named as a cause [rashid2024domainadapt]; a 2026 single-author preprint reports the `https://`/`www.` shortcut and near-100 % prediction instability under reformatting [giri2026shieldphish]; corpus-identification probes and artifact-removal ablations exist for phishing *e-mail* [bhuiyan2026fragility]; insufficient benign diversity in 55 detectors [alam2026philter]; leakage and base rates in web-page benchmarks [dalton2025phreshphish].

**What earlier work accomplishes.** Documents cross-dataset drops (Mia, Rashid, Henry), prescribes guidelines (Marchal, El Aassal, Arp), and — in one unreviewed preprint — names the scheme/`www.` artifact.

**Unresolved limitation.** No peer-reviewed study (a) quantifies, across several public URL corpora, how much of the in-distribution performance of standard lexical detectors is carried by a small set of *nameable* collection artifacts; (b) shows that the *sign* of those artifacts differs between corpora (which mechanistically explains cross-dataset collapse); (c) measures how much domain memorisation (random vs registered-domain-grouped splits) adds on top; or (d) tests whether removing the artifacts at feature level is sufficient to generalise. Prior cross-dataset work used pre-computed feature tables rather than raw URLs, so artifacts could not be isolated.

**Why it matters.** Dozens of papers report > 97 % accuracy with such features; deployment on real traffic (where benign URLs have paths and phishing URLs are https) gives the FPR observed in our smoke test, which would make a product unusable.

**Repository shortfall.** The baseline is a textbook instance: a random split, one-hot TLDs, no external test, scheme/`www.` features on top.

**Technical solution.** Artifact-aware evaluation protocol: per-class artifact statistics; artifact-feature ablation; registered-domain-grouped splits; dataset-identification probe; cross-corpus transfer matrix; models re-trained with artifact-neutral features.

**Hypotheses.**
- H1a: Removing `{scheme, www, label-count}` features reduces in-distribution AUC on PhiUSIIL only marginally (< 0.01) but changes external-set FPR by a large margin (> 20 points) for tree ensembles.
- H1b: Random splits over-estimate grouped-split performance, with the gap largest on corpora with few domains per URL (ISCX-2016, Kaggle lineage).
- H1c: A linear probe can identify the source corpus of a benign URL from lexical features far above chance (≥ 2× chance), and removing artifact features reduces but does not eliminate this.

**Experiment.** Runs `A_b28_*`, `A_v2_*`, `*_noart_*`, `B_*` with external tests (Sections 4–6 of `EXPERIMENT_PROTOCOL.md`); `analysis_dataset_probe.py`; `analysis_dataset_artifacts.py`.

**Measurable outcomes.** ΔAUC / ΔFPR / ΔTPR@FPR=1 % between (random, grouped) and (with, without artifacts), with paired bootstrap CIs over 5 seeds; probe accuracy vs chance.

**Risks / competing approaches.** Unsupervised domain adaptation [rashid2024domainadapt] and transfer learning [henry2026ensembletransfer] attack the symptom (shift) rather than the cause; canonicalisation [giri2026shieldphish] is a special case of our artifact-neutral features. Risk: artifact removal may expose that *nothing* transfers, in which case the paper's contribution is diagnostic rather than a better detector — still valid and reportable.

## 2. Candidate gap G2 — Operating-point reliability: calibration and FPR-constrained thresholds under shift (A + I)

**Supporting literature.** Boosted trees are systematically mis-calibrated and Platt/isotonic correct this [niculescumizil2005calibration]; calibration of modern models [guo2017calibration]; in security, calibration degrades under dataset shift and collapses under adversarial inputs for Android malware [li2021malwarecalibration] — the authors and our searches found **no equivalent for phishing URLs**; prevalence shift makes fixed thresholds fail asymmetrically [bhuiyan2026fragility]; realistic prevalence 1:100 or lower [marchal2018designing, dalton2025phreshphish, pendlebury2019tesseract]; metrics for imbalance [alam2026philter].

**Unresolved limitation.** Phishing-URL papers report accuracy/F1 at threshold 0.5 on balanced data. Whether a threshold chosen for a 1 % FPR budget on validation *holds* on external data, and whether post-hoc calibration helps or hurts under the artifact-induced shift, is unmeasured.

**Repository shortfall.** Threshold 0.5, uncalibrated soft-vote probabilities presented as "confidence".

**Solution.** Validation-only threshold policies (max-F1; FPR ≤ 1 %, 0.1 %), isotonic/Platt calibration fitted on validation, ECE/Brier/reliability diagrams, in-distribution vs external.

**Hypotheses.** H2a: Thresholds set at 1 % validation FPR produce external FPR an order of magnitude higher for artifact-bearing models and closer to target for artifact-neutral ones. H2b: Isotonic calibration lowers in-distribution ECE but does not repair external calibration (shift dominates).

**Experiment / outcome.** `analysis_calibration.py` on every run; report realised FPR at the validation-chosen threshold on each external set; ECE before/after.

**Risks.** Positive-only external sets (PhishTank) support recall but not FPR; FPR claims rest on Hannousse, Ebbu2017, PhishStorm, ISCX.

## 3. Candidate gap G3 — Temporal recall of lexical detectors over a 15-year phishing stream (I)

**Supporting literature.** Temporal bias and time-decay metrics [pendlebury2019tesseract, kan2024tesseractext]; concept-drift detection [jordaney2017transcend, barbero2022transcending]; phishing life cycle and blacklist latency [oest2020sunrise, oest2020phishtime]; concept drift in phishing detectors [fernando2026driftphish, ejaz2023lifelong, krishnan2025drift]; public URL corpora lack timestamps (noted by [pendlebury2019tesseract] for malware and by us for URLs).

**Unresolved limitation.** No study scores a frozen URL classifier against a long, timestamped phishing stream to show how recall decays with the move to https phishing (PhishTank 2026: 92 % https). Existing drift papers use synthetic or short windows.

**Solution.** Score frozen models (trained on A/B) on the 67k PhishTank URLs grouped by submission year/month; recall curves per feature set.

**Hypothesis.** H3: Recall of artifact-bearing models decreases monotonically with phishing year (as https adoption rises), while artifact-neutral models are flatter.

**Risks.** PhishTank's 2011–2024 portion is small (most entries are recent); it is positive-only, so this is a *recall-over-time* study, not a full temporal benchmark; PhishTank itself is a source for several training corpora (lineage overlap for B).

## 4. Candidate gap G4 — Lightweight character model vs handcrafted features under the grouped/external protocol (I)

**Supporting literature.** Char-level CNNs and transformers outperform handcrafted features in-distribution (collected by L1: URLNet, eXpose, Texception, URLTran, GramBeddings, PhishLang [roy2024phishlang]); but these are evaluated on random splits; GramBeddings and PhishLang discuss efficiency. Cross-dataset for deep URL models: [rashid2024domainadapt] (partial), [henry2026ensembletransfer].

**Unresolved limitation.** Whether learned character representations are *more* or *less* artifact-dependent than handcrafted features under grouped and external evaluation is not established with controlled artifact ablation (char models see the scheme and `www.` tokens directly).

**Solution.** Small char-CNN and a hybrid char+lexical model under the identical protocol, including Tier-B mutation tests (toggle scheme/`www.`).

**Hypothesis.** H4: The char-CNN matches tree ensembles in-distribution but shows higher flip rates under scheme/`www.` toggles unless trained on canonicalised input.

**Risks.** CPU-only budget limits model size and seeds (3); no transformer baseline — stated as a limitation.

## 5. Direction not pursued

- *Adversarial attacks with gradient-based or GAN-generated URLs* [aleroud2020gan, bahnsen2018deepphish, nowroozi2022advurl]: well covered by [sabir2022reliability, apruzzese2022spacephish]; our budget is better spent on label-preserving, deployment-realistic variants.
- *Content/HTML or host-based enrichment*: changes the problem (online lookups, latency, privacy); out of scope for an offline URL detector.
- *New ensemble architectures*: the audit shows the existing soft-vote does not beat RF; novelty by combination is not warranted.

## 6. Selection

| Criterion | G1 artifacts | G2 calibration | G3 temporal | G4 char models |
|---|---|---|---|---|
| Problem importance | very high | high | high | medium |
| Evidence unresolved | A + I, strong | A (no URL study) | I | I |
| Difference from prior work | first multi-corpus, raw-URL, ablation-based quantification | first for URLs | first long-horizon recall curve | incremental |
| Feasibility (CPU, data in hand) | yes | yes | yes (positive-only) | yes, limited seeds |
| Fair measurability | yes (paired, grouped) | yes | partial | yes |
| Practical usefulness | high (explains deployment FPR) | high | medium | medium |

**Primary direction: G1**, with **G2** as the operational complement (together: an *artifact-aware evaluation and training protocol*). **G3** and **G4** are secondary analyses executed under the same runs. The contribution is therefore: (1) a diagnostic showing that reported performance of lexical URL detectors is carried by nameable collection artifacts whose direction is corpus-specific; (2) a protocol (grouped splits, artifact-neutral features, validation-only FPR thresholds, calibration, external and temporal tests) implemented as reusable, tested code; (3) empirical answers on whether artifact-neutral training recovers external performance. All three remain **provisional until the runs in `results/runs/` are complete**.

## 7. Novelty check (closest prior work and how we differ)

| Work | Overlap | Difference |
|---|---|---|
| [giri2026shieldphish] (Zenodo preprint, single author) | names https/www shortcut; external benign test | we: peer-review-grade protocol, 6 corpora, 5 seeds, paired statistics, artifact *direction* analysis, probe, grouped splits, calibration, temporal recall, three model families |
| [mia2024featurestrust] | cross-dataset + SHAP | they use pre-computed feature tables (cannot ablate artifacts); two datasets; no grouped split |
| [rashid2024domainadapt] | names recording-format shift | proposes domain adaptation; no artifact ablation; abstract-only to us |
| [bhuiyan2026fragility] | probe + ablation design | e-mail text, linear models |
| [sabir2022reliability] | Alexa index-page bias noted | focus on adversarial URLs, not on evaluation protocol |
| [hannousse2021benchmark] | dataset-dependence | provides a dataset + guidelines; no artifact quantification |
