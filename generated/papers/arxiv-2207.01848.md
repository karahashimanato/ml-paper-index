<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second

- カード: [`arxiv-2207.01848`](../../papers/arxiv-2207.01848.yaml)
- 著者: Noah Hollmann, Samuel Müller, Katharina Eggensperger, Frank Hutter
- 年・掲載: 2023 ICLR 2023
- タグ: automl-systems, gradient-boosted-trees, in-context-learning, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

- **c1** On the 18 small numerical OpenML-CC18 datasets, TabPFN clearly outperformed boosted trees and was on par with AutoML systems, with up to 230x speedup.(Abstract)
- **c2** TabPFN targets small tasks: up to 1,000 training examples, 100 purely numerical features without missing values, and 10 classes.(Section 1)
- **c3** TabPFN is pre-trained once, offline, on synthetic datasets (12-layer Transformer, 20 hours on 8 GPUs); the same model is used for all evaluations.(Section 3)
- **c4** TabPFN predicts by in-context learning: training examples are given as input and no parameters are updated on the new dataset.(Abstract)
- **c5** The synthetic-data prior is based on structural causal models with a preference for simple structures (mixed with a BNN prior).(Abstract)
- **c6** No method, including TabPFN, was best on all individual datasets; TabPFN lost even to default baselines on some.(Section 5.2)
- **c7** TabPFN is weaker when categorical features or missing values are present.(Section 5.2)
- **c8** Evaluation: 5 repetitions per dataset, each with its own seed and a 50/50 train/test split shared by all methods.(Section 5.2)
- **c9** Test datasets: all OpenML-CC18 datasets with up to 2,000 samples (1,000 for training), 100 features and 10 classes (30 datasets; 18 purely numerical without missing values).(Section 5.2)
- **c10** Averaging TabPFN and AutoGluon predictions strongly outperformed all other methods in Table 1; TabPFN's errors are relatively uncorrelated with the baselines'.(Section 5.2)
- **c11** On the small datasets of the OpenML-AutoML Benchmark, using official baseline results, TabPFN outperformed all baselines in mean cross-entropy, accuracy and the OpenML metric.(Section 5.2)
- **c12** Limitation: the Transformer architecture only scales to small datasets.(Section 6)
- **c13** TabPFN generalized to training-set sizes larger than those seen during prior-fitting.(Section 5.2)
- **c14** Baselines were tuned by random search with 5-fold cross-validation until a time budget was exhausted.(Section 5.2)
- **c15** On all 30 test datasets (including categorical/missing), aggregate results were still strong but weaker than on purely numerical data.(Section 5.2)
- **c16** TabPFN needs no hyperparameter tuning.(Abstract)
- **c17** Results are aggregated across datasets as average ROC AUC (OVO for multiclass), ranks and wins with 95% confidence intervals.(Section 5.2)

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### mean-rank-roc-auc-ovo(小さいほど良い)

繰り返し: Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1).

| method | `hollmann2023-cc18-small-numerical` |
|---|---|
| LightGBM | 6.9722 |
| CatBoost | 4.9444 |
| XGBoost | 6.1944 |
| Auto-sklearn 2.0 | 4.4722 |
| AutoGluon | 4 |
| TabPFN (no ensembling) | 3.8056 |
| TabPFN | 2.9444 |
| TabPFN + AutoGluon | **2.6667** |

#### mean-rank-accuracy(小さいほど良い)

繰り返し: Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1).

| method | `hollmann2023-cc18-small-numerical` |
|---|---|
| LightGBM | 6.8889 |
| CatBoost | 4.9722 |
| XGBoost | 6.0556 |
| Auto-sklearn 2.0 | 5.1667 |
| AutoGluon | 3.8889 |
| TabPFN (no ensembling) | 3.8889 |
| TabPFN | 2.8889 |
| TabPFN + AutoGluon | **2.25** |

#### mean-rank-cross-entropy(小さいほど良い)

繰り返し: Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1).

| method | `hollmann2023-cc18-small-numerical` |
|---|---|
| LightGBM | 5.7778 |
| CatBoost | 5.4444 |
| XGBoost | 6 |
| Auto-sklearn 2.0 | 6.4167 |
| AutoGluon | 3.1111 |
| TabPFN (no ensembling) | 4.1389 |
| TabPFN | 3.0278 |
| TabPFN + AutoGluon | **2.0833** |

#### mean-roc-auc-ovo(大きいほど良い)

繰り返し: Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1).

| method | `hollmann2023-cc18-small-numerical` |
|---|---|
| LightGBM | 0.92 ± 0.013 |
| CatBoost | 0.924 ± 0.011 |
| XGBoost | 0.924 ± 0.01 |
| Auto-sklearn 2.0 | 0.929 ± 0.0096 |
| AutoGluon | 0.93 ± 0.0091 |
| TabPFN (no ensembling) | 0.932 ± 0.0088 |
| TabPFN | **0.934 ± 0.0086** |
| TabPFN + AutoGluon | **0.934 ± 0.0084** |

#### mean-accuracy(大きいほど良い)

繰り返し: Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1).

| method | `hollmann2023-cc18-small-numerical` |
|---|---|
| LightGBM | 0.862 ± 0.012 |
| CatBoost | 0.864 ± 0.011 |
| XGBoost | 0.866 ± 0.011 |
| Auto-sklearn 2.0 | 0.87 ± 0.014 |
| AutoGluon | 0.881 ± 0.01 |
| TabPFN (no ensembling) | 0.873 ± 0.0095 |
| TabPFN | 0.879 ± 0.0089 |
| TabPFN + AutoGluon | **0.886 ± 0.0094** |

#### mean-cross-entropy(小さいほど良い)

繰り返し: Aggregated over 18 datasets x 5 splits; ranks and means across datasets (Table 1).

| method | `hollmann2023-cc18-small-numerical` |
|---|---|
| LightGBM | 0.75 ± 0.039 |
| CatBoost | 0.747 ± 0.029 |
| XGBoost | 0.759 ± 0.04 |
| Auto-sklearn 2.0 | 0.813 ± 0.073 |
| AutoGluon | 0.714 ± 0.014 |
| TabPFN (no ensembling) | 0.727 ± 0.021 |
| TabPFN | 0.716 ± 0.019 |
| TabPFN + AutoGluon | **0.711 ± 0.014** |

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| Auto-sklearn 2.0 | AutoGluon | 0 | 0 | 6 |
| Auto-sklearn 2.0 | CatBoost | 3 | 0 | 3 |
| Auto-sklearn 2.0 | LightGBM | 4 | 0 | 2 |
| Auto-sklearn 2.0 | TabPFN | 0 | 0 | 6 |
| Auto-sklearn 2.0 | TabPFN (no ensembling) | 0 | 0 | 6 |
| Auto-sklearn 2.0 | TabPFN + AutoGluon | 0 | 0 | 6 |
| Auto-sklearn 2.0 | XGBoost | 4 | 0 | 2 |
| AutoGluon | CatBoost | 6 | 0 | 0 |
| AutoGluon | LightGBM | 6 | 0 | 0 |
| AutoGluon | TabPFN | 2 | 0 | 4 |
| AutoGluon | TabPFN (no ensembling) | 3 | 1 | 2 |
| AutoGluon | TabPFN + AutoGluon | 0 | 0 | 6 |
| AutoGluon | XGBoost | 6 | 0 | 0 |
| CatBoost | LightGBM | 6 | 0 | 0 |
| CatBoost | TabPFN | 0 | 0 | 6 |
| CatBoost | TabPFN (no ensembling) | 0 | 0 | 6 |
| CatBoost | TabPFN + AutoGluon | 0 | 0 | 6 |
| CatBoost | XGBoost | 4 | 1 | 1 |
| LightGBM | TabPFN | 0 | 0 | 6 |
| LightGBM | TabPFN (no ensembling) | 0 | 0 | 6 |
| LightGBM | TabPFN + AutoGluon | 0 | 0 | 6 |
| LightGBM | XGBoost | 2 | 0 | 4 |
| TabPFN | TabPFN (no ensembling) | 6 | 0 | 0 |
| TabPFN | TabPFN + AutoGluon | 0 | 1 | 5 |
| TabPFN | XGBoost | 6 | 0 | 0 |
| TabPFN (no ensembling) | TabPFN + AutoGluon | 0 | 0 | 6 |
| TabPFN (no ensembling) | XGBoost | 6 | 0 | 0 |
| TabPFN + AutoGluon | XGBoost | 6 | 0 | 0 |

