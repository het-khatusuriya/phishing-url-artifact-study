# tajaddodianfar2020texception

## Citation
Tajaddodianfar, Farid; Stokes, Jack W.; Gururajan, Arun (2020). *Texception: A Character/Word-Level Deep Learning Model for Phishing URL Detection*. ICASSP 2020 - IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 2857-2861. DOI: 10.1109/ICASSP40776.2020.9053670 URL: https://doi.org/10.1109/ICASSP40776.2020.9053670

- Type: conference | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/tajaddodianfar2020texception.pdf

## Verification
Checked 2026-10-11: Microsoft Research-hosted PDF (microsoft.com/en-us/research/wp-content/uploads/2020/07/Texception_Icassp20.pdf) read; Crossref record for DOI 10.1109/ICASSP40776.2020.9053670 (ICASSP 2020, pp. 2857-2861).

## Problem
Internet-scale phishing URL detection operating at extremely low FPR.

## Method
Character path and word path with parallel convolution blocks (Inception-like), concatenated, dense output; compared with a traditional text classifier and a URLNet baseline.

## Dataset(s)
Microsoft production telemetry: six weeks of data; first two weeks -> 1.7M training samples (benign down-sampled to 5% positives); test set 20M instances sampled from production (Sec. 2)

## Features
Learned char embeddings + pre-trained word embeddings (Table 1 parameters).

## Evaluation protocol
Temporal: train on first 2 weeks, test on later production data; TPR at fixed 0.01% FPR (Table 2)

## Metrics reported
TPR increased by 126.7% relative to a traditional text classifier at 0.01% FPR (abstract; Table 2 lists TP and error rates at fixed 0.01% FPR, e.g. Baseline_URLNet 12.3% TP).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Char/word parallel-CNN generalises better to new URLs than classical text classification at production FPRs.

## Limitations
- Stated by authors: Proprietary data; production labels.
- Our own caveats: Not reproducible; absolute TPRs are low at 0.01% FPR, showing how hard low-FPR operation is.

## Research gap
Public low-FPR benchmarks.

## Relevance to our project
Model design precedent and strong argument for reporting TPR at low FPR (relevant to calibration/threshold choice).

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
