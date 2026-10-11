# ma2011learning

## Citation
Ma, Justin; Saul, Lawrence K.; Savage, Stefan; Voelker, Geoffrey M. (2011). *Learning to detect malicious URLs*. ACM Transactions on Intelligent Systems and Technology, 2(3), Article 30, pp. 1-24. DOI: 10.1145/1961189.1961202 URL: https://doi.org/10.1145/1961189.1961202

- Type: journal | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1145/1961189.1961202 (TIST vol 2 issue 3, 2011, pp. 1-24) and Semantic Scholar record. NOTE: the eScholarship PDF that Semantic Scholar lists as open access for this DOI is actually Justin Ma's 2010 UCSD PhD dissertation, not the TIST article, so it was NOT saved as this paper's full text.

## Problem
Journal synthesis: large-scale, real-time URL classification with lexical and host features.

## Method
Unifies the batch (KDD'09) and online (ICML'09) studies; adds analysis of feature importance and system considerations.

## Dataset(s)
Consolidates the KDD/ICML datasets: about 2M-URL web-mail feed over 100 days plus directory/blacklist pairings

## Features
As in ma2009beyond / ma2009identifying.

## Evaluation protocol
Random splits and day-ahead temporal evaluation (as in the conference versions)

## Metrics reported
Abstract-level only here; conference versions report 95-99% accuracy and about 1-2% cumulative error online.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Same conclusions as the conference papers with extended analysis.

## Limitations
- Stated by authors: See conference versions.
- Our own caveats: Content assessed via metadata and the conference papers; article itself paywalled.

## Research gap
As above.

## Relevance to our project
Preferred archival citation for the Ma et al. feature families.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
