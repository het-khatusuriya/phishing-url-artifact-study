> **Duplicate record.** Same paper as `bahnsen2017rnnurl` (identical DOI); cite `bahnsen2017rnnurl`. Kept for traceability of the bahnsen2017classifying search path.

# bahnsen2017classifying

## Citation
Correa Bahnsen, Alejandro; Contreras Bohorquez, Eduardo; Villegas, Sergio; Vargas, Javier; Gonzalez, Fabio A. (2017). *Classifying phishing URLs using recurrent neural networks*. 2017 APWG Symposium on Electronic Crime Research (eCrime), pp. 1-8. DOI: 10.1109/ECRIME.2017.7945048 URL: https://doi.org/10.1109/ECRIME.2017.7945048

- Type: conference | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/bahnsen2017classifying.pdf

## Verification
Checked 2026-10-11: Author-hosted camera-ready PDF (albahnsen.github.io) read; Crossref record for DOI 10.1109/ECRIME.2017.7945048 (eCrime 2017, pp. 1-8).

## Problem
Compare feature-engineering + RF against an end-to-end LSTM on URLs.

## Method
RF on lexical/statistical features (incl. KS/KL statistics, Alexa rank flag); LSTM over character sequences with sigmoid output.

## Dataset(s)
2,000,000 URLs: 1M phishing from PhishTank + 1M benign from Common Crawl (Sec. IV)

## Features
RF: lexical/statistical features (Sec. III-A); LSTM: raw characters.

## Evaluation protocol
3-fold cross-validation; learning-curve experiment on 200k held-out URLs (Sec. V)

## Metrics reported
RF accuracy 93.47% (recall 93.28%, precision 93.63%, AUC 98.44%); LSTM accuracy 98.76% (std 0.03%), F1 0.98 vs 0.93 (Sec. V, Tables II-III, Fig. 8); throughput 942 URLs/s (RF) vs 281 (LSTM).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Char-LSTM beats RF by about 5 points without feature engineering, at a throughput cost.

## Limitations
- Stated by authors: LSTM slower to train/evaluate.
- Our own caveats: Benign = Common Crawl pages vs PhishTank; random CV means same campaigns/domains appear in train and test (likely inflated).

## Research gap
Domain-grouped evaluation.

## Relevance to our project
Standard char-RNN baseline; its RF-vs-LSTM comparison is the kind we replicate under stricter splits.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
