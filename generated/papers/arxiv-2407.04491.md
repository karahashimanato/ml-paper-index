<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Better by Default: Strong Pre-Tuned MLPs and Boosted Trees on Tabular Data

- カード: [`arxiv-2407.04491`](../../papers/arxiv-2407.04491.yaml)
- 著者: David Holzmüller, Léo Grinsztajn, Ingo Steinwart
- 年・掲載: 2024 NeurIPS 2024
- 原論文: [PDF](https://arxiv.org/pdf/2407.04491v3)(arXiv v3、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, random-forests, supervised, tabular-attention, tabular-classification, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** RealMLP offers a favorable time-accuracy tradeoff compared with other neural baselines and is competitive with GBDTs on medium-to-large datasets.([Abstract, p.1](https://arxiv.org/pdf/2407.04491v3#page=1 "RealMLP offers a favorable time-accuracy tradeoff compared to other neural baselines and is competitive with GBDTs in terms of benchmark scores."))
- **c2** Combining RealMLP and GBDTs with improved default parameters gives excellent results without hyperparameter tuning.([Abstract, p.1](https://arxiv.org/pdf/2407.04491v3#page=1 "a combination of RealMLP and GBDTs with improved default parameters can achieve excellent results without hyperparameter tuning."))
- **c3** Defaults are tuned on a meta-train benchmark of 118 datasets and evaluated on a disjoint meta-test benchmark of 90 datasets.([Abstract, p.1](https://arxiv.org/pdf/2407.04491v3#page=1 "We tune RealMLP and the default parameters on a meta-train benchmark with 118 datasets and compare them to hyperparameter-optimized versions on a disjoint meta-test benchmark with 90 datasets"))
- **c4** The benchmarks cover medium-to-large datasets (1K-500K samples).([Abstract, p.1](https://arxiv.org/pdf/2407.04491v3#page=1 "Our benchmark results on medium-to-large tabular datasets (1K–500K samples)"))
- **c5** Unlike McElfresh et al., who favor tuning CatBoost over trying NNs, the authors' results favor model portfolios as in AutoML systems.([Section 5, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "Unlike McElfresh et al. [43], who argue in favor of CatBoost-HPO over trying NNs, our results favor model portfolios as used in modern AutoML systems [10]."))
- **c6** Trying all default (tuned-default) algorithms is faster and very often better than naive single-algorithm HPO.([Section 5, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "Simply trying all default algorithms is faster and very often better than (naive) single-algorithm HPO."))
- **c7** RealMLP's tuned defaults transfer very well from meta-train to meta-test.([Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "indicating that the tuned defaults transfer very well to the meta-test benchmark."))
- **c8** For GBDTs, tuned defaults match HPO on meta-train but not on meta-test (still clearly better than library defaults).([Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "For GBDTs, tuned defaults are competitive with HPO on the meta-train set, but not as good on the meta-test set."))
- **c9** Using AUROC instead of classification error favors GBDTs.([Section 6, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "For classification, using AUROC instead of classification error (Figure 3, Appendix B.5) favors GBDTs."))
- **c10** Aggregation metrics other than the shifted geometric mean reduce the advantage of tuned-default methods.([Section 6, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "The use of different aggregation metrics than the shifted geometric mean reduces the advantage of TD methods"))
- **c11** Non-architectural aspects are not equalized across NN models, so the work is not a comparison of architectures.([Section 6 Limitations, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "our work should therefore not be seen as a comparison of architectures."))
- **c12** Generalization of the defaults to very small data, distribution shift, missing numerical values and other metrics such as log-loss is unclear.([Section 6 Limitations, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "it is unclear to which extent the obtained defaults can generalize to very small datasets, distribution shifts, datasets with missing numerical values, and other metrics such as log-loss."))
- **c13** Each dataset is evaluated on 10 random 60/20/20 train/validation/test splits.([Section 2.2, p.4](https://arxiv.org/pdf/2407.04491v3#page=4 "we evaluate a method on Nsplits = 10 random training-validation-test splits (60%-20%-20%) on each dataset."))
- **c14** HPO uses 50 steps of random search per split and dataset.([Section 5, p.7](https://arxiv.org/pdf/2407.04491v3#page=7 "Hyperparameters optimized separately for every train-test split on every dataset, using 50 steps of random search."))
- **c15** XGBoost results on some (mainly meta-test) datasets are affected by a bug in handling rare categories.([Figure 2 caption, p.8](https://arxiv.org/pdf/2407.04491v3#page=8 "Note that XGB results on some (mainly meta-test) datasets are affected by a bug in handling rare categories, see Appendix B."))
- **c16** On the electricity dataset MLPs struggle to learn high-frequency patterns.([Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "where MLPs struggle to learn high-frequency patterns"))
- **c17** Among GBDTs, CatBoost defaults are better but slower.([Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "Among GBDTs, CatBoost defaults are better and slower."))
- **c18** RealMLP's numerical preprocessing (robust scaling + smooth clipping) is easy to adopt and often helps other NNs.([Section 6, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "our numerical preprocessing is easy to adopt and often beneficial for other NNs as well"))
- **c19** Label smoothing is influential but can hurt metrics like AUROC.([Section 6, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "label smoothing is influential but can be detrimental for metrics like AUROC"))
- **c20** A single training-validation split per train-test split means HPO can overfit the validation set more easily than with cross-validation.([Section 6 Limitations, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "This means that HPO can overfit the validation set more easily than in a cross-validation setup."))
- **c21** With good default parameters it is worth trying both NNs and GBDTs, even with a moderate time budget.([Section 7, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "with good default parameters, it is worth trying both algorithm families even with a moderate training time budget."))

## 論文内の勝敗(本文の記述)

| 勝ち | 負け | 根拠 | 比較条件 | 出典 |
|---|---|---|---|---|
| RealMLP and RealTabR | GBDTs (XGBoost, LightGBM, CatBoost) | Shifted geometric mean error on the meta-train benchmarks (Figure 2); the sentence does not specify D/TD/HPO variants. | `holzmuller2024-meta-train` | [Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "On the meta-train and meta-test benchmarks, RealMLP and RealTabR perform better than GBDTs in terms of shifted geometric mean error") |
| RealMLP and RealTabR | GBDTs (XGBoost, LightGBM, CatBoost) | Shifted geometric mean error on the meta-test benchmarks (Figure 2); the sentence does not specify D/TD/HPO variants. | `holzmuller2024-meta-test` | [Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "On the meta-train and meta-test benchmarks, RealMLP and RealTabR perform better than GBDTs in terms of shifted geometric mean error") |
| CatBoost | RealMLP | Grinsztajn et al. classification benchmark under this paper's protocol (Figure 2). | `holzmuller2024-grinsztajn` | [Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "On the Grinsztajn et al. [18] benchmark, RealMLP performs worse than CatBoost for classification and comparably for regression, while RealTabR-D performs comparably to CatBoost-TD for classification and better for regression.") |
| RealTabR-D | CatBoost-TD | Grinsztajn et al. regression benchmark under this paper's protocol (Figure 2). | `holzmuller2024-grinsztajn` | [Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "On the Grinsztajn et al. [18] benchmark, RealMLP performs worse than CatBoost for classification and comparably for regression, while RealTabR-D performs comparably to CatBoost-TD for classification and better for regression.") |
| RealTabR-D | RealMLP-TD | Four out of six benchmarks, especially all regression benchmarks (Figure 2). | – | [Section 5, p.9](https://arxiv.org/pdf/2407.04491v3#page=9 "RealTabR-D performs even better on four out of six benchmarks, especially all regression benchmarks.") |
| RealMLP-HPO | Best-D (best of library-default XGB, LGBM, CatBoost, MLP-PLR) | Benchmark scores in Figure 2 ('often'). | – | [Section 5, p.10](https://arxiv.org/pdf/2407.04491v3#page=10 "Best-D is often outperformed by RealMLP-HPO.") |

