<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Latent Inference-Time Guidance of Time Series Foundation Models

- カード: [`arxiv-2609.38058`](../../papers/arxiv-2609.38058.yaml)
- 著者: Chloé Hashimoto-Cullen, Amaury Durand, Laurent Bozzi, Benjamin Guedj, Yannig Goude, Sylvain Le Corff
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.38058v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-foundation-model, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** LITiG-TSFM combines a pool of TSFM forecasts through a time-dependent latent space with independent components.([Abstract, p.1](https://arxiv.org/pdf/2609.38058v1#page=1 "This paper introduces Latent Inference-Time Guidance for TSFMs, which adaptively combines a pool of TSFM forecasts through a time-dependent latent space with independent components."))
- **c2** Experiments on datasets of various frequencies and domains show the approach is competitive with traditional ensembling.([Abstract, p.1](https://arxiv.org/pdf/2609.38058v1#page=1 "We provide experiments on datasets at various frequencies and from multiple domains: these show that the approach is competitive with traditional ensembling approaches."))
- **c3** The experts are forecasts from a single foundation model, TabICLv2, chosen as representative rather than searched for the best TSFM.([Baselines, p.7](https://arxiv.org/pdf/2609.38058v1#page=7 "Rather than looking to find the best TSFM and its best configuration, we choose TabICLv2 as a representative sample of the current state of the art for TSFMs and use a set of its forecasts."))
- **c4** The best single TSFM forecast is selected on a validation fold and evaluated on the test fold.([Baselines, p.7](https://arxiv.org/pdf/2609.38058v1#page=7 "To replicate implementation conditions where performance is evaluated on a static training dataset to select a model, the best TSFM from the validation fold of the data is retained as the best TSFM, and evaluated on the test fold of the data."))
- **c5** The oracle mixture, which uses ground truth to pick the best expert per step, is reported as a performance floor, not as a baseline to beat.([Baselines, p.7](https://arxiv.org/pdf/2609.38058v1#page=7 "So we use it as a performance floor, rather than a baseline to beat."))
- **c6** Limitation: some assumptions behind the guarantees may be too restrictive for real-life datasets.([Discussion, limitations and conclusion, p.10](https://arxiv.org/pdf/2609.38058v1#page=10 "Furthermore, some of the assumptions made to achieve the results can be too restrictive for a real-life dataset."))

