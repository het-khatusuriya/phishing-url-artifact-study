# verma2015character

## Citation
Verma, Rakesh; Dyer, Keith (2015). *On the Character of Phishing URLs: Accurate and Robust Statistical Learning Classifiers*. Proceedings of the 5th ACM Conference on Data and Application Security and Privacy (CODASPY '15), pp. 111-122. DOI: 10.1145/2699026.2699115 URL: https://doi.org/10.1145/2699026.2699115

- Type: conference | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1145/2699026.2699115 (CODASPY '15, pp. 111-122); OpenAlex abstract; author's publication page confirms citation. Full text not open.

## Problem
Improve accuracy/robustness of phishing URL classification with character-level statistical features.

## Method
Adds distributional features: KS statistic between URL character distribution and reference distributions, plus classic lexical features; evaluates several learners.

## Dataset(s)
Phishing (PhishTank) and legitimate URLs; sizes not in abstract

## Features
Character-distribution statistics (KS and related), character-class counts, lengths, dots, hyphens, suspicious tokens.

## Evaluation protocol
Not in abstract

## Metrics reported
99.3% accuracy with FPR < 0.4% (abstract).
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Character-level statistics boost accuracy over token-only lexical features.

## Limitations
- Stated by authors: Not available.
- Our own caveats: Very high accuracy likely dataset-dependent; no cross-dataset evidence.

## Research gap
Robustness claims untested over time.

## Relevance to our project
Direct precedent for our character-distribution/entropy features; cite when motivating char-level statistics inside a lexical ensemble.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
