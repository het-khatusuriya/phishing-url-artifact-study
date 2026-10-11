# Repository Audit — Malicious-URL-Detection-Project

Audit date: 2026-10-11. Audited commit: `65364b4` ("Initial commit - Malicious URL Detection project"), the only commit in the repository. Research work proceeds on branch `research-v2`; the original code is preserved on `main`.

Method: every file in the repository was read in full. Notebook execution history (stored outputs, execution counts, kernel metadata) was extracted programmatically and compared with the Python modules. No stored output was taken as proof of reproducibility; see Section 6.

---

## 1. Repository map

| Path | Size | Status | Notes |
|---|---|---|---|
| `app.py` | 1.4 KB | Functional but fragile | Flask API; loads `weighted_soft_voting_ensemble.joblib` from the working directory (not `models/`); serves `index.html` which does not exist (the file is named `idex.html`). Bare `except:`. Reports a "confidence" and labels a URL "Legitimate". |
| `feature_extractor.py` (root) | 5.9 KB | Functional | Byte-identical duplicate of `src/features/feature_extractor.py`. |
| `idex.html` | 4.6 KB | Functional UI | Calls `/api/predict`; shows a green check for "Legitimate". Misnamed. |
| `src/config.py` | 0 B | Empty | |
| `src/utils.py` | 0 B | Empty | |
| `src/data/load_data.py` | 0 B | Empty | |
| `src/data/data_cleaning.py` | 1.7 KB | Implemented, **not used by notebooks** | `normalize_url` lowercases scheme and netloc and rebuilds the URL. Notebook 02 only strips whitespace and lowercases labels, so training data never went through this module. Also `clean_dataset` triggers a pandas `SettingWithCopy` pattern (slice then assign). |
| `src/data/data_splitting.py` | 1.0 KB | Implemented, used by NB 05 | Stratified random 60/20/20 split, `random_state=42`. Maps `legitimate→0`, `phishing→1`. No grouping by domain, no temporal option. |
| `src/features/feature_extractor.py` | 5.9 KB | Implemented, used by NB 03 (copied inline) and NB 09 | 28 features; see Section 3. |
| `src/features/url_features.py`, `domain_features.py`, `security_features.py` | 0 B | Empty placeholders | |
| `src/models/logistic_regression.py`, `random_forest.py`, `xgboost.py`, `ensemble.py` | 0.5–0.6 KB | Implemented, used by NB 06 | Factory functions; fixed hyperparameters (no tuning anywhere). |
| `src/evaluation/metrics.py`, `confusion_matrix.py` | 0.7–1.0 KB | Implemented, used by NB 07 | Accuracy/precision/recall/F1 + confusion counts only. No ROC-AUC/PR-AUC/FPR/FNR/specificity. |
| `src/evaluation/model_comparison.py` | 108 B | Trivial | Wraps `pd.DataFrame`. |
| `src/explainability/shap_analysis.py` | 4.9 KB | Implemented, partially broken | `SHAPAnalyzer` uses `KernelExplainer` on the full ensemble; `plot_shap_summary` indexes `shap_values[1]` which is wrong for the 3-D array returned by recent SHAP versions (NB 08 works around this inline with `shap_values[:, :, 1]`). Output filename differs from the one actually used in NB 08. |
| `src/prediction/predict_url.py` | 0 B | Empty | Prediction logic lives only inline in NB 09 and `app.py`. |
| `tests/test_*.py` (4 files) | 0 B | **Empty — no tests exist** | |
| `notebooks/01–09` | — | Executed (outputs stored) | Kernel Python 3.13.9, Anaconda; absolute paths `C:\Users\Jiya\Documents\Malicious URL Detection\…`. |
| `results/**` | ~5 MB | Present | Metrics CSVs, figures, SHAP CSV, 6 example predictions. |
| `.gitignore` | 51 B | | Ignores `*.joblib`, `__pycache__/`, and (malformed line) `.ipynb_checkpoints/data/ `. The intention was presumably to ignore `data/`; the `data/` and `models/` directories are absent from the repository. |
| `requirements.txt`, `README.md`, `setup.py`, config files | — | **Absent** | No dependency specification, no documentation, no CLI. |

Dependencies inferred from imports and notebook pip output: pandas 2.3.3, numpy 2.3.5, scikit-learn 1.7.2, xgboost 3.4.1, shap 0.52.0, matplotlib, seaborn, joblib, flask.

## 2. Current architecture (as executed)

```
data/raw/raw_data.csv (253,098 rows: url,label)         [NOT IN REPO]
   └─ NB02: strip whitespace, lowercase label           → data/cleaned/cleaned_urls.csv
   └─ NB03: extract_features (28 lexical features)      → data/processed/url_features.csv
   └─ NB05: one-hot tld_type (521 values → 548 cols);
            stratified 60/20/20 split (seed 42);
            fit LR / RF / XGB pipelines (median imputer [+scaler])
   └─ NB06: VotingClassifier(soft, weights 1:2:2) over fresh LR/RF/XGB → models/*.joblib
   └─ NB07: test metrics, confusion matrices, ROC/PR figures
   └─ NB08: SHAP (KernelExplainer, 500 validation rows, 100 background rows)
   └─ NB09 / app.py: single-URL prediction, reindex to 548 training columns
```

Label encoding: `phishing = 1` (positive class), `legitimate = 0`. The dataset label is "phishing", but the app and notebooks describe outputs as "Malicious"; the two terms are used interchangeably in the project.

## 3. Features (28 defined, 548 after one-hot)

The 28 features are purely lexical (no host/WHOIS/content lookups), which is good for offline deployment. Observations from reading the code:

- `num_subdomains = max(len(host.split('.')) - 2, 0)`: counts labels, so `www.example.com` → 1 and `example.com` → 0; `example.co.uk` → 1 (wrong). Uses no public-suffix list.
- `tld_type` is the last hostname label, then one-hot encoded into 521 columns at training time; at prediction time unseen TLDs silently become all-zero rows (`reindex(fill_value=0)`). This makes the feature matrix sparse, inflates dimensionality and lets rare TLDs memorise individual sources.
- `hexadecimal_characters` counts every two-character `[0-9a-f]{2}` run anywhere in the URL, so it fires on ordinary words ("ca", "de", "fa", "ce"...). It is a noisy proxy for URL length rather than hex encoding.
- `https_usage`: scheme == https. In the dataset, 93.2% of legitimate URLs but only 50.2% of phishing URLs are https (NB04 `feature_means_by_label`). This is the single most important SHAP feature of the ensemble (mean |SHAP| 0.156, nearly twice the next feature). See Section 7.
- `brand_name_presence` and `suspicious_keywords` are substring matches (e.g. "apple" matches "pineapple", "account" matches "accountant").
- `url_shortening_service`, `suspicious_tld`: small hard-coded lists (14 and 20 entries).
- `random_looking_domain`: hand-set thresholds (length ≥ 12, ≥ 3 digits, entropy ≥ 3.5) with no justification.
- No handling of: ports, userinfo, fragments, IDN decoding (only literal `xn--`), percent-decoding before analysis, path depth, longest token, token statistics, registered-domain extraction, digit runs in hostname, or character n-grams.
- `urlsplit` on malformed input (e.g. `http://[::1`) raises `ValueError`; there is no guard, so `app.py` returns HTTP 400 with the exception text.

## 4. Models and training configuration

| Model | Config | Preprocessing |
|---|---|---|
| Logistic Regression | `max_iter=1000, class_weight='balanced', seed 42` | median imputer + StandardScaler |
| Random Forest | `n_estimators=200, class_weight='balanced', seed 42` | median imputer |
| XGBoost | `n_estimators=200, max_depth=6, lr=0.1, subsample=0.8, colsample_bytree=0.8` | median imputer |
| Weighted soft voting | LR:RF:XGB = 1:2:2 | each member's own pipeline |

- No hyperparameter search; no validation-based model selection; the validation split is used only to print metrics.
- The ensemble weights (1,2,2) are hard-coded and never justified or tuned.
- Decision threshold is the default 0.5 everywhere.
- The imputer is a no-op (no missing values exist), so it is harmless but misleading.
- The ensemble is trained in NB06 on fresh pipelines; the standalone LR/RF/XGB evaluated in NB07 were trained in NB05 with identical settings, so the comparison is fair but duplicates the work.

## 5. Stored results (origin: notebook outputs, test split of seed-42 random split)

Test set n = 50,620 (25,884 legitimate / 24,736 phishing).

| Model | Acc | Prec | Rec | F1 | FP | FN |
|---|---|---|---|---|---|---|
| Logistic Regression | 0.8864 | 0.9030 | 0.8598 | 0.8809 | 2,285 | 3,467 |
| Random Forest | 0.9679 | 0.9771 | 0.9568 | 0.9668 | 555 | 1,068 |
| XGBoost | 0.9671 | 0.9828 | 0.9492 | 0.9657 | 410 | 1,257 |
| Weighted soft voting | 0.9678 | 0.9824 | 0.9512 | 0.9665 | 422 | 1,207 |

Findings about these numbers:
- The ensemble does **not** outperform Random Forest on accuracy, recall or F1; the differences between RF, XGB and the ensemble are ≤ 0.001 in F1 and have no uncertainty estimates. The "hybrid" contribution of the original project is therefore not supported by its own results.
- ROC-AUC / PR-AUC values exist only inside the figure legends of `roc_curves.png` / `pr_curves.png`; they were never saved as data.
- All numbers come from a single random split with a single seed.

## 6. Reproducibility status

| Item | Status |
|---|---|
| Raw dataset `data/raw/raw_data.csv` | **Not in repository, not documented.** Origin, licence, collection period unknown. Needed to reproduce anything. |
| Trained models `models/*.joblib` | Not in repository (gitignored). |
| Split files `data/processed/splits/*.csv` | Not in repository, but the split is deterministic (seed 42, stratified) given the feature file. |
| Environment | No `requirements.txt`; versions only inferable from notebook pip logs. |
| Paths | Absolute Windows paths in NB outputs; notebooks use `Path.cwd().parent`, which works only when the kernel is started inside `notebooks/`. |
| Tests | None (four empty files). |
| Random seeds | `random_state=42` for split and models; `np.random.choice` in NB09 unseeded; KernelExplainer sampling unseeded. |
| Can the stored metrics be reproduced today? | **Not without the raw CSV.** With it, NB02→NB07 should reproduce them up to library-version differences (XGBoost/sklearn versions differ between the author's environment and ours). |

Conclusion: at present nothing in `results/` can be independently regenerated from the repository alone. The first blocker for Phase 1.2 is obtaining `raw_data.csv` (or an equivalent documented dataset).

## 7. Evaluation and leakage concerns

1. **Source/collection artifacts dominate the model.** From the author's own feature means by label: `https_usage` 0.93 vs 0.50; `num_subdomains` 1.20 vs 0.80 (i.e. legitimate URLs mostly carry `www.`); `excessive_hyphens` higher for legitimate; `ip_address` is exactly 0.0 for legitimate. SHAP ranks `https_usage` (0.156) and `num_subdomains` (0.091) far above all other features. These are properties of *how the two classes were collected* (e.g. a curated benign list normalised to `https://www.` vs. a phishing feed) rather than properties of maliciousness. The saved `results/url_predictions.csv` confirms the consequence: `https://google.com/` is predicted MALICIOUS with 88% confidence, `https://www.goggle.com` (a typosquat) LEGITIMATE with 82%, and `https://www.wikipedia.org` only 62% legitimate. The model has learned "no www. → phishing".
2. **Random split with URL-level deduplication only.** Many URLs share a registered domain (e.g. many `docs.google.com` phishing pages, many pages from the same university site). A random split places pages of the same site in train and test, so the test score partly measures memorisation of domains. Domain overlap was never quantified.
3. **No temporal information** exists in the dataset, so temporal generalisation cannot be assessed with it.
4. **One-hot TLD over 521 values** fitted on the full dataset before splitting (`pd.get_dummies` on `df_features` in NB05 before `create_data_splits`). This is a mild leak of the TLD vocabulary (test-only TLDs get columns); it does not leak labels, but it is not a train-only fit.
5. **Threshold and ensemble weights** were never selected on validation data; the validation split is effectively unused.
6. **Single seed, no confidence intervals, no statistical tests.**
7. **No external dataset** evaluation.

## 8. Consistency between training, prediction and app

- Feature code is consistent (root file, `src` file and NB03/NB09 inline copies are identical), but it exists in four copies, which will diverge.
- Prediction reconstructs the 548-column schema by reading `X_test.csv` at inference time (NB09) — the schema is not persisted with the model. `app.py` does not do even this: it passes a 28-column frame (with a string `tld_type` column) to a model trained on 548 numeric columns, which will raise inside the imputer. **`app.py` cannot work as committed.**
- `app.py` reads `index.html`, but the file is `idex.html`.
- The app presents "Legitimate" with a confidence percentage derived from an uncalibrated soft-vote probability; no uncertainty or limitation statement is shown.

## 9. Code quality summary

Strengths: the notebooks are clean and linear; the feature list is explicit and documented in `results/logs/feature_definitions.csv`; pipelines wrap preprocessing so no scaler leakage occurs inside a split; the ensemble is built from reusable factories.

Weaknesses (prioritised):
1. Dataset not available / undocumented (blocks everything).
2. Shortcut features (`https_usage`, `www`-driven `num_subdomains`) dominate and produce absurd predictions on well-known domains.
3. No grouped or external evaluation; no uncertainty.
4. No tests; empty modules; duplicated feature code; broken app.
5. No ROC/PR-AUC, FPR/FNR, calibration, latency, or model-size measurements saved as data.
6. No hyperparameter tuning, no validation-based threshold or weight selection.
7. No requirements/README/CLI; absolute paths.

## 10. Prioritised improvement plan

| Priority | Action | Phase |
|---|---|---|
| P0 | Obtain/document the raw dataset; otherwise adopt documented public datasets (see `research/DATASET_SOURCES.md`). | 1, 4 |
| P0 | Re-implement the pipeline as importable, tested modules with a config file, deterministic splits saved to disk, and a CLI (`scripts/`). | 5 |
| P0 | Quantify registered-domain overlap between splits; implement domain-grouped splitting with `tldextract`. | 4 |
| P0 | Reproduce the baseline (28 features, LR/RF/XGB/soft vote, seed 42 random split) with the new code and save predictions, probabilities, AUCs. | 1 |
| P1 | Artifact analysis: measure how much performance depends on `https_usage`/`www` and how the models behave on random vs grouped vs external splits; ablate artifact features. | 6 |
| P1 | Improved lexical feature set (public-suffix-aware, token statistics, encoding/IDN handling) and a char-level model; fair comparison. | 5, 6 |
| P1 | Multi-seed runs, bootstrap CIs, paired tests. | 6 |
| P2 | Calibration (reliability diagrams, ECE), threshold selection at fixed FPR on validation, latency/model size, SHAP with TreeExplainer, error analysis, controlled mutation robustness. | 6, 7 |
| P2 | Fix app: load persisted schema, present estimates with uncertainty, no "safe" claim. | 5 |
| P3 | Manuscript, README, requirements, reproducibility checks. | 8, 9 |
