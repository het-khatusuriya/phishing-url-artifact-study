# bozkir2023grambeddings

## Citation
Ahmet Selman Bozkir; Firat Coskun Dalgic; Murat Aydos (2023). *GramBeddings: A New Neural Network for URL Based Identification of Phishing Web Pages Through N-gram Embeddings*. Computers & Security 124:102964. DOI: 10.1016/j.cose.2022.102964 URL: https://doi.org/10.1016/j.cose.2022.102964

## Verification
- Verified on 2026-10-11. Status: **yes**. Access: **abstract_only**.
- Evidence: Crossref record for DOI 10.1016/j.cose.2022.102964 (title, authors, C&S vol. 124, art. 102964, 2023); dataset page web.cs.hacettepe.edu.tr/~selman/grambeddings-dataset/ (counts, period, access form).

## Problem
Pre-trained embeddings are unavailable for URLs; need URL-native representation.

## Method
Learn n-gram embeddings during training; cascade CNN, LSTM and attention.

## Dataset(s)
Download: request via Google Form linked on dataset page (no direct URL). License: not stated. Timestamps: not stated (collection window May 2019-Jun 2021 only). Labels: phishing/legitimate. Known problems: access gated; sources of legitimate URLs described only as 'custom crawler'.

## Features
Character n-grams (raw URL).

## Evaluation protocol
Hold-out on 800k set; comparison with prior URL models

## Metrics reported (only numbers present in the source)
Not verified (paywalled).

## Main findings
Large recent balanced URL corpus; deep model competitive.

## Limitations
- Authors' stated limitations: n/a
- My assessment: Gated access hampers reproducibility; no metadata.

## Research gap
n/a

## Relevance to our project (score 4/5)
Candidate large external set if access is granted; otherwise cite as comparison corpus.

Our project: lexical-feature + ensemble phishing URL detector with SHAP explanations on a ~250k binary URL dataset; planned work: probability calibration, controlled label-preserving URL-mutation robustness tests, latency/model-size comparison, and external-dataset evaluation.
