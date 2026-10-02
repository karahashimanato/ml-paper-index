<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Revisiting Deep Learning Models for Tabular Data

- カード: [`arxiv-2106.11959`](../../papers/arxiv-2106.11959.yaml)
- 著者: Yury Gorishniy, Ivan Rubachev, Valentin Khrulkov, Artem Babenko
- 年・掲載: 2021 NeurIPS 2021
- 原論文: [PDF](https://arxiv.org/pdf/2106.11959v5)(arXiv v5、カード作成時に読んだ版)
- タグ: differentiable-trees, gradient-boosted-trees, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** None of the considered DL models consistently outperformed the simple ResNet-like baseline.([Section 1, p.2](https://arxiv.org/pdf/2106.11959v5#page=2 "First, we reveal that none of the considered DL models can consistently outperform the ResNet-like model."))
- **c2** FT-Transformer (proposed) performed best among DL models on most tasks.([Section 1, p.2](https://arxiv.org/pdf/2106.11959v5#page=2 "Second, FT-Transformer demonstrates the best performance on most tasks and becomes a new powerful solution for the field."))
- **c3** There is no universally superior solution among GBDT and deep models.([Section 1, p.2](https://arxiv.org/pdf/2106.11959v5#page=2 "We reveal that there is still no universally superior solution among GBDT and deep models."))
- **c4** With tuned hyperparameters, GBDT ensembles dominated on California Housing, Adult and Yahoo.([Section 4.5, p.8](https://arxiv.org/pdf/2106.11959v5#page=8 "Once hyperparameters are properly tuned, GBDTs start dominating on some datasets (California Housing, Adult, Yahoo; see Table 4)."))
- **c5** Authors state that DL winning on most of their datasets reflects a benchmark slightly biased towards DL-friendly problems, not DL being better.([Section 4.5, p.8](https://arxiv.org/pdf/2106.11959v5#page=8 "it only means that the constructed benchmark is slightly biased towards 'DL-friendly' problems."))
- **c6** GBDT struggled on multiclass problems with many classes: poor on Helena (100 classes), untunable on ALOI (1000 classes) due to slow training.([Section 4.5, p.8](https://arxiv.org/pdf/2106.11959v5#page=8 "GBDT can demonstrate unsatisfactory performance (Helena) or even be untunable due to extremely slow training (ALOI)."))
- **c7** Ensembles of default FT-Transformers performed roughly on par with ensembles of tuned FT-Transformers.([Section 4.5, p.8](https://arxiv.org/pdf/2106.11959v5#page=8 "Interestingly, the ensemble of default FT-Transformers performs quite on par with the ensembles of tuned FT-Transformers."))
- **c8** Tuning made simple models (MLP, ResNet) competitive; authors recommend tuning baselines.([Section 4.4, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "Tuning makes simple models such as MLP and ResNet competitive, so we recommend tuning baselines when possible."))
- **c9** FT-Transformer needs more hardware and time than ResNet and may not scale to very many features (attention is quadratic in the number of features).([Section 3.3 Limitations, p.5](https://arxiv.org/pdf/2106.11959v5#page=5 "FT-Transformer requires more resources (both hardware and time) for training than simple models such as ResNet"))
- **c10** NODE was inferior to ResNet on six of the eleven datasets despite being more complex.([Section 4.4, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "However, it is still inferior to ResNet on six datasets (Helena, Jannis, Higgs, ALOI, Epsilon, Covertype), while being a more complex solution."))
- **c11** On synthetic targets interpolating between GBDT-friendly and DL-friendly functions, ResNet degraded as targets became GBDT-friendly while FT-Transformer stayed competitive.([Section 5.1, Figure 3, p.9](https://arxiv.org/pdf/2106.11959v5#page=9 "By contrast, FT-Transformer yields competitive performance across the whole range of tasks."))
- **c12** FT-Transformer was not tuned on Yahoo (default configuration reported) and only heuristic default configurations were tried on Epsilon.([Appendix E.2, p.18](https://arxiv.org/pdf/2106.11959v5#page=18 "For Yahoo, we did not perform tuning at all, since the default configuration already performed well."))
- **c13** Each tuned configuration was evaluated over 15 random seeds; ensembles are three disjoint groups of 5 models.([Section 4.3, p.6](https://arxiv.org/pdf/2106.11959v5#page=6 "For each tuned configuration, we run 15 experiments with different random seeds and report the performance on the test set."))
- **c14** XGBoost used one-hot encoding for categorical features; CatBoost used its built-in categorical support.([Section 4.3, p.6](https://arxiv.org/pdf/2106.11959v5#page=6 "For XGBoost, we use one-hot encoding."))
- **c15** Averaging [CLS] attention maps gave feature-importance rankings comparable to Integrated Gradients at much lower cost.([Section 5.3, p.10](https://arxiv.org/pdf/2106.11959v5#page=10 "we conclude that the simple averaging of attention maps can be a good choice in terms of cost-effectiveness."))
- **c16** Dataset sizes (#objects) range from 20,640 (California Housing) to 1,200,192 (Microsoft); the 11 datasets include multiclass problems with 100 (Helena) and 1000 (ALOI) classes.([Table 1, p.6](https://arxiv.org/pdf/2106.11959v5#page=6 "#objects 20640 48842 65196 83733 98050 108000 500000 515345 581012 709877 1200192"))
- **c17** Most models were tuned with Optuna's TPE (Bayesian optimization); the rest used predefined configurations from their papers. The test set was never used for tuning.([Section 4.3, p.6](https://arxiv.org/pdf/2106.11959v5#page=6 "we use the Optuna library (Akiba et al., 2019) to run Bayesian optimization (the Tree-Structured Parzen Estimator algorithm)"))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### rmse(小さいほど良い)

繰り返し: Mean of 15 runs with different random seeds of the tuned configuration (Section 4.3).

| method | `gorishniy2021-ca-single` | `gorishniy2021-ye-single` | `gorishniy2021-ya-single` | `gorishniy2021-mi-single` |
|---|---|---|---|---|
| TabNet | 0.51 | 8.909 | 0.823 | 0.751 |
| SNN | 0.493 | 8.895 | 0.761 | 0.751 |
| AutoInt | 0.474 | 8.882 | 0.768 | 0.75 |
| GrowNet | 0.487 | 8.827 | 0.765 | 0.751 |
| MLP | 0.499 | 8.853 | 0.757 | 0.747 |
| DCN2 | 0.484 | 8.89 | 0.757 | 0.749 |
| NODE | 0.464 | **8.784** | **0.753** | **0.745** |
| ResNet | 0.486 | 8.846 | 0.757 | 0.748 |
| FT-Transformer | **0.459** | 8.855 | 0.756 | 0.746 |
| FT-Transformer (w/o feature biases) | 0.47 | 8.843 | – | 0.751 |

出典: [Table 2, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "TabNet 0.510 0.850 0.378 0.723 0.719 0.954 0.8896 8.909 0.957 0.823 0.751 7.5 (2.0)") / [Table 5, p.9](https://arxiv.org/pdf/2106.11959v5#page=9 "FT-Transformer (w/o feature biases) 0.470 0.381 0.724 0.727 0.958 8.843 0.964 0.751")

#### accuracy(大きいほど良い)

繰り返し: Mean of 15 runs with different random seeds of the tuned configuration (Section 4.3).

| method | `gorishniy2021-ad-single` | `gorishniy2021-he-single` | `gorishniy2021-ja-single` | `gorishniy2021-hi-single` | `gorishniy2021-al-single` | `gorishniy2021-ep-single` | `gorishniy2021-co-single` |
|---|---|---|---|---|---|---|---|
| TabNet | 0.85 | 0.378 | 0.723 | 0.719 | 0.954 | 0.8896 | 0.957 |
| SNN | 0.854 | 0.373 | 0.719 | 0.722 | 0.954 | 0.8975 | 0.961 |
| AutoInt | **0.859** | 0.372 | 0.721 | 0.725 | 0.945 | 0.8949 | 0.934 |
| GrowNet | 0.857 | – | – | 0.722 | – | 0.897 | – |
| MLP | 0.852 | 0.383 | 0.719 | 0.723 | 0.954 | 0.8977 | 0.962 |
| DCN2 | 0.853 | 0.385 | 0.716 | 0.723 | 0.955 | 0.8977 | 0.965 |
| NODE | 0.858 | 0.359 | 0.727 | 0.726 | 0.918 | 0.8958 | 0.958 |
| ResNet | 0.854 | **0.396** | 0.728 | 0.727 | **0.963** | 0.8969 | 0.964 |
| FT-Transformer | **0.859** | 0.391 | **0.732** | **0.729** | 0.96 | **0.8982** | **0.97** |
| FT-Transformer (w/o feature biases) | – | 0.381 | 0.724 | 0.727 | 0.958 | – | 0.964 |

出典: [Table 2, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "TabNet 0.510 0.850 0.378 0.723 0.719 0.954 0.8896 8.909 0.957 0.823 0.751 7.5 (2.0)") / [Table 5, p.9](https://arxiv.org/pdf/2106.11959v5#page=9 "FT-Transformer (w/o feature biases) 0.470 0.381 0.724 0.727 0.958 8.843 0.964 0.751")

#### average-rank(小さいほど良い)

繰り返し: Ranks computed per dataset by sorting the 15-seed mean scores (Table 2 caption).

| method | `gorishniy2021-avg-rank-single` |
|---|---|
| TabNet | 7.5 ± 2 |
| SNN | 6.4 ± 1.4 |
| AutoInt | 5.7 ± 2.3 |
| GrowNet | 5.7 ± 2.2 |
| MLP | 4.8 ± 1.9 |
| DCN2 | 4.7 ± 2 |
| NODE | 3.9 ± 2.8 |
| ResNet | 3.3 ± 1.8 |
| FT-Transformer | **1.8 ± 1.2** |

出典: [Table 2, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "TabNet 0.510 0.850 0.378 0.723 0.719 0.954 0.8896 8.909 0.957 0.823 0.751 7.5 (2.0)")

#### rmse(小さいほど良い)

繰り返し: 15 single models split into three disjoint groups of 5; predictions averaged within a group; mean over the three ensembles (Section 4.3).

| method | `gorishniy2021-ca-ensemble` | `gorishniy2021-ye-ensemble` | `gorishniy2021-ya-ensemble` | `gorishniy2021-mi-ensemble` |
|---|---|---|---|---|
| ResNet (tuned) | 0.478 | 8.77 | 0.751 | 0.745 |
| FT-Transformer (tuned) | 0.448 | 8.751 | 0.747 | 0.743 |
| NODE (tuned) | 0.464 | 8.784 | 0.753 | 0.745 |
| CatBoost (default) | 0.428 | 8.885 | 0.749 | 0.744 |
| FT-Transformer (default) | 0.454 | **8.727** | 0.747 | 0.742 |
| XGBoost (default) | 0.462 | 9.192 | 0.761 | 0.751 |
| XGBoost (tuned) | 0.431 | 8.819 | **0.732** | 0.742 |
| CatBoost (tuned) | **0.423** | 8.837 | 0.74 | **0.741** |

出典: [Table 3, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "ResNet 0.478 0.857 0.398 0.734 0.731 0.966 0.8976 8.770 0.967 0.751 0.745") / [Table 4, p.8](https://arxiv.org/pdf/2106.11959v5#page=8 "CatBoost 0.428 0.873 0.386 0.724 0.728 0.948 0.8893 8.885 0.910 0.749 0.744")

#### accuracy(大きいほど良い)

繰り返し: 15 single models split into three disjoint groups of 5; predictions averaged within a group; mean over the three ensembles (Section 4.3).

| method | `gorishniy2021-ad-ensemble` | `gorishniy2021-he-ensemble` | `gorishniy2021-ja-ensemble` | `gorishniy2021-hi-ensemble` | `gorishniy2021-al-ensemble` | `gorishniy2021-ep-ensemble` | `gorishniy2021-co-ensemble` |
|---|---|---|---|---|---|---|---|
| ResNet (tuned) | 0.857 | **0.398** | 0.734 | **0.731** | 0.966 | 0.8976 | 0.967 |
| FT-Transformer (tuned) | 0.86 | **0.398** | **0.739** | **0.731** | **0.967** | **0.8984** | **0.973** |
| NODE (tuned) | 0.858 | 0.359 | 0.727 | 0.726 | 0.918 | 0.8958 | 0.958 |
| CatBoost (default) | 0.873 | 0.386 | 0.724 | 0.728 | 0.948 | 0.8893 | 0.91 |
| FT-Transformer (default) | 0.86 | 0.395 | 0.734 | **0.731** | 0.966 | 0.8969 | **0.973** |
| XGBoost (default) | **0.874** | 0.348 | 0.711 | 0.717 | 0.924 | 0.8799 | 0.964 |
| XGBoost (tuned) | 0.872 | 0.377 | 0.724 | 0.728 | – | 0.8861 | 0.969 |
| CatBoost (tuned) | **0.874** | 0.388 | 0.727 | 0.729 | – | 0.8898 | 0.968 |

出典: [Table 3, p.7](https://arxiv.org/pdf/2106.11959v5#page=7 "ResNet 0.478 0.857 0.398 0.734 0.731 0.966 0.8976 8.770 0.967 0.751 0.745") / [Table 4, p.8](https://arxiv.org/pdf/2106.11959v5#page=8 "CatBoost 0.428 0.873 0.386 0.724 0.728 0.948 0.8893 8.885 0.910 0.749 0.744")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| AutoInt | DCN2 | 5 | 0 | 7 |
| AutoInt | FT-Transformer | 0 | 1 | 11 |
| AutoInt | FT-Transformer (w/o feature biases) | 1 | 0 | 7 |
| AutoInt | GrowNet | 4 | 1 | 3 |
| AutoInt | MLP | 4 | 0 | 8 |
| AutoInt | NODE | 3 | 0 | 9 |
| AutoInt | ResNet | 2 | 0 | 10 |
| AutoInt | SNN | 7 | 0 | 5 |
| AutoInt | TabNet | 8 | 0 | 4 |
| CatBoost (default) | CatBoost (tuned) | 0 | 0 | 10 |
| CatBoost (default) | FT-Transformer (default) | 2 | 0 | 9 |
| CatBoost (default) | FT-Transformer (tuned) | 2 | 0 | 9 |
| CatBoost (default) | NODE (tuned) | 7 | 0 | 4 |
| CatBoost (default) | ResNet (tuned) | 4 | 0 | 7 |
| CatBoost (default) | XGBoost (default) | 9 | 0 | 2 |
| CatBoost (default) | XGBoost (tuned) | 4 | 2 | 4 |
| CatBoost (tuned) | FT-Transformer (default) | 4 | 0 | 6 |
| CatBoost (tuned) | FT-Transformer (tuned) | 4 | 0 | 6 |
| CatBoost (tuned) | NODE (tuned) | 7 | 1 | 2 |
| CatBoost (tuned) | ResNet (tuned) | 5 | 0 | 5 |
| CatBoost (tuned) | XGBoost (default) | 9 | 1 | 0 |
| CatBoost (tuned) | XGBoost (tuned) | 7 | 0 | 3 |
| DCN2 | FT-Transformer | 0 | 0 | 12 |
| DCN2 | FT-Transformer (w/o feature biases) | 3 | 0 | 5 |
| DCN2 | GrowNet | 6 | 0 | 2 |
| DCN2 | MLP | 6 | 3 | 3 |
| DCN2 | NODE | 4 | 0 | 8 |
| DCN2 | ResNet | 3 | 1 | 8 |
| DCN2 | SNN | 10 | 0 | 2 |
| DCN2 | TabNet | 11 | 0 | 1 |
| FT-Transformer | FT-Transformer (w/o feature biases) | 7 | 0 | 1 |
| FT-Transformer | GrowNet | 7 | 0 | 1 |
| FT-Transformer | MLP | 11 | 0 | 1 |
| FT-Transformer | NODE | 9 | 0 | 3 |
| FT-Transformer | ResNet | 9 | 0 | 3 |
| FT-Transformer | SNN | 12 | 0 | 0 |
| FT-Transformer | TabNet | 12 | 0 | 0 |
| FT-Transformer (default) | FT-Transformer (tuned) | 2 | 4 | 5 |
| FT-Transformer (default) | NODE (tuned) | 11 | 0 | 0 |
| FT-Transformer (default) | ResNet (tuned) | 6 | 3 | 2 |
| FT-Transformer (default) | XGBoost (default) | 10 | 0 | 1 |
| FT-Transformer (default) | XGBoost (tuned) | 6 | 1 | 3 |
| FT-Transformer (tuned) | NODE (tuned) | 11 | 0 | 0 |
| FT-Transformer (tuned) | ResNet (tuned) | 9 | 2 | 0 |
| FT-Transformer (tuned) | XGBoost (default) | 10 | 0 | 1 |
| FT-Transformer (tuned) | XGBoost (tuned) | 6 | 0 | 4 |
| FT-Transformer (w/o feature biases) | GrowNet | 2 | 1 | 1 |
| FT-Transformer (w/o feature biases) | MLP | 6 | 0 | 2 |
| FT-Transformer (w/o feature biases) | NODE | 4 | 0 | 4 |
| FT-Transformer (w/o feature biases) | ResNet | 2 | 2 | 4 |
| FT-Transformer (w/o feature biases) | SNN | 7 | 1 | 0 |
| FT-Transformer (w/o feature biases) | TabNet | 7 | 1 | 0 |
| GrowNet | MLP | 3 | 0 | 5 |
| GrowNet | NODE | 1 | 0 | 7 |
| GrowNet | ResNet | 3 | 0 | 5 |
| GrowNet | SNN | 4 | 2 | 2 |
| GrowNet | TabNet | 7 | 1 | 0 |
| MLP | NODE | 4 | 0 | 8 |
| MLP | ResNet | 2 | 1 | 9 |
| MLP | SNN | 8 | 2 | 2 |
| MLP | TabNet | 10 | 1 | 1 |
| NODE | ResNet | 5 | 0 | 7 |
| NODE | SNN | 8 | 0 | 4 |
| NODE | TabNet | 10 | 0 | 2 |
| NODE (tuned) | ResNet (tuned) | 2 | 1 | 8 |
| NODE (tuned) | XGBoost (default) | 7 | 0 | 4 |
| NODE (tuned) | XGBoost (tuned) | 3 | 0 | 7 |
| ResNet | SNN | 10 | 1 | 1 |
| ResNet | TabNet | 12 | 0 | 0 |
| ResNet (tuned) | XGBoost (default) | 9 | 0 | 2 |
| ResNet (tuned) | XGBoost (tuned) | 5 | 0 | 5 |
| SNN | TabNet | 8 | 2 | 2 |
| XGBoost (default) | XGBoost (tuned) | 1 | 0 | 9 |

