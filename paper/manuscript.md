# When the Scheme Is the Signal: Collection Artifacts, Domain Leakage and Cross-Corpus Failure in Lexical Phishing-URL Detection

*Working draft — 2026-10-11. Every number in Sections 5–6 is generated from `results/` (see `results/tables/paper_tables.md`); entries marked **[pending]** are experiments still running and must not be read as results.*

## Abstract

[Written last; see end of file for the status of the quantitative claims.]

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

[pending — generated after all runs complete]

## 7. Discussion

[pending]

## 8. Threats to Validity and Limitations

[pending — draft items: original dataset unavailable; corpus B is a lineage sample, not the original; public corpora carry their own artifacts, so "external" means "differently collected", not "realistic traffic"; balanced prevalence; positive-only timestamped feeds concentrated in 2021–2026; registered-domain grouping does not remove kit-level near-duplicates across domains; Tier B mutations assume label preservation; no transformer baseline; char models with fewer seeds and a short training budget; canonicalisation and LOCO were added after inspecting the first baseline run.]

## 9. Conclusion

[pending]

## References

Keys refer to `research/references.bib` (verified entries only).
