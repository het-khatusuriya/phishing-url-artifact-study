# Search log L3 (XAI, adversarial robustness, calibration, efficiency, datasets)

Date: 2026-10-11. Engines: WebSearch (built-in), WebFetch of doi.org / arxiv.org / semanticscholar api / publisher pages.

## Session log (2026-10-11)

| # | Engine | Query / fetch | Hits examined | Decision |
|---|--------|---------------|---------------|----------|
| 1 | Semantic Scholar API | arXiv:1705.07874 (SHAP) | 1 | Accept lundberg2017shap; S2 DOI field spurious -> DOI left blank |
| 2 | Semantic Scholar API | DOI 10.1038/s42256-019-0138-9 | 1 | Accept lundberg2020treeexplainer; PDF via arXiv 1905.04610 |
| 3 | arXiv | 1706.04599 (Guo calibration) | 1 | Accept guo2017calibration (S2 rate-limited) |
| 4 | Semantic Scholar API | DOI 10.1145/1102351.1102430 | 1 | Accept niculescumizil2005calibration (paywalled) |
| 5 | Semantic Scholar API | DOI 10.1016/j.cose.2023.103545 + UCI id 967 page | 2 | Accept prasad2024phiusiil; dataset facts from UCI |
| 6 | Semantic Scholar API | DOI 10.1016/j.eswa.2018.09.029 | 1 | Accept sahingoz2019ebbu2017; GitHub pdd/input file list for counts |
| 7 | Semantic Scholar API | guessed DOI 10.1016/j.dib.2021.107630 (Hannousse) | 1 | WRONG paper (unrelated Data in Brief) -> discarded; re-searched |
| 8 | Semantic Scholar API | guessed DOI 10.1145/3134600.3134619 (Kintis) | 1 | WRONG (ai.lock) -> discarded; Crossref confirmed 10.1145/3133956.3134002 |
| 9 | Semantic Scholar API | guessed DOI 10.1109/ICCCN.2016.7568488 (Mamun) | 1 | WRONG -> discarded; Crossref confirmed 10.1007/978-3-319-46298-1_30 |
| 10 | Semantic Scholar API | guessed DOI 10.1109/NOMS.2014.6838316 (PhishStorm) | 1 | WRONG -> discarded; Crossref confirmed 10.1109/TNSM.2014.2377295 |
| 11 | Semantic Scholar API | guessed DOI 10.1016/j.cose.2017.07.004 | 1 | WRONG (unrelated) -> discarded |
| 12 | Semantic Scholar API | DOIs for Tian 2018, Verma 2017, Oest 2018, AlEroud 2020, Tranco | 5 | All confirmed |
| 13 | WebSearch | Hannousse Yahiouche 2021 EAAI | 9 | Crossref query -> 10.1016/j.engappai.2021.104347; Mendeley c2gw7fy2j4 v3 |
| 14 | WebSearch | Kintis combosquatting CCS 2017 | 9 | DOI confirmed via Crossref |
| 15 | WebSearch | Mamun 2016 NSS ISCX-URL-2016 | 9 | UNB CIC page fetched for dataset composition |
| 16 | WebSearch | Marchal PhishStorm TNSM 2014 | 10 | Aalto dataset page fetched (96,018 URLs) |
| 17 | WebSearch + Crossref | Bahnsen DeepPhish 2018 | 9 + 2 Crossref queries | No peer-reviewed record found; Black Hat EU 2018 slides used; verified=partial |
| 18 | WebSearch + Crossref | GramBeddings C&S 2023 | 11 | DOI confirmed; dataset page fetched (800k, May 2019-Jun 2021) |
| 19 | WebSearch | SHAP explainable phishing URL 2023-2024 | 9 | Took arXiv 2411.09813 (Mia), iJOE XAI-PhD (Crossref), Sci Rep 2025 (PMC); rejected Indonesian regional journals (unverifiable) |
| 20 | WebSearch | adversarial character-level URL perturbation | 9 | Took Sabir 2005.08454; noted 2025-26 preprints out of scope |
| 21 | WebSearch | SpacePhish ACSAC 2022 | 10 | Accept; arXiv v3 = extended Multi-SpacePhish |
| 22 | WebSearch | Lee et al. MADWeb 2020 | 9 | NDSS page + PDF; workshop DOI not verified |
| 23 | WebSearch | lightweight real-time URL detection | 10 | Took PhishLang (arXiv); SwiftURL/MalURLDozer 2026 not verified -> skipped |
| 24 | WebSearch (x2) | calibration ECE phishing; Platt/isotonic phishing URL | 10 + 9 | No phishing-URL calibration paper found (gap confirmed); took Li et al. ACSAC 2021 (malware) |
| 25 | WebSearch | IDN homograph punycode USENIX/NDSS | 9 | Took Hu et al. USENIX Sec 2021 (page fetched) |
| 26 | WebSearch | Siddhartha Kaggle Malicious URLs sources | 10 | Kaggle meta confirms 651,191; breakdown/licence unreadable -> partial |
| 27 | WebSearch | Arp et al. Dos and Don'ts | 10 | USENIX page fetched; PDF |
| 28 | WebSearch | Alexa retirement May 2022 | 10 | Official page not renderable -> partial, press sources |
| 29 | WebSearch | Tesseract time-aware evaluation | 9 | USENIX page fetched; PDF |
| 30 | WebSearch | Common Crawl benign URLs | 10 | commoncrawl.org overview fetched; PhishSim etc. noted but not added |
| 31 | WebSearch | model size / inference time URL detection | 10 | Nothing verifiable in target venues; Haynes 2021 via Crossref instead |
| 32 | Crossref | Bahnsen 2017 RNN eCrime; Haynes 2021; Li 2021; XAI-PhD; AlEroud; Verma | 6 | All confirmed |
| 33 | Fetch | PhishTank developer_info, OpenPhish feeds, URLhaus API, tranco-list.eu | 4 | Dataset entries written |
| 34 | Fetch | Kaggle pages via curl (meta tags) | 2 | Titles/descriptions only; counts for taruntiwarihp not readable |

Failures: Springer chapter page (auth redirect), ScienceDirect (403), HAL (bot wall), IEEE Xplore (empty), web.archive.org (blocked), Semantic Scholar 429s. PDFs that failed header check were deleted (PMC nihms, HAL document, APWG docs 5349040, UH Verma copy, UMBC AlEroud copy, albahnsen DeepPhish copy).
Duplicate handling: sabir2022urlbug.pdf removed (identical to sabir2022reliability.pdf saved by another agent); mia2024featurestrust.pdf is byte-identical to aslam2024featuretrust.pdf (first author is Mia, not Aslam).
