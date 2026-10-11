# Search log - Agent L1 (detection methods)

Date of all searches: 2026-10-11. Theme: (a) foundational lexical/host + classical ML, (b) ensembles/hybrids 2020-2026, (c) character-level deep models, (d) transformer / pretrained-LM / LLM URL classifiers.

Verification tooling used for every included paper: Crossref REST API (`api.crossref.org/works/<DOI>`) for DOIs; arXiv Atom API (`export.arxiv.org/api/query?id_list=`) for arXiv ids; Semantic Scholar Graph API and OpenAlex API for abstracts/open-access links; publisher pages where reachable (Springer article pages, UCI repository, USENIX, Microsoft Research, GitHub). Raw API responses were kept in the session scratchpad (`scratchpad/crossref/*.json`, `scratchpad/arxiv/feed.xml`, `scratchpad/s2/*.json`, `scratchpad/oa/*.json`).

Legend for decisions: INC = included (row in `paper_metadata_L1.csv`, note in `reading_notes/`), EXC = excluded, UNV = could not verify.

## 1. Seed list supplied by the coordinator (verified directly by identifier)

| Query / identifier | Engine | Hits looked at | Decision |
|---|---|---|---|
| DOI 10.1145/1557019.1557153 (Ma et al. KDD 2009) | Crossref + S2 | 1 | INC `ma2009beyond`; author-hosted PDF at cseweb.ucsd.edu |
| DOI 10.1145/1553374.1553462 (Ma et al. ICML 2009) | Crossref + S2 | 1 | INC `ma2009identifying`; author-hosted PDF |
| DOI 10.1145/1961189.1961202 (Ma et al. TIST 2011) | Crossref + S2 | 1 | INC `ma2011learning` (abstract only). S2's "open access PDF" (eScholarship qt4j86t705) turned out to be Ma's PhD dissertation, not the article; downloaded file inspected and discarded. |
| DOI 10.1145/1866423.1866434 (Blum et al. AISec 2010) | Crossref + OpenAlex | 1 | INC `blum2010lexical` (abstract only; no legal PDF found) |
| "Blum Wardman Solorio Warner lexical feature phishing URL online learning pdf" | WebSearch | 9 | No open PDF; surfaced PhishDef (arXiv 1009.2275) which was added (INC `le2011phishdef`) |
| Kolari Finin Joshi splog / SVMs for the blogosphere | S2 search API; DBLP (blocked by bot protection) | 3 | INC `kolari2006svms` as verified=partial (no DOI; symposium paper; low relevance, lineage only) |
| DOI 10.1145/2699026.2699115 (Verma & Dyer CODASPY 2015) | Crossref + OpenAlex | 1 | INC `verma2015character` (abstract only) |
| "Verma Dyer On the character of phishing URLs CODASPY 2015 pdf" | WebSearch | 10 | No open PDF (author page lists citation only) |
| arXiv 1701.07179 (Sahoo, Liu, Hoi survey) | arXiv API | 1 | INC `sahoo2017survey` (full text) |
| DOI 10.1007/978-3-319-46298-1_30 (Mamun et al. NSS 2016 / ISCX-URL-2016) | Crossref + Springer page | 1 | INC `mamun2016lexical` (abstract only) |
| arXiv 1702.08568 (Saxe & Berlin eXpose) | arXiv API | 1 | INC `saxe2017expose` |
| arXiv 1802.03162 (Le et al. URLNet) | arXiv API | 1 | INC `le2018urlnet` |
| DOI 10.1109/ECRIME.2017.7945048 (Bahnsen et al.) | Crossref | 1 | INC `bahnsen2017classifying`; author-hosted camera-ready PDF (albahnsen.github.io) |
| DOI 10.1109/ICASSP40776.2020.9053670 (Texception) | Crossref + S2 | 1 | INC `tajaddodianfar2020texception`; PDF from Microsoft Research site |
| "Huang PhishingNet phishing URL detection CNN attention hierarchical RNN" | WebSearch | 9 | Identified as Huang, Yang, Qin, Wen, TrustCom/BigDataSE 2019; DOI verified via Crossref -> INC `huang2019phishingnet` (abstract only) |
| DOI 10.1016/j.cose.2022.102964 (GramBeddings) | Crossref + DBLP listing + GitHub README + dataset page | 1 | INC `bozkir2023grambeddings` (abstract text unavailable; metadata verified) |
| arXiv 2106.05256 / URLTran | arXiv API + Crossref | 1 | INC `maneriker2021urltran`. Guessed DOI 10.1109/BigData52589.2021.9671622 was WRONG (it resolves to Singh & Goyal); correct venue/DOI is MILCOM 2021, 10.1109/MILCOM52596.2021.9653028 |
| "URLBERT contrastive adversarial pre-trained model URL classification arXiv 2024" | WebSearch + arXiv API + Crossref | 9 | arXiv 2402.11495 (retitled "Continuous Multi-Task Pre-training..."), journal version Computer Networks 270:111513 (2025) -> INC `li2025urlbert` |
| "PhishBERT / large-scale pretrained deep model for phishing URL detection ICASSP 2023" | WebSearch + Crossref + S2 | 9 | INC `wang2023phishbert` (abstract only) |
| "TransURL ... Computer Networks 2024" | WebSearch + arXiv API + Crossref | 9 | INC `liu2024transurl` (arXiv 2312.00508; DOI 10.1016/j.comnet.2024.110707) |
| "large language model phishing URL classification 2025 fine-tuned LLM" | WebSearch (extended) | 9 | INC `ali2025phishurldetect`, `kibriya2025lightweight`, `trikilis2026reasoning`, `chen2026memophishagent`, `tian2025survey`, `ghalechyan2024empirical`; URL2Graph++ (arXiv 2509.10287) seen but EXC (graph model, out of theme scope); PhishLang (arXiv 2408.05667) EXC (HTML/page-based) |

## 2. Additional identifier-based searches (my own candidate list)

| Identifier | Engine | Decision |
|---|---|---|
| 10.1145/1314389.1314391 Garera et al. 2007 | Crossref + OpenAlex | INC `garera2007framework` |
| 10.1145/1099554.1099649 Kan & Thi 2005 | Crossref + OpenAlex | INC `kan2005fast` |
| McGrath & Gupta LEET 2008 | USENIX legacy page + PDF | INC `mcgrath2008behind` (partial: no DOI) |
| 10.1109/TNSM.2014.2377295 PhishStorm | Crossref; orbilu.uni.lu repository PDF | INC `marchal2014phishstorm` |
| 10.1016/j.eswa.2018.09.029 Sahingoz 2019 | Crossref + S2 + Marmara repo (PDF link 500) | INC `sahingoz2019machine` (abstract only) |
| 10.1016/j.ins.2019.01.064 Chiew 2019 | Crossref + OpenAlex | INC `chiew2019hybrid` |
| 10.1007/s12652-019-01311-4 CatchPhish | Crossref + Springer page | INC `rao2020catchphish` |
| 10.1109/ACCESS.2020.2991403 PhishHaven | Crossref; IEEE OA PDF | INC `sameen2020phishhaven` |
| 10.1109/ACCESS.2022.3168681 PILU-90K | Crossref; IEEE OA PDF | INC `sanchezpaniagua2022phishing` |
| 10.1007/s12652-022-04426-3 Jalil 2023 | Crossref + Springer page | INC `jalil2023highly` |
| 10.1016/j.cose.2023.103545 PhiUSIIL | Crossref + UCI page | INC `prasad2024phiusiil` (abstract not retrievable) |
| 10.3390/electronics9091514 Aljofey 2020 | Crossref; MDPI CDN PDF | INC `aljofey2020effective` |
| 10.3390/electronics12010232 Alshingiti 2023 | Crossref; MDPI CDN PDF | INC `alshingiti2023deep` (low relevance: tabular features) |
| 10.1155/2019/2595794 PDRCNN | Crossref (abstract) | INC `wang2019pdrcnn` (PDF blocked by Wiley bot protection) |
| 10.1016/j.comnet.2020.107275 Wei 2020 | Crossref + S2 | INC `wei2020accurate` |
| 10.1007/s00521-021-06401-z Ozcan | Crossref + S2 | INC `ozcan2023hybrid` (print year 2023; Springer PDF not open) |
| 10.1016/j.procs.2021.07.040 Haynes 2021 | Crossref + OpenAlex | INC `haynes2021lightweight` (ScienceDirect PDF blocked) |
| arXiv 2011.03040 Rudd & Abdallah | arXiv API | INC `rudd2020training` |
| 10.1109/ACCESS.2024.3352629 DEPHIDES | Crossref; IEEE OA PDF via OpenAlex link | INC `sahingoz2024dephides` |
| 10.1016/j.eswa.2023.121183 Opara 2024 | Crossref | EXC (URL + HTML model; outside URL-only method scope) |
| 10.1016/j.inffus.2024.102638 PMANet | Crossref + S2 | INC `liu2025pmanet` |
| 10.3390/make6010018 Trad & Chehab | Crossref; MDPI CDN PDF | INC `trad2024prompt` |
| 10.1038/s41598-024-74725-6 Ghalechyan | Crossref + OpenAlex | INC (abstract only; Nature/PMC PDF downloads failed) |
| 10.1038/s41598-025-26653-2 Kibriya | Crossref; Nature OA PDF | INC `kibriya2025lightweight` |

## 3. Topical web searches for 2020-2026 ensembles / explainability

| Query | Engine | Hits looked at | Decisions |
|---|---|---|---|
| "phishing URL detection ensemble stacking XGBoost random forest lexical features journal 2023 2024 2025 cross-dataset generalization" | WebSearch (extended) | 9 | INC `sankaranarayanan2024ensemble` (PLOS ONE 2024), `yi2026crossdataset` (Wiley Security and Privacy 2026), `khan2026stacking` (Frontiers AI 2026). EXC: PhishGuard arXiv 2409.19825 (unreviewed preprint, superseded by the above), ScienceDirect "filter-based feature selection stacking" (could not verify DOI/venue), ResearchGate "XGBoost cross-dataset validation" (no verifiable record), GitHub repo, IJACSA paper (not verified), arXiv 2605.17891 (not verified in time) |
| "explainable phishing URL detection SHAP ensemble lexical features 2024 2025 journal" | WebSearch | 9 | EXC all: J. Eng. 10.1049/tje2.70110 uses website (non-URL) features; ETASR 2026 hybrid uses web-page behaviour features; Indonesian regional journals and RIT thesis not peer-reviewed venues of sufficient standing / not verifiable in time |
| "Sahingoz Buber Demir Diri Machine learning based phishing detection from URLs pdf Ebbu2017" | WebSearch | 9 | Confirmed metadata and dataset size (73,575 URLs) via secondary sources; no open PDF |
| "Tajaddodianfar Stokes Gururajan Texception pdf microsoft research" | WebSearch + MSR JSON API | 9 | Found legal publisher-hosted PDF |
| "GramBeddings Bozkir Dalgic Aydos abstract ..." and "PhiUSIIL Prasad Chandra abstract" | WebSearch | 10 + 10 | Confirmed bibliographic details; abstracts not retrievable from blocked publisher pages |

## 4. Access notes
- Blocked for automated access (403/bot checks): ACM DL, IEEE Xplore HTML, ScienceDirect, Wiley/Hindawi, MDPI main site (CDN mdpi-res.com worked), Nature article pages (one PDF succeeded, one failed), Europe PMC render endpoint, DBLP search API (Anubis). Where blocked, metadata came from Crossref/OpenAlex/Semantic Scholar APIs and the paper is marked `abstract_only`.
- All 26 saved PDFs were checked to start with `%PDF`; non-PDF downloads were deleted. The mis-identified dissertation PDF for `ma2011learning` was removed.

## 5. Papers suspected to exist but NOT verified (not included)
- "XGBoost-based URL phishing detection method with cross-dataset validation" (ResearchGate listing, 2025) - no DOI/venue found.
- "A Filter-Based Feature Selection Framework to Detect Phishing URLs Using Stacking Ensemble Machine Learning" (ScienceDirect listing S1526149225003716, 2025) - venue/DOI not confirmed.
- "Explainable Machine Learning for Phishing Detection on Heterogeneous Datasets with MCP-Enabled Deployment" (arXiv 2605.17891) - not verified via arXiv API.
- Kolari et al. 2006 included only as partial (no DOI, no full text).
- Venue for `chen2026memophishagent` (ACL 2026 Industry Track) rests on the arXiv comment field only.
