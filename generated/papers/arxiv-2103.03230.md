<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Barlow Twins: Self-Supervised Learning via Redundancy Reduction

- カード: [`arxiv-2103.03230`](../../papers/arxiv-2103.03230.yaml)
- 著者: Jure Zbontar, Li Jing, Ishan Misra, Yann LeCun, Stéphane Deny
- 年・掲載: 2021 ICML 2021
- 原論文: [PDF](https://arxiv.org/pdf/2103.03230v3)(arXiv v3、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Claim of the method: Barlow Twins needs neither large batches nor asymmetry between the twins (predictor, stop-gradient, moving-average weights), and benefits from very high-dimensional output vectors.([Abstract, p.1](https://arxiv.org/pdf/2103.03230v3#page=1 "BARLOW TWINS does not require large batches nor asymmetry between the network twins such as a predictor network, gradient stopping, or a moving average on the weight updates."))
- **c2** Loss ablation (300-epoch runs; Table 5 caption, with the body text saying the same): removing either the invariance (on-diagonal) term or the redundancy-reduction (off-diagonal) term gives worse or collapsed solutions.([Table 5, p.5](https://arxiv.org/pdf/2103.03230v3#page=5 "We ablate the invariance and redundancy terms in our proposed loss and observe that both terms are necessary for good performance."))
- **c3** Batch size: with a LARS learning-rate grid search per batch size, performance is almost unaffected down to batch 256, unlike SimCLR. The BYOL and SimCLR curves in Figure 2 are taken from their papers, not re-run.([Section 4 (Robustness to Batch Size), p.5](https://arxiv.org/pdf/2103.03230v3#page=5 "We ﬁnd that, unlike SIMCLR, our model is robust to small batch sizes (Fig. 2), with a performance almost unaffected for a batch as small as 256."))
- **c4** Augmentations: Barlow Twins is not robust to removing some augmentations, like SimCLR and unlike BYOL; the authors present this as a possible disadvantage, or as the representation being better controlled by the chosen distortions.([Section 4 (Effect of Removing Augmentations), p.5](https://arxiv.org/pdf/2103.03230v3#page=5 "We ﬁnd that our model is not robust to removing some types of data augmentations, like SIMCLR but unlike BYOL (Fig. 3)."))
- **c5** Projector dimensionality: performance keeps improving with all output dimensionalities tested, while other methods saturate (data for SimCLR and BYOL taken from their papers), even though the 2048-d ResNet output is a bottleneck.([Section 4 (Projector Network Depth & Width), p.6](https://arxiv.org/pdf/2103.03230v3#page=6 "Other methods rapidly saturate when the dimensionality of the output increases, but our method keeps improving with all output dimensionality tested (Fig. 4)."))
- **c6** Adding BYOL/SimSiam-style asymmetry (a predictor and/or a stop-gradient) slightly decreases Barlow Twins' performance.([Section 4 (Breaking Symmetry), p.6](https://arxiv.org/pdf/2103.03230v3#page=6 "We ﬁnd that these asymmetries slightly decrease the performance of our network (see Table 6)."))
- **c7** The authors argue that asymmetric methods (BYOL, SimSiam) cannot be described as optimizing an overall objective, since trivial solutions exist that they avoid through implementation choices or learning dynamics, whereas Barlow Twins avoids them by construction.([Section 5.1 (Asymmetric Twins), p.8](https://arxiv.org/pdf/2103.03230v3#page=8 "It should be noted however that these asymmetric methods cannot be described as the optimization of an overall learning objective."))
- **c8** Theory caveat: the information-bottleneck interpretation assumes Gaussian representations, and the actual loss is linked to it only through listed simplifications and approximations (e.g. replacing the log-determinant by a decorrelation proxy, cross- instead of auto-correlation).([Appendix A, p.12](https://arxiv.org/pdf/2103.03230v3#page=12 "In order to circumvent this difﬁculty, we make the simplifying assumption that the representation Z is distributed as a Gaussian."))

