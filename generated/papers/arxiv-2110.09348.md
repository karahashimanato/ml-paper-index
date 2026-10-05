<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Understanding Dimensional Collapse in Contrastive Self-supervised Learning

- カード: [`arxiv-2110.09348`](../../papers/arxiv-2110.09348.yaml)
- 著者: Li Jing, Pascal Vincent, Yann LeCun, Yuandong Tian
- 年・掲載: 2021 ICLR 2022
- 原論文: [PDF](https://arxiv.org/pdf/2110.09348v3)(arXiv v3、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Empirical observation: for a SimCLR model with a two-layer MLP projector trained 100 epochs on ImageNet, the singular-value spectrum of the covariance of 128-d embeddings on the validation set has a number of singular values collapsing to zero, although negatives prevent complete collapse.([Dimensional Collapse, p.3](https://arxiv.org/pdf/2110.09348v3#page=3 "We observe that a number of singular values collapse to zero, thus representing collapsed dimensions."))
- **c2** Mechanism 1 (single linear layer, additive-noise augmentation, InfoNCE, plain SGD without momentum or weight decay): the weight update is driven by the difference of a weighted data covariance and a weighted augmentation covariance; if augmentation is strong enough that this matrix has negative eigenvalues, the weight matrix gets vanishing singular values and the embedding covariance becomes low-rank.([Dimensional Collapse Caused by Strong Augmentation (Theorem 1), p.4](https://arxiv.org/pdf/2110.09348v3#page=4 "With ﬁxed matrix X (deﬁned in Eqn 6) and strong augmentation such that X has negative eigenvalues, the weight matrix W has vanishing singular values."))
- **c3** The strong-augmentation theory is limited to linear networks; for nonlinear networks the authors say 'strong augmentation' would depend on more complicated properties (higher-order statistics, manifold properties) conditioned on network capacity.([Dimensional Collapse Caused by Strong Augmentation, p.5](https://arxiv.org/pdf/2110.09348v3#page=5 "Our theory in this section is limited to linear network settings."))
- **c4** Mechanism 2 (implicit regularization): with small augmentation and an over-parametrized two-layer linear network (no bias, unnormalized output), adjacent weight matrices align and small singular values grow much more slowly, so the embedding covariance becomes low-rank; this happens only with more than one layer.([Dimensional Collapse Caused by Implicit Regularization (Corollary 2), p.6](https://arxiv.org/pdf/2110.09348v3#page=6 "With small augmentation and over-parametrized linear networks, the embedding space covariance matrix becomes low-rank."))
- **c5** The alignment result (Theorem 2) assumes distinct singular values; the toy experiment initializes non-degenerate singular values, and with random initialization in real scenarios only block-diagonal alignment is expected.([Weight Alignment, p.6](https://arxiv.org/pdf/2110.09348v3#page=6 "In real scenario, when weight matrices are randomly initialized, we will only observe the alignment matrix to converge to a block-diagonal matrix, with each block representing a group of degenerate singular values."))
- **c6** Role of the projector: comparing SimCLR trained with and without a projector, dimensional collapse in the representation (backbone output) space appears without a projector, so the projector prevents collapse there.([DirectCLR (Motivation), p.7](https://arxiv.org/pdf/2110.09348v3#page=7 "The dimensional collapse in representation space happens when the model is trained without a projector."))
- **c7** Stated limit of the theory: it can explain a linear projector (DirectCLR replaces it) but cannot fully explain why a nonlinear projector prevents dimensional collapse, and DirectCLR still relies on the last nonlinear backbone block for that mechanism.([DirectCLR (Disclaimer), p.9](https://arxiv.org/pdf/2110.09348v3#page=9 "But our theory is not able to fully explain why a nonlinear projector is able to prevent dimensional collapse."))
- **c8** Protocol: ResNet-50, SimCLR recipe for 100 epochs (LARS, batch size 4096 on 32 GPUs); the sub-vector size d0 was tuned on ImageNet linear-probe top-1 accuracy. No separate held-out split for this tuning was found in the text (searched for validation, held-out, tuning).([Appendix E (Figure 12), p.17](https://arxiv.org/pdf/2110.09348v3#page=17 "Hyperparameter tuning on d0 based on ImageNet linear probe Top-1 accuracy."))

