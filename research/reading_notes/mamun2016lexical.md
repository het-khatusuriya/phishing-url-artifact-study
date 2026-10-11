> **Duplicate record.** Same paper as `mamun2016iscxurl` (identical DOI); cite `mamun2016iscxurl`. Kept for traceability of the mamun2016lexical search path.

# mamun2016lexical

## Citation
Mamun, Mohammad Saiful Islam; Rathore, Mohammad Ahmad; Lashkari, Arash Habibi; Stakhanova, Natalia; Ghorbani, Ali A. (2016). *Detecting Malicious URLs Using Lexical Analysis*. Network and System Security (NSS 2016), Lecture Notes in Computer Science vol. 9955, Springer, pp. 467-482. DOI: 10.1007/978-3-319-46298-1_30 URL: https://doi.org/10.1007/978-3-319-46298-1_30

- Type: conference | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: full
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Crossref record for DOI 10.1007/978-3-319-46298-1_30 (LNCS, pp. 467-482) and Springer chapter page (abstract, NSS 2016, LNCS 9955).

## Problem
Lightweight lexical detection and type-categorisation of malicious URLs (spam, phishing, malware, defacement).

## Method
Extracts lexical/statistical features (lengths, counts, entropy, token statistics, argument features); studies which obfuscation tricks relate to each URL type; defacement on trusted Alexa sites considered.

## Dataset(s)
ISCX-URL-2016 (UNB CIC): 'over 110,000 URLs' across benign, spam, phishing, malware, defacement (abstract)

## Features
Lexical features incl. lengths of URL components, counts of delimiters/digits, entropy, longest token/argument lengths (one example feature named on the Springer page).

## Evaluation protocol
Per-class binary and multi-class experiments; split details not in abstract

## Metrics reported
Abstract gives no numbers.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
Lexical analysis is effective and efficient for proactive detection; released the ISCX-URL-2016 benchmark.

## Limitations
- Stated by authors: Not available.
- Our own caveats: ISCX-URL-2016 benign class drawn from Alexa top sites; later studies note duplicate/near-duplicate URLs; features partially overlap with ours, so cross-dataset use needs care.

## Research gap
Benchmark artifacts and temporal validity not analysed.

## Relevance to our project
Source of ISCX-URL-2016, a candidate external test set for our cross-dataset generalisation study.

Relevance score: 4/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
