<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Accurate predictions on small data with a tabular foundation model

- カード: [`doi-10.1038_s41586-024-08328-6`](../../papers/doi-10.1038_s41586-024-08328-6.yaml)
- 著者: Noah Hollmann, Samuel Müller, Lennart Purucker, Arjun Krishnakumar, Max Körfer, Shi Bin Hoo, Robin Tibor Schirrmeister, Frank Hutter
- 年・掲載: 2025 Nature 637, 319-326 (2025)
- 原論文: [PDF](https://www.nature.com/articles/s41586-024-08328-6.pdf)(Nature published version (open access)、カード作成時に読んだ版)
- タグ: automl-systems, gradient-boosted-trees, in-context-learning, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabPFN v2 outperformed all previous methods on datasets with up to 10,000 samples by a wide margin, with much less training time.([Abstract, p.1](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=1 "a tabular foundation model that outperforms all previous methods on datasets with up to 10,000 samples by a wide margin, using substantially less training time."))
- **c2** In 2.8 s, TabPFN v2 outperformed an ensemble of the strongest baselines tuned for 4 h (classification).([Abstract, p.1](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=1 "In 2.8 s, TabPFN outperforms an ensemble of the strongest baselines tuned for 4 h in a classification setting."))
- **c3** Compared with the 2023 TabPFN, v2 scales to 50x larger datasets, supports regression, categorical data and missing values, and is robust to unimportant features and outliers.([Introduction, p.2](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=2 "the new TabPFN scales to 50× larger datasets; supports regression tasks, categorical data and missing values; and is robust to unimportant features and outliers."))
- **c4** Training only on synthetic data avoids privacy/copyright issues and contamination of training data with test data.([Architecture / prior, p.3](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=3 "By relying on synthetic data instead of large collections of public tabular data, we avoid common problems of foundational models, such as privacy and copyright infringements, contaminating our training data with test data"))
- **c5** About 100 million synthetic datasets (from structural causal models) are generated per model training.([Synthetic data, p.4](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=4 "we created a massive corpus of around 100 million synthetic datasets per model training"))
- **c6** The architecture uses two-way attention: each cell attends within its row, then within its column, making it invariant to sample and feature order.([Architecture, p.3](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=3 "uses a two-way attention mechanism, with each cell attending to the other features in its row (that is, its sample) and then attending to the same feature across its column (that is, all other samples)."))
- **c7** Primary evaluation: 29 classification and 28 regression datasets from the AutoML Benchmark and OpenML-CTR23 with up to 10,000 samples, 500 features and 10 classes.([Results, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "we use the 29 classification datasets and 28 regression datasets that have up to 10,000 samples, 500 features and 10 classes."))
- **c8** Each dataset and method: 10 repetitions with different seeds and 90/10 train/test splits.([Results, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "For each dataset and method, we ran 10 repetitions with different random seeds and train–test splits (90% train, 10% test)."))
- **c9** Baselines were tuned by random search with five-fold CV, with budgets from 30 s to 4 h.([Results, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "We tuned hyperparameters using random search with five-fold cross-validation, with time budgets ranging from 30 s to 4 h."))
- **c10** TabPFN v2 was pre-trained once on eight RTX 2080 GPUs for 2 weeks.([Results, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "TabPFN was pre-trained once using eight NVIDIA RTX 2080 GPUs over 2 weeks"))
- **c11** Scores are normalized per dataset, 1.0 = best and 0.0 = worst with respect to all baselines (so values depend on the set of baselines).([Results, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "Scores were normalized per dataset, with 1.0 representing the best and 0.0 the worst performance with respect to all baselines."))
- **c12** TabPFN v2 also substantially outperformed all baselines on the Grinsztajn et al. and McElfresh et al. (TabZilla) benchmarks (refs 14, 15).([Results, Extended Data Fig. 2, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "TabPFN substantially outperformed all baselines on the benchmarks of refs. 14,15."))
- **c13** Default TabPFN v2 beat default CatBoost on all five recent Kaggle tabular competitions with fewer than 10,000 training samples.([Results, Extended Data Table 6, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "default TabPFN outperforms default CatBoost on all five Kaggle competitions with less than 10,000 training samples"))
- **c14** Dataset characteristics (categorical features, missing values, size) did not strongly change TabPFN v2's relative performance, but this is not evidence that it scales beyond 10,000 samples and 500 features.([Results, p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "these results should not be taken as evidence that TabPFN scales well beyond the 10,000 samples and 500 features considered here."))
- **c15** TabPFN v2 was very robust to added uninformative features and outliers.([Results, Fig. 5a, p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "The results show that TabPFN is very robust to uninformative features and outliers"))
- **c16** With half the training samples, TabPFN v2 still performed as well as the next best method.([Results, Fig. 5a, p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "with half the samples TabPFN still performs as well as the next best method"))
- **c17** For regression, hyperparameter tuning of TabPFN v2 matters more than for classification.([Results, p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "For regression tasks, tuning hyperparameters is more important."))
- **c18** Competing interests: two authors are affiliated with PriorLabs (a tabular foundation model company); related patent applications were filed by Bosch.([Competing interests, p.13](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=13 "F.H. and N.H. are affiliated with PriorLabs, a company focused on developing tabular foundation models."))

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

出典: [Results (main text), p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "TabPFN surpasses CatBoost, the strongest default baseline, by 0.187 (0.939 compared with 0.752) in normalized ROC AUC in the default setting") / [Results (main text), p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "TabPFN (PHE) further improves performance leading to an average normalized ROC AUC score of 0.971, compared with 0.939 for TabPFN (default) and 0.914 for AutoGluon.")

#### normalized-rmse(大きいほど良い)

繰り返し: Scores normalized per dataset (1 = best, 0 = worst w.r.t. all baselines), then averaged over datasets (Results).

| method | `hollmann2025-amlb-ctr23-small-regression` |
|---|---|
| TabPFN v2 (default) | 0.923 |
| CatBoost (default) | 0.872 |
| TabPFN v2 (tuned) | **0.968** |
| CatBoost (tuned) | 0.875 |

出典: [Results (main text), p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "TabPFN outperforms CatBoost in normalized RMSE by 0.051 (0.923 compared with 0.872) in the default setting")

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
| TabPFN v2 (default, ~2.8 s / ~4.8 s) | All baselines tuned for up to 4 h | Normalized ROC AUC / RMSE vs. tuning time (Fig. 4c). | `hollmann2025-amlb-small-classification` | [Results, p.5](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=5 "The default of TabPFN, taking 2.8 s on average for classification and 4.8 s for regression, outperforms all baselines, even when tuning them for 4 h") |
| TabPFN v2 (default) | AutoGluon 1.0 (up to 4 h) | Classification, normalized ROC AUC (Fig. 5c). | `hollmann2025-amlb-small-classification` | [Results, p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "In just 2.8 s, TabPFN (default) outperforms AutoGluon for classification tasks, even if AutoGluon is allowed up to 4 h") |
| TabPFN v2 (PHE) | AutoGluon 1.0 (allowed 4 h) | Regression, normalized RMSE, after TabPFN (PHE)'s minimal 300 s budget (Fig. 5d). | `hollmann2025-amlb-ctr23-small-regression` | [Results, p.6](https://www.nature.com/articles/s41586-024-08328-6.pdf#page=6 "TabPFN (PHE) outperforms AutoGluon (allowed 4 h) after its minimal") |

