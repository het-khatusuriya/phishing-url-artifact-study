# jalil2023highly

## Citation
Jalil, Sajjad; Usman, Muhammad; Fong, Alvis (2023). *Highly accurate phishing URL detection based on machine learning*. Journal of Ambient Intelligence and Humanized Computing, 14(7), pp. 9233-9251. DOI: 10.1007/s12652-022-04426-3 URL: https://doi.org/10.1007/s12652-022-04426-3

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1007/s12652-022-04426-3 (JAIHC 14(7), 9233-9251) and Springer article page (abstract, accuracies).

## Problem
Fast, third-party-free URL phishing detection with domain-informed feature selection and broader evaluation.

## Method
Feature set from full URL/protocol/host/path incl. entropy and brand TF-IDF; compares 8 learners across 6 datasets.

## Dataset(s)
Six datasets: two Kaggle URL datasets and four benchmark datasets (names/sizes not on abstract page)

## Features
30 lexical features incl. entropy, suspicious words, brand matching.

## Evaluation protocol
Multiple datasets; protocol not on abstract page

## Metrics reported
RF accuracy 96.25% and 94.65% (Kaggle sets); 92.2%, 91.63%, 94.80%, 96.85% (benchmark sets) (Springer abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Accuracy varies noticeably across datasets (91.6-96.9%), illustrating dataset dependence.

## Limitations
- Stated by authors: Not available.
- Our own caveats: No cross-dataset (train A / test B) protocol visible from abstract.

## Research gap
Cross-dataset transfer and calibration.

## Relevance to our project
Useful multi-dataset lexical RF reference; the spread across datasets supports our generalisation concern.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
