<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Lagged Exact Bayesian Online Changepoint Detection with Parameter Estimation

- カード: [`arxiv-1710.03276`](../../papers/arxiv-1710.03276.yaml)
- 著者: Michael Byrd, Linh Nghiem, Jing Cao
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1710.03276v3)(arXiv v3、カード作成時に読んだ版)
- タグ: bayesian-changepoint-models, online-change-point-detection, streaming
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Assumptions: observations form non-overlapping regimes (a product partition model); observations within a regime are i.i.d. and independent of other regimes.([Section 2, p.3](https://arxiv.org/pdf/1710.03276v3#page=3 "Further, assume that observations generated within the same regime are iid, and also independent from observations in other regimes"))
- **c2** Declaring changes from the run-length posterior in EXO is left to the practitioner, for example when the posterior mass shifts greatly toward 0 after being concentrated near the maximum run length.([Section 2, p.4](https://arxiv.org/pdf/1710.03276v3#page=4 "For instance, if the concentration of the mass of the run length’s distribution shifts greatly toward 0 at time t + 1 after being mostly concentrated around the max possible run length at time t, then this would indicate a change in the regime."))
- **c3** Hazard: as in Adams and MacKay, the prior on the interval between changepoints is geometric with time scale λgap, so the hazard is constant at 1/λgap.([Section 2, p.5](https://arxiv.org/pdf/1710.03276v3#page=5 "this prior distribution is chosen to be the geometric distribution"))
- **c4** LEXO-ℓ refines inference for time t-ℓ with a backward pass while staying online (past data need not be reused); Theorem 1 states it gives exact run-length posteriors computed recursively with complexity O(ℓt). The run-length pruning used with EXO (setting probabilities below a threshold, e.g. 10^-5, to 0) is said to extend easily to LEXO.([Section 2, p.8](https://arxiv.org/pdf/1710.03276v3#page=8 "Our algorithm remains online in the sense that once a new datum is observed the past data need not be reused to update the model."))
- **c5** The backward step relies on the fact that, if a new regime starts at t, the earlier data become irrelevant; the derivation uses that the changepoint probability given the previous run length is the constant hazard H.([Section 2, p.9](https://arxiv.org/pdf/1710.03276v3#page=9 "Intuitively, if we have a new regime at t, all the past information before that becomes irrelevant."))
- **c6** Theorem 2: the posterior of the regime parameter under LEXO-ℓ is a mixture of mixture models that can be computed exactly and recursively, and its posterior moments are computed in two recursive stages.([Section 3, p.10](https://arxiv.org/pdf/1710.03276v3#page=10 "is a mixture of mixture models and can be computed exactly and recursively for all"))
- **c7** Simulation protocol: three settings (Normal mean shift, Normal precision shift, Poisson), 5 equally spaced changepoints, 1000 samples each; non-informative priors and hazard H = 1/50; run length assessed by the median of the MAP run length (described as a common practitioner choice, citing Adams and MacKay) and parameters by the ratio of posterior MSE of EXO over LEXO-ℓ (ℓ = 1..30). The only comparison is EXO versus LEXO.([Section 4, p.13](https://arxiv.org/pdf/1710.03276v3#page=13 "The hyperparameters for the prior were chosen to be non-informative, and the hazard rate was chosen to be H = 1/50."))
- **c8** Caveat: right before a changepoint, a large number of lags can hurt parameter estimates (MSE ratio below 1) because the lags include points from the next regime, while detection does not deteriorate; the authors suggest a high lag for detection and a smaller lag for moment calculations.([Section 4, p.15](https://arxiv.org/pdf/1710.03276v3#page=15 "A reasonable solution is to use as higher order a lag as possible for the detection of changepoints, while using a smaller lag for moment calculations."))
- **c9** Real-data evaluation (Dow Jones 1972-75 returns, hazard 1/250, lags up to 100; coal mine disasters, lags up to 30) is qualitative: detected changepoints are matched to historical events, and for EXO the authors ignore random MAP jumps that appear to be mistakes.([Section 5, p.19](https://arxiv.org/pdf/1710.03276v3#page=19 "For EXO, we ignore random jumps that appear to be mistakes from the procedure."))

