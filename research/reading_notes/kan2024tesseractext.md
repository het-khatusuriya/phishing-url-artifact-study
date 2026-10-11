# kan2024tesseractext

## Citation
Zeliang Kan, Shae McFadden, Daniel Arp, Feargus Pendlebury, Roberto Jordaney, Johannes Kinder, Fabio Pierazzi, Lorenzo Cavallaro (2024). TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time (Extended Version). *arXiv preprint*. DOI: 10.48550/arXiv.2402.01359; arXiv: 2402.01359

- URL: https://arxiv.org/abs/2402.01359
- Access status: full_text (research/papers/kan2024tesseractext.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 3

## Verification
Semantic Scholar record for arXiv:2402.01359 (title, 8 authors, 2024) and PDF front matter (v2, 9 Apr 2025), checked 2026-10-11.

## Problem
Same as TESSERACT, extended to Windows PE and PDF domains and to drift-mitigation strategies.

## Method
Extended TESSERACT: constraints, AUT metric, training-data tuning, plus delay-decay mitigation strategies (active learning, rejection, incremental retraining) compared across domains

## Dataset(s)
Android: 259,230 samples over five years (abstract); additional case studies on Windows PE and PDF malware

## Features
Reuses published feature sets from the re-evaluated detectors

## Evaluation protocol
Time-aware evaluation with AUT over multi-year windows; cross-domain (Android, PE, PDF)

## Metrics reported
Abstract states reported F1 'upwards of 0.99' in prior work are inflated under realistic settings; per-domain AUT curves in Sec. 6-7 (full text available).

## Main findings
Spatial and temporal bias generalise beyond Android; periodic tuning and drift-mitigation strategies delay but do not remove decay.

## Limitations
**Authors' stated:** Preprint, not yet peer-reviewed in this extended form; malware-focused.

**Our caveats:** Still no URL/phishing case study; the mitigation comparison assumes labelled fresh data is affordable.

## Research gap
Extending the PE/PDF case-study methodology to phishing URL feeds is open.

## Relevance to our project
Useful as the up-to-date reference for AUT and for the catalogue of drift-mitigation strategies we may discuss in future work.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
