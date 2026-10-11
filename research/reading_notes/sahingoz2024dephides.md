# sahingoz2024dephides

## Citation
Sahingoz, Ozgur Koray; Buber, Ebubekir; Kugu, Emin (2024). *DEPHIDES: Deep Learning Based Phishing Detection System*. IEEE Access, 12, pp. 8052-8070. DOI: 10.1109/ACCESS.2024.3352629 URL: https://doi.org/10.1109/ACCESS.2024.3352629

- Type: journal | Theme (L1): c-char-level | Access: full_text | Verified: full
- Local PDF: research/papers/sahingoz2024dephides.pdf

## Verification
Checked 2026-10-11: IEEE Access open-access PDF (ielx7/6287639/6514899/10388305.pdf; CC BY-NC-ND per Crossref) read; Crossref record for DOI 10.1109/ACCESS.2024.3352629 (vol 12, 8052-8070).

## Problem
Large-scale deep-learning URL phishing detection and release of a multi-million URL dataset.

## Method
Character vectorisation of URLs; five architectures compared; extensive related-work table of datasets.

## Dataset(s)
About 5.1M URLs (shared on GitHub ebubekirbbr/dephides): 2,320,893 phishing (PhishTank up to Aug 2018) + legitimate URLs crawled (about 30 per domain) from top-100k domains; 'small' 10% subsample 232,090 phishing / 288,195 legitimate (Sec. IV)

## Features
Learned char features.

## Evaluation protocol
Random train/test splits on small and full datasets

## Metrics reported
CNN best with 98.74% accuracy (abstract; Sec. V).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
CNN > RNN/attention variants at this scale; dataset released.

## Limitations
- Stated by authors: Phishing data up to 2018; legitimate URLs crawled from top domains.
- Our own caveats: Random splits with about 30 URLs per legitimate domain almost guarantee domain overlap between train and test (domain-grouped split needed).

## Research gap
Domain-grouped and temporal evaluation.

## Relevance to our project
Largest public URL dataset for stress-testing; a prime example where domain-grouped splitting would change results.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
