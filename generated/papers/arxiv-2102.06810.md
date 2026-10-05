<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Understanding self-supervised Learning Dynamics without Contrastive Pairs

- カード: [`arxiv-2102.06810`](../../papers/arxiv-2102.06810.yaml)
- 著者: Yuandong Tian, Xinlei Chen, Surya Ganguli
- 年・掲載: 2021 ICML 2021
- 原論文: [PDF](https://arxiv.org/pdf/2102.06810v4)(arXiv v4、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Theorem 2 (SimSiam case, W_a = W): removing the stop-gradient turns the update into a PSD-matrix flow, and if its minimal eigenvalue stays bounded below the weights go to zero; the authors say this proves, in this simple setting, collapse without stop-gradient (and similarly without a predictor).([Two-layer linear model (Theorem 2), p.3](https://arxiv.org/pdf/2102.06810v4#page=3 "Thus we have proven analytically in this simple setting that removing the stop-gradient leads to representational collapse"))
- **c2** Theorem 1: weight decay promotes balancing between predictor and online weights, so what the predictor learns the online network also learns; a nonzero weight decay could help remove the initialization-dependent constant.([Two-layer linear model (Theorem 1), p.3](https://arxiv.org/pdf/2102.06810v4#page=3 "Instead what the predictor learns, the online network will also learn, which is important as the online network’s representations are what is used for downstream tasks."))
- **c3** Simplifying assumptions behind the analytic results: (1) the EMA target stays proportional to the online network, (2) isotropic data (zero mean, identity covariance) and isotropic augmentation noise, (3) a symmetric predictor; the authors report that the predictions still hold qualitatively when the assumptions do not.([How multiple factors affect learning dynamics (Assumption 2), p.4](https://arxiv.org/pdf/2102.06810v4#page=4 "We assume the data distribution p(x) has zero mean and identity covariance, while the augmentation distribution paug(·/x) has mean x and covariance σ2I."))
- **c4** Theorem 3: under these assumptions the eigenspaces of the predictor and of the correlation matrix of its inputs gradually align (given a positive-definite condition), giving decoupled per-mode dynamics; the non-symmetric-predictor case is left for future work.([Section 3.1, p.5](https://arxiv.org/pdf/2102.06810v4#page=5 "When Assumption 3 is absent, the analysis is much more convoluted."))
- **c5** Collapse in the decoupled dynamics: a collapsed fixed point always exists; with weight decay there is a basin of attraction to collapse that grows with weight decay, and under strong enough weight decay collapse is unavoidable.([Section 3.2, p.7](https://arxiv.org/pdf/2102.06810v4#page=7 "Under such strong weight decay collapse is unavoidable (Obs#5)."))
- **c6** EMA can act as an automatic curriculum by setting a small initial goal for the predictor eigenvalues and raising it gradually, with the trade-offs of slow training for slow EMA and more modes possibly trapped in the collapsed basin.([Section 3.2 (Role of EMA), p.7](https://arxiv.org/pdf/2102.06810v4#page=7 "Therefore, EMA can serve as an automatic curriculum (Obs#8)"))
- **c7** Experimental protocol: STL-10/CIFAR-10 use ResNet-18, SGD (lr 0.03, momentum 0.9, weight decay 0.0004, EMA 0.996), 5 repeats per setting; ImageNet uses the authors' own BYOL implementation with ResNet-50, with architecture, augmentations and linear classification protocol strictly following BYOL (60-epoch and 300-epoch settings).([Optimization-free Predictor Wp (ImageNet experiments), p.9](https://arxiv.org/pdf/2102.06810v4#page=9 "The architecture design (e.g., feature dimensions), augmentation strategies (e.g., color jittering, blur (Chen et al., 2020a), solarization, etc.) and linear classiﬁcation protocol strictly follow BYOL (Grill et al., 2020)."))
- **c8** Scope: the theory covers a linear predictor; for the 2-layer predictor used in practice the authors give no formal analysis, only an intuition that its wide hidden layer offers 'lucky' initial directions that speed up eigenspace alignment.([Section 5 (Discussion), p.9](https://arxiv.org/pdf/2102.06810v4#page=9 "While we don’t provide a formal analysis and the math can be quite complicated"))

