# lee2020robustphishing

## Citation
Jehyun Lee; Pingxiao Ye; Ruofan Liu; Dinil Mon Divakaran; Mun Choon Chan (2020). *Building Robust Phishing Detection System: an Empirical Analysis*. NDSS Workshop on Measurements, Attacks, and Defenses for the Web (MADWeb 2020). URL: https://www.ndss-symposium.org/wp-content/uploads/2020/02/23007-paper.pdf

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **full_text** (PDF: research/papers/lee2020robustphishing.pdf).
- Evidence: NDSS symposium paper page (title, author initials, PDF path 2020/02); author full names from the PDF header. Workshop DOI not verified -> blank. PDF from ndss-symposium.org.

## Problem
Phishing classifiers can be evaded by mimicking benign feature values.

## Method
Train multiple models, each on a random feature subset with injected noise; majority vote; evaluate against evasion strategies that alter feature values.

## Dataset(s)
Benign: Alexa top 300k domains ranked Feb 2019, 110,090 pages crawled May-Aug 2019; phishing: PhishTank daily feed (paper Sec. IV). No license stated.

## Features
URL and HTML content features (see paper Table I).

## Evaluation protocol
Native model vs. proposed ensemble under several evasion strategies (feature mimicry)

## Metrics reported (only numbers present in the source)
Ensemble 'performs close to native model' without attack and is 'more robust against evasion attacks' (abstract); numeric tables in Sec. V.

## Main findings
Feature-subset noisy ensembles raise evasion cost at small clean-accuracy cost.

## Limitations
- Authors' stated limitations: Evasion strategies are simulated by feature manipulation.
- My assessment: Not URL-only; small-scale; no calibration or latency reporting.

## Research gap
Robust ensembles for lexical-only URL models with explicit mutation operators.

## Relevance to our project (score 4/5)
Directly supports our ensemble design as a robustness device and gives a template for 'native vs ensemble under attack' tables.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
