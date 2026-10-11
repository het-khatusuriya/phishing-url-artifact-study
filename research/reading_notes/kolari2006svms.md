# kolari2006svms

## Citation
Kolari, Pranam; Finin, Tim; Joshi, Anupam (2006). *SVMs for the Blogosphere: Blog Identification and Splog Detection*. AAAI Spring Symposium on Computational Approaches to Analyzing Weblogs (2006). URL: https://www.semanticscholar.org/paper/b54518d807f05ebe5ce39fb7e22f943cd70cb4f1

- Type: conference | Theme (L1): a-foundational-lexical | Access: abstract_only | Verified: partial
- Local PDF: none (not legally downloadable at time of search)

## Verification
Checked 2026-10-11: Semantic Scholar API search result (paperId b54518d8..., DBLP conf/aaaiss/KolariFJ06; title, authors, venue, year). No DOI exists for this symposium paper; full text not retrieved, so verified=partial.

## Problem
Identify blogs and detect spam blogs (splogs).

## Method
SVM classifiers over textual and URL-derived feature sets; URL tokens shown useful.

## Dataset(s)
Blog/splog samples (sizes not retrieved)

## Features
Bag-of-words, anchor text, tokenized URL words.

## Evaluation protocol
Not retrieved

## Metrics reported
Not retrieved.
(Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)

## Main findings
URL-token features contribute to spam-blog detection (often cited as early use of URL lexical features).

## Limitations
- Stated by authors: Not retrieved.
- Our own caveats: Peripheral to phishing; included only for lineage.

## Research gap
n/a

## Relevance to our project
Lineage citation only (tokenised-URL features); low relevance.

Relevance score: 1/5. (Our project: lexical-feature + ensemble + char-level phishing URL detector with explainability on a ~250k-URL binary dataset; concerns: dataset shortcut artifacts (https/www prevalence), domain-grouped and cross-dataset generalization, calibration, robustness.)
