# kintis2017combosquatting

## Citation
Panagiotis Kintis; Najmeh Miramirkhani; Charles Lever; Yizheng Chen; Rosa Romero-Gomez; Nikolaos Pitropakis; Nick Nikiforakis; Manos Antonakakis (2017). *Hiding in Plain Sight: A Longitudinal Study of Combosquatting Abuse*. Proceedings of the 2017 ACM SIGSAC Conference on Computer and Communications Security (CCS '17), pp. 569-586. DOI: 10.1145/3133956.3134002 URL: https://doi.org/10.1145/3133956.3134002

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/kintis2017combosquatting.pdf).
- Evidence: Crossref record for DOI 10.1145/3133956.3134002 (title, 8 authors, CCS 2017, pp. 569-586); PDF from arXiv 1708.08519.

## Problem
Characterise combosquatting, a squatting form not captured by typo-distance.

## Method
Identify combosquatting domains for popular trademarks in large DNS datasets; study registration, longevity, abuse.

## Dataset(s)
Passive DNS + active DNS over ~6 years (paper Sec. 3); not released.

## Features
n/a

## Evaluation protocol
Prevalence, lifetime, abuse categories

## Metrics reported (only numbers present in the source)
~468B DNS records analysed; ~60% of abusive combosquatting domains active for >1,000 days (per abstract/summary).

## Main findings
Combosquatting is more prevalent than typosquatting and long-lived.

## Limitations
- Authors' stated limitations: Trademark list limited; attribution of abuse is heuristic.
- My assessment: No ML detection; lexical cues (brand token + hyphen/keyword) are what our model should capture.

## Research gap
Combosquatting-specific lexical features in URL classifiers are rarely isolated or explained.

## Relevance to our project (score 3/5)
Motivates brand-keyword features and the 'brand + keyword' mutation operator; SHAP can show whether our model uses them.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
