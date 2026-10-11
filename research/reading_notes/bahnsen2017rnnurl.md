# bahnsen2017rnnurl

## Citation
Alejandro Correa Bahnsen; Eduardo Contreras Bohorquez; Sergio Villegas; Javier Vargas; Fabio A. Gonzalez (2017). *Classifying phishing URLs using recurrent neural networks*. 2017 APWG Symposium on Electronic Crime Research (eCrime). DOI: 10.1109/ecrime.2017.7945048 URL: https://doi.org/10.1109/ecrime.2017.7945048

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/bahnsen2017rnnurl.pdf).
- Evidence: Crossref record for DOI 10.1109/ecrime.2017.7945048 (title, authors, event, 2017); author camera-ready PDF from albahnsen.github.io.

## Problem
Detect phishing from URL alone without content download.

## Method
Compare engineered lexical features + RF against character LSTM reading the URL string.

## Dataset(s)
2,000,000 URLs: 1M PhishTank phishing, 1M Common Crawl benign (paper Sec. IV); collection period not stated; no license.

## Features
Lexical: length, digit/char counts, Alexa top-1M membership, keyword presence, etc.; LSTM uses raw characters.

## Evaluation protocol
3-fold cross-validation; accuracy; learning curves with 200k test URLs

## Metrics reported (only numbers present in the source)
LSTM accuracy 98.7%, 'beating by 5%' the RF (abstract; Table II in paper).

## Main findings
Character RNN outperforms hand-crafted features at scale.

## Limitations
- Authors' stated limitations: No evaluation on temporal splits.
- My assessment: Alexa membership feature leaks list-based priors; PhishTank/Common Crawl distribution gap makes task easy.

## Research gap
Robustness and interpretability of the RNN not studied (motivating DeepPhish follow-up).

## Relevance to our project (score 4/5)
Classic PhishTank+Common Crawl construction used by many later datasets; baseline numbers and a cautionary example of source-based shortcut learning.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
