# chiew2019hybrid

## Citation
Chiew, Kang Leng; Tan, Choon Lin; Wong, KokSheik; Yong, Kelvin S. C.; Tiong, Wei King (2019). *A new hybrid ensemble feature selection framework for machine learning-based phishing detection system*. Information Sciences, 484, pp. 153-166. DOI: 10.1016/j.ins.2019.01.064 URL: https://doi.org/10.1016/j.ins.2019.01.064

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1016/j.ins.2019.01.064 (Inf. Sci. 484, 153-166); OpenAlex abstract.

## Problem
Select a compact, robust feature subset for ML phishing detection.

## Method
Two-phase ensemble feature selection; evaluates with RF, SVM, NB, C4.5, JRip, PART.

## Dataset(s)
Authors' dataset with 48 features (URL + HTML) and the UCI phishing-websites dataset

## Features
48 URL/HTML features reduced to 10 baseline features.

## Evaluation protocol
Not in abstract

## Metrics reported
94.6% accuracy with RF using 20.8% of features (10 of 48) (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Small feature subsets with RF outperform full feature sets with other learners.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Includes HTML features, so not URL-only; UCI dataset is pre-extracted and dated.

## Research gap
Feature-selection stability across datasets.

## Relevance to our project
Relevant to our explainability/feature-pruning story (compact feature sets, ensemble-based selection).

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
