<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# In a Streaming World, Should You Stand Still? A Comprehensive Benchmark of Anomaly Detection in Streams

- カード: [`arxiv-2609.39215`](../../papers/arxiv-2609.39215.yaml)
- 著者: Magali Parrino, Antoine Ajenjo, Emmanuel Remy, Pierre Stephan, Pierre Senellart, Paul Boniol
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.39215v1)(arXiv v1、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, deep-learning, streaming, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Most streaming anomaly detection methods come from streaming outlier detection and largely ignore core characteristics of time-series anomalies; their evaluation is typically on synthetic or small-scale benchmarks.([Abstract, p.1](https://arxiv.org/pdf/2609.39215v1#page=1 "most of these approaches originate from the streaming outlier detection litera- ture and largely ignore core characteristics of time series anomalies."))
- **c2** Contrary to common assumptions, static TSAD methods significantly outperform streaming approaches in most streaming settings.([Abstract, p.1](https://arxiv.org/pdf/2609.39215v1#page=1 "Our results show that, contrary to common assumptions, static TSAD methods significantly outperform streaming approaches in most streaming settings."))
- **c3** AUC-ROC is overly optimistic on imbalanced data, so AUC-PR is used.([Evaluation measures, p.6](https://arxiv.org/pdf/2609.39215v1#page=6 "Consequently, the Area Under the Precision- Recall Curve (AUC-PR) is preferred in this study."))
- **c4** The main limitation of streaming TSAD is its focus on point-wise outliers rather than collective anomalies.([Conclusion, p.9](https://arxiv.org/pdf/2609.39215v1#page=9 "The most significant limitation is the legacy focus on point-wise outliers."))

