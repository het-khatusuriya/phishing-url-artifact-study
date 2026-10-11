# apruzzese2023realattackers

## Citation
Giovanni Apruzzese, Hyrum S. Anderson, Savino Dambra, David Freeman, Fabio Pierazzi, Kevin A. Roundy (2023). "Real Attackers Don't Compute Gradients": Bridging the Gap Between Adversarial ML Research and Practice. *2023 IEEE Conference on Secure and Trustworthy Machine Learning (SaTML)*. DOI: 10.1109/SaTML54575.2023.00031; arXiv: 2212.14315

- URL: https://doi.org/10.1109/SaTML54575.2023.00031
- Access status: full_text (research/papers/apruzzese2023realattackers.pdf)
- Verified: yes
- Theme (L2): b - dataset bias, leakage, shortcut learning
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI 10.1109/SaTML54575.2023.00031, SaTML 2023) checked 2026-10-11; arXiv PDF 2212.14315.

## Problem
Adversarial-ML research threat models (gradient attacks) diverge from what operational ML security systems actually face.

## Method
Position paper contrasting research threat models with operational reality; case study (b) reports lack of evidence of gradient-based adversarial examples against a commercial phishing detector

## Dataset(s)
Three industrial case studies (an online social network ML system; a commercial ML phishing-webpage detector; an ML evasion competition) plus analysis of recent adversarial-ML papers

## Features
N/A

## Evaluation protocol
Qualitative; literature analysis

## Metrics reported
No benchmark numbers; the phishing case study is qualitative (Sec. III).

## Main findings
Operational ML security problems are dominated by data drift, cheap problem-space manipulations and pipeline effects rather than gradient attacks; evaluation should reflect realistic attacker economics.

## Limitations
**Authors' stated:** Case studies are anecdotal by design.

**Our caveats:** Useful for scoping our robustness analysis toward cheap URL manipulations (scheme/www changes, path padding) rather than gradient attacks.

## Research gap
Realistic, cheap perturbation benchmarks for URL detectors.

## Relevance to our project
Justifies testing our model against trivial URL rewrites (http vs https, with/without www) as a 'realistic attacker' robustness check, which also doubles as an artefact-sensitivity test.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
