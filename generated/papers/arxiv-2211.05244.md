<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Deep Learning for Time Series Anomaly Detection: A Survey

- カード: [`arxiv-2211.05244`](../../papers/arxiv-2211.05244.yaml)
- 著者: Zahra Zamanzadeh Darban, Geoffrey I. Webb, Shirui Pan, Charu C. Aggarwal, Mahsa Salehi
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2211.05244v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, forecasting-based-detectors, reconstruction-based-detectors, time-series-anomaly-detection, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Deep TSAD models are classified into four categories: forecasting-based, reconstruction-based, representation-based and hybrid.([Introduction (contributions), p.2](https://arxiv.org/pdf/2211.05244v3#page=2 "These models are broadly classified into four categories: forecasting-based, reconstruction-based, representation-based and hybrid methods."))
- **c2** 64 recent deep models are discussed and categorized.([Discussion and conclusion, p.28](https://arxiv.org/pdf/2211.05244v3#page=28 "64 recent deep models were comprehensively discussed and categorised."))
- **c3** Real-world time series are non-stationary, so deep models need online or incremental training.([Discussion and conclusion, p.27](https://arxiv.org/pdf/2211.05244v3#page=27 "This non-stationary nature necessitates the adaptation of deep learning models through online or incremental training approaches"))
- **c4** Without labeled anomalies, many normal instances are flagged; reducing false positives is a key challenge.([Discussion and conclusion, p.27](https://arxiv.org/pdf/2211.05244v3#page=27 "one of the key challenges is to find a mechanism for minimising false positives and improve recall rates of detection."))
- **c5** Research focuses on detection precision and neglects interpretability, which diagnostics require.([Discussion and conclusion, p.28](https://arxiv.org/pdf/2211.05244v3#page=28 "anomaly detection research focuses primarily on detection precision, failing to address the issue of interpretability."))
- **c6** Multivariate high-dimensional series are particularly challenging (sparsity, temporal and inter-dimension dependencies).([Discussion and conclusion, p.27](https://arxiv.org/pdf/2211.05244v3#page=27 "The detection of anomalies in multivariate high-dimensional time series data presents a particular challenge"))
- **c7** Models are vulnerable to noise in the input data.([Discussion and conclusion, p.27](https://arxiv.org/pdf/2211.05244v3#page=27 "models are vulnerable, and their performance is compromised by noise in the input data."))
- **c8** The anomaly score is mostly defined from a loss function (e.g. reconstruction error).([Deep anomaly detection methods, p.9](https://arxiv.org/pdf/2211.05244v3#page=9 "An anomaly score is mostly defined based on a loss function."))

