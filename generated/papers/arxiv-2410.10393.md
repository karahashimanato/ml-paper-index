<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation

- カード: [`arxiv-2410.10393`](../../papers/arxiv-2410.10393.yaml)
- 著者: Taha Aksu, Gerald Woo, Juncheng Liu, Xu Liu, Chenghao Liu, Silvio Savarese, Caiming Xiong, Doyen Sahoo
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2410.10393v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, linear-models, self-supervised, supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** GIFT-Eval's train/test component has 23 datasets (over 144,000 series, 177 million points) across seven domains, 10 frequencies, univariate and multivariate inputs, and short to long horizons; results are aggregated over 97 dataset/frequency/horizon configurations with MAPE and CRPS normalized by Seasonal Naive plus an average CRPS rank.([Abstract, p.1](https://arxiv.org/pdf/2410.10393v2#page=1 "GIFT-Eval encompasses 23 datasets over 144,000 time series and 177 million data points, spanning seven domains, 10 frequencies, multivariate inputs, and prediction lengths ranging from short to long-term forecasts."))
- **c2** The benchmark also provides a pretraining corpus (71 univariate and 17 multivariate datasets) stated to have no leakage into the train/test split, so that foundation models pretrained on it can be fairly evaluated.([Benchmark (Pretraining data), p.6](https://arxiv.org/pdf/2410.10393v2#page=6 "Notably this collection of data has no leakage issue with the train/test split and can be used to pretrain foundation models that can be fairly evaluated on GIFT-Eval."))
- **c3** Leakage: the pretraining sets of public TimesFM, Chronos and Moirai partially overlap with GIFT-Eval; the authors retrained Moirai on the non-leaking split for the main tables and compared it with the original Moirai, finding that in most cases leakage can boost test performance, more so at longer horizons, which they read as memorization.([Appendix (Data leakage effect in foundation models), p.21](https://arxiv.org/pdf/2410.10393v2#page=21 "In most cases, data leakage from training sets can boost performance on the corresponding test sets, with this effect becoming more pronounced as prediction length increases."))
- **c4** Tuning asymmetry: deep learning baselines are tuned with 15 trials per model for each of the 97 runs (validation = last training window), whereas foundation models are evaluated zero-shot on the test split, with TimesFM and VisionTS settings taken from their papers/defaults, a context-length search for Moirai, and a seasonality search on validation data for VisionTS (see notes on which Moirai checkpoints are used).([Appendix (Deep learning models), p.16](https://arxiv.org/pdf/2410.10393v2#page=16 "We search for 15 trials for each deep learning model per each of the 97 runs."))
- **c5** Overall result: PatchTST has the top average scores in all metrics, with MoiraiLarge second; by best/second-best counts Crossformer is most often best and MoiraiLarge most often in the top 2.([Results (Overall), p.9](https://arxiv.org/pdf/2410.10393v2#page=9 "PatchTST emerges as the most dominant model, securing the top average scores in all metrics, with MoiraiLarge consistently following in second place."))
- **c6** Foundation models (particularly Moirai variants) lead on short horizons (and, in the separate frequency analysis, on daily to yearly data), but TimesFM and Chronos decline at medium/long horizons (attributed to recursive decoding error accumulation) and deep models such as PatchTST do better there; the authors also report that GIFT-Eval does not consistently support scaling laws for TSFMs.([Results (Prediction length), p.8](https://arxiv.org/pdf/2410.10393v2#page=8 "Thus despite the progress in foundational time series research, there remains a notable performance gap between deep learning and foundation models for medium to long-term predictions,"))
- **c7** Affiliation: authors are at Salesforce AI Research (and NUS); the paper's own reference for Moirai lists Woo, C. Liu, Kumar, Xiong, Savarese and Sahoo, five of whom are GIFT-Eval authors, i.e. the benchmark authors overlap with the authors of one of the evaluated models (no explicit conflict-of-interest statement found).([References, p.15](https://arxiv.org/pdf/2410.10393v2#page=15 "Gerald Woo, Chenghao Liu, Akshat Kumar, Caiming Xiong, Silvio Savarese, and Doyen Sahoo."))

