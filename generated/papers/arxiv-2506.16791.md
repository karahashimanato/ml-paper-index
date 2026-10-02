<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabArena: A Living Benchmark for Machine Learning on Tabular Data

- カード: [`arxiv-2506.16791`](../../papers/arxiv-2506.16791.yaml)
- 著者: Nick Erickson, Lennart Purucker, Andrej Tschalzev, David Holzmüller, Prateek Mutalik Desai, David Salinas, Frank Hutter
- 年・掲載: 2025 NeurIPS 2025 Datasets and Benchmarks Track
- タグ: automl-systems, gradient-boosted-trees, heterogeneous-ensembles, in-context-learning, linear-models, random-forests, supervised, tabular-classification, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

- **c1** GBDTs remain strong on practical tabular data, but deep learning methods caught up under larger time budgets with ensembling.(Abstract)
- **c2** Tabular foundation models excel on smaller datasets.(Abstract)
- **c3** Ensembles across models advance the state of the art.(Abstract)
- **c4** Some deep learning models are overrepresented in cross-model ensembles due to validation-set overfitting.(Abstract)
- **c5** 51 datasets were manually curated out of 1053 datasets used in tabular research.(Section 1)
- **c6** 16 models were curated, including 3 tabular foundation models.(Section 1)
- **c7** TabArena-v0.1 covers IID classification and regression in the small-to-medium data regime (non-IID, tiny and large data are out of scope).(Section 1)
- **c8** Outer evaluation: 10x repeated 3-fold CV for datasets under 2,500 samples, otherwise 3 repeats.(Section 2.3)
- **c9** Elo is computed from ROC AUC (binary), log-loss (multiclass) and RMSE (regression).(Section 2.3)
- **c10** Elo is calibrated so that the default RandomForest is 1000; 95% CIs from 200 bootstrap rounds.(Section 2.3)
- **c11** In the conventional tuning regime (single best configuration), CatBoost ranked first.(Section 3.1)
- **c12** After post-hoc ensembling of hyperparameter configurations, neural networks were the strongest single models on average.(Section 3.1)
- **c13** On datasets within its constraints, TabPFNv2 outperformed related approaches by a large margin.(Section 3.1)
- **c14** Using holdout instead of cross-validation for model selection greatly underestimates all models and favors models that already ensemble.(Section 3.2)
- **c15** Given their training cost GBDTs are strong; RealMLP only dominates them after considerable training time with 25+ ensembled configurations.(Section 3.1)
- **c16** Authors call GBDT vs. deep learning a false dichotomy: both families contribute to cross-model ensembles that outperform individual families.(Section 3.2)
- **c17** Top leaderboard models are not necessarily those with the highest weights in the cross-model ensemble.(Section 3.2)
- **c18** Limitation: a fixed set of 200 random hyperparameter configurations is used (no study of HPO variance or advanced HPO).(Section 5)
- **c19** Limitation: no feature engineering beyond the given dataset state; it could change the ranking.(Section 5)
- **c20** TabPFNv2 is only run on datasets with up to 10,000 training samples, 500 features and 10 classes; TabICL on classification with up to 100,000 samples and 500 features.(Section 2.1)
- **c21** The TabPFNv2-compatible subset has 33 datasets and the TabICL-compatible subset 36 classification datasets.(Figure 4 caption)
- **c22** Competing interest: one author co-authored RealMLP and TabICL.(Competing Interests)
- **c23** Competing interest: two authors are among the authors of TabPFNv2 (one affiliated with Prior Labs).(Competing Interests)
- **c24** Reference pipeline: AutoGluon 1.3, best_quality preset, 4 hours of training.(Section 2.3)

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| CatBoost (tuned) | All other models (tuned, single best configuration) | Elo, tuning regime without post-hoc ensembling (Figure 1). | `tabarena-v0-1` | Section 3.1 |
| CatBoost (tuned) | TabM, LightGBM, RealMLP (tuned, without post-hoc ensembling) | Elo; these three are the top-3 only after post-hoc ensembling (Figure 1). | `tabarena-v0-1` | Section 3.1 |
| TabPFNv2 (tuned + ensembled) | AutoGluon 1.3 (4h) | Elo on the TabPFNv2-compatible subset (Figure 4 left). | `tabarena-v0-1-tabpfnv2-subset` | Section 3.1 |
| TabArena ensemble (all models, simulated) | All individual models and AutoGluon 1.3 (4h) | Elo (Figure 7 left). | `tabarena-v0-1` | Section 3.2 |

