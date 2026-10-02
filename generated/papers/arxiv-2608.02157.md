<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# RamanPFN: learning from Raman spectral structure with a tabular foundation model

- カード: [`arxiv-2608.02157`](../../papers/arxiv-2608.02157.yaml)
- 著者: Xingyu Pan, Huan Wang, Jinjia Guo, Zhenlin Zhao, Siming Dong, Jixi Lu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.02157v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** RamanPFN is a spectral framework that feeds physics-guided Raman representations to a tabular foundation model for in-context inference.([Abstract, p.1](https://arxiv.org/pdf/2608.02157v2#page=1 "Here we present RamanPFN, a general-purpose spectral foundation framework that enables unified in-context inference through physics-guided spectral learning."))
- **c2** RamanPFN achieves the best aggregate metrics against 28 independently reproduced methods, including tabular foundation models.([Abstract, p.1](https://arxiv.org/pdf/2608.02157v2#page=1 "RamanPFN achieved state-of-the-art performance across all reported aggregate metrics against 28 independently reproduced methods spanning chemometrics, spectral neural networks, deep tabular learners and tabular foundation models."))
- **c3** Evaluation uses the public RamanBench collection and its published task definitions.([Methods, p.11](https://arxiv.org/pdf/2608.02157v2#page=11 "We evaluated RamanPFN using the public RamanBench collection and its published task definitions [12]."))
- **c4** The protocol is the published 80/20 train-test split with three seeds.([Methods, p.11](https://arxiv.org/pdf/2608.02157v2#page=11 "Experiments followed the published 80/20 train–test protocol, with seeds 0, 1 and 2 defining three repetitions."))
- **c5** Baselines keep their own preprocessing and fitting procedures on common partitions; a hyperparameter tuning budget for baselines was not found in the text.([Methods, p.13](https://arxiv.org/pdf/2608.02157v2#page=13 "Each baseline retained its own preprocessing and fitting procedure on the common data partitions."))
- **c6** Regression tasks are small and wide: 6 to 6,203 training spectra with 114 to 11,689 channels.([Results, p.3](https://arxiv.org/pdf/2608.02157v2#page=3 "Regression training sets ranged from 6 to 6,203 spectra, with 114 to 11,689 wavenumber channels."))

