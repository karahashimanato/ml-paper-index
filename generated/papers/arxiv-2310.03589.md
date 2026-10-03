<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TimeGPT-1

- カード: [`arxiv-2310.03589`](../../papers/arxiv-2310.03589.yaml)
- 著者: Azul Garza, Cristian Challu, Max Mergenthaler-Canseco
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.03589v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Pre-training data: TimeGPT was trained on what the authors describe as the largest collection of publicly available time series, over 100 billion data points from domains such as finance, economics, healthcare, weather, IoT, energy, web traffic, sales and transport; the individual datasets are not named in the text.([Training dataset, p.5](https://arxiv.org/pdf/2310.03589v3#page=5 "TimeGPT was trained on, to our knowledge, the largest collection of publicly available time series, collectively encompassing over 100 billion data points."))
- **c2** Zero-shot definition: the test set (over 300 thousand series from finance, web traffic, IoT, weather, demand and electricity) is described as never seen by the model during training; the authors argue a per-series train/test cutoff is not strict enough for a foundation model. The specific test datasets are not named in the text.([Experimental Results, p.5](https://arxiv.org/pdf/2310.03589v3#page=5 "In this section, we explore TimeGPT’s capabilities as a forecasting foundation model by testing it in a large and diverse set of time series that were never seen by the model during training."))
- **c3** Evaluation protocol: only the last forecasting window of each series is evaluated, with frequency-dependent horizons (12 monthly, 1 weekly, 7 daily, 24 hourly); metrics are rMAE and rRMSE relative to Seasonal Naive (both point-error metrics; no probabilistic metric is reported in the results tables).([Experimental Results, p.6](https://arxiv.org/pdf/2310.03589v3#page=6 "The evaluation is performed in the last forecasting window of each time series, varying in length by the sampling frequency."))
- **c4** Baseline protocol: baselines and statistical models are fit per series on the history before the last window, while machine learning and deep learning models are trained as one global model per frequency on all series of the test set; Prophet and ARIMA were excluded for computational cost. How baseline hyperparameters were chosen was not found in the text (the 'hyperparameter exploration' mentioned concerns TimeGPT's own training).([Experimental Results, p.6](https://arxiv.org/pdf/2310.03589v3#page=6 "Some popular models like Prophet [Taylor and Letham, 2018] and ARIMA were excluded from the analysis due to their prohibitive computational requirements and extensive training times."))
- **c5** Main empirical claim: zero-shot TimeGPT outperforms the compared statistical and deep learning models, ranking among the top-3 performers across frequencies.([Zero-shot inference, p.7](https://arxiv.org/pdf/2310.03589v3#page=7 "Remarkably, TimeGPT outperforms a comprehensive collection of battle-tested statistical models and SoTA deep learning approaches, ranking among the top-3 performers across frequencies."))
- **c6** Hedge in the discussion: the authors relate their results to scaling laws and say simpler models might outperform Transformers on smaller datasets, so simpler models might be more fitting when large datasets or compute are limited.([Discussion and Future Research, p.9](https://arxiv.org/pdf/2310.03589v3#page=9 "In situations where there are limitations on the availability of large datasets or computational resources, simpler models might be more fitting."))
- **c7** Affiliation/product disclosure: all authors are at Nixtla, and TimeGPT is offered as a Python SDK and REST API in private beta; the paper is thus a vendor evaluating its own model.([Appendix (Access and early testing), p.12](https://arxiv.org/pdf/2310.03589v3#page=12 "TimeGPT is accessible through both a Python SDK and a REST API endpoint, currently available in private beta."))

