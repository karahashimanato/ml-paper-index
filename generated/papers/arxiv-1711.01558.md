<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Wasserstein Auto-Encoders

- カード: [`arxiv-1711.01558`](../../papers/arxiv-1711.01558.yaml)
- 著者: Ilya Tolstikhin, Olivier Bousquet, Sylvain Gelly, Bernhard Schölkopf
- 年・掲載: 2017 ICLR 2018
- 原論文: [PDF](https://arxiv.org/pdf/1711.01558v4)(arXiv v4、カード作成時に読んだ版)
- タグ: autoencoders, generative-modeling, representation-learning, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main idea: WAE minimizes a penalized form of the Wasserstein distance between the model and data distributions, which yields a regularizer different from the VAE's; this regularizer encourages the encoded training distribution to match the prior.([Abstract, p.1](https://arxiv.org/pdf/1711.01558v4#page=1 "This regularizer encourages the encoded training distribution to match the prior."))
- **c2** Objective: for a deterministic decoder, the optimal-transport cost can be written as an optimization over probabilistic encoders whose aggregate Q_Z equals the prior (Theorem 1, from earlier work [4]); relaxing this constraint with a penalty lambda * D_Z(Q_Z, P_Z) gives the WAE objective, which, unlike the VAE, allows deterministic encoders.([Proposed method, p.4](https://arxiv.org/pdf/1711.01558v4#page=4 "Note that as opposed to VAEs, the WAE formulation allows for non-random encoders deterministically mapping inputs to their latent codes."))
- **c3** Difference from the VAE regularizer: citing [13], the VAE regularizer equals KL(Q_Z, P_Z) plus the mutual information between X and Z, and WAE simply drops the mutual-information term.([Related work, p.6](https://arxiv.org/pdf/1711.01558v4#page=6 "WAEs simply drop the mutual information term IQ(X, Z) in the VAE regularizer."))
- **c4** Relation to AAE: with squared cost, WAE-GAN is equivalent to adversarial autoencoders, so the theory of [4] suggests AAEs minimize the 2-Wasserstein distance between data and model; WAE generalizes AAE to any input-space cost and any latent discrepancy (e.g. MMD).([Related work, p.6](https://arxiv.org/pdf/1711.01558v4#page=6 "This provides the ﬁrst theoretical justiﬁcation for AAEs known to the authors."))
- **c5** Stability: in some cases WAE-GAN seems to give better matching and better samples than WAE-MMD, but because of adversarial training it is less stable than WAE-MMD, whose training is very stable much like the VAE.([Experiments, p.10](https://arxiv.org/pdf/1711.01558v4#page=10 "However, due to adversarial training WAE-GAN is less stable than WAE-MMD, which has a very stable training much like VAE."))
- **c6** Sample quality depends on how accurately Q_Z matches P_Z, because the decoder is trained only on encoded data points; the authors noticed that even slight differences between Q_Z and P_Z may affect sample quality.([Experiments, p.10](https://arxiv.org/pdf/1711.01558v4#page=10 "In our experiments we noticed that even slight diﬀerences between QZ and PZ may aﬀect the quality of samples."))
- **c7** Experimental setup (MNIST and CelebA): deterministic encoder-decoder pairs, isotropic Gaussian prior, squared cost, DCGAN-like architectures; the regularization weight was set by trying various values, and lambda = 10 seemed to work well across datasets.([Experiments, p.8](https://arxiv.org/pdf/1711.01558v4#page=8 "We tried various values of λ and noticed that λ = 10 seems to work good across all datasets we considered."))
- **c8** Larger-scale comparison (bigVAE/bigWAE in Table 1): over 3,000 WAE-GAN, WAE-MMD and VAE models with randomly sampled hyperparameters (latent dimension, batch size, learning rates, lambda or the VAE decoder variance, DCGAN-style or ResNet50-v2 architectures), with each algorithm given exactly the same computational budget and three random seeds per configuration.([Supplementary D, p.19](https://arxiv.org/pdf/1711.01558v4#page=19 "In total we trained over 3 thousand WAE-GAN, WAE-MMD, and VAE models with various hyperparameters while making sure each one of the three algorithms gets exactly the same computational budget."))

