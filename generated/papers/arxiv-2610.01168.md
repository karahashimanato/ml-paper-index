<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability

- カード: [`arxiv-2610.01168`](../../papers/arxiv-2610.01168.yaml)
- 著者: Roberto Stanzione, Jules Barbe, Magali Parrino, Jérémie Fourmann, Paul Boniol
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2610.01168v1)(arXiv v1、カード作成時に読んだ版)
- タグ: classical-outlier-detectors, deep-learning, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Current benchmarks focus on detection accuracy; few evaluate explainability and none provides rich semantic annotations.([Abstract, p.1](https://arxiv.org/pdf/2610.01168v1#page=1 "One of the main reasons for this gap is that current benchmarks primarily focus on detection accuracy, and only few of them evaluate spatial explainability."))
- **c2** SHAD has 215 multivariate high-dimensional series from real distributed cloud storage systems, with per-dimension labels and textual annotations.([Abstract, p.1](https://arxiv.org/pdf/2610.01168v1#page=1 "a fully annotated benchmark composed of 215 multivariate, high-dimensional time series collected from real-world distributed cloud storage systems operated by Scality."))
- **c3** Detection is evaluated with threshold-independent VUS-PR.([Experimental setup, p.7](https://arxiv.org/pdf/2610.01168v1#page=7 "Performance is evaluated using VUS- PR (a robust, threshold-independent metric) with a 25-point buffer"))
- **c4** State-of-the-art detectors are accurate but not perfect; explainability is not solved by existing methods; frozen LLMs cannot correctly interpret anomalies.([Conclusion, p.10](https://arxiv.org/pdf/2610.01168v1#page=10 "(ii) Explanability on SHAD cannot be natively solved with existing TSAD methods, and (iii) frozen LLMs are not able to provide correct interpretations of anomalies."))

