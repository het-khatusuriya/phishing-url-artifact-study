# tang2021survey

## Citation
Lizhen Tang, Qusay H. Mahmoud (2021). A Survey of Machine Learning-Based Solutions for Phishing Website Detection. *Machine Learning and Knowledge Extraction*, pp. 672-694. DOI: 10.3390/make3030034

- URL: https://doi.org/10.3390/make3030034
- Access status: full_text (research/papers/tang2021survey.pdf)
- Verified: yes
- Theme (L2): f - surveys & SoKs discussing evaluation
- Relevance score (1-5): 2

## Verification
Semantic Scholar record (DOI 10.3390/make3030034, MAKE vol. 3 no. 3, CC BY) checked 2026-10-11; PDF from mdpi-res.com. Page range from PDF footer.

## Problem
Compare ML phishing-website solutions, their datasets and reported results.

## Method
Comparative review of ML solutions, features, datasets and reported accuracies

## Dataset(s)
Survey; tabulates datasets (UCI, Mendeley, ISCXURL-2016, PhishTank/OpenPhish + Alexa/Common Crawl crawls)

## Features
URL lexical, content, third-party

## Evaluation protocol
Notes that many solutions report >99% accuracy on single datasets; Table 5 lists 'did not use multiple different datasets to train the model, compare the results' as a limitation

## Metrics reported
Qualitative; reported accuracies 98-99.6% across surveyed works (Table 5).

## Main findings
Single-dataset evaluation and reliance on PhishTank + Alexa/Common Crawl sources are the norm.

## Limitations
**Authors' stated:** Breadth over depth.

**Our caveats:** Does not analyse artefacts or base rates.

## Research gap
N/A

## Relevance to our project
Evidence that single-dataset >99% accuracy is the literature norm, which our cross-dataset results will contextualise.

> Project context: Our detector: lexical-feature + ensemble phishing-URL classifier trained on a ~250k binary URL dataset in which legitimate URLs are ~93% https and mostly 'www.' while phishing URLs are ~50% https; it predicted https://google.com/ as malicious. Planned: domain-grouped splits, artifact-removal ablations, cross-dataset tests, calibration and robustness analysis.
