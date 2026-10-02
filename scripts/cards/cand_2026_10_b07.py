"""候補 Issue #1(表データ)で承認された論文のうち、バッチ cand_2026_10_b07 の5本のカード。
各論文の主張と評価方法(ベンチマーク・ベースラインの扱い・選択に使うデータ)の記述を記録する。結果表の数値は記録しない。
書誌(著者・版・年)は scratchpad の batches/cand_2026_10_b07.json(arXiv API の値)をそのまま書き写した。"""

import sys

sys.path.insert(0, "scripts/cards")
from _spec_builder import build  # noqa: E402

SPECS = [
  {"id": "arxiv-2609.12105",
   "title": "Language Is an Insufficient Substrate for Quantitative Reasoning, and Consequential Domains Need Large Quantitative Models",
   "authors": ["Reuben Vandeventer", "David Imrem", "David J. Wild"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.12105"},
   "tasks": ["tabular-classification", "tabular-regression"], "fam": ["large-language-models", "tabular-foundation-model"], "par": [],
   "proposes": ["Large Quantitative Model (LQM) as a model class (position paper)"],
   "claims": [
     ("The paper's position is that the assumption that progress on consequential quantitative decisions will follow from progress in LLMs is mistaken, and that the mistake is structural rather than a matter of present capability.", "Abstract",
      "This paper takes the position that the assumption is mistaken, and that the mistake is structural rather than a matter of present capability."),
     ("Fidelity, reproducibility, lineage and calibration are argued to define a distinct model class, the Large Quantitative Model (LQM).", "Abstract",
      "We argue that these properties define a distinct model class, which we call the Large Quantitative Model (LQM)"),
     ("A tabular foundation model can be native to the quantitative data and still lack lineage and structural explicitness, because its representation of the domain lives in its weights.", "Tabular and time-series foundation models",
      "A tabular foundation model can be substrate-native and still fail lineage and structural explicitness, because its representation of the domain lives in weights."),
     ("Citing prior literature (not its own experiments), the paper states that on tabular prediction with modest datasets, gradient-boosted trees or purpose-built tabular transformers continue to outperform general-purpose deep models.", "Empirical corroboration",
      "In the setting closest to our own argument—tabular prediction on modest datasets—models designed for the statistical character of the data, whether gradient-boosted trees or purpose-built tabular transformers, continue to outperform general-purpose deep models"),
     ("The paper runs no benchmark experiments of its own; its empirical evidence is one deployed system (a security-operations architecture described by Vallabhaneni et al.), which the authors say is not a full LQM.", "Evidence",
      "We have one deployed test of this prediction that we can report in full."),
     ("Competing interests: all three authors are affiliated with Duo Dimensio LLC, which develops systems of the kind the paper describes.", "Competing interests",
      "R.V., D.I. and D.J.W. are affiliated with Duo Dimensio LLC, which develops systems of the kind described in Section 7."),
   ],
   "notes": "Position paper without its own benchmark experiments. Task tags are approximate: the paper discusses quantitative decision-making on tabular/relational records in general, not a specific classification or regression benchmark."},

  {"id": "arxiv-2609.09586",
   "title": "Distillation of Synthetic Data for Time Series Foundation Models",
   "authors": ["Niloy Biswas", "Noureddine El Karoui"], "year": 2026, "version": "arXiv v2",
   "links": {"arxiv": "https://arxiv.org/abs/2609.09586", "code": "https://github.com/niloyb/sdd"},
   "tasks": ["time-series-forecasting"], "fam": ["time-series-foundation-model"], "par": [],
   "proposes": ["Synthetic data distillation (SDD): pre-training loss against the conditional forecast distribution of synthetic trajectories"],
   "claims": [
     ("SDD replaces the usual loss against the realized future values of a synthetic trajectory with a loss against the trajectory's conditional forecast distribution.", "Abstract",
      "We instead propose loss objectives which compare TSFM outputs to the conditional forecast distribution of each trajectory, a procedure we call synthetic data distillation (SDD)."),
     ("SDD is a Rao-Blackwellization of the training objective: the expected stochastic gradient is unchanged while its covariance is provably reduced.", "Abstract",
      "SDD corresponds to a Rao-Blackwellization of the training objective, in that it leaves the expectation of stochastic gradients unchanged while provably reducing the covariance of the stochastic gradient under the Loewner partial ordering."),
     ("SDD reaches the same validation loss as the status-quo loss with fewer FLOPs, with the speed-up depending on model size.", "Numerical Experiments",
      "Figure 2 shows that SDD attains the same validation loss as Status Quo while spending 38-46% fewer FLOPs, a convergence speed-up of 1.6× to 1.85× depending on model size."),
     ("Experimental setup: five Toto-2 architectures are pre-trained from random initialization on univariate Gaussian-process trajectories only.", "Numerical Experiments",
      "We pre-train the five Toto-2 architectures [9], spanning 4M to 2.5B parameters, from random initialization on trajectories from univariate Gaussian processes of length T = 512."),
     ("The held-out validation set is drawn fresh from the same synthetic generator (with disjoint seeds), so no real-world forecasting benchmark is used.", "Experimental Details (appendix)",
      "Held-out throughout means a validation set drawn fresh from the same generator, using generator seeds disjoint from those that produced the training data, rather than a held-out split of the training corpus."),
     ("Seeds vary only initialization and masking draws, not the training corpus, so the reported error bars understate the spread from retraining on a freshly drawn corpus.", "Experimental Details (appendix)",
      "The error bars therefore carry no data-sampling variability and understate the spread that retraining on a freshly drawn corpus would show."),
   ],
   "notes": "Time-series forecasting paper (not tabular); it mentions applying SDD to tabular foundation models only as future work. "
            "Under teacher forcing (appendix) the paper reports that SDD still wins every paired seed but the effect is an order of magnitude smaller than under contiguous patch masking."},

  {"id": "arxiv-2609.06941",
   "title": "When and Why LLM Causal Priors Help: Closed-Loop Prior Selection for Amortized Causal Inference",
   "authors": ["Haohao Zhou"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.06941"},
   "tasks": ["causal-effect-estimation"], "fam": ["tabular-foundation-model", "large-language-models"], "par": ["in-context-learning"],
   "proposes": ["Closed-loop prior selection for injecting LLM-distilled causal graphs into a PFN (Do-PFN)"],
   "claims": [
     ("On a 7.34M-parameter Do-PFN, the selected prior gives a significant gain on the primary evaluation domain (5 paired seeds), with error below the uninjected official base.", "Abstract",
      "On a 7.34M-parameter Do-PFN, the framework’s winner attains a formally significant 2.75× gain on the primary evaluation domain (n = 5 paired seeds, p = 0.0086), and its error falls below that of the uninjected official base."),
     ("The comparison with the official base is only descriptive: the winner is built on a locally retrained base and the official base is not part of the paired test.", "Abstract",
      "Because the winner is built on a locally retrained base and the official base is not part of the paired test, this is a descriptive cross-lineage comparison."),
     ("Injection gives significant gains only when the base is underfit on the task domain, the prior domain matches the task domain, and the task lies within the support of the base's training prior.", "Abstract",
      "injection yields significant gains only when the base is underfit on the task domain, the prior domain matches the task domain, and the task lies within the support of the base’s training prior."),
     ("The primary and adjacent evaluation domains are synthetic/proprietary causal benchmarks whose generation mechanism and release policy are not yet stated.", "Reproducibility Statement",
      "The primary domain law_race and the adjacent domain sales are synthetic/proprietary causal benchmarks with ground-truth graphs; their generation mechanism and release policy will be stated in the released materials."),
     ("Baselines (CausalPFN and classical estimators such as S/T/X/DR-learners and CausalForestDML) are run under the same 5-fold split and protocol; baseline hyperparameter tuning was not found in the text.", "External validity",
      "On our two domains, we compare against the direct SOTA (CausalPFN [3]) and a classical-estimator panel (S/T/X/DR-learner [13, 11], CausalForestDML [2], naive ATE) under the same 5-fold split and the same protocol as model training."),
     ("On standard causal benchmarks (IHDP, Lalonde), the injection method is not superior to, and often worse than, existing methods.", "Discussion",
      "We state plainly: on standard causal benchmarks, our injection method is not superior to, and is often inferior to, existing methods."),
   ],
   "notes": "Causal effect estimation with a PFN on tabular observational data; the priors are causal graphs distilled from LLMs. "
            "Many comparisons use n = 3 seeds and are labelled directional by the author."},

  {"id": "arxiv-2609.07655",
   "title": "Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery",
   "authors": ["Xiaotang Feng", "Philip Torr", "Bruno Andreis"], "year": 2026, "version": "arXiv v2",
   "links": {"arxiv": "https://arxiv.org/abs/2609.07655"},
   "tasks": ["tabular-regression"], "fam": ["tabular-foundation-model", "large-language-models"], "par": ["in-context-learning"],
   "proposes": ["Online surrogate repair (OSR) / Online EI with a tabular foundation model surrogate"],
   "claims": [
     ("OSR uses sparse high-fidelity evaluations to update a surrogate during a longer agent search that mostly relies on cheap surrogate feedback.", "Abstract",
      "We propose online surrogate repair (OSR), a closed-loop algorithm that uses sparse high-fidelity evaluations to update the surrogate throughout a longer agent search conducted primarily with inexpensive surrogate feedback."),
     ("In controlled synthetic environments, improving global surrogate fit does not necessarily reduce maximum regret, while Q90-UCB and EI acquisitions substantially reduce it.", "Abstract",
      "Across controlled synthetic environments, we demonstrate that improving global surrogate fit does not necessarily reduce maximum regret, whereas Q90-UCB and expected improvement (EI) substantially reduce regret by directing evaluations toward regions that determine the optimizer’s decisions."),
     ("The authors argue that TabArena (global predictive accuracy) and TabPFN's training objective do not match the maximum-regret objective of closed-loop discovery.", "Static surrogate repair",
      "This is a crucial result because TabArena evaluates global predictive accuracy and TabPFN is trained for global prediction, not maximum regret, creating an objective mismatch with closed-loop discovery (Erickson et al., 2025; Hollmann et al., 2025; Grinsztajn et al., 2026)."),
     ("Static study protocol: 40 synthetic tabular worlds, a fixed budget of oracle queries, two context draws per world, two context sizes, with TabPFN-3 and TabICLv2 as surrogates.", "Static surrogate repair",
      "Each acquisition rule repairs the surrogate with Q = 32 oracle queries on 40 synthetically generated tabular worlds, with two independent context draws per world, at both context sizes N = 100 and N = 1000"),
     ("On the MADE benchmark the 'oracle' is a stronger machine-learned potential (Orb-v3), and a weaker one (MACE) provides surrogate feedback.", "MADE benchmark",
      "The weaker MACE model (Batatia et al., 2025) provides surrogate feedback, while the stronger Orb-v3 model (Rhodes et al., 2025) serves as the oracle."),
     ("Not tested: agents with test-time training or reinforcement learning, other surrogate classes, and more advanced scheduling.", "Discussions and Conclusion",
      "We have not tested OSR or Online EI with agents using test-time training or reinforcement learning, with other surrogate classes, or with more advanced and optimization-aware scheduling."),
   ],
   "notes": "Tabular foundation models are used as in-context regression surrogates (labels appended as context rows, no parameter training). "
            "Surrogate hyperparameter settings (defaults vs tuned) were not found in the text. No competing-interest statement was found."},

  {"id": "arxiv-2609.05955",
   "title": "LoGIC: Budgeted Context Construction for Node-Level Graph In-Context Learning with Tabular Foundation Models",
   "authors": ["Mingqi Yang", "Zidong Guo", "Jihui Yang", "Wenming Zuo"], "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.05955"},
   "tasks": ["graph-node-prediction"], "fam": ["tabular-foundation-model", "graph-neural-networks"], "par": ["in-context-learning"],
   "proposes": ["LoGIC: budgeted labeled-context and unlabeled-halo construction for frozen tabular-FM graph ICL"],
   "claims": [
     ("LoGIC retrieves labeled nodes by structural, feature and coverage channels, shares contexts within graph-local query clusters, adds an unlabeled halo for adapter backbones, and selects channel and budget without test labels.", "Abstract",
      "We present LoGIC, which retrieves labeled nodes via structural, feature-based, and coverage channels, shares each context across the queries in a graph-local cluster, incorporates an unlabeled halo for adapter backbones, and chooses the channel and context budget without test labels."),
     ("Budgeted contexts keep locally runnable full-context performance, remain competitive with published large-dataset results, and markedly reduce peak memory.", "Abstract",
      "budgeted contexts maintain locally runnable full-context performance, stay competitive with published large-dataset results, and markedly lower peak memory requirements compared with full-context and whole-graph inference."),
     ("Evaluation uses eight GraphLand node-level benchmarks (12k-168k nodes) with classification (AP) and regression (R2) targets.", "Experimental Setup",
      "We conduct evaluations on eight GraphLand benchmarks [16] covering 12k–168k nodes, classification (AP) and regression (R2), and both assortative and disassortative targets."),
     ("The retrieval channel and budget k are chosen per dataset on held-out validation data from a coarse budget ladder.", "Channel and Budget Configuration",
      "For the reported LoGIC configurations, we assess a coarse ×4 budget ladder using held-out validation data and preserve one (channel, k) pair for each dataset."),
     ("Per-dataset trained baselines (LightGBM-NFA and GNNs) are published numbers taken from the G2T-FM evaluation, not rerun.", "Predictive Performance on GraphLand",
      "The first block lists individually trained LightGBM-NFA and GNN references from the G2T-FM evaluation."),
     ("The authors state that LoGIC is not a universal accuracy substitute for per-dataset training; it lags the strongest trained baselines on several datasets.", "Predictive Performance on GraphLand",
      "The contribution consequently does not constitute a universal accuracy substitute for per-dataset training."),
   ],
   "notes": "Node-level classification/regression on graphs with tabular node attributes; GNNs appear as per-dataset trained baselines and adapter backbones use message passing. "
            "The fixed-channel ablation tables report test-set values, while the deployed configuration is selected on held-out data; the paper notes held-out and test rankings may diverge on some datasets. "
            "One author is affiliated with Meta Superintelligence Lab; no competing-interest statement was found in the text."},
]

build(SPECS, base_note="Approved from candidate issue #1 (2026-10-02); carded by a subagent. Results tables not recorded; claims only.")
