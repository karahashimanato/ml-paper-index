<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift

- カード: [`arxiv-1810.11953`](../../papers/arxiv-1810.11953.yaml)
- 著者: Stephan Rabanser, Stephan Günnemann, Zachary C. Lipton
- 年・掲載: 2019 NeurIPS 2019
- 原論文: [PDF](https://arxiv.org/pdf/1810.11953v4)(arXiv v4、カード作成時に読んだ版)
- タグ: dataset-shift-detection, dimensionality-reduction-for-shift, supervised, two-sample-tests
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Across the explored shifts, two-sample testing on representations from a pre-trained label classifier (black-box shift detection) performed best.([Abstract, p.1](https://arxiv.org/pdf/1810.11953v4#page=1 "a two-sample-testing-based approach, using pre-trained classifiers for dimensionality reduction, performs best."))
- **c2** BBSD works surprisingly well across many shifts even when its label-shift assumption does not hold.([Introduction, p.2](https://arxiv.org/pdf/1810.11953v4#page=2 "We show (empirically) that BBSD works surprisingly well under a broad set of shifts, even when the label shift assumption is not met."))
- **c3** Aggregated univariate tests (KS + Bonferroni) performed comparably to multivariate kernel tests (MMD).([Experiments (results), p.6](https://arxiv.org/pdf/1810.11953v4#page=6 "despite the heavy correction, multiple univariate testing seem to offer comparable performance to multivariate testing"))
- **c4** BBSDs (softmax outputs) was the best dimensionality reduction for univariate testing and overall; an untrained autoencoder (UAE) was best for multivariate testing.([Experiments (results), p.6](https://arxiv.org/pdf/1810.11953v4#page=6 "In the multivariate-testing case, UAE performed best."))
- **c5** The domain classifier performs badly with few samples (<=100) but catches up with more samples.([Experiments (results), p.6](https://arxiv.org/pdf/1810.11953v4#page=6 "The domain classifier, a popular shift detection approach, performs badly in the low-sample regime (≤100 samples), but catches up as more samples are obtained."))
- **c6** Multivariate testing without dimensionality reduction performs poorly.([Experiments (results), p.6](https://arxiv.org/pdf/1810.11953v4#page=6 "the multivariate test performs poorly in the no reduction case"))
- **c7** Domain-discriminating classifiers help characterize shifts and judge whether they are harmful.([Abstract, p.1](https://arxiv.org/pdf/1810.11953v4#page=1 "we demonstrate that domain-discriminating approaches tend to be helpful for characterizing shifts qualitatively and determining if they are harmful."))
- **c8** In practice, ML pipelines rarely inspect incoming data for distribution shift.([Introduction, p.1](https://arxiv.org/pdf/1810.11953v4#page=1 "in practice, ML pipelines rarely inspect incoming data for signs of distribution shift."))
- **c9** Kernel two-sample tests scale badly with sample size and lose power in high dimensions.([Introduction, p.2](https://arxiv.org/pdf/1810.11953v4#page=2 "they scale badly with dataset size and their statistical power is known to decay badly with high ambient dimension"))
- **c10** Detection results are averaged over 5 random splits, at significance level 0.05.([Experiments, p.6](https://arxiv.org/pdf/1810.11953v4#page=6 "shift detection performance is averaged over a total of 5 random splits"))
- **c11** The original MNIST train/test split is not i.i.d. (a statistically significant but harmless shift in the digit 6).([Experiments (results), p.9](https://arxiv.org/pdf/1810.11953v4#page=9 "this result however still shows that the original MNIST split is not i.i.d."))
- **c12** The experiments mostly use standard image classification; other domains (NLP, graphs) and online data are left for future work.([Conclusions, p.9](https://arxiv.org/pdf/1810.11953v4#page=9 "since we have mostly explored a standard image classification setting for our experiments"))
- **c13** A detected shift is not necessarily harmful: on COIL-100 the detected shift did not hurt the classifier.([Experiments (results), p.9](https://arxiv.org/pdf/1810.11953v4#page=9 "this shift does not harm the classifier's performance"))
- **c14** Shift detection for online (streaming) data would need to handle correlation between adjacent time steps (future work).([Conclusions, p.9](https://arxiv.org/pdf/1810.11953v4#page=9 "shift detection for online data, which would require us to account for and exploit the high degree of correlation between adjacent time steps"))

## 結果表

列ごとに比較条件が異なる。**同じ列の中だけ**比較できる。太字は列内の最良値。

#### detection-accuracy(大きいほど良い)

繰り返し: Detection accuracy averaged over 5 random splits and all simulated shift types/intensities/fractions (Table 1a).

| method | `rabanser2019-shift-suite-n10` | `rabanser2019-shift-suite-n20` | `rabanser2019-shift-suite-n50` | `rabanser2019-shift-suite-n100` | `rabanser2019-shift-suite-n200` | `rabanser2019-shift-suite-n500` | `rabanser2019-shift-suite-n1000` | `rabanser2019-shift-suite-n10000` |
|---|---|---|---|---|---|---|---|---|
| NoRed + KS (Bonferroni) | 0.03 | 0.15 | 0.26 | 0.36 | 0.41 | 0.47 | 0.54 | 0.72 |
| PCA + KS (Bonferroni) | 0.11 | 0.15 | 0.3 | 0.36 | 0.41 | 0.46 | 0.54 | 0.63 |
| SRP + KS (Bonferroni) | 0.15 | 0.15 | 0.23 | 0.27 | 0.34 | 0.42 | 0.55 | 0.68 |
| UAE + KS (Bonferroni) | 0.12 | 0.16 | 0.27 | 0.33 | 0.41 | 0.49 | 0.56 | 0.77 |
| TAE + KS (Bonferroni) | 0.18 | 0.23 | 0.31 | 0.38 | 0.43 | 0.47 | 0.55 | 0.69 |
| BBSDs + KS (Bonferroni) | 0.19 | **0.28** | **0.47** | **0.47** | **0.51** | **0.65** | **0.7** | **0.79** |
| BBSDh + Chi-squared | 0.03 | 0.07 | 0.12 | 0.22 | 0.22 | 0.4 | 0.46 | 0.57 |
| Classif + Binomial | 0.01 | 0.03 | 0.11 | 0.21 | 0.28 | 0.42 | 0.51 | 0.67 |
| NoRed + MMD | 0.14 | 0.15 | 0.22 | 0.28 | 0.32 | 0.44 | 0.55 | – |
| PCA + MMD | 0.15 | 0.18 | 0.33 | 0.38 | 0.4 | 0.46 | 0.55 | – |
| SRP + MMD | 0.12 | 0.18 | 0.23 | 0.31 | 0.31 | 0.44 | 0.54 | – |
| UAE + MMD | **0.2** | 0.27 | 0.4 | 0.43 | 0.45 | 0.53 | 0.61 | – |
| TAE + MMD | 0.18 | 0.26 | 0.37 | 0.38 | 0.45 | 0.52 | 0.59 | – |
| BBSDs + MMD | 0.16 | 0.2 | 0.25 | 0.35 | 0.35 | 0.47 | 0.5 | – |

出典: [Table 1(a), p.7](https://arxiv.org/pdf/1810.11953v4#page=7 "NoRed 0.03 0.15 0.26 0.36 0.41 0.47 0.54 0.72")

## 論文内の勝敗(結果から導出)

同じ比較条件での数値の大小だけを数えたもの。**統計的有意性は考慮していない**。

| A | B | A勝ち | 引き分け | B勝ち |
|---|---|---|---|---|
| BBSDh + Chi-squared | BBSDs + KS (Bonferroni) | 0 | 0 | 8 |
| BBSDh + Chi-squared | BBSDs + MMD | 0 | 0 | 7 |
| BBSDh + Chi-squared | Classif + Binomial | 4 | 0 | 4 |
| BBSDh + Chi-squared | NoRed + KS (Bonferroni) | 0 | 1 | 7 |
| BBSDh + Chi-squared | NoRed + MMD | 0 | 0 | 7 |
| BBSDh + Chi-squared | PCA + KS (Bonferroni) | 0 | 0 | 8 |
| BBSDh + Chi-squared | PCA + MMD | 0 | 0 | 7 |
| BBSDh + Chi-squared | SRP + KS (Bonferroni) | 0 | 0 | 8 |
| BBSDh + Chi-squared | SRP + MMD | 0 | 0 | 7 |
| BBSDh + Chi-squared | TAE + KS (Bonferroni) | 0 | 0 | 8 |
| BBSDh + Chi-squared | TAE + MMD | 0 | 0 | 7 |
| BBSDh + Chi-squared | UAE + KS (Bonferroni) | 0 | 0 | 8 |
| BBSDh + Chi-squared | UAE + MMD | 0 | 0 | 7 |
| BBSDs + KS (Bonferroni) | BBSDs + MMD | 7 | 0 | 0 |
| BBSDs + KS (Bonferroni) | Classif + Binomial | 8 | 0 | 0 |
| BBSDs + KS (Bonferroni) | NoRed + KS (Bonferroni) | 8 | 0 | 0 |
| BBSDs + KS (Bonferroni) | NoRed + MMD | 7 | 0 | 0 |
| BBSDs + KS (Bonferroni) | PCA + KS (Bonferroni) | 8 | 0 | 0 |
| BBSDs + KS (Bonferroni) | PCA + MMD | 7 | 0 | 0 |
| BBSDs + KS (Bonferroni) | SRP + KS (Bonferroni) | 8 | 0 | 0 |
| BBSDs + KS (Bonferroni) | SRP + MMD | 7 | 0 | 0 |
| BBSDs + KS (Bonferroni) | TAE + KS (Bonferroni) | 8 | 0 | 0 |
| BBSDs + KS (Bonferroni) | TAE + MMD | 7 | 0 | 0 |
| BBSDs + KS (Bonferroni) | UAE + KS (Bonferroni) | 8 | 0 | 0 |
| BBSDs + KS (Bonferroni) | UAE + MMD | 6 | 0 | 1 |
| BBSDs + MMD | Classif + Binomial | 6 | 0 | 1 |
| BBSDs + MMD | NoRed + KS (Bonferroni) | 2 | 1 | 4 |
| BBSDs + MMD | NoRed + MMD | 6 | 0 | 1 |
| BBSDs + MMD | PCA + KS (Bonferroni) | 3 | 0 | 4 |
| BBSDs + MMD | PCA + MMD | 3 | 0 | 4 |
| BBSDs + MMD | SRP + KS (Bonferroni) | 6 | 0 | 1 |
| BBSDs + MMD | SRP + MMD | 6 | 0 | 1 |
| BBSDs + MMD | TAE + KS (Bonferroni) | 0 | 1 | 6 |
| BBSDs + MMD | TAE + MMD | 0 | 0 | 7 |
| BBSDs + MMD | UAE + KS (Bonferroni) | 3 | 0 | 4 |
| BBSDs + MMD | UAE + MMD | 0 | 0 | 7 |
| Classif + Binomial | NoRed + KS (Bonferroni) | 0 | 0 | 8 |
| Classif + Binomial | NoRed + MMD | 0 | 0 | 7 |
| Classif + Binomial | PCA + KS (Bonferroni) | 1 | 0 | 7 |
| Classif + Binomial | PCA + MMD | 0 | 0 | 7 |
| Classif + Binomial | SRP + KS (Bonferroni) | 0 | 1 | 7 |
| Classif + Binomial | SRP + MMD | 0 | 0 | 7 |
| Classif + Binomial | TAE + KS (Bonferroni) | 0 | 0 | 8 |
| Classif + Binomial | TAE + MMD | 0 | 0 | 7 |
| Classif + Binomial | UAE + KS (Bonferroni) | 0 | 0 | 8 |
| Classif + Binomial | UAE + MMD | 0 | 0 | 7 |
| NoRed + KS (Bonferroni) | NoRed + MMD | 4 | 1 | 2 |
| NoRed + KS (Bonferroni) | PCA + KS (Bonferroni) | 2 | 4 | 2 |
| NoRed + KS (Bonferroni) | PCA + MMD | 2 | 0 | 5 |
| NoRed + KS (Bonferroni) | SRP + KS (Bonferroni) | 5 | 1 | 2 |
| NoRed + KS (Bonferroni) | SRP + MMD | 4 | 1 | 2 |
| NoRed + KS (Bonferroni) | TAE + KS (Bonferroni) | 1 | 1 | 6 |
| NoRed + KS (Bonferroni) | TAE + MMD | 0 | 0 | 7 |
| NoRed + KS (Bonferroni) | UAE + KS (Bonferroni) | 1 | 1 | 6 |
| NoRed + KS (Bonferroni) | UAE + MMD | 0 | 0 | 7 |
| NoRed + MMD | PCA + KS (Bonferroni) | 2 | 1 | 4 |
| NoRed + MMD | PCA + MMD | 0 | 1 | 6 |
| NoRed + MMD | SRP + KS (Bonferroni) | 2 | 2 | 3 |
| NoRed + MMD | SRP + MMD | 3 | 1 | 3 |
| NoRed + MMD | TAE + KS (Bonferroni) | 0 | 1 | 6 |
| NoRed + MMD | TAE + MMD | 0 | 0 | 7 |
| NoRed + MMD | UAE + KS (Bonferroni) | 1 | 0 | 6 |
| NoRed + MMD | UAE + MMD | 0 | 0 | 7 |
| PCA + KS (Bonferroni) | PCA + MMD | 1 | 1 | 5 |
| PCA + KS (Bonferroni) | SRP + KS (Bonferroni) | 4 | 1 | 3 |
| PCA + KS (Bonferroni) | SRP + MMD | 4 | 1 | 2 |
| PCA + KS (Bonferroni) | TAE + KS (Bonferroni) | 0 | 0 | 8 |
| PCA + KS (Bonferroni) | TAE + MMD | 0 | 0 | 7 |
| PCA + KS (Bonferroni) | UAE + KS (Bonferroni) | 2 | 1 | 5 |
| PCA + KS (Bonferroni) | UAE + MMD | 0 | 0 | 7 |
| PCA + MMD | SRP + KS (Bonferroni) | 5 | 2 | 0 |
| PCA + MMD | SRP + MMD | 6 | 1 | 0 |
| PCA + MMD | TAE + KS (Bonferroni) | 1 | 2 | 4 |
| PCA + MMD | TAE + MMD | 0 | 1 | 6 |
| PCA + MMD | UAE + KS (Bonferroni) | 4 | 0 | 3 |
| PCA + MMD | UAE + MMD | 0 | 0 | 7 |
| SRP + KS (Bonferroni) | SRP + MMD | 3 | 1 | 3 |
| SRP + KS (Bonferroni) | TAE + KS (Bonferroni) | 0 | 1 | 7 |
| SRP + KS (Bonferroni) | TAE + MMD | 0 | 0 | 7 |
| SRP + KS (Bonferroni) | UAE + KS (Bonferroni) | 1 | 0 | 7 |
| SRP + KS (Bonferroni) | UAE + MMD | 0 | 0 | 7 |
| SRP + MMD | TAE + KS (Bonferroni) | 0 | 0 | 7 |
| SRP + MMD | TAE + MMD | 0 | 0 | 7 |
| SRP + MMD | UAE + KS (Bonferroni) | 1 | 1 | 5 |
| SRP + MMD | UAE + MMD | 0 | 0 | 7 |
| TAE + KS (Bonferroni) | TAE + MMD | 0 | 2 | 5 |
| TAE + KS (Bonferroni) | UAE + KS (Bonferroni) | 5 | 0 | 3 |
| TAE + KS (Bonferroni) | UAE + MMD | 0 | 0 | 7 |
| TAE + MMD | UAE + KS (Bonferroni) | 7 | 0 | 0 |
| TAE + MMD | UAE + MMD | 0 | 1 | 6 |
| UAE + KS (Bonferroni) | UAE + MMD | 0 | 0 | 7 |

