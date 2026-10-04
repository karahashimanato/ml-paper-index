<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Variational Diffusion Models

- カード: [`arxiv-2107.00630`](../../papers/arxiv-2107.00630.yaml)
- 著者: Diederik P. Kingma, Tim Salimans, Ben Poole, Jonathan Ho
- 年・掲載: 2021 NeurIPS 2021
- 原論文: [PDF](https://arxiv.org/pdf/2107.00630v6)(arXiv v6、カード作成時に読んだ版)
- タグ: diffusion-models, generative-modeling, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Framing: diffusion probabilistic models can be viewed as a type of VAE whose structure and loss allow efficient training of arbitrarily deep models; optimizing the diffusion process jointly with the rest of the model turns it into a type of VAE.([Related work, p.2](https://arxiv.org/pdf/2107.00630v6#page=2 "DPMs can be viewed as a type of variational autoencoder (VAE) [Kingma and Welling, 2013, Rezende et al., 2014], whose structure and loss function allows for efﬁcient training of arbitrarily deep models."))
- **c2** Theory: in continuous time, the diffusion loss depends on alpha(t) and sigma(t) only through SNR at the endpoints t = 0 and t = 1; given SNR_min and SNR_max, the VLB is invariant to the shape of SNR(t) in between, and diffusion specifications satisfying the paper's mild constraints (including variance-exploding and variance-preserving) can be seen as equivalent in continuous time.([Equivalence of diffusion models in continuous time, p.6](https://arxiv.org/pdf/2107.00630v6#page=6 "The VLB is thus only impacted by the function SNR(t) through its endpoints SNRmin and SNRmax."))
- **c3** Discrete vs continuous time: if the denoising model is sufficiently good, doubling the number of timesteps (with a fixed SNR function) lowers the diffusion loss, i.e. more timesteps give a better VLB; this motivates the continuous-time (T -> infinity) model.([More steps leads to a lower loss, p.5](https://arxiv.org/pdf/2107.00630v6#page=5 "We then ﬁnd that if our trained denoising model ˆxθ is sufﬁciently good, we have that L2T (x) < LT (x), i.e. that our VLB will be better for a larger number of timesteps."))
- **c4** Weighted losses (as used for perceptual quality) put more emphasis on noisier data than the VLB and can sometimes improve FID and Inception Score; the models in this paper use w(v) = 1, the unweighted VLB.([Weighted diffusion loss, p.7](https://arxiv.org/pdf/2107.00630v6#page=7 "For the models presented in this paper, we further use w(v) = 1 as corresponding to the (unweighted) VLB."))
- **c5** Likelihood vs sample quality: the CIFAR-10 model, with hyperparameters tuned for likelihood, has FID 7.41, worse than recent diffusion models that target FID; with the weighting of Ho et al. (2020) the FID improves to 4.0. The authors did not tune further for FID.([Likelihood and samples, p.8](https://arxiv.org/pdf/2107.00630v6#page=8 "Our CIFAR-10 model, whose hyper-parameters were tuned for likelihood, results in a FID (perceptual quality) score of 7.41."))
- **c6** Ablation: learning the SNR is necessary to get the most out of Fourier features; with the fixed schedule of Ho et al. (2020) the maximum log-SNR is about 8 and test-set negative likelihood stays above 4 bits per dim, whereas the learned maximum log-SNR ends up at 13.3.([Ablations, p.8](https://arxiv.org/pdf/2107.00630v6#page=8 "In addition, we ﬁnd that learning the SNR is necessary to get the most out of including Fourier features"))
- **c7** The authors hypothesize that DDPM and improved DDPM report better FID and IS than NCSN and this paper because their implied loss weightings emphasize global consistency and coarse patterns more than fine-scale features.([Appendix K, p.21](https://arxiv.org/pdf/2107.00630v6#page=21 "The latter two works report better FID and Inception Score than Song et al. [2020] and the current paper, which we hypothesize is due to their loss emphasizing the global consistence and coarse level patterns more than the ﬁne scale features of the data."))
- **c8** Evaluation protocol: the variational bound is regularly evaluated on the validation set and the models were not found to overfit, so no early stopping is used; CIFAR-10 models are trained for 10 million updates and ImageNet for 2 million before reporting test-set numbers. The reported VDM numbers are variational bounds.([Appendix B.1, p.15](https://arxiv.org/pdf/2107.00630v6#page=15 "We therefore do not use early stopping and instead allow the network to be optimized for 10 million parameter updates for CIFAR-10, and for 2 million updates for ImageNet, before obtaining the test set numbers reported in this paper."))

