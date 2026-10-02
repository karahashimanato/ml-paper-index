"""TabArena (Erickson et al., NeurIPS 2025 D&B) のカード。結果は図(Elo)のみのため、本文に明記された勝敗を relations として記録する。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, register, write_card  # noqa: E402

P = Paper("arxiv-2506.16791")

claims = P.claims([
  ("GBDTs remain strong on practical tabular data, but deep learning methods caught up under larger time budgets with ensembling.", "Abstract",
   "While gradient-boosted trees are still strong contenders on practical tabular datasets, we observe that deep learning methods have caught up under larger time budgets with ensembling."),
  ("Tabular foundation models excel on smaller datasets.", "Abstract",
   "At the same time, foundation models excel on smaller datasets."),
  ("Ensembles across models advance the state of the art.", "Abstract",
   "Finally, we show that ensembles across models advance the state-of-the-art in tabular machine learning."),
  ("Some deep learning models are overrepresented in cross-model ensembles due to validation-set overfitting.", "Abstract",
   "We observe that some deep learning models are overrepresented in cross-model ensembles due to validation set overfitting"),
  ("51 datasets were manually curated out of 1053 datasets used in tabular research.", "Section 1",
   "We investigate 1053 datasets used in tabular data research and carefully, manually curate a set of 51 datasets out of these"),
  ("16 models were curated, including 3 tabular foundation models.", "Section 1",
   "We curate 16 tabular machine learning models, including 3 tabular foundation models"),
  ("TabArena-v0.1 covers IID classification and regression in the small-to-medium data regime (non-IID, tiny and large data are out of scope).", "Section 1",
   "Tabular classification and regression for independent and identically distributed (IID) data, spanning the small to medium data regime."),
  ("Outer evaluation: 10x repeated 3-fold CV for datasets under 2,500 samples, otherwise 3 repeats.", "Section 2.3",
   "for datasets with less than 2 500 samples, we use 10 times repeated 3-fold outer cross-validation; (II) for all other datasets, we use 3 repeats."),
  ("Elo is computed from ROC AUC (binary), log-loss (multiclass) and RMSE (regression).", "Section 2.3",
   "In our main results, Elo scores are computed using ROC AUC for binary classification, log-loss for multiclass classification, and RMSE for regression."),
  ("Elo is calibrated so that the default RandomForest is 1000; 95% CIs from 200 bootstrap rounds.", "Section 2.3",
   "We calibrate 1000 Elo to the performance of our default random forest configuration across all figures"),
  ("In the conventional tuning regime (single best configuration), CatBoost ranked first.", "Section 3.1",
   "In line with previous work [33], CatBoost is ranked first in the conventional tuning regime (Figure 1)."),
  ("After post-hoc ensembling of hyperparameter configurations, neural networks were the strongest single models on average.", "Section 3.1",
   "after post-hoc ensembling, neural networks are the strongest single models on average in TabArena-v0.1."),
  ("On datasets within its constraints, TabPFNv2 outperformed related approaches by a large margin.", "Section 3.1",
   "TabPFNv2 outperforms related approaches by a large margin, establishing tabular foundation models as the go-to solution for datasets within their constraints."),
  ("Using holdout instead of cross-validation for model selection greatly underestimates all models and favors models that already ensemble.", "Section 3.2",
   "when using holdout validation instead of cross-validation for model selection, all models are greatly underestimated, and performance is biased in favor of models that already use ensembling."),
  ("Given their training cost GBDTs are strong; RealMLP only dominates them after considerable training time with 25+ ensembled configurations.", "Section 3.1",
   "RealMLP only starts to dominate them after a considerable amount of training time with an ensemble of 25+ configurations."),
  ("Authors call GBDT vs. deep learning a false dichotomy: both families contribute to cross-model ensembles that outperform individual families.", "Section 3.2",
   "We argue that the battle between GBDTs and deep learning is a false dichotomy, as both model families contribute to ensembles that strongly outperform individual model families"),
  ("Top leaderboard models are not necessarily those with the highest weights in the cross-model ensemble.", "Section 3.2",
   "models with the highest performance on the leaderboard are not necessarily the ones with the highest weights"),
  ("Limitation: a fixed set of 200 random hyperparameter configurations is used (no study of HPO variance or advanced HPO).", "Section 5",
   "We use a fixed set of 200 random hyperparameter configurations to enable the study of ensemble pipelines."),
  ("Limitation: no feature engineering beyond the given dataset state; it could change the ranking.", "Section 5",
   "we assess predictive performance without feature engineering on top of the existing dataset state."),
  ("TabPFNv2 is only run on datasets with up to 10,000 training samples, 500 features and 10 classes; TabICL on classification with up to 100,000 samples and 500 features.", "Section 2.1",
   "This only affects TabPFNv2, which is restricted to datasets with up to 10, 000 training samples, 500 features, and 10 classes for classification tasks"),
  ("The TabPFNv2-compatible subset has 33 datasets and the TabICL-compatible subset 36 classification datasets.", "Figure 4 caption",
   "For TabPFNv2, we obtain 33 datasets (≤10K training samples, ≤500 features). For TabICL, we obtain 36 classification datasets (≤100K, ≤500)."),
  ("Competing interest: one author co-authored RealMLP and TabICL.", "Competing Interests",
   "D.H. is one of the authors of RealMLP and one of the authors of TabICL."),
  ("Competing interest: two authors are among the authors of TabPFNv2 (one affiliated with Prior Labs).", "Competing Interests",
   "L.P. and F.H. are a subset of the authors of TabPFNv2."),
  ("Reference pipeline: AutoGluon 1.3, best_quality preset, 4 hours of training.", "Section 2.3",
   "We select the predictive machine learning system AutoGluon [19] (version 1.3, with the best_quality preset and 4 hours for training) as the first official TabArena reference pipeline."),
])


def rel(winner, loser, basis, bench, quote, location):
    return {"winner": winner, "loser": loser, "basis": basis, "benchmark": bench, "location": location, "page": P.page_of(quote), "quote": quote}


relations = [
  rel("CatBoost (tuned)", "All other models (tuned, single best configuration)", "Elo, tuning regime without post-hoc ensembling (Figure 1).",
      "tabarena-v0-1", "In line with previous work [33], CatBoost is ranked first in the conventional tuning regime (Figure 1).", "Section 3.1"),
  rel("CatBoost (tuned)", "TabM, LightGBM, RealMLP (tuned, without post-hoc ensembling)",
      "Elo; these three are the top-3 only after post-hoc ensembling (Figure 1).", "tabarena-v0-1",
      "the top three models in our leaderboard (TabM, LightGBM, RealMLP; see Figure 1) would all be worse than the actual fourth-best model (CatBoost) without post-hoc ensembling.",
      "Section 3.1"),
  rel("TabPFNv2 (tuned + ensembled)", "AutoGluon 1.3 (4h)", "Elo on the TabPFNv2-compatible subset (Figure 4 left).", "tabarena-v0-1-tabpfnv2-subset",
      "TabPFNv2 with tuning and post-hoc ensembling again outperforms AutoGluon", "Section 3.1"),
  rel("TabArena ensemble (all models, simulated)", "All individual models and AutoGluon 1.3 (4h)", "Elo (Figure 7 left).", "tabarena-v0-1",
      "a simulated ensembling pipeline using all models in TabArena outperforms all individual models and AutoGluon", "Section 3.2"),
]

write_card({
  "id": P.id,
  "title": "TabArena: A Living Benchmark for Machine Learning on Tabular Data",
  "authors": ["Nick Erickson", "Lennart Purucker", "Andrej Tschalzev", "David Holzmüller", "Prateek Mutalik Desai", "David Salinas", "Frank Hutter"],
  "year": 2025,
  "venue": "NeurIPS 2025 Datasets and Benchmarks Track",
  "links": {"arxiv": "https://arxiv.org/abs/2506.16791", "url": "https://tabarena.ai"},
  "source": {"version": "arXiv v4", "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256()},
  "tags": {"tasks": ["tabular-classification", "tabular-regression"],
           "method_families": ["gradient-boosted-trees", "tabular-mlp", "tabular-foundation-model", "random-forests", "linear-models",
                               "automl-systems", "heterogeneous-ensembles"],
           "paradigms": ["supervised", "in-context-learning"]},
  "proposes": ["TabArena living benchmark (v0.1)", "TabArena-Lite"],
  "claims": claims,
  "results": [],
  "relations": relations,
  "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False,
           "notes": ("All main results are figures (Elo bars with bootstrap CIs); no numeric result tables in the paper, so only relations from explicit statements were recorded. "
                     "This card describes TabArena-v0.1 as in arXiv v4; the live leaderboard at tabarena.ai changes over time and is NOT covered by this card. "
                     "Some authors are authors of evaluated models (TabPFNv2, RealMLP, TabICL; c22, c23).")},
})

COMMON = {"split": "Outer CV: 10x repeated 3-fold for datasets with <2,500 samples, 3 repeats otherwise; class-stratified for classification (Section 2.3).",
          "preprocessing": "Model-specific pipelines implemented with model authors; no extra feature engineering (Sections 2.1, 5).",
          "tuning": "Default, tuned (best of 200 fixed random configurations, selected by inner cross-validation) and tuned + post-hoc weighted ensembling of configurations (Sections 2.1, 3.1, 5).",
          "repetitions": "Elo with 1000 = default RandomForest; 95% CIs from 200 bootstrap rounds (Section 2.3)."}
elo = [{"name": "elo", "higher_is_better": True,
        "definition": "Pairwise Elo across datasets from ROC AUC (binary), log-loss (multiclass), RMSE (regression); default RandomForest = 1000."}]
register(P.id, [
  {"id": "tabarena-v0-1", "scope": "public", "task": "tabular-classification",
   "dataset": "TabArena-v0.1: 51 curated IID datasets (classification and regression)", "protocol": COMMON, "metrics": elo, "defined_in": P.id,
   "notes": "Versioned: later TabArena versions must be registered as new IDs. Mixes classification and regression."},
  {"id": "tabarena-v0-1-tabpfnv2-subset", "scope": "public", "task": "tabular-classification",
   "dataset": "TabArena-v0.1 datasets within TabPFNv2 constraints (33 datasets: <=10K training samples, <=500 features)", "protocol": COMMON, "metrics": elo, "defined_in": P.id},
  {"id": "tabarena-v0-1-tabicl-subset", "scope": "public", "task": "tabular-classification",
   "dataset": "TabArena-v0.1 classification datasets within TabICL constraints (36 datasets: <=100K samples, <=500 features)", "protocol": COMMON, "metrics": elo, "defined_in": P.id},
])
print(len(claims), "claims,", len(relations), "relations")
