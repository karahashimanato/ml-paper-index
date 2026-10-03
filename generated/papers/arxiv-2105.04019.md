<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Differentiable Sorting Networks for Scalable Sorting and Ranking Supervision

- カード: [`arxiv-2105.04019`](../../papers/arxiv-2105.04019.yaml)
- 著者: Felix Petersen, Christian Borgelt, Hilde Kuehne, Oliver Deussen
- 年・掲載: 2021
- 原論文: [PDF](https://arxiv.org/pdf/2105.04019v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, differentiable-sorting, image-classification, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution and relation to classical sorting: classical sorting networks (fixed, data-oblivious compare-and-swap structures; odd-even and Batcher's bitonic sorter) are made differentiable by relaxing their pairwise conditional swap operations.([Abstract, p.1](https://arxiv.org/pdf/2105.04019v2#page=1 "For that, we propose differentiable sorting networks by relaxing their pairwise conditional swap operations."))
- **c2** Why sorting networks are non-differentiable: they use min and max operators for the conditional swaps, which the paper relaxes with softmin/softmax.([Introduction, p.1](https://arxiv.org/pdf/2105.04019v2#page=1 "Sorting networks are conventionally non-differentiable as they use min and max operators for conditionally swapping elements."))
- **c3** Stated complexity: the differentiable odd-even network runs in O(n^3) and the differentiable bitonic network in O(n^2 (log n)^2), with the layer-wise permutation-matrix product computed as a sparse multiplication.([5.5 Runtime and Memory Analysis, p.9](https://arxiv.org/pdf/2105.04019v2#page=9 "The asymptotic runtime of differentiable odd-even sort is in O(n3) and for bitonic sort the runtime is in O(n2(log n)2)."))
- **c4** Runtime comparison with other relaxations: for large n the authors empirically confirm FastRank (Blondel et al.) is the fastest method, partly because it outputs only ranks/sorted values rather than differentiable permutation matrices, which they say are necessary for their cross-entropy objective.([5.5 Runtime and Memory Analysis, p.9](https://arxiv.org/pdf/2105.04019v2#page=9 "For large n, we empirically conﬁrm that FastRank (Blondel et al., 2020) is the fastest method, i.a., because it produces only output ranks / sorted output values and not differentiable permutation matrices."))
- **c5** Evaluation protocol caveat: in the four-digit MNIST comparison, the NeuralSort and Optimal Transport rows are copied from Cuturi et al. rather than rerun (same CNN architecture; averaged over 5 runs for the new rows).([5.1 Sorting and Ranking Supervision (Table 1 caption), p.6](https://arxiv.org/pdf/2105.04019v2#page=6 "The ﬁrst three rows are duplicated from Cuturi et al. (2019)."))
- **c6** Evaluation protocol caveat: Blondel et al.'s Fast Sort & Rank was trained with a mean-squared-error loss on ranks, because it does not produce differentiable permutation matrices (the proposed method uses a cross-entropy loss on relaxed permutation matrices).([Appendix B.3 (Fast Sort & Rank), p.12](https://arxiv.org/pdf/2105.04019v2#page=12 "To evaluate the fast sorting and ranking method by Blondel et al. (2020), we used the mean-squared-error loss between predicted and ground truth ranks as this method does not produce differentiable permutation matrices."))
- **c7** Main empirical claim (four-digit MNIST sorting benchmark of Grover et al. / Cuturi et al., n in {3, 5, 7, 9, 15}): the authors state the odd-even network outperforms current methods on all metrics and input set sizes; the NeuralSort and OT figures it is compared with are the rows copied from Cuturi et al.([5.1.1 Results (Comparison to State-of-the-Art (MNIST)), p.7](https://arxiv.org/pdf/2105.04019v2#page=7 "Our approach outperforms current methods on all metrics and input set sizes."))

