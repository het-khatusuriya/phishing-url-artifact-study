# When the Scheme Is the Signal: Collection Artifacts, Domain Leakage and Cross-Corpus Failure in Lexical Phishing-URL Detection

*Working draft — 2026-10-11. Every number in Sections 5–6 is generated from `results/` (see `results/tables/paper_tables.md`); entries marked **[pending]** are experiments still running and must not be read as results.*

## Abstract

*Provisional — based on the completed runs listed in §6; to be finalised when the experiment matrix completes.*

Lexical URL classifiers are routinely reported with 95–99 % accuracy on public phishing benchmarks, yet they fail when moved to differently collected data. We audit a typical detector (28 lexical features and a weighted soft-voting ensemble of logistic regression, random forest and XGBoost) and six public corpora with raw URLs, plus three live feeds. In one widely used corpus, every benign URL is an `https://www.` homepage; across corpora, the scheme, the `www.` prefix and URL length change in strength and even in direction of association with phishing. A linear probe identifies the source corpus of a benign URL with 83 % accuracy (chance 17 %); dropping artifact columns barely changes this, while canonicalising the URL string lowers it to 62 %. Models trained on PhiUSIIL reach ROC-AUC 0.998–0.999 with or without registered-domain-grouped splitting, yet with a threshold set for a 1 % false-positive budget they flag 99–100 % of benign URLs in four other corpora, and their ROC-AUC falls to 0.34–0.78, below chance on two corpora. Training on five pooled corpora restores ranking on a held-out corpus (ROC-AUC 0.77–0.98) but leaves validation-chosen thresholds badly miscalibrated, under-flagging one unseen corpus and over-flagging another. We release a tested, reproducible pipeline and argue that URL detectors should be evaluated across corpora, at fixed false-positive budgets, with recording format canonicalised.

**Keywords:** phishing detection; malicious URL detection; lexical features; dataset bias; shortcut learning; cross-dataset generalisation; domain-grouped evaluation; calibration; machine learning for security

---

## 1. Introduction

Phishing remains one of the most damaging and highest-volume attack vectors on the web, and most phishing campaigns live for hours rather than days [oest2020sunrise]. Blacklists react too slowly to protect users during that window [oest2020phishtime], which motivates *proactive* detectors that judge a URL from its string alone, before the page is fetched. Lexical URL classifiers are attractive for this role: they need no network access, add sub-millisecond latency, and are routinely reported with accuracies of 95–99 % [ma2009beyond, le2011phishdef, mamun2016iscxurl, sahingoz2019machine, sankaranarayanan2024ensemble, khan2026stacking].

These numbers are hard to reconcile with what happens when such models leave the dataset they were trained on. Cross-dataset accuracy of URL classifiers has been reported at 51–59 % [mia2024featurestrust] and 57 % [henry2026ensembletransfer]; detectors "work effectively only when the test sets are split from the same training dataset" [rashid2024domainadapt]; and models trained against homepage-only benign sets lose 27–39 points on legitimate login URLs [sanchezpaniagua2022phishing]. The security-ML literature has a name for the likely cause — *spurious correlations from sampling bias* [arp2022dosdonts] — and phishing researchers have long warned that benign URLs drawn from popularity lists are structurally unlike phishing URLs [marchal2018designing, elaassal2020benchmarking, hannousse2021benchmark, sabir2022reliability]. What is missing is a measurement: *which* properties of public URL corpora carry the reported performance, whether they point the same way across corpora, and whether removing them helps.

This study began as an audit of a course-project detector (28 lexical features, a 1:2:2 soft-voting ensemble of logistic regression, random forest and XGBoost, reported test accuracy 96.8 %). Its two most influential features by SHAP were the URL scheme (`https`) and a subdomain count driven by the `www.` prefix, and it classified `https://google.com/` as malicious with 88 % probability. We show that this is not an implementation accident but a property of the data the field evaluates on.

**Research questions.**
- **RQ1.** How much of the in-distribution performance of lexical URL classifiers on public phishing corpora is carried by nameable *collection artifacts* (scheme, `www.` prefix, homepage-only benign URLs) and by registered-domain memorisation?
- **RQ2.** Do these artifacts point in the same direction across corpora, and does that explain cross-corpus failure?
- **RQ3.** Does an artifact-aware recipe — string canonicalisation, domain-grouped model selection, validation-chosen operating thresholds — restore performance on unseen corpora, and do probabilities and thresholds remain reliable under shift?

**Contributions.** (Stated as *provisional* until every run in §6 is complete; each is tied to a table.)
1. A per-class artifact audit of six public phishing-URL corpora and three live feeds, showing that the dominant artifacts reverse sign between corpora (§5.1, Table T1, DATASET_AUDIT).
2. A dataset-identification probe showing that the source corpus of a benign URL is predictable from lexical features far above chance, that dropping artifact columns barely changes this, and that canonicalising the string does (§6.2, Table T10).
3. A controlled comparison of random versus registered-domain-grouped splits, in-distribution versus external and leave-one-corpus-out evaluation, for three feature representations and four model families including a character CNN (§6.3–6.5).
4. An operating-point analysis: calibration and the transfer of validation-chosen false-positive thresholds to unseen corpora (§6.6).
5. An open, tested implementation (parser, features, splits, metrics, runner, 90+ unit tests) and full provenance of every dataset and number.

## 2. Related Work

**Lexical features and classical learners.** The URL string alone was shown to separate phishing from benign pages in early measurement work [mcgrath2008behind, garera2007framework], and bag-of-token and host features reached 95–99 % accuracy [ma2009beyond, ma2009identifying, ma2011learning]. Later work added obfuscation-resistant and online features [le2011phishdef, blum2010lexical], distributional character statistics [verma2015character], word-level NLP features [sahingoz2019machine], search-engine relatedness [marchal2014phishstorm] and benchmark corpora [mamun2016iscxurl, hannousse2021benchmark, prasad2024phiusiil]. Tree ensembles are consistently strongest among classical learners, and stacking or voting adds about one point on random splits [sankaranarayanan2024ensemble, khan2026stacking, rao2020catchphish, chiew2019hybrid].

**Learned representations.** Character CNNs and LSTMs [saxe2017expose, bahnsen2017rnnurl, le2018urlnet, tajaddodianfar2020texception, aljofey2020effective, bozkir2023grambeddings, sahingoz2024dephides] and transformers or URL-pretrained encoders [maneriker2021urltran, rudd2020training, wang2023phishbert, li2025urlbert, liu2024transurl, roy2024phishlang] improve in-distribution scores, especially at low false-positive rates on production telemetry. TransURL is the only representation paper we found with a substantial cross-dataset test, where all models degrade sharply [liu2024transurl]. Notably, Aljofey et al. strip `http://`, `https://` and `www.` before modelling without measuring the effect [aljofey2020effective].

**Evaluation realism.** Arp et al. identify sampling bias, spurious correlations and the base-rate fallacy as pervasive pitfalls of security ML [arp2022dosdonts]; TESSERACT shows that temporally inconsistent splits inflate malware F1 [pendlebury2019tesseract]; and pragmatic assessment calls for repeated trials over several datasets [apruzzese2023pragmatic]. For phishing, guidelines require diverse benign URLs with paths, realistic prevalence and temporal tests [marchal2018designing]; balanced, Alexa-derived benchmarks are criticised [elaassal2020benchmarking, das2020sokphishing, alam2026philter]; benign index pages are said to "create a bias in the data" [sabir2022reliability]; and leakage and base rates inflate web-page benchmarks [dalton2025phreshphish]. Cross-dataset studies of URL detectors report collapse [mia2024featurestrust, rashid2024domainadapt, henry2026ensembletransfer] but operate on pre-computed feature tables or do not isolate the mechanism. The closest work is a single-author preprint that names the `https://` and `www.` shortcut and tests canonicalisation on one external benign set [giri2026shieldphish], and a study of phishing *e-mail* that uses a corpus-identification probe and artifact-removal ablations [bhuiyan2026fragility].

**Robustness, explanation and calibration.** URL detectors are brittle to cheap adversarial URLs [sabir2022reliability, apruzzese2022spacephish, aleroud2020gan], and real attackers favour such cheap manipulations [apruzzese2023realattackers]. SHAP [lundberg2017shap, lundberg2020treeexplainer] is widely used for feature selection in phishing work [alfayoumi2024xaiphd, kehkashan2025explainable] but rarely to diagnose artifacts [mia2024featurestrust]. Calibration under dataset shift has been studied for Android malware [li2021malwarecalibration] building on [niculescumizil2005calibration, guo2017calibration], but we found no study for phishing URLs.

**Positioning.** We work on raw URLs from six public corpora, name and quantify specific artifacts per class and per corpus, separate artifact effects from domain memorisation with grouped splits, test the recipe under leave-one-corpus-out transfer, and measure whether operating thresholds survive the shift. A full comparison table is in `research/LITERATURE_SURVEY_TABLE.md`.

## 3. Problem Definition and Hypotheses

Given a URL string *u*, a detector outputs *p(u)* ≈ P(malicious | *u*), and flags *u* when *p(u)* ≥ τ. We call a property *a(u)* a **collection artifact** if (i) it is determined by how a source recorded or sampled URLs rather than by the URL's intent, and (ii) its class-conditional distribution differs within a corpus. The scheme prefix (absent, `http`, `https`), a leading `www.` label, and the restriction of a benign source to bare homepages satisfy both conditions in the corpora studied (§5.1).

Hypotheses (pre-registered in `research/RESEARCH_GAPS.md`; H1c and canonicalisation were added post hoc as described in `EXPERIMENT_PROTOCOL.md`):
- **H1a** Removing artifact features changes in-distribution ROC-AUC only marginally but changes false-positive rates on external corpora substantially.
- **H1b** Random splits over-estimate grouped-split performance, most on corpora with many URLs per registered domain.
- **H1c** The source corpus of a URL is identifiable from lexical features well above chance.
- **H2** Thresholds selected for a 1 % false-positive budget on validation data do not hold on external corpora; post-hoc calibration does not repair this.
- **H3** Recall on timestamped phishing feeds changes with submission year as the share of https phishing rises.
- **H4** A character CNN shares the artifact dependence of lexical models unless its input is canonicalised.

## 4. Method

### 4.1 Pipeline overview

```
raw sources ──► prepare_external.py ──► canonical corpora (dedup, conflict removal, registered-domain group)
                                                │
             ┌──────────────────────────────────┼─────────────────────────────┐
             ▼                                  ▼                             ▼
   split: random | grouped | LOCO      features: baseline28 | lexical_v2 |   char sequence
   (indices + overlap report saved)    lexical_v2 − artifacts | canon       (raw or canonical)
             └──────────────► models: LR, RF, XGB, LGBM, soft vote 1:2:2, char-CNN, hybrid
                                        │
                     validation: thresholds (0.5, max-F1, FPR≤1 %, FPR≤0.1 %), calibrators
                                        │
                 test / external / feeds: metrics, CIs, paired tests, SHAP, mutations, errors
```

### 4.2 Data handling

Each source is mapped to `url, label` with malicious = 1. URLs are stripped of surrounding whitespace; a *normalised key* (lower-case scheme and host, default port and fragment removed, empty path collapsed) is used only for duplicate detection; all normalised keys carrying both labels are removed. Features are always computed on the original string. The grouping key is the registered domain — the label directly below the public suffix, computed with the offline Public Suffix List snapshot of `tldextract` 5.3.1 — or the literal address for IP hosts.

### 4.3 URL parsing

The parser accepts any string, prepends `http://` when no scheme is present (recording the fact), and never raises: malformed authorities (e.g. unmatched IPv6 brackets) and invalid ports set a `parse_error` flag. It extracts scheme, userinfo, host, port, path, query, fragment, subdomain, registered domain and public suffix, IP and IPv6 status, and the IDNA-decoded host. Tests cover missing schemes, IPv4/IPv6 literals, ports, userinfo, punycode, Unicode hosts, percent-encoding (including double encoding), 15 kB strings and non-URL strings (`tests/test_feature_extractor.py`).

### 4.4 Representations

- **baseline28** — the original project's 28 features computed by its unmodified code (lengths and character counts, digit-to-letter ratio, entropy, subdomain count, last host label as a categorical `tld_type`, IP host, `https`, shortener and suspicious-TLD lists, keyword and brand substrings, hyphen and randomness heuristics). `tld_type` is one-hot encoded with the encoder fitted on training rows only and TLDs with fewer than 20 training occurrences pooled.
- **lexical_v2** — 91 numeric features computed from the parsed components: whole-URL shape (length, entropy, character-class counts and ratios, longest digit run, token statistics, hex tokens, double encoding); scheme and authority (`https`, explicit scheme, `www.` prefix, userinfo, ports); hostname (length, entropy, label counts with and without the public suffix, registered-domain length and entropy, digit and hyphen counts, consonant runs, IP/punycode/non-ASCII, abused suffix, free-hosting suffix, shortener); brand tokens *placed* in subdomain, registered domain or path rather than matched as raw substrings; path, query and fragment structure (depth, extensions, embedded URLs or e-mail addresses, keyword placement).
- **lexical_v2 − artifacts** — `lexical_v2` without the five columns that encode recording format: `https_scheme`, `had_explicit_scheme`, `has_www_prefix`, `host_num_labels`, `num_subdomain_labels_psl`. The analogous ablation of baseline28 removes `https_usage` and `num_subdomains`.
- **lexical_v2_canon** — the string is first *canonicalised* by removing the scheme and one leading `www.`/`wwwN.` label (regular expression `^(?:[a-zA-Z][a-zA-Z0-9+.-]*://)?(?:www\d?\.)?`); `lexical_v2` is computed on the result and the five artifact columns are dropped, leaving 86 features. By construction every feature is invariant to the presence or form of the scheme and `www.` prefix, which is unit-tested.
- **char** — the first 160 characters as ASCII codes (others mapped to an unknown symbol), optionally canonicalised.

No representation uses network lookups.

### 4.5 Models

Logistic regression (standardised inputs, C = 1, balanced class weights), random forest (200 trees, balanced class weights) and XGBoost (200 rounds, depth 6, learning rate 0.1, row and column subsampling 0.8) keep the original project's settings so that the reproduction is faithful; LightGBM (400 rounds, 63 leaves, learning rate 0.05) is added as a second boosting family; the **soft vote** averages LR, RF and XGBoost probabilities with weights 1:2:2 as in the original project. The **char-CNN** follows eXpose/URLNet [saxe2017expose, le2018urlnet] at small scale: a 32-dimensional character embedding, three parallel 1-D convolutions (kernel widths 3, 5, 7; 128 filters each) with ReLU and global max-pooling, dropout 0.3, a 128-unit dense layer and a sigmoid output (115,329 parameters). The **hybrid** concatenates standardised `lexical_v2 − artifacts` features to the pooled convolutional vector before the dense layer. Char models are trained with Adam (learning rate 10⁻³, batch 256), class-balanced binary cross-entropy, at most 5 epochs or 20 minutes, keeping the epoch with the best validation ROC-AUC (patience 2). No hyper-parameter was tuned on test or external data.

### 4.6 Operating thresholds and calibration

For each model and seed, four thresholds are fixed on the validation split: τ = 0.5; the τ maximising validation F1; and the smallest τ whose validation false-positive rate is at most 1 % (respectively 0.1 %), i.e. the most sensitive threshold within the false-positive budget. The same τ is applied unchanged to the test split and to every external corpus. Post-hoc calibration (isotonic regression and Platt scaling) is fitted on validation scores only.

### 4.7 Evaluation

Positive class: malicious. Reported: accuracy, precision, recall, specificity, F1, FPR, FNR, balanced accuracy, MCC, ROC-AUC, PR-AUC (average precision), TPR at FPR 1 % and 0.1 %, log-loss, Brier score and expected calibration error (15 equal-width bins). On positive-only feeds only recall is defined. Uncertainty: mean ± standard deviation over seeds; 95 % percentile-bootstrap intervals (1,000 resamples) for single-seed point estimates; paired bootstrap of metric differences and McNemar's exact test for comparisons on identical test URLs. A difference is called significant only when the paired 95 % interval excludes zero and its sign is the same for all seeds.

**Probe.** For each class separately, 8,000 URLs per corpus (fewer where unavailable) are pooled from six corpora, and a multinomial logistic regression predicts the source corpus from a representation under 5-fold cross-validation grouped by registered domain. Chance is 1/6.

**Explanations.** TreeExplainer SHAP values [lundberg2020treeexplainer] for XGBoost on 3,000 test URLs.

**Label-preserving variants.** Tier A transformations are equivalent under RFC 3986 and preserve the label by construction: upper-casing scheme and host, adding an empty-path slash, adding the default port, percent-encoding one unreserved path character, adding a fragment. Tier B transformations change only presentation and are *assumed* label-preserving: toggling a leading `www.`, toggling `http`/`https`, appending a tracking parameter. We report the share of predictions that flip at τ = 0.5 and the mean absolute change in probability.

## 5. Experimental Setup

### 5.1 Corpora

[Table T1 — generated; see `results/tables/paper_tables.md`.] Corpus A is PhiUSIIL [prasad2024phiusiil] (234,687 URLs after cleaning). Corpus B is a 253,098-URL stratified sample of the Kaggle/HuggingFace lineage (`Mitake/PhishingURLsANDBenignURLs`), sized and balanced like the original project's unavailable dataset (129,420 / 123,678); 252,394 remain after cleaning. External labelled corpora: Hannousse & Yahiouche 2021 [hannousse2021benchmark], Ebbu2017 [sahingoz2019machine], PhishStorm [marchal2014phishstorm], ISCX-URL-2016 benign and phishing lists [mamun2016iscxurl], and (two early runs only) the 651k Kaggle corpus [siddhartha2021maliciousurls]. Positive-only feeds: PhishTank verified-online dump with submission times (67,326 URLs, 2011–2026; only 64 submitted before 2021), URLhaus malware URLs (72,847; scored to check out-of-task behaviour), and an OpenPhish snapshot (300).

The original project's dataset could not be obtained; its provenance analysis (`research/DATASET_AUDIT.md` §1) indicates a scheme-normalised compilation of the same Kaggle lineage with a newer phishing source.

### 5.2 Splits

Random: stratified 60/20/20. Grouped: `StratifiedGroupKFold` with 10 folds on registered domain; two folds for test, two for validation, six for training; no registered domain occurs in two partitions. LOCO: for each of six labelled corpora, the other five are pooled (each capped at 50,000 URLs, stratified), split by registered domain into train/validation/test, and the whole held-out corpus is the evaluation set. Split indices, class balance and domain overlap are saved for every seed.

### 5.3 Environment

Intel Core i7-1355U (10 cores, 12 threads), 16 GB RAM, no GPU; Windows 11; Python 3.10.11, scikit-learn 1.7.2, XGBoost 3.2.0, LightGBM 4.7.0, PyTorch 2.13.0 (CPU), SHAP 0.49.1, NumPy 1.26.4, pandas 2.3.3, tldextract 5.3.1. Seeds 42–46 (tabular), 42–44 (LOCO and char models on corpus A), 42 (char models on corpus B). Every run directory contains `config.json` and `environment.json`.

## 6. Results

Status of the evidence on 2026-10-12: complete for §6.1, §6.2 and the baseline-feature runs on corpus A (random split, 5 seeds; grouped split, 5 seeds); partial for leave-one-corpus-out (2 of 6 held-out corpora); **pending** for corpus B, `lexical_v2` and canonicalised runs, character models, calibration, SHAP, mutation and error analyses. Pending items are listed explicitly and no number is extrapolated.

### 6.1 Baseline reproduction

The original repository's code path — its unmodified feature extractor, data-splitting function, model factories, ensemble and metric functions — runs end to end on both substitute corpora (Table T2). On PhiUSIIL it scores higher than the project reported on its own unavailable data: the 1:2:2 soft vote reaches test accuracy 0.9970, F1 0.9965 and ROC-AUC 0.9988, against the stored accuracy of 0.9678 on the original data. The four models are within 0.0018 accuracy of each other, and the ensemble exceeds XGBoost by only 0.0002 ROC-AUC. This matches the audit's observation that the ensemble did not beat random forest on the original data either.

On corpus B the same code reaches only 0.8484 accuracy and 0.9317 ROC-AUC. The cause is a defect, not a property of the corpus. 99.8 % of corpus-B URLs carry no scheme, and for such input the original extractor parses no host at all, so domain length, subdomain count and TLD collapse to constants (verified on single examples; regression test in the repository). Corpus-B results that use `baseline28` therefore measure this defect as well as the model. `lexical_v2` uses a parser that handles scheme-less input.

### 6.2 Collection artifacts differ in size and direction across corpora (RQ1, RQ2)

Figure 1 (`results/figures/dataset_artifacts.png`) and DATASET_AUDIT §3 report the class-conditional shares of three recording properties. In PhiUSIIL, **every** benign URL is an `https://www.` homepage with an empty path, against 48 % https, 42 % `www.` and 72 % homepages among phishing URLs. A single binary indicator therefore separates the classes well: the single-feature ROC-AUC is 0.21 for the `www.` prefix and 0.24 for the scheme, where values far below 0.5 mean "more frequent in benign URLs".

The same indicators carry little or opposite information elsewhere. The `www.` prefix has single-feature AUC 0.27–0.34 in Hannousse 2021, Ebbu2017 and PhishStorm, but 0.71 in ISCX-2016 and 0.69 in the Kaggle corpus, where it marks *phishing*. URL length points to phishing in PhiUSIIL and PhishStorm (0.72–0.73) and to benign in ISCX-2016 (0.24), whose 35,378 benign URLs are deep pages from only about 300 sites. The present-day phishing population differs again: 92 % of PhishTank's verified-online URLs are https and only 4 % start with `www.`.

The dataset-identification probe (Table T10) shows that these differences are learnable. With `lexical_v2`, a linear model identifies which of six corpora a **benign** URL comes from with accuracy 0.830 (chance 0.167), and a malicious URL with accuracy 0.606. Removing the five artifact columns barely changes this (0.814 and 0.578), because the scheme still leaks through slash, colon and length counts; the two scheme-less corpora stay identifiable at 0.97 or higher. Canonicalising the string before computing features lowers the accuracies to 0.617 and 0.428 and makes the scheme-less corpus B nearly indistinguishable among benign URLs (0.184). PhiUSIIL's benign URLs remain identifiable at 0.981 even after canonicalisation: being a bare homepage is a sampling artifact that no string transformation removes. The original 28 features give 0.803 and 0.577. H1c is supported.

### 6.3 Random versus registered-domain-grouped splits on corpus A (RQ1, H1b)

Random splitting leaks domains asymmetrically. With seed 42, 59.4 % of phishing test URLs share a registered domain with a training URL, against 2.4 % of benign test URLs (26.7 % overall; seed 43: 58.7 % and 2.3 %). Grouped splitting removes the overlap by construction (Table T3; `split_domain_overlap.png`).

Despite this leakage, grouping hardly changes in-distribution performance on PhiUSIIL with the baseline features (5 seeds each):

| Model | ROC-AUC random | ROC-AUC grouped | F1@0.5 random | F1@0.5 grouped |
|---|---|---|---|---|
| Logistic regression | 0.998 ± 0.000 | 0.998 ± 0.000 | 0.995 ± 0.001 | 0.993 ± 0.003 |
| Random forest | 0.998 ± 0.000 | 0.998 ± 0.000 | 0.996 ± 0.001 | 0.994 ± 0.003 |
| XGBoost | 0.999 ± 0.000 | 0.999 ± 0.000 | 0.996 ± 0.001 | 0.995 ± 0.003 |
| Soft vote 1:2:2 | 0.999 ± 0.000 | 0.999 ± 0.000 | 0.996 ± 0.001 | 0.995 ± 0.003 |

H1b is **not supported on corpus A**. The models do not need memorised domains because the recording artifacts already separate the classes. Whether grouping matters on corpora with many URLs per domain (corpus B; ISCX-2016 within LOCO) is **pending**.

### 6.4 External corpora: near-total false-positive rates (RQ2, H1a, H2)

Models trained on corpus A were applied unchanged to every other corpus, using the threshold chosen on corpus-A validation data for a 1 % false-positive budget (Figure 2, `external_roc_auc_A_b28_grouped.png`; Table T4). In-distribution the threshold holds: realised test FPR is 0.009–0.010 at recall 0.992–0.995.

On external corpora it fails for every model. **99.4–100 % of the benign URLs of Hannousse 2021, Ebbu2017, PhishStorm and ISCX-2016 are flagged.** On corpus B, logistic regression flags 74 % and every tree model and the soft vote flag 100 %. Ranking quality collapses as well. External ROC-AUC is 0.56–0.76 on Hannousse, Ebbu2017 and PhishStorm and falls **below chance** on ISCX-2016 (0.42–0.47) and the Kaggle corpus (0.35–0.48), the two corpora where `www.` marks phishing rather than benign URLs (§6.2).

The in-distribution model ranking (all ≥ 0.998) bears no relation to the external ranking. Random forest, which ties for best in-distribution, has the lowest external AUC on Hannousse, Ebbu2017 and PhishStorm (0.56–0.62).

Recall on the positive-only feeds is 0.99–1.00 (PhishTank 0.992–0.996, OpenPhish 1.000, URLhaus malware URLs 1.000). This is not evidence of good detection: a detector that flags every URL not shaped like an `https://www.` homepage has near-perfect recall and near-total FPR. At an operational prevalence of 1 % malicious URLs, recall 0.995 with FPR 0.994 gives a precision of about 1 %, no better than flagging at random.

The random-split runs give the same picture (FPR 0.994–1.000 on the four independent labelled corpora, 0.74–1.00 on corpus B; external AUC 0.34–0.78; Table T4). H2 is supported for the baseline representation.

*Preliminary (1 of 5 seeds):* removing the two artifact columns of the original features (`https_usage`, `num_subdomains`) barely changes in-distribution ROC-AUC (XGBoost 0.999, soft vote 0.999, random forest 0.997, logistic regression 0.987) and does not repair external behaviour: 94–100 % of the benign URLs of Hannousse 2021, Ebbu2017, PhishStorm and ISCX-2016 are still flagged, and XGBoost's ROC-AUC on ISCX-2016 falls further, to 0.10. This is consistent with the probe (§6.2): the shortcut survives column removal because the remaining length and path features still encode the homepage-only benign class. The remaining seeds, `lexical_v2` and the canonicalised representation are **pending** (runs `A_b28noart_grouped`, `A_v2noart_grouped`, `A_v2canon_grouped`).

### 6.5 Leave-one-corpus-out: training on diverse corpora (RQ3)

So far two held-out corpora have been evaluated. With PhiUSIIL held out (3 seeds), using models trained on a pool of the other five corpora with grouped train/validation/test splits. Training on diverse data changes the failure mode. Ranking transfers well to the held-out corpus: with `lexical_v2`, ROC-AUC is 0.977 (XGBoost), 0.966 (LR) and 0.891 (RF), and FPR at the validation-chosen 1 % threshold is 0.000. Recall at that threshold, however, falls to 0.42 (XGBoost), 0.25 (RF) and 0.15 (LR) on PhiUSIIL phishing, and to 0.16–0.44 on PhishTank. The held-out corpus's score distribution has shifted, so a threshold that is right for the pool is far too conservative for the new corpus.

Removing the five artifact columns *lowers* held-out ROC-AUC (XGBoost 0.977 → 0.878; LR 0.966 → 0.888; RF 0.891 → 0.866), while recall at the validation threshold stays similar (0.32–0.42). In this direction the artifact columns carried information that transferred, so artifact removal is not uniformly beneficial.

With corpus B held out (`lexical_v2`, 3 seeds), ranking transfers less well: held-out ROC-AUC is 0.874 ± 0.004 (XGBoost), 0.865 ± 0.004 (LR) and 0.772 ± 0.003 (RF), against 0.934–0.980 on the pool's own test split. Here the validation threshold errs in the *opposite* direction from the PhiUSIIL case: at the threshold chosen for a 1 % false-positive budget, the models flag 16.0 % (XGBoost), 17.6 % (RF) and 94.6 % (LR) of corpus-B benign URLs, at recall 0.71, 0.42 and 1.00. The same recipe thus under-flags one unseen corpus and over-flags another.

Removing the five artifact columns (3 seeds) changes held-out ROC-AUC on corpus B only slightly (XGBoost 0.874 → 0.849; LR 0.865 → 0.883; RF 0.772 → 0.780) but removes logistic regression's over-flagging: its FPR at the validation threshold falls from 0.946 ± 0.034 to 0.152 ± 0.113, with recall 0.72 instead of 1.00. For the tree models FPR stays at 0.15–0.19. Corpus B stores URLs without a scheme, so a linear model that gives weight to the scheme columns shifts all corpus-B scores at once; without those columns the shift disappears. The remaining four held-out corpora and the canonicalised representation are **pending**.

### 6.6 Pending analyses

These are implemented and will run on the completed matrix; no result is claimed for them yet:
- random vs grouped splits on corpus B;
- `lexical_v2` and artifact ablations on both corpora;
- canonicalised features, in-corpus and LOCO (H1a);
- character CNN, canonicalised character CNN and hybrid (H4);
- paired bootstrap and McNemar comparisons (T6);
- post-hoc calibration under shift (T7, H2);
- label-preserving mutation flip rates (T8);
- temporal recall on PhishTank by year (H3; only 64 URLs predate 2021, so the analysis covers 2021–2026);
- SHAP and error analysis;
- computational cost (T9; two timings from 2026-10-11 are inflated by a system standby and are excluded).

## 7. Discussion

*Provisional; restricted to the completed evidence.*

**What the high scores measure.** On PhiUSIIL the original pipeline reaches ROC-AUC 0.999 whether or not registered domains are shared between training and test, and it then flags essentially all benign URLs of four independently collected corpora. With the probe results, the simplest explanation is that these models learn *how each class was recorded* — benign as `https://www.` homepages, phishing as everything else — rather than properties of phishing URLs. This is the shortcut-learning pitfall described by Arp et al. [arp2022dosdonts], here with named, measurable artifacts. It matches the benign-homepage effect reported for login URLs [sanchezpaniagua2022phishing] and the `https://`/`www.` shortcut reported in a recent preprint [giri2026shieldphish]. The original project's misclassification of `https://google.com/` is the same phenomenon seen through one URL.

**Why cross-corpus results vary so much.** The artifacts reverse sign across corpora (§6.2), so a model's external performance depends on whether the target corpus happens to share the training corpus's recording conventions. This explains the below-chance AUC on ISCX-2016 and the Kaggle corpus. It also explains why cross-dataset numbers in the literature range from near chance [mia2024featurestrust, henry2026ensembletransfer] to moderate [liu2024transurl]: the outcome is largely a property of the dataset pair.

**Model choice is secondary.** In-distribution, the soft vote, XGBoost, random forest and logistic regression differ by at most 0.001 ROC-AUC. Externally they differ by up to 0.2, in an order unrelated to their in-distribution ranking. A single random split therefore says little about which model, ensemble or otherwise, to deploy.

**Thresholds are the operational failure.** Even where ranking transfers (LOCO with PhiUSIIL held out, AUC up to 0.977), a threshold chosen for a 1 % FPR budget on the training distribution transfers badly: it over-flags in one direction and under-flags in the other. Deployment would need threshold recalibration on traffic from the target environment, a step the public-benchmark protocol never exercises.

**What is not established yet.** Until the pending runs finish, it remains open whether canonicalised features or character models on canonical input reduce the external failure, whether random splits inflate results on domain-heavy corpora, and whether calibration repairs threshold transfer. All conclusions above come from balanced public corpora and the baseline representation.

## 8. Threats to Validity and Limitations

- **Original data unavailable.** The project's own 253,098-URL dataset could not be obtained. Conclusions about it rest on analogy with PhiUSIIL, whose benign class has the same `https://www.` form, and with a size-matched sample of its probable source lineage (corpus B).
- **"External" is not "real traffic".** Every external corpus is itself a public compilation with its own artifacts. A model that transferred perfectly between them would still not be validated on real user traffic, so these results show failure modes, not deployment performance.
- **Balanced prevalence.** All labelled corpora are roughly balanced; precision at realistic prevalence is derived analytically, not measured.
- **Temporal coverage.** Timestamped data are positive-only (PhishTank, URLhaus) and concentrated in 2021–2026. No temporally split benchmark with benign URLs was available.
- **Grouping granularity.** Registered-domain grouping does not remove near-duplicates that share a phishing kit across domains, or benign URLs of one organisation under several domains.
- **Label noise.** Labels are inherited from the sources (blacklists, curated lists); no URL was relabelled.
- **Mutations.** Tier B variants (scheme and `www.` toggles) are assumed, not proven, to preserve the label.
- **Model coverage and budget.** No transformer baseline was trained (CPU only), and character models use a short training budget and fewer seeds.
- **Post-hoc additions.** Canonicalised features and the leave-one-corpus-out design were added after the dataset probe and after inspecting the first baseline run. They are reported as such and use the same fixed hyper-parameters.
- **Incomplete runs.** Part of the experiment matrix is still running; §6 marks every pending item.

## 9. Conclusion

*Provisional.* Lexical phishing-URL detectors evaluated on a public corpus can reach ROC-AUC 0.999 while flagging 99–100 % of the benign URLs of four other public corpora. The cause we can name and measure is how each corpus recorded its classes — scheme, `www.` prefix and homepage-only benign URLs — whose predictive direction reverses between corpora, so the source corpus of a URL is predictable from lexical features far above chance. Training on several corpora restores much of the ranking ability on an unseen corpus but leaves operating thresholds unreliable.

Future work should evaluate URL detectors on benign traffic sampled the way deployed systems see it, canonicalise recording format before learning, report results across corpora and at fixed false-positive budgets, and treat threshold recalibration as part of deployment. The pending runs will establish whether canonicalisation and character-level models change these conclusions.

## References

Keys refer to `research/references.bib` (verified entries only).
