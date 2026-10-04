<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Understanding disentangling in β-VAE

- カード: [`arxiv-1804.03599`](../../papers/arxiv-1804.03599.yaml)
- 著者: Christopher P. Burgess, Irina Higgins, Arka Pal, Loic Matthey, Nick Watters, Guillaume Desjardins, Alexander Lerchner
- 年・掲載: 2018 NIPS 2017 Workshop on Learning Disentangled Representations
- 原論文: [PDF](https://arxiv.org/pdf/1804.03599v1)(arXiv v1、カード作成時に読んだ版)
- タグ: representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Citing the original beta-VAE paper [15], the authors state that the higher beta values needed for disentangling often trade reconstruction fidelity against how disentangled the latent code is, due to information lost through the restricted-capacity bottleneck.([β-VAE, p.3](https://arxiv.org/pdf/1804.03599v1#page=3 "Higher values of β necessary to encourage disentangling often lead to a trade-off between the ﬁdelity of β-VAE reconstructions and the disentangled nature of its latent code z (see Fig. 6 in [15])."))
- **c2** Information-theoretic view: treating each latent unit of the diagonal-Gaussian posterior as an additive white Gaussian noise channel, the KL term can be seen as an upper bound on the information transmitted through the latent channels per data sample.([β-VAE through the information bottleneck perspective, p.3](https://arxiv.org/pdf/1804.03599v1#page=3 "can be seen as an upper bound on the amount of information that can be transmitted through the latent channels per data sample"))
- **c3** Key hypothesis: beta-VAE finds latent components that make different contributions to the log-likelihood term, and the diagonal posterior covariance pushes these components into separate latent dimensions, which may align them with the generative factors.([β-VAE aligns latent dimensions with components that make different contributions to reconstruction, p.4](https://arxiv.org/pdf/1804.03599v1#page=4 "Our key hypothesis is that β-VAE ﬁnds latent components which make different contributions to the log-likelihood term of the cost function (Eq. 5)."))
- **c4** Illustration on a dataset with two factors (x and y position of a Gaussian blob): the standard VAE (beta = 1) spread the two factors across four latent dimensions with representational discontinuities, while beta-VAE (beta = 150) represented them in two.([Comparing disentangling in β-VAE and VAE, p.4](https://arxiv.org/pdf/1804.03599v1#page=4 "The standard VAE learns to represent these two factors across four latent dimensions, whereas β-VAE represents them in two."))
- **c5** Proposed modification: the objective penalizes the absolute deviation of the KL from a target capacity C, and C is gradually increased from zero to a value large enough for good reconstructions.([Improving disentangling in β-VAE with controlled capacity increase, p.7](https://arxiv.org/pdf/1804.03599v1#page=7 "Similar to the generator model, C is gradually increased from zero to a value large enough to produce good quality reconstructions (see Sec. A.2 for more details)."))
- **c6** Evaluation is qualitative: results on coloured dSprites and 3D Chairs are shown as latent traversals and reconstructions judged by eye; no quantitative disentanglement metric was found in the text (searched for 'metric' and 'quantitative').([Improving disentangling in β-VAE with controlled capacity increase, p.8](https://arxiv.org/pdf/1804.03599v1#page=8 "Furthermore, the quality of the traversal images are high, and by eye, the model reconstructions (second row) are quite difﬁcult to distinguish from the corresponding data samples used to generate them (top row)."))
- **c7** On 3D Chairs, the authors note that it is unclear what the disentangled axes should correspond to.([Improving disentangling in β-VAE with controlled capacity increase, p.8](https://arxiv.org/pdf/1804.03599v1#page=8 "With this richer dataset it is unclear exactly what the disentangled axes should correspond to"))

