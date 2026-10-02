<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tabular foundation models for non-tabular tasks

- カード: [`arxiv-2608.22594`](../../papers/arxiv-2608.22594.yaml)
- 著者: Goran Nakerst, John Brennan, Wouter Beugeling, Masudul Haque
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.22594v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, gradient-boosted-trees, in-context-learning, supervised, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabPFN v3 is applied to three non-tabular classification problems: MNIST digits, French vs. German word identification, and Tiny ImageNet.([Abstract, p.1](https://arxiv.org/pdf/2608.22594v1#page=1 "We address this question by using TabPFN v3 on three non-tabular classification problems: handwritten digit recognition on MNIST, language identification of French and German words, and image classification on Tiny ImageNet."))
- **c2** Without access to spatial or sequential structure, TabPFN v3 in some cases reaches accuracies comparable to task-specific models.([Abstract, p.1](https://arxiv.org/pdf/2608.22594v1#page=1 "Despite having no explicit access to the spatial or sequential structure characterizing the data, TabPFN v3 in some cases achieves accuracies comparable with that of models or methods geared specifically toward the corresponding tasks."))
- **c3** TabPFN v3 is run with library defaults, with one override that disables the pretraining input-size limits. Every experiment exceeds those limits.([Appendix A (TabPFN v3 configuration), p.6](https://arxiv.org/pdf/2608.22594v1#page=6 "All TabPFN results use model v3 library defaults with a single override"))
- **c4** On MNIST, the LightGBM baseline is not hyperparameter-searched. Its regularization is scaled by hand with training size.([Appendix A (MNIST), p.6](https://arxiv.org/pdf/2608.22594v1#page=6 "LightGBM sees the same 784 columns, with regularization scaled to the training size rather than searched"))
- **c5** On the word task, LightGBM is tuned separately at each training size and encoding with randomized search and stratified 5-fold CV on the training set only. The test set is never seen during tuning.([Appendix A (French/German words), p.7](https://arxiv.org/pdf/2608.22594v1#page=7 "LightGBM is tuned independently at each training size and encoding."))
- **c6** On the word task, tuned LightGBM pulls clearly ahead only when data is plentiful.([Conclusion, p.4](https://arxiv.org/pdf/2608.22594v1#page=4 "Only once data is plentiful does the tuned LightGBM pull clearly ahead."))

