<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium

- カード: [`arxiv-1706.08500`](../../papers/arxiv-1706.08500.yaml)
- 著者: Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter
- 年・掲載: 2017 NeurIPS 2017
- 原論文: [PDF](https://arxiv.org/pdf/1706.08500v6)(arXiv v6、カード作成時に読んだ版)
- タグ: deep-learning, generative-modeling, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TTUR (briefly): with separate learning rates for discriminator and generator, the authors prove via stochastic approximation theory that GAN training converges under mild assumptions to a stationary local Nash equilibrium; the convergence carries over to Adam.([Abstract, p.1](https://arxiv.org/pdf/1706.08500v6#page=1 "Using the theory of stochastic approximation, we prove that the TTUR converges under mild assumptions to a stationary local Nash equilibrium."))
- **c2** Motivation for FID: the drawback of the Inception Score is that it does not use the statistics of real-world samples and compare them with those of synthetic samples.([Experiments (Performance Measure), p.6](https://arxiv.org/pdf/1706.08500v6#page=6 "Drawback of the Inception Score is that the statistics of real world samples are not used and compared to the statistics of synthetic samples."))
- **c3** FID definition and its assumption: only the first two moments (mean and covariance) of the Inception coding layer are used, the coding units are assumed to follow a multidimensional Gaussian (justified as the maximum-entropy distribution for given mean and covariance), and the two Gaussians are compared with the Fréchet (Wasserstein-2) distance.([Experiments (Performance Measure), p.6](https://arxiv.org/pdf/1706.08500v6#page=6 "The Gaussian is the maximum entropy distribution for given mean and covariance, therefore we assume the coding units to follow a multidimensional Gaussian."))
- **c4** Evidence offered for FID: on CelebA, six disturbances (Gaussian noise, Gaussian blur, implanted black rectangles, swirl, salt-and-pepper noise, contamination with ImageNet images) are applied at increasing levels, and the authors state that FID captures the disturbance level very well (shown as a figure). The text claims FID is consistent with 'disturbances and human judgment', but no human study was found in the text (searched for human, judg).([Experiments (Performance Measure), p.6](https://arxiv.org/pdf/1706.08500v6#page=6 "The FID captures the disturbance level very well."))
- **c5** Comparison with the Inception Score (Appendix A1, figure caption): across the disturbances, FID increases monotonically with the disturbance level, whereas the Inception Score (converted to a distance) fluctuates, stays flat or decreases; the comparison is shown only as a figure.([Appendix A1 (Figure A8), p.13](https://arxiv.org/pdf/1706.08500v6#page=13 "The FID captures the disturbance level very well by monotonically increasing whereas the Inception Score ﬂuctuates, stays ﬂat or even, in the worst case, decreases."))
- **c6** FID computation protocol: reference statistics are computed from all training images passed through the pretrained Inception-v3 (last pooling layer as coding layer), and model statistics from 50,000 generated images.([Experiments (Model Selection and Evaluation), p.7](https://arxiv.org/pdf/1706.08500v6#page=7 "To approximate these moments for the model distribution, we generate 50,000 images, propagate them through the Inception-v3 model, and then compute the mean m and the covariance matrix C."))
- **c7** Model selection used the evaluation metric: learning rates were optimized to be large while keeping training stable as indicated by a decreasing FID (or JSD), and the stopping time was fixed to the update step when the FID or JSD of the best models stopped decreasing; Table 1 reports the best FID for optimized number of updates and learning rates.([Experiments (Model Selection and Evaluation), p.7](https://arxiv.org/pdf/1706.08500v6#page=7 "We further ﬁxed the time point for stopping training to the update step when the FID or Jensen-Shannon-divergence of the best models was no longer decreasing."))
- **c8** Scope limitation: FID only works for images, so the character-level language experiments (One Billion Word) are evaluated with the Jensen-Shannon divergence instead, as done previously [23].([Experiments (WGAN-GP on Language Data), p.9](https://arxiv.org/pdf/1706.08500v6#page=9 "Since the FID criterium only works for images, we measured the performance by the Jensen-Shannon-divergence (JSD) between the model and the real world distribution as has been done previously [23]."))

