### alam2026philter
C: Mahbub Alam, Muhammad Lutfor Rahman, Sonjoy Kumar Paul, Amy W. Hays, Aftab Hussain, Md Imanul Huq, Nitesh Saxena (2026). SoK: PHILTER: Uncovering Security and Functional Gaps in AI-based Phishing Website Detection Literature via an LLM-based Reasoning Framewor
M: LLM-assisted extraction plus expert validation against four functionality metrics (incl. F3 robustness on diverse benign pages, F4 evaluation transparency under class imbalance) and three security metrics (S1 adaptation to concept drift via temporally disjoint evaluation, S2 resistance to active attackers, S3 privacy)
D: 55 academic AI-based phishing-website detection approaches assessed
E: Rubric scoring of each paper; taxonomy of detection strategies
R: No study fulfils all requirements; most risk elevated false alarms due to limited testing on diverse benign pages (long-tail/low-rank domains); many assume static tactics (abstract, Sec. 4-5).
F: Accuracy-driven evaluation hides blind spots: insufficient benign diversity, no temporally disjoint testing, metrics unsuited to class imbalance (recommends AUC-PR, MCC, class-specific metrics).
L: **Authors' stated:** LLM extraction validated by experts but still subjective; website-level focus. **Our caveats:** Prepublication version; URL-only works are a subset of the 55.
G: Same rubric applied specifically to URL-only detectors.

### aleroud2020gan
C: Ahmed AlEroud; George Karabatis (2020). *Bypassing Detection of URL-based Phishing Attacks Using Generative Adversarial Deep Neural Networks*. Proceedings of the Sixth International Workshop on Security and Privacy Analytics (IWSPA '20), pp. 53-60. DOI: 10.114
M: Train a GAN on phishing URLs; feed generated URLs to ML detectors (including PhishStorm-style intra-URL similarity features).
D: Not detailed in abstract.
E: Evasion rate against simple and advanced detectors
R: Abstract: the approach 'fooled both simple and advanced detection models' (no numbers in abstract).
F: GAN-generated URLs evade detectors.
L: - Authors' stated limitations: n/a (abstract only). - My assessment: Generated URLs may be unregistrable/unrealistic; unclear labels.
G: Realism constraints on generated adversarial URLs.

### alexa2022retirement
C: Amazon (Alexa Internet) (2022). *Alexa.com Top Sites retirement (1 May 2022)*. Alexa.com end-of-service notice; press coverage. URL: https://www.alexa.com/minisiteinfo/
M: n/a
D: n/a
E: n/a
R: n/a
F: Alexa top-1M, the benign source of ISCX-URL-2016 and many phishing datasets, is no longer maintained; snapshots are frozen as of 2022.
L: - Authors' stated limitations: n/a - My assessment: n/a
G: n/a

### alfayoumi2024xaiphd
C: Mustafa Al-Fayoumi; Bushra Alhijawi; Qasem Abu Al-Haija; Rakan Armoush (2024). *XAI-PhD: Fortifying Trust of Phishing URL Detection Empowered by Shapley Additive Explanations*. International Journal of Online and Biomedical Engineering (iJOE) 20(11):80-101. DO
M: Compute SHAP values, retain most influential features, train a lightweight gradient boosting classifier.
D: Not specified in the abstract (full text not retrieved).
E: Hold-out classification; accuracy, F1, per-record prediction time
R: Abstract reports 99.8% accuracy and 99% F1 and 'very low' per-record prediction time (abstract only; tables not seen).
F: SHAP-driven feature pruning keeps accuracy while reducing cost.
L: - Authors' stated limitations: Not available (abstract only). - My assessment: Venue is low-tier; 99.8% accuracy suggests possible leakage/within-dataset optimism; no external test.
G: No robustness or calibration analysis; no cross-dataset validation.

### ali2025phishurldetect
C: Ali, Irshad; Subba, Basant (2025). *PhishURLDetect: A parameter efficient fine-tuning of LLMs using LoRA for detection of phishing URLs*. Proceedings of the 26th International Conference on Distributed Computing and Networking (ICDCN 2025), pp. 278-279. DOI: 1
M: LoRA adapters on RoBERTa/GPT-2.
D: Proprietary corpus of 573,880 phishing + benign URLs (abstract)
E: Not in abstract
R: 99.86% accuracy (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: LoRA matches full fine-tuning at a fraction of parameters.
L: - Stated by authors: Not available. - Our own caveats: 2-page poster; proprietary data; accuracy-only reporting.
G: Public evaluation.

### aljofey2020effective
C: Aljofey, Ali; Jiang, Qingshan; Qu, Qiang; Huang, Mingqing; Niyigena, Jean-Pierre (2020). *An Effective Phishing Detection Model Based on Character Level Convolutional Neural Network from URL*. Electronics, 9(9), 1514. DOI: 10.3390/electronics9091514 URL: https
M: Char-CNN (embedding + conv + pooling); baselines include RF/LR/NB/MNB with hand-crafted features across URL/host/path/file/query parts.
D: D1: 318,642 URLs (Alexa, OpenPhish, Spamhaus, techhelplist, SANS ISC, PhishTank); D2 Ebbu2017 (Yandex/PhishTank); D3, D4 benchmark sets (Common Crawl+Alexa vs PhishTank) (Sec. 4.1)
E: Random splits per dataset; five experiments; metrics accuracy/precision/recall/F1/AUC/time
R: Accuracy 95.02% on D1; 98.58%, 95.46%, 95.22% on D2-D4 (abstract, Sec. 5); common prefixes 'http://', 'https://', 'www.' are removed before modelling (Sec. 4.1, Table 3). (Numbers taken from the full text; section/table references given where identified.)
F: Char-CNN outperforms classical ML with hand-crafted or TF-IDF features; URL-length distributions differ by class (Fig. 10).
L: - Stated by authors: Cannot handle shortened URLs; may misclassify unusual legitimate URLs (Sec. 6). - Our own caveats: Explicitly removes scheme/www prefixes - evidence that authors recognised these as artifacts; no cross-dataset transfer reported.
G: Cross-dataset generalisation and artifact quantification.

### aljofey2022effective
C: Ali Aljofey, Qingshan Jiang, Abdur Rasool, Hui Chen, Wenyin Liu, Qiang Qu, Yang Wang (2022). An effective detection approach for phishing websites using URL and HTML features. *Scientific Reports*, art. 8842. DOI: 10.1038/s41598-022-10841-5
M: XGBoost on URL character sequences, hyperlink features and TF-IDF of noisy HTML/plaintext
D: Self-built dataset of 60,252 webpages (32,972 benign, 27,280 phishing) plus a benchmark dataset for external validation
E: Evaluation on own dataset and on a second benchmark dataset (cross-dataset check)
R: 96.76% accuracy with 1.39% FPR on own data; 98.48% accuracy with 2.09% FPR on the benchmark dataset (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Reports that a model built for zero-hour detection transfers to a second dataset; one of the few mainstream papers to include an external dataset.
L: **Authors' stated:** Lack of large public datasets motivated self-collection. **Our caveats:** Content-heavy; cross-dataset result involves retraining on the benchmark rather than a frozen-model transfer (verify in full text before citing as generalisation).
G: Frozen-model external validation is still rare.

### alshingiti2023deep
C: Alshingiti, Zainab; Alaqel, Rabeah; Al-Muhtadi, Jalal; Haq, Qazi Emad Ul; Saleem, Kashif; Faheem, Muhammad Hamza (2023). *A Deep Learning-Based Phishing Detection System Using CNN, LSTM, and LSTM-CNN*. Electronics, 12(1), 232. DOI: 10.3390/electronics12010232 
M: Applies 1D-CNN, LSTM and stacked LSTM-CNN to tabular URL features.
D: Pre-extracted feature dataset of 20,000 URLs (9,800 phishing) with 80 features, reduced to 30 via SelectKBest (Sec. 3.2)
E: 80/20 random split (Sec. 3.2)
R: Accuracy 99.2% (CNN), 97.6% (LSTM-CNN), 96.8% (LSTM) (abstract; Sec. 4). (Numbers taken from the full text; section/table references given where identified.)
F: CNN on tabular features best.
L: - Stated by authors: Small dataset. - Our own caveats: Despite the title it is not character-level; 20k pre-featurised samples; random split - results not comparable to raw-URL models.
G: Raw-URL evaluation.

### apruzzese2022spacephish
C: Giovanni Apruzzese, Mauro Conti, Ying Yuan (2022). SpacePhish: The Evasion-space of Adversarial Attacks against Phishing Website Detectors using Machine Learning. *Proceedings of the 38th Annual Computer Security Applications Conference (ACSAC 2022)*, pp. 171-
M: Formalises the 'evasion-space' (problem-space vs feature-space perturbations) and a realistic threat model; evaluates 12 cheap evasion attacks
D: Two public phishing website datasets (Zenodo and delta-phish style collections; see Sec. 5 of PDF), 18 ML-PWD configurations
E: Statistical significance testing of detection-rate degradation across 18 detectors and 12 attacks, repeated trials
R: Realistic cheap evasions induce a statistically significant 3-10% degradation; combined problem+feature-space perturbations can drop detection rate from 0.95 to 0 (extended version abstract).
F: Even trivial, cheap URL/HTML manipulations measurably reduce detection; some detectors are immune to some attacks, so robustness must be measured per feature set.
L: **Authors' stated:** Only two datasets; attacks are heuristic. **Our caveats:** The URL-feature detectors' sensitivity to small lexical perturbations is the same vulnerability our scheme/www artefact exposes.
G: Joint analysis of artefact reliance and evasion susceptibility.

### apruzzese2023pragmatic
C: Giovanni Apruzzese, Pavel Laskov, Johannes Schneider (2023). SoK: Pragmatic Assessment of Machine Learning for Network Intrusion Detection. *2023 IEEE 8th European Symposium on Security and Privacy (EuroS&P)*, pp. 592-614. DOI: 10.1109/EuroSP57164.2023.00042; 
M: Defines 'pragmatic assessment': report what practitioners need (hardware, data pre-processing, costs, multiple datasets, statistical variance over many trials); hundreds of thousands of model runs to quantify variance
D: Systematisation of NID papers plus large experimental campaign on public NID datasets (Sec. 5-6) and a practitioner survey
E: Multiple random seeds/splits, multiple datasets, reporting of runtime and resources; shows how single-split results mislead
R: Demonstrates run-to-run variance large enough to change rankings of methods (Sec. 6, full text).
F: Single-dataset, single-run evaluations are unreliable; cross-dataset and repeated-trial reporting should be standard.
L: **Authors' stated:** NID-specific datasets. **Our caveats:** The methodology (repeat trials, cross-dataset, cost reporting) transfers directly to URL classification.
G: Pragmatic assessment has not been applied to phishing URL detectors.

### apruzzese2023realattackers
C: Giovanni Apruzzese, Hyrum S. Anderson, Savino Dambra, David Freeman, Fabio Pierazzi, Kevin A. Roundy (2023). "Real Attackers Don't Compute Gradients": Bridging the Gap Between Adversarial ML Research and Practice. *2023 IEEE Conference on Secure and Trustworth
M: Position paper contrasting research threat models with operational reality; case study (b) reports lack of evidence of gradient-based adversarial examples against a commercial phishing detector
D: Three industrial case studies (an online social network ML system; a commercial ML phishing-webpage detector; an ML evasion competition) plus analysis of recent adversarial-ML papers
E: Qualitative; literature analysis
R: No benchmark numbers; the phishing case study is qualitative (Sec. III).
F: Operational ML security problems are dominated by data drift, cheap problem-space manipulations and pipeline effects rather than gradient attacks; evaluation should reflect realistic attacker economics.
L: **Authors' stated:** Case studies are anecdotal by design. **Our caveats:** Useful for scoping our robustness analysis toward cheap URL manipulations (scheme/www changes, path padding) rather than gradient attacks.
G: Realistic, cheap perturbation benchmarks for URL detectors.

### arp2022dosdonts
C: Daniel Arp, Erwin Quiring, Feargus Pendlebury, Alexander Warnecke, Fabio Pierazzi, Christian Wressnegger, Lorenzo Cavallaro, Konrad Rieck (2022). Dos and Don'ts of Machine Learning in Computer Security. *31st USENIX Security Symposium (USENIX Security 22)*, pp
M: Taxonomy of ten pitfalls: P1 sampling bias, P2 label inaccuracy, P3 data snooping, P4 spurious correlations, P5 biased parameter selection, P6 inappropriate baseline, P7 inappropriate performance measures, P8 base rate fallacy, P9 lab-only evaluation, P10 inappropriate threat model; prevalence survey and author feedback
D: Literature study of 30 top-tier security papers (2010-2020) plus four impact case studies (mobile malware, vulnerability discovery, source-code authorship, network intrusion detection)
E: Prevalence analysis across 30 papers; controlled experiments showing each pitfall's inflation effect
R: Each pitfall is present in a majority of surveyed papers (e.g., sampling bias and data snooping are marked present in most; see Fig. 2/Table 1). Base-rate example: a 1% FPR at a 1:100 ratio yields roughly one false alarm per true positive (Sec. 2, P8).
F: Spurious correlations ('artifacts unrelated to the security problem create shortcut patterns for separating classes') and sampling bias are endemic; recommends explanation-based artefact checks, temporal splits, realistic base rates and precision/recall reporting.
L: **Authors' stated:** Survey limited to top venues and 30 papers; pitfall boundaries overlap. **Our caveats:** Does not include a phishing-URL case study, but P1/P4/P8 map one-to-one to our situation.
G: A phishing-URL instantiation of the pitfall analysis with concrete artefact ablations.

### axelsson2000baserate
C: Stefan Axelsson (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*. DOI: 10.1145/357830.357849
M: Bayesian analysis of detector alarms under low attack prevalence
D: Analytical; no dataset
E: Shows that with realistic base rates the false-alarm rate dominates the Bayesian detection rate (positive predictive value)
R: Classic result: to achieve a useful PPV at low prevalence the FPR must be on the order of 1e-5 (Sec. 4-5 of original). (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Accuracy/TPR on balanced data say little about operational usefulness; precision collapses at low prevalence.
L: **Authors' stated:** Intrusion-detection framing. **Our caveats:** Prevalence of phishing among URLs a user visits is far below 50%, so our balanced-set precision is not meaningful operationally.
G: Base-rate-adjusted reporting is still rare in phishing-URL papers.

### bahnsen2017classifying
C: Correa Bahnsen, Alejandro; Contreras Bohorquez, Eduardo; Villegas, Sergio; Vargas, Javier; Gonzalez, Fabio A. (2017). *Classifying phishing URLs using recurrent neural networks*. 2017 APWG Symposium on Electronic Crime Research (eCrime), pp. 1-8. DOI: 10.1109/
M: RF on lexical/statistical features (incl. KS/KL statistics, Alexa rank flag); LSTM over character sequences with sigmoid output.
D: 2,000,000 URLs: 1M phishing from PhishTank + 1M benign from Common Crawl (Sec. IV)
E: 3-fold cross-validation; learning-curve experiment on 200k held-out URLs (Sec. V)
R: RF accuracy 93.47% (recall 93.28%, precision 93.63%, AUC 98.44%); LSTM accuracy 98.76% (std 0.03%), F1 0.98 vs 0.93 (Sec. V, Tables II-III, Fig. 8); throughput 942 URLs/s (RF) vs 281 (LSTM). (Numbers taken from the full text; section/table references given where identified.)
F: Char-LSTM beats RF by about 5 points without feature engineering, at a throughput cost.
L: - Stated by authors: LSTM slower to train/evaluate. - Our own caveats: Benign = Common Crawl pages vs PhishTank; random CV means same campaigns/domains appear in train and test (likely inflated).
G: Domain-grouped evaluation.

### bahnsen2017rnnurl
C: Alejandro Correa Bahnsen; Eduardo Contreras Bohorquez; Sergio Villegas; Javier Vargas; Fabio A. Gonzalez (2017). *Classifying phishing URLs using recurrent neural networks*. 2017 APWG Symposium on Electronic Crime Research (eCrime). DOI: 10.1109/ecrime.2017.79
M: Compare engineered lexical features + RF against character LSTM reading the URL string.
D: 2,000,000 URLs: 1M PhishTank phishing, 1M Common Crawl benign (paper Sec. IV); collection period not stated; no license.
E: 3-fold cross-validation; accuracy; learning curves with 200k test URLs
R: LSTM accuracy 98.7%, 'beating by 5%' the RF (abstract; Table II in paper).
F: Character RNN outperforms hand-crafted features at scale.
L: - Authors' stated limitations: No evaluation on temporal splits. - My assessment: Alexa membership feature leaks list-based priors; PhishTank/Common Crawl distribution gap makes task easy.
G: Robustness and interpretability of the RNN not studied (motivating DeepPhish follow-up).

### bahnsen2018deepphish
C: Alejandro Correa Bahnsen; Ivan Torroledo; Luis David Camacho; Sergio Villegas (2018). *DeepPhish: Simulating Malicious AI*. Black Hat Europe 2018 (talk, 5 Dec 2018, slides); also presented at DEF CON 26 AI Village. URL: https://i.blackhat.com/eu-18/Wed-Dec-5/e
M: Cluster PhishTank URLs by threat actor, train LSTM per actor on URLs that bypassed the detector, generate new URLs, measure evasion.
D: PhishTank-derived; sizes on slides.
E: Attack 'effectiveness' = fraction of generated URLs classified benign
R: Press/DEF CON summaries report attack effectiveness rising from 0.69% to 20.9% and 4.91% to 36.28% for two actors (secondary sources; slide numbers not re-verified here).
F: Generative evasion is feasible against character-level URL detectors.
L: - Authors' stated limitations: Not peer reviewed. - My assessment: No code/dataset release; vendor talk; numbers hard to reproduce.
G: Need reproducible, open mutation benchmarks instead of vendor demonstrations.

### barbero2022transcending
C: Federico Barbero, Feargus Pendlebury, Fabio Pierazzi, Lorenzo Cavallaro (2022). Transcending TRANSCEND: Revisiting Malware Classification in the Presence of Concept Drift. *2022 IEEE Symposium on Security and Privacy (S&P)*. DOI: 10.1109/SP46214.2022.9833659; 
M: TRANSCENDENT: formal treatment of conformal evaluation; two new conformal evaluators (inductive, cross-conformal) that are cheaper than the original transductive one; classification-with-rejection under drift
D: Android malware over time (AndroZoo-derived, time-stamped) and other drift settings (Sec. VI)
E: Time-aware train/test with rejection; compares rejection quality against baselines (probability thresholds, etc.)
R: Reported rejection-vs-performance curves show TRANSCENDENT outperforms the original Transcend and probability-based rejection (Sec. VII; full text).
F: Rejection via conformal evaluation is a principled, efficient way to cope with drift; naive softmax/probability thresholds are weaker.
L: **Authors' stated:** Requires periodic calibration; cost of rejected samples must be absorbed by analysts. **Our caveats:** Benefit for lightweight URL models is untested.
G: Conformal rejection for URL classifiers remains open.

### bhuiyan2026fragility
C: Istiaque Bhuiyan, Tanvir Bhuiyan (2026). The Fragility of Phishing Detection Models: Evidence from Cross-Corpus Transfer, Prevalence Shift, Artifact Learning, and Evasion Risk. *Big Data and Cognitive Computing*, art. 211. DOI: 10.3390/bdcc10070211
M: TF-IDF logistic regression and linear SVC; pooled baseline, single-corpus cross-dataset transfer, leave-one-corpus-out, prevalence-shift simulation, training-prevalence manipulation, dataset-identification probe, top-feature inspection, artifact-removal ablation, feature-sensitivity masking
D: Six public phishing/spam email corpora: CEAS_08, Enron, Ling, Nazario, Nigerian Fraud, SpamAssassin
E: Cross-corpus and leave-one-out; prevalence shift with fixed thresholds vs alert budgets; artefact ablations
R: Leave-one-corpus-out F1 0.8201-0.8994 (LR) and 0.7607-0.8910 (SVC); dataset-identification accuracy 0.9722 (LR) / 0.9806 (SVC), i.e., corpus identity is highly learnable (abstract).
F: Models partly learn corpus markers (date tokens, headers, URL/domain terms) rather than phishing semantics; prevalence shift failure is asymmetric and threshold dependent; recommends cross-corpus validation, prevalence-aware thresholding and artefact tests.
L: **Authors' stated:** Linear models only; email modality. **Our caveats:** Email, not URL; but the 'dataset-identification probe' and artefact-removal ablation design transfer directly to URL features.
G: Same protocol for URL datasets.

### blum2010lexical
C: Blum, Aaron; Wardman, Brad; Solorio, Thamar; Warner, Gary (2010). *Lexical feature based phishing URL detection using online learning*. Proceedings of the 3rd ACM Workshop on Artificial Intelligence and Security (AISec '10), pp. 54-60. DOI: 10.1145/1866423.186
M: Lexical bag-of-tokens features (host/path/binary indicators) fed to a confidence-weighted (CW) online classifier so the model adapts as new phishing campaigns appear.
D: UAB phishing URLs and benign URLs (sizes not in abstract)
E: Not stated in abstract
R: Not in abstract (often cited as about 97% accuracy; unverified here). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Lexical-only online learning is viable for zero-hour phishing detection.
L: - Stated by authors: Not available. - Our own caveats: Small, non-public dataset; no cross-dataset test.
G: Reproducibility; feature drift analysis.

### botacin2021pitfalls
C: Marcus Botacin, Fabricio Ceschin, Ruimin Sun, Daniela Oliveira, André Grégio (2021). Challenges and pitfalls in malware research. *Computers & Security*, art. 102287. DOI: 10.1016/j.cose.2021.102287
M: Literature review identifying 20 pitfalls (threat model, closed datasets, ground truth from closed-source AV, etc.)
D: Systematic review of 491 malware papers (2000-2018)
E: N/A
R: 20 pitfalls identified across 491 papers (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Dataset and ground-truth practices (private datasets, AV-label ground truth, non-deterministic analysis) limit validity and reproducibility.
L: **Authors' stated:** Malware focus; through 2018. **Our caveats:** Secondary relevance; complements Arp et al. with reproducibility pitfalls.
G: N/A

### bozkir2023grambeddings
C: Bozkir, Ahmet Selman; Dalgic, Firat Coskun; Aydos, Murat (2023). *GramBeddings: A New Neural Network for URL Based Identification of Phishing Web Pages Through N-gram Embeddings*. Computers & Security, 124, 102964. DOI: 10.1016/j.cose.2022.102964 URL: https://
M: Three n-gram granularities embedded in parallel; each channel CNN -> LSTM -> attention; concatenated for classification.
D: GramBeddings dataset (public via request form): 800,000 URLs, 400K phishing + 400K legitimate (custom crawler), collected May 2019-June 2021 (dataset page; TransURL Sec. 3)
E: Not retrieved (publisher blocked)
R: Not retrieved from the paper (TransURL Fig. 5 reproduces GramBeddings results on its dataset). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Multi-granular n-gram embeddings with attention are competitive; dataset spans 2+ years with weekly collection to reduce duplicates.
L: - Stated by authors: Not retrieved. - Our own caveats: Legitimate URLs crawled from top sites; dataset access via form.
G: Cross-dataset tests appear only in follow-up work (TransURL).

### chen2023continuous
C: Yizheng Chen, Zhoujie Ding, David Wagner (2023). Continuous Learning for Android Malware Detection. *32nd USENIX Security Symposium (USENIX Security 23)*, pp. 1127-1144. arXiv: 2302.04332
M: Hierarchical contrastive learning plus a new active-learning sample-selection strategy to maintain a drifting classifier with limited analyst labels
D: Android apps over a 7-year period (AndroZoo-based, time-stamped)
E: Train on one year, deploy over subsequent months/years with a monthly labelling budget; compares against prior active-learning baselines
R: F1 of a static classifier drops from 0.99 to 0.76 after six months on new samples (Sec. 1); proposed method lowers FNR from 14% to 9% and FPR from 0.86% to 0.48% versus prior active learning (abstract/Sec. 1).
F: Even strong classifiers decay fast under drift; the choice of which new samples to label matters as much as the model.
L: **Authors' stated:** Relies on timely analyst labels; Android-only. **Our caveats:** Transferring to URLs needs a time-stamped phishing feed; our dataset has none.
G: No equivalent labelling-budget study for phishing URLs.

### chen2026memophishagent
C: Chen, Xuan; Liu, Hao; Yuan, Tao; Kafai, Mehran; Habas, Piotr; Zhang, Xiangyu (2026). *MemoPhishAgent: Memory-Augmented Multi-Modal LLM Agent for Phishing URL Detection*. arXiv preprint arXiv:2602.21394 (v3; arXiv comment states ACL 2026 Industry Track camera-r
M: Tool-using agent (page crawl, screenshot, memory retrieval) with episodic memory; ablations of tools/memory.
D: TR-OP (5,000 phishing + 5,000 benign, Jul-Dec 2023), DynaPD, and new SocPhish (2,765 URLs: 516 phishing, 2,249 benign from five social platforms) (Sec. 4, Table 6)
E: Held-out evaluation on public sets plus real-world SocPhish; production deployment (about 60k URLs/week); prompt-injection robustness test
R: Recall +13.6% over SOTA on public sets, +20% on SocPhish; production 91.44% recall, 90.34% F1 (abstract; Tables 1, 5); 1.07 s/URL latency. (Numbers taken from the full text; section/table references given where identified.)
F: Agentic multimodal reasoning improves recall on novel threats; URL-only URLTran degrades on real-world social-media URLs.
L: - Stated by authors: Latency/cost; prompt-injection sensitivity (Appendix A.3). - Our own caveats: Not URL-only; heavy; included to bound the design space.
G: n/a

### chiew2019hybrid
C: Chiew, Kang Leng; Tan, Choon Lin; Wong, KokSheik; Yong, Kelvin S. C.; Tiong, Wei King (2019). *A new hybrid ensemble feature selection framework for machine learning-based phishing detection system*. Information Sciences, 484, pp. 153-166. DOI: 10.1016/j.ins.2
M: Two-phase ensemble feature selection; evaluates with RF, SVM, NB, C4.5, JRip, PART.
D: Authors' dataset with 48 features (URL + HTML) and the UCI phishing-websites dataset
E: Not in abstract
R: 94.6% accuracy with RF using 20.8% of features (10 of 48) (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Small feature subsets with RF outperform full feature sets with other learners.
L: - Stated by authors: Not available. - Our own caveats: Includes HTML features, so not URL-only; UCI dataset is pre-extracted and dated.
G: Feature-selection stability across datasets.

### commoncrawl
C: Common Crawl Foundation (2026). *Common Crawl web corpus and URL index (benign URL source)*. https://commoncrawl.org/overview. URL: https://commoncrawl.org/overview
M: n/a
D: Download: s3://commoncrawl/ (free), URL index https://index.commoncrawl.org/ . License: Common Crawl Terms of Use (crawl data free for use; respect source copyrights). Timestamps: YES (crawl ID and fetch time per record). Labels: none - 'benign' is an assumption; crawls contain malicious pages. Known problems: used as benign in Bahnsen 2017, GramBeddings-style corpora, Mendeley/IEEE DataPort sets; benign label unveri
E: n/a
R: n/a
F: n/a
L: - Authors' stated limitations: n/a - My assessment: Benign-by-assumption; needs screening (e.g. Google Safe Browsing/VirusTotal) as PhiShark-style papers do.
G: n/a

### dalton2025phreshphish
C: Thomas Dalton, Hemanth Gowda, Girish Rao, Sachin Pargi, Alireza Hadj Khodabakhshi, Joseph Rombs, Stephan Jou, Manish Marwah (2025). PhreshPhish: A Real-World, High-Quality, Large-Scale Phishing Website Dataset and Benchmark. *arXiv preprint*. arXiv: 2507.10854
M: Dataset construction pipeline: temporal train/test split, pruning of near-duplicate test points via locality-sensitive hashing, diversity/difficulty filters, base-rate adjustment; baseline models
D: New large phishing-website dataset (HTML+URL) crawled with a real browser, quality-checked by heuristics and human annotation; hosted on Hugging Face; benchmark subsets at base rates from 0.05% to 5%
E: Temporal split + leakage pruning + five base rates; precision reported as a function of recall, FPR and base rate
R: Benchmarks span base rates 0.05%-5%; states existing public datasets 'suffer from leakage and unrealistic base rates, leading to overly optimistic performance results' (Sec. 1); baseline tables in Sec. 6.
F: Train/test leakage (same kit/template, near-duplicate pages) and balanced base rates inflate published results; realistic benchmarks need temporal splits, near-duplicate pruning and low prevalence.
L: **Authors' stated:** Preprint; industrial collection pipeline not fully reproducible; HTML-centric. **Our caveats:** URL-only baselines are secondary; still the most explicit public treatment of leakage + base rate for phishing benchmarks.
G: A URL-only benchmark with the same leakage/base-rate discipline.

### dambra2023decoding
C: Savino Dambra, Yufei Han, Simone Aonzo, Platon Kotzias, Antonino Vitale, Juan Caballero, Davide Balzarotti, Leyla Bilge (2023). Decoding the Secrets of Machine Learning in Malware Classification: A Deep Dive into Datasets, Feature Extraction, and Model Perform
M: Controlled study of how dataset composition (families, samples per family, benign/malware balance), feature type and classifier drive reported performance
D: 67k Windows PE samples from 670 families (100 each) plus benign set; static and dynamic features
E: Varies dataset properties systematically; family-aware splits
R: Shows performance strongly tied to dataset nature/distribution (Sec. 5-6).
F: Near-perfect numbers in prior work are tied to dataset construction choices; family-level grouping and composition matter.
L: **Authors' stated:** Windows PE only. **Our caveats:** Analogue: family-aware splits in malware correspond to registered-domain/campaign-grouped splits for URLs.
G: Equivalent composition study for URL datasets.

### das2020sokphishing
C: Avisha Das, Shahryar Baki, Ayman El Aassal, Rakesh Verma, Arthur Dunbar (2020). SoK: A Comprehensive Reexamination of Phishing Research From the Security Perspective. *IEEE Communications Surveys & Tutorials*. DOI: 10.1109/COMST.2019.2957750; arXiv: 1911.00953
M: Critical survey with dataset-property, feature, algorithm and metric analysis
D: Systematisation of phishing detection literature (email, website, URL) against four 'security challenges': real-time detection, active attacker, dataset quality, base-rate fallacy
E: Reviews evaluation practice and finds: use of balanced datasets and inappropriate metrics, unreported timings, lack of generalisation studies
R: Qualitative; tables of dataset sizes/ratios per paper (Sec. V-VII).
F: Base-rate fallacy, active attacker, dataset diversity and generalisation studies 'are rarely mentioned, let alone emphasized' in prior surveys and papers.
L: **Authors' stated:** Coverage through 2019. **Our caveats:** None substantial.
G: Empirical generalisation studies for URL detectors (which later Mia 2024 / Rashid 2024 begin to provide).

### do2022deeplearning
C: Nguyet Quang Do, Ali Selamat, Ondrej Krejcar, Enrique Herrera-Viedma, Hamido Fujita (2022). Deep Learning for Phishing Detection: Taxonomy, Current Challenges and Future Directions. *IEEE Access*, pp. 36429-36463. DOI: 10.1109/ACCESS.2022.3151903
M: Taxonomy of DL approaches; analysis of datasets, features, metrics, challenges
D: Systematic review of DL phishing-detection papers
E: Reports that many works train on old, non-diverse or highly imbalanced data and use accuracy on imbalanced sets
R: Qualitative; states that 'datasets comprising of old phishing attacks do not represent real attack scenarios', that accuracy/error rate are unsuitable for imbalanced data, and that batch learning adapts poorly to concept drift (Sec. VI-VII).
F: Dataset recency/diversity/imbalance and metric choice are listed as open challenges; recommends online learning for drift.
L: **Authors' stated:** Review scope; recommends a 'recent and balanced dataset', which conflicts with base-rate advice. **Our caveats:** Their 'balanced dataset' recommendation illustrates the field's inconsistency on class ratios.
G: Clear guidance on realistic prevalence in evaluation.

### ejaz2023lifelong
C: Asif Ejaz, Adnan Noor Mian, Sanaullah Manzoor (2023). Life-long phishing attack detection using continual learning. *Scientific Reports*, art. 11488. DOI: 10.1038/s41598-023-37552-9
M: Continual-learning (CL) algorithms on a vanilla neural network over FastText embeddings of HTML content, compared with static training and transfer learning
D: Self-collected phishing and benign web pages for 2018, 2019, 2020, split into six temporally ordered datasets
E: Train on earlier period, test on later periods; measures deterioration over time
R: CL keeps accuracy over time with 2.45% deterioration, versus 20.65% (static VNN) and 8% (transfer learning) (abstract).
F: A static phishing classifier loses over 20 percentage points across three years; incremental adaptation reduces but does not eliminate the loss.
L: **Authors' stated:** HTML-based, relatively small yearly samples; CL hyper-parameters. **Our caveats:** Content-based, not URL-based; still one of the few phishing papers with a genuine temporal split.
G: Equivalent temporal study for lexical URL models.

### elaassal2020benchmarking
C: Ayman El Aassal, Shahryar Baki, Avisha Das, Rakesh M. Verma (2020). An In-Depth Benchmarking and Evaluation of Phishing Detection Research for Security Needs. *IEEE Access*, pp. 22170-22192. DOI: 10.1109/ACCESS.2020.2969780
M: PhishBench benchmarking framework; systematic feature taxonomies for URLs, websites, emails; evaluation of published methods under varying imbalance and dataset size; feature-importance and extraction-time analysis
D: New URL, website and email datasets with varying legitimate:phishing ratios; legitimate URLs from diverse sources rather than Alexa domain lists
E: Balanced vs imbalanced ratios, scaling experiments, retraining on new attacks
R: Shows that increasing legitimate:phishing ratio degrades the performance of published methods and that 'retraining alone is not enough to defeat new attacks' (abstract; Sec. VII tables).
F: Explicitly criticises prior work for using balanced datasets and Alexa domain-only legitimate sets; argues for imbalance-aware evaluation, proper metrics and representative datasets.
L: **Authors' stated:** Feature reproduction of prior work is approximate. **Our caveats:** 2020-era datasets; still no domain-grouped splitting.
G: Combining imbalance-aware benchmarking with temporal and domain-grouped splits.

### fernando2026driftphish
C: Warren Fernando, Nikos Komninos (2026). Evaluating and Combating the Impact of Concept Drift on the Performance of Machine Learning-Based Phishing Detection Systems. *arXiv preprint*. arXiv: 2606.11471
M: Statistical framework (adapted from the FeSAD ransomware drift framework) to quantify similarity of phishing vs benign samples and flag drifted samples; feature-robustness analysis across time
D: Public phishing/spam email corpora (the paper is email-centric, not URL-centric; see PDF Sec. 2-4)
E: Temporal evaluation across dataset periods with drift scoring
R: Full text available, but headline numbers are not summarised in the abstract; treat quantitative claims cautiously (preprint).
F: Argues that phishing detectors degrade with evolution of attacks and that a drift score can be used to decide re-training.
L: **Authors' stated:** Preprint; limited datasets. **Our caveats:** Email modality; relevance to URL lexical models is indirect. Included to show that 2026 work still frames phishing drift mainly through emails, leaving URL drift under-studied.
G: URL-level drift quantification with public time-stamped data.

### garera2007framework
C: Garera, Sujata; Provos, Niels; Chew, Monica; Rubin, Aviel D. (2007). *A framework for detection and measurement of phishing attacks*. Proceedings of the 2007 ACM Workshop on Recurring Malcode (WORM '07), pp. 1-8. DOI: 10.1145/1314389.1314391 URL: https://doi.o
M: Taxonomy of URL obfuscation (IP host, redirection, brand in host/path, etc.); features incl. page rank and host-name/path heuristics; logistic regression filter; used for large-scale measurement.
D: Google-internal URL data; 'several million URLs' measured (abstract); labelled set size not in abstract
E: Not stated in abstract (Ma et al. KDD 2009 summarise it as 97.3% accuracy over 2,500 URLs)
R: Accuracy 97.3% over 2,500 URLs is how Ma et al. (KDD 2009, related-work section) summarise this paper; the abstract itself gives no number. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Phishing URLs are often identifiable from their structure alone; brand names embedded in host/path are strong cues.
L: - Stated by authors: Not available (abstract only). - Our own caveats: Small labelled set; proprietary Google features (page rank) not reproducible; 2007 URL ecosystem.
G: No public dataset; no robustness analysis.

### ghalechyan2024empirical
C: Ghalechyan, Hayk; Israyelyan, Elina; Arakelyan, Avag; Hovhannisyan, Gerasim; Davtyan, Arman (2024). *Phishing URL detection with neural networks: an empirical study*. Scientific Reports, 14, 25134. DOI: 10.1038/s41598-024-74725-6 URL: https://doi.org/10.1038/s
M: Feature engineering without third-party dependencies; deterministic vs probabilistic NNs; daily re-validation.
D: Combination of open sources (Alexa, PhishTank, OpenPhish) and EasyDMARC production data; daily validation feed
E: Daily validation on newly reported URLs (temporal, production)
R: About 97% average accuracy on daily validation data labelled by PhishTank/OpenPhish/EasyDMARC (abstract); high accuracy on short (<50 chars) and long URLs. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Model trained on open+private data succeeds in production; probabilistic NN improves accuracy.
L: - Stated by authors: Validation labels may contain mislabelled data that could not be checked (abstract). - Our own caveats: Private data not shareable; exact architectures unknown here.
G: Public temporal benchmark.

### giri2026shieldphish
C: Gandhi Raj Giri (2026). ShieldPhish: Evaluating Representation Robustness and Cross-Source Generalization in Phishing URL Detection. *Zenodo preprint (submitted to IEEE)*. DOI: 10.5281/zenodo.23141305
M: Diagnoses 'representation shift' (models keying on https:// scheme and leading www.), introduces component-aware URL canonicalisation and hybrid rule fusion, then tests a frozen model on independently sourced, hash-verified post-freeze data
D: Lexical URL classifier trained on conventional public phishing/benign URL sets; post-freeze external snapshots: OpenPhish (phishing) and a Cisco Umbrella Top-1M snapshot (benign); domain-disjoint
E: Pre-registration-style freeze protocol; domain-disjoint external test; bootstrap 95% CIs; variant-stability tests (same URL re-formatted)
R: Trivial formatting shortcuts (https://, www.) inflate offline accuracy and cause near-100% prediction instability across URL variants; after canonicalisation FPR on secondary benchmarks 0.6%; on the external Umbrella benign set FPR 86.84% (95% CI 83.6-90.0) with phishing recall 91.34% (87.4-94.8) and ROC-AUC 0.460 (0.392-0.524) (abstract).
F: Removing representation shortcuts is necessary but not sufficient: cross-source benign traffic still breaks a lexical model; the main driver was vocabulary/score distribution shift on unseen benign sources.
L: **Authors' stated:** Single model family; specific source composition; preprint. **Our caveats:** Not peer reviewed and single-authored; numbers should be cited as a preprint observation. Nonetheless the failure mode (https/www shortcut, catastrophic FPR on popular benign domains) is exactly ours.
G: Peer-reviewed replication of the https/www shortcut effect across datasets.

### guo2017calibration
C: Chuan Guo; Geoff Pleiss; Yu Sun; Kilian Q. Weinberger (2017). *On Calibration of Modern Neural Networks*. Proceedings of the 34th International Conference on Machine Learning (ICML 2017), PMLR 70. URL: https://arxiv.org/abs/1706.04599
M: Define/popularise ECE and reliability diagrams; evaluate post-hoc calibration methods; propose temperature scaling.
D: Standard vision/NLP benchmarks (paper Sec. 5).
E: Expected Calibration Error (ECE), Maximum Calibration Error, NLL, reliability diagrams
R: Temperature scaling achieves lowest ECE on most datasets (paper Table 1).
F: Depth/width/BatchNorm/weight decay affect calibration; one-parameter temperature scaling is surprisingly effective.
L: - Authors' stated limitations: Post-hoc methods assume calibration set from same distribution. - My assessment: Our models are tree ensembles; temperature scaling applies to logits/scores but Platt/isotonic are more usual for RF/GBDT; distribution shift to external datasets breaks post-hoc calibration guarantees.
G: Calibration of security classifiers under dataset shift and adversarial mutation.

### hannousse2021benchmark
C: Abdelhakim Hannousse, Salima Yahiouche (2021). Towards benchmark datasets for machine learning based website phishing detection: An experimental study. *Engineering Applications of Artificial Intelligence*, art. 104347. DOI: 10.1016/j.engappai.2021.104347; arX
M: Reproducible dataset-construction scheme with guidelines (G1: collect from several sources; do not use Alexa domain lists directly because they lack sub-domains/paths); feature-importance and runtime analysis; comparison of classifiers
D: New balanced dataset of 11,430 URLs with 87 features (56 URL, 24 content, 7 external services); phishing from PhishTank/OpenPhish, legitimate from Alexa-derived crawls with paths (Mendeley c2gw7fy2j4)
E: Random stratified splits on the new dataset; feature relevance via several selectors
R: Random forest reaches about 96.6% accuracy on the full feature set (Sec. 6, Table 9 of preprint); hybrid URL+content features outperform URL-only.
F: States that findings in the literature 'are dataset dependent and are far away from generalization' because of unreplicable datasets and the Alexa-domain-only sampling problem.
L: **Authors' stated:** Dataset is small and balanced; external-service features are time-varying. **Our caveats:** Even with their fix for paths, legitimate URLs still come from popular domains, so popularity/format artefacts persist; balanced 50/50 design contradicts base-rate guidance.
G: Large, time-stamped, source-diverse URL benchmark with documented artefact statistics.

### haynes2021lightweight
C: Haynes, Katherine; Shirazi, Hossein; Ray, Indrakshi (2021). *Lightweight URL-based phishing detection using natural language processing transformers for mobile devices*. Procedia Computer Science, 191, pp. 127-134 (FNC/MobiSPC 2021). DOI: 10.1016/j.procs.2021.
M: Baseline ANNs on features; deep ANN on URL-only features (poor); pre-trained transformers fine-tuned on URL text.
D: URL and HTML feature datasets (sizes not in abstract)
E: Not in abstract
R: ANNs on URL+HTML features >96%; deep ANN on URL-only features max 86.2%; pre-trained transformers outperform custom-vocabulary model; about 8 min training (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Pre-trained text transformers transfer to URLs better than custom-vocab models in this setting.
L: - Stated by authors: Not available. - Our own caveats: Abstract omits transformer accuracy numbers.
G: n/a

### henry2026ensembletransfer
C: Saviour Henry, Bliss Utibe-Abasi Stephen, Philip Asuquo (2026). Ensemble transfer learning for cross-dataset phishing detection. *Franklin Open*, art. 100579. DOI: 10.1016/j.fraope.2026.100579
M: Cross-Domain Ensemble Probability Fusion: PCA harmonisation into a 20-dim space plus information-theoretic weighted fusion
D: UCI Phishing Websites dataset and PhiUSIIL phishing URL dataset (zero feature overlap)
E: Cross-dataset accuracy before/after the framework
R: Cross-dataset accuracy 57.4% baseline vs 94.4% with the framework (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Reports a 57.4% cross-dataset baseline, i.e., near chance, between two popular phishing datasets.
L: **Authors' stated:** Not visible from abstract. **Our caveats:** PCA-harmonising non-overlapping feature sets is hard to interpret; the 94.4% figure needs scrutiny for leakage. Use only the baseline collapse as evidence.
G: Interpretable cross-dataset adaptation for URL detectors.

### hu2021idnhomograph
C: Hang Hu; Steve T. K. Jan; Yang Wang; Gang Wang (2021). *Assessing Browser-level Defense against IDN-based Phishing*. 30th USENIX Security Symposium, pp. 3739-3756. URL: https://www.usenix.org/conference/usenixsecurity21/presentation/hu-hang
M: Generate homograph IDNs for popular domains, test display behaviour across browser versions, run a user study.
D: Test cases generated from popular domains; not a URL classifier dataset.
E: Policy bypass rates per browser/version; user deception rates
R: All 7 browsers have rule weaknesses; Chrome reversed some rules over time; bypassing homographs remain highly deceptive to users (abstract; detailed rates in Sec. 5-6).
F: Punycode/IDN homographs still reach users; defenses inconsistent.
L: - Authors' stated limitations: Snapshot to April 2020. - My assessment: Not about ML detection; relevant as threat model for homoglyph mutations.
G: ML URL detectors' handling of punycode (xn--) vs. Unicode rendering is rarely tested.

### huang2019phishingnet
C: Huang, Yongjie; Yang, Qiping; Qin, Jinghui; Wen, Wushao (2019). *Phishing URL Detection via CNN and Attention-Based Hierarchical RNN*. 2019 18th IEEE International Conference on Trust, Security and Privacy in Computing and Communications / 13th IEEE Internatio
M: Character CNN for spatial features, word-level hierarchical RNN with attention for temporal features, CNN fusion, classifier.
D: 'Verified dataset collected from the Internet' (abstract); sizes not available
E: Not available; abstract emphasises generalisation to newly emerging URLs
R: Not in abstract ('competitive performance'). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Fused char/word representations improve generalisation on new URLs (authors' claim).
L: - Stated by authors: Not available. - Our own caveats: No public code/data located.
G: Reproducibility.

### jalil2023highly
C: Jalil, Sajjad; Usman, Muhammad; Fong, Alvis (2023). *Highly accurate phishing URL detection based on machine learning*. Journal of Ambient Intelligence and Humanized Computing, 14(7), pp. 9233-9251. DOI: 10.1007/s12652-022-04426-3 URL: https://doi.org/10.1007/
M: Feature set from full URL/protocol/host/path incl. entropy and brand TF-IDF; compares 8 learners across 6 datasets.
D: Six datasets: two Kaggle URL datasets and four benchmark datasets (names/sizes not on abstract page)
E: Multiple datasets; protocol not on abstract page
R: RF accuracy 96.25% and 94.65% (Kaggle sets); 92.2%, 91.63%, 94.80%, 96.85% (benchmark sets) (Springer abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Accuracy varies noticeably across datasets (91.6-96.9%), illustrating dataset dependence.
L: - Stated by authors: Not available. - Our own caveats: No cross-dataset (train A / test B) protocol visible from abstract.
G: Cross-dataset transfer and calibration.

### jordaney2017transcend
C: Roberto Jordaney, Kumar Sharad, Santanu K. Dash, Zhi Wang, Davide Papini, Ilia Nouretdinov, Lorenzo Cavallaro (2017). Transcend: Detecting Concept Drift in Malware Classification Models. *26th USENIX Security Symposium (USENIX Security 17)*, pp. 625-642.
M: Conformal-evaluator framework: non-conformity measures and p-value-based credibility/confidence to detect when a deployed classifier's decisions are no longer supported by training data; rejection of drifting samples
D: Android (Drebin and Marvin datasets) and Windows malware families (Sec. 5)
E: Train on older data, test on newer; measures how rejection thresholds trade off kept-accuracy vs rejected fraction
R: Shows that rejecting low-credibility predictions restores high precision on drifted Android/Windows data (Sec. 5 tables; full text).
F: Statistical assessment of prediction quality can flag aging models before accuracy visibly collapses; ties drift detection to a decision to abstain.
L: **Authors' stated:** Calibration set requirements and computational cost of conformal p-values; threshold selection needs validation data. **Our caveats:** Not evaluated on URLs; conformal credibility depends on a meaningful distance in feature space, which is weak for sparse lexical URL features.
G: Abstention/rejection as an answer to drift is almost absent from phishing-URL papers.

### kan2005fast
C: Kan, Min-Yen; Thi, Hoang Oanh Nguyen (2005). *Fast webpage classification using URL features*. Proceedings of the 14th ACM International Conference on Information and Knowledge Management (CIKM '05), pp. 325-326. DOI: 10.1145/1099554.1099649 URL: https://doi.o
M: Segments URLs into meaningful tokens, adds component (which URL part), sequential (order) and orthographic features; supervised maximum-entropy modelling.
D: Two standardized webpage-classification domains (topical classification); sizes not in abstract
E: Standard topical-classification benchmarks; split details not in abstract
R: Abstract states URL-only methods 'approach the performance' of full-text/link-based methods in certain scenarios; no numbers available without full text. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Early evidence that URL tokens carry strong signal for page classification; introduced the token-segmentation idea reused by later phishing-URL work.
L: - Stated by authors: Not available (abstract only). - Our own caveats: Topic classification, not security; 2-page poster; no adversarial setting.
G: Pre-dates phishing-specific URL work; no temporal or adversarial evaluation.

### kan2024tesseractext
C: Zeliang Kan, Shae McFadden, Daniel Arp, Feargus Pendlebury, Roberto Jordaney, Johannes Kinder, Fabio Pierazzi, Lorenzo Cavallaro (2024). TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time (Extended Version). *arXiv preprin
M: Extended TESSERACT: constraints, AUT metric, training-data tuning, plus delay-decay mitigation strategies (active learning, rejection, incremental retraining) compared across domains
D: Android: 259,230 samples over five years (abstract); additional case studies on Windows PE and PDF malware
E: Time-aware evaluation with AUT over multi-year windows; cross-domain (Android, PE, PDF)
R: Abstract states reported F1 'upwards of 0.99' in prior work are inflated under realistic settings; per-domain AUT curves in Sec. 6-7 (full text available).
F: Spatial and temporal bias generalise beyond Android; periodic tuning and drift-mitigation strategies delay but do not remove decay.
L: **Authors' stated:** Preprint, not yet peer-reviewed in this extended form; malware-focused. **Our caveats:** Still no URL/phishing case study; the mitigation comparison assumes labelled fresh data is affordable.
G: Extending the PE/PDF case-study methodology to phishing URL feeds is open.

### kehkashan2025explainable
C: Tanzila Kehkashan; Maha Abdelhaq; Ahmad Sami Al-Shamayleh; Nazish Huda; Imran Ashraf Yaseen; Abdelmuttlib Ibrahim Abdalla Ahmed; Adnan Akhunzada (2025). *Explainable phishing website detection for secure and sustainable cyber infrastructure*. Scientific Report
M: Rank features with SHAP, retain top features, train five classical classifiers; ablation with/without SHAP selection.
D: UCI Phishing Websites dataset (Mohammad et al.), 11,055 records, 30 engineered features (the abstract instead mentions a Kaggle dataset of >11,000 URLs; the paper does not reconcile the two).
E: Hold-out; accuracy, precision, recall, F1; ablation without SHAP
R: RF with SHAP selection: accuracy 97.0%, precision 97.0%, recall 97.6%, F1 97.3%; RF without SHAP 90.0% (ablation); other models 93.3-96.0% (results section/tables as read on PMC).
F: SHAP-guided feature selection improved all classifiers; RF best.
L: - Authors' stated limitations: Single small dataset; classical models only. - My assessment: UCI dataset is 2015-era with pre-extracted features, so no raw URLs and no mutation tests are possible; inconsistent dataset description.
G: No raw-URL lexical pipeline, no latency or calibration reporting.

### khan2026stacking
C: Khan, Hafiz Aziz; Akter, Sonia; Lindon, Abdur Rahman; Akter, Taslima; Rasul, Iftekhar; Rahman, Mamunur; Tohfa, Nasrin Akter; Hossain, Iftekhar (2026). *Explainable AI for phishing URL detection: a Bayesian-optimized stacking ensemble framework with SHAP-guided
M: 12-stage pipeline: EDA, SHAP feature selection, benchmarking seven algorithm families, Bayesian optimisation, stacking, threshold tuning, SHAP explanations.
D: Public Kaggle benchmark (Harisudhan 2024): 247,950 URLs with 41 pre-extracted structural/lexical features; raw URL strings not released (Sec. 3.1)
E: Stratified 80/20 split, 5-fold CV inside training; no cross-dataset
R: Top tier: Extra Trees Acc 0.9671 / AUC 0.9948, RF Acc 0.9667 / AUC 0.9930; stacking ensemble leads on Acc/F1/MCC/Kappa with AUC 0.9947 vs 0.9948 for Extra Trees; confusion matrix 24,977 TN, 731 FP, 883 FN on test set, FPR 731/25,708 = 2.84% (Sec. 5, Tables 6-10). (Numbers taken from the full text; section/table references given where identified.)
F: Stacking gives marginal gains over tuned Extra Trees; SHAP-selected features retain performance.
L: - Stated by authors: Dataset lacks raw URLs, undocumented collection windows/sources; single dataset; no temporal validation (Sec. 3.1 and limitations). - Our own caveats: About 248k pre-featurised Kaggle set is very similar in scale to ours; results on random splits are likely optimistic.
G: Cross-dataset / temporal evaluation, artifact audit, calibration measurement.

### kibriya2025lightweight
C: Kibriya, Hareem; Amin, Rashid; Alshamrani, Sultan S.; Rehman, Safia; Hassan, Mehdi; Alsubaei, Faisal S. (2025). *Lightweight malicious URL detection using deep learning and large language models*. Scientific Reports, 15, 43044. DOI: 10.1038/s41598-025-26653-2 
M: Extract URL embeddings with pre-trained LLMs; train small recurrent head; LIME for token-level attributions; latency measurement.
D: Kaggle malicious-urls dataset: 651,191 URLs (428,103 benign, 96,457 defacement, 94,111 phishing, 32,520 malware), aggregated from ISCX-URL-2016, PhishTank, Malware Domains, PhishStorm (Dataset section)
E: 60:40 random train/test split; ablations; per-class PR/ROC curves
R: 97.5% accuracy with BERT and T5 embeddings (avg precision/recall/F1 0.97/0.97/0.96); GPT-2 97%; 0.119 ms per sample; per-class AUC 0.99-1.0 (Results; Table 2, Figs. 6-8). (Numbers taken from the full text; section/table references given where identified.)
F: Frozen LLM embeddings + tiny head reach boosted-tree-level accuracy on the Kaggle set; LIME gives readable token attributions.
L: - Stated by authors: Single dataset; obfuscation robustness tested only partly. - Our own caveats: Same aggregated Kaggle dataset as Sankaranarayanan 2024 - source-formatting shortcuts likely; random split.
G: Cross-dataset/temporal validation.

### kintis2017combosquatting
C: Panagiotis Kintis; Najmeh Miramirkhani; Charles Lever; Yizheng Chen; Rosa Romero-Gomez; Nikolaos Pitropakis; Nick Nikiforakis; Manos Antonakakis (2017). *Hiding in Plain Sight: A Longitudinal Study of Combosquatting Abuse*. Proceedings of the 2017 ACM SIGSAC C
M: Identify combosquatting domains for popular trademarks in large DNS datasets; study registration, longevity, abuse.
D: Passive DNS + active DNS over ~6 years (paper Sec. 3); not released.
E: Prevalence, lifetime, abuse categories
R: ~468B DNS records analysed; ~60% of abusive combosquatting domains active for >1,000 days (per abstract/summary).
F: Combosquatting is more prevalent than typosquatting and long-lived.
L: - Authors' stated limitations: Trademark list limited; attribution of abuse is heuristic. - My assessment: No ML detection; lexical cues (brand token + hyphen/keyword) are what our model should capture.
G: Combosquatting-specific lexical features in URL classifiers are rarely isolated or explained.

### kolari2006svms
C: Kolari, Pranam; Finin, Tim; Joshi, Anupam (2006). *SVMs for the Blogosphere: Blog Identification and Splog Detection*. AAAI Spring Symposium on Computational Approaches to Analyzing Weblogs (2006). URL: https://www.semanticscholar.org/paper/b54518d807f05ebe5ce
M: SVM classifiers over textual and URL-derived feature sets; URL tokens shown useful.
D: Blog/splog samples (sizes not retrieved)
E: Not retrieved
R: Not retrieved. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: URL-token features contribute to spam-blog detection (often cited as early use of URL lexical features).
L: - Stated by authors: Not retrieved. - Our own caveats: Peripheral to phishing; included only for lineage.
G: n/a

### krishnan2025drift
C: Sruthi Krishnan, Manohar Naik S (2025). An Efficient Framework for Phishing URL Detection Using Adaptive Drift-Aware Feature Monitoring and Online Learning. *Security and Privacy (Wiley)*. DOI: 10.1002/spy2.70057
M: Kolmogorov-Smirnov drift detection on feature distributions plus online SGD updates
D: Real-time phishing URLs from PhishTank (abstract); benign source not stated in abstract
E: Not specified in abstract beyond 'validation using real-time phishing URLs from PhishTank'
R: 99.85% accuracy, 0.067% false-positive rate (abstract). (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Claims that drift-aware online learning sustains near-perfect accuracy.
L: **Authors' stated:** Not visible from abstract. **Our caveats:** A 99.85%/0.067% result on a PhishTank-centred set is exactly the kind of figure TESSERACT/Arp et al. warn is inflated; no cross-source or base-rate analysis mentioned. Useful as an example of the prevailing evaluation style, not as a benchmark.
G: Independent, source-disjoint validation of drift-aware URL detectors.

### kulkarni2024mitigating
C: Aditya Kulkarni, Vivek Balachandran, Dinil Mon Divakaran, Tamal Das (2024). Mitigating Bias in Machine Learning Models for Phishing Webpage Detection. *arXiv preprint*. arXiv: 2401.08363
M: Identifies dataset-assembly biases (imbalanced, non-diverse, stale datasets; zero-day gap) and proposes a tool to synthesise phishing pages for any set of legitimate URLs to debias/test detectors
D: Position paper; proposes generating synthetic phishing pages from legitimate URLs
E: None reported (short paper)
R: None.
F: Argues that classifiers 'learn distinctive features from training data' and that biased dataset composition skews decision rules; proposes synthetic augmentation.
L: **Authors' stated:** No evaluation. **Our caveats:** Short preprint, limited evidence; include only as a recent explicit statement of dataset bias in phishing detection.
G: Empirical measurement of how much dataset composition bias changes learned rules.

### le2011phishdef
C: Le, Anh; Markopoulou, Athina; Faloutsos, Michalis (2011). *PhishDef: URL names say it all*. 2011 Proceedings IEEE INFOCOM, pp. 191-195 (arXiv:1009.2275). DOI: 10.1109/INFCOM.2011.5934995 URL: https://arxiv.org/abs/1009.2275 - Type: conference | Theme (L1): a-f
M: Selects lexical features resistant to obfuscation (host/path tokens, lengths, counts), compares lexical-only vs full (host/WHOIS) features, proposes AROW online learning; PhishDef combines these.
D: PhishTank (4,082 verified phishing, June 2010), MalwarePatrol (2,001), Yahoo random (4,143) and DMOZ random (4,012) URLs; 5 pairings (Table I)
E: Online cumulative error over batches of 400 URLs; label-noise injection experiments
R: Lexical-only accuracy 96-98%, within about 1% of full features (Sec. V, Table II); AROW reduces error up to 27% vs CW on DMOZ-Malware (Table III); about 95% accuracy with 5-10% label noise (Sec. V-C); external feature collection averages 1.64 s/URL. (Numbers taken from the full text; section/table references given where identified.)
F: Lexical features suffice for practical purposes; online AROW is robust to mislabelled data.
L: - Stated by authors: Small datasets; obfuscation list may be incomplete. - Our own caveats: Benign classes are directory/random homepages; no temporal split.
G: Robustness to adversarial token manipulation beyond listed obfuscations.

### le2018urlnet
C: Le, Hung; Pham, Quang; Sahoo, Doyen; Hoi, Steven C. H. (2018). *URLNet: Learning a URL Representation with Deep Learning for Malicious URL Detection*. arXiv preprint arXiv:1802.03162. URL: https://arxiv.org/abs/1802.03162 - Type: preprint | Theme (L1): c-char-
M: Character CNN branch + word CNN branch (words embedded via character CNNs to handle rare words); jointly trained; ablations on branches and embedding modes.
D: VirusTotal crawl: 5M URLs for training (sampled from first 60%, time-ordered), 10M for testing (from last 40%); malicious = flagged by >=5 blacklists, benign = 0 (Sec. 4.1.1, Table 1)
E: Temporal split (train earlier 60%, test later 40%); ROC/AUC and TPR at FPR 1e-4..1e-1 (Table 3)
R: URLNet(Full) achieves the best AUC and higher TPR at FPR 1e-3..1e-1 vs BoW baselines; slightly worse than word-level at FPR 1e-4 (Table 3, Fig. 4); feature vectors about 14x smaller than BoW for 2k URLs (Sec. 4.5). (Numbers taken from the full text; section/table references given where identified.)
F: Joint char+word CNN generalises to unseen words better than BoW.
L: - Stated by authors: Hyperparameter sensitivity; large compute. - Our own caveats: Labels from blacklist counts; multi-class malware vs phishing collapsed into 'malicious'.
G: Explainability of learned features; robustness.

### lee2020robustphishing
C: Jehyun Lee; Pingxiao Ye; Ruofan Liu; Dinil Mon Divakaran; Mun Choon Chan (2020). *Building Robust Phishing Detection System: an Empirical Analysis*. NDSS Workshop on Measurements, Attacks, and Defenses for the Web (MADWeb 2020). URL: https://www.ndss-symposium
M: Train multiple models, each on a random feature subset with injected noise; majority vote; evaluate against evasion strategies that alter feature values.
D: Benign: Alexa top 300k domains ranked Feb 2019, 110,090 pages crawled May-Aug 2019; phishing: PhishTank daily feed (paper Sec. IV). No license stated.
E: Native model vs. proposed ensemble under several evasion strategies (feature mimicry)
R: Ensemble 'performs close to native model' without attack and is 'more robust against evasion attacks' (abstract); numeric tables in Sec. V.
F: Feature-subset noisy ensembles raise evasion cost at small clean-accuracy cost.
L: - Authors' stated limitations: Evasion strategies are simulated by feature manipulation. - My assessment: Not URL-only; small-scale; no calibration or latency reporting.
G: Robust ensembles for lexical-only URL models with explicit mutation operators.

### lepochat2019tranco
C: Victor Le Pochat, Tom Van Goethem, Samaneh Tajalizadehkhoob, Maciej Korczyński, Wouter Joosen (2019). Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation. *Network and Distributed System Security Symposium (NDSS 2019)*. DOI: 10.14722/nd
M: Measurement of top-list instability and manipulability (demonstrates cheap insertion into Alexa); proposes Tranco aggregate list
D: Alexa, Cisco Umbrella, Majestic and Quantcast top lists over time; 133 security papers surveyed for top-list usage
E: Longitudinal list comparison; manipulation experiments
R: Shows large day-to-day churn in Alexa and that a domain can be inserted into the top 1M cheaply (Sec. 4-5); many security papers (incl. phishing) use Alexa as benign ground truth (Sec. 3).
F: Using Alexa as 'legitimate' ground truth is unreliable and manipulable; Tranco is proposed for reproducibility.
L: **Authors' stated:** Any list is a proxy for popularity, not legitimacy. **Our caveats:** Popularity lists contain only registrable domains/hostnames, which is the root of the 'www./index page' artefact in URL datasets.
G: Legitimate-URL sampling beyond popularity lists.

### li2021malwarecalibration
C: Deqiang Li; Tian Qiu; Shuo Chen; Qianmu Li; Shouhuai Xu (2021). *Can We Leverage Predictive Uncertainty to Detect Dataset Shift and Adversarial Examples in Android Malware Detection?*. Annual Computer Security Applications Conference (ACSAC '21), pp. 596-608. 
M: Re-build four Android malware detectors with six calibration methods; measure nine uncertainty metrics incl. imbalance-aware ones; test on shifted and adversarial data.
D: Android malware datasets with temporal split (paper Sec. 5); not URL data.
E: Calibration (ECE, Brier, NLL) and uncertainty quality under temporal dataset shift and under adversarial evasion
R: Main findings (abstract): predictive uncertainty helps under dataset shift but cannot cope with adversarial evasion; approximate Bayesian methods most promising; calibration methods can fail under attack (numeric tables in Sec. 6).
F: Vanilla detectors poorly calibrated; calibration degrades under shift and collapses under adversarial examples.
L: - Authors' stated limitations: Android-only; specific attack set. - My assessment: Different domain, but the protocol (calibration x shift x adversarial) maps directly onto our plan.
G: No equivalent study for phishing URL classifiers.

### li2025urlbert
C: Li, Yujie; Liu, Yiwei; Li, Peiyue; Jia, Yifan; Wang, Yanbin (2025). *Continuous Multi-Task Pre-training for Malicious URL Detection and Webpage Classification (URLBERT)*. Computer Networks, 270, 111513 (arXiv:2402.11495, first titled 'URLBERT: A Contrastive an
M: Custom URL tokenizer; multi-task pre-training with contrastive and adversarial objectives; evaluation on phishing detection, ad-URL detection, webpage topic classification; code github.com/Davidup1/URLBERT.
D: Pre-training: 3.28B unique URLs (Common Crawl 2.85B, Open PageRank 338.71M, expired domains 538.2M, malicious sources 8.26M, ODP 3.86M); phishing task: GramBeddings + Mendeley merged, 126,733 phishing / 237,889 benign (Table 1)
E: 60/40 train/test for phishing and ad tasks; 80/20 for topic task; data-scale experiments; TPR at FPR 0.001
R: Phishing detection AUC > 0.99; with 60% of training data accuracy 0.9720 and TPR about 0.8 at FPR 0.001; outperforms BERT (0.9156) and RoBERTa (0.9206) in a low-data setting at 0.9506 (Sec. 5); traditional KNN/RF/NB still > 96% accuracy on this benchmark. (Numbers taken from the full text; section/table references given where identified.)
F: URL-domain pre-training helps most in low-data regimes; classical lexical models remain strong on in-distribution benchmarks.
L: - Stated by authors: Compute; multi-task interference partially addressed. - Our own caveats: Removed URLs longer than 150 chars from the phishing benchmark (Table 1) - a preprocessing choice that interacts with length artifacts.
G: Cross-dataset and temporal evaluation of pre-trained URL encoders.

### liu2024transurl
C: Liu, Ruitong; Wang, Yanbin; Guo, Zhenhao; Xu, Haitao; Qin, Zhan; Ma, Wenrui; Zhang, Fan (2024). *TransURL: Improving malicious URL detection with multi-layer Transformer encoding and multi-scale pyramid features*. Computer Networks, 253, 110707 (arXiv:2312.005
M: Co-trains char-aware transformer with pyramid/multi-scale modules; baselines URLNet, GramBeddings, URLTran, TextCNN etc.; code released (github.com/Vul-det/TransURL).
D: GramBeddings (800k balanced, 2019-2021), Mendeley/MalCrawler (1,561,934; 35,315 malicious), Kaggle-1 (632,503 balanced), Kaggle-2 (4-class, about 651k) (Table 2)
E: Random splits; class-imbalance subsampling; multi-class; cross-dataset (Table 6); adversarial evasion-character attacks; 30 live-URL case study
R: Peak F1 improvement 40% in class-imbalanced setting and +14.13% accuracy under adversarial attack vs best baseline (abstract); cross-dataset example: TransURL Acc 0.9023 / F1 0.8846 / AUC 0.9839 vs GramBeddings Acc 0.7018 (Table 6); all 30 live malicious pages detected. (Numbers taken from the full text; section/table references given where identified.)
F: Cross-dataset performance drops sharply for all models (GramBeddings to about 70% accuracy), TransURL degrades least; adversarial character insertion hurts baselines.
L: - Stated by authors: Compute cost; evasion types limited. - Our own caveats: Cross-dataset results still far from in-distribution, confirming our generalisation concern; Table 2 shows TLD/length distribution differences across datasets - artifact candidates.
G: Artifact-aware evaluation; explainability.

### liu2025pmanet
C: Liu, Ruitong; Wang, Yanbin; Xu, Haitao; Qin, Zhan; Zhang, Fan; Liu, Yiwei; Cao, Zheng (2025). *PMANet: Malicious URL detection via post-trained language model guided multi-level feature attention network*. Information Fusion, 113, 102638. DOI: 10.1016/j.inffus
M: Post-training (masked token, noisy-text recognition, domain discrimination) then attention-based fusion network.
D: Public URL datasets (specifics not in abstract)
E: Small-data, class-imbalance and adversarial scenarios; 20-URL live case study (abstract)
R: AUC 0.9941; all 20 malicious URLs in case study detected (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Post-training + multi-level attention improves robustness.
L: - Stated by authors: Not available. - Our own caveats: Same group as TransURL/URLBERT; heavy models.
G: Explainability, cost.

### lundberg2017shap
C: Scott M. Lundberg; Su-In Lee (2017). *A Unified Approach to Interpreting Model Predictions*. Advances in Neural Information Processing Systems 30 (NeurIPS 2017). URL: https://arxiv.org/abs/1705.07874
M: Defines the class of additive feature attribution methods, shows a unique solution (SHAP values) satisfying three desirable properties, and gives model-agnostic (KernelSHAP) and model-specific estimators.
D: None specific to security; experiments on standard ML benchmarks and MNIST-style tasks (see paper Sec. 5).
E: Theoretical axioms (local accuracy, missingness, consistency) + user-study agreement and sample-efficiency experiments
R: No security metrics; qualitative/user-study results only (paper Sec. 5, Fig. 4-5).
F: SHAP unifies LIME, DeepLIFT, layer-wise relevance propagation and Shapley sampling; KernelSHAP is more sample-efficient than LIME-style sampling.
L: - Authors' stated limitations: Exact Shapley computation is exponential; KernelSHAP is an approximation and assumes feature independence under the background distribution. - My assessment: Explanations on correlated lexical URL features (e.g. url_length vs. path_length) can split credit arbitrarily; needs TreeExplainer or grouped features.
G: Little guidance on explanation stability under input perturbation, which we need for mutation-robustness tests.

### lundberg2020treeexplainer
C: Scott M. Lundberg; Gabriel Erion; Hugh Chen; Alex DeGrave; Jordan M. Prutkin; Bala Nair; Ronit Katz; Jonathan Himmelfarb; Nisha Bansal; Su-In Lee (2020). *From local explanations to global understanding with explainable AI for trees*. Nature Machine Intelligen
M: Exact SHAP computation for trees (TreeExplainer), SHAP interaction values, and aggregation of local explanations into global importance, dependence and clustering plots.
D: Three medical datasets (NHANES mortality, chronic kidney disease, hospital procedure duration); not security data.
E: Benchmarks of 13 explanation methods on consistency/accuracy metrics; medical mortality/kidney/hospital datasets
R: Method-comparison benchmark scores reported in the paper's Fig. 2/3; no classification accuracy relevant to us.
F: TreeExplainer is exact and fast; gain/split-count importances can be inconsistent; local explanations reveal interaction effects and dataset shift.
L: - Authors' stated limitations: Interventional vs. observational conditional expectation choice affects attributions; limited to tree models. - My assessment: Our ensemble (if it mixes non-tree models) needs KernelSHAP or per-model explanation; per-sample cost rises with ensemble size.
G: No study of explanation drift between training and external datasets for security tasks.

### ma2009beyond
C: Ma, Justin; Saul, Lawrence K.; Savage, Stefan; Voelker, Geoffrey M. (2009). *Beyond blacklists: learning to detect malicious web sites from suspicious URLs*. Proceedings of the 15th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KD
M: Automatically extracts tens of thousands of binary lexical tokens (hostname and path tokens, delimiters) plus host-based properties; compares feature groups; L1-LR for sparse interpretable models.
D: Benign: 15,000 URLs each from Yahoo random-URL feed and DMOZ; malicious: 5,500 PhishTank + Spamscatter URLs; 4 benign/malicious pairings, 20k-30k URLs each (Sec. 4.1)
E: 10 random 50/50 splits per dataset; also cross-source training/testing (Table 4)
R: Overall accuracy 95-99% (abstract); error rates 1.2-6% for full feature set and 1.1-3.4% without WHOIS/blacklist features (Sec. 4.2, Fig. 2); lexical-only about 15% error at best vs 10% for host-only on the hardest set (Sec. 4.2); cross-source training degrades strongly (Table 4: e.g. 14-21% error when trained on one source and tested on another). (Numbers taken from the full text; section/table references given wher
F: Lexical and host features are complementary; automatically generated token features beat hand-chosen ones; models trained on one data source generalise poorly to another.
L: - Stated by authors: Features assume infrastructure lookups (WHOIS/DNS) are available; redirection and short URLs not handled; distribution shift between sources acknowledged (Sec. 4.4). - Our own caveats: Benign sources (Yahoo/DMOZ) are directory homepages, so length/token artifacts favour the classifier; blacklist features leak labels.
G: Cross-source generalisation and temporal robustness left largely open.

### ma2009identifying
C: Ma, Justin; Saul, Lawrence K.; Savage, Stefan; Voelker, Geoffrey M. (2009). *Identifying suspicious URLs: an application of large-scale online learning*. Proceedings of the 26th International Conference on Machine Learning (ICML '09), pp. 681-688. DOI: 10.1145
M: Real-time feature collection system; sparse high-dimensional lexical+host features (grows to millions); compares online algorithms with continuous retraining to batch models retrained at intervals.
D: Live feed from a large web-mail provider: about 20,000 URLs/day (6-7k malicious, about 2:1 benign:malicious) over 100 days, nearly 2 million URLs (Sec. 4.1)
E: Temporal: train on days up to t, test on day t+1; cumulative error over 100 days (Fig. 3-4)
R: Up to 99% accuracy on balanced data (abstract); CW online learning tracks batch accuracy with cumulative error about 1-2% while stale batch models degrade (Fig. 3-4; per-day false negatives up to 15% on some days, Sec. 5). (Numbers taken from the full text; section/table references given where identified.)
F: Continuous retraining matters: feature distribution of malicious URLs drifts daily; online CW matches batch at a fraction of cost.
L: - Stated by authors: Depends on a proprietary labelled feed; host features require live lookups. - Our own caveats: Day-ahead protocol is strong, but labels come from the same provider's filters (potential label bias).
G: Public reproducible temporal benchmarks absent.

### ma2011learning
C: Ma, Justin; Saul, Lawrence K.; Savage, Stefan; Voelker, Geoffrey M. (2011). *Learning to detect malicious URLs*. ACM Transactions on Intelligent Systems and Technology, 2(3), Article 30, pp. 1-24. DOI: 10.1145/1961189.1961202 URL: https://doi.org/10.1145/19611
M: Unifies the batch (KDD'09) and online (ICML'09) studies; adds analysis of feature importance and system considerations.
D: Consolidates the KDD/ICML datasets: about 2M-URL web-mail feed over 100 days plus directory/blacklist pairings
E: Random splits and day-ahead temporal evaluation (as in the conference versions)
R: Abstract-level only here; conference versions report 95-99% accuracy and about 1-2% cumulative error online. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Same conclusions as the conference papers with extended analysis.
L: - Stated by authors: See conference versions. - Our own caveats: Content assessed via metadata and the conference papers; article itself paywalled.
G: As above.

### mamun2016iscxurl
C: Mohammad Saiful Islam Mamun; Mohammad Ahmad Rathore; Arash Habibi Lashkari; Natalia Stakhanova; Ali A. Ghorbani (2016). *Detecting Malicious URLs Using Lexical Analysis*. Network and System Security (NSS 2016), LNCS 9955, pp. 467-482, Springer. DOI: 10.1007/97
M: Extract lexical features, select sufficient feature subsets, classify with tree-based and kNN methods; study obfuscation techniques per URL type.
D: ISCX-URL-2016 (see Dataset section). Download: http://cicresearch.ca/CICDataset/ISCX-URL-2016/ (UNB CIC page). License: none stated (UNB copyright). Timestamps: none in released CSVs (lexical feature files). Labels: benign / spam / phishing / malware / defacement by source.
E: Per-class and multi-class accuracy; feature selection
R: ~99% accuracy for single-type detection and 93-99% as a group with Random Forest (abstract/Sec. 5; Table 2a: >97% on single-class datasets).
F: Lexical analysis is effective and efficient; RF best; obfuscation types differ by attack class.
L: - Authors' stated limitations: Class labels inherited from sources; dataset era 2016. - My assessment: Source-per-class design means classifiers can learn source artefacts (Arp et al. pitfall); benign = Alexa top sites only.
G: Temporal metadata absent; URL strings in the public release are partially feature-only.

### mamun2016lexical
C: Mamun, Mohammad Saiful Islam; Rathore, Mohammad Ahmad; Lashkari, Arash Habibi; Stakhanova, Natalia; Ghorbani, Ali A. (2016). *Detecting Malicious URLs Using Lexical Analysis*. Network and System Security (NSS 2016), Lecture Notes in Computer Science vol. 9955,
M: Extracts lexical/statistical features (lengths, counts, entropy, token statistics, argument features); studies which obfuscation tricks relate to each URL type; defacement on trusted Alexa sites considered.
D: ISCX-URL-2016 (UNB CIC): 'over 110,000 URLs' across benign, spam, phishing, malware, defacement (abstract)
E: Per-class binary and multi-class experiments; split details not in abstract
R: Abstract gives no numbers. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Lexical analysis is effective and efficient for proactive detection; released the ISCX-URL-2016 benchmark.
L: - Stated by authors: Not available. - Our own caveats: ISCX-URL-2016 benign class drawn from Alexa top sites; later studies note duplicate/near-duplicate URLs; features partially overlap with ours, so cross-dataset use needs care.
G: Benchmark artifacts and temporal validity not analysed.

### maneriker2021urltran
C: Maneriker, Pranav; Stokes, Jack W.; Lazo, Edir Garcia; Carutasu, Diana; Tajaddodianfar, Farid; Gururajan, Arun (2021). *URLTran: Improving Phishing URL Detection Using Transformers*. MILCOM 2021 - IEEE Military Communications Conference, pp. 197-204 (arXiv:210
M: Compares URLTran_BERT, URLTran_RoBERTa, URLTran_CustVoc against URLNet and Texception; adversarial data augmentation and fine-tuning.
D: Microsoft browser telemetry: 6 weeks; train 1,039,413, validation 259,854, test 1,784,155 URLs (8,742 phishing) after 1:20 down-sampling (Sec. 3)
E: Temporal split (4 weeks train / 1 validation / 1 test); TPR at FPR 0.01%; adversarial fine-tuning tests
R: Table 2: URLTran_BERT Acc 99.67%, TPR@0.01%FPR 86.80%, F1 0.9971, AUC 0.9993; URLNet TPR@0.01% 71.20%; Texception 52.15%; relative TPR improvement over 21.9% (abstract). (Numbers taken from the full text; section/table references given where identified.)
F: Fine-tuned BERT beats char/word CNNs at low FPR; adversarial fine-tuning preserves low FPR under homoglyph/compound-split attacks.
L: - Stated by authors: Proprietary data; attack coverage limited. - Our own caveats: Accuracy about 99.6% for all models shows accuracy is uninformative at this imbalance; TPR@low-FPR is the meaningful metric.
G: Public reproducible low-FPR benchmark; explainability of transformer URL models.

### marchal2014phishstorm
C: Marchal, Samuel; Francois, Jerome; State, Radu; Engel, Thomas (2014). *PhishStorm: Detecting Phishing With Streaming Analytics*. IEEE Transactions on Network and Service Management, 11(4), pp. 458-471. DOI: 10.1109/TNSM.2014.2377295 URL: https://doi.org/10.110
M: Splits URL into registered domain (mld.ps) vs rest; computes relatedness among words using search-engine query logs; features on word counts, brand presence, Alexa rank; ML classification and a confidence-rated score; Bloom-filter streaming design.
D: 96,018 URLs: 48,009 phishing (PhishTank, from 53,089 unique) + 48,009 legitimate (DMOZ); released as urlset.csv (Sec. VI-A)
E: 10-fold cross-validation, 100 runs (Sec. VI-B)
R: Accuracy 94.91% with 1.44% FPR after threshold tuning (abstract; Sec. VI-C), 95.66% at default threshold; features 1-9 alone 93.48% (Sec. VI-C). (Numbers taken from the full text; section/table references given where identified.)
F: Legitimate URLs show coherent word relatedness across domain and path; phishing URLs do not.
L: - Stated by authors: Depends on search-engine query APIs; relatedness changes over time. - Our own caveats: The released 'PhishStorm' dataset is widely reused (e.g., in Kaggle mixes); DMOZ benign class again homepage-heavy.
G: External-API dependence conflicts with offline/lexical deployment.

### marchal2018designing
C: Samuel Marchal, N. Asokan (2018). On Designing and Evaluating Phishing Webpage Detection Techniques for the Real World. *11th USENIX Workshop on Cyber Security Experimentation and Test (CSET 18)*.
M: Guidelines for ground-truth composition, evaluation metrics and temporal-resilience testing of phishing webpage detectors
D: Position/guidelines paper; no new dataset
E: Recommends: legitimate set must include unpopular/long-tail sites, URLs with paths (not just FQDNs from Alexa/DMOZ), real-world class distribution (about 1 phish per 100 benign) to avoid base-rate fallacy, test set larger than training set, and temporal-resilience tests (train at time t, test on later pages)
R: No experiments; prescriptive. States that balanced (1/1) datasets 'suffer from base rate fallacy' and that a 1:100 distribution is needed for a meaningful precision (Sec. 3-4).
F: Academic detectors look excellent on non-representative data; representativity of the legitimate class (popularity, URL structure) and temporal evaluation are the main missing pieces.
L: **Authors' stated:** Guidelines not empirically validated in the paper. **Our caveats:** Written for webpage (content) detectors, but every data-composition guideline applies verbatim to URL-only detectors.
G: Few later URL papers follow these guidelines; our paper can operationalise them.

### mcgrath2008behind
C: McGrath, D. Kevin; Gupta, Minaxi (2008). *Behind Phishing: An Examination of Phisher Modi Operandi*. USENIX Workshop on Large-Scale Exploits and Emergent Threats (LEET '08). URL: https://www.usenix.org/legacy/event/leet08/tech/full_papers/mcgrath/mcgrath.pdf -
M: Compares phishing URL feeds against DMOZ: URL/domain length distributions, character/vowel distributions, brand-name inclusion, subdomain use, IP hosts, shorteners; domain registration-to-activation delays; lifetime.
D: PhishTank and MarkMonitor real-time phishing feeds (>2 months, 2007-08), MarkMonitor-2006 archive; DMOZ URLs as benign comparison; whois/zone files
E: Descriptive statistics; no classification
R: URL length modes: 22 chars (DMOZ) vs 67 (PhishTank) vs 107 (MarkMonitor) (Sec. 3, Fig. 1); domain length mode 7 vs 10 chars (Fig. 2); 50-75% of phishing URLs contain target brand (Table 3); >3/4 contain subdomains; mean domain lifetime about 3 days (Sec. 5). (Numbers taken from the full text; section/table references given where identified.)
F: Length, vowel ratio, character-diversity and brand-in-URL are strongly discriminative; phishing domains are short-lived.
L: - Stated by authors: Preliminary work; feeds biased toward reported phishing. - Our own caveats: 2007-era statistics; DMOZ as 'benign' is homepage-heavy (same shortcut risk as later datasets).
G: No learning or temporal-drift evaluation.

### mia2024featurestrust
C: Maraz Mia, Darius Derakhshan, Mir Mehedi A. Pritom (2024). Can Features for Phishing URL Detection Be Trusted Across Diverse Datasets? A Case Study with Explainable AI. *Proceedings of the 11th International Conference on Networking, Systems, and Security (NSy
M: Train/test within and across datasets (Exp-1..6); SHAP global/local explanations to compare feature contribution
D: Dataset-1: Vrbancic et al. (88,647 instances, 58,000 benign); Dataset-2: Kaggle set with 19,431 rows (9,716 benign); 20 overlapping numeric URL features
E: Random splits within dataset; cross-dataset transfer on common features; merged training
R: Within-dataset accuracy is high, but cross-dataset accuracy 'drops drastically to 51%' (train D1, test D2) and 59% (train D2, test D1) (Sec. 3.5); SHAP shows the same feature (e.g., url_google_index, qty_dot_url) changing sign/importance across datasets.
F: Features are dataset dependent; near-chance cross-dataset accuracy from models that look excellent in-distribution.
L: **Authors' stated:** Only two datasets; only overlapping features. **Our caveats:** Datasets are pre-extracted feature tables, so raw-URL artefacts (scheme/www) cannot be ablated.
G: Cross-dataset tests on raw URLs with controllable artefacts.

### niculescumizil2005calibration
C: Alexandru Niculescu-Mizil; Rich Caruana (2005). *Predicting good probabilities with supervised learning*. Proceedings of the 22nd International Conference on Machine Learning (ICML '05). DOI: 10.1145/1102351.1102430 URL: https://doi.org/10.1145/1102351.1102430
M: Empirical comparison across ten learners; Platt scaling vs isotonic regression on held-out calibration data.
D: Eight binary classification problems (paper Sec. 3).
E: Squared error (Brier), log-loss, reliability diagrams
R: Boosted trees and SVMs push predictions away from 0/1 (sigmoid-shaped reliability diagrams); RF/bagging are better calibrated; isotonic needs >~1000 calibration points (paper Sec. 4-5; numbers not reproduced here).
F: Boosting (max-margin) methods are systematically miscalibrated and benefit most from Platt/isotonic; RF and bagged trees nearly calibrated.
L: - Authors' stated limitations: 2005-era learners; no gradient boosting with log-loss. - My assessment: Modern XGBoost/LightGBM with logistic loss are better calibrated than AdaBoost, so findings need re-checking on our ensemble.
G: Calibration behaviour of soft-voting/stacked ensembles on security data.

### nowroozi2022advurl
C: Ehsan Nowroozi; Abhishek; Mohammadreza Mohammadi; Mauro Conti (2022). *An Adversarial Attack Analysis on Malicious Advertisement URL Detection Framework*. arXiv:2204.13172 (preprint). URL: https://arxiv.org/abs/2204.13172
M: Six feature groups (lexical + scraped), four boosting/bagging models, K-Means visual analysis, Zeroth-Order-Optimization attack.
D: Twelve dataset variants built by the authors (paper Sec. IV); no license statement seen.
E: Accuracy, FNR; mismatched and unlabelled datasets; limited-knowledge exploratory attack
R: Best FNR 0.0037 and accuracy 99.63% (abstract).
F: Tree ensembles are accurate but can be attacked in a black-box setting.
L: - Authors' stated limitations: Preprint; ZOO attack operates on feature vectors. - My assessment: Feature-space attack realism unclear (cf. SpacePhish).
G: Problem-space URL attacks on gradient-boosted lexical models.

### oest2018phisherkit
C: Adam Oest; Yeganeh Safei; Adam Doupe; Gail-Joon Ahn; Brad Wardman; Gary Warner (2018). *Inside a phisher's mind: Understanding the anti-phishing ecosystem through phishing kit analysis*. 2018 APWG Symposium on Electronic Crime Research (eCrime). DOI: 10.1109/E
M: Analyse phishing kits' .htaccess cloaking and propose a URL classification scheme.
D: Phishing kits and URLs 2016-2017 (industry-sourced; not public).
E: Descriptive measurement
R: None quantitative in abstract.
F: Phishers track and evade anti-phishing infrastructure; URL type correlates with compromised infrastructure.
L: - Authors' stated limitations: n/a (abstract only). - My assessment: Tangential to URL classifiers.
G: n/a

### oest2020phishtime
C: Adam Oest, Yeganeh Safaei, Penghui Zhang, Brad Wardman, Kevin Tyers, Yan Shoshitaishvili, Adam Doupé, Gail-Joon Ahn (2020). PhishTime: Continuous Longitudinal Measurement of the Effectiveness of Anti-phishing Blacklists. *29th USENIX Security Symposium (USENIX
M: Controlled, longitudinal experiments measuring blacklist speed, coverage and consistency; reproduces evasion techniques seen in the wild
D: 2,862 researcher-deployed, innocuous PayPal-branded phishing sites across six deployments over nine months
E: Time-to-blacklist measurement per browser/platform; evasion vs. non-evasion arms
R: 2,862 sites launched; identifies a JavaScript/behaviour-based evasion that blacklists failed to detect; mobile protections lag desktop (abstract; Sec. 6-7).
F: Ground-truth sources such as blacklists are slow, inconsistent, and evasion-sensitive; the labels researchers harvest from them are therefore delayed and biased toward unevasive phish.
L: **Authors' stated:** Artificial sites; single brand; nine-month window. **Our caveats:** Implication for us: PhishTank-style labels over-represent the easy-to-detect phish, so our test set is easier than deployment traffic.
G: Label-source bias in phishing URL datasets is rarely quantified.

### oest2020sunrise
C: Adam Oest, Penghui Zhang, Brad Wardman, Eric Nunes, Jakub Burgis, Ali Zand, Kurt Thomas, Adam Doupé, Gail-Joon Ahn (2020). Sunrise to Sunset: Analyzing the End-to-end Life Cycle and Effectiveness of Phishing Attacks at Scale. *29th USENIX Security Symposium (U
M: Large-scale measurement of the phishing life cycle: deployment, email lure, victim visits, detection by the ecosystem, account compromise
D: One year of victim traffic to phishing pages impersonating a major financial brand (PayPal), via the 'Golden Hour' passive monitoring framework; 4.8M victim visits
E: Longitudinal measurement; timing analysis of campaign phases relative to blacklist detection
R: 4.8 million victims recorded in one year; average campaign lasts 21 hours from start to last victim; at least 7.42% of visitors submit credentials; a small set of campaigns causes 89.13% of victims (abstract, Sec. 1).
F: Phishing sites are extremely short-lived and most harm happens before blacklists react ('golden hour'); detection must be fast and must work on never-before-seen URLs/domains.
L: **Authors' stated:** Single brand/ecosystem vantage point; cloaking limits visibility. **Our caveats:** Not about ML evaluation per se, but its timing data undermines any evaluation that lets near-duplicate URLs of the same campaign sit in both train and test.
G: Evaluation protocols rarely simulate the 'first hours' regime where the model is the only defence.

### openphish
C: OpenPhish (2026). *OpenPhish Community Feed*. https://openphish.com/phishing_feeds.html. URL: https://openphish.com/phishing_feeds.html
M: n/a
D: Download: https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt . License: OpenPhish Terms of Use (community feed free, 'limited'). Timestamps: not in community text feed (only snapshot time). Labels: all phishing. Known problems: no timestamps/brand in free tier; short retention; was the phishing source of ISCX-URL-2016.
E: n/a
R: n/a
F: n/a
L: - Authors' stated limitations: n/a - My assessment: n/a
G: n/a

### ozcan2023hybrid
C: Ozcan, Alper; Catal, Cagatay; Donmez, Emrah; Senturk, Behcet (2023). *A hybrid DNN-LSTM model for detecting phishing URLs*. Neural Computing and Applications, 35(7), pp. 4957-4973 (online 2021). DOI: 10.1007/s00521-021-06401-z URL: https://doi.org/10.1007/s005
M: DNN branch over NLP features + LSTM over char embeddings, fused.
D: Phishing URL datasets (sizes not in abstract)
E: Not in abstract
R: Not in abstract ('outperform other models in accuracy'). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Hybrid feature+sequence model beats single-view models (authors).
L: - Stated by authors: Not available. - Our own caveats: No numbers verified.
G: n/a

### pendlebury2019tesseract
C: Feargus Pendlebury, Fabio Pierazzi, Roberto Jordaney, Johannes Kinder, Lorenzo Cavallaro (2019). TESSERACT: Eliminating Experimental Bias in Malware Classification across Space and Time. *28th USENIX Security Symposium (USENIX Security 19)*, pp. 729-746. arXiv
M: Evaluation framework; constraints C1 (temporal training consistency), C2 (temporal goodware/malware window consistency), C3 (realistic malware-to-goodware ratio in testing); new metric AUT (area under time); tuning algorithm for training class ratio; re-evaluation of three published classifiers (linear SVM on Drebin features, Random Forest on MaMaDroid Markov features, a deep net)
D: Android apps: ~129k samples (AndroZoo) spanning 2014-2016, labelled via VirusTotal (details Sec. 2.2); ~10% malware in realistic setting
E: Time-aware splits with monthly test periods over 24 months; compares 10-fold CV (biased) vs temporally consistent evaluation; varies malware ratio in train/test
R: With temporal bias removed, AUT(F1,24m) = 0.58 (ALG1), 0.32 (ALG2), 0.64 (DL), all lower than the 10-fold F1 reported in the original papers (Fig. 5, Sec. 4; p. 736 of proceedings). Realistic 10% malware ratio in train and test.
F: Random k-fold splits leak future knowledge (temporal bias) and unrealistic class ratios (spatial bias) jointly inflate reported malware-detection performance; sound evaluation needs time-ordered splits, realistic base rates and a time-decay metric; retraining/active learning only partially mitigates decay.
L: **Authors' stated:** Android-only evaluation; labelling via VirusTotal thresholds is noisy; ground-truth timestamps can be unreliable; dataset ends 2016. **Our caveats:** Phishing URLs have much shorter lifetimes than Android malware, so monthly windows may be too coarse; URL datasets commonly lack timestamps at all, making C1/C2 impossible to enforce without re-collection.
G: No TESSERACT-style constraint set exists for phishing URL datasets; most public URL corpora carry no first-seen timestamps.

### phishtank
C: Cisco Talos / OpenDNS (community) (2026). *PhishTank verified online phishing URL database*. https://phishtank.org/developer_info.php. URL: https://phishtank.org/developer_info.php
M: n/a
D: Download: http://data.phishtank.com/data/online-valid.{csv,json,xml}[.gz|.bz2] (optionally with app key). License: Cisco end-user licence terms (research use permitted under terms; redistribution restricted). Timestamps: YES (submission_time, verification_time, ISO 8601). Labels: all entries are community-verified phishing; target brand when known. Known problems: only 'online & valid' at dump time; survivorship bias
E: n/a
R: n/a
F: Only major public phishing source with per-URL timestamps.
L: - Authors' stated limitations: n/a - My assessment: Benign counterpart must be sourced separately (Tranco/Common Crawl), creating distribution artefacts.
G: n/a

### prasad2024phiusiil
C: Prasad, Arvind; Chandra, Shalini (2024). *PhiUSIIL: A diverse security profile empowered phishing URL detection framework based on similarity index and incremental learning*. Computers & Security, 136, 103545. DOI: 10.1016/j.cose.2023.103545 URL: https://doi.o
M: Computes URLSimilarityIndex, CharContinuationRate, TLDLegitimateProb and other URL/HTML-derived features; incremental learning to adapt to new data.
D: PhiUSIIL dataset (UCI #967, CC BY 4.0): 235,795 URLs (134,850 legitimate, 100,945 phishing), 54 features from URL and page source
E: Not retrievable (publisher page blocked); UCI page documents dataset only
R: Not retrieved. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Dataset is now a common benchmark (used by Yi 2026 and others).
L: - Stated by authors: Not retrieved. - Our own caveats: Dataset mixes URL and page-source features and some derived features (e.g., TLDLegitimateProb) risk label leakage; collection windows undocumented on UCI page.
G: Leakage audit of derived features.

### rao2020catchphish
C: Rao, Routhu Srinivasa; Vaishnavi, Tatti; Pais, Alwyn Roshan (2020). *CatchPhish: detection of phishing websites by inspecting URLs*. Journal of Ambient Intelligence and Humanized Computing, 11(2), pp. 813-825. DOI: 10.1007/s12652-019-01311-4 URL: https://doi.o
M: Hand-crafted hostname/URL features + TF-IDF features + phishing hint words; RF classifier.
D: Authors' dataset plus two benchmark datasets (names/sizes not on abstract page)
E: Not stated on abstract page
R: 93.25% (TF-IDF only) and 94.26% (TF-IDF + hand-crafted) on own data; 98.25% and 97.49% on two benchmark datasets (Springer abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Combining TF-IDF n-grams with hand-crafted lexical features improves RF accuracy.
L: - Stated by authors: Not available. - Our own caveats: Benchmark names unclear from abstract; no temporal test.
G: Cross-dataset evaluation.

### rashid2024domainadapt
C: Fariza Rashid, Ben Doyle, Soyeon Caren Han, Suranga Seneviratne (2024). Phishing URL detection generalisation using Unsupervised Domain Adaptation. *Computer Networks*, art. 110398. DOI: 10.1016/j.comnet.2024.110398
M: Unsupervised domain adaptation framework to transfer URL classifiers between datasets
D: Three phishing-URL datasets (abstract); pairwise cross-dataset experiments
E: Train on one dataset, test on another (cross-dataset F1), with and without adaptation
R: Cross-dataset F1 improves by 0.06 on average and up to about 0.2 with adaptation (abstract). Secondary reports (not verified from full text) attribute part of the baseline drop to URL-length shift and the classifiers' focus on specific tokens such as 'www'. (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Existing ML/DL URL detectors 'work effectively only when the test sets are split from the same training dataset'; format differences between collection vantage points (how URLs are recorded) are an explicit cause.
L: **Authors' stated:** Not visible from abstract. **Our caveats:** Full text not accessed; the 'www' token claim must be verified before citing it as the paper's finding.
G: Explains cross-dataset drops mechanistically (format artefacts) rather than only reporting them.

### roy2024phishlang
C: Sayak Saha Roy; Shirin Nilizadeh (2024). *PhishLang: A Real-Time, Fully Client-Side Phishing Detection Framework Using MobileBERT*. arXiv:2408.05667 (v3, Apr 2025); CC BY 4.0. URL: https://arxiv.org/abs/2408.05667
M: Fine-tune MobileBERT on URL and parsed source code; ensemble; ship as browser extension.
D: Author-crawled datasets (paper Sec. 3); sizes in paper.
E: Accuracy/precision/recall/F1 of nine language models; median inference time and memory (Table 2); comparison with anti-phishing tools; zero-day evaluation
R: MobileBERT accuracy 0.96 with precision 0.95 / recall 0.96, fastest among SLMs; Llama 2 F1 0.96 but much slower; memory per model ranges from 74 MB to 7,352 MB (paper Table 2).
F: Small transformer achieves near-LLM accuracy with far lower memory/latency; fully local operation is feasible.
L: - Authors' stated limitations: Transformer still heavier than classical models; relies on page source for best accuracy. - My assessment: No comparison with lexical gradient-boosting baselines on the same hardware.
G: Head-to-head latency/model-size of lexical ensembles vs. small transformers on identical URL sets.

### rudd2020training
C: Rudd, Ethan M.; Abdallah, Ahmed (2020). *Training Transformers for Information Security Tasks: A Case Study on Malicious URL Prediction*. arXiv preprint arXiv:2011.03040. URL: https://arxiv.org/abs/2011.03040 - Type: preprint | Theme (L1): d-transformer-llm | 
M: Auto-regressive pre-training on 20M unlabeled URLs does not transfer; adding an auxiliary auto-regressive loss while training from scratch (balanced dynamically) helps; compared with baselines.
D: FireEye URL corpus: 1,007,451 training, 111,930 validation (20,013 malicious, 91,813 benign), 279,874 test URLs; 20M unlabeled URLs for pre-training (Sec. 3)
E: Held-out split; ROC-AUC comparison (Fig. 2-3)
R: Mixed-objective transformer on par with the best baseline (1D CNN) by ROC-AUC (Fig. 3); numbers in figure legends. (Numbers taken from the full text; section/table references given where identified.)
F: Generic NLP pre-training recipes do not transfer directly to URLs; char-CNNs remain a strong baseline.
L: - Stated by authors: Proprietary data; limited pre-training scale. - Our own caveats: Not peer reviewed.
G: Public pre-training corpora for URLs.

### sabir2022reliability
C: Bushra Sabir, M. Ali Babar, Raj Gaire, Alsharif Abuadbba (2022). Reliability and Robustness analysis of Machine Learning based Phishing URL Detectors. *IEEE Transactions on Dependable and Secure Computing*. DOI: 10.1109/TDSC.2022.3218043; arXiv: 2005.08454
M: Methodology to test reliability and robustness: adversarial URL generator (URLBUG), reproduction of 50 traditional-ML and DL detectors, evaluation on Advdata
D: Reproduces 50 ML phishing-URL detectors; phishing URLs from PhishTank/OpenPhish/ISCXURL2016/PhishStorm (96,693); legitimate URLs crawled from 1,500 Alexa domains to obtain full paths; adversarial set 'Advdata' generated by URLBUG
E: Baseline (balanced, in-distribution) vs adversarial URLs; MCC as main metric; registration-cost and real-world-use analysis of adversarial domains
R: Median MCC falls from 0.92 (baseline) to 0.02 on Advdata; adversarial domains registrable at a median $11.99/yr; 63.94% of already-registered ones were used maliciously (abstract).
F: State-of-the-art URL detectors are brittle; the training vocabulary is biased toward phishing target brand tokens. Explicitly notes that using Alexa index pages as the legitimate class 'creates a bias in the data' because phishing feeds provide full URLs while Alexa provides only index pages.
L: **Authors' stated:** Adversarial generation is heuristic; reproduction may not match original hyper-parameters. **Our caveats:** Baseline evaluation remains balanced and random-split; no domain grouping.
G: Combining robustness testing with artefact ablation and domain-grouped splits.

### sahingoz2019ebbu2017
C: Ozgur Koray Sahingoz; Ebubekir Buber; Onder Demir; Banu Diri (2019). *Machine learning based phishing detection from URLs*. Expert Systems with Applications 117:345-357. DOI: 10.1016/j.eswa.2018.09.029 URL: https://doi.org/10.1016/j.eswa.2018.09.029
M: Extract NLP word-based features from URL tokens; compare with word-vector features; evaluate seven classifiers.
D: Ebbu2017. Download: https://github.com/ebubekirbbr/pdd/tree/master/input . License: none stated in repo listing. Timestamps: none. Labels: phishing (PhishTank-sourced) vs legitimate (Yandex search-derived, per commonly cited description - not verified here). Known problems: 2017 vintage; counts inferred from file names.
E: Hold-out; accuracy
R: RF with only NLP features: 97.98% accuracy (abstract).
F: Word-level lexical features suffice for high accuracy with low latency.
L: - Authors' stated limitations: n/a (abstract). - My assessment: Dataset small and old; no timestamps.
G: n/a

### sahingoz2019machine
C: Sahingoz, Ozgur Koray; Buber, Ebubekir; Demir, Onder; Diri, Banu (2019). *Machine learning based phishing detection from URLs*. Expert Systems with Applications, 117, pp. 345-357. DOI: 10.1016/j.eswa.2018.09.029 URL: https://doi.org/10.1016/j.eswa.2018.09.029 
M: Word-level tokenisation of URLs; 'NLP features' (brand/keyword, random-word, digit/length statistics), word vectors and hybrid sets; compares seven classifiers.
D: Ebbu2017: 73,575 URLs (36,400 legitimate via Yandex queries, 37,175 phishing from PhishTank) - figures as reported by Sanchez-Paniagua 2022 and DEPHIDES 2024, which reuse the set
E: Not confirmed from full text
R: 97.98% accuracy with RF on NLP features (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Random Forest on NLP-style lexical features performs best; dataset released and widely reused.
L: - Stated by authors: Not available. - Our own caveats: Legitimate URLs from Yandex search results (deeper pages) vs PhishTank; later work (Sanchez-Paniagua 2022) shows models trained on this era degrade on 2020 data.
G: Temporal validity; artifact analysis.

### sahingoz2024dephides
C: Sahingoz, Ozgur Koray; Buber, Ebubekir; Kugu, Emin (2024). *DEPHIDES: Deep Learning Based Phishing Detection System*. IEEE Access, 12, pp. 8052-8070. DOI: 10.1109/ACCESS.2024.3352629 URL: https://doi.org/10.1109/ACCESS.2024.3352629 - Type: journal | Theme (L1)
M: Character vectorisation of URLs; five architectures compared; extensive related-work table of datasets.
D: About 5.1M URLs (shared on GitHub ebubekirbbr/dephides): 2,320,893 phishing (PhishTank up to Aug 2018) + legitimate URLs crawled (about 30 per domain) from top-100k domains; 'small' 10% subsample 232,090 phishing / 288,195 legitimate (Sec. IV)
E: Random train/test splits on small and full datasets
R: CNN best with 98.74% accuracy (abstract; Sec. V). (Numbers taken from the full text; section/table references given where identified.)
F: CNN > RNN/attention variants at this scale; dataset released.
L: - Stated by authors: Phishing data up to 2018; legitimate URLs crawled from top domains. - Our own caveats: Random splits with about 30 URLs per legitimate domain almost guarantee domain overlap between train and test (domain-grouped split needed).
G: Domain-grouped and temporal evaluation.

### sahoo2017survey
C: Sahoo, Doyen; Liu, Chenghao; Hoi, Steven C. H. (2017). *Malicious URL Detection using Machine Learning: A Survey*. arXiv preprint arXiv:1701.07179 (v3, 2019). URL: https://arxiv.org/abs/1701.07179 - Type: preprint | Theme (L1): a-foundational-lexical | Access:
M: Defines the learning problem, surveys feature families and learning algorithms, discusses system design and open challenges.
D: Survey (no new data); reviews datasets up to 2.4M URLs (Ma et al.)
E: n/a (survey)
R: n/a (Numbers taken from the full text; section/table references given where identified.)
F: Lexical BoW features scale best; online learning suits drift; deep representation learning was emerging (precursor to URLNet).
L: - Stated by authors: Points out lack of large public benchmarks, concept drift, adversarial evasion, and short-lived URLs (open-challenges section). - Our own caveats: Pre-dates transformers; benchmark discussion dated.
G: Standardised benchmarks and temporal evaluation protocols.

### sameen2020phishhaven
C: Sameen, Maria; Han, Kyunghyun; Hwang, Seong Oun (2020). *PhishHaven-An Efficient Real-Time AI Phishing URLs Detection System*. IEEE Access, 8, pp. 83425-83443. DOI: 10.1109/ACCESS.2020.2991403 URL: https://doi.org/10.1109/ACCESS.2020.2991403 - Type: journal | 
M: Lexical feature extraction with HTML-encoding decoding; ensemble of ML models with unbiased voting; multi-threaded execution; URL-Hit expands shortened URLs.
D: 100,000 URLs: 50,000 Alexa benign + 50,000 DeepPhish AI-generated phishing (Sec. VI, Table 4); plus 50,000 PhishTank 'simple' phishing (collected by 4 Sep 2019)
E: 5:5 split ratio train/test (Sec. VI); theoretical analysis
R: 98.00% accuracy and F1 about 98% on the 100k set; 97% TPR, 99.17% TNR, 0.8% FPR (Sec. VII, Tables 7-9). (Numbers taken from the full text; section/table references given where identified.)
F: Lexical ensembles can separate DeepPhish-generated URLs from Alexa benign URLs with high accuracy.
L: - Stated by authors: Tiny-URL handling needs expansion service; '100% on future AI URLs' claim is theoretical (Sec. V). - Our own caveats: Benign = Alexa homepages vs long generated URLs: a strong length/structure shortcut; random split only.
G: Realistic benign class and temporal validation.

### sanchezpaniagua2022phishing
C: Sanchez-Paniagua, Manuel; Fidalgo Fernandez, Eduardo; Alegre, Enrique; Al-Nabki, Wesam; Gonzalez-Castro, Victor (2022). *Phishing URL Detection: A Real-Case Scenario Through Login URLs*. IEEE Access, 10, pp. 42949-42960. DOI: 10.1109/ACCESS.2022.3168681 URL: h
M: Builds PILU-90K; compares 8 classical learners on handcrafted features, TF-IDF+LR, and two char-CNNs; measures accuracy decay over time and clusters phishing domains.
D: PILU-90K (public): 30K legitimate homepage URLs (Quantcast top sites), 30K legitimate login URLs, 30K phishing URLs (PhishTank); plus older sets (Ebbu2017, PWD2016, 2009-2017 data) for temporal tests (Sec. III, Tables 1,3,4)
E: Train on homepage-vs-phishing then test on legitimate login URLs (FPR stress test); temporal: train on 2016 data, test on 2020 data (Table 7); random splits within PILU
R: Models trained on PIU-60K (homepages) lose 27-39% accuracy on legitimate login URLs (best 69.50%, SVM 54.46%) (Sec. V-A, Fig. 4); TF-IDF + LR reaches 96.50% in the login scenario (abstract, Table 6); accuracy of 2016-trained models decreases on 2020 URLs (Table 7). (Numbers taken from the full text; section/table references given where identified.)
F: Benign-class composition is a major shortcut; URL length separability largely disappears when login URLs are used (Fig. 3); models age quickly.
L: - Stated by authors: Dataset limited to top-site login pages; deep models not exhaustively tuned. - Our own caveats: Still a random split within year; no domain-grouped split.
G: Domain-grouped and calibrated evaluation; artifact quantification (https/www).

### sankaranarayanan2024ensemble
C: Sankaranarayanan, Suresh; Sivachandran, Arvinthan Thevar; Mohd Khairuddin, Anis Salwa; Hasikin, Khairunnisa; Wahab Sait, Abdul Rahman (2024). *An ensemble classification method based on machine learning models for malicious Uniform Resource Locators (URL)*. PL
M: Lexical feature extraction; individual boosted/bagged trees; stacking meta-learner; hyperparameter tuning.
D: Kaggle 'malicious-urls-dataset' (sid321axn): 651,191 URLs; 4 classes benign/defacement/phishing/malware (Sec. 3)
E: Stratified 80/20 train/test split (Sec. 3.2.3); no cross-dataset
R: Individual accuracies 93.6% (RF), 95.2% (XGB), 95.7% (LGBM), 94.8% (CatBoost); stacking average accuracy 96.8%; per-class precision 91-99%, recall 87-99% (abstract; Sec. 4). (Numbers taken from the full text; section/table references given where identified.)
F: Stacking adds about 1 point over the best single booster on lexical features.
L: - Stated by authors: Lexical features only; short-lived URLs (Sec. 2). - Our own caveats: Kaggle aggregate dataset mixes sources (ISCX, PhishStorm, PhishTank...) so class is partly predictable from source formatting; random split only.
G: Source-aware / cross-dataset evaluation and calibration.

### saxe2017expose
C: Saxe, Joshua; Berlin, Konstantin (2017). *eXpose: A Character-Level Convolutional Neural Network with Embeddings For Detecting Malicious URLs, File Paths and Registry Keys*. arXiv preprint arXiv:1702.08568. URL: https://arxiv.org/abs/1702.08568 - Type: preprin
M: Embeds characters (dim 32), parallel convolutions of several kernel sizes, sum pooling, dense layers; trained on raw URL strings.
D: Invincea/VirusTotal-derived URLs (counts in Table 1; URLs with 1-4 AV detections discarded), plus file paths and registry keys
E: Held-out split with low-FPR ROC analysis (FPR 1e-4 to 1e-2) (Sec. 4)
R: 5-10% detection-rate gain over manual-feature baselines at 0.1% FPR (abstract); about 6% higher at FPR 1e-3 for URLs (Sec. 4, Fig. 3). (Numbers taken from the full text; section/table references given where identified.)
F: Char-CNN beats hashed n-gram baselines on URLs at low FPR.
L: - Stated by authors: Labels derived from AV engine counts (noisy); not peer reviewed. - Our own caveats: Dataset proprietary; no cross-dataset test.
G: Public reproducibility.

### scheitle2018toplists
C: Quirin Scheitle, Oliver Hohlfeld, Julien Gamba, Jonas Jelten, Torsten Zimmermann, Stephen D. Strowes, Narseo Vallina-Rodriguez (2018). A Long Way to the Top: Significance, Structure, and Stability of Internet Top Lists. *Proceedings of the Internet Measurement
M: Structural and stability analysis of top lists and their effect on research results
D: Alexa, Umbrella, Majestic lists; survey of list use in measurement/security papers
E: Repeats several published measurements with different lists/dates to show result sensitivity
R: Demonstrates that list choice and date materially change research conclusions (Sec. 6).
F: Top lists differ strongly in structure (e.g., Umbrella contains many non-web hosts) and churn; results that depend on them are fragile.
L: **Authors' stated:** Measurement scope. **Our caveats:** Relevance is indirect: it quantifies how arbitrary the 'legitimate' class becomes when sourced from a list.
G: N/A

### siddhartha2021maliciousurls
C: Manu Siddhartha (Kaggle user sid321axn) (2021). *Malicious URLs dataset (Kaggle: 'Huge dataset of 6,51,191 Malicious URLs')*. Kaggle dataset. URL: https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset
M: Concatenation of public lists keeping only URL and class.
D: Download: Kaggle page above (malicious_phish.csv; requires Kaggle login). License: not confirmed (Kaggle pages commonly show CC0/unknown - verify on page). Timestamps: none. Labels: type in {benign, defacement, phishing, malware}; binary tasks usually map benign vs rest. Known problems: duplicates across sources; many URLs lack scheme; defacement class comes from ISCX Alexa-ranked compromised sites; source-specific f
E: n/a
R: n/a
F: Most widely used multi-class URL corpus on Kaggle; our ~250k binary dataset likely derives from or overlaps with it.
L: - Authors' stated limitations: n/a - My assessment: Provenance only partially documented; no per-URL dates; label noise unknown.
G: A documented, timestamped, de-duplicated version with source column.

### sommer2010closedworld
C: Robin Sommer, Vern Paxson (2010). Outside the Closed World: On Using Machine Learning for Network Intrusion Detection. *2010 IEEE Symposium on Security and Privacy*. DOI: 10.1109/SP.2010.25
M: Analysis of why ML anomaly detection is rarely deployed: high cost of errors, semantic gap, diversity of traffic, difficulty of sound evaluation, adversarial setting
D: Position paper; no dataset
E: Recommends evaluation with realistic data, understanding of what the system learns, and attention to false-positive cost
R: None. (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Closed-world assumptions and lack of insight into learned features produce systems that look good in the lab and fail in deployment.
L: **Authors' stated:** NID-specific. **Our caveats:** The 'semantic gap' maps to our model learning 'looks like a popular www/https site' instead of 'is legitimate'.
G: N/A

### tajaddodianfar2020texception
C: Tajaddodianfar, Farid; Stokes, Jack W.; Gururajan, Arun (2020). *Texception: A Character/Word-Level Deep Learning Model for Phishing URL Detection*. ICASSP 2020 - IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 2857-2861. DOI: 10.
M: Character path and word path with parallel convolution blocks (Inception-like), concatenated, dense output; compared with a traditional text classifier and a URLNet baseline.
D: Microsoft production telemetry: six weeks of data; first two weeks -> 1.7M training samples (benign down-sampled to 5% positives); test set 20M instances sampled from production (Sec. 2)
E: Temporal: train on first 2 weeks, test on later production data; TPR at fixed 0.01% FPR (Table 2)
R: TPR increased by 126.7% relative to a traditional text classifier at 0.01% FPR (abstract; Table 2 lists TP and error rates at fixed 0.01% FPR, e.g. Baseline_URLNet 12.3% TP). (Numbers taken from the full text; section/table references given where identified.)
F: Char/word parallel-CNN generalises better to new URLs than classical text classification at production FPRs.
L: - Stated by authors: Proprietary data; production labels. - Our own caveats: Not reproducible; absolute TPRs are low at 0.01% FPR, showing how hard low-FPR operation is.
G: Public low-FPR benchmarks.

### tang2021survey
C: Lizhen Tang, Qusay H. Mahmoud (2021). A Survey of Machine Learning-Based Solutions for Phishing Website Detection. *Machine Learning and Knowledge Extraction*, pp. 672-694. DOI: 10.3390/make3030034
M: Comparative review of ML solutions, features, datasets and reported accuracies
D: Survey; tabulates datasets (UCI, Mendeley, ISCXURL-2016, PhishTank/OpenPhish + Alexa/Common Crawl crawls)
E: Notes that many solutions report >99% accuracy on single datasets; Table 5 lists 'did not use multiple different datasets to train the model, compare the results' as a limitation
R: Qualitative; reported accuracies 98-99.6% across surveyed works (Table 5).
F: Single-dataset evaluation and reliance on PhishTank + Alexa/Common Crawl sources are the norm.
L: **Authors' stated:** Breadth over depth. **Our caveats:** Does not analyse artefacts or base rates.
G: N/A

### tian2018needle
C: Ke Tian; Steve T. K. Jan; Hang Hu; Danfeng Yao; Gang Wang (2018). *Needle in a Haystack: Tracking Down Elite Phishing Domains in the Wild*. Proceedings of the Internet Measurement Conference 2018 (IMC '18), Boston, MA. DOI: 10.1145/3278532.3278569 URL: https:/
M: Enumerate five squatting types for 702 brands, scan 224M DNS records, classify pages with visual+OCR features, verify manually.
D: DNS zone data and crawled pages (2017-2018); not released as a URL benchmark.
E: Precision via manual verification; blacklist evasion measured over time
R: 657K candidate squatting domains; 1,175 verified squatting phishing pages; >90% evaded popular blacklists for at least a month (abstract).
F: Squatting phishing is long-lived and under-blacklisted; domain-level impersonation is a core evasion tactic.
L: - Authors' stated limitations: Brand list limited to 702; manual verification bottleneck. - My assessment: Content-based detector; our lexical model must rely on domain string cues.
G: Squatting-aware lexical features (brand-in-domain edit distance) under controlled mutation.

### tian2025survey
C: Tian, Ye; Yu, Yanqiu; Sun, Jianguo; Wang, Yanbin (2025). *From Past to Present: A Survey of Malicious URL Detection Techniques, Datasets and Code Repositories*. arXiv preprint arXiv:2504.16449 (v2, under review at Computer Science Review). URL: https://arxiv.o
M: Reviews blacklists -> classical ML -> deep learning -> LLM prompting/agents; tabulates datasets and reported accuracies.
D: Survey: catalogues public datasets 2016-2024 and open-source implementations 2013-2025 (GitHub list)
E: n/a (survey)
R: n/a (Numbers taken from the full text; section/table references given where identified.)
F: Notes lack of proper baselines and standardised benchmarks; many works report >99% on small sets.
L: - Stated by authors: Preprint under review. - Our own caveats: Accuracy tables are copied from papers without protocol normalisation.
G: Standard benchmarks and protocol reporting.

### tiwari2020phishingsiteurls
C: Tarun Tiwari (Kaggle user taruntiwarihp) (2020). *Phishing Site URLs (Kaggle: 'Malicious and Phishing attacks ulrs')*. Kaggle dataset. URL: https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls
M: n/a
D: Download: Kaggle page (phishing_site_urls.csv). License: not confirmed. Timestamps: none. Labels: 'good'/'bad'. Known problems: undocumented provenance; heavy duplication reported by users; many URLs lack scheme.
E: n/a
R: n/a
F: n/a
L: - Authors' stated limitations: n/a - My assessment: Provenance unknown - weak as an external benchmark.
G: n/a

### trad2024prompt
C: Trad, Fouad; Chehab, Ali (2024). *Prompt Engineering or Fine-Tuning? A Case Study on Phishing Detection with Large Language Models*. Machine Learning and Knowledge Extraction, 6(1), pp. 367-384. DOI: 10.3390/make6010018 URL: https://doi.org/10.3390/make6010018
M: Multiple prompt strategies on chat models; fine-tuning of small base LLMs for binary URL classification; comparison with prior results on the same dataset (Table 3).
D: Hannousse & Yahiouche Mendeley dataset: 11,430 URLs (balanced); 1,000-sample balanced test subset (500/500); remaining 10,430 for fine-tuning (Sec. 4)
E: Fixed 1,000 test subset; also varying phishing ratio experiments (Fig. 8-10)
R: Best prompting F1 92.74% (Claude 2); fine-tuned gpt2-medium F1 97.29%, AUC 99.56% (abstract; Sec. 5); at low phishing ratios GPT-2 F1 76.19%/86.73% vs Claude 2 59.15%/74.58% (Sec. 5.3). (Numbers taken from the full text; section/table references given where identified.)
F: Fine-tuned small LLMs beat prompted frontier chat models; prompted models degrade under class imbalance.
L: - Stated by authors: Small test set (1,000); single dataset (Sec. 6). - Our own caveats: Dataset is small; results may not transfer to 250k-scale data.
G: Larger, temporally split LLM evaluations.

### trikilis2026reasoning
C: Trikilis, Holly; Marasinghe, Pasindu; Rashid, Fariza; Seneviratne, Suranga (2026). *Eliciting Least-to-Most Reasoning for Phishing URL Detection*. arXiv preprint arXiv:2601.20270 (short paper). URL: https://arxiv.org/abs/2601.20270 - Type: preprint | Theme (L1
M: Decomposes URL judgement into sub-questions, iterates, uses answer-sensitivity to trigger re-reasoning.
D: HP, EBBU (Ebbu2017) and ISCX-URL-2016; random balanced 1,000-URL test subsets, 5 repetitions (Sec. 3)
E: Mean F1 over 5 random 1,000-URL draws per dataset (Table 1)
R: Least-to-Most average F1 0.9040 vs 0.8726 one-shot across models/datasets; Gemini best at 0.9621 average F1; URLTran supervised about 0.99 F1 (Table 1). (Numbers taken from the full text; section/table references given where identified.)
F: Prompted LLMs approach but do not reach supervised transformers; reasoning prompts help smaller models most.
L: - Stated by authors: Small test subsets; API cost. - Our own caveats: Not peer reviewed; 1,000-URL subsets give wide confidence intervals.
G: Cost-aware comparison with lightweight models.

### urlhaus
C: abuse.ch / Spamhaus (2026). *URLhaus (abuse.ch) malware URL feed*. https://urlhaus.abuse.ch/api/. URL: https://urlhaus.abuse.ch/api/
M: n/a
D: Download: https://urlhaus-api.abuse.ch/v2/files/exports/<AUTH-KEY>/recent.csv (and full/active variants). License: abuse.ch terms of use, free under fair use; commercial API paid. Timestamps: dumps are known to include a date-added field, but this was not verified on the fetched page. Labels: malware distribution URLs (threat type, tags), not phishing. Known problems: label semantics differ from phishing; many URLs a
E: n/a
R: n/a
F: n/a
L: - Authors' stated limitations: n/a - My assessment: Malware != phishing; mixing shifts the task definition.
G: n/a

### verma2015character
C: Verma, Rakesh; Dyer, Keith (2015). *On the Character of Phishing URLs: Accurate and Robust Statistical Learning Classifiers*. Proceedings of the 5th ACM Conference on Data and Application Security and Privacy (CODASPY '15), pp. 111-122. DOI: 10.1145/2699026.26
M: Adds distributional features: KS statistic between URL character distribution and reference distributions, plus classic lexical features; evaluates several learners.
D: Phishing (PhishTank) and legitimate URLs; sizes not in abstract
E: Not in abstract
R: 99.3% accuracy with FPR < 0.4% (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Character-level statistics boost accuracy over token-only lexical features.
L: - Stated by authors: Not available. - Our own caveats: Very high accuracy likely dataset-dependent; no cross-dataset evidence.
G: Robustness claims untested over time.

### verma2017whatsinaurl
C: Rakesh Verma; Avisha Das (2017). *What's in a URL: Fast Feature Extraction and Malicious URL Detection*. Proceedings of the 3rd ACM International Workshop on Security and Privacy Analytics (IWSPA '17), pp. 55-63. DOI: 10.1145/3041008.3041016 URL: https://doi.o
M: Design lexical/character n-gram features computable in linear time; evaluate several classifiers.
D: Not verified (abstract unavailable).
E: Classification accuracy and feature-extraction speed
R: Not verified.
F: URL-only features allow fast, accurate detection (per title/abstract framing).
L: - Authors' stated limitations: n/a - My assessment: Older datasets; no robustness analysis.
G: n/a

### wang2019pdrcnn
C: Wang, Weiping; Zhang, Feng; Luo, Xi; Zhang, Shigeng (2019). *PDRCNN: Precise Phishing Detection with Recurrent Convolutional Neural Networks*. Security and Communication Networks, 2019, Article 2595794, pp. 1-15. DOI: 10.1155/2019/2595794 URL: https://doi.org/
M: URL encoded as 2-D tensor; BiLSTM extracts global features; CNN selects key characters; fixed-length vector -> classifier.
D: Nearly 500,000 URLs from Alexa (benign) and PhishTank (phishing) (abstract)
E: Not in abstract
R: Accuracy 97%, AUC 99%, 0.4 ms per URL (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: RNN+CNN hybrid beats either alone.
L: - Stated by authors: Not available. - Our own caveats: Alexa-vs-PhishTank construction (homepage shortcut).
G: Realistic benign class.

### wang2023phishbert
C: Wang, Yanbin; Zhu, Weifan; Xu, Haitao; Qin, Zhan; Ren, Kui; Ma, Wenrui (2023). *A Large-Scale Pretrained Deep Model for Phishing URL Detection*. ICASSP 2023 - IEEE International Conference on Acoustics, Speech and Signal Processing, pp. 1-5. DOI: 10.1109/ICASS
M: URL-specific pre-training (3B+ URLs), adversarial fine-tuning for classification.
D: More than 3 billion unlabeled URLs for pre-training; labelled benign/malicious URL benchmarks (sizes not in abstract)
E: Not in abstract ('extensive and rigorous benchmark studies')
R: None in abstract ('significantly superior ... efficiency, robustness and accuracy'). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: URL-domain pre-training beats text-pretrained transfer (authors).
L: - Stated by authors: Not available. - Our own caveats: No public weights located; not reproducible for us.
G: Open URL foundation models.

### wei2020accurate
C: Wei, Wei; Ke, Qiao; Nowak, Jakub; Korytkowski, Marcin; Scherer, Rafal; Wozniak, Marcin (2020). *Accurate and fast URL phishing detector: A convolutional neural network approach*. Computer Networks, 178, 107275. DOI: 10.1016/j.comnet.2020.107275 URL: https://do
M: Char-CNN sized for mobile inference.
D: Not in abstract (phishing/legitimate URL text)
E: Not in abstract
R: 'Almost 100% accuracy' (abstract) - no precise figures retrieved. (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Char-CNN sufficient and fast.
L: - Stated by authors: Not available. - Our own caveats: Near-perfect accuracy claims suggest easy/biased data.
G: Realistic evaluation.

### yi2026crossdataset
C: Yi, Liyan; Omotosho, Adebayo; Balogun, Hamed (2026). *Phishing URL Detection and Interpretability With Machine Learning: A Cross-Dataset Approach*. Security and Privacy (Wiley), 9(1), e70175. DOI: 10.1002/spy2.70175 URL: https://doi.org/10.1002/spy2.70175 - Ty
M: Trains three tree ensembles; evaluates on secondary datasets; SHAP for feature attribution.
D: Primary email-URL dataset plus secondary/test datasets (four test sets in total; names not in abstract)
E: Cross-dataset: train on primary set, evaluate on four secondary test sets
R: Across four test sets: average classification error 4.03%, average accuracy 94% (abstract). (Only abstract/publisher-page information was available; no additional numbers should be attributed to this paper without checking the full text.)
F: Tree ensembles with a common lexical feature set transfer reasonably across datasets; SHAP highlights consistent key features.
L: - Stated by authors: Not available. - Our own caveats: Abstract-level only; cannot verify whether test sets share sources with training data.
G: Domain-grouped splits, calibration, artifact analysis.

### zeng2020phishbench
C: Victor Zeng, Shahryar Baki, Ayman El Aassal, Rakesh M. Verma, Luis Felipe Teixeira De Moraes, Avisha Das (2020). Diverse Datasets and a Customizable Benchmarking Framework for Phishing. *Proceedings of the Sixth International Workshop on Security and Privacy A
M: Benchmarking framework (PhishBench) for features and classifiers
D: Diverse phishing email, website and URL datasets released with PhishBench
E: Framework supports metrics beyond accuracy and imbalanced evaluation
R: None in abstract. (Full text not accessed; numbers restricted to the abstract/landing page.)
F: Researchers 'usually test their proposed methods with limited metrics, datasets, and parameters'; a common benchmark is needed.
L: **Authors' stated:** Workshop paper. **Our caveats:** Datasets are 2019-2020 and website-heavy.
G: A maintained URL benchmark with leakage controls.

### zieni2023survey
C: Rasha Zieni, Luisa Massari, Maria Carla Calzarossa (2023). Phishing or Not Phishing? A Survey on the Detection of Phishing Websites. *IEEE Access*, pp. 18499-18519. DOI: 10.1109/ACCESS.2023.3247135
M: Structured review of features, selection, algorithms, metrics
D: Survey of list-based, similarity-based and ML-based detection; dataset sources (PhishTank, OpenPhish, Alexa, DMOZ, Google queries)
E: Notes that Alexa retired in May 2022 and DMOZ was discontinued, that datasets 'often share the data sources' yet differ in content, and highlights work demonstrating 'the importance of taking precisely into account the imbalanced nature of phishing attacks'
R: Qualitative.
F: Benign data provenance (Alexa/DMOZ) is fragile and the imbalanced nature of the problem is under-addressed.
L: **Authors' stated:** Survey. **Our caveats:** No explicit artefact discussion.
G: N/A
