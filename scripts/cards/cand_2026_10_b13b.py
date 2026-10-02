"""候補 Issue #2(ドリフト検知)で承認された論文のうち、バッチ cand_2026_10_b13b の7本のカード(arXiv 論文)。
各論文の主張と評価方法(データ・正解ドリフト点の作り方・比較手法と設定・しきい値の決め方)の記述を記録する。結果表の数値は記録しない。
書誌(タイトル・著者・版・年)は scratchpad の batches/cand_2026_10_b13b.json(arXiv API の値)をそのまま書き写した。
7本のうち 2610.00649 / 2609.39473 / 2609.35703 / 2609.33940 はドリフト検知そのものではない(分布シフト下の頑健性・OOD・失敗予測)。"""

import sys

sys.path.insert(0, "scripts/cards")
from _spec_builder import build  # noqa: E402

SPECS = [
  {"id": "arxiv-2608.16659",
   "title": "Hoeffding adaptive splitting trees for data stream classification with concept drift and ensemble learning",
   "authors": ["Daniel Nowak Assis", "Jean Paul Barddal", "Fabrício Enembreck"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2608.16659"},
   "tasks": ["stream-classification"], "fam": ["tree-ensembles", "random-forests", "error-rate-drift-detectors"],
   "par": ["supervised", "streaming"],
   "proposes": ["Hoeffding Adaptive Splitting Trees (HLAST, EFLAST): incremental trees that split both periodically (Hoeffding bound) and when a leaf change detector fires, used as ensemble base learners"],
   "claims": [
     ("Main claim: the proposed Hoeffding Adaptive Splitting Trees improve ensemble performance and achieve state-of-the-art results in an evaluation covering benchmark comparisons, computational cost and concept drift adaptation.", "Abstract",
      "Experimental results demonstrate that Hoeffding Adaptive Splitting Trees enhance ensemble performance and achieve state-of-the-art results across a comprehensive evaluation, including benchmark comparisons, computational cost analysis, and concept drift adaptation."),
     ("Data: 13 real-world streams and 24 synthetic streams (AGRAWAL, SEA, LED, RBF, HYPER generators); in the synthetic streams drift is simulated by the generator (e.g. switching concept functions), so drift positions are known by construction.", "Methodology",
      "We performed experiments with 13 real-world datasets made available in [32] and 24 synthetic datasets retrieved from [33]."),
     ("Ensemble hyperparameters were not tuned: all ensembles (100 base learners) used the MOA default parameters.", "Methodology",
      "All parameters from ensembles were set to default as implemented in the MOA framework."),
     ("Evaluation protocol: prequential (test-then-train) evaluation, with metrics averaged over 20 evenly spaced points of the stream; ensembles are compared with a Friedman test and Holm-corrected Wilcoxon post-hoc tests.", "Methodology",
      "As in [7], we assess the predictive performance obtained with a test-then-train validation strategy, where every instance is used first for testing and then for training, known as Prequential evaluation [40]."),
     ("The change detector inside all LAST-type trees is HDDM_A, chosen from the authors' earlier detector comparison, where HDDM_A, MDDM_A and ADWIN performed comparably and were cheaper than DDM-type detectors.", "Methodology",
      "The detector used in all LAST versions was HDDMA [44], given the analysis done in [6]."),
     ("On synthetic drifting streams the proposed trees have little effect relative to a Hoeffding Tree; the gains appear mainly on real-world, multi-class data.", "Results",
      "Figure 6 shows that on synthetic data the proposed trees have little effect, with the F1-Score difference to HT staying close to zero for all ensembles."),
   ],
   "notes": "Stream classification with drift adaptation, not a drift-detector benchmark: change detectors are used inside tree leaves to trigger splits and in ensembles (ARF/SRP/ARTE) for resets; no detection metrics (delay, false alarms, missed detections) are reported. Drift reaction is assessed only by F1-Score curves over time with the known drift points of the synthetic streams marked; the drift type of most real-world streams is listed as Unknown (INSECTS variants are labeled abrupt/incremental/gradual). "
            "Detector parameter settings beyond the HDDM_A choice were not found in the text. Tuning the base learners' hyperparameters is listed as future work. SGBT was excluded for computational cost. "
            "The authors also proposed LAST (the main adaptive baseline) in earlier work. Code/results site in the PDF: https://sites.google.com/view/last-ensemble (not added to links because it is not a code repository URL)."},

  {"id": "arxiv-2608.08245",
   "title": "Privacy-Preserving Data Drift Detection and Recovery for Large-Scale LLM Applications via Proxy Representations",
   "authors": ["Michael Levit", "Josh Ledgard", "Haoyu Dong", "Vishwas Suryanarayanan", "Eyal Kolman", "Sharon Tan", "Qiang Gan", "Vishal Chowdhary"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2608.08245"},
   "tasks": ["dataset-shift-detection"], "fam": ["dimensionality-reduction-for-shift", "large-language-models"], "par": ["unsupervised"],
   "proposes": ["ProxyDrift: drift measurement between production traffic and offline evaluation sets on LLM-classified non-PII proxy descriptors",
                "Chance-calibrated, redundancy-aware (RA) alignment score", "Chow-Liu tree conditional sampler for synthetic evaluation proxies"],
   "claims": [
     ("ProxyDrift identifies and measures drift between production traffic and offline evaluation sets, and builds/refreshes those sets, without access to raw user data.", "Abstract",
      "We present PROXYDRIFT, a framework that (i) identifies and measures drift between production traffic and offline evaluation sets, and (ii) constructs and refreshes those evaluation sets accordingly; all without access to raw user data."),
     ("Per-dimension drift is measured with the Jensen-Shannon distance on categorical proxy distributions, chosen because it reacts strongly to support mismatches; it is then chance-calibrated against a permutation baseline.", "Drift Measurement",
      "Among several candidate distance metrics (Total Variation, Wasserstein, Euclidean, ...), we selected Jensen–Shannon distance (JSD) as the default for categorical distributions because it reacts strongly to support mismatches."),
     ("Decision bands are fixed, not learned: the alignment range is split into equal thirds (bad / average / good); dimension importance weights are set by domain experts.", "Drift Measurement",
      "we use equal thirds (bad < 1/3, average ≥1/3, good ≥2/3) uniformly throughout the paper."),
     ("Drift evaluation setup: one week of production traffic is the reference, against which two synthetic samplers and the legacy hand-curated test set are scored; there are no labeled drift events.", "Evaluation (end-to-end drift alignment)",
      "Reference distributions were computed from a week of production traffic (2026-04-02 to 2026-04-08)."),
     ("The legacy hand-curated offline test set is poorly aligned with production on most dimensions; the paper adds that quality scores were lower on a distribution-aligned synthetic set and says this suggests score inflation in conventional offline evaluation.", "Evaluation (end-to-end drift alignment)",
      "By contrast, the legacy hand-curated test set fails on most dimensions, with individual per-dimension alignment scores typically below 0.40 and the overall alignment score in the bad range."),
     ("The system is deployed in a large commercial productivity suite (all authors are at Microsoft Corporation).", "Introduction",
      "PROXYDRIFT has been deployed in a major cloud-based productivity suite serving hundreds of millions of users, where it monitors multiple application scenarios continuously and generates synthetic evaluation data on a weekly cadence."),
   ],
   "notes": "Distribution-comparison (production vs. offline evaluation set) rather than change-point detection on a stream: no ground-truth drift points, no detection metrics (delay, false alarms), and no comparison with drift detectors such as ADWIN/DDM/KSWIN or with statistical two-sample tests were found in the text (searched 'baseline', 'threshold', 'ground truth'). "
            "Tagged dimensionality-reduction-for-shift as the closest family: raw queries are reduced to 21 LLM-classified categorical proxy dimensions before comparison; no family tag fits a distance-based (non-test) categorical comparison. large-language-models because the proxies are produced by LLM-based classification and the monitored application is an LLM product. "
            "Affiliation: all authors at Microsoft Corporation; the case study is on Microsoft Copilot. Data are private production telemetry."},

  {"id": "arxiv-2610.00649",
   "title": "On Evaluating Quantum Kernel Robustness for Low-Resource Cross-Corpus Audio Deepfake Detection",
   "authors": ["Lisan Al Amin", "Lei Zhang", "Vandana P. Janeja"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2610.00649"},
   "tasks": ["tabular-classification"], "fam": ["kernel-methods", "tabular-mlp", "linear-models", "random-forests", "gradient-boosted-trees"], "par": ["supervised"],
   "proposes": ["Controlled comparison of a quantum-kernel SVM, an RBF SVM and an MLP back-end on 4-dimensional PCA-reduced frozen wav2vec 2.0 embeddings for cross-corpus audio deepfake detection"],
   "claims": [
     ("Design: QSVM, classical SVM and MLP back-ends are trained on the same frozen wav2vec 2.0 embeddings with only 200 labeled training samples.", "Abstract",
      "We compare a Quantum Support Vector Machine (QSVM), a classical support vector machine (SVM), and a multilayer perceptron (MLP), all trained on frozen wav2vec 2.0 embeddings using a strict low-resource budget of 200 training samples."),
     ("Main claim: quantum kernels can be competitive under severe cross-corpus shift with few labels, but give no consistent advantage under near-domain transfer.", "Abstract",
      "These findings suggest that quantum kernel methods can provide a competitive alternative under severe cross-corpus shifts and strict low-resource constraints, although they provide no consistent advantage under near-domain transfer."),
     ("Tuning protocol: hyperparameters are selected on the training split only with inner cross-validation, using the same search ranges for all back-ends.", "Experimental setup",
      "For fairness, hyperparameters are selected on the training split only, using an inner cross-validation loop, and the same search ranges are used across back-ends."),
     ("Thresholds: EER is computed by sweeping the threshold on the target data, while accuracy uses the training-derived threshold; the authors note the gap between the two is the cost of carrying the threshold across the shift and recommend re-estimating it on labeled target data.", "Results (cross-corpus robustness)",
      "The threshold should be re-estimated on a small labeled sample from the target domain rather than carried over from training."),
     ("No significance tests are reported because the five folds come from the same 200-sample pool.", "Results (in-corpus discrimination)",
      "We do not attach significance tests to these differences as the five folds are drawn from the same 200-sample pool and are not independent, so a paired test would overstate the evidence."),
     ("Limitation: no comparison with fine-tuned state-of-the-art detectors and no results on recent large multilingual corpora; all back-ends see only the 4-dimensional PCA features.", "Limitations",
      "We do not benchmark against fine-tuned state-of-the-art detectors such as Whisper- or AASIST-based systems [30], and we do not report results on the recent large-scale multilingual corpora MLAAD [31] and XMAD-Bench [32]."),
   ],
   "notes": "Off-theme for drift detection: the paper studies classifier robustness under cross-corpus distribution shift (ASVspoof 2019, ASVspoof 5, ADD 2023, In-the-Wild), not detecting when a shift occurs. "
            "Task is binary audio deepfake classification on 4-dimensional embedding vectors; no audio/representation-classification tag exists, so tabular-classification is used as the closest. Family tags: kernel-methods for the QSVM and RBF SVM, plus the classical comparators (MLP, LR, RF, GB); k-NN has no family tag. "
            "The authors frame results as the inductive bias of a classically simulable 4-qubit kernel, not quantum advantage. Funding: NSF award stated in Acknowledgment."},

  {"id": "arxiv-2609.39473",
   "title": "Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning",
   "authors": ["Quan M. Tran", "Zhuo Huang", "Zhen Fang", "Jing Zhang", "Mingming Gong", "Tongliang Liu"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.39473"},
   "tasks": ["dataset-shift-detection"], "fam": ["large-language-models"], "par": ["in-context-learning", "post-hoc"],
   "proposes": ["FAME: training-free false-memory evaluation for LLM agents via counterfactual queries and hidden-state 'concept drift'",
                "Counterfactual templates for GSM-Symbolic, GitChameleon 2.0 and BigBench-Hard"],
   "claims": [
     ("FAME evaluates false memory in agents by tracking how internal beliefs change under counterfactual reasoning, without training.", "Abstract",
      "Therefore, we propose FAME, a training-free framework that evaluates false memory through the evolution of agent beliefs under counterfactual reasoning."),
     ("Main claim: monitoring answers alone often fails to detect false memory, while FAME achieves high AUROC across the false-memory settings.", "Abstract",
      "Empirical experiments reveal that simply monitoring answers often fails to detect false memory, while FAME achieves AUROCs of 76.2% – 96.7% across false-memory settings"),
     ("Ground truth: false-memory labels are derived from correct operations/answers (GSM), applied library syntax (GitChameleon) and final answers (BBH); they are used only for evaluation.", "Appendix (Evaluation metric)",
      "To construct the ground-truth labels, we leverage the arithmetic operations and final answers in GSM, the syntax of the applied functions or libraries in Git, and the final answers in BBH."),
     ("Decision rule: the authors state that in practice FAME only needs a threshold on the normalized projection of the concept drift, while the reported metric (AUROC) is threshold-free.", "Appendix (Evaluation metric)",
      "In practice, FAME requires no such ground-truth labels; thresholding the normalized projection of the concept drift onto the readout direction is sufficient for distinguishing faithful from false memories, as described in Alg. 1."),
     ("Realistic-benchmark baselines are representation/uncertainty signals (input similarity, surface layer, logit confidence, task and function vectors, EigenScore, ContextCite, entity-aware probe), not drift detectors.", "Real-World Evaluations",
      "We compare FAME with the following baselines: Input similarity [50], Surface, Logit confidence, Task vector [40], Function vector [41], EigenScore from INSIDE [53], ContextCite [54], Entity-aware probe [25]."),
     ("Limitation: FAME requires access to the agent's hidden states and to counterfactual queries.", "Conclusion",
      "Although promising, FAME requires access to agent hidden states and counterfactual queries."),
   ],
   "notes": "Off-theme for data-stream drift detection: 'concept drift' here means the shift of an LLM's hidden-state representation between memory and counterfactual queries, used to flag false memory. dataset-shift-detection is used as the closest task tag; in-context-learning because memory is given as in-context demonstrations; post-hoc because FAME reads hidden states of a fixed LLM without training. "
            "Main model Llama-3.2-3B-Instruct (layer 14, chosen from prior work and a layer sweep); generalization runs with Llama-3.1-8B, Mistral-7B and Qwen2.5-3B. Controlled settings use Rotten Tomatoes (spurious tag), a film-review-to-tweet shift, and a synthetic versioning convention. "
            "The readout direction is built from held-out queries that clearly induce the memory vs. counterfactual concepts (per template). How the threshold tau would be set in deployment was not found in the text; only AUROC is reported."},

  {"id": "arxiv-2609.36594",
   "title": "Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond",
   "authors": ["Xiaokai Luo", "Chenghao Xu", "Haotian Xu", "Carlos Misael Madrid Padilla", "Daren Wang"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.36594"},
   "tasks": ["change-point-detection"], "fam": ["two-sample-tests"], "par": ["unsupervised"],
   "proposes": ["Tensor-moment CUSUM change-point method (seeded intervals + narrowest-over-threshold, then local refinement) detecting changes in all joint moments up to order p in multivariate time series, with confidence intervals"],
   "claims": [
     ("A tensor representation unifies moments of different orders, giving a method that detects changes in all moments up to a fixed order p.", "Abstract",
      "Our tensor representation unifies moments of different orders within a common linear algebraic framework, enabling a new method to detect changes in moments of all orders up to a prescribed fixed order p."),
     ("Theory: under regularity conditions the localization error rate matches a new minimax lower bound (temporal dependence and growing dimension allowed).", "Abstract",
      "Under suitable regularity conditions, the proposed procedure achieves a localization error rate that matches a newly developed minimax lower bound."),
     ("Competing methods (CPWZ, changeAUC, mean-change binary segmentation, MNSBS) use their default or paper-recommended tuning parameters and their own data-driven selection procedures.", "Simulation and real data example (tuning parameter selection)",
      "For the competing methods, we use their default or paper-recommended tuning parameters and their associated data-driven selection procedures."),
     ("The proposed method's threshold tau and moment order p are chosen jointly from a grid by sample splitting: fit on odd-indexed observations and score the segmentation on even-indexed observations with an empirical kernel score (no ground-truth change points used).", "Simulation and real data example (tuning parameter selection)",
      "To select the candidate pair in a data-driven manner, we evaluate these segments on the even-indexed observations using an empirical kernel score (Steinwart and Ziegel, 2021)."),
     ("Simulations: D = 100 dimensional AR(1) series, 100 repetitions per setting, with change points injected at fixed known locations; accuracy is the Hausdorff distance between true and estimated change sets plus the frequency of under/over-estimating the number of changes.", "Simulation studies",
      "We use D = 100 and 100 independent repetitions per setting."),
     ("Main empirical claim: in the simulations the method recovers the correct number of changes in every repetition and has the lowest mean Hausdorff distance.", "Simulation studies",
      "Table 1 shows that Tensor recovers the correct number of changes in all 100 repetitions of each setting, and its refined estimates attain the lowest mean Hausdorff distance."),
   ],
   "notes": "Offline (retrospective) multiple change-point detection in multivariate time series, not online stream drift detection; no detection delay or false-alarm-rate metrics. Tagged change-point-detection; two-sample-tests is the closest family (CUSUM contrasts of moment tensors between adjacent segments). "
            "Ground truth exists only for the synthetic settings R1-R5; the real-data example (two Nasdaq-100 return panels) has no ground truth and estimated dates are compared with market events (Lehman bankruptcy, COVID-19 onset). CPWZ is omitted in the two-change settings because it targets a single change."},

  {"id": "arxiv-2609.35703",
   "title": "A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion",
   "authors": ["Fred Xu", "Thomas Markovich", "Florence Regol", "Yizhou Sun"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.35703", "code": "https://github.com/heraclixus/DSSGNN"},
   "tasks": ["graph-node-prediction"], "fam": ["graph-neural-networks"], "par": ["supervised"],
   "proposes": ["DSS-GNN: doubly-spectral stochastic (graph Fourier x polynomial chaos) node-embedding representation with standalone and hybrid (DSS-Hybrid) deployment modes"],
   "claims": [
     ("DSS-GNN can be used standalone or as a residual branch beside a deterministic encoder (DSS-Hybrid).", "Abstract",
      "DSS-GNN has two deployment modes: standalone, or as a residual branch beside a deterministic encoder (DSS-Hybrid)."),
     ("Main claim: the standalone model has the lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc calibration.", "Abstract",
      "Standalone DSS-GNN achieves the lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc correction"),
     ("OOD-detection baselines GNNSafe, GNNSafe++ and GPN are taken from the values reported by Wu et al., while Graph-EBM, MC-dropout and Deep Ensembles are run in the authors' pipeline on the same backbone.", "Experiments (setup)",
      "against GNNSafe, GNNSafe++, and GPN [30] at the values reported by Wu et al. [36]"),
     ("Distribution-shift baselines on GOOD (ERM through TAR) are also copied from Zheng et al., with only G-ΔUQ run in the authors' pipeline.", "Experiments (distribution-shifted classification)",
      "ERM through TAR as reported by Zheng et al. [38]"),
     ("For the standalone model under the GOOD protocol, the epoch and the configuration (BatchNorm, learning rate, hidden width, P) are selected on the GOOD OOD-validation split.", "Appendix (standalone under the GOOD protocol)",
      "the epoch is selected by OOD-validation loss within each run and the configuration (BatchNorm on/off, learning rate, hidden width, P) on the GOOD OOD-validation split"),
     ("Limitation: all stochastic variation comes from one shared scalar Gaussian factor, so joint cross-node uncertainty is not modeled.", "Conclusion and Limitations",
      "All stochastic variation is due to one shared Gaussian factor, perfectly dependent across nodes, so the logit covariance across nodes has rank at most P."),
   ],
   "notes": "Off-theme for drift detection: GNN calibration, node-level OOD detection (GNNSafe benchmark, AUROC/AUPR/FPR95) and accuracy under GOOD concept shift; no drift points or detection delay. "
            "Several baseline numbers are copied from earlier papers rather than re-run under the same protocol. Affiliation: first author's work was done during an internship at Block, Inc.; a co-author is at Block, Inc. NeurIPS 2026 is stated on the PDF's first page (not recorded as venue because the metadata JSON has no venue)."},

  {"id": "arxiv-2609.33940",
   "title": "Behavioral Monitoring of JEPA World Models with Jacobian Centroids",
   "authors": ["Thomas Walker", "Randall Balestriero", "Richard Baraniuk"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.33940"},
   "tasks": ["dataset-shift-detection"], "fam": ["deep-learning", "reconstruction-based-detectors", "saliency-maps"], "par": ["unsupervised", "post-hoc"],
   "proposes": ["Jacobian-centroid (behavioral) signals for runtime monitoring of JEPA world models: failure prediction, encoder/predictor dissociation gate, saliency maps"],
   "claims": [
     ("Centroids (sub-component Jacobian row-sums) identify behavioral properties of world models and complement activation-based signals.", "Abstract",
      "Here, we show that centroids—sub-component Jacobian row-sums—effectively identify the behavioral properties of WMs, complementing traditional activation-based knowledge signals."),
     ("Main claim: centroid-based methods outperform baseline methods as distribution-shift detectors.", "Abstract",
      "Moreover, centroid-based methods outperform baseline methods as distribution-shift detectors."),
     ("Evaluation: the target is episode success/failure from environment feedback on Push-T and TwoRoom (LeWorldModel + CEM planner), scored by AUC; distribution shift is induced by a larger goal offset than in-distribution.", "Centroid Signals for Failure Prediction (experimental setup)",
      "We evaluate on Push-T and TwoRoom using the trained LeWorldModel with a CEM planner (300 samples, 30 steps, receding-horizon K = 2), and label each episode as a success or failure based on the environment’s feedback."),
     ("The pre-execution gate thresholds are calibrated from in-distribution data only, without labeled failures.", "Pre-Execution Gate and Adaptive Replanning",
      "Both thresholds are calibrated from in-distribution data alone with no labeled failures, and yield zero in-distribution false positives on Push-T and a 1% false-alarm rate on TwoRoom."),
     ("Layer choice for the calibration signal is task-specific (layer 0 for Push-T, deepest layer for TwoRoom) and is reported relative to the oracle-best layer.", "Appendix (signal definitions)",
      "Layer-0 suffices for Push-T (AUC within 0.02 of oracle in-distribution, within 0.01 out-of-distribution), whereas layer-5 (deepest) is consistently oracle-optimal across all seeds and regimes on TwoRoom."),
     ("Limitation: all results come from one world-model family on two tasks.", "Conclusion",
      "All results come from a single WM family (LeWorldModel) on two tasks."),
   ],
   "notes": "Off-theme for stream drift detection: per-episode failure prediction for world-model planning under an induced goal-offset shift; 'distribution-shift detectors' in the abstract refers to this failure-prediction AUC. dataset-shift-detection is used as the closest task tag; saliency-maps because centroid-based saliency maps are one of the proposed tools; post-hoc because the signals are read from a trained world model without changing it. "
            "Baselines are activation-based signals (embedding cost, activation calibration, OMP/SAE goal codes) and a reconstruction-error analogue of VAE-based monitoring; no classical drift detectors. "
            "The main text says the per-layer OOD AUC profile (Figure 6) motivated the task-adaptive layer heuristic, so layer choice was informed by outcome-labeled evaluation data. The conclusion states that in-distribution the centroid and activation views are largely interchangeable."},
]

build(SPECS, base_note="Approved from candidate issue #2 (2026-10-02); carded by a subagent. Results tables not recorded; claims only.")
