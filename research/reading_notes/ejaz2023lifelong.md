# ejaz2023lifelong

## Citation
Asif Ejaz, Adnan Noor Mian, Sanaullah Manzoor (2023). Life-long phishing attack detection using continual learning. *Scientific Reports*, art. 11488. DOI: 10.1038/s41598-023-37552-9

- URL: https://doi.org/10.1038/s41598-023-37552-9
- Access status: full_text (research/papers/ejaz2023lifelong.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 3

## Verification
Semantic Scholar record (DOI, Sci Rep 2023, CC BY) checked 2026-10-11; PDF downloaded from nature.com.

## Problem
Static phishing classifiers trained on historical pages lose accuracy on future pages; can continual learning sustain performance over years?

## Method
Continual-learning (CL) algorithms on a vanilla neural network over FastText embeddings of HTML content, compared with static training and transfer learning

## Dataset(s)
Self-collected phishing and benign web pages for 2018, 2019, 2020, split into six temporally ordered datasets

## Features
Deep feature embedding of HTML contents

## Evaluation protocol
Train on earlier period, test on later periods; measures deterioration over time

## Metrics reported
CL keeps accuracy over time with 2.45% deterioration, versus 20.65% (static VNN) and 8% (transfer learning) (abstract).

## Main findings
A static phishing classifier loses over 20 percentage points across three years; incremental adaptation reduces but does not eliminate the loss.

## Limitations
**Authors' stated:** HTML-based, relatively small yearly samples; CL hyper-parameters.

**Our caveats:** Content-based, not URL-based; still one of the few phishing papers with a genuine temporal split.

## Research gap
Equivalent temporal study for lexical URL models.

## Relevance to our project
Evidence that a temporally held-out test set reveals decay hidden by random splits; supports our recommendation to report time-aware results where timestamps exist.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
