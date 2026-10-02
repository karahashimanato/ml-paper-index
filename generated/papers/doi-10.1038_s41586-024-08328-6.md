<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Accurate predictions on small data with a tabular foundation model

- カード: [`doi-10.1038_s41586-024-08328-6`](../../papers/doi-10.1038_s41586-024-08328-6.yaml)
- 著者: Noah Hollmann, Samuel Müller, Lennart Purucker, Arjun Krishnakumar, Max Körfer, Shi Bin Hoo, Robin Tibor Schirrmeister, Frank Hutter
- 年・掲載: 2025 Nature 637, 319-326 (2025)
- タグ: automl-systems, gradient-boosted-trees, in-context-learning, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

- **c1** TabPFN v2 outperformed all previous methods on datasets with up to 10,000 samples by a wide margin, with much less training time.(Abstract)
- **c2** In 2.8 s, TabPFN v2 outperformed an ensemble of the strongest baselines tuned for 4 h (classification).(Abstract)
- **c3** Compared with the 2023 TabPFN, v2 scales to 50x larger datasets, supports regression, categorical data and missing values, and is robust to unimportant features and outliers.(Introduction)
- **c4** Training only on synthetic data avoids privacy/copyright issues and contamination of training data with test data.(Architecture / prior)
- **c5** About 100 million synthetic datasets (from structural causal models) are generated per model training.(Synthetic data)
- **c6** The architecture uses two-way attention: each cell attends within its row, then within its column, making it invariant to sample and feature order.(Architecture)
- **c7** Primary evaluation: 29 classification and 28 regression datasets from the AutoML Benchmark and OpenML-CTR23 with up to 10,000 samples, 500 features and 10 classes.(Results)
- **c8** Each dataset and method: 10 repetitions with different seeds and 90/10 train/test splits.(Results)
- **c9** Baselines were tuned by random search with five-fold CV, with budgets from 30 s to 4 h.(Results)
- **c10** TabPFN v2 was pre-trained once on eight RTX 2080 GPUs for 2 weeks.(Results)
- **c11** Scores are normalized per dataset, 1.0 = best and 0.0 = worst with respect to all baselines (so values depend on the set of baselines).(Results)
- **c12** TabPFN v2 also substantially outperformed all baselines on the Grinsztajn et al. and McElfresh et al. (TabZilla) benchmarks (refs 14, 15).(Results, Extended Data Fig. 2)
- **c13** Default TabPFN v2 beat default CatBoost on all five recent Kaggle tabular competitions with fewer than 10,000 training samples.(Results, Extended Data Table 6)
- **c14** Dataset characteristics (categorical features, missing values, size) did not strongly change TabPFN v2's relative performance, but this is not evidence that it scales beyond 10,000 samples and 500 features.(Results)
- **c15** TabPFN v2 was very robust to added uninformative features and outliers.(Results, Fig. 5a)
- **c16** With half the training samples, TabPFN v2 still performed as well as the next best method.(Results, Fig. 5a)
- **c17** For regression, hyperparameter tuning of TabPFN v2 matters more than for classification.(Results)
- **c18** Competing interests: two authors are affiliated with PriorLabs (a tabular foundation model company); related patent applications were filed by Bosch.(Competing interests)

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### normalized-roc-auc(大きいほど良い)

繰り返し: Scores normalized per dataset (1 = best, 0 = worst w.r.t. all baselines), then averaged over datasets (Results).

| method | `hollmann2025-amlb-small-classification` |
|---|---|
| TabPFN v2 (default) | 0.939 |
| CatBoost (default) | 0.752 |
| TabPFN v2 (tuned) | 0.952 |
| CatBoost (tuned) | 0.822 |
| TabPFN v2 (PHE) | **0.971** |
| AutoGluon 1.0 | 0.914 |

#### normalized-rmse(大きいほど良い)

繰り返し: Scores normalized per dataset (1 = best, 0 = worst w.r.t. all baselines), then averaged over datasets (Results).

| method | `hollmann2025-amlb-ctr23-small-regression` |
|---|---|
| TabPFN v2 (default) | 0.923 |
| CatBoost (default) | 0.872 |
| TabPFN v2 (tuned) | **0.968** |
| CatBoost (tuned) | 0.875 |

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| AutoGluon 1.0 | CatBoost (default) | 1 | 0 | 0 |
| AutoGluon 1.0 | CatBoost (tuned) | 1 | 0 | 0 |
| AutoGluon 1.0 | TabPFN v2 (PHE) | 0 | 0 | 1 |
| AutoGluon 1.0 | TabPFN v2 (default) | 0 | 0 | 1 |
| AutoGluon 1.0 | TabPFN v2 (tuned) | 0 | 0 | 1 |
| CatBoost (default) | CatBoost (tuned) | 0 | 0 | 2 |
| CatBoost (default) | TabPFN v2 (PHE) | 0 | 0 | 1 |
| CatBoost (default) | TabPFN v2 (default) | 0 | 0 | 2 |
| CatBoost (default) | TabPFN v2 (tuned) | 0 | 0 | 2 |
| CatBoost (tuned) | TabPFN v2 (PHE) | 0 | 0 | 1 |
| CatBoost (tuned) | TabPFN v2 (default) | 0 | 0 | 2 |
| CatBoost (tuned) | TabPFN v2 (tuned) | 0 | 0 | 2 |
| TabPFN v2 (PHE) | TabPFN v2 (default) | 1 | 0 | 0 |
| TabPFN v2 (PHE) | TabPFN v2 (tuned) | 1 | 0 | 0 |
| TabPFN v2 (default) | TabPFN v2 (tuned) | 0 | 0 | 2 |

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| TabPFN v2 (default, ~2.8 s / ~4.8 s) | All baselines tuned for up to 4 h | Normalized ROC AUC / RMSE vs. tuning time (Fig. 4c). | `hollmann2025-amlb-small-classification` | Results |
| TabPFN v2 (default) | AutoGluon 1.0 (up to 4 h) | Classification, normalized ROC AUC (Fig. 5c). | `hollmann2025-amlb-small-classification` | Results |
| TabPFN v2 (PHE) | AutoGluon 1.0 (allowed 4 h) | Regression, normalized RMSE, after TabPFN (PHE)'s minimal 300 s budget (Fig. 5d). | `hollmann2025-amlb-ctr23-small-regression` | Results |

