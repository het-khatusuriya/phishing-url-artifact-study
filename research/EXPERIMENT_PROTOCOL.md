# Experiment Protocol (v1 draft, 2026-10-11 — to be frozen before the main runs)

This protocol is fixed *before* looking at test results. Any later change is logged in `DECISIONS.md` with the reason.

## 1. Task and label definition

Binary classification. Positive class = malicious/phishing URL (label 1); negative = benign/legitimate (label 0). All security metrics (recall, FNR, FPR, precision, TPR@FPR) use this encoding. Datasets with finer labels (e.g. malware/defacement) are mapped to positive and this is recorded in the dataset report.

## 2. Data preparation (identical for every dataset)

1. Load raw CSV; drop rows with missing URL or label; strip whitespace. Record SHA-256 of the raw file.
2. Map labels; drop unmappable rows (count logged).
3. Normalisation-based duplicate detection (lowercase scheme and host, drop fragment, drop trailing slash on empty path, drop default ports). Keep first occurrence. **Remove** every normalised URL carrying conflicting labels.
4. Compute the grouping key = registered domain (public suffix list snapshot bundled in tldextract) or the IP literal.
5. Write `data/processed/canonical/<name>.parquet` and `results/logs/dataset_report_<name>.json` (row counts at every step, class balance, scheme/`www`/IP shares, timestamp range).

Raw features are extracted from the *original* URL string, not the normalised one.

## 3. Feature sets

| Name | Columns | Purpose |
|---|---|---|
| `baseline28` | 28 features of the original repository, code imported unchanged; `tld_type` one-hot encoded with the encoder fitted on the training partition only (`min_frequency=20`, infrequent bucket) | Faithful reproduction |
| `baseline28 − artifacts` | `baseline28` without `https_usage`, `num_subdomains` | Artifact ablation (RQ1) |
| `lexical_v2` | ~95 numeric offline features (public-suffix aware, encoding/IDN aware, token statistics, brand/keyword placement) | Improved handcrafted set |
| `lexical_v2 − artifacts` | without `https_scheme`, `had_explicit_scheme`, `has_www_prefix`, `host_num_labels`, `num_subdomain_labels_psl` | Artifact ablation |
| `char` | raw characters (≤ 200, ASCII vocabulary) | Learned representation |
| `char + lexical_v2` | both | Hybrid |

No feature uses network access.

## 4. Splitting strategies

| Strategy | Definition | Used for |
|---|---|---|
| `random` | Stratified 60/20/20 (train/val/test), seed s | Reproduction; upper bound with domain leakage |
| `grouped` | StratifiedGroupKFold (10 folds, shuffle, seed s) on registered domain; folds 0–1 → test, 2–3 → val, rest → train. No registered domain in two partitions. | Main protocol |
| `temporal` | Sort by timestamp; oldest 60 % train, next 20 % val, newest 20 % test | Only where trustworthy timestamps exist (URLhaus-based set) |
| `external` | Train on dataset A (grouped split), evaluate on the entire dataset B | Cross-collection generalisation |

For every split we store the index arrays, the class balance per partition, and the domain-overlap report (`share_test_rows_with_group_in_train`).

## 5. Models and hyper-parameters

Fixed configurations (no test-set tuning). Hyper-parameters of LR/RF/XGB are the original repository's values so that reproduction is faithful; LightGBM, stacking and the char-CNN use conventional defaults listed in `src/urlresearch/models/`. Any hyper-parameter search (if performed) uses 5-fold *grouped* CV inside the training partition only and is reported separately.

| Key | Model |
|---|---|
| `lr` | Logistic regression, standardised inputs, balanced class weights, C = 1 |
| `rf` | Random forest, 200 trees, balanced class weights |
| `xgb` | XGBoost, 200 rounds, depth 6, η = 0.1, subsample/colsample 0.8 |
| `lgbm` | LightGBM, 400 rounds, 63 leaves, η = 0.05 |
| `softvote` | Original hybrid: soft vote LR:RF:XGB with weights 1:2:2 |
| `stack` | Stacking of LR/RF/XGB with logistic meta-learner (5-fold internal CV) |
| `charcnn` | Char-CNN: emb 32, 3 parallel convs (k = 3,5,7; 128 filters), dense 128, dropout 0.3, Adam 1e-3, batch 256, ≤ 8 epochs, early stopping on validation AUC (patience 2) |
| `charcnn_hybrid` | Char-CNN with standardised `lexical_v2` features concatenated before the dense head |

## 6. Threshold policies (chosen on validation only)

`t0.5` (default), `val_maxf1` (maximises F1 on validation), `val_fpr0.01` and `val_fpr0.001` (largest-recall threshold whose validation FPR ≤ 1 % / 0.1 %). The same threshold is then applied unchanged to test and external sets.

## 7. Metrics

Per model × seed × evaluation set × policy: accuracy, precision, recall, specificity, F1, FPR, FNR, balanced accuracy, MCC, ROC-AUC, PR-AUC (average precision), TPR@FPR = 1 % and 0.1 %, log-loss, Brier score, ECE (15 bins), confusion counts. Resources: fit time, per-URL prediction latency, pickled model size, parameter count.

## 8. Repetition and statistics

- Random and grouped protocols: 5 seeds (42–46) → mean ± sd. Char models: 3 seeds (CPU budget).
- Within a seed, paired comparisons on identical test examples: paired bootstrap (1 000 resamples) of ΔAUC / ΔPR-AUC / ΔF1 with 95 % percentile CI and a two-sided bootstrap p-value; McNemar's exact test on paired correctness at the policy threshold.
- Point estimates carry 95 % percentile-bootstrap CIs (1 000 resamples).
- A difference is called "significant" only when the paired 95 % CI excludes 0 **and** the effect is consistent in sign across seeds.

## 9. Leakage controls checklist

- [ ] No normalised URL appears in two partitions (asserted in `load_dataset` + split tests).
- [ ] Grouped split: zero registered-domain overlap (asserted by `overlap_report`).
- [ ] Encoders/scalers are inside sklearn Pipelines → fitted on training rows only.
- [ ] Thresholds selected on validation; test used once per configuration.
- [ ] Char-CNN early stopping monitors validation, never test.
- [ ] External datasets are never used for any fitting or selection.
- [ ] Feature lists are fixed before experiments (this document).

## 10. Robustness and diagnostics (P2)

- Mutation tests (`evaluation/mutations.py`): Tier A RFC-equivalent transformations (label preserved by construction); Tier B presentation variants (`www` toggle, scheme toggle, tracking parameter) with the stated assumption that intent is unchanged. Report flip rate, mean |Δp|, AUC/recall/FPR before vs after.
- SHAP TreeExplainer on XGBoost (3 000 test URLs) for each feature set / split.
- Reliability diagrams and ECE; optional post-hoc calibration (isotonic/Platt) fitted on validation.
- Error analysis: FPs and FNs stratified by registered-domain novelty, length, IP host, `www`/scheme, encoding, and free-hosting suffix.
