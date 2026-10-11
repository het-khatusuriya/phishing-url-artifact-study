# nowroozi2022advurl

## Citation
Ehsan Nowroozi; Abhishek; Mohammadreza Mohammadi; Mauro Conti (2022). *An Adversarial Attack Analysis on Malicious Advertisement URL Detection Framework*. arXiv:2204.13172 (preprint). URL: https://arxiv.org/abs/2204.13172

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/nowroozi2022advurl.pdf).
- Evidence: arXiv abs page 2204.13172 (title, authors, 27 Apr 2022). A later journal version (IEEE TNSM) is sometimes cited but was not verified here -> DOI blank.

## Problem
Detect fraudulent advertisement URLs and assess vulnerability of tree ensembles to adversarial attacks.

## Method
Six feature groups (lexical + scraped), four boosting/bagging models, K-Means visual analysis, Zeroth-Order-Optimization attack.

## Dataset(s)
Twelve dataset variants built by the authors (paper Sec. IV); no license statement seen.

## Features
Lexical (length, tokens, entropy-type) plus web-scraped features.

## Evaluation protocol
Accuracy, FNR; mismatched and unlabelled datasets; limited-knowledge exploratory attack

## Metrics reported (only numbers present in the source)
Best FNR 0.0037 and accuracy 99.63% (abstract).

## Main findings
Tree ensembles are accurate but can be attacked in a black-box setting.

## Limitations
- Authors' stated limitations: Preprint; ZOO attack operates on feature vectors.
- My assessment: Feature-space attack realism unclear (cf. SpacePhish).

## Research gap
Problem-space URL attacks on gradient-boosted lexical models.

## Relevance to our project (score 3/5)
Shows that boosting ensembles like ours are attackable in feature space; our mutations should be problem-space.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
