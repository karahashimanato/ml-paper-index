<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Comparative Framework for Evaluating Foundation Models on Tabular Data: A Case Study in Healthcare

- カード: [`arxiv-2609.22154`](../../papers/arxiv-2609.22154.yaml)
- 著者: Majid Lotfian Delouee, Sjors G. J. G. In 't Veld, Martijn C. Schut
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.22154v1)(arXiv v1、カード作成時に読んだ版)
- タグ: tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** OpTFM scores and ranks tabular foundation models across six clinically meaningful dimensions.([Abstract, p.1](https://arxiv.org/pdf/2609.22154v1#page=1 "We introduce OpTFM, a comparative evaluation framework that scores and ranks tabular foundation models (TFMs) across six clinically meaningful dimensions"))
- **c2** Applied to two healthcare use cases, the same metrics lead to different model rankings depending on clinical priorities.([Abstract, p.1](https://arxiv.org/pdf/2609.22154v1#page=1 "To show how the framework works in practice, we apply it to two healthcare use cases, screening for iron deficiency and predicting heart failure, demonstrating how the same set of metrics leads to different model rankings depending on what matters most in each clinical context."))
- **c3** Evaluation protocol: no models are run; sub-metric scores are derived from each model's documented design properties.([Framework, p.7](https://arxiv.org/pdf/2609.22154v1#page=7 "sub-metric scores are derived from each model’s documented design properties"))
- **c4** Scores start at a default of 10 and are reduced by 1 for each missing or problematic property.([Case study, p.12](https://arxiv.org/pdf/2609.22154v1#page=12 "Models start with a default sub-metric score of 10, and each missing or problematic property reduces the relevant sub-metric scores by 1."))
- **c5** The scores are property-based estimates, not substitutes for empirical measurement.([Case study, p.12](https://arxiv.org/pdf/2609.22154v1#page=12 "The resulting scores should therefore be interpreted as property- based estimates of model suitability for comparison within the framework, rather than as substitutes for direct empirical measurement."))
- **c6** Scoring each model only against its own paper rewards papers with narrow or dated baselines and penalises papers candid about limitations, which motivated a second audit pass using independent literature.([Case study, p.22](https://arxiv.org/pdf/2609.22154v1#page=22 "scoring each model’s properties against its own publication alone systematically rewards models whose papers compare against a narrow or dated set of baselines, and penalizes models whose papers are comparatively candid about their own limitations"))

