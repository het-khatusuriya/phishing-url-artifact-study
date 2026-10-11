# marchal2014phishstorm

## Citation
Marchal, Samuel; Francois, Jerome; State, Radu; Engel, Thomas (2014). *PhishStorm: Detecting Phishing With Streaming Analytics*. IEEE Transactions on Network and Service Management, 11(4), pp. 458-471. DOI: 10.1109/TNSM.2014.2377295 URL: https://doi.org/10.1109/TNSM.2014.2377295

- Type: journal | Theme (L1): a-foundational-lexical | Access: full_text | Verified: full
- Local PDF: research/papers/marchal2014phishstorm.pdf

## Verification
Checked 2026-10-11: Author-hosted PDF (orbilu.uni.lu, University of Luxembourg repository) read; Crossref record for DOI 10.1109/TNSM.2014.2377295 (TNSM 11(4), 458-471).

## Problem
Real-time phishing URL rating for proxies/mail servers using URL-word relatedness.

## Method
Splits URL into registered domain (mld.ps) vs rest; computes relatedness among words using search-engine query logs; features on word counts, brand presence, Alexa rank; ML classification and a confidence-rated score; Bloom-filter streaming design.

## Dataset(s)
96,018 URLs: 48,009 phishing (PhishTank, from 53,089 unique) + 48,009 legitimate (DMOZ); released as urlset.csv (Sec. VI-A)

## Features
Intra-URL relatedness (12 features), word counts, Alexa ranking of mld.ps.

## Evaluation protocol
10-fold cross-validation, 100 runs (Sec. VI-B)

## Metrics reported
Accuracy 94.91% with 1.44% FPR after threshold tuning (abstract; Sec. VI-C), 95.66% at default threshold; features 1-9 alone 93.48% (Sec. VI-C).
(Numbers taken from the full text; section/table references given where identified.)

## Main findings
Legitimate URLs show coherent word relatedness across domain and path; phishing URLs do not.

## Limitations
- Stated by authors: Depends on search-engine query APIs; relatedness changes over time.
- Our own caveats: The released 'PhishStorm' dataset is widely reused (e.g., in Kaggle mixes); DMOZ benign class again homepage-heavy.

## Research gap
External-API dependence conflicts with offline/lexical deployment.

## Relevance to our project
Source of a widely reused 96k dataset; useful for cross-dataset tests and to discuss API-dependent features we deliberately avoid.

Relevance score: 3/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
