# marchal2018designing

## Citation
Samuel Marchal, N. Asokan (2018). On Designing and Evaluating Phishing Webpage Detection Techniques for the Real World. *11th USENIX Workshop on Cyber Security Experimentation and Test (CSET 18)*. 

- URL: https://www.usenix.org/conference/cset18/presentation/marchal
- Access status: full_text (research/papers/marchal2018designing.pdf)
- Verified: yes
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 5

## Verification
USENIX CSET'18 presentation page (title, authors, PDF) checked 2026-10-11.

## Problem
Phishing detectors that score highly in papers rarely work in deployment; dataset composition and evaluation choices are the cause.

## Method
Guidelines for ground-truth composition, evaluation metrics and temporal-resilience testing of phishing webpage detectors

## Dataset(s)
Position/guidelines paper; no new dataset

## Features
Discusses popularity-based features (Alexa rank, DNS) as sources of dataset bias

## Evaluation protocol
Recommends: legitimate set must include unpopular/long-tail sites, URLs with paths (not just FQDNs from Alexa/DMOZ), real-world class distribution (about 1 phish per 100 benign) to avoid base-rate fallacy, test set larger than training set, and temporal-resilience tests (train at time t, test on later pages)

## Metrics reported
No experiments; prescriptive. States that balanced (1/1) datasets 'suffer from base rate fallacy' and that a 1:100 distribution is needed for a meaningful precision (Sec. 3-4).

## Main findings
Academic detectors look excellent on non-representative data; representativity of the legitimate class (popularity, URL structure) and temporal evaluation are the main missing pieces.

## Limitations
**Authors' stated:** Guidelines not empirically validated in the paper.

**Our caveats:** Written for webpage (content) detectors, but every data-composition guideline applies verbatim to URL-only detectors.

## Research gap
Few later URL papers follow these guidelines; our paper can operationalise them.

## Relevance to our project
Directly names the mechanism behind our https://google.com/ false positive: a legitimate set drawn from popular 'www.' index pages makes the model learn popularity/format artefacts. Cite for base-rate and legitimate-sampling recommendations.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
