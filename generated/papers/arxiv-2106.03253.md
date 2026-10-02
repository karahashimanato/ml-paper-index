<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tabular Data: Deep Learning is Not All You Need

- カード: [`arxiv-2106.03253`](../../papers/arxiv-2106.03253.yaml)
- 著者: Ravid Shwartz-Ziv, Amitai Armon
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2106.03253v2)(arXiv v2、カード作成時に読んだ版)
- タグ: differentiable-trees, gradient-boosted-trees, heterogeneous-ensembles, supervised, tabular-attention, tabular-classification, tabular-cnn, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** XGBoost outperformed the four deep tabular models (TabNet, NODE, DNF-Net, 1D-CNN) across the 11 datasets, including datasets from the deep models' own papers.([Abstract, p.1](https://arxiv.org/pdf/2106.03253v2#page=1 "Our study shows that XGBoost outperforms these deep models across the datasets, including the datasets used in the papers that proposed the deep models."))
- **c2** XGBoost needed much less hyperparameter tuning than the deep models.([Abstract, p.1](https://arxiv.org/pdf/2106.03253v2#page=1 "We also demonstrate that XGBoost requires much less tuning."))
- **c3** An ensemble of the deep models and XGBoost performed better than XGBoost alone on these datasets.([Abstract, p.1](https://arxiv.org/pdf/2106.03253v2#page=1 "we show that an ensemble of deep models and XGBoost performs better on these datasets than XGBoost alone."))
- **c4** Each deep model did best only on the datasets from its own paper; no deep model was consistently better than the others.([Section 3.2, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "Each deep model was better only on the datasets that appeared in its own paper."))
- **c5** Authors name selection bias in the original papers (datasets chosen where the model works well) as one possible explanation.([Section 3.2, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "The first possibility is selection bias."))
- **c6** Authors name unequal hyperparameter optimization in the original papers as a second possible explanation.([Section 3.2, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "The second possibility is differences in the optimization of hyperparameters."))
- **c7** All models were tuned with HyperOpt (Bayesian optimization) for 1,000 steps per dataset on a validation set.([Section 3.1.2, p.4](https://arxiv.org/pdf/2106.03253v2#page=4 "The hyperparameter search was run for 1, 000 steps on each dataset by optimizing the results on a validation set."))
- **c8** XGBoost trained/tuned more than an order of magnitude faster than the deep models in their runs; authors caution this depends on software optimization.([Section 3.2, p.7](https://arxiv.org/pdf/2106.03253v2#page=7 "Generally, we found XGBoost to be significantly faster than the deep networks in our experiments (more than an order of magnitude)."))
- **c9** An ensemble of classical models (XGBoost, SVM, CatBoost) was reported to perform much worse than the deep-models-plus-XGBoost ensemble.([Section 3.2, p.7](https://arxiv.org/pdf/2106.03253v2#page=7 "Table 2 shows that the ensemble of classical models performed much worse than the ensemble of deep networks and XGBoost."))
- **c10** On Shrutime, choosing ensemble members by validation loss needed only three models for near-optimal performance.([Section 3.2, Figure 1, p.7](https://arxiv.org/pdf/2106.03253v2#page=7 "Only three models were needed to achieve almost optimal performance this way."))
- **c11** The text says the regression metric is RMSE.([Section 3.1.2, p.5](https://arxiv.org/pdf/2106.03253v2#page=5 "For regression problems, we report the root mean square error."))
- **c12** The Table 2 caption says MSE is shown for YearPrediction and Rossman (inconsistent with the RMSE statement in Section 3.1.2).([Table 2 caption, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "MSE is presented for the YearPrediction and Rossman datasets"))
- **c13** The 11 datasets are nine taken from the TabNet, DNF-Net and NODE papers (three each) plus two Kaggle datasets not used by any of them.([Section 3.1.1, p.4](https://arxiv.org/pdf/2106.03253v2#page=4 "We use nine datasets from the TabNet, DNF-Net, and NODE papers, drawing three datasets from each paper."))
- **c14** Table 2 values are averages of four training runs with the standard error of the mean.([Table 2 caption, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "The values are the averages of four training runs (lower value is better), along with the standard error of the mean (SEM)"))
- **c15** Each dataset was preprocessed and trained as described in its original paper.([Section 3.1.1, p.4](https://arxiv.org/pdf/2106.03253v2#page=4 "Each dataset was preprocessed and trained as described in the original paper."))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### table2-mse(小さいほど良い)

繰り返し: Three random partitions if the original split was random, otherwise four seeds on the same partition; Table 2 reports mean and SEM of four runs.

| method | `shwartzziv2021-rossmann` | `shwartzziv2021-yearprediction` |
|---|---|---|
| XGBoost | 490.18 ± 1.19 | 77.98 ± 0.11 |
| NODE | 488.59 ± 1.24 | 76.39 ± 0.13 |
| DNF-Net | 503.83 ± 1.41 | 81.21 ± 0.18 |
| TabNet | **485.12 ± 1.93** | 83.19 ± 0.19 |
| 1D-CNN | 493.81 ± 2.23 | 78.94 ± 0.14 |
| Simple Ensemble | 488.57 ± 2.14 | 78.01 ± 0.17 |
| Deep Ensemble w/o XGBoost | 489.94 ± 2.09 | 78.99 ± 0.11 |
| Deep Ensemble w XGBoost | 485.33 ± 1.29 | **76.19 ± 0.21** |

出典: [Table 2, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "XGBoost 490.18 ± 1.19 3.13 ± 0.09 21.62 ± 0.33 2.18 ± 0.20 56.07±0.65 80.64 ± 0.80")

#### cross-entropy-x100(小さいほど良い)

繰り返し: Three random partitions if the original split was random, otherwise four seeds on the same partition; Table 2 reports mean and SEM of four runs.

| method | `shwartzziv2021-covertype` | `shwartzziv2021-higgs` | `shwartzziv2021-gas-concentrations` | `shwartzziv2021-eye-movements` | `shwartzziv2021-gesture-phase` | `shwartzziv2021-mslr-web10k` | `shwartzziv2021-epsilon` | `shwartzziv2021-shrutime` | `shwartzziv2021-blastchar` |
|---|---|---|---|---|---|---|---|---|---|
| XGBoost | 3.13 ± 0.09 | 21.62 ± 0.33 | 2.18 ± 0.2 | **56.07 ± 0.65** | 80.64 ± 0.8 | 55.43 ± 0.02 | 11.12 ± 0.03 | 13.82 ± 0.19 | 20.39 ± 0.21 |
| NODE | 4.15 ± 0.13 | 21.19 ± 0.69 | 2.17 ± 0.18 | 68.35 ± 0.66 | 92.12 ± 0.82 | 55.72 ± 0.03 | **10.39 ± 0.01** | 14.61 ± 0.1 | 21.4 ± 0.25 |
| DNF-Net | 3.96 ± 0.11 | 23.68 ± 0.83 | **1.44 ± 0.09** | 68.38 ± 0.65 | 86.98 ± 0.74 | 56.83 ± 0.03 | 12.23 ± 0.04 | 16.8 ± 0.09 | 27.91 ± 0.17 |
| TabNet | 3.01 ± 0.08 | **21.14 ± 0.2** | 1.92 ± 0.14 | 67.13 ± 0.69 | 96.42 ± 0.87 | 56.04 ± 0.01 | 11.92 ± 0.03 | 14.94 ± 0.13 | 23.72 ± 0.19 |
| 1D-CNN | 3.51 ± 0.13 | 22.33 ± 0.73 | 1.79 ± 0.19 | 67.9 ± 0.64 | 97.89 ± 0.82 | 55.97 ± 0.04 | 11.08 ± 0.06 | 15.31 ± 0.16 | 24.68 ± 0.22 |
| Simple Ensemble | 3.19 ± 0.18 | 22.46 ± 0.38 | 2.36 ± 0.13 | 58.72 ± 0.67 | 89.45 ± 0.89 | 55.46 ± 0.04 | 11.07 ± 0.04 | 13.61 ± 0.14 | 21.18 ± 0.17 |
| Deep Ensemble w/o XGBoost | 3.52 ± 0.1 | 22.41 ± 0.54 | 1.98 ± 0.13 | 69.28 ± 0.62 | 93.5 ± 0.75 | 55.59 ± 0.03 | 10.95 ± 0.01 | 14.69 ± 0.11 | 24.25 ± 0.22 |
| Deep Ensemble w XGBoost | **2.99 ± 0.08** | 22.34 ± 0.81 | 1.69 ± 0.1 | 59.43 ± 0.6 | **78.93 ± 0.73** | **55.38 ± 0.01** | 11.18 ± 0.01 | **13.1 ± 0.15** | **20.18 ± 0.16** |

出典: [Table 2, p.6](https://arxiv.org/pdf/2106.03253v2#page=6 "XGBoost 490.18 ± 1.19 3.13 ± 0.09 21.62 ± 0.33 2.18 ± 0.20 56.07±0.65 80.64 ± 0.80")

#### avg-relative-deterioration-pct(小さいほど良い)

繰り返し: Three random partitions if the original split was random, otherwise four seeds on the same partition; Table 2 reports mean and SEM of four runs.

| method | `shwartzziv2021-unseen-average` |
|---|---|
| XGBoost | 3.34 |
| NODE | 14.21 |
| DNF-Net | 11.96 |
| TabNet | 10.51 |
| 1D-CNN | 7.56 |
| Simple Ensemble | 3.15 |
| Deep Ensemble w/o XGBoost | 6.91 |
| Deep Ensemble w XGBoost | **2.32** |

出典: [Table 3, p.7](https://arxiv.org/pdf/2106.03253v2#page=7 "XGBoost 3.34")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| 1D-CNN | DNF-Net | 10 | 0 | 2 |
| 1D-CNN | Deep Ensemble w XGBoost | 2 | 0 | 10 |
| 1D-CNN | Deep Ensemble w/o XGBoost | 5 | 0 | 7 |
| 1D-CNN | NODE | 4 | 0 | 8 |
| 1D-CNN | Simple Ensemble | 2 | 0 | 10 |
| 1D-CNN | TabNet | 5 | 0 | 7 |
| 1D-CNN | XGBoost | 2 | 0 | 10 |
| DNF-Net | Deep Ensemble w XGBoost | 1 | 0 | 11 |
| DNF-Net | Deep Ensemble w/o XGBoost | 3 | 0 | 9 |
| DNF-Net | NODE | 4 | 0 | 8 |
| DNF-Net | Simple Ensemble | 2 | 0 | 10 |
| DNF-Net | TabNet | 3 | 0 | 9 |
| DNF-Net | XGBoost | 1 | 0 | 11 |
| Deep Ensemble w XGBoost | Deep Ensemble w/o XGBoost | 11 | 0 | 1 |
| Deep Ensemble w XGBoost | NODE | 10 | 0 | 2 |
| Deep Ensemble w XGBoost | Simple Ensemble | 10 | 0 | 2 |
| Deep Ensemble w XGBoost | TabNet | 10 | 0 | 2 |
| Deep Ensemble w XGBoost | XGBoost | 9 | 0 | 3 |
| Deep Ensemble w/o XGBoost | NODE | 4 | 0 | 8 |
| Deep Ensemble w/o XGBoost | Simple Ensemble | 3 | 0 | 9 |
| Deep Ensemble w/o XGBoost | TabNet | 6 | 0 | 6 |
| Deep Ensemble w/o XGBoost | XGBoost | 3 | 0 | 9 |
| NODE | Simple Ensemble | 4 | 0 | 8 |
| NODE | TabNet | 6 | 0 | 6 |
| NODE | XGBoost | 5 | 0 | 7 |
| Simple Ensemble | TabNet | 8 | 0 | 4 |
| Simple Ensemble | XGBoost | 4 | 0 | 8 |
| TabNet | XGBoost | 4 | 0 | 8 |

