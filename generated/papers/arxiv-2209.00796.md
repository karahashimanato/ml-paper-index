<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Diffusion Models: A Comprehensive Survey of Methods and Applications

- カード: [`arxiv-2209.00796`](../../papers/arxiv-2209.00796.yaml)
- 著者: Ling Yang, Zhilong Zhang, Yang Song, Shenda Hong, Runsheng Xu, Yue Zhao, Wentao Zhang, Bin Cui, Ming-Hsuan Yang
- 年・掲載: 2022 ACM Computing Surveys
- 原論文: [PDF](https://arxiv.org/pdf/2209.00796v15)(arXiv v15、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Taxonomy: research on diffusion models is categorized into efficient sampling (Section 3), improved likelihood estimation (Section 4) and handling data with special structures (Section 5), with connections to other generative models in Section 6.([Introduction, p.5](https://arxiv.org/pdf/2209.00796v15#page=5 "categorizing it into three key areas: efficient sampling (Section 3), improved likelihood estimation (Section 4), and methods for handling data with special structures (Section 5)"))
- **c2** Improved likelihood: the training objective is a variational lower bound that, citing VDM [155], may not be tight in many cases, leading to potentially suboptimal log-likelihoods; the survey covers noise schedule optimization, reverse variance learning and exact log-likelihood evaluation.([Diffusion Models with Improved Likelihood, p.14](https://arxiv.org/pdf/2209.00796v15#page=14 "This bound, however, may not be tight in many cases [155], leading to potentially suboptimal log-likelihoods from diffusion models."))
- **c3** Summary of VDM: noise schedules do not affect the VLB as long as they share the same endpoint SNR values, and only affect the variance of Monte Carlo estimators of the VLB.([Noise Schedule Optimization, p.15](https://arxiv.org/pdf/2209.00796v15#page=15 "As a result, noise schedules do not affect the VLB as long as they share the same values at Rmin and Rmax, and will only affect the variance of Monte Carlo estimators for VLB."))
- **c4** Summary of reverse variance learning: classical diffusion models fix the reverse-kernel variance, and many methods train it to further maximize the VLB and log-likelihood (iDDPM's interpolation with a hybrid objective; Analytic-DPM's optimal variance from a pre-trained score model).([Reverse Variance Learning, p.15](https://arxiv.org/pdf/2209.00796v15#page=15 "Many methods propose to train the reverse variances as well to further maximize VLB and log-likelihood values."))
- **c5** Exact likelihood: the probability-flow-ODE likelihood can be computed accurately but cannot be directly optimized because it requires an expensive ODE solve per data point; Song et al. (2021) maximize the SDE variational bound as a proxy (ScoreFlows).([Exact Likelihood Computation, p.16](https://arxiv.org/pdf/2209.00796v15#page=16 "Unfortunately, this formula cannot be directly optimized to maximize 𝑝ode 𝜃 on data, as it requires calling expensive ODE solvers for each data point x0."))
- **c6** VAE connection: DDPM can be conceptualized as a hierarchical Markovian VAE with a fixed encoder (the linear Gaussian forward process), a decoder shared across decoding steps, and latents of the same size as the data.([Variational Autoencoders and Connections with Diffusion Models, p.21](https://arxiv.org/pdf/2209.00796v15#page=21 "The DDPM can be conceptualized as a hierarchical Markovian VAE with a fixed encoder."))
- **c7** Future directions: the assumption that the forward process completely erases information may not always hold, since complete removal is unachievable in finite time; when to halt the forward process to balance sampling efficiency and sample quality is open.([Future Directions, p.44](https://arxiv.org/pdf/2209.00796v15#page=44 "In reality, complete removal of information is unachievable in finite time."))
- **c8** Future directions: diffusion models are less effective than VAEs or GANs at providing good latent representations, and because the latent space often has the data's dimensionality, sampling efficiency suffers and the models may not learn representation schemes well.([Future Directions, p.44](https://arxiv.org/pdf/2209.00796v15#page=44 "Unlike variational autoencoders or generative adversarial networks, diffusion models are less effective for providing good representations of data in their latent space."))

