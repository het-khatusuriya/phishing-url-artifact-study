# [Working title — to be finalised after results] Collection Artifacts and Domain Memorisation in Lexical Phishing-URL Detection: An Artifact-Aware Evaluation and Training Protocol

> **Status legend used throughout this draft:** `[PLANNED]` = not yet executed; `[PRELIM]` = intermediate result, may change; `[VERIFIED]` = traced to a result file under `results/runs/`. All quantitative claims remain provisional until marked `[VERIFIED]`.

## Abstract

`[PLANNED]` To be written after results are verified. Will state: problem, motivation (artifact-driven shortcuts in URL benchmarks), method (artifact-aware feature design, registered-domain-grouped evaluation, validation-based operating thresholds, calibration), datasets, key quantitative results, contribution, conclusion.

## Keywords

malicious URL detection; phishing; lexical features; ensemble learning; character-level CNN; dataset bias; shortcut learning; domain-grouped evaluation; calibration; explainability

## 1. Introduction

`[PLANNED]` Problem and importance; limitations of current solutions (benchmark optimism, artifact reliance); motivation from the audited baseline (Section 3 of `research/REPOSITORY_AUDIT.md`); research questions RQ1–RQ3 (see `research/RESEARCH_PLAN.md`); contributions (to be stated only as demonstrated).

## 2. Related Work

`[PLANNED]` Organised by theme (from `research/LITERATURE_REVIEW.md`): 2.1 lexical/handcrafted features and classical ML; 2.2 ensembles and hybrids; 2.3 character-level and transformer models; 2.4 evaluation realism — temporal drift, dataset bias, shortcut learning, cross-dataset generalisation; 2.5 explainability and robustness; 2.6 datasets. Closing paragraph: how this work differs.

## 3. Research Problem and Contributions

`[PLANNED]` RQs, hypotheses (H1–H3), contributions implemented vs explored.

## 4. Methodology

4.1 System overview (figure: pipeline). 4.2 Data and labels. 4.3 URL parsing and normalisation (safe parser; public-suffix extraction). 4.4 Feature sets: `baseline28` (original), `lexical_v2`, artifact-neutral variants. 4.5 Models: LR, RF, XGBoost, LightGBM, weighted soft vote (1:2:2, original), stacking, char-CNN, hybrid char+lexical. 4.6 Training, model selection, thresholds (validation-only; FPR-constrained). 4.7 Calibration. 4.8 Explainability (TreeExplainer SHAP on tree models). 4.9 Complexity and implementation.

`[PLANNED]` Every description must match `src/urlresearch/`.

## 5. Experimental Setup

Dataset provenance, sizes, class balance, dedup, grouping statistics, split protocols (random / grouped / temporal / external), hardware (12-core CPU, no GPU), software versions (`requirements.txt`), seeds, hyper-parameters, baselines, metrics, statistical procedures (paired bootstrap, McNemar, bootstrap CIs).

## 6. Results

6.1 Baseline reproduction `[PLANNED]`. 6.2 Random vs grouped evaluation `[PLANNED]`. 6.3 Artifact ablations `[PLANNED]`. 6.4 Model family comparison `[PLANNED]`. 6.5 External-dataset generalisation `[PLANNED]`. 6.6 Calibration and operating thresholds `[PLANNED]`. 6.7 Robustness to controlled mutations `[PLANNED]`. 6.8 Explainability and error analysis `[PLANNED]`. 6.9 Efficiency `[PLANNED]`.

## 7. Discussion

`[PLANNED]`

## 8. Threats to Validity and Limitations

`[PLANNED]` Dataset bias; label noise; unknown provenance of the original dataset; no temporal labels in main data; CPU-only (no transformer baseline); adversarial adaptation not covered beyond tested mutations; external datasets have their own collection artifacts.

## 9. Conclusion and Future Work

`[PLANNED]`

## References

Generated from `research/references.bib`; every in-text key must exist there.
