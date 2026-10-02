<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Localized TabICLv2: Scaling Tabular In-Context Learning through k-NN

- カード: [`arxiv-2608.16429`](../../papers/arxiv-2608.16429.yaml)
- 著者: Beimnet Bekele Guta
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.16429v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, in-context-learning, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Localized TabICLv2 cuts TabICLv2's inference cost by retrieving only the k nearest training neighbours of each test point in the model's Stage 2 representation space, instead of using the full training context.([Abstract, p.1](https://arxiv.org/pdf/2608.16429v1#page=1 "Localized TabICLv2 introduces a method that reduces the inference cost of TabICLv2 by retrieving only the k nearest training neighbours for each test point, measured by similarity in the model’s Stage 2 row-representation space, rather than using the full training context."))
- **c2** On TabArena classification tasks, the fine-tuned localized model keeps most of Full TabICLv2's accuracy and speeds up batch inference.([Abstract, p.1](https://arxiv.org/pdf/2608.16429v1#page=1 "On TabArena classification tasks, the fine-tuned localized model retains 98.64% of Full TabICLv2 accuracy and it achieves a median 2.18× speedup in batch inference"))
- **c3** Evaluation covers 38 TabArena binary and multiclass classification datasets, using an 80/20 stratified train/test split and three random seeds.([Results and Discussion, p.3](https://arxiv.org/pdf/2608.16429v1#page=3 "We use an 80/20 stratified train/test split and run each experiment over three random seeds."))
- **c4** The XGBoost baseline is trained on the full training set. No hyperparameter configuration or tuning for XGBoost was found in the text.([Results and Discussion, p.3](https://arxiv.org/pdf/2608.16429v1#page=3 "XGBoost trained on the full training set and retrieval-only baselines"))
- **c5** The localized method does not exceed Full TabICLv2's accuracy.([Results and Discussion, p.3](https://arxiv.org/pdf/2608.16429v1#page=3 "Overall, the localized method does not surpass the accuracy of Full TabICLv2."))
- **c6** Limitation: localization may underperform when the retrieved neighbours miss useful evidence, and retrieval overhead can reduce speedups on smaller datasets or large query batches.([Conclusion, p.4](https://arxiv.org/pdf/2608.16429v1#page=4 "However, localization may underperform when useful evidence is not captured by the retrieved neighbours, and retrieval overhead can reduce speedups on smaller datasets or large query batches."))

