<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Distillation of Synthetic Data for Time Series Foundation Models

- カード: [`arxiv-2609.09586`](../../papers/arxiv-2609.09586.yaml)
- 著者: Niloy Biswas, Noureddine El Karoui
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.09586v2)(arXiv v2、カード作成時に読んだ版)
- タグ: time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** SDD replaces the usual loss against the realized future values of a synthetic trajectory with a loss against the trajectory's conditional forecast distribution.([Abstract, p.1](https://arxiv.org/pdf/2609.09586v2#page=1 "We instead propose loss objectives which compare TSFM outputs to the conditional forecast distribution of each trajectory, a procedure we call synthetic data distillation (SDD)."))
- **c2** SDD is a Rao-Blackwellization of the training objective: the expected stochastic gradient is unchanged while its covariance is provably reduced.([Abstract, p.1](https://arxiv.org/pdf/2609.09586v2#page=1 "SDD corresponds to a Rao-Blackwellization of the training objective, in that it leaves the expectation of stochastic gradients unchanged while provably reducing the covariance of the stochastic gradient under the Loewner partial ordering."))
- **c3** SDD reaches the same validation loss as the status-quo loss with fewer FLOPs, with the speed-up depending on model size.([Numerical Experiments, p.4](https://arxiv.org/pdf/2609.09586v2#page=4 "Figure 2 shows that SDD attains the same validation loss as Status Quo while spending 38-46% fewer FLOPs, a convergence speed-up of 1.6× to 1.85× depending on model size."))
- **c4** Experimental setup: five Toto-2 architectures are pre-trained from random initialization on univariate Gaussian-process trajectories only.([Numerical Experiments, p.4](https://arxiv.org/pdf/2609.09586v2#page=4 "We pre-train the five Toto-2 architectures [9], spanning 4M to 2.5B parameters, from random initialization on trajectories from univariate Gaussian processes of length T = 512."))
- **c5** The held-out validation set is drawn fresh from the same synthetic generator (with disjoint seeds), so no real-world forecasting benchmark is used.([Experimental Details (appendix), p.11](https://arxiv.org/pdf/2609.09586v2#page=11 "Held-out throughout means a validation set drawn fresh from the same generator, using generator seeds disjoint from those that produced the training data, rather than a held-out split of the training corpus."))
- **c6** Seeds vary only initialization and masking draws, not the training corpus, so the reported error bars understate the spread from retraining on a freshly drawn corpus.([Experimental Details (appendix), p.11](https://arxiv.org/pdf/2609.09586v2#page=11 "The error bars therefore carry no data-sampling variability and understate the spread that retraining on a freshly drawn corpus would show."))

