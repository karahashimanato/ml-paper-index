<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Exploring Simple Siamese Representation Learning

- カード: [`arxiv-2011.10566`](../../papers/arxiv-2011.10566.yaml)
- 著者: Xinlei Chen, Kaiming He
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2011.10566v1)(arXiv v1、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main finding: collapsing solutions exist for the SimSiam loss and architecture, but a stop-gradient operation plays an essential role in preventing collapse.([Abstract, p.1](https://arxiv.org/pdf/2011.10566v1#page=1 "Our experiments show that collapsing solutions do exist for the loss and structure, but a stop-gradient operation plays an essential role in preventing collapsing."))
- **c2** Removing only the stop-gradient (architecture and hyperparameters unchanged) gives chance-level linear accuracy; collapse is diagnosed by the loss reaching its minimum of -1 and by the per-channel std of the l2-normalized output going to zero. The authors note in a footnote that chance-level accuracy alone does not indicate collapse, since a diverging loss can also give it.([Section 4.1, p.4](https://arxiv.org/pdf/2011.10566v1#page=4 "Solely removing stop-gradient, the accuracy becomes 0.1%, which is the chance-level guess in ImageNet."))
- **c3** The predictor is needed: removing it (identity mapping) collapses, which is expected for the symmetrized loss; the asymmetric loss also fails without it; a predictor fixed at random initialization fails without collapsing (training does not converge).([Section 4.2, p.4](https://arxiv.org/pdf/2011.10566v1#page=4 "The model does not work if removing h (Table 1a), i.e., h is the identity mapping."))
- **c4** Batch size (64 to 4096, plain SGD, 100-epoch pre-training): SimSiam works reasonably well over the whole range, unlike SimCLR and SwAV which the authors say need large batches; the result is lower with 4096, which they attribute to SGD with very large batches.([Section 4.3, p.4](https://arxiv.org/pdf/2011.10566v1#page=4 "Our method works reasonably well over this wide range of batch sizes."))
- **c5** Batch size, batch normalization, similarity function and symmetrization may affect accuracy, but the authors saw no evidence that they are related to collapse prevention; it is mainly the stop-gradient.([Section 4.7, p.5](https://arxiv.org/pdf/2011.10566v1#page=5 "The optimizer (batch size), batch normalization, similarity function, and symmetrization may affect accuracy, but we have seen no evidence that they are related to collapse prevention."))
- **c6** On BYOL's momentum encoder: the authors argue that the importance of stop-gradient can be obscured by a momentum encoder (always accompanied by stop-gradient), and that moving averaging may improve accuracy but is not directly related to preventing collapse.([Related Work (BYOL), p.2](https://arxiv.org/pdf/2011.10566v1#page=2 "While the moving-average behavior may improve accuracy with an appropriate momentum coefﬁcient, our experiments show that it is not directly related to preventing collapsing."))
- **c7** Hypothesis, not proof: SimSiam is hypothesized to be an EM-like alternating optimization over network weights and per-image representations (Section 5); the authors state that this hypothesis is about what the optimization problem can be, that it does not explain why collapse is prevented, and that non-collapse remains an empirical observation.([Section 5.3, p.7](https://arxiv.org/pdf/2011.10566v1#page=7 "We point out that SimSiam and its variants’ non-collapsing behavior still remains as an empirical observation."))
- **c8** Comparisons on ImageNet linear evaluation use the authors' own reproductions of all competitors (some improved over the original papers), each with its original hyperparameter and augmentation recipe, ResNet-50 and two 224x224 views.([Section 6.1, p.7](https://arxiv.org/pdf/2011.10566v1#page=7 "For fair comparisons, all competitors are based on our reproduction, and “+” denotes improved reproduction vs. the original papers (see supplement)."))

