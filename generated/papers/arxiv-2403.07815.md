<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Chronos: Learning the Language of Time Series

- カード: [`arxiv-2403.07815`](../../papers/arxiv-2403.07815.yaml)
- 著者: Abdul Fatir Ansari, Lorenzo Stella, Caner Turkmen, Xiyuan Zhang, Pedro Mercado, Huibin Shen, Oleksandr Shchur, Syama Sundar Rangapuram, Sebastian Pineda Arango, Shubham Kapoor, Jasper Zschiegner, Danielle C. Maddix, Hao Wang, Michael W. Mahoney, Kari Torkkola, Andrew Gordon Wilson, Michael Bohlke-Schneider, Yuyang Wang
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2403.07815v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: Chronos scales and quantizes time series values into a fixed vocabulary and trains existing transformer language-model architectures on these tokens with the cross-entropy loss.([Abstract, p.1](https://arxiv.org/pdf/2403.07815v3#page=1 "Chronos tokenizes time series values using scaling and quantization into a fixed vocabulary and trains existing transformer-based language model architectures on these tokenized time series via the cross-entropy loss."))
- **c2** Zero-shot definition: datasets are split into pretraining-only (13), Benchmark I (15; used for both training and in-domain evaluation) and Benchmark II (27; used only for evaluation, i.e. zero-shot).([Datasets, p.9](https://arxiv.org/pdf/2403.07815v3#page=9 "(b) Benchmark I datasets, employed for both training and evaluation, representing an in-domain evaluation (15 datasets); and (c) Bench-mark II datasets, used solely for evaluation, constituting a zero-shot evaluation (27 datasets)."))
- **c3** Leakage caveat (footnote): the authors acknowledge that strictly preventing leakage would require Benchmark II data to start after the last pretraining observation, but they consider the risk minimal because the datasets share no overlap beyond high-level conceptual categorization.([Results (Benchmark II footnote), p.12](https://arxiv.org/pdf/2403.07815v3#page=12 "From a rigorous standpoint, to prevent information leakage, the start time of any dataset within this category must be after the timestamp of the last observation from the pretraining dataset and Benchmark I."))
- **c4** Evaluation protocol: probabilistic forecasts are scored with WQL on 9 quantile levels and point forecasts with MASE (median forecast); per-dataset scores are divided by Seasonal Naive and aggregated with a geometric mean, and failed/timed-out models get relative score 1.([Evaluation Metrics, p.10](https://arxiv.org/pdf/2403.07815v3#page=10 "For each dataset, we compute the relative score of each model as the model’s score divided by the score of a baseline model (here, Seasonal Naive)."))
- **c5** Baseline tuning: statistical baselines used StatsForecast defaults (with frequency-implied season lengths), and unless otherwise specified baseline implementations kept their default hyperparameters with no dataset-specific or global hyperparameter tuning.([Appendix (Baselines), p.34](https://arxiv.org/pdf/2403.07815v3#page=34 "Unless otherwise specified, the default hyperparameter configurations provided in baseline implementations were kept as is, and no dataset specific or global hyperparameter tuning was performed."))
- **c6** Cross-model leakage remark: the authors note that the evaluation setup may have favored Moirai-1.0-R on Benchmark II because many Benchmark II datasets were in Moirai's pretraining corpus.([Results (Benchmark II), p.12](https://arxiv.org/pdf/2403.07815v3#page=12 "Moirai-1.0-R obtains the best performance after Chronos, although the evaluation setup may have been advantageous for Moirai-1.0-R as many datasets in Benchmark II were part of its pretraining corpus."))
- **c7** Affiliation: the title page lists AWS AI Labs and Amazon Supply Chain Optimization Technologies (some authors also list universities; two contributed as AWS interns), and the footnote states that three authors hold concurrent Amazon/university appointments and that the paper describes work performed at Amazon.([Title page (footnote), p.1](https://arxiv.org/pdf/2403.07815v3#page=1 "Hao Wang, Michael W. Mahoney, and Andrew Gordon Wilson hold concurrent appointments at Amazon and their corresponding universities, and this paper describes work performed at Amazon."))

