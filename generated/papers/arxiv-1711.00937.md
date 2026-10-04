<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Neural Discrete Representation Learning

- カード: [`arxiv-1711.00937`](../../papers/arxiv-1711.00937.yaml)
- 著者: Aaron van den Oord, Oriol Vinyals, Koray Kavukcuoglu
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1711.00937v2)(arXiv v2、カード作成時に読んだ版)
- タグ: generative-modeling, representation-learning, unsupervised, variational-autoencoders
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** VQ-VAE differs from VAEs in two ways: the encoder outputs discrete codes, and the prior is learnt rather than static; the authors state that using vector quantisation lets the model circumvent posterior collapse with powerful autoregressive decoders.([Abstract, p.1](https://arxiv.org/pdf/1711.00937v2#page=1 "Using the VQ method allows the model to circumvent issues of “posterior collapse”"))
- **c2** Training: since the nearest-neighbour lookup has no gradient, gradients are copied from the decoder input to the encoder output (straight-through estimator).([Learning, p.3](https://arxiv.org/pdf/1711.00937v2#page=3 "we approximate the gradient similar to the straight-through estimator [3] and just copy gradients from decoder input zq(x) to encoder output ze(x)."))
- **c3** The loss adds a codebook term and a commitment term weighted by beta; the authors report that results did not vary for beta between 0.1 and 2.0 and use beta = 0.25 throughout, noting that in general this depends on the scale of the reconstruction loss.([Learning, p.4](https://arxiv.org/pdf/1711.00937v2#page=4 "We found the resulting algorithm to be quite robust to β, as the results did not vary for values of β ranging from 0.1 to 2.0."))
- **c4** With a deterministic one-hot posterior and a uniform prior, the KL term is a constant (log K) and is ignored in training; the prior is kept uniform during VQ-VAE training and an autoregressive prior is fitted afterwards (joint training left to future work).([Prior, p.5](https://arxiv.org/pdf/1711.00937v2#page=5 "Whilst training the VQ-VAE, the prior is kept constant and uniform."))
- **c5** The authors could not train with a soft-to-hard relaxation of vector quantisation from scratch because the decoder always learned to invert the continuous relaxation, so no actual quantisation took place.([Related Work, p.3](https://arxiv.org/pdf/1711.00937v2#page=3 "In our experiments we were unable to train using the soft-to-hard relaxation approach from scratch as the decoder was always able to invert the continuous relaxation during training, so that no actual quantisation took place."))
- **c6** Comparison on CIFAR10 with the same architecture (lower bounds in bits/dim): the continuous VAE obtains a better bound than VQ-VAE, and VQ-VAE a better bound than VIMCO; all reported likelihoods are lower bounds.([Comparison with continuous variables, p.5](https://arxiv.org/pdf/1711.00937v2#page=5 "The VAE, VQ-VAE and VIMCO models obtain 4.51 bits/dim, 4.67 bits/dim and 5.14 respectively."))
- **c7** ImageNet 128x128 images compressed to a 32x32x1 discrete latent (K = 512) are reconstructed with an MSE-trained deconvolutional decoder and look only slightly blurrier than the originals (qualitative, Figure 2); a perceptual or GAN loss is left to future work.([Images, p.6](https://arxiv.org/pdf/1711.00937v2#page=6 "Even considering that we greatly reduce the dimensionality with discrete encoding, the reconstructions look only slightly blurrier than the originals."))

