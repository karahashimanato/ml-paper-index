<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# From Variational to Deterministic Autoencoders

- カード: [`arxiv-1903.12436`](../../papers/arxiv-1903.12436.yaml)
- 著者: Partha Ghosh, Mehdi S. M. Sajjadi, Antonio Vergari, Michael Black, Bernhard Schölkopf
- 年・掲載: 2019 ICLR 2020
- 原論文: [PDF](https://arxiv.org/pdf/1903.12436v4)(arXiv v4、カード作成時に読んだ版)
- タグ: autoencoders, generative-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Citing several works, the authors state that even after convergence the learned aggregated posterior of a VAE rarely matches the assumed prior, which hurts the quality of generated samples.([Introduction, p.2](https://arxiv.org/pdf/1903.12436v4#page=2 "Lastly, even after a satisfactory convergence of the objective, the learned aggregated posterior distribution rarely matches the assumed latent prior in practice (Kingma et al., 2016; Bauer & Mnih, 2019; Dai & Wipf, 2019), ultimately hurting the quality of generated samples."))
- **c2** Key observation: with the common Gaussian assumptions and a 1-sample estimate, a VAE can be viewed as a deterministic autoencoder whose decoder input is perturbed with Gaussian noise; the authors argue this noise injection is a key factor in regularizing the decoder.([Deterministic regularized autoencoders, p.4](https://arxiv.org/pdf/1903.12436v4#page=4 "In this light, a VAE can be seen as a deterministic autoencoder where (Gaussian) noise is added to the decoder’s input."))
- **c3** Proposal: replace noise injection with explicit decoder regularization, giving a deterministic Regularized Autoencoder; without the KL term there is no fixed prior, so a generative mechanism must be regained separately.([Deterministic regularized autoencoders, p.4](https://arxiv.org/pdf/1903.12436v4#page=4 "We propose to substitute noise injection with an explicit regularization scheme for the decoder."))
- **c4** Ex-post density estimation (fitting a density to the latent codes after training) is proposed for RAEs and, according to the authors, can be applied to any VAE or WAE as a remedy for aggregated-posterior mismatch without adding cost to training.([Ex-post density estimation, p.5](https://arxiv.org/pdf/1903.12436v4#page=5 "This simple approach not only ﬁts our RAE framework well, but it can also be readily adopted for any VAE or variants thereof such as the WAE as a practical remedy to the aggregated posterior mismatch without adding any computational overhead to the costly training phase."))
- **c5** Citing earlier work, the authors note that generative use of denoising and contractive autoencoders via MCMC was hard to diagnose for convergence, required considerable tuning and did not scale beyond MNIST, so they were superseded by VAEs.([Related works, p.6](https://arxiv.org/pdf/1903.12436v4#page=6 "However, they are hard to diagnose for convergence, require a considerable effort in tuning (Cowles & Carlin, 1996), and have not scaled beyond MNIST, leading to them being superseded by VAEs."))
- **c6** Evaluation protocol: VAE, constant-variance VAE, WAE (MMD) and 2-stage VAE baselines and RAE variants use the same network architecture on MNIST, CIFAR-10 and CelebA; quality is measured with FID on reconstructions, random samples and interpolations (precision/recall in an appendix).([RAEs for image modeling, p.7](https://arxiv.org/pdf/1903.12436v4#page=7 "For a fair comparison, we use the same network architecture for all models."))
- **c7** Tuning caveat: when comparing their best FIDs with a large-scale VAE study, the authors note a slightly different architecture and that their models underwent only modest fine-tuning rather than an extensive hyperparameter search.([RAEs for image modeling, p.8](https://arxiv.org/pdf/1903.12436v4#page=8 "While we are employing a slightly different architecture than theirs, our models underwent only modest ﬁnetuning instead of an extensive hyperparameter search."))
- **c8** No clear winner among the decoder regularizers (gradient penalty, L2, spectral normalization), and even an autoencoder without explicit regularization obtained strong FIDs when the latent density was fitted with a GMM, which the authors relate to neural networks being surprisingly smooth by design.([RAEs for image modeling, p.8](https://arxiv.org/pdf/1903.12436v4#page=8 "Surprisingly, the implicitly regularized RAE and AE models are shown to be able to score impressive FIDs when qδ(z) is ﬁt through GMMs."))
- **c9** Ex-post density estimation consistently improved sample quality across all settings and models in Table 1, including the VAE and WAE baselines.([RAEs for image modeling, p.8](https://arxiv.org/pdf/1903.12436v4#page=8 "In Table 1, ex-post density estimation consistently improves sample quality across all settings and models."))

