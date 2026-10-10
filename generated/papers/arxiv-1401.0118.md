<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Black Box Variational Inference

- カード: [`arxiv-1401.0118`](../../papers/arxiv-1401.0118.yaml)
- 著者: Rajesh Ranganath, Sean Gerrish, David M. Blei
- 年・掲載: 2013
- 原論文: [PDF](https://arxiv.org/pdf/1401.0118v1)(arXiv v1、カード作成時に読んだ版)
- タグ: mcmc, posterior-inference, unsupervised, variational-inference
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: for generic models and variational families, closed-form coordinate ascent is unavailable and practitioners resort to model-specific algorithms; the authors describe deriving these model by model as tedious, which hinders rapid model exploration.([Section 1 (Introduction), p.1](https://arxiv.org/pdf/1401.0118v1#page=1 "Deriving these algorithms on a model-by-model basis is tedious work."))
- **c2** Score-function gradient: the ELBO gradient is written as E_q[grad log q(z|lambda) (log p(x,z) - log q(z|lambda))] and estimated with S samples from q; the score function and sampling routines depend only on the variational family, and the only model requirement is evaluating the log joint p(x, z).([Section 2, p.3](https://arxiv.org/pdf/1401.0118v1#page=3 "We emphasize that the score function and sampling algorithms depend only on the variational distribution, not the underlying model."))
- **c3** Failure mode of the basic estimator: its variance can be too large to be useful; high-variance gradients would require very small steps and lead to slow convergence.([Section 3, p.3](https://arxiv.org/pdf/1401.0118v1#page=3 "In practice, the high variance gradients would require very small steps which would lead to slow convergence."))
- **c4** Rao-Blackwellization under the mean-field family: each gradient component can use only the terms of the joint that depend on that variable's Markov blanket, giving a lower-variance estimator without model-specific integrals.([Section 3.1, p.4](https://arxiv.org/pdf/1401.0118v1#page=4 "This equation says that Rao-Blackwellized estimators can be computed for each component of the gradient without needing to compute model-speciﬁc conditional expectations."))
- **c5** Control variate: the score function of the variational approximation is used because it always has expectation zero and depends only on the variational distribution; the scaling a* = Cov(f, h)/Var(h) is estimated from the same Monte Carlo samples.([Section 3.2, p.4](https://arxiv.org/pdf/1401.0118v1#page=4 "This equation implies that good control variates have high covariance with the function whose expectation is being computed."))
- **c6** Evaluation protocol: longitudinal data of 976 chronic-kidney-disease patients (803 train + 173 test, about 33K visits, 17 labs) with a nonconjugate Gamma-Normal time-series model; fully factorized gamma/normal variational families, AdaGrad and data subsampling, 1,000 samples from q and batch size 25; predictive likelihood on 25% of held-out test data after fitting local parameters on 75%.([Section 5, p.6](https://arxiv.org/pdf/1401.0118v1#page=6 "We use 1,000 samples from the variational distribution and set the batch size at 25 in all our experiments."))
- **c7** Comparison with sampling (fixed 20-hour budget): standard Metropolis-Hastings is stated to fail on the Gamma-Normal-TS model, so BBVI is compared with Metropolis-Hastings within Gibbs; the authors report BBVI reaches better predictive likelihoods faster (figure). A footnote notes that methods requiring a bit more work, such as HMC, could work in this setting but were not compared.([Section 5.3, p.7](https://arxiv.org/pdf/1401.0118v1#page=7 "We ﬁnd that it fails for the Gamma-Normal-TS model."))
- **c8** Variance reduction result: Rao-Blackwellization reduced gradient variance by several orders of magnitude and control variates reduced it further; in the time allotted, the algorithm without variance reductions failed to make noticeable progress.([Section 5.4, p.7](https://arxiv.org/pdf/1401.0118v1#page=7 "We found that Rao-Blackwellization reduces the variance by several orders of magnitude."))

