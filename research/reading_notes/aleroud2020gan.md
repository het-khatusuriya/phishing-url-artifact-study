# aleroud2020gan

## Citation
Ahmed AlEroud; George Karabatis (2020). *Bypassing Detection of URL-based Phishing Attacks Using Generative Adversarial Deep Neural Networks*. Proceedings of the Sixth International Workshop on Security and Privacy Analytics (IWSPA '20), pp. 53-60. DOI: 10.1145/3375708.3380315 URL: https://doi.org/10.1145/3375708.3380315

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Crossref record for DOI 10.1145/3375708.3380315 (title, authors, proceedings, pages 53-60, 2020); Semantic Scholar abstract.

## Problem
Can generative models create phishing URLs that bypass URL classifiers?

## Method
Train a GAN on phishing URLs; feed generated URLs to ML detectors (including PhishStorm-style intra-URL similarity features).

## Dataset(s)
Not detailed in abstract.

## Features
Target detectors use lexical and intra-URL-similarity features.

## Evaluation protocol
Evasion rate against simple and advanced detectors

## Metrics reported (only numbers present in the source)
Abstract: the approach 'fooled both simple and advanced detection models' (no numbers in abstract).

## Main findings
GAN-generated URLs evade detectors.

## Limitations
- Authors' stated limitations: n/a (abstract only).
- My assessment: Generated URLs may be unregistrable/unrealistic; unclear labels.

## Research gap
Realism constraints on generated adversarial URLs.

## Relevance to our project (score 3/5)
Cited as the generative-evasion counterpart to our rule-based, label-preserving mutations.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
