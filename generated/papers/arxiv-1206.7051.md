<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Stochastic Variational Inference

- カード: [`arxiv-1206.7051`](../../papers/arxiv-1206.7051.yaml)
- 著者: Matt Hoffman, David M. Blei, Chong Wang, John Paisley
- 年・掲載: 2012 JMLR
- 原論文: [PDF](https://arxiv.org/pdf/1206.7051v3)(arXiv v3、カード作成時に読んだ版)
- タグ: language-modeling, posterior-inference, unsupervised, variational-inference
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: neither MCMC nor VI scales easily to massive data; according to the authors, proposed speed-ups of both are usually tailored to specific models or compromise the correctness of the algorithm (or both).([Section 1 (Introduction), p.4](https://arxiv.org/pdf/1206.7051v3#page=4 "Researchers have proposed speed-ups of both approaches, but these usually are tailored to speciﬁc models or compromise the correctness of the algorithm (or both)."))
- **c2** Inefficiency of batch coordinate-ascent VI: global parameters are initialized randomly, yet every data point must be analyzed with these uninformative values before even one global update is completed.([Section 2.2, p.12](https://arxiv.org/pdf/1206.7051v3#page=12 "This is wasteful, especially if we expect that we can learn something about the global variational parameters from only a subset of the data."))
- **c3** SVI update: sample a data point, optimize its local variational parameters, compute intermediate global parameters as if that point were replicated N times, and set the new global parameters to a weighted average of the old ones and the intermediate ones; this is a step along a noisy but unbiased natural gradient of the ELBO.([Section 2.4, p.17](https://arxiv.org/pdf/1206.7051v3#page=17 "This is a weighted average of the previous estimate of λ and the estimate of λ that we would obtain if the sampled data point was replicated N times."))
- **c4** Step size rho_t = (t + tau)^-kappa with forgetting rate kappa in (0.5, 1] and delay tau >= 0 satisfies the Robbins-Monro conditions; as long as these hold, the algorithm converges to a local optimum of the ELBO (not a global one).([Section 2.4, p.18](https://arxiv.org/pdf/1206.7051v3#page=18 "As long as the step size conditions in Equation 23 are satisﬁed, this iterative algorithm converges to a local optimum of the ELBO."))
- **c5** Minibatches amortize the cost of global updates and may help find better local optima: SVI is guaranteed to converge to a local optimum, but taking large steps based on very few data points may lead to a poor one.([Section 2.5, p.19](https://arxiv.org/pdf/1206.7051v3#page=19 "Stochastic variational inference is guaranteed to converge to a local optimum but taking large steps on the basis of very few data points may lead to a poor one."))
- **c6** Evaluation protocol: three corpora (Nature 350K documents, New York Times 1.8M, Wikipedia 3.8M), each with a held-out test set of 10,000 documents; model fit is measured by the per-word predictive log likelihood of held-out words given the observed part of each test document, which the authors prefer over held-out perplexity because it avoids comparing bounds.([Section 4, p.34](https://arxiv.org/pdf/1206.7051v3#page=34 "Unlike previous methods, like held-out perplexity (Blei et al., 2003), evaluating the predictive distribution avoids comparing bounds or forming approximations of the evaluation metric."))
- **c7** Comparison with batch VI for 100-topic LDA: SVI on the full collection vs batch inference on a subset of 100,000 documents (described as the size batch inference can handle); the authors state SVI converges faster and to a better model (shown in a figure).([Section 3.2, p.22](https://arxiv.org/pdf/1206.7051v3#page=22 "We see that stochastic variational inference converges faster and to a better model."))
- **c8** Sensitivity to learning parameters (HDP, batch size 500): all three fits were sensitive to the forgetting rate kappa, with values close to one converging to a better local optimum; batch sizes that are too small (e.g. ten documents) can affect performance. Grid: kappa in {0.5,...,1.0}, S in {10, 50, 100, 500, 1000}, tau = 1 (the algorithms were reported not sensitive to tau).([Section 4, p.37](https://arxiv.org/pdf/1206.7051v3#page=37 "All three ﬁts were sensitive to the forgetting rate; we see that a higher value (i.e., close to one) leads to convergence to a better local optimum."))
- **c9** Scope limitation: the algorithm was developed for conjugate exponential-family models with mean-field VI and closed-form coordinate updates; the general algorithm cannot be used for nonconjugate models (e.g. correlated or dynamic topic models). The authors also ask whether the gradient variance can be reduced while keeping unbiasedness.([Section 5 (Discussion), p.38](https://arxiv.org/pdf/1206.7051v3#page=38 "We developed our algorithm with conjugate exponential family models."))

