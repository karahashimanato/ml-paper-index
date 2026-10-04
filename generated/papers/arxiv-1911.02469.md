<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Don't Blame the ELBO! A Linear VAE Perspective on Posterior Collapse

- カード: [`arxiv-1911.02469`](../../papers/arxiv-1911.02469.yaml)
- 著者: James Lucas, George Tucker, Roger Grosse, Mohammad Norouzi
- 年・掲載: 2019 NeurIPS 2019
- 原論文: [PDF](https://arxiv.org/pdf/1911.02469v1)(arXiv v1、カード作成時に読んだ版)
- タグ: generative-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Prevailing view being challenged: most existing papers attribute posterior collapse to the KL term in the ELBO, and many heuristics try to diminish the effect of the KL term.([Introduction, p.1](https://arxiv.org/pdf/1911.02469v1#page=1 "Most existing papers suggest that posterior collapse is caused by the KL-divergence term in the ELBO objective, which directly encourages the variational distribution to match the prior [7, 25, 38]."))
- **c2** Theoretical result: for a linear VAE, the ELBO does not introduce any spurious local maxima beyond those of the log marginal likelihood of probabilistic PCA, and its global optimum recovers the (scaled) principal components as the decoder columns.([Analysis of linear VAE, p.5](https://arxiv.org/pdf/1911.02469v1#page=5 "Theorem 1. The ELBO objective for a linear VAE does not introduce any additional local maxima to the pPCA model."))
- **c3** Posterior collapse can occur when optimizing the exact log marginal likelihood even without powerful decoders: in pPCA, collapsed stationary points (zeroed decoder columns) become stable local maxima as the observation noise sigma^2 grows, so learning sigma^2 is necessary for a full latent representation.([Analysis of linear VAE, p.4](https://arxiv.org/pdf/1911.02469v1#page=4 "Therefore, learning σ2 is necessary for gaining a full latent representation."))
- **c4** Critique of KL annealing (with Bowman et al. cited among its users): during annealing one is no longer optimizing a bound on the log-likelihood, schedules are hard to design, and the authors found that the posterior typically collapses again once regular ELBO training resumes.([Related work, p.3](https://arxiv.org/pdf/1911.02469v1#page=3 "Also, it is difﬁcult to design these annealing schedules and we have found that once regular ELBO training resumes the posterior will typically collapse again (Section 6.2)."))
- **c5** Measurement: the authors note that posterior collapse has not been measured or defined consistently and define a latent dimension as (epsilon, delta)-collapsed if its per-example KL to the prior is below epsilon for at least a 1 - delta fraction of the data (delta fixed at 0.01).([Section 6.2, p.8](https://arxiv.org/pdf/1911.02469v1#page=8 "Despite the large volume of work studying posterior collapse it has not been measured in a consistent way (or even deﬁned so)."))
- **c6** Deep nonlinear VAEs (MNIST, CelebA, Gaussian observation model): many public implementations fix sigma^2 = 1, which the linear analysis suggests is suboptimal; with large initial sigma^2 the variational distribution matched the prior closely even when sigma^2 was learned, suggesting that local optima may contribute to posterior collapse in deep VAEs.([Section 6.2, p.8](https://arxiv.org/pdf/1911.02469v1#page=8 "This was true even when σ2 is learned — suggesting that local optima may contribute to posterior collapse in deep VAEs."))
- **c7** The gap between different sigma^2 initializations when sigma^2 is learned is not predicted by the linear VAE, which the authors take to suggest that learning sigma^2 correctly is more challenging in the nonlinear case.([Section 6.2, p.8](https://arxiv.org/pdf/1911.02469v1#page=8 "The linear VAE does not predict this gap which suggests that learning σ2 correctly is more challenging in the nonlinear case."))

