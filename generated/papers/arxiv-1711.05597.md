<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Advances in Variational Inference

- カード: [`arxiv-1711.05597`](../../papers/arxiv-1711.05597.yaml)
- 著者: Cheng Zhang, Judith Butepage, Hedvig Kjellstrom, Stephan Mandt
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1711.05597v3)(arXiv v3、カード作成時に読んだ版)
- タグ: bayesian-deep-learning, posterior-inference, variational-autoencoders, variational-inference
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Positioning VI against MCMC: MCMC is often unbiased by construction and converges to the true posterior in the limit but can be slow to converge; optimization-based methods (VI, loopy BP, EP) are often faster but may suffer from oversimplified posterior approximations (citing Bishop and Wainwright & Jordan).([Section 1 (Introduction), p.1](https://arxiv.org/pdf/1711.05597v3#page=1 "Optimization-based methods, on the other hand, are often faster but may suffer from oversimpliﬁed posterior approximations [14], [205]."))
- **c2** Limitations of mean-field VI: it explicitly ignores correlations between variables; citing Wainwright & Jordan [205], the more dependencies are broken by the variational distribution, the more non-convex the optimization becomes, while more structure removes certain local optima.([Section 5.1, p.10](https://arxiv.org/pdf/1711.05597v3#page=10 "The main limitation of mean ﬁeld approximations is that they explicitly ignore correlations between different variables e.g., between the spins in the Ising model."))
- **c3** Shortcomings of KL(q||p) VI listed by the authors with citations: underestimating posterior variances [128], in some cases inability to break symmetry when multiple modes are close [141], and being a comparably loose bound [221]; these motivate alternative divergence measures.([Section 5.2, p.10](https://arxiv.org/pdf/1711.05597v3#page=10 "In other cases, it is unable to break symmetry when multiple modes are close [141], and is a comparably loose bound [221]."))
- **c4** With Renyi's alpha-divergence, a smaller alpha leads to more mass-covering behaviour and a larger alpha to zero-forcing behaviour (the approximation avoids areas of low posterior probability); alpha -> 1 recovers standard KL-based VI.([Section 5.2, p.10](https://arxiv.org/pdf/1711.05597v3#page=10 "a smaller α leads to more mass-covering effects, while a larger α results in zero-forcing effects"))
- **c5** Black-box VI writes the ELBO gradient as an expectation under q of the score function times (log p(x,z) - log q(z)), estimated by sampling from q, so only the joint needs to be specified. A direct implementation suffers from high gradient variance; the authors attribute much of BBVI's success to Rao-Blackwellization and control variates (citing Ranganath et al. [154]).([Section 4.2, p.8](https://arxiv.org/pdf/1711.05597v3#page=8 "A direct implementation of stochastic gradient ascent based on Eq. 14 suffers from high variances of the estimated gradients."))
- **c6** Reparameterization gradients are empirically often lower-variance than score-function gradients, but a theoretical analysis (cited) shows this is not guaranteed; the trick does not trivially extend to many distributions, in particular discrete ones, which require further approximations (e.g. Gumbel-softmax relaxations with a temperature).([Section 4.3, p.9](https://arxiv.org/pdf/1711.05597v3#page=9 "While the variance of this estimator (Eq. 16) is often lower than the variance of the score function gradient (Eq. 14), a theoretical analysis shows that this is not guaranteed, see Chapter 3 in [48]."))
- **c7** Open question on theory: few authors address theoretical aspects of VI; quantifying the approximation error of replacing the posterior by a variational distribution, and the related predictive error, are named as important directions.([Section 7 (Discussion), p.16](https://arxiv.org/pdf/1711.05597v3#page=16 "Despite progress in modeling and inference, few authors address theoretical aspects of VI [95], [133], [213]."))
- **c8** Automatic VI in probabilistic programming (Stan, Infer.Net, Edward, etc.) is still not straightforward for non-experts: e.g. Infer.Net requires manually identifying and breaking posterior symmetries, and control variates need model-specific design for best performance; the authors state these problems were not yet addressed in toolboxes at the time of writing.([Section 7 (Discussion), p.17](https://arxiv.org/pdf/1711.05597v3#page=17 "Despite current efforts to make VI more accessible to practitioners, its usage is still not straightforward for non-experts."))

