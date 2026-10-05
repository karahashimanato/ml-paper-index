<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Unsupervised Learning of Visual Features by Contrasting Cluster Assignments

- カード: [`arxiv-2006.09882`](../../papers/arxiv-2006.09882.yaml)
- 著者: Mathilde Caron, Ishan Misra, Julien Mairal, Priya Goyal, Piotr Bojanowski, Armand Joulin
- 年・掲載: 2020 NeurIPS 2020
- 原論文: [PDF](https://arxiv.org/pdf/2006.09882v5)(arXiv v5、カード作成時に読んだ版)
- タグ: image-classification, joint-embedding, representation-learning, self-supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Collapse prevention: codes are computed so that the examples in a batch are equally partitioned among the prototypes; this equipartition constraint keeps codes of different images distinct and prevents the trivial solution where every image has the same code.([Method (Computing codes online), p.4](https://arxiv.org/pdf/2006.09882v5#page=4 "This equipartition constraint ensures that the codes for different images in a batch are distinct, thus preventing the trivial solution where every image has the same code."))
- **c2** A strong entropy regularization (high epsilon) generally leads to a trivial solution where all samples collapse to a single representation and are assigned uniformly to all prototypes, so epsilon is kept low.([Method (Computing codes online), p.4](https://arxiv.org/pdf/2006.09882v5#page=4 "We observe that a strong entropy regularization (i.e. using a high ε) generally leads to a trivial solution where all samples collapse into an unique representation and are all assigned uniformely to all prototypes."))
- **c3** Small batches: when the batch is too small compared with the number of prototypes, an equal partition is impossible, so features from previous batches are stored to augment the assignment problem (around 3K features, i.e. the last 15 batches of 256, versus the 65K instances the authors say contrastive methods typically store).([Method (Working with small batches), p.5](https://arxiv.org/pdf/2006.09882v5#page=5 "Therefore, when working with small batches, we use features from the previous batches to augment the size of Z in Prob. (3)."))
- **c4** Batch size caveat: the headline ImageNet linear result is from 800 epochs with batches of 4096; results with shorter training and small batches are given separately (Fig. 3, Table 3).([Main Results, p.6](https://arxiv.org/pdf/2006.09882v5#page=6 "Note that we train SwAV during 800 epochs with large batches (4096)."))
- **c5** Cost in the small-batch setting (batch 256): SwAV with multi-crop runs 1.2x slower per epoch than SimCLR and about 1.4x slower than MoCov2; one epoch of MoCov2 or SimCLR is faster, but the authors say these methods need more epochs for good downstream performance.([Training with small batches, p.7](https://arxiv.org/pdf/2006.09882v5#page=7 "Hence, one epoch of MoCov2 or SimCLR is faster in wall clock time than one of SwAV, but these methods need more epochs for good downstream performance."))
- **c6** Sinkhorn iterations ablation: 3 iterations suffice for convergence; with fewer iterations the loss fails to converge, and more iterations slightly alter transfer performance (conjectured to be due to converging too rapidly, as with discrete codes).([Appendix C.4, p.21](https://arxiv.org/pdf/2006.09882v5#page=21 "When performing less iterations, the loss fails to converge."))
- **c7** Prototypes: learning them improves over fixed random prototypes only modestly; the authors say the prototypes are not strongly encouraged to be categorical, and that they help contrast views without pairwise comparisons with many negatives.([Appendix (Learning the prototypes), p.20](https://arxiv.org/pdf/2006.09882v5#page=20 "Indeed, the prototypes in SwAV are not strongly encouraged to be categorical and random ﬁxed prototypes work almost as well."))
- **c8** Multi-crop improves several self-supervised methods (SimCLR, SeLa-v2, DeepCluster-v2, SwAV) in the authors' re-implementations with matched augmentation, epochs and batch size, and seems to benefit clustering-based methods more than contrastive ones; it does not improve the supervised model.([Ablation Study (Applying the multi-crop strategy to different methods), p.8](https://arxiv.org/pdf/2006.09882v5#page=8 "Interestingly, multi-crop seems to beneﬁt more clustering-based methods than contrastive methods."))

