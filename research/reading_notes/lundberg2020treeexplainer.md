# lundberg2020treeexplainer

## Citation
Scott M. Lundberg; Gabriel Erion; Hugh Chen; Alex DeGrave; Jordan M. Prutkin; Bala Nair; Ronit Katz; Jonathan Himmelfarb; Nisha Bansal; Su-In Lee (2020). *From local explanations to global understanding with explainable AI for trees*. Nature Machine Intelligence 2(1):56-67. DOI: 10.1038/s42256-019-0138-9 URL: https://doi.org/10.1038/s42256-019-0138-9

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/lundberg2020treeexplainer.pdf).
- Evidence: Semantic Scholar API record for DOI 10.1038/s42256-019-0138-9 (title, 10 authors, venue, year); PDF saved is the arXiv preprint 1905.04610 'Explainable AI for Trees: From Local Explanations to Global Understanding' (arXiv abs page checked).

## Problem
Tree ensembles (RF, GBDT) are accurate but opaque; heuristic feature importances are inconsistent.

## Method
Exact SHAP computation for trees (TreeExplainer), SHAP interaction values, and aggregation of local explanations into global importance, dependence and clustering plots.

## Dataset(s)
Three medical datasets (NHANES mortality, chronic kidney disease, hospital procedure duration); not security data.

## Features
n/a

## Evaluation protocol
Benchmarks of 13 explanation methods on consistency/accuracy metrics; medical mortality/kidney/hospital datasets

## Metrics reported (only numbers present in the source)
Method-comparison benchmark scores reported in the paper's Fig. 2/3; no classification accuracy relevant to us.

## Main findings
TreeExplainer is exact and fast; gain/split-count importances can be inconsistent; local explanations reveal interaction effects and dataset shift.

## Limitations
- Authors' stated limitations: Interventional vs. observational conditional expectation choice affects attributions; limited to tree models.
- My assessment: Our ensemble (if it mixes non-tree models) needs KernelSHAP or per-model explanation; per-sample cost rises with ensemble size.

## Research gap
No study of explanation drift between training and external datasets for security tasks.

## Relevance to our project (score 5/5)
Direct justification for using TreeExplainer on RF/XGBoost/LightGBM members of our ensemble and for global beeswarm/dependence plots.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
