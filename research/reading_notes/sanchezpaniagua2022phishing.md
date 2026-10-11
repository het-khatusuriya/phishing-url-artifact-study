# sanchezpaniagua2022phishing

## Citation
Sanchez-Paniagua, Manuel; Fidalgo Fernandez, Eduardo; Alegre, Enrique; Al-Nabki, Wesam; Gonzalez-Castro, Victor (2022). *Phishing URL Detection: A Real-Case Scenario Through Login URLs*. IEEE Access, 10, pp. 42949-42960. DOI: 10.1109/ACCESS.2022.3168681 URL: https://doi.org/10.1109/ACCESS.2022.3168681

- Type: journal | Theme (L1): b-ensemble-hybrid | Access: full_text | Verified: full
- Local PDF: research/papers/sanchezpaniagua2022phishing.pdf

## Verification
Checked 2026-10-11: IEEE Access CC BY PDF (ielx7/.../09759382.pdf) read in full; Crossref record for DOI 10.1109/ACCESS.2022.3168681 (vol 10, 42949-42960).

## Problem
Show that standard datasets (legitimate = homepages) overstate performance; legitimate login pages look like phishing URLs.

## Method
Builds PILU-90K; compares 8 classical learners on handcrafted features, TF-IDF+LR, and two char-CNNs; measures accuracy decay over time and clusters phishing domains.

## Dataset(s)
PILU-90K (public): 30K legitimate homepage URLs (Quantcast top sites), 30K legitimate login URLs, 30K phishing URLs (PhishTank); plus older sets (Ebbu2017, PWD2016, 2009-2017 data) for temporal tests (Sec. III, Tables 1,3,4)

## Features
Handcrafted lexical (lengths, counts, tokens, TLD cues) and char n-gram TF-IDF.

## Evaluation protocol
Train on homepage-vs-phishing then test on legitimate login URLs (FPR stress test); temporal: train on 2016 data, test on 2020 data (Table 7); random splits within PILU

## Metrics reported
Models trained on PIU-60K (homepages) lose 27-39% accuracy on legitimate login URLs (best 69.50%, SVM 54.46%) (Sec. V-A, Fig. 4); TF-IDF + LR reaches 96.50% in the login scenario (abstract, Table 6); accuracy of 2016-trained models decreases on 2020 URLs (Table 7).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Benign-class composition is a major shortcut; URL length separability largely disappears when login URLs are used (Fig. 3); models age quickly.

## Limitations
- Stated by authors: Dataset limited to top-site login pages; deep models not exhaustively tuned.
- Our own caveats: Still a random split within year; no domain-grouped split.

## Research gap
Domain-grouped and calibrated evaluation; artifact quantification (https/www).

## Relevance to our project
Most important methodological precedent for our shortcut-artifact and cross-time analysis; PILU-90K is an ideal external test set.

Relevance score: 5/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
