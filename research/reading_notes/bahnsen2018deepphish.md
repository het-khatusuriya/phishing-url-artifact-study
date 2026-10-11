# bahnsen2018deepphish

## Citation
Alejandro Correa Bahnsen; Ivan Torroledo; Luis David Camacho; Sergio Villegas (2018). *DeepPhish: Simulating Malicious AI*. Black Hat Europe 2018 (talk, 5 Dec 2018, slides); also presented at DEF CON 26 AI Village. URL: https://i.blackhat.com/eu-18/Wed-Dec-5/eu-18-CorreaBahnsen-DeepPhish-Simulating-Malicious-AI.pdf

## Verification
- Verified on 2026-10-11. Status: **partial**. Access: **full_text** (PDF: research/papers/bahnsen2018deepphish.pdf).
- Evidence: PARTIAL: Black Hat Europe 2018 slide deck retrieved from i.blackhat.com (title/presenter confirmed on slides); conference listing on infocondb.org and press coverage in search results. The commonly cited 'APWG eCrime 2018' peer-reviewed venue could NOT be confirmed via Crossref (no 2018-2019 record titled DeepPhish) and should not be cited as such without checking IEEE Xplore. Author list beyond Correa Bahnsen taken from the widely used citation and is unverified.

## Problem
Can attackers use AI to craft URLs that evade AI-based phishing detectors?

## Method
Cluster PhishTank URLs by threat actor, train LSTM per actor on URLs that bypassed the detector, generate new URLs, measure evasion.

## Dataset(s)
PhishTank-derived; sizes on slides.

## Features
Character-level LSTM; target detector is the eCrime 2017 URL LSTM.

## Evaluation protocol
Attack 'effectiveness' = fraction of generated URLs classified benign

## Metrics reported (only numbers present in the source)
Press/DEF CON summaries report attack effectiveness rising from 0.69% to 20.9% and 4.91% to 36.28% for two actors (secondary sources; slide numbers not re-verified here).

## Main findings
Generative evasion is feasible against character-level URL detectors.

## Limitations
- Authors' stated limitations: Not peer reviewed.
- My assessment: No code/dataset release; vendor talk; numbers hard to reproduce.

## Research gap
Need reproducible, open mutation benchmarks instead of vendor demonstrations.

## Relevance to our project (score 3/5)
Historical motivation for adversarial URL robustness; cite cautiously as a talk.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
