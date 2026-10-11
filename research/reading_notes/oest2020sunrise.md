# oest2020sunrise

## Citation
Adam Oest, Penghui Zhang, Brad Wardman, Eric Nunes, Jakub Burgis, Ali Zand, Kurt Thomas, Adam Doupé, Gail-Joon Ahn (2020). Sunrise to Sunset: Analyzing the End-to-end Life Cycle and Effectiveness of Phishing Attacks at Scale. *29th USENIX Security Symposium (USENIX Security 20)*. 

- URL: https://www.usenix.org/conference/usenixsecurity20/presentation/oest-sunrise
- Access status: full_text (research/papers/oest2020sunrise.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 4

## Verification
USENIX presentation page (title, authors, Distinguished Paper Award, PDF) checked 2026-10-11; page range not listed on the page, so omitted.

## Problem
The end-to-end timeline of real phishing campaigns, and how much harm occurs before defences react, was unknown.

## Method
Large-scale measurement of the phishing life cycle: deployment, email lure, victim visits, detection by the ecosystem, account compromise

## Dataset(s)
One year of victim traffic to phishing pages impersonating a major financial brand (PayPal), via the 'Golden Hour' passive monitoring framework; 4.8M victim visits

## Features
Not an ML detector paper

## Evaluation protocol
Longitudinal measurement; timing analysis of campaign phases relative to blacklist detection

## Metrics reported
4.8 million victims recorded in one year; average campaign lasts 21 hours from start to last victim; at least 7.42% of visitors submit credentials; a small set of campaigns causes 89.13% of victims (abstract, Sec. 1).

## Main findings
Phishing sites are extremely short-lived and most harm happens before blacklists react ('golden hour'); detection must be fast and must work on never-before-seen URLs/domains.

## Limitations
**Authors' stated:** Single brand/ecosystem vantage point; cloaking limits visibility.

**Our caveats:** Not about ML evaluation per se, but its timing data undermines any evaluation that lets near-duplicate URLs of the same campaign sit in both train and test.

## Research gap
Evaluation protocols rarely simulate the 'first hours' regime where the model is the only defence.

## Relevance to our project
Justifies zero-day / unseen-domain evaluation: because campaigns live ~21 h, the deployed model will mostly see domains absent from training; random splits with shared domains overstate real protection.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
