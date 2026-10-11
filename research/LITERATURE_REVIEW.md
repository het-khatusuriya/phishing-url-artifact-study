# Literature Review — Malicious / Phishing URL Detection and the Realism of its Evaluation

Version 1, 2026-10-11. Scope, sources and screening are in §1; the per-paper evidence is in `reading_notes/<citekey>.md`; the comparison table is `LITERATURE_SURVEY_TABLE.md`; metadata in `paper_metadata.csv`; bibliography in `references.bib`.

**Reading conventions.** Numbers quoted below are the numbers *reported by the cited authors*; none was reproduced by us unless explicitly marked "(ours)". Scores from different papers are **not comparable** with each other: datasets, label definitions, class ratios, splits and metrics all differ. Where a note is based on the abstract or publisher page only, the paper is marked †. Preprints are marked ‡.

---

## 1. Method of the review

### 1.1 Search and screening

Three parallel searches (2026-10-11) covered (L1) detection methods, (L2) evaluation realism, and (L3) explainability, robustness, calibration, efficiency and datasets. Engines and indexes: web search, arXiv API, Crossref, Semantic Scholar, OpenAlex, USENIX/NDSS proceedings pages, IEEE Xplore/ACM/Springer/ScienceDirect/MDPI landing pages, UCI, Mendeley Data, Zenodo. Query strings and inclusion/exclusion decisions are logged in `search_log_L1.md`, `search_log_L2.md`, `search_log_L3.md`.

Inclusion: peer-reviewed or clearly labelled preprint work on (a) URL-based malicious/phishing detection, (b) evaluation methodology for security ML that applies to it, (c) datasets and feeds used in this study, (d) explainability, calibration, robustness or efficiency relevant to URL classifiers. Exclusion: papers whose identity (title, authors, venue, DOI/arXiv id) could not be confirmed on an authoritative page; content/visual-only phishing detectors unless they inform evaluation; vendor marketing.

### 1.2 Outcome

| | Count |
|---|---|
| Unique verified sources | 111 after removing 3 duplicate records of the same DOI (104 fully verified; 7 partially verified, e.g. no DOI or venue page available) |
| Full text read: 70 legal open-access PDFs in `papers/`, plus dataset/feed pages read as primary sources | 75 |
| Abstract / publisher page only (marked †) | 35 |
| Paywalled, metadata only | 1 |
| Candidate items rejected as unverifiable | 9 (listed at the end of each search log; e.g. a guessed DOI for Marchal et al. *Off-the-Hook* that resolved to another paper) |

Corrections found during verification and propagated to the bibliography: URLTran was published at **MILCOM 2021**, not IEEE BigData [maneriker2021urltran]; URLBERT appeared in *Computer Networks* 2025 under a new title [li2025urlbert]; arXiv 2411.09813 is first-authored by **Maraz Mia** [mia2024featurestrust]; the DeepPhish work is verifiable only as a Black Hat talk [bahnsen2018deepphish].

This review is systematic and traceable but **not exhaustive**: ACM/IEEE full texts behind paywalls were not read, and Kaggle-hosted notebooks and grey literature were excluded.

---

## 2. Lexical and handcrafted URL features

The field's foundation is the observation that the URL string alone carries strong signal. McGrath and Gupta measured, on 2007–08 PhishTank/MarkMonitor feeds against DMOZ, much longer URLs (modal length 67–107 vs 22 characters), brand tokens in 50–75 % of phishing URLs, and frequent subdomains [mcgrath2008behind]. Garera et al. built a taxonomy of URL obfuscation (IP hosts, redirection, brand in host/path) [garera2007framework†]. Ma et al. showed that tens of thousands of automatically generated bag-of-token features plus host properties reach 95–99 % accuracy, and — importantly for us — that **training on one data source and testing on another raised error to roughly 14–21 %** (their Table 4) [ma2009beyond]; their online-learning follow-up used a 100-day, day-ahead protocol on ~2 M web-mail URLs and showed that stale batch models degrade [ma2009identifying, ma2011learning†]. Subsequent lexical work added obfuscation-resistant features and online AROW learning [le2011phishdef], online confidence-weighted learning [blum2010lexical†], character-distribution statistics [verma2015character†, verma2017whatsinaurl†], word-level NLP features [sahingoz2019machine†] and search-engine word relatedness [marchal2014phishstorm]. ISCX-URL-2016 released a five-class lexical benchmark [mamun2016iscxurl]. The survey by Sahoo et al. consolidated the area and listed the absence of standardised benchmarks, concept drift and adversarial evasion as open challenges [sahoo2017survey].

**Common thread relevant to us.** Almost every foundational dataset pairs a phishing feed (PhishTank, MarkMonitor) with a benign *directory or popularity list* (DMOZ, Yahoo random, Alexa). Several authors note in passing that the benign side is homepage-heavy [mcgrath2008behind, marchal2014phishstorm], which makes length, path depth and token counts separable for reasons unrelated to maliciousness.

## 3. Classical classifiers, ensembles and hybrids

Tree ensembles dominate tabular URL work. Random forests were best in ISCX-URL-2016 (≈99 % per class) [mamun2016iscxurl], CatchPhish (TF-IDF + handcrafted, 94–98 %) [rao2020catchphish†], hybrid feature selection (94.6 % with 10 of 48 features) [chiew2019hybrid†] and multi-dataset studies (91.6–96.9 % across six datasets) [jalil2023highly†]. Ensembles and stacking add little: on the 651k Kaggle corpus, stacking reached 96.8 % against 95.7 % for LightGBM [sankaranarayanan2024ensemble]; on a 248k Kaggle feature table, a Bayesian-tuned stacking ensemble matched but did not exceed Extra Trees in AUC (0.9947 vs 0.9948) [khan2026stacking]; PhishHaven's voting ensemble reported 98 % on Alexa homepages vs generated URLs [sameen2020phishhaven]. PhiUSIIL combined URL similarity indices with incremental learning and released the 235,795-URL dataset we use as Corpus A [prasad2024phiusiil†]. Noisy feature-subset voting ensembles were proposed as a robustness device [lee2020robustphishing].

**Assessment.** The marginal gain of hybrid ensembles over a single well-configured tree ensemble is small, and is reported almost exclusively on random splits of a single dataset. The audited repository repeats this pattern: its 1:2:2 soft vote does not beat its own random forest (`REPOSITORY_AUDIT.md` §5).

## 4. Character-level and sequence models

Character CNNs (eXpose: +5–10 % detection rate at 0.1 % FPR over manual features on proprietary data [saxe2017expose‡]), character LSTMs (98.7 % vs 93.5 % for RF on 2 M PhishTank/Common Crawl URLs with 3-fold CV [bahnsen2017rnnurl]) and joint character+word CNNs (URLNet, with a time-ordered 60/40 split and TPR at FPR 10⁻⁴–10⁻¹ [le2018urlnet‡]) established learned representations. Later variants: CNN+attention RNN [huang2019phishingnet†], BiLSTM+CNN [wang2019pdrcnn†], Inception-style char/word CNN evaluated at 0.01 % FPR on production telemetry [tajaddodianfar2020texception], char-CNN with stripped `http://`, `https://` and `www.` prefixes [aljofey2020effective], mobile-sized CNN [wei2020accurate†], DNN-LSTM [ozcan2023hybrid†], n-gram embeddings with attention (GramBeddings, 800k URLs collected 2019–2021) [bozkir2023grambeddings†], and a 5.1 M-URL CNN study [sahingoz2024dephides]. Alshingiti et al. use CNN/LSTM on 30 pre-extracted features rather than raw characters [alshingiti2023deep].

Two observations matter for our design. First, Aljofey et al. **explicitly remove the scheme and `www.` prefix** before modelling [aljofey2020effective] — an implicit acknowledgement that these tokens are recording artifacts — yet they do not measure the effect. Second, the production studies with temporal splits and low-FPR operating points [le2018urlnet, tajaddodianfar2020texception, maneriker2021urltran] report far lower true-positive rates at realistic FPRs than the 97–99 % accuracies typical of public-benchmark papers, which illustrates how much evaluation design changes the picture.

## 5. Transformers, pre-trained URL encoders and LLMs

URLTran fine-tuned BERT/RoBERTa on six weeks of Microsoft telemetry (temporal split, 1:20 class ratio) and reached TPR 86.8 % at FPR 0.01 % vs 71.2 % for URLNet [maneriker2021urltran]. Generic NLP pre-training did not transfer straightforwardly in Rudd and Abdallah's study, where a mixed-objective transformer only matched a 1-D CNN [rudd2020training‡]. URL-specific pre-training at billion-URL scale followed (PhishBERT [wang2023phishbert†]; URLBERT, with TPR ≈ 0.8 at FPR 10⁻³ and the observation that classical KNN/RF/NB still exceed 96 % accuracy on the same benchmark [li2025urlbert]; TransURL [liu2024transurl]; PMANet [liu2025pmanet†]). Lightweight transformers for client-side use report 74 MB–7.3 GB memory per model and MobileBERT accuracy 0.96 [roy2024phishlang‡, haynes2021lightweight†]. LLM work spans prompting vs fine-tuning on the 11k Hannousse set (fine-tuned GPT-2 F1 97.3 %, prompted models degrade under class imbalance) [trad2024prompt], least-to-most prompting (average F1 0.904) [trikilis2026reasoning‡], frozen LLM embeddings with a small head on the 651k Kaggle set (97.5 %) [kibriya2025lightweight], LoRA fine-tuning [ali2025phishurldetect†] and multimodal agents [chen2026memophishagent‡]. A 2025 survey notes the lack of proper baselines and standard benchmarks [tian2025survey‡].

**Assessment.** TransURL is the only learned-representation paper in our set with a substantial cross-dataset experiment: all models drop sharply (GramBeddings to ≈70 % accuracy), TransURL least (90.2 %) [liu2024transurl]. Its Table 2 also documents TLD and length distribution differences between datasets — candidate artifacts that were not analysed further.

## 6. Evaluation realism: drift, bias, leakage and base rates

This is the body of work our study builds on most directly.

**General security-ML pitfalls.** Arp et al. catalogue ten pitfalls in 30 top-venue papers; sampling bias (P1), spurious correlations — "artifacts unrelated to the security problem create shortcut patterns for separating classes" (P4) — and the base-rate fallacy (P8) are each present in most surveyed work [arp2022dosdonts]. Sommer and Paxson's closed-world critique [sommer2010closedworld†] and Axelsson's base-rate analysis [axelsson2000baserate†] are the classical antecedents. Apruzzese et al. show that single-dataset, single-run results can change method rankings [apruzzese2023pragmatic] and that real attackers use cheap problem-space manipulations [apruzzese2023realattackers]. Malware research reached similar conclusions about dataset composition [dambra2023decoding, botacin2021pitfalls†].

**Temporal bias and drift.** TESSERACT formalised temporal and spatial bias and showed that time-aware evaluation lowers F1 well below published 10-fold numbers (AUT(F1, 24 m) 0.32–0.64) [pendlebury2019tesseract, kan2024tesseractext‡]. Transcend and TRANSCENDENT detect drift and reject unreliable predictions [jordaney2017transcend, barbero2022transcending]; continuous learning reduces but does not remove decay [chen2023continuous]. For phishing specifically: content-based detectors lost 20.65 points over 2018–2020 without continual learning [ejaz2023lifelong]; URL models trained on 2016 data degrade on 2020 URLs [sanchezpaniagua2022phishing]; drift studies remain largely e-mail-centred [fernando2026driftphish‡] or report near-perfect drift-aware accuracy without cross-source validation [krishnan2025drift†]. Phishing sites live hours to days [oest2020sunrise], and blacklist-derived labels are delayed and biased towards non-evasive phish [oest2020phishtime]. Pendlebury et al. themselves note that public URL corpora lack first-seen timestamps, which prevents TESSERACT-style evaluation [pendlebury2019tesseract].

**Dataset bias and benign-class composition.** This is where the evidence is strongest and most specific:

- Using Alexa index pages as the benign class "creates a bias in the data" because phishing feeds contain full URLs [sabir2022reliability].
- Benchmarks are "dataset dependent and far away from generalization"; Alexa lists should not be used directly because they lack sub-domains and paths [hannousse2021benchmark].
- Prior work uses balanced datasets and Alexa domain-only benign sets; performance degrades as the legitimate:phishing ratio grows [elaassal2020benchmarking]; generalisation studies "are rarely mentioned" [das2020sokphishing].
- The benign set must include unpopular sites and URLs with paths, at about 1:100 prevalence, with temporal tests [marchal2018designing].
- Models trained on homepage-vs-phishing data **lose 27–39 % accuracy on legitimate login URLs** (best 69.5 %), and URL-length separability largely disappears [sanchezpaniagua2022phishing].
- Top lists are unstable, manipulable and differ structurally; any list is a proxy for popularity, not legitimacy [lepochat2019tranco, scheitle2018toplists]; Alexa itself was retired in 2022 [alexa2022retirement, zieni2023survey].
- Most of 55 surveyed phishing detectors risk high false alarms because of limited benign diversity [alam2026philter‡].
- Public datasets "suffer from leakage and unrealistic base rates" [dalton2025phreshphish‡]; synthetic debiasing has been proposed [kulkarni2024mitigating‡]; benchmarking frameworks exist [zeng2020phishbench†].
- Surveys repeatedly flag single-dataset evaluation, old data and accuracy on imbalanced sets [do2022deeplearning, tang2021survey, zieni2023survey].

**Cross-dataset generalisation.** Cross-dataset accuracy falls to 51 % and 59 % between two public URL feature datasets, with SHAP showing the same features changing sign [mia2024featurestrust]; detectors "work effectively only when the test sets are split from the same training dataset", with URL recording format named as a cause [rashid2024domainadapt†]; a 57.4 % cross-dataset baseline between UCI and PhiUSIIL [henry2026ensembletransfer†]; tree ensembles averaging 94 % over four secondary test sets [yi2026crossdataset†] (sources of the test sets could not be checked); and an external benign test with FPR 86.84 % (95 % CI 83.6–90.0) after canonicalisation in a single-author preprint that names the `https://` and `www.` shortcut directly [giri2026shieldphish‡]. For phishing e-mail, a dataset-identification probe reached 97–98 % accuracy and artifact-removal ablations were used to expose corpus markers [bhuiyan2026fragility].

## 7. Explainability

SHAP provides additive attributions with consistency guarantees [lundberg2017shap]; TreeExplainer computes them exactly for tree ensembles and supports global summaries [lundberg2020treeexplainer]. In phishing work, SHAP is used mostly for feature selection (XAI-PhD, 99.8 % accuracy reported [alfayoumi2024xaiphd†]; Kehkashan et al., RF 97.0 % on the UCI set [kehkashan2025explainable]; Khan et al. [khan2026stacking]) or for post-hoc justification [yi2026crossdataset†]. Only Mia et al. use SHAP *diagnostically*, to show feature effects differ across datasets [mia2024featurestrust]; Arp et al. recommend explanation-based artifact checks in general [arp2022dosdonts]. Lundberg and Lee note that KernelSHAP assumes feature independence, which is violated by correlated lexical counts [lundberg2017shap] — the audited repository uses KernelSHAP on the full soft-vote, at high cost.

## 8. Adversarial robustness and obfuscation

Fifty reproduced URL detectors fell from median MCC 0.92 to 0.02 on cheaply registrable adversarial URLs (URLBUG: homoglyphs, hyphenation, subdomain insertion, character swaps) [sabir2022reliability]. SpacePhish distinguishes problem-space from feature-space perturbations and finds statistically significant 3–10 % degradation from cheap evasions [apruzzese2022spacephish]. GAN- and LSTM-generated URLs evade detectors [aleroud2020gan†, bahnsen2018deepphish], as do black-box attacks on ad-URL classifiers [nowroozi2022advurl‡]. Measurement studies describe the realistic threat model: IDN homographs still bypass browser defences [hu2021idnhomograph], squatting phishing domains evade blacklists for weeks [tian2018needle], combosquatting is long-lived [kintis2017combosquatting], and phishing kits cloak against crawlers [oest2018phisherkit]. URLTran's adversarial fine-tuning preserves low-FPR behaviour against homoglyph and compound-split attacks [maneriker2021urltran].

**Gap relevant to us.** Robustness studies measure *adversarial* manipulations; none measures sensitivity to *label-irrelevant recording variants* (scheme present or absent, `www.` present or absent, default port, fragments), which our audit shows is where lexical models are most fragile.

## 9. Calibration and operating points

Boosting pushes probabilities away from 0 and 1 while bagged trees are near-calibrated; Platt and isotonic scaling correct this given enough held-out data [niculescumizil2005calibration]. Guo et al. popularised ECE and reliability diagrams and warned that post-hoc calibration assumes the calibration set matches deployment [guo2017calibration]. For Android malware, calibration degrades under dataset shift and fails under adversarial examples [li2021malwarecalibration]. Production URL papers report TPR at fixed low FPR [saxe2017expose, le2018urlnet, tajaddodianfar2020texception, maneriker2021urltran, li2025urlbert]; most public-benchmark papers report accuracy at 0.5. **No study in our set measures calibration of phishing-URL classifiers or whether validation-chosen FPR thresholds hold under cross-dataset shift** (confirmed by targeted searches logged in `search_log_L3.md`).

## 10. Efficiency and deployability

Lexical tree models are fast and small; char-LSTMs were ≈3× slower than RF in Bahnsen et al. (281 vs 942 URLs/s) [bahnsen2017rnnurl]; PDRCNN reports 0.4 ms/URL [wang2019pdrcnn†]; frozen-LLM embeddings 0.119 ms/sample excluding embedding cost [kibriya2025lightweight]; MobileBERT-class models are the lightest transformers but still 74 MB+ [roy2024phishlang‡]; agents need ≈1 s/URL [chen2026memophishagent‡]. External lookups (WHOIS, search engines) cost seconds per URL [le2011phishdef, marchal2014phishstorm]. Head-to-head latency and size comparisons on identical hardware and data are rare.

## 11. Datasets

| Dataset | Size / classes | Benign source | Timestamps | Known issues (literature + our audit) |
|---|---|---|---|---|
| ISCX-URL-2016 [mamun2016iscxurl] | ~110k, 5 classes | Alexa-derived crawl | no | source-per-class; our audit: benign from ≈300 sites, deep paths |
| PhishStorm [marchal2014phishstorm] | 96,018 balanced | DMOZ | no | homepage-heavy benign (paper); ours: 70 % `www.` benign vs 35 % phish |
| Ebbu2017 [sahingoz2019machine] | 73,575 | Yandex search results | no | many duplicates (ours: 26 % removed) |
| Hannousse 2021 [hannousse2021benchmark] | 11,430 balanced | Alexa crawl *with paths* | no (May 2020) | small, balanced |
| PhiUSIIL [prasad2024phiusiil] | 235,795 | — | no | ours: 100 % of benign are `https://www.<domain>` homepages |
| GramBeddings [bozkir2023grambeddings] | 800k balanced | top sites crawl | collection window 2019–21 | access by form (not obtained) |
| PILU-90K [sanchezpaniagua2022phishing] | 90k incl. 30k login URLs | Quantcast | no | not obtained in this study |
| DEPHIDES [sahingoz2024dephides] | 5.1 M | ≈30 URLs per top domain | no | random splits leak domains |
| Kaggle sid321axn [siddhartha2021maliciousurls] | 651,191, 4 classes | aggregated | no | mixed sources; scheme often absent |
| PhreshPhish [dalton2025phreshphish‡] | large, HTML+URL | browser crawl | temporal split | not used (HTML-centred) |
| Feeds: PhishTank, OpenPhish, URLhaus [phishtank, openphish, urlhaus]; Tranco [lepochat2019tranco]; Common Crawl [commoncrawl] | live | — | PhishTank/URLhaus yes | positive-only (feeds) or not labels (lists) |

## 12. Synthesis: what is established, what is not

**Established by prior work.**
1. Lexical URL features and simple tree ensembles reach very high in-distribution scores on public benchmarks.
2. Cross-dataset performance of URL classifiers collapses, often to near chance (A: [ma2009beyond, mia2024featurestrust, rashid2024domainadapt, henry2026ensembletransfer, liu2024transurl]).
3. Benign-class sampling from popularity lists produces biased, homepage-heavy benign data (A: [sabir2022reliability, hannousse2021benchmark, marchal2018designing, elaassal2020benchmarking, sanchezpaniagua2022phishing]).
4. Random splits, balanced classes and accuracy over-state deployability; temporal and low-FPR evaluation is needed (A: [arp2022dosdonts, pendlebury2019tesseract, marchal2018designing, maneriker2021urltran]).
5. URL detectors are fragile to cheap adversarial manipulation (A: [sabir2022reliability, apruzzese2022spacephish]).

**Not established (gaps; developed in `RESEARCH_GAPS.md`).**
- (I) A *quantified, multi-corpus, raw-URL* account of which specific recording artifacts carry in-distribution performance, whether their direction is consistent across corpora, and how much registered-domain memorisation adds. Prior cross-dataset studies used pre-computed feature tables [mia2024featurestrust, henry2026ensembletransfer] or abstracts do not report the mechanism [rashid2024domainadapt]; the only direct treatment is a non-peer-reviewed single-model preprint [giri2026shieldphish].
- (I) Whether removing artifacts at the *feature* level suffices, versus canonicalising the input, and whether either restores external performance.
- (A for malware, I for URLs) Calibration and threshold transfer of phishing-URL classifiers under dataset shift [li2021malwarecalibration].
- (I) Sensitivity of URL classifiers to label-irrelevant recording variants (scheme/`www.`/port/fragment), as distinct from adversarial perturbations.
- (A) Public URL corpora lack timestamps; long-horizon temporal evaluation of URL models on public data is missing [pendlebury2019tesseract].

## 13. How this project differs

| Closest work | What it does | What we add |
|---|---|---|
| [mia2024featurestrust] | 2 datasets, pre-computed features, random splits, SHAP | raw URLs from 6 corpora + 3 positive-only feeds; ablation of named artifacts; grouped splits; probe; calibration |
| [rashid2024domainadapt] | domain adaptation between 3 datasets | mechanism (artifact direction) rather than adaptation |
| [giri2026shieldphish] ‡ | one model, canonicalisation, external benign set | multi-model, multi-seed, paired statistics, 6-way leave-one-corpus-out, probe, calibration, temporal recall |
| [sanchezpaniagua2022phishing] | homepage vs login benign shortcut; 2016→2020 decay | generalises the shortcut analysis across corpora and recording formats |
| [bhuiyan2026fragility] | probe + artifact ablation for e-mail | same diagnostic design for URLs |
| [khan2026stacking], [sankaranarayanan2024ensemble] | stacking on one Kaggle set, random split | shows why such results do not transfer |
