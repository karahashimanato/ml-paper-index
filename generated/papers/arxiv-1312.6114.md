<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Auto-Encoding Variational Bayes

- カード: [`arxiv-1312.6114`](../../papers/arxiv-1312.6114.yaml)
- 著者: Diederik P Kingma, Max Welling
- 年・掲載: 2013
- 原論文: [PDF](https://arxiv.org/pdf/1312.6114v11)(arXiv v11、カード作成時に読んだ版)
- タグ: generative-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: reparameterizing the variational lower bound gives a lower-bound estimator that can be optimized with standard stochastic gradient methods; for i.i.d. data with continuous per-datapoint latent variables, an approximate inference (recognition) model is fitted to the intractable posterior with this estimator.([Abstract, p.1](https://arxiv.org/pdf/1312.6114v11#page=1 "First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly optimized using standard stochastic gradient methods."))
- **c2** Link to autoencoders: in the objective, the KL divergence of the approximate posterior from the prior acts as a regularizer and the second term is an expected negative reconstruction error.([Section 2.3, p.4](https://arxiv.org/pdf/1312.6114v11#page=4 "The ﬁrst term is (the KL divergence of the approximate posterior from the prior) acts as a regularizer, while the second term is a an expected negative reconstruction error."))
- **c3** Citing Bengio, Courville & Vincent [BCV13], the authors note that the reconstruction criterion alone is known not to be sufficient for learning useful representations, which motivated denoising, contractive and sparse autoencoder variants.([Related work, p.6](https://arxiv.org/pdf/1312.6114v11#page=6 "However, it is well known that this reconstruction criterion is in itself not sufﬁcient for learning useful representations [BCV13]."))
- **c4** In contrast to those regularized autoencoders, the regularization term in the SGVB objective is dictated by the variational bound, without the usual regularization hyperparameter.([Related work, p.6](https://arxiv.org/pdf/1312.6114v11#page=6 "The SGVB objective contains a regularization term dictated by the variational bound (e.g. eq. (10)), lacking the usual nuisance regularization hyperparameter required to learn useful representations."))
- **c5** The diagonal-Gaussian approximate posterior used in the VAE example is described as a simplifying choice, not a limitation of the method.([Example: Variational Auto-Encoder (footnote 2), p.5](https://arxiv.org/pdf/1312.6114v11#page=5 "Note that this is just a (simplifying) choice, and not a limitation of our method."))
- **c6** Evaluation setup: generative models of MNIST and Frey Face images are compared on the variational lower bound and on an estimated marginal likelihood, against the wake-sleep algorithm (same encoder) and, for marginal likelihood, Monte Carlo EM; the Adagrad step size was chosen from three values based on training-set performance in the first few iterations.([Experiments, p.7](https://arxiv.org/pdf/1312.6114v11#page=7 "the Adagrad global stepsize parameters were chosen from {0.01, 0.02, 0.1} based on performance on the training set in the ﬁrst few iterations."))
- **c7** The authors state (Figure 2 caption) that AEVB converged considerably faster than wake-sleep and reached a better lower bound in all experiments; the comparison is shown only as a figure.([Figure 2, p.7](https://arxiv.org/pdf/1312.6114v11#page=7 "Our method converged considerably faster and reached a better solution in all experiments."))
- **c8** Adding superfluous latent variables did not cause overfitting in these experiments, which the authors attribute to the regularizing nature of the variational bound.([Experiments, p.7](https://arxiv.org/pdf/1312.6114v11#page=7 "Interestingly, superﬂuous latent variables did not result in overﬁtting, which is explained by the regularizing nature of the variational bound."))
- **c9** Limitation of the evaluation: the marginal likelihood could only be estimated (by MCMC) for a 3-dimensional latent space, because for higher-dimensional latent spaces the estimates became unreliable.([Experiments, p.7](https://arxiv.org/pdf/1312.6114v11#page=7 "for higher dimensional latent space the estimates became unreliable."))

