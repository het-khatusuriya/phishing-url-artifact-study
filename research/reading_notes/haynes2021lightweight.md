# haynes2021lightweight

## Citation
Katherine Haynes; Hossein Shirazi; Indrakshi Ray (2021). *Lightweight URL-based phishing detection using natural language processing transformers for mobile devices*. Procedia Computer Science 191:127-134 (MobiSPC/FNC 2021). DOI: 10.1016/j.procs.2021.07.040 URL: https://doi.org/10.1016/j.procs.2021.07.040

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Crossref record for DOI 10.1016/j.procs.2021.07.040 (title, authors, journal, volume 191, pages 127-134, 2021). Elsevier page blocked (403); abstract details from the Crossref record of the 2022 extended version (10.5383/juspn.17.01.005).

## Problem
Phishing detection on mobile devices needs URL-only, lightweight models.

## Method
Compare pre-trained transformers fine-tuned on URL text with custom-vocabulary models.

## Dataset(s)
Not verified (abstract only).

## Features
URL text tokens.

## Evaluation protocol
Accuracy; prediction speed

## Metrics reported (only numbers present in the source)
Per the extended-version abstract: URL-only standard NNs best accuracy 86.2%; MobileBERT competitive and ~3x faster than other transformers (numbers for the 2021 paper itself not verified).

## Main findings
MobileBERT is the practical trade-off for mobile URL detection.

## Limitations
- Authors' stated limitations: n/a (abstract).
- My assessment: No classical baseline in abstract.

## Research gap
Lexical GBDT vs. MobileBERT efficiency comparison.

## Relevance to our project (score 3/5)
Supports the efficiency axis of our comparison.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
