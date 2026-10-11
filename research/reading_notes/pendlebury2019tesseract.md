# pendlebury2019tesseract

## Citation
Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, Lorenzo Cavallaro (2019). TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time. *28th USENIX Security Symposium (USENIX Security 19)*, pp. 729-746. arXiv: 1807.07838

- URL: https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury
- Access status: full_text (research/papers/pendlebury2019tesseract.pdf)
- Verified: yes
- Theme (L2): a - concept drift / temporal evaluation
- Relevance score (1-5): 5

## Verification
USENIX presentation page (title, authors, pages 729-746, PDF) and arXiv API record 1807.07838v4, both checked 2026-10-11. No DOI issued by USENIX.

## Problem
Reported malware-classifier accuracy is inflated by unrealistic class ratios (spatial bias) and by train/test splits that leak future knowledge (temporal bias).

## Method
Evaluation framework; constraints C1 (temporal training consistency), C2 (temporal goodware/malware window consistency), C3 (realistic malware-to-goodware ratio in testing); new metric AUT (area under time); tuning algorithm for training class ratio; re-evaluation of three published classifiers (linear SVM on Drebin features, Random Forest on MaMaDroid Markov features, a deep net)

## Dataset(s)
Android apps: ~129k samples (AndroZoo) spanning 2014-2016, labelled via VirusTotal (details Sec. 2.2); ~10% malware in realistic setting

## Features
Not a feature paper; reuses Drebin binary features, MaMaDroid API-call Markov chains, and a DL baseline

## Evaluation protocol
Time-aware splits with monthly test periods over 24 months; compares 10-fold CV (biased) vs temporally consistent evaluation; varies malware ratio in train/test

## Metrics reported
With temporal bias removed, AUT(F1,24m) = 0.58 (ALG1), 0.32 (ALG2), 0.64 (DL), all lower than the 10-fold F1 reported in the original papers (Fig. 5, Sec. 4; p. 736 of proceedings). Realistic 10% malware ratio in train and test.

## Main findings
Random k-fold splits leak future knowledge (temporal bias) and unrealistic class ratios (spatial bias) jointly inflate reported malware-detection performance; sound evaluation needs time-ordered splits, realistic base rates and a time-decay metric; retraining/active learning only partially mitigates decay.

## Limitations
**Authors' stated:** Android-only evaluation; labelling via VirusTotal thresholds is noisy; ground-truth timestamps can be unreliable; dataset ends 2016.

**Our caveats:** Phishing URLs have much shorter lifetimes than Android malware, so monthly windows may be too coarse; URL datasets commonly lack timestamps at all, making C1/C2 impossible to enforce without re-collection.

## Research gap
No TESSERACT-style constraint set exists for phishing URL datasets; most public URL corpora carry no first-seen timestamps.

## Relevance to our project
Defines the vocabulary (spatial/temporal bias, AUT) that justifies our domain-grouped and, where timestamps exist, time-ordered splits. Our 50/50-ish training ratio is exactly the 'spatial bias' TESSERACT warns about; we should report performance at realistic phishing prevalence as well.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
