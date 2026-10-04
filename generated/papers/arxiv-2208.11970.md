<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Understanding Diffusion Models: A Unified Perspective

- カード: [`arxiv-2208.11970`](../../papers/arxiv-2208.11970.yaml)
- 著者: Calvin Luo
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2208.11970v1)(arXiv v1、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Tutorial framing: a variational diffusion model is presented as a Markovian hierarchical VAE with three restrictions: latent dimension equal to data dimension, a fixed (not learned) linear Gaussian encoder at each timestep, and encoder parameters chosen so the final latent is a standard Gaussian.([Variational Diffusion Models, p.6](https://arxiv.org/pdf/2208.11970v1#page=6 "The easiest way to think of a Variational Diﬀusion Model (VDM) [4, 5, 6] is simply as a Markovian Hierarchical Variational Autoencoder with three key restrictions:"))
- **c2** The ELBO derivations use only the Markov assumption, so they hold for any Markovian HVAE, and with T = 1 both forms reduce exactly to the ELBO of a vanilla VAE.([Variational Diffusion Models, p.10](https://arxiv.org/pdf/2208.11970v1#page=10 "Furthermore, when we set T = 1, both of the ELBO interpretations for a VDM exactly recreate the ELBO equation of a vanilla VAE, as written in Equation 19."))
- **c3** A first ELBO form (consistency terms over two random variables per timestep) may have high-variance Monte Carlo estimates for large T; rewriting encoder transitions via Bayes' rule gives a form where each term is an expectation over at most one random variable, estimable with lower variance.([Variational Diffusion Models, p.9](https://arxiv.org/pdf/2208.11970v1#page=9 "As it is computed by summing up T −1 consistency terms, the ﬁnal estimated value of the ELBO may have high variance for large T values."))
- **c4** Learning the noise schedule: the per-timestep objective can be written in terms of the SNR, which must decrease monotonically, and the SNR can be parameterized by a neural network and learned jointly with the diffusion model.([Learning Diffusion Noise Parameters, p.14](https://arxiv.org/pdf/2208.11970v1#page=14 "Following the simpliﬁcation of the objective in Equation 110, we can directly parameterize the SNR at each timestep using a neural network, and learn it jointly along with the diﬀusion model."))
- **c5** Three equivalent objectives: predicting the original image x0, the source noise, or the score at an arbitrary noise level (the latter via Tweedie's formula). Citing [5, 7] (Ho et al.; Saharia et al.), the tutorial notes that some works found noise prediction to perform better empirically.([Three Equivalent Interpretations, p.17](https://arxiv.org/pdf/2208.11970v1#page=17 "We have therefore derived three equivalent objectives to optimize a VDM: learning a neural network to predict the original image x0, the source noise ϵ0, or the score of the image at an arbitrary noise level ∇log p(xt)."))
- **c6** Score-based link: citing Song and Ermon, vanilla score matching has three problems (ill-defined score on low-dimensional manifolds, inaccurate scores in low-density regions, Langevin dynamics that may not mix), which adding multiple levels of Gaussian noise addresses; the resulting objective almost exactly matches the VDM objective.([Score-based Generative Models, p.19](https://arxiv.org/pdf/2208.11970v1#page=19 "It turns out that these three drawbacks can be simultaneously addressed by adding multiple levels of Gaussian noise to the data."))
- **c7** Stated drawbacks of diffusion models: no interpretable latents (the encoder is a fixed linear Gaussian, so intermediate latents are just noisy versions of the input), latents restricted to the input dimensionality, and expensive sampling because all timesteps must be iterated.([Closing, p.22](https://arxiv.org/pdf/2208.11970v1#page=22 "The VDM does not produce interpretable latents."))
- **c8** The author suggests that the success of diffusion models highlights the power of hierarchical VAEs, and that further gains may be achieved with general deep HVAEs with complex encoders and semantically meaningful latent spaces.([Closing, p.22](https://arxiv.org/pdf/2208.11970v1#page=22 "As a ﬁnal note, the success of diﬀusion models highlights the power of Hierarchical VAEs as a generative model."))

