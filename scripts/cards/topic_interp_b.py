"""Topic batch topic_interp_b (interpretability): 7 papers on interpretable models vs post-hoc explanation,
attention as explanation, and Shapley-value feature attribution (TreeSHAP and its critiques).
Claims only (what is proposed, assumptions, how explanation quality was evaluated, failure modes, limitations); no results tables.
Bibliographic data (title, authors, year, version) copied from the batch metadata JSON (arXiv API)."""

import sys

sys.path.insert(0, "scripts/cards")
from _spec_builder import build  # noqa: E402

SPECS = [
  {"id": "arxiv-1811.10154",
   "title": "Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use Interpretable Models Instead",
   "authors": ["Cynthia Rudin"],
   "year": 2018, "version": "arXiv v3", "links": {"arxiv": "https://arxiv.org/abs/1811.10154"},
   "tasks": ["model-explanation"], "fam": ["interpretable-models"], "par": ["supervised"],
   "proposes": ["Position: use inherently interpretable models instead of post-hoc explanations of black boxes for high-stakes decisions"],
   "claims": [
     ("Rudin argues that trying to explain black box models, instead of building models that are interpretable in the first place, "
      "is likely to perpetuate bad practices and can potentially cause catastrophic harm to society.", "Abstract",
      "trying to explain black box models, rather than creating models that are interpretable in the first place, is likely to "
      "perpetuate bad practices and can potentially cause catastrophic harm to society"),
     ("The paper argues it is a myth that there is necessarily an accuracy-interpretability trade-off: for problems with structured data "
      "and meaningful features, there is often no significant performance difference between complex classifiers (deep nets, boosted "
      "trees, random forests) and much simpler ones (logistic regression, decision lists) after preprocessing.",
      "Key Issues with Explainable ML",
      "there is often no significant difference in performance between more complex classifiers (deep neural networks, boosted "
      "decision trees, random forests) and much simpler classifiers (logistic regression, decision lists) after preprocessing"),
     ("Post-hoc explanations cannot have perfect fidelity to the original model: a fully faithful explanation would equal the model "
      "itself, so an explanation may misrepresent the black box in parts of the feature space.", "Key Issues with Explainable ML",
      "If the explanation was completely faithful to what the original model computes, the explanation would equal the original "
      "model, and one would not need the original model in the first place, only the explanation."),
     ("The paper criticises saliency maps, which can look essentially the same for different classes, and the practice of showing "
      "explanations only for the correct label, which it calls misleading.", "Key Issues with Explainable ML",
      "Demonstrating a method using explanations only for the correct class is misleading."),
     ("As evidence, the paper compares the proprietary COMPAS model with a three-rule CORELS rule list using only age, priors and "
      "(optionally) gender, stating that both have similar true/false positive and negative rates on Broward County, Florida data.",
      "Key Issues with Interpretable ML",
      "Both models have similar true and false positive rates and true and false negative rates on data from Broward County, Florida."),
     ("The paper's 'Rashomon set' argument: when the data admit a large set of nearly equally accurate models, that set often "
      "contains at least one interpretable model.", "A Technical Reason Why Accurate Interpretable Models Might Exist in Many Domains",
      "Because this set of accurate models is large, it often contains at least one model that is interpretable."),
     ("Scope/limitation: Rudin concedes there could be application domains where a complete black box is required for a high-stakes "
      "decision, while stating she has not yet encountered one.", "Key Issues with Explainable ML",
      "It could be possible that there are application domains where a complete black box is required for a high stakes decision."),
   ],
   "notes": ("Position/commentary paper: no systematic benchmark experiments were found in the text; evidence consists of argument and "
             "case examples (COMPAS vs CORELS, FICO challenge, prototype networks for images). PDF states a preliminary version appeared "
             "at a workshop ('Please Stop Explaining Black Box Machine Learning Models for High Stakes Decisions'). "
             "Wiegreffe & Pinter (arxiv-1908.04626) cite Rudin's distinction between explainability and interpretability.")},

  {"id": "arxiv-1902.10186", "title": "Attention is not Explanation",
   "authors": ["Sarthak Jain", "Byron C. Wallace"],
   "year": 2019, "version": "arXiv v3",
   "links": {"arxiv": "https://arxiv.org/abs/1902.10186", "code": "https://github.com/successar/AttentionExplanation"},
   "tasks": ["model-explanation"], "fam": ["attention-explanations", "feature-attribution", "deep-learning"], "par": ["post-hoc"],
   "proposes": ["Empirical tests of attention as explanation: correlation with gradient / leave-one-out importance, attention permutation, adversarial attention search"],
   "claims": [
     ("Across a variety of NLP tasks, learned attention weights are frequently uncorrelated with gradient-based feature importance, and "
      "very different attention distributions can yield equivalent predictions; the authors conclude standard attention modules do not "
      "provide meaningful explanations.", "Abstract",
      "learned attention weights are frequently uncorrelated with gradient-based measures of feature importance, and one can identify "
      "very different attention distributions that nonetheless yield equivalent predictions"),
     ("Assumed properties of faithful attention explanations: (i) attention should correlate with feature-importance measures and "
      "(ii) alternative (counterfactual) attention configurations should change the prediction.", "Introduction",
      "(i) Attention weights should correlate with feature importance measures (e.g., gradient-based measures); (ii) Alternative "
      "(or counterfactual) attention weight configurations ought to yield corresponding changes in prediction"),
     ("Neither property was consistently observed for a BiLSTM with a standard attention mechanism on text classification, "
      "question answering and natural language inference.", "Introduction",
      "We report that neither property is consistently observed by a BiLSTM with a standard attention mechanism in the context of "
      "text classification, question answering (QA), and Natural Language Inference (NLI) tasks."),
     ("Evaluation protocol (no ground-truth explanations): Kendall tau correlation of attention with gradient-based importance and with "
      "leave-one-out output differences, computed on test sets.", "Section 4.1",
      "Specifically we measure correlations between attention and: (1) gradient based measures of feature importance (τg), and, "
      "(2) differences in model output induced by leaving features out (τloo)."),
     ("For the adversarial attention search, the allowed change in model output (epsilon, in total variation distance) was set to "
      "0.01 for text classification and 0.05 for QA datasets.", "Adversarial Attention",
      "In practice we simply set this to 0.01 for text classification and 0.05 for QA datasets."),
     ("Limitation: the authors do not claim that gradient or leave-one-out measures are ideal or should be treated as ground truth.",
      "Discussion and Conclusions",
      "We do not intend to imply that such alternative measures are necessarily ideal or that they should be considered ‘ground truth’."),
     ("Limitation: only a handful of attention variants (focused on BiLSTM encoders with attention) were considered; alternative "
      "attention specifications may lead to different conclusions.", "Discussion and Conclusions",
      "An additional limitation is that we have only considered a handful of attention variants, selected to reflect common module "
      "architectures for the respective tasks included in our analysis."),
   ],
   "notes": ("Data are text (SST, IMDB, ADR Tweets, 20 Newsgroups, AG News, MIMIC ICD9 Diabetes/Anemia, CNN, bAbI, SNLI); no data-task "
             "tag for NLP exists, so only model-explanation is tagged. The paper also states that attention over simple feedforward "
             "(averaging) encoders correlates better with the importance measures. No human evaluation was found in the text. "
             "Directly rebutted by Wiegreffe & Pinter (arxiv-1908.04626).")},

  {"id": "arxiv-1908.04626", "title": "Attention is not not Explanation",
   "authors": ["Sarah Wiegreffe", "Yuval Pinter"],
   "year": 2019, "version": "arXiv v2",
   "links": {"arxiv": "https://arxiv.org/abs/1908.04626", "code": "https://github.com/sarahwie/attention"},
   "tasks": ["model-explanation"], "fam": ["attention-explanations", "deep-learning"], "par": ["post-hoc"],
   "proposes": ["Four tests for attention as explanation: uniform-weights baseline, random-seed variance baseline, diagnostic MLP guided by frozen attention weights, model-consistent adversarial attention training"],
   "claims": [
     ("The paper proposes four tests of when attention can serve as explanation: a uniform-weights baseline, a variance calibration "
      "over random seeds, a diagnostic framework using frozen pretrained attention weights, and end-to-end adversarial attention training.",
      "Abstract",
      "We propose four alternative tests to determine when/whether attention can be used as explanation"),
     ("Critique of Jain & Wallace: they detach the attention distribution and output layer from the parameters that compute them and "
      "treat each attention score as a standalone unit, and compute an independent adversarial distribution per instance.",
      "Attention Might be Explanation",
      "Jain and Wallace detach the attention distribution and output layer of their pretrained network from the parameters that "
      "compute them (see Figure 1), treating each attention score as a standalone unit independent of the model."),
     ("Compared with a variant whose attention is frozen to uniform weights, the attention layer appears to offer little to no "
      "improvement on three of the classification tasks; the authors conclude these datasets (notably AG News and 20 Newsgroups) are "
      "not useful test cases, since attention is not explanation if it is not needed.",
      "Uniform as the Adversary",
      "We conclude that these datasets, notably AG NEWS and 20 NEWSGROUPS, are not useful test cases for the debated question: "
      "attention is not explanation if you don’t need it."),
     ("Their evaluation is functionally grounded: an analysis on proxy tasks without human evaluation.", "Defining Explanation",
      "our proposed methods provide a functionally-grounded evaluation of attention as explanation, i.e. an analysis conducted on "
      "proxy tasks without human evaluation."),
     ("Whether attention is explanation depends on the definition one adopts: plausible explanations, faithful explanations, or both.",
      "Attention is All you Need it to Be",
      "Whether or not attention is explanation depends on the definition of explainability one is looking for: plausible or faithful "
      "explanations (or both)."),
     ("Partial agreement with Jain & Wallace: adversarial attention distributions can be found for LSTM models in some classification tasks.",
      "Attention is All you Need it to Be",
      "However, we have confirmed that adversarial distributions can be found for LSTM models in some classification tasks, as "
      "originally hypothesized by Jain and Wallace."),
     ("Adversarially trained attention distributions perform poorly, relative to the original attention, when used as guide weights "
      "in the diagnostic MLP.", "Attention is All you Need it to Be",
      "We’ve shown that alternative attention distributions found via adversarial training methods perform poorly relative to "
      "traditional attention mechanisms when used in our diagnostic MLP model."),
   ],
   "notes": ("Scope: experiments restricted to the binary classification subset of Jain & Wallace's datasets (SST, IMDB, 20 Newsgroups, "
             "AG News, MIMIC Diabetes/Anemia; ADR dropped) and a single-layer BiLSTM with additive attention, using Jain & Wallace's "
             "hyperparameters and train/test splits; analysis on test sets. Direct response to arxiv-1902.10186.")},

  {"id": "arxiv-2004.13912", "title": "Neural Additive Models: Interpretable Machine Learning with Neural Nets",
   "authors": ["Rishabh Agarwal", "Levi Melnick", "Nicholas Frosst", "Xuezhou Zhang", "Ben Lengerich", "Rich Caruana", "Geoffrey Hinton"],
   "year": 2020, "version": "arXiv v2", "links": {"arxiv": "https://arxiv.org/abs/2004.13912"},
   "tasks": ["model-explanation", "tabular-classification", "tabular-regression"],
   "fam": ["interpretable-models", "deep-learning"], "par": ["supervised"],
   "proposes": ["Neural Additive Models (NAMs): GAMs whose shape functions are per-feature neural nets", "ExU (exp-centered) hidden units for jagged shape functions"],
   "claims": [
     ("NAMs learn a linear combination of neural networks, each of which takes a single input feature (a generalized additive model "
      "with neural-net shape functions), trained jointly.", "Abstract",
      "NAMs learn a linear combination of neural networks that each attend to a single input feature."),
     ("Interpretability argument: the per-feature shape-function plots are not just an explanation but an exact description of how "
      "the NAM computes a prediction.", "Intelligibility and Modularity of NAMs",
      "Please note these shape function plots are not just an explanation but an exact description of how NAMs compute a prediction."),
     ("As an example of intelligibility, the authors state that they validated the behaviour of NAMs on MIMIC-II with a doctor "
      "(Appendix A.1, a qualitative discussion of shape functions).",
      "Intelligibility and Modularity of NAMs",
      "A decision-maker can easily interpret such models and understand exactly how they make decisions, for example, we validated "
      "the behavior of NAMs on the MIMIC-II dataset [38] with a doctor (Appendix A.1)."),
     ("NAMs achieve performance comparable to Explainable Boosting Machines on the classification and regression datasets, evaluated "
      "by 5-fold cross validation.", "Evaluating the Accuracy of NAMs",
      "NAMs achieve comparable performance to EBMs on both classification and regression datasets, making them a competitive "
      "alternative to EBMs."),
     ("NAM hyperparameters (learning rate, output penalty, weight decay, dropout, feature dropout) are tuned by Bayesian optimization "
      "based on cross-validation performance with a single train-validation split per fold.", "Appendix (Experimental Details)",
      "For computational efficiency, we tune these hyperparameters using Bayesian optimization [11, 39] based on cross-validation "
      "performance with a single train-validation split for each fold."),
     ("Baseline tuning: EBMs use the open-source implementation with parameters specified by prior work (linear models and decision "
      "trees are tuned by grid search).", "Appendix (Hyperparameters)",
      "We use the open-source implementation [26] with the parameters specified by prior work [5] for a fair comparison."),
     ("Limitation/scope: pairwise feature interactions are not considered, to keep the paper focused on additive modelling.",
      "Related Work",
      "We don’t consider such interactions to keep the paper focused on additive modeling with neural nets."),
   ],
   "notes": ("PDF states: 35th Conference on Neural Information Processing Systems (NeurIPS 2021). Datasets in the main accuracy table: "
             "MIMIC-II, Credit (fraud), California Housing, FICO; plus COMPAS and synthetic multitask data. Main text says AUC denotes area "
             "under the precision-recall curve, while the COMPAS table caption says ROC AUC. Tuning protocol for the XGBoost baseline was "
             "not found in the text. Authors include Rich Caruana (Microsoft Research), whose prior work is the EBM/GA2M baseline. "
             "No quantitative explanation-quality metric was found; interpretability is argued from the additive structure. "
             "Source code is announced at 'neural-additive-models.github.io' (not added as a link).")},

  {"id": "arxiv-1905.04610", "title": "Explainable AI for Trees: From Local Explanations to Global Understanding",
   "authors": ["Scott M. Lundberg", "Gabriel Erion", "Hugh Chen", "Alex DeGrave", "Jordan M. Prutkin", "Bala Nair", "Ronit Katz",
               "Jonathan Himmelfarb", "Nisha Bansal", "Su-In Lee"],
   "year": 2019, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/1905.04610", "code": "https://github.com/suinleelab/treeexplainer-study"},
   "tasks": ["model-explanation", "tabular-classification", "tabular-regression"],
   "fam": ["feature-attribution", "tree-ensembles", "gradient-boosted-trees"], "par": ["post-hoc"],
   "proposes": ["TreeExplainer (Tree SHAP): exact polynomial-time SHAP values for tree ensembles", "SHAP interaction values",
                "Global tools built from local explanations (summary/dependence plots, explanation embeddings, loss-based model monitoring)"],
   "claims": [
     ("TreeExplainer is a local explanation method for trees that computes optimal local explanations, defined by game-theoretic "
      "properties, in tractable (polynomial) time.", "Introduction",
      "Here we propose TreeExplainer, a new local explanation method for trees that enables the tractable computation of optimal local "
      "explanations, as defined by desirable properties from game theory (Section 2.5)."),
     ("Axiomatic justification: within additive feature attribution methods, Shapley values are the only way to satisfy local accuracy, "
      "consistency and missingness.", "Results (TreeExplainer)",
      "results from game theory imply the Shapley values are the only way to satisfy three important properties: local accuracy, "
      "consistency, and missingness (Methods 9)"),
     ("By default TreeExplainer computes conditional expectations by tree traversal; an option enforces feature independence and "
      "supports explaining the model's loss.", "Results (TreeExplainer)",
      "By default, TreeExplainer computes conditional expectations using tree traversal, but it also provides an option that enforces "
      "feature independence and supports explaining a model’s loss function (Methods 10)."),
     ("Explanation quality was evaluated with 21 metrics designed by the authors, applied to eight explanation methods across three "
      "model types and three datasets.", "Results (TreeExplainer)",
      "We designed 21 metrics to comprehensively evaluate the performance of local explanation methods, and applied these metrics to "
      "eight different explanation methods across three different model types and three datasets (Methods 11)."),
     ("The benchmark hides features by mean masking, by resampling under feature independence, or by imputation; metrics based on "
      "retraining the model were deliberately excluded because they can be misleading in certain situations.",
      "Methods (Benchmark evaluation metrics)",
      "After extensive consideration, we did not include metrics based on retraining the original model since, while informative, "
      "these can produce misleading results in certain situations."),
     ("A user-study benchmark of 12 scenarios compared methods with human consensus explanations of simple models; Shapley-value-based "
      "methods agreed with human intuition in all tested scenarios, unlike the Saabas heuristic.", "Results (TreeExplainer)",
      "In contrast to the heuristic Saabas values, Shapley value based explanation methods agree with human intuition in all the "
      "scenarios we tested (Methods 12)."),
     ("Failure mode of the prior Saabas heuristic: it is inconsistent, i.e. a model can be changed to make a feature clearly more "
      "important while the Saabas attribution of that feature decreases.", "Results",
      "This causes Saabas values to be inconsistent, which means we can modify a model to make a feature clearly more important, and "
      "yet the Saabas value attributed to that feature will decrease (Supplementary Figure 2)."),
   ],
   "notes": ("Conflict of interest to note: the authors developed SHAP/TreeExplainer and also designed the 21-metric benchmark on which "
             "TreeExplainer is reported to be best. Data: three medical tabular datasets (NHANES I mortality with Cox loss, CRIC kidney "
             "disease classification, hospital procedure duration regression). The paper also reports gradient boosted trees "
             "outperforming lasso linear models and neural networks on these datasets (hyperparameters chosen on validation sets, "
             "100 random train/test splits for significance); not carded as a claim here. Kumar et al. (arxiv-2002.11097) classify "
             "TreeSHAP as a conditional method; Chen et al. (arxiv-2006.16234) discuss the interventional vs observational choice.")},

  {"id": "arxiv-2006.16234", "title": "True to the Model or True to the Data?",
   "authors": ["Hugh Chen", "Joseph D. Janizek", "Scott Lundberg", "Su-In Lee"],
   "year": 2020, "version": "arXiv v1",
   "links": {"arxiv": "https://arxiv.org/abs/2006.16234",
             "code": "https://github.com/slundberg/shap/blob/master/shap/explainers/linear.py"},
   "tasks": ["model-explanation"], "fam": ["feature-attribution", "linear-models"], "par": ["post-hoc"],
   "proposes": ["Argument that the interventional vs observational Shapley value function choice is application dependent ('true to the model' vs 'true to the data')",
                "Efficient observational (conditional) Shapley values for linear models under a multivariate normal assumption"],
   "claims": [
     ("Responding to Kumar et al. (2020), who suggest the two value functions present an irreconcilable problem, the authors argue "
      "that interventional and observational Shapley values are each meaningful when applied in the proper context (the choice is "
      "application dependent).", "Introduction",
      "in this paper, we argue that rather than representing some critical flaw in using the Shapley value for feature attribution, "
      "each approach is meaningful when applied in the proper context"),
     ("Assumption: to compute observational Shapley values for linear models, inputs are assumed to be multivariate normal.",
      "Linear SHAP",
      "Estimating this conditional expectation is hard in general, so we assume the inputs x ∼N(µ, Σ) are multivariate normal."),
     ("On NHANES mortality data, a feature excluded from a linear model (BMI) receives importance under observational Shapley values "
      "because of its correlation with the used features.", "Explaining a feature not used by the model",
      "This implies that even though BMI is not included in the model, the correlation between BMI and other features makes BMI "
      "important under observational Shapley values."),
     ("'True to the model' evaluation on LendingClub with logistic regression: features are ranked by Shapley value, mean-imputed one "
      "at a time (up to 10), and the change in predicted log-odds of default is measured.", "True to the Model",
      "We then measured the change in the model’s predicted log odds of default after each feature (up to 10 features) had been "
      "mean-imputed."),
     ("In that loan setting, interventional Shapley values led to significantly better results than observational ones.",
      "True to the Model",
      "We find that using the interventional conditional expectation leads to significantly better results than the observational "
      "conditional expectation (Figure 3)."),
     ("'True to the data' evaluation with ground truth: drug-response labels are simulated from 40 randomly selected causal genes on "
      "real RNA-seq data; for a Lasso model, observational Shapley values recover more true causal genes than interventional ones.",
      "True to the Data",
      "To create an experimental setting where we have access to the ground truth, we take the real RNA-seq data and simulate a drug "
      "response label as a function of 40 randomly selected causal genes (out of 1000 total genes)."),
     ("Limitation: the best case for feature attribution is when the perturbed features are independent, in which case observational "
      "and interventional attributions coincide.", "Conclusion",
      "Currently, the best case for feature attribution is when the features that being perturbed are independent to start with."),
         ("Two value functions for Shapley-based local attribution: the observational conditional expectation v(S) = E[f(X) | X_S = x_S] (Eq. 2) and the interventional conditional expectation v(S) = E[f(x) | do(S)] (Eq. 3), which intervenes on the features by breaking the dependence between features in S and the remaining features.", "Section 1.1 (Choice of value function)", "There are two ways the model’s output (f : x ∈R|N|×1 →R1) for a particular sample is used to deﬁne v(S):"),
         ("Shapley value as an average over orderings (Eq. 1): phi_i = (1/M!) sum over permutations R of [v(S_R union {i}) - v(S_R)], where S_R is the set of players joining before player i.", "Section 1 (Shapley values)", "where R is one possible permutation of the order in which the players join the coalition, SR is the set of players joining the coalition before player i"),
   ],
   "notes": ("All analysis is on linear models (linear regression, logistic regression, Lasso, Elastic Net). Co-authored by Scott Lundberg "
             "(SHAP author). Explicitly responds to Kumar et al. 2020 (arxiv-2002.11097), arguing the two value functions are each "
             "meaningful in the proper context rather than an irreconcilable problem.")},

  {"id": "arxiv-2002.11097", "title": "Problems with Shapley-value-based explanations as feature importance measures",
   "authors": ["I. Elizabeth Kumar", "Suresh Venkatasubramanian", "Carlos Scheidegger", "Sorelle Friedler"],
   "year": 2020, "version": "arXiv v2", "links": {"arxiv": "https://arxiv.org/abs/2002.11097"},
   "tasks": ["model-explanation"], "fam": ["feature-attribution"], "par": ["post-hoc"],
   "proposes": ["Mathematical and human-centric critique of Shapley-value-based feature importance"],
   "claims": [
     ("Mathematical problems arise when Shapley values are used for feature importance, and mitigating them necessarily adds complexity "
      "such as the need for causal reasoning.", "Abstract",
      "We show that mathematical problems arise when Shapley values are used for feature importance, and that the solutions to mitigate "
      "these necessarily induce further complexity, such as the need for causal reasoning."),
     ("Choosing between conditional and interventional value functions is a catch-22: conditional methods require extra modelling of "
      "feature dependencies, interventional methods induce an out-of-distribution problem.", "Conditional versus interventional distributions",
      "Unfortunately, the decision between the two types of value functions is a catch-22."),
     ("With conditional value functions, adding a redundant copy of a feature changes the relative attributions of the other features, "
      "even though the model is effectively the same.", "Issues with conditional distributions",
      "The relative apparent importances of A and B thus depend on whether C is considered to be a third feature, even though the two "
      "functions are effectively the same."),
     ("Interventional value functions fundamentally rely on evaluating the model on out-of-distribution samples, which makes them "
      "highly sensitive to model properties not relevant to what it learned about the training data.", "Issues with interventional distributions",
      "Methods which use an interventional value function fundamentally rely on evaluating a model on out-of-distribution samples (Figure 1)."),
     ("Additivity issue: for multiplicative functions of independent, zero-centred features, every feature receives the same Shapley "
      "value regardless of its value.", "Additivity constraints",
      "This property will, in fact, hold for all multiplicative functions of independently distributed, zero-centered data."),
     ("A large Shapley influence of a feature does not necessarily imply that changing that feature will change the outcome favourably, "
      "and Shapley-value frameworks do not explicitly attempt to guide how a user might alter their situation (unlike actionable-recourse methods).", "Using Shapley-valued based methods to enable action",
      "Further, observing that a certain feature carries a large influence over the model does not necessarily imply that changing that "
      "feature (even significantly) will change the outcome favorably."),
     ("Evaluation evidence is drawn from the literature rather than new experiments; e.g. a cited human-grounded evaluation of SHAP found "
      "no evidence that it helped users assess prediction correctness.", "Shapley-based explanations for normative evaluation",
      "Weerts et al. (2019), for instance, conducted a human-grounded evaluation of SHAP and did not find evidence that it helped users "
      "assess the correctness of predictions."),
   ],
   "notes": ("PDF states: Proceedings of the 37th International Conference on Machine Learning (ICML 2020), PMLR 119. No experiments were "
             "found in the text; the critique is analytic (toy functions) plus literature on human explanation. Classifies TreeSHAP as a "
             "conditional method and KernelSHAP as effectively interventional (Table 1). Chen et al. (arxiv-2006.16234) respond to this paper.")},
]

build(SPECS, base_note="Selected for the topic article requested by the user (2026-10-03): interpretability; carded by a subagent. "
                       "Results tables not recorded; claims only.")
