<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# NVAE: A Deep Hierarchical Variational Autoencoder

- カード: [`arxiv-2007.03898`](../../papers/arxiv-2007.03898.yaml)
- 著者: Arash Vahdat, Jan Kautz
- 年・掲載: 2020 NeurIPS 2020
- 原論文: [PDF](https://arxiv.org/pdf/2007.03898v3)(arXiv v3、カード作成時に読んだ版)
- タグ: generative-modeling, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Positioning: VAEs offer fast sampling and easy-to-access encoders but are currently outperformed by normalizing flows and autoregressive models; most VAE research focuses on statistical challenges, while this paper focuses on neural architecture design for hierarchical VAEs.([Abstract, p.1](https://arxiv.org/pdf/2007.03898v3#page=1 "However, they are currently outperformed by other models such as normalizing ﬂows and autoregressive models."))
- **c2** Training instability: due to the unbounded KL term, training very deep hierarchical VAEs is often unstable; the authors observe that instability remains a major roadblock as the number of hierarchical groups increases, independent of batch normalization.([Introduction, p.2](https://arxiv.org/pdf/2007.03898v3#page=2 "We also observe that instability of training remains a major roadblock when the number of hierarchical groups is increased, independent of the presence of BN."))
- **c3** Batch normalization: earlier state-of-the-art VAEs omitted BN; the authors observed that BN's negative impact occurs during evaluation (running statistics shift the outputs), and address it by adjusting the BN momentum and regularizing the norm of BN scaling parameters.([Section 3.1, p.4](https://arxiv.org/pdf/2007.03898v3#page=4 "In our early experiments, we observed that the negative impact of BN is during evaluation, not training."))
- **c4** Spectral regularization: residual Normal distributions alone do not stabilize training because the KL is still unbounded; the authors add a penalty on the largest singular value of each layer to keep encoder outputs bounded.([Section 3.2, p.5](https://arxiv.org/pdf/2007.03898v3#page=5 "The residual Normal distributions do not sufﬁce for stabilizing VAE training as KL in Eq. 2 is still unbounded."))
- **c5** Architecture over statistics: NVAE's performance is only slightly improved by adding normalizing flows in the encoder, which the authors take to indicate that network architecture is an important component of VAEs.([Section 4.1, p.6](https://arxiv.org/pdf/2007.03898v3#page=6 "This indicates that the network architecture is an important component in VAEs and a carefully designed network with Normal distributions in encoder can compensate for some of the statistical challenges."))
- **c6** Sampling protocol for the shown images: samples are drawn with a reduced prior temperature (which often improves quality but reduces diversity), and BN statistics are readjusted by sampling 500 times at that temperature; the quantitative evaluation uses the default BN setting.([Section 4.2, p.7](https://arxiv.org/pdf/2007.03898v3#page=7 "This is done by scaling down the standard deviation of the Normal distributions in each conditional in the prior, and it often improves the quality of the samples, but it also reduces their diversity."))
- **c7** Comparison with VQ-VAE-2 (Related Work): although VQ-VAE is motivated by VAEs, its objective does not correspond to a lower bound on the data log-likelihood, whereas NVAE is trained directly with the VAE objective.([Introduction (Related Work), p.2](https://arxiv.org/pdf/2007.03898v3#page=2 "Although VQ-VAE’s formulation is motivated by VAEs, its objective does not correspond to a lower bound on data log-likelihood."))

