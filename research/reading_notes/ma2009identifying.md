# ma2009identifying

## Citation
Ma, Justin; Saul, Lawrence K.; Savage, Stefan; Voelker, Geoffrey M. (2009). *Identifying suspicious URLs: an application of large-scale online learning*. Proceedings of the 26th International Conference on Machine Learning (ICML '09), pp. 681-688. DOI: 10.1145/1553374.1553462 URL: https://doi.org/10.1145/1553374.1553462

- Type: conference | Theme (L1): a-foundational-lexical | Access: full_text | Verified: full
- Local PDF: research/papers/ma2009identifying.pdf

## Verification
Checked 2026-10-11: Author-hosted PDF (cseweb.ucsd.edu/~voelker/pubs/mal-url-icml09.pdf) read; Crossref record for DOI 10.1145/1553374.1553462 (ICML '09, pp. 681-688).

## Problem
Scale URL classification to continuous, non-stationary streams where batch retraining is infeasible.

## Method
Real-time feature collection system; sparse high-dimensional lexical+host features (grows to millions); compares online algorithms with continuous retraining to batch models retrained at intervals.

## Dataset(s)
Live feed from a large web-mail provider: about 20,000 URLs/day (6-7k malicious, about 2:1 benign:malicious) over 100 days, nearly 2 million URLs (Sec. 4.1)

## Features
Same families as KDD'09 (lexical tokens, WHOIS, DNS, IP, geo, blacklist); feature count grows over time (Fig. 1).

## Evaluation protocol
Temporal: train on days up to t, test on day t+1; cumulative error over 100 days (Fig. 3-4)

## Metrics reported
Up to 99% accuracy on balanced data (abstract); CW online learning tracks batch accuracy with cumulative error about 1-2% while stale batch models degrade (Fig. 3-4; per-day false negatives up to 15% on some days, Sec. 5).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Continuous retraining matters: feature distribution of malicious URLs drifts daily; online CW matches batch at a fraction of cost.

## Limitations
- Stated by authors: Depends on a proprietary labelled feed; host features require live lookups.
- Our own caveats: Day-ahead protocol is strong, but labels come from the same provider's filters (potential label bias).

## Research gap
Public reproducible temporal benchmarks absent.

## Relevance to our project
Primary citation for temporal (day-ahead) evaluation and concept drift; motivates our temporal/cross-dataset splits.

Relevance score: 5/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
