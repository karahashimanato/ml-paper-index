<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# PACE: Plug-and-Play Contextual Embedding for Feature Screening with Pretrained Tabular Foundation Models

- カード: [`arxiv-2609.23574`](../../papers/arxiv-2609.23574.yaml)
- 著者: Qi Qin, Erbo Li, Ting Wei, Zizhou Huang, Zixuan Qin, Wu Wang, Yifan Sun
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.23574v1)(arXiv v1、カード作成時に読んだ版)
- タグ: supervised, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** PACE inserts a frozen tabular foundation model column encoder before an existing feature-scoring rule, expanding each feature into a higher-dimensional contextual representation.([Abstract, p.1](https://arxiv.org/pdf/2609.23574v1#page=1 "We intro- duce PACE (Plug-and-Play Contextual Embedding), which inserts a frozen tabular foundation model (TFM) column encoder before an existing feature-scoring rule, expanding each feature into a higher-dimensional contextual representation."))
- **c2** Matched random-weight and random-feature controls indicate the gains come from pretrained structure, not just dimensional expansion.([Abstract, p.1](https://arxiv.org/pdf/2609.23574v1#page=1 "Matched random-weight and random-feature controls show that PACE gains from pretrained structure beyond generic dimen- sional expansion."))
- **c3** Evaluation protocol: TALENT datasets are augmented with independent Gaussian nuisance features up to a fixed total width before screening.([Appendix, p.28](https://arxiv.org/pdf/2609.23574v1#page=28 "the nuisance-augmented table adds independent N(0, 1) features until its total width is 2,000"))
- **c4** Screened features are evaluated with ten downstream learners in three families (tree models, neural networks, tabular foundation models).([Experimental setup, p.6](https://arxiv.org/pdf/2609.23574v1#page=6 "We evaluate the selected columns using ten learners in three families"))
- **c5** When a TALENT training partition is large, embedding and utility estimation use a row-capped subsample.([Appendix, p.14](https://arxiv.org/pdf/2609.23574v1#page=14 "When a TALENT training partition exceeds 2,000 rows, embedding and utility estimation use at most 2,000 rows, selected by stratified sampling for classification and by sampling without replacement for regression using the corresponding random seed."))
- **c6** Limitation: screening performance still depends on representation, utility, backbone and extraction strategy.([Conclusion, p.9](https://arxiv.org/pdf/2609.23574v1#page=9 "Screening performance still depends on the representation, utility, backbone, and extraction strategy."))

