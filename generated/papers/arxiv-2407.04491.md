<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data

- カード: [`arxiv-2407.04491`](../../papers/arxiv-2407.04491.yaml)
- 著者: David Holzmüller, Léo Grinsztajn, Ingo Steinwart
- 年・掲載: 2024 NeurIPS 2024
- タグ: gradient-boosted-trees, random-forests, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

- **c1** RealMLP offers a favorable time-accuracy tradeoff compared with other neural baselines and is competitive with GBDTs on medium-to-large datasets.(Abstract)
- **c2** Combining RealMLP and GBDTs with improved default parameters gives excellent results without hyperparameter tuning.(Abstract)
- **c3** Defaults are tuned on a meta-train benchmark of 118 datasets and evaluated on a disjoint meta-test benchmark of 90 datasets.(Abstract)
- **c4** The benchmarks cover medium-to-large datasets (1K-500K samples).(Abstract)
- **c5** Unlike McElfresh et al., who favor tuning CatBoost over trying NNs, the authors' results favor model portfolios as in AutoML systems.(Section 5)
- **c6** Trying all default (tuned-default) algorithms is faster and very often better than naive single-algorithm HPO.(Section 5)
- **c7** RealMLP's tuned defaults transfer very well from meta-train to meta-test.(Section 5)
- **c8** For GBDTs, tuned defaults match HPO on meta-train but not on meta-test (still clearly better than library defaults).(Section 5)
- **c9** Using AUROC instead of classification error favors GBDTs.(Section 6)
- **c10** Aggregation metrics other than the shifted geometric mean reduce the advantage of tuned-default methods.(Section 6)
- **c11** Non-architectural aspects are not equalized across NN models, so the work is not a comparison of architectures.(Section 6 Limitations)
- **c12** Generalization of the defaults to very small data, distribution shift, missing numerical values and other metrics such as log-loss is unclear.(Section 6 Limitations)
- **c13** Each dataset is evaluated on 10 random 60/20/20 train/validation/test splits.(Section 2.2)
- **c14** HPO uses 50 steps of random search per split and dataset.(Section 5)
- **c15** XGBoost results on some (mainly meta-test) datasets are affected by a bug in handling rare categories.(Figure 2 caption)
- **c16** On the electricity dataset MLPs struggle to learn high-frequency patterns.(Section 5)
- **c17** Among GBDTs, CatBoost defaults are better but slower.(Section 5)
- **c18** RealMLP's numerical preprocessing (robust scaling + smooth clipping) is easy to adopt and often helps other NNs.(Section 6)
- **c19** Label smoothing is influential but can hurt metrics like AUROC.(Section 6)
- **c20** A single training-validation split per train-test split means HPO can overfit the validation set more easily than with cross-validation.(Section 6 Limitations)
- **c21** With good default parameters it is worth trying both NNs and GBDTs, even with a moderate time budget.(Section 7)

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| RealMLP and RealTabR | GBDTs (XGBoost, LightGBM, CatBoost) | Shifted geometric mean error on the meta-train benchmarks (Figure 2); the sentence does not specify D/TD/HPO variants. | `holzmuller2024-meta-train` | Section 5 |
| RealMLP and RealTabR | GBDTs (XGBoost, LightGBM, CatBoost) | Shifted geometric mean error on the meta-test benchmarks (Figure 2); the sentence does not specify D/TD/HPO variants. | `holzmuller2024-meta-test` | Section 5 |
| CatBoost | RealMLP | Grinsztajn et al. classification benchmark under this paper's protocol (Figure 2). | `holzmuller2024-grinsztajn` | Section 5 |
| RealTabR-D | CatBoost-TD | Grinsztajn et al. regression benchmark under this paper's protocol (Figure 2). | `holzmuller2024-grinsztajn` | Section 5 |
| RealTabR-D | RealMLP-TD | Four out of six benchmarks, especially all regression benchmarks (Figure 2). | – | Section 5 |
| RealMLP-HPO | Best-D (best of library-default XGB, LGBM, CatBoost, MLP-PLR) | Benchmark scores in Figure 2 ('often'). | – | Section 5 |

