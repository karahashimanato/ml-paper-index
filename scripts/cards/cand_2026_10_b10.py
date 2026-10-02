"""候補 Issue #1(表データ)で承認された論文 8 本のカード(バッチ cand_2026_10_b10)。
主張と評価方法(ベンチマーク・ベースラインの調整方法・利益相反・限界)だけを記録し、結果表の数値は記録しない。
書誌(著者・版・年)はバッチのメタデータ JSON(arXiv API 由来)をそのまま書き写した。"""

import sys

sys.path.insert(0, "scripts/cards")
from _spec_builder import build  # noqa: E402

BOTH = ["tabular-classification", "tabular-regression"]

SPECS = [
  {"id": "arxiv-2608.13793",
   "title": "On the Brittleness of Maximum Likelihood Estimation for Gaussian Process Hyperparameter Optimization",
   "authors": ["Tyler R. Johnson", "Kian Ben-Jacob", "Christopher P. Muller", "Ramin Bostanabad"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2608.13793",
             "code": "https://github.com/Bostanabad-Research-Group/GP-vs-TabPFN-vs-GPyTorch"},
   "tasks": BOTH, "fam": ["gaussian-processes", "tabular-foundation-model"], "par": ["supervised", "in-context-learning"],
   "proposes": ["Practical remedies for MLE-based GP training (log-scale reparameterization, multiple initializations, smooth hyperparameter bounds)"],
   "claims": [
     ("Implemented carefully, GPs trained via MLE remain highly competitive and can outperform foundation models such as TabPFN in prediction accuracy, UQ quality and inference cost.", "Conclusion",
      "When implemented carefully, GPs trained via MLE remain highly competitive and can outperform foundation models such as TabPFN in prediction accuracy, UQ quality, and inference cost."),
     ("To stress-test GPs, the GPs are trained with the default settings of GPyTorch and GP+.", "Evaluation protocols",
      "To stress-test GPs, we train them via the default settings of Gpytorch [55] and GP+ [56]."),
     ("The regression benchmarks are analytic test functions from a simulation-experiment library, with categorical inputs studied via the Buckling function.", "Evaluation protocols",
      "Nine benchmark regression problems are adopted from [57] (i.e. Ackley, Borehole, Dixon-Price, Griewank, Rosenbrock, Wing Weight, and Zakharov) and we study the effects of categorical inputs in the Buckling function obtained from [58]."),
     ("For the comparison with TabPFN, the GP training process and kernel were not fine-tuned; evaluating the models under their best settings is left open.", "Conclusion",
      "For a fair comparison, we refrained from fine-tuning the training process and kernel of the GPs when comparing them to TabPFN but it is interesting to evaluate these models under their best settings."),
     ("The studies were mostly limited to analytic benchmarks with Gaussian observation noise.", "Conclusion",
      "Our studies were mostly limited to analytic benchmarks with Gaussian observation noise."),
     ("GP+, one of the evaluated GP libraries, is described by the authors as their own package (conflict-of-interest relevant: the authors' library is compared against TabPFN).", "Section 3.2",
      "In our GP+ package, the hyperparameters corresponding to the kernel in Equation (11) are bounded"),
   ],
   "notes": ("The GP+ reference [56] lists the corresponding author (Ramin Bostanabad) as an author. "
             "TabPFN v2.0 and v2.5 are compared; in the 1D examples TabPFN v2.5 is also shown with a tuned configuration (small-samples checkpoint, larger ensemble). "
             "Each regression experiment is repeated 10 times with 5000 test samples.")},

  {"id": "arxiv-2608.10522",
   "title": "Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training",
   "authors": ["Yingsheng Liu", "Haiming Li", "Jingmin Zhu", "Jiajun Sun", "Victoria Mar", "Monika Janda", "H. Peter Soyer",
               "Zongyuan Ge", "Zhen Yu"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2608.10522", "code": "https://github.com/Ethan-ysliu/AID"},
   "tasks": ["tabular-classification"], "fam": ["deep-learning", "tabular-attention"], "par": ["self-supervised"],
   "proposes": ["AID (Adaptive Importance-guided Discretized reconstruction) for image-tabular pre-training",
                "Importance-Aware Adaptive Masking", "Soft-Label Discretized Module"],
   "claims": [
     ("The paper proposes a semantic-aware multimodal pre-training framework that explicitly models the two-dimensional structure of medical tabular data.", "Abstract",
      "To overcome this, we propose a novel semantic-aware framework explicitly modeling the intrinsic two-dimensional structure of tabular data."),
     ("Experiments on dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets are reported as establishing a new state of the art.", "Abstract",
      "Extensive experiments across large-scale dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets establish a new state-of-the-art (SOTA), demonstrating exceptional robustness and cross-domain generalizability."),
     ("Label-free feature importance is obtained by fitting a frozen tabular foundation model (TabPFN v2) to PCA-derived binary pseudo-labels and reading its attention weights.", "Methodology",
      "These pseudo-labels adapt a frozen tabular foundation model[12]."),
     ("On SLICE-3D, samples from 220 patients are geographically held out as an out-of-domain test set and excluded from pre-training.", "Experimental setup",
      "To ensure rigorous evaluation, 80,433 samples from 220 patients are geographically isolated as an Out-of-Domain (OOD) test set and strictly excluded from pre-training."),
     ("Baselines (including CatBoost, FT-Transformer and TabPFN v2) are stated to be reproduced under identical settings; no baseline hyperparameter-tuning procedure was found in the text.", "Main results",
      "As presented in Table 1, all baseline experiments were rigorously reproduced under identical experimental settings."),
     ("The proposed method's hyperparameters were set empirically through validation experiments.", "Experimental setup",
      "All hyperparameter settings were empirically established through extensive validation experiments."),
   ],
   "notes": ("Image-tabular multimodal setting (ViT image encoder plus tabular transformer), not pure tabular prediction. "
             "HOP is a private dataset. The paper declares no competing interests.")},

  {"id": "arxiv-2608.11431", "title": "AutoGrable: What Is a Good Graph for a Table?",
   "authors": ["Tamara Cucumides", "Floris Geerts"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2608.11431", "code": "https://github.com/TamaraCucumides/autoGrable"},
   "tasks": ["tabular-classification", "graph-node-prediction"], "fam": ["graph-neural-networks"], "par": ["supervised"],
   "proposes": ["AutoGrable (training-free table-to-graph construction via a label-alignment score over column subsets)"],
   "claims": [
     ("The alignment score builds no graph and trains no GNN, so AutoGrable can greedily search column subsets for both single tables and foreign-key schemas.", "Abstract",
      "The score materialises no graph and trains no GNN, so AUTOGRABLE can search the space of subsets greedily and cheaply, and returns the resulting grable for single tables and for foreign-key schemas alike."),
     ("AutoGrable recovers label-generating columns on controlled tasks and outperforms fixed, random and task-aware constructors on real tasks under a fixed predictor.", "Abstract",
      "that AUTOGRABLE recovers the columns that generate the label on controlled tasks and outperforms fixed, random, and task-aware constructors on real tasks under a fixed predictor"),
     ("All constructions are evaluated with GraphSAGE using a fixed architecture, budget and hyperparameters within each regime, with no per-constructor tuning.", "Experimental setup",
      "We use GraphSAGE throughout, with fixed architecture, budget and hyperparameters within regime (see Appendix D.6.1) for every construction and every dataset, and no per-constructor tuning."),
     ("TabArena is used as a negative control, since on i.i.d. single-table data each label should depend only on its own row.", "Experimental setup",
      "Negative control: the i.i.d. single-table benchmark TabArena [15], where each label should depend only on its own row."),
     ("Only a subset of TabArena is used: datasets with more than 8 categorical features and a binary target.", "Appendix",
      "The datasets are selected for having more than 8 categorical features and a binary classification target."),
     ("The association between the score and downstream AUC is weaker on test than on validation, which the authors expect because the score is also computed on the validation split.", "Results",
      "The association is weaker on test than on validation, as expected since J is also computed on the validation split."),
   ],
   "notes": ("Real-task regimes: FDB fraud tables (transactional), RelBench (relational), TabArena subset (negative control). "
             "For the auGraph baseline, the reported metric variant is the one best on the validation set.")},

  {"id": "arxiv-2609.12712", "title": "InRTL: Effective Intra-Inter Interaction Learning for Relational Tables",
   "authors": ["Weichen Li", "Ken Zhong", "Zheng Wang", "Li Pan", "Jianhua Li"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.12712", "code": "https://github.com/W1nterFloW/InRTL"},
   "tasks": BOTH, "fam": ["tabular-attention", "graph-neural-networks"], "par": ["supervised"],
   "proposes": ["InRTL (Intra-Inter Relational Table Learning: linearized self-attention within tables, HGNN cross-attention across PK-FK links)"],
   "claims": [
     ("InRTL is a unified framework that explicitly models dependencies within and across relational tables.", "Abstract",
      "In this paper, we propose Intra–Inter Relational Table Learning (InRTL), a unified framework that explicitly models dependencies both within and across relational tables."),
     ("Experiments are reported to show that InRTL consistently outperforms state-of-the-art baselines on diverse relational table tasks.", "Conclusion",
      "Extensive experiments demonstrate that InRTL consistently outperforms state-of-the-art baselines on diverse relational table tasks."),
     ("All experiments follow the standard preprocessing and train/val/test splits of each benchmark (SJTUTables and RelBench).", "Experimental setup",
      "Additionally, for all experiments, we follow the standard data preprocessing and train/val/test split provided by each benchmark."),
     ("All baselines were re-implemented from official code or the original papers and tuned by grid search over key hyperparameters.", "Appendix",
      "To ensure fairness, we re-implemented all baselines based on the official code or their original papers and performed a comprehensive grid search over key hyper-parameters (see Appendix C.5 for details)."),
     ("Hyperparameters of all models are selected on validation performance.", "Appendix",
      "We tune all model hyper-parameters based on validation performance."),
     ("The evaluation focuses mainly on well-curated relational databases with explicit table relationships.", "Limitations",
      "Our evaluation mainly focuses on well-curated relational databases with explicit table relationships."),
   ],
   "notes": ("Single-table baselines (LightGBM, TabPFN, FT-Transformer, TabNet, SAINT, Trompt, ExcelFormer) are given a flattened table built by LEFT JOINs. "
             "Results are averaged over 20 runs. Baselines include LightGBM and TabPFN but no CatBoost/XGBoost.")},

  {"id": "arxiv-2608.02412", "title": "Why Large Language Models Fail at Tabular Prediction",
   "authors": ["Marta Garnelo", "Wojciech M. Czarnecki"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2608.02412"},
   "tasks": ["tabular-classification"], "fam": ["large-language-models"], "par": ["in-context-learning"],
   "proposes": ["Controlled evaluation protocol for LLM in-context tabular classification (including a memorisation probe)"],
   "claims": [
     ("Under random linear projections, the LLM is the only one of nine methods whose accuracy decreases as dimensionality grows, while every classical baseline stays flat or improves.", "Abstract",
      "Dimensionality, in contrast, is decisive: sweeping random linear projections of thirty-one benchmark datasets, the LLM is the only method among nine whose accuracy decreases as dimensionality grows, while every classical baseline stays flat or improves."),
     ("The experiments use claude-opus-4-6, with an initial generalisation experiment using Qwen.", "What do we mean by LLM",
      "Concretely, our experiments use claude-opus-4-6 [2], a frontier model at the time of writing (Section C.3), alongside an initial generalizing experiment using Qwen to begin moving our claims from a single model to LLMs more broadly."),
     ("Splits are 5-fold stratified cross-validation repeated over 5 seeds.", "Datasets and experimental setup",
      "Splits are 5-fold stratified cross-validation repeated over 5 seeds, giving 25 splits per dataset and 475 queries in total."),
     ("The main classical baselines use fixed scikit-learn configurations; e.g. gradient boosting uses 100 estimators and otherwise sklearn defaults. No tuning of the main baselines was found in the text.", "Appendix",
      "GradientBoostingClassifier with n_estimators=100 and random_state=0; sklearn defaults otherwise"),
     ("The authors suggest that a memorisation probe should be standard practice in any LLM-for-tabular evaluation.", "Data hygiene",
      "More broadly, we suggest that a probe of this kind should be standard practice in any LLM-for-tabular evaluation."),
     ("The evaluation is restricted to toy-scale tabular datasets, a restriction partly forced by the cost and context limits of the LLM.", "Limitations",
      "A limitation of our evaluation is that it is restricted to toy-scale tabular datasets; however, this restriction is itself partly forced by the cost and context limits of the method being studied."),
   ],
   "notes": ("The memorisation probe finds the LLM recovers held-out labels of classic datasets (e.g. breast cancer, iris); such datasets are excluded, leaving 11 of 19 datasets for main analyses. "
             "Inconsistency: the abstract and introduction say 'thirty-one benchmark datasets' for the projection sweep, whereas the Figure 8 caption says '11 benchmark datasets'; not reconciled here. "
             "The evaluated LLM is an Anthropic model; the authors' stated affiliations are Fundamental Technologies and Voylab.")},

  {"id": "arxiv-2609.39628",
   "title": "MIND: Marginal-Invariant Neural Dependency Diffusion for Mixed-Type Tabular Generation",
   "authors": ["Pengfei Li", "Mohammad Khalil"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.39628"},
   "tasks": ["tabular-data-generation"], "fam": ["deep-learning"], "par": ["unsupervised"],
   "proposes": ["MIND (marginal-invariant dependency diffusion with column-wise marginal transport, copula-tangent denoising and rank projection)"],
   "claims": [
     ("MIND maps different variable types into a unified latent dependency space via column-wise marginal transport instead of learning the joint distribution in the raw feature space.", "Abstract",
      "Instead, it first maps different variable types into a unified latent dependency space via column-wise marginal transport."),
     ("Across nine tabular benchmarks, MIND is reported to consistently improve marginal fidelity and dependency preservation over existing unified approaches.", "Abstract",
      "Experiments across nine diverse tabular benchmarks show that MIND consistently improves marginal fidelity and dependency preservation over existing unified approaches."),
     ("For each of three seeds, all methods share the same stratified 64/16/20 train/validation/test split.", "Experiment setup",
      "For each seed in {42, 43, 44}, all methods use the same stratified 64%/16%/20% train/validation/test split"),
     ("TSTR utility is averaged over XGBoost, LightGBM and MLP downstream models, using AUC for classification and R2 for regression.", "Results",
      "Scores are averaged over XGBoost, LightGBM, and MLP, using AUC for classification datasets and R2 for regression datasets"),
     ("The aggregate TSTR advantage of MIND is substantially influenced by Covertype, so the authors interpret MIND as competitive with diffusion-based SOTA rather than dominant.", "Discussion",
      "Although the aggregate TSTR mean favours MIND, this difference is influenced substantially by Covertype."),
     ("MIND assumes a designated target column and batch-level generation, limiting direct use in target-free or multi-target settings.", "Limitations",
      "Currently, we assume a designated target column and perform batch-level generation, which limits direct use in target-free or multi-target settings."),
   ],
   "notes": ("Synthetic data generation paper; utility is evaluated by TSTR on classification and regression targets. Baselines: independent marginals, Gaussian Copula, CTGAN, TVAE, TabSyn, TabDiff. "
             "Baseline hyperparameter tuning was not found in the text (details are deferred to a supplementary not included in the PDF text). "
             "The PDF carries an AAAI copyright line; venue omitted because it is not in the metadata.")},

  {"id": "arxiv-2609.39613", "title": "Hybrid Methods for Robust Tabular Data Imputation",
   "authors": ["Jinwei Li", "Michelle Bruch", "Daniel Tenbrinck"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2609.39613"},
   "tasks": ["tabular-imputation"], "fam": ["random-forests"], "par": ["unsupervised"],
   "proposes": ["NuclearForest (adaptive SVT initialization + one-pass random forest refinement)",
                "SoftForest (SoftImpute initialization + one-pass random forest refinement)"],
   "claims": [
     ("The paper proposes NuclearForest and SoftForest, combining nuclear-norm low-rank initialization (SVT or SoftImpute) with a non-iterative random forest refinement.", "Abstract",
      "In this work, we propose two hybrid imputation methods called NuclearForest and SoftForest, which combine nuclear-norm-based low-rank initialization using Singular Value Thresholding (SVT) and SoftImpute, respectively, with a non-iterative Random Forest refinement."),
     ("The hybrids are reported to match or exceed the imputation fidelity of iterative methods such as MissForest at lower computational cost.", "Abstract",
      "Our results demonstrate that NuclearForest and SoftForest match or exceed the imputation fidelity of state-of-the-art iterative methods such as MissForest, while significantly reducing computational cost."),
     ("Missing entries are regenerated independently over 10 repeated runs per setting.", "Experiments and results",
      "For each setting, missing entries are regenerated independently over 10 repeated experimental runs, ensuring different missingness masks across runs while preserving reproducibility."),
     ("Neural-network imputation methods are not included as primary baselines.", "Experiments and results",
      "Neural-network-based imputation methods are not included as primary baselines because the focus of this study is on efficient classical and hybrid tabular imputers."),
     ("On the metabolomics data, NuclearForest is competitive with MissForest and strong at low missing rates, while MissForest is best in several medium- and high-missingness settings.", "Conclusion",
      "On the former, NuclearForest remains competitive with MissForest across missingness levels and is particularly strong at low missing rates, while MissForest achieves the best performance in several medium- and high-missingness settings."),
     ("The gains do not fully extend to the left-censored MNAR setting, where Half-min is well aligned with the mechanism.", "Conclusion",
      "A limitation is that these gains do not fully extend to the left-censored MNAR setting, where Half-min is well aligned with this mechanism."),
   ],
   "notes": ("Only two datasets: a metabolomics dataset (Wei et al. 2018) and a Kaggle housing dataset. All methods use fixed hyperparameters listed in the appendix; no tuning procedure was found in the text. "
             "Code is stated to be released upon acceptance (no URL in the text).")},

  {"id": "arxiv-2610.00391",
   "title": "Interpretable Synthetic Medical Tabular Data Generation for Clinical Decision Support Using Fuzzy Cognitive Maps",
   "authors": ["Michael Vasilakakis", "Dimitris K. Iakovidis"],
   "year": 2026, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2610.00391"},
   "tasks": ["tabular-data-generation"], "fam": ["interpretable-models"], "par": ["unsupervised"],
   "proposes": ["Fuzzy Cognitive Map (FCM) based synthetic medical tabular data generator"],
   "claims": [
     ("The paper applies Fuzzy Cognitive Maps to synthetic medical tabular data generation with explicit causality and privacy preservation.", "Abstract",
      "This paper proposes a novel application of Fuzzy Cognitive Maps (FCMs) in a framework for synthetic medical tabular data generation with explicit causality and privacy preservation."),
     ("On UCI medical datasets the method is reported to be competitive under a train-on-synthetic-test-on-real protocol.", "Abstract",
      "Experimental evaluation on UCI medical benchmark datasets demonstrates competitive performance under a Train-on-Synthetic-Test-on-Real (TSTR) protocol."),
     ("All baselines (Gaussian Copula, CTGAN, TVAE) use their default SDV configurations.", "Experimental setup",
      "All baseline models were implemented using their default SDV configurations."),
     ("Each dataset uses a single 80/20 train-test split shared across methods.", "Experimental setup",
      "For each dataset, a consistent train–test split of 80/20 was applied across all methods."),
     ("Models requiring extensive GPU resources were excluded from the comparison.", "Experimental setup",
      "Models requiring extensive GPU resources were excluded to maintain consistent experimental conditions."),
     ("Gaussian Copula attains marginally higher fidelity in some cases, which the authors say is often accompanied by reduced predictive utility.", "Results",
      "Although Gaussian Copula achieves marginally higher fidelity in certain cases, this is often accompanied by reduced predictive utility, whereas the proposed framework maintains a balanced trade-off between realism and downstream task performance."),
   ],
   "notes": ("Three small UCI datasets (Pima Indians Diabetes, South African Heart Disease, Statlog Heart). "
             "The downstream TSTR classifier and the number of repetitions were not found in the text. "
             "The PDF states acceptance at IEEE CBMS 2026; venue omitted because it is not in the metadata. "
             "Funded by the EU IHI JU project SEARCH with industry partners listed in the acknowledgement footnote. "
             "No fuzzy-model family tag exists; interpretable-models was used as the closest (FCM structure with linguistic fuzzy sets is itself interpretable).")},
]

build(SPECS, base_note="Approved from candidate issue #1 (2026-10-02); carded by a subagent. Results tables not recorded; claims only.")
