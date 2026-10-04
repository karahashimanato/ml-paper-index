<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Importance Weighted Autoencoders

- カード: [`arxiv-1509.00519`](../../papers/arxiv-1509.00519.yaml)
- 著者: Yuri Burda, Roger Grosse, Ruslan Salakhutdinov
- 年・掲載: 2015
- 原論文: [PDF](https://arxiv.org/pdf/1509.00519v4)(arXiv v4、カード作成時に読んだ版)
- タグ: generative-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Motivation: VAEs typically assume an approximately factorial posterior whose parameters can be predicted by nonlinear regression; the authors show empirically that the VAE objective can lead to overly simplified representations that do not use the network's full capacity.([Abstract, p.1](https://arxiv.org/pdf/1509.00519v4#page=1 "VAE objective can lead to overly simpliﬁed representations which fail to use the network’s entire modeling capacity."))
- **c2** Theorem 1: the bounds are monotone in the number of samples, log p(x) >= L_{k+1} >= L_k, and if p(h,x)/q(h|x) is bounded, L_k approaches log p(x) as k goes to infinity; k = 1 equals the standard VAE objective.([Importance weighted autoencoder, p.3](https://arxiv.org/pdf/1509.00519v4#page=3 "Observe, however, that the special case of k = 1 is equivalent to the standard VAE objective"))
- **c3** Cost: in the basic implementation the forward and backward passes are done independently for each of the k samples, so the number of operations scales linearly with k.([Training procedure, p.5](https://arxiv.org/pdf/1509.00519v4#page=5 "Therefore, the number of operations scales linearly with k."))
- **c4** Evaluation protocol: held-out log-likelihood on binarized MNIST and Omniglot (standard splits), estimated as the mean of L_5000 on the test set (a stochastic lower bound); VAE and IWAE trained for k in {1, 5, 50} for about the same time; the learning-rate schedule was chosen from preliminary experiments with a one-layer VAE on MNIST.([Evaluation on density estimation, p.7](https://arxiv.org/pdf/1509.00519v4#page=7 "All log-likelihood values were estimated as the mean of L5000 on the test set."))
- **c5** The authors note that the generative-modelling literature binarizes MNIST inconsistently and that different binarizations can lead to considerably different log-likelihood values.([Evaluation on density estimation (footnote 2), p.6](https://arxiv.org/pdf/1509.00519v4#page=6 "Unfortunately, the generative modeling literature is inconsistent about the method of binarization, and different choices can lead to considerably different log-likelihood values."))
- **c6** Inactive latent dimensions: both VAEs and IWAEs learned representations with effective dimensions far below their capacity (a dimension counted as active if the covariance over x of its posterior mean exceeds 10^-2); with k > 1 the IWAE learned more active dimensions than the VAE in all cases.([Latent space representation, p.7](https://arxiv.org/pdf/1509.00519v4#page=7 "We have observed that both VAEs and IWAEs tend to learn latent representations with effective dimensions far below their capacity."))
- **c7** Swapping objectives after training (VAE continued with the IWAE objective and vice versa) changed the number of active dimensions and the log-likelihood in the direction of the new objective, which the authors take as strong evidence that inactivation is driven by the objective rather than by optimization, while noting that optimization also appears to play a role.([Latent space representation, p.8](https://arxiv.org/pdf/1509.00519v4#page=8 "The fact that training with the VAE objective actively reduces both the number of active dimensions and the log-likelihood strongly suggests that inactivation of the latent dimensions is driven by the objective functions rather than by optimization issues."))

