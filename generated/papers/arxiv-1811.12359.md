<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations

- カード: [`arxiv-1811.12359`](../../papers/arxiv-1811.12359.yaml)
- 著者: Francesco Locatello, Stefan Bauer, Mario Lucic, Gunnar Rätsch, Sylvain Gelly, Bernhard Schölkopf, Olivier Bachem
- 年・掲載: 2018 ICML 2019
- 原論文: [PDF](https://arxiv.org/pdf/1811.12359v4)(arXiv v4、カード作成時に読んだ版)
- タグ: representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Theoretical result: unsupervised learning of disentangled representations is fundamentally impossible without inductive biases on both the models and the data (for factorized priors, there are infinitely many completely entangled bijections of z with the same marginal distribution, so observations alone cannot distinguish them).([Abstract, p.1](https://arxiv.org/pdf/1811.12359v4#page=1 "We ﬁrst theoretically show that the unsupervised learning of disentangled representations is fundamentally impossible without inductive biases on both the models and the data."))
- **c2** Study design: six methods (beta-VAE, AnnealedVAE, FactorVAE, beta-TCVAE, DIP-VAE-I, DIP-VAE-II) with the same convolutional architecture, optimizer, batch size, Gaussian encoder, Bernoulli decoder and 10 latent dimensions; six regularization strengths per method chosen a priori (partly from ranges in the literature); 50 random seeds per setting; more than 12 000 models on seven datasets.([Section 4, p.4](https://arxiv.org/pdf/1811.12359v4#page=4 "We ﬁx our experimental setup in advance and we run all the considered methods on each data set for 50 different random seeds and evaluate them on the considered metrics."))
- **c3** The methods are effective at making the dimensions of the sampled aggregated posterior uncorrelated, but this does not seem to make the dimensions of the mean representation (the one usually used) uncorrelated; the total correlation of the mean representation generally increases with regularization strength (DIP-VAE-I is an exception).([Section 5.1, p.5](https://arxiv.org/pdf/1811.12359v4#page=5 "this does not seem to imply that the dimensions of the mean representation (usually used for representation) are uncorrelated."))
- **c4** Across methods, the attainable disentanglement scores overlap heavily; the authors (qualitatively) conclude that hyperparameters and random seeds seem substantially more important than the choice of objective, and that a good run with a bad hyperparameter can beat a bad run with a good one. They note that the fixed hyperparameter grid means specific models might have done better with other values.([Section 5.3, p.5](https://arxiv.org/pdf/1811.12359v4#page=5 "the choice of hyperparameters and the random seed seems to be substantially more important than the choice of objective function."))
- **c5** Model selection: unsupervised scores (reconstruction error, KL, ELBO, estimated total correlation) showed no clear pattern of correlation with the disentanglement metrics, so the authors consider selecting models with them unlikely to succeed in practice.([Section 5.4, p.7](https://arxiv.org/pdf/1811.12359v4#page=7 "While we do observe some correlations, no clear pattern emerges which leads us to conclude that this approach is unlikely to be successful in practice."))
- **c6** Transferring good hyperparameters across datasets or metrics does not allow distinguishing good from bad random seeds on the target task; the authors conclude that unsupervised model selection remains unsolved.([Section 5.4, p.7](https://arxiv.org/pdf/1811.12359v4#page=7 "Unsupervised model selection remains an unsolved problem."))
- **c7** Downstream usefulness: on the simplest downstream task (predicting the true factors with logistic regression or gradient boosted trees), higher disentanglement scores did not reliably lead to higher sample efficiency.([Section 5.5, p.7](https://arxiv.org/pdf/1811.12359v4#page=7 "We do not observe that higher disentanglement scores reliably lead to a higher sample efﬁciency."))
- **c8** Cost of the study: reproducing the experiments requires approximately 2.52 GPU years (NVIDIA P100); the authors release more than 10 000 trained models.([Section 1 (footnote 1), p.2](https://arxiv.org/pdf/1811.12359v4#page=2 "Reproducing these experiments requires approximately 2.52 GPU years (NVIDIA P100)."))

