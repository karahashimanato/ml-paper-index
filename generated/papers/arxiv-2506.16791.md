<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabArena: A Living Benchmark for Machine Learning on Tabular Data

- カード: [`arxiv-2506.16791`](../../papers/arxiv-2506.16791.yaml)
- 著者: Nick Erickson, Lennart Purucker, Andrej Tschalzev, David Holzmüller, Prateek Mutalik Desai, David Salinas, Frank Hutter
- 年・掲載: 2025 NeurIPS 2025 Datasets and Benchmarks Track
- 原論文: [PDF](https://arxiv.org/pdf/2506.16791v4)(arXiv v4、カード作成時に読んだ版)
- タグ: automl-systems, gradient-boosted-trees, heterogeneous-ensembles, in-context-learning, linear-models, random-forests, supervised, tabular-classification, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** GBDTs remain strong on practical tabular data, but deep learning methods caught up under larger time budgets with ensembling.([Abstract, p.1](https://arxiv.org/pdf/2506.16791v4#page=1 "While gradient-boosted trees are still strong contenders on practical tabular datasets, we observe that deep learning methods have caught up under larger time budgets with ensembling."))
- **c2** Tabular foundation models excel on smaller datasets.([Abstract, p.1](https://arxiv.org/pdf/2506.16791v4#page=1 "At the same time, foundation models excel on smaller datasets."))
- **c3** Ensembles across models advance the state of the art.([Abstract, p.1](https://arxiv.org/pdf/2506.16791v4#page=1 "Finally, we show that ensembles across models advance the state-of-the-art in tabular machine learning."))
- **c4** Some deep learning models are overrepresented in cross-model ensembles due to validation-set overfitting.([Abstract, p.1](https://arxiv.org/pdf/2506.16791v4#page=1 "We observe that some deep learning models are overrepresented in cross-model ensembles due to validation set overfitting"))
- **c5** 51 datasets were manually curated out of 1053 datasets used in tabular research.([Section 1, p.2](https://arxiv.org/pdf/2506.16791v4#page=2 "We investigate 1053 datasets used in tabular data research and carefully, manually curate a set of 51 datasets out of these"))
- **c6** 16 models were curated, including 3 tabular foundation models.([Section 1, p.2](https://arxiv.org/pdf/2506.16791v4#page=2 "We curate 16 tabular machine learning models, including 3 tabular foundation models"))
- **c7** TabArena-v0.1 covers IID classification and regression in the small-to-medium data regime (non-IID, tiny and large data are out of scope).([Section 1, p.2](https://arxiv.org/pdf/2506.16791v4#page=2 "Tabular classification and regression for independent and identically distributed (IID) data, spanning the small to medium data regime."))
- **c8** Outer evaluation: 10x repeated 3-fold CV for datasets under 2,500 samples, otherwise 3 repeats.([Section 2.3, p.6](https://arxiv.org/pdf/2506.16791v4#page=6 "for datasets with less than 2 500 samples, we use 10 times repeated 3-fold outer cross-validation; (II) for all other datasets, we use 3 repeats."))
- **c9** Elo is computed from ROC AUC (binary), log-loss (multiclass) and RMSE (regression).([Section 2.3, p.6](https://arxiv.org/pdf/2506.16791v4#page=6 "In our main results, Elo scores are computed using ROC AUC for binary classification, log-loss for multiclass classification, and RMSE for regression."))
- **c10** Elo is calibrated so that the default RandomForest is 1000; 95% CIs from 200 bootstrap rounds.([Section 2.3, p.6](https://arxiv.org/pdf/2506.16791v4#page=6 "We calibrate 1000 Elo to the performance of our default random forest configuration across all figures"))
- **c11** In the conventional tuning regime (single best configuration), CatBoost ranked first.([Section 3.1, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "In line with previous work [33], CatBoost is ranked first in the conventional tuning regime (Figure 1)."))
- **c12** After post-hoc ensembling of hyperparameter configurations, neural networks were the strongest single models on average.([Section 3.1, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "after post-hoc ensembling, neural networks are the strongest single models on average in TabArena-v0.1."))
- **c13** On datasets within its constraints, TabPFNv2 outperformed related approaches by a large margin.([Section 3.1, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "TabPFNv2 outperforms related approaches by a large margin, establishing tabular foundation models as the go-to solution for datasets within their constraints."))
- **c14** Using holdout instead of cross-validation for model selection greatly underestimates all models and favors models that already ensemble.([Section 3.2, p.8](https://arxiv.org/pdf/2506.16791v4#page=8 "when using holdout validation instead of cross-validation for model selection, all models are greatly underestimated, and performance is biased in favor of models that already use ensembling."))
- **c15** Given their training cost GBDTs are strong; RealMLP only dominates them after considerable training time with 25+ ensembled configurations.([Section 3.1, p.8](https://arxiv.org/pdf/2506.16791v4#page=8 "RealMLP only starts to dominate them after a considerable amount of training time with an ensemble of 25+ configurations."))
- **c16** Authors call GBDT vs. deep learning a false dichotomy: both families contribute to cross-model ensembles that outperform individual families.([Section 3.2, p.9](https://arxiv.org/pdf/2506.16791v4#page=9 "We argue that the battle between GBDTs and deep learning is a false dichotomy, as both model families contribute to ensembles that strongly outperform individual model families"))
- **c17** Top leaderboard models are not necessarily those with the highest weights in the cross-model ensemble.([Section 3.2, p.9](https://arxiv.org/pdf/2506.16791v4#page=9 "models with the highest performance on the leaderboard are not necessarily the ones with the highest weights"))
- **c18** Limitation: a fixed set of 200 random hyperparameter configurations is used (no study of HPO variance or advanced HPO).([Section 5, p.10](https://arxiv.org/pdf/2506.16791v4#page=10 "We use a fixed set of 200 random hyperparameter configurations to enable the study of ensemble pipelines."))
- **c19** Limitation: no feature engineering beyond the given dataset state; it could change the ranking.([Section 5, p.10](https://arxiv.org/pdf/2506.16791v4#page=10 "we assess predictive performance without feature engineering on top of the existing dataset state."))
- **c20** TabPFNv2 is only run on datasets with up to 10,000 training samples, 500 features and 10 classes; TabICL on classification with up to 100,000 samples and 500 features.([Section 2.1, p.3](https://arxiv.org/pdf/2506.16791v4#page=3 "This only affects TabPFNv2, which is restricted to datasets with up to 10, 000 training samples, 500 features, and 10 classes for classification tasks"))
- **c21** The TabPFNv2-compatible subset has 33 datasets and the TabICL-compatible subset 36 classification datasets.([Figure 4 caption, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "For TabPFNv2, we obtain 33 datasets (≤10K training samples, ≤500 features). For TabICL, we obtain 36 classification datasets (≤100K, ≤500)."))
- **c22** Competing interest: one author co-authored RealMLP and TabICL.([Competing Interests, p.11](https://arxiv.org/pdf/2506.16791v4#page=11 "D.H. is one of the authors of RealMLP and one of the authors of TabICL."))
- **c23** Competing interest: two authors are among the authors of TabPFNv2 (one affiliated with Prior Labs).([Competing Interests, p.11](https://arxiv.org/pdf/2506.16791v4#page=11 "L.P. and F.H. are a subset of the authors of TabPFNv2."))
- **c24** Reference pipeline: AutoGluon 1.3, best_quality preset, 4 hours of training.([Section 2.3, p.6](https://arxiv.org/pdf/2506.16791v4#page=6 "We select the predictive machine learning system AutoGluon [19] (version 1.3, with the best_quality preset and 4 hours for training) as the first official TabArena reference pipeline."))

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| CatBoost (tuned) | All other models (tuned, single best configuration) | Elo, tuning regime without post-hoc ensembling (Figure 1). | `tabarena-v0-1` | [Section 3.1, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "In line with previous work [33], CatBoost is ranked first in the conventional tuning regime (Figure 1).") |
| CatBoost (tuned) | TabM, LightGBM, RealMLP (tuned, without post-hoc ensembling) | Elo; these three are the top-3 only after post-hoc ensembling (Figure 1). | `tabarena-v0-1` | [Section 3.1, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "the top three models in our leaderboard (TabM, LightGBM, RealMLP; see Figure 1) would all be worse than the actual fourth-best model (CatBoost) without post-hoc ensembling.") |
| TabPFNv2 (tuned + ensembled) | AutoGluon 1.3 (4h) | Elo on the TabPFNv2-compatible subset (Figure 4 left). | `tabarena-v0-1-tabpfnv2-subset` | [Section 3.1, p.7](https://arxiv.org/pdf/2506.16791v4#page=7 "TabPFNv2 with tuning and post-hoc ensembling again outperforms AutoGluon") |
| TabArena ensemble (all models, simulated) | All individual models and AutoGluon 1.3 (4h) | Elo (Figure 7 left). | `tabarena-v0-1` | [Section 3.2, p.9](https://arxiv.org/pdf/2506.16791v4#page=9 "a simulated ensembling pipeline using all models in TabArena outperforms all individual models and AutoGluon") |

