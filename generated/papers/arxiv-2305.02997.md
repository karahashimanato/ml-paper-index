<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# When Do Neural Nets Outperform Boosted Trees on Tabular Data?

- カード: [`arxiv-2305.02997`](../../papers/arxiv-2305.02997.yaml)
- 著者: Duncan McElfresh, Sujay Khandagale, Jonathan Valverde, Vishak Prasad C, Benjamin Feuer, Chinmay Hegde, Ganesh Ramakrishnan, Micah Goldblum, Colin White
- 年・掲載: 2023 NeurIPS 2023 Datasets and Benchmarks Track
- 原論文: [PDF](https://arxiv.org/pdf/2305.02997v4)(arXiv v4、カード作成時に読んだ版)
- タグ: differentiable-trees, gradient-boosted-trees, in-context-learning, linear-models, random-forests, supervised, tabular-attention, tabular-classification, tabular-foundation-model, tabular-mlp
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The 'NN vs. GBDT' debate is overemphasized: for many datasets the GBDT-NN difference is negligible or light GBDT tuning matters more than the choice.([Abstract, p.1](https://arxiv.org/pdf/2305.02997v4#page=1 "we find that the 'NN vs. GBDT' debate is overemphasized"))
- **c2** Light hyperparameter tuning of a GBDT is often more important than choosing between NNs and GBDTs.([Abstract, p.1](https://arxiv.org/pdf/2305.02997v4#page=1 "light hyperparameter tuning on a GBDT is more important than choosing between NNs and GBDTs"))
- **c3** TabPFN outperformed all other algorithms on average, even when only a random 3000-sample subset of the training data was used.([Abstract, p.1](https://arxiv.org/pdf/2305.02997v4#page=1 "we find that it outperforms all other algorithms on average, even when randomly sampling 3000 training datapoints."))
- **c4** GBDTs handle skewed or heavy-tailed feature distributions and other dataset irregularities much better than NNs.([Abstract, p.1](https://arxiv.org/pdf/2305.02997v4#page=1 "GBDTs are much better than NNs at handling skewed or heavy-tailed feature distributions and other forms of dataset irregularities."))
- **c5** For about one-third of datasets, light tuning (30 random-search iterations) of CatBoost improved performance more than choosing between the best default GBDT and NN.([Section 2.1, p.7](https://arxiv.org/pdf/2305.02997v4#page=7 "Surprisingly, light hyperparameter tuning yields a greater performance improvement than GBDT-vs-NN selection for about one-third of all datasets."))
- **c6** GBDTs performed comparatively better than NNs and baselines on larger datasets.([Section 2.2, p.8](https://arxiv.org/pdf/2305.02997v4#page=8 "Throughout our metafeature analyses, we find that GBDTs perform comparatively better than NNs and baselines with larger datasets."))
- **c7** Authors' recommendation: try simple baselines first, then lightly tune CatBoost.([Section 2.2, p.9](https://arxiv.org/pdf/2305.02997v4#page=9 "first try simple baselines, and then conduct light hyperparameter tuning on CatBoost."))
- **c8** Each dataset uses the ten train/test folds provided by OpenML (comparable with other works using the same folds).([Section 2, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "For each dataset, we use the ten train/test folds provided by OpenML"))
- **c9** Each algorithm was evaluated with at most 30 hyperparameter sets (default + 29 random via Optuna), up to 10 hours per algorithm and split.([Section 2, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "we train and evaluate the algorithm with at most 30 hyperparameter sets (one default set and 29 random sets, using Optuna [3])."))
- **c10** The 98-dataset comparison excludes datasets on which many algorithms hit memory or time limits.([Section 2.1, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "while excluding datasets which ran into memory or timeout issues on a nontrivial number of algorithms"))
- **c11** On the 57 smallest datasets (<=1250 instances), TabPFN had the best average performance and the fastest training time.([Section 2.1, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "Now, we find that TabPFN achieves the best average performance of all algorithms, while also having the fastest training time."))
- **c12** The text states CatBoost's average rank is 5.06 (Table 1 shows a mean rank of 5.50 for CatBoost; the paper is inconsistent).([Section 2.1, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "The fact that the best out of all algorithms, CatBoost, only achieved an average rank of 5.06"))
- **c13** The text says Figure 3 uses accuracy and Table 1 log loss, but the Figure 3 caption says log loss and the Table 1 caption says accuracy (inconsistent).([Section 2.1, p.6](https://arxiv.org/pdf/2305.02997v4#page=6 "Note that the slight differences between Figure 3 and Table 1 is that the former uses accuracy, while the latter uses log loss."))
- **c14** By log-loss rank with Wilcoxon signed-rank tests (Holm-Bonferroni), TabPFN outperformed all other algorithms across the 98 datasets with statistical significance.([Section 2.1, Figure 3, p.6](https://arxiv.org/pdf/2305.02997v4#page=6 "We find that TabPFN outperforms all other algorithms on average across 98 datasets, and this result is statistically significant."))
- **c15** TabPFN was run on larger datasets by randomly subsampling 3000 training samples (TabPFN*).([Section 2, p.3](https://arxiv.org/pdf/2305.02997v4#page=3 "In order to run on datasets of size larger than 3000, we simply take a random sample of size 3000 from the full training dataset."))
- **c16** Dataset sizes range from 32 to 1,025,009 (vs. 3,000-10,000 or 50,000 in Grinsztajn et al.).([Section 1, p.3](https://arxiv.org/pdf/2305.02997v4#page=3 "in contrast to our dataset sizes which range from 32 to 1 025 009"))
- **c17** TabPFN was excluded from the GBDT-vs-NN family analyses because it works differently from other NNs.([Section 2.1 footnote, p.7](https://arxiv.org/pdf/2305.02997v4#page=7 "we exclude it from our analysis in this section and the next section when discussing 'GBDTs vs. NNs.'"))
- **c18** The TabZilla Benchmark Suite consists of the 36 'hardest' of the 176 datasets.([Section 3, p.9](https://arxiv.org/pdf/2305.02997v4#page=9 "a collection of the 36 'hardest' of the 176 datasets we studied in Section 2."))
- **c19** All 176 datasets are classification datasets from OpenML.([Section 2, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "We run the algorithms on 176 classification datasets from OpenML"))
- **c20** Across datasets, accuracy is aggregated with the average distance to the minimum (ADTM): per-dataset 0-1 scaling after selecting the best hyperparameters.([Section 2, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "we use the average distance to the minimum (ADTM) metric, which consists of 0-1 scaling"))
- **c21** The study compares 19 algorithms on 176 datasets.([Abstract, p.1](https://arxiv.org/pdf/2305.02997v4#page=1 "comparing 19 algorithms across 176 datasets"))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### mean-rank(小さいほど良い)

繰り返し: Ten folds per dataset; accuracy 0-1 scaled per dataset (ADTM) and aggregated over datasets (Section 2).

| method | `mcelfresh2023-98-datasets` | `mcelfresh2023-57-small-datasets` |
|---|---|---|
| CatBoost | **5.5** | 5.37 |
| TabPFN* (3000-sample subset) | 5.89 | **4.88** |
| XGBoost | 6.87 | 8.3 |
| ResNet | 7.65 | 6.75 |
| SAINT | 7.9 | 7.67 |
| NODE | 7.9 | 8.35 |
| FTTransformer | 8.14 | 7.93 |
| RandomForest | 8.26 | 7.65 |
| LightGBM | 8.46 | 10 |
| SVM | 9.09 | 9.54 |
| DANet | 9.73 | 10.74 |
| MLP-rtdl | 9.85 | 9.77 |
| STG | 11.76 | 11.49 |
| DecisionTree | 11.81 | 11.44 |
| MLP | 12 | 11.49 |
| LinearModel | 12.18 | 10.21 |
| TabNet | 12.69 | 14.54 |
| KNN | 13.69 | 13.12 |
| VIME | 14.98 | 14.88 |

出典: [Table 1, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "CatBoost GBDT 1 18 5.50 4 0.87 0.93 0.30 0.22 21.70 2.08") / [Table 2, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "TabPFN∗ 1 18 4.88 3 0.84 0.93 0.35 0.26 0.00 0.00")

#### mean-normalized-accuracy(大きいほど良い)

繰り返し: Ten folds per dataset; accuracy 0-1 scaled per dataset (ADTM) and aggregated over datasets (Section 2).

| method | `mcelfresh2023-98-datasets` | `mcelfresh2023-57-small-datasets` |
|---|---|---|
| CatBoost | **0.87** | **0.85** |
| TabPFN* (3000-sample subset) | 0.83 | 0.84 |
| XGBoost | 0.81 | 0.74 |
| ResNet | 0.75 | 0.77 |
| SAINT | 0.73 | 0.74 |
| NODE | 0.74 | 0.73 |
| FTTransformer | 0.76 | 0.75 |
| RandomForest | 0.76 | 0.76 |
| LightGBM | 0.76 | 0.68 |
| SVM | 0.69 | 0.68 |
| DANet | 0.73 | 0.68 |
| MLP-rtdl | 0.65 | 0.64 |
| STG | 0.56 | 0.57 |
| DecisionTree | 0.59 | 0.6 |
| MLP | 0.57 | 0.57 |
| LinearModel | 0.51 | 0.61 |
| TabNet | 0.54 | 0.42 |
| KNN | 0.45 | 0.46 |
| VIME | 0.37 | 0.33 |

出典: [Table 1, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "CatBoost GBDT 1 18 5.50 4 0.87 0.93 0.30 0.22 21.70 2.08") / [Table 2, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "TabPFN∗ 1 18 4.88 3 0.84 0.93 0.35 0.26 0.00 0.00")

#### median-normalized-accuracy(大きいほど良い)

繰り返し: Ten folds per dataset; accuracy 0-1 scaled per dataset (ADTM) and aggregated over datasets (Section 2).

| method | `mcelfresh2023-98-datasets` | `mcelfresh2023-57-small-datasets` |
|---|---|---|
| CatBoost | **0.93** | 0.91 |
| TabPFN* (3000-sample subset) | 0.92 | **0.93** |
| XGBoost | 0.89 | 0.8 |
| ResNet | 0.83 | 0.79 |
| SAINT | 0.86 | 0.87 |
| NODE | 0.81 | 0.75 |
| FTTransformer | 0.8 | 0.78 |
| RandomForest | 0.83 | 0.82 |
| LightGBM | 0.84 | 0.71 |
| SVM | 0.76 | 0.72 |
| DANet | 0.79 | 0.69 |
| MLP-rtdl | 0.72 | 0.69 |
| STG | 0.63 | 0.64 |
| DecisionTree | 0.68 | 0.67 |
| MLP | 0.57 | 0.54 |
| LinearModel | 0.53 | 0.71 |
| TabNet | 0.6 | 0.4 |
| KNN | 0.51 | 0.51 |
| VIME | 0.32 | 0.27 |

出典: [Table 1, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "CatBoost GBDT 1 18 5.50 4 0.87 0.93 0.30 0.22 21.70 2.08") / [Table 2, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "TabPFN∗ 1 18 4.88 3 0.84 0.93 0.35 0.26 0.00 0.00")

#### mean-fold-std-normalized-accuracy(小さいほど良い)

繰り返し: Ten folds per dataset; accuracy 0-1 scaled per dataset (ADTM) and aggregated over datasets (Section 2).

| method | `mcelfresh2023-98-datasets` | `mcelfresh2023-57-small-datasets` |
|---|---|---|
| CatBoost | 0.3 | 0.39 |
| TabPFN* (3000-sample subset) | 0.27 | **0.35** |
| XGBoost | 0.33 | 0.42 |
| ResNet | 0.3 | 0.42 |
| SAINT | 0.31 | 0.42 |
| NODE | **0.26** | 0.36 |
| FTTransformer | 0.31 | 0.42 |
| RandomForest | 0.32 | 0.4 |
| LightGBM | 0.36 | 0.45 |
| SVM | **0.26** | **0.35** |
| DANet | 0.32 | 0.41 |
| MLP-rtdl | 0.28 | 0.39 |
| STG | 0.29 | 0.4 |
| DecisionTree | 0.35 | 0.45 |
| MLP | 0.29 | 0.38 |
| LinearModel | 0.31 | 0.38 |
| TabNet | 0.39 | 0.52 |
| KNN | 0.29 | 0.38 |
| VIME | 0.27 | 0.36 |

出典: [Table 1, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "CatBoost GBDT 1 18 5.50 4 0.87 0.93 0.30 0.22 21.70 2.08") / [Table 2, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "TabPFN∗ 1 18 4.88 3 0.84 0.93 0.35 0.26 0.00 0.00")

#### mean-train-time-per-1000(小さいほど良い)

繰り返し: Ten folds per dataset; accuracy 0-1 scaled per dataset (ADTM) and aggregated over datasets (Section 2).

| method | `mcelfresh2023-98-datasets` | `mcelfresh2023-57-small-datasets` |
|---|---|---|
| CatBoost | 21.7 | 26.22 |
| TabPFN* (3000-sample subset) | 0.25 | **0** |
| XGBoost | 0.81 | 0.95 |
| ResNet | 16.01 | 23.67 |
| SAINT | 169.54 | 197.41 |
| NODE | 138.36 | 173.55 |
| FTTransformer | 27.67 | 32.93 |
| RandomForest | 0.35 | 0.47 |
| LightGBM | 0.87 | 0.64 |
| SVM | 30.4 | 23.9 |
| DANet | 68.82 | 83.57 |
| MLP-rtdl | 14.27 | 21.48 |
| STG | 18.44 | 21.22 |
| DecisionTree | 0.03 | 0.02 |
| MLP | 18.39 | 27.88 |
| LinearModel | 0.04 | 0.06 |
| TabNet | 34.95 | 41.83 |
| KNN | **0.01** | **0** |
| VIME | 16.81 | 18.95 |

出典: [Table 1, p.4](https://arxiv.org/pdf/2305.02997v4#page=4 "CatBoost GBDT 1 18 5.50 4 0.87 0.93 0.30 0.22 21.70 2.08") / [Table 2, p.5](https://arxiv.org/pdf/2305.02997v4#page=5 "TabPFN∗ 1 18 4.88 3 0.84 0.93 0.35 0.26 0.00 0.00")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| CatBoost | DANet | 10 | 0 | 0 |
| CatBoost | DecisionTree | 8 | 0 | 2 |
| CatBoost | FTTransformer | 10 | 0 | 0 |
| CatBoost | KNN | 6 | 0 | 4 |
| CatBoost | LightGBM | 8 | 0 | 2 |
| CatBoost | LinearModel | 7 | 0 | 3 |
| CatBoost | MLP | 7 | 0 | 3 |
| CatBoost | MLP-rtdl | 6 | 1 | 3 |
| CatBoost | NODE | 8 | 0 | 2 |
| CatBoost | RandomForest | 8 | 0 | 2 |
| CatBoost | ResNet | 7 | 1 | 2 |
| CatBoost | SAINT | 10 | 0 | 0 |
| CatBoost | STG | 7 | 0 | 3 |
| CatBoost | SVM | 7 | 0 | 3 |
| CatBoost | TabNet | 10 | 0 | 0 |
| CatBoost | TabPFN* (3000-sample subset) | 4 | 0 | 6 |
| CatBoost | VIME | 6 | 0 | 4 |
| CatBoost | XGBoost | 8 | 0 | 2 |
| DANet | DecisionTree | 8 | 0 | 2 |
| DANet | FTTransformer | 1 | 0 | 9 |
| DANet | KNN | 6 | 0 | 4 |
| DANet | LightGBM | 2 | 1 | 7 |
| DANet | LinearModel | 4 | 0 | 6 |
| DANet | MLP | 6 | 0 | 4 |
| DANet | MLP-rtdl | 4 | 1 | 5 |
| DANet | NODE | 2 | 0 | 8 |
| DANet | RandomForest | 0 | 1 | 9 |
| DANet | ResNet | 1 | 0 | 9 |
| DANet | SAINT | 3 | 1 | 6 |
| DANet | STG | 6 | 0 | 4 |
| DANet | SVM | 2 | 1 | 7 |
| DANet | TabNet | 8 | 0 | 2 |
| DANet | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| DANet | VIME | 6 | 0 | 4 |
| DANet | XGBoost | 2 | 0 | 8 |
| DecisionTree | FTTransformer | 2 | 0 | 8 |
| DecisionTree | KNN | 6 | 0 | 4 |
| DecisionTree | LightGBM | 3 | 1 | 6 |
| DecisionTree | LinearModel | 5 | 0 | 5 |
| DecisionTree | MLP | 8 | 0 | 2 |
| DecisionTree | MLP-rtdl | 2 | 0 | 8 |
| DecisionTree | NODE | 2 | 0 | 8 |
| DecisionTree | RandomForest | 2 | 0 | 8 |
| DecisionTree | ResNet | 2 | 0 | 8 |
| DecisionTree | SAINT | 2 | 0 | 8 |
| DecisionTree | STG | 7 | 0 | 3 |
| DecisionTree | SVM | 2 | 0 | 8 |
| DecisionTree | TabNet | 10 | 0 | 0 |
| DecisionTree | TabPFN* (3000-sample subset) | 1 | 0 | 9 |
| DecisionTree | VIME | 8 | 0 | 2 |
| DecisionTree | XGBoost | 2 | 0 | 8 |
| FTTransformer | KNN | 6 | 0 | 4 |
| FTTransformer | LightGBM | 6 | 1 | 3 |
| FTTransformer | LinearModel | 6 | 1 | 3 |
| FTTransformer | MLP | 6 | 0 | 4 |
| FTTransformer | MLP-rtdl | 6 | 0 | 4 |
| FTTransformer | NODE | 6 | 0 | 4 |
| FTTransformer | RandomForest | 2 | 1 | 7 |
| FTTransformer | ResNet | 1 | 1 | 8 |
| FTTransformer | SAINT | 4 | 2 | 4 |
| FTTransformer | STG | 6 | 0 | 4 |
| FTTransformer | SVM | 7 | 0 | 3 |
| FTTransformer | TabNet | 10 | 0 | 0 |
| FTTransformer | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| FTTransformer | VIME | 6 | 0 | 4 |
| FTTransformer | XGBoost | 3 | 1 | 6 |
| KNN | LightGBM | 4 | 0 | 6 |
| KNN | LinearModel | 3 | 1 | 6 |
| KNN | MLP | 2 | 2 | 6 |
| KNN | MLP-rtdl | 3 | 0 | 7 |
| KNN | NODE | 2 | 0 | 8 |
| KNN | RandomForest | 4 | 0 | 6 |
| KNN | ResNet | 4 | 0 | 6 |
| KNN | SAINT | 4 | 0 | 6 |
| KNN | STG | 3 | 1 | 6 |
| KNN | SVM | 2 | 0 | 8 |
| KNN | TabNet | 7 | 0 | 3 |
| KNN | TabPFN* (3000-sample subset) | 1 | 1 | 8 |
| KNN | VIME | 8 | 0 | 2 |
| KNN | XGBoost | 4 | 0 | 6 |
| LightGBM | LinearModel | 5 | 1 | 4 |
| LightGBM | MLP | 8 | 0 | 2 |
| LightGBM | MLP-rtdl | 7 | 0 | 3 |
| LightGBM | NODE | 4 | 0 | 6 |
| LightGBM | RandomForest | 1 | 1 | 8 |
| LightGBM | ResNet | 4 | 0 | 6 |
| LightGBM | SAINT | 3 | 0 | 7 |
| LightGBM | STG | 8 | 0 | 2 |
| LightGBM | SVM | 5 | 1 | 4 |
| LightGBM | TabNet | 10 | 0 | 0 |
| LightGBM | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| LightGBM | VIME | 8 | 0 | 2 |
| LightGBM | XGBoost | 1 | 0 | 9 |
| LinearModel | MLP | 5 | 1 | 4 |
| LinearModel | MLP-rtdl | 4 | 0 | 6 |
| LinearModel | NODE | 2 | 0 | 8 |
| LinearModel | RandomForest | 4 | 0 | 6 |
| LinearModel | ResNet | 3 | 0 | 7 |
| LinearModel | SAINT | 3 | 1 | 6 |
| LinearModel | STG | 6 | 0 | 4 |
| LinearModel | SVM | 2 | 0 | 8 |
| LinearModel | TabNet | 8 | 0 | 2 |
| LinearModel | TabPFN* (3000-sample subset) | 1 | 0 | 9 |
| LinearModel | VIME | 8 | 0 | 2 |
| LinearModel | XGBoost | 4 | 0 | 6 |
| MLP | MLP-rtdl | 1 | 0 | 9 |
| MLP | NODE | 2 | 0 | 8 |
| MLP | RandomForest | 2 | 0 | 8 |
| MLP | ResNet | 2 | 0 | 8 |
| MLP | SAINT | 4 | 0 | 6 |
| MLP | STG | 3 | 3 | 4 |
| MLP | SVM | 1 | 0 | 9 |
| MLP | TabNet | 9 | 0 | 1 |
| MLP | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| MLP | VIME | 6 | 0 | 4 |
| MLP | XGBoost | 2 | 0 | 8 |
| MLP-rtdl | NODE | 2 | 0 | 8 |
| MLP-rtdl | RandomForest | 2 | 0 | 8 |
| MLP-rtdl | ResNet | 4 | 0 | 6 |
| MLP-rtdl | SAINT | 4 | 0 | 6 |
| MLP-rtdl | STG | 9 | 0 | 1 |
| MLP-rtdl | SVM | 2 | 0 | 8 |
| MLP-rtdl | TabNet | 10 | 0 | 0 |
| MLP-rtdl | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| MLP-rtdl | VIME | 7 | 0 | 3 |
| MLP-rtdl | XGBoost | 2 | 0 | 8 |
| NODE | RandomForest | 3 | 0 | 7 |
| NODE | ResNet | 2 | 0 | 8 |
| NODE | SAINT | 5 | 1 | 4 |
| NODE | STG | 8 | 0 | 2 |
| NODE | SVM | 6 | 1 | 3 |
| NODE | TabNet | 8 | 0 | 2 |
| NODE | TabPFN* (3000-sample subset) | 1 | 0 | 9 |
| NODE | VIME | 7 | 1 | 2 |
| NODE | XGBoost | 2 | 0 | 8 |
| RandomForest | ResNet | 5 | 1 | 4 |
| RandomForest | SAINT | 6 | 0 | 4 |
| RandomForest | STG | 8 | 1 | 1 |
| RandomForest | SVM | 8 | 0 | 2 |
| RandomForest | TabNet | 10 | 0 | 0 |
| RandomForest | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| RandomForest | VIME | 8 | 0 | 2 |
| RandomForest | XGBoost | 7 | 0 | 3 |
| ResNet | SAINT | 7 | 1 | 2 |
| ResNet | STG | 7 | 0 | 3 |
| ResNet | SVM | 8 | 0 | 2 |
| ResNet | TabNet | 10 | 0 | 0 |
| ResNet | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| ResNet | VIME | 7 | 0 | 3 |
| ResNet | XGBoost | 3 | 1 | 6 |
| SAINT | STG | 6 | 0 | 4 |
| SAINT | SVM | 6 | 0 | 4 |
| SAINT | TabNet | 8 | 0 | 2 |
| SAINT | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| SAINT | VIME | 6 | 0 | 4 |
| SAINT | XGBoost | 3 | 2 | 5 |
| STG | SVM | 2 | 0 | 8 |
| STG | TabNet | 10 | 0 | 0 |
| STG | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| STG | VIME | 6 | 0 | 4 |
| STG | XGBoost | 2 | 0 | 8 |
| SVM | TabNet | 10 | 0 | 0 |
| SVM | TabPFN* (3000-sample subset) | 1 | 1 | 8 |
| SVM | VIME | 8 | 0 | 2 |
| SVM | XGBoost | 2 | 0 | 8 |
| TabNet | TabPFN* (3000-sample subset) | 0 | 0 | 10 |
| TabNet | VIME | 6 | 0 | 4 |
| TabNet | XGBoost | 0 | 0 | 10 |
| TabPFN* (3000-sample subset) | VIME | 9 | 1 | 0 |
| TabPFN* (3000-sample subset) | XGBoost | 10 | 0 | 0 |
| VIME | XGBoost | 2 | 0 | 8 |

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| TabPFN* (3000-sample subset) | All other 18 algorithms | Mean log-loss rank over the 98 datasets; Friedman test then Wilcoxon signed-rank tests with Holm-Bonferroni correction (Figure 3). | `mcelfresh2023-98-datasets` | [Section 2.1, Figure 3, p.6](https://arxiv.org/pdf/2305.02997v4#page=6 "We find that TabPFN outperforms all other algorithms on average across 98 datasets, and this result is statistically significant.") |

