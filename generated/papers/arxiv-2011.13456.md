<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Score-Based Generative Modeling through Stochastic Differential Equations

- カード: [`arxiv-2011.13456`](../../papers/arxiv-2011.13456.yaml)
- 著者: Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, Ben Poole
- 年・掲載: 2020 ICLR 2021
- 原論文: [PDF](https://arxiv.org/pdf/2011.13456v2)(arXiv v2、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Key idea: a forward SDE slowly injects noise to turn data into a known prior, and the corresponding reverse-time SDE depends only on the time-dependent score of the perturbed data distribution, which is estimated with neural networks and then integrated with numerical SDE solvers.([Abstract, p.1](https://arxiv.org/pdf/2011.13456v2#page=1 "Crucially, the reverse-time SDE depends only on the time-dependent gradient ﬁeld (a.k.a., score) of the perturbed data distribution."))
- **c2** The authors group SMLD (Song & Ermon, 2019) and DDPM (Sohl-Dickstein et al., 2015; Ho et al., 2020) together as score-based generative models because, for continuous state spaces, the DDPM objective implicitly computes scores at each noise scale.([Introduction, p.1](https://arxiv.org/pdf/2011.13456v2#page=1 "For continuous state spaces, the DDPM training objective implicitly computes scores at each noise scale."))
- **c3** Unification: in the limit of infinitely many noise scales, the SMLD perturbations become the Variance Exploding (VE) SDE and the DDPM perturbations the Variance Preserving (VP) SDE; DDPM ancestral sampling corresponds to one particular discretization of the reverse-time VP SDE.([Section 3.4, p.5](https://arxiv.org/pdf/2011.13456v2#page=5 "Therefore, the noise perturbations used in SMLD and DDPM correspond to discretizations of SDEs Eqs. (9) and (11)."))
- **c4** Predictor-Corrector sampling on CIFAR-10: adding one corrector (score-based MCMC) step per predictor step doubles computation but always improved sample quality over predictor-only sampling with the same number of steps, and was typically better than doubling the predictor steps; corrector-only sampling was worse at equal computation.([Predictor-corrector samplers, p.6](https://arxiv.org/pdf/2011.13456v2#page=6 "For all predictors, adding one corrector step for each predictor step (PC1000) doubles computation but always improves sample quality (against P1000)."))
- **c5** Probability flow ODE and likelihood protocol: the deterministic ODE sharing the SDE's marginals allows exact likelihood computation; NLLs are computed on uniformly dequantized CIFAR-10 and compared only with models evaluated the same way, except DDPM whose ELBO values on discrete data are included.([Section 4.3, p.7](https://arxiv.org/pdf/2011.13456v2#page=7 "We compute log-likelihoods on uniformly dequantized data, and only compare to models evaluated in the same way (omitting models evaluated with variational dequantization (Ho et al., 2019) or discrete data)"))
- **c6** Trade-off: VE SDEs typically gave better sample quality than VP/sub-VP SDEs but empirically worse likelihoods, which the authors take to indicate practitioners likely need to experiment with different SDEs for different domains and architectures.([Section 4.4, p.8](https://arxiv.org/pdf/2011.13456v2#page=8 "As shown in Table 3, VE SDEs typically provide better sample quality than VP/sub-VP SDEs, but we also empirically observe that their likelihoods are worse than VP/sub-VP SDE counterparts."))
- **c7** Evaluation protocol: Table 3 (sample quality) reports the checkpoint with the smallest FID over training, sampled with PC samplers, whereas Table 2 reports the last checkpoint with black-box ODE solvers; FIDs use 50k samples, and the PC samplers' signal-to-noise ratio was grid-searched on CIFAR-10 (Appendix G).([Section 4.4, p.8](https://arxiv.org/pdf/2011.13456v2#page=8 "Results reported in Table 3 are for the checkpoint with the smallest FID over the course of training, where samples are generated with PC samplers."))
- **c8** Stated limitations: the proposed samplers remain slower than GANs on the same datasets, and the range of possible samplers introduces many hyperparameters that future work should select and tune automatically.([Conclusion, p.9](https://arxiv.org/pdf/2011.13456v2#page=9 "While our proposed sampling approaches improve results and enable more efﬁcient sampling, they remain slower at sampling than GANs (Goodfellow et al., 2014) on the same datasets."))

