<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Toto: Time Series Optimized Transformer for Observability

- カード: [`arxiv-2407.07874`](../../papers/arxiv-2407.07874.yaml)
- 著者: Ben Cohen, Emaad Khwaja, Kan Wang, Charles Masson, Elise Ramé, Youssef Doubli, Othmane Abou-Amal
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2407.07874v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Pre-training data: Toto was trained on about one trillion time series points, of which 75% are anonymous observability metrics from the Datadog platform, alongside publicly available time series datasets.([Abstract, p.1](https://arxiv.org/pdf/2407.07874v2#page=1 "Alongside publicly available time series datasets, 75% of the data used to train Toto consists of fully anonymous numerical metric data points from the Datadog platform."))
- **c2** The training-data section says the non-Datadog points come from the LOTSA collection; a later subsection adds synthetic data (generated similarly to TimesFM) at approximately 5% of the training dataset. Whether the LSF evaluation datasets were excluded from the LOTSA portion is not stated in the text (searched for leakage, overlap, exclusion, held-out: not found).([Training data, p.7](https://arxiv.org/pdf/2407.07874v2#page=7 "The remaining points come from the LOTSA dataset [15], a compilation of publicly-available time series datasets across many different domains."))
- **c3** Architecture: Toto is a decoder-only forecasting model that uses causal next-patch prediction, techniques from recent LLM architectures (pre-normalization, RMSNorm, SwiGLU feed-forward layers), and a novel adaptation of multi-head attention to multivariate time series.([Model architecture, p.5](https://arxiv.org/pdf/2407.07874v2#page=5 "Toto is a decoder-only forecasting model."))
- **c4** LSF evaluation protocol: ETTh1, ETTh2, ETTm1, ETTm2, Electricity and Weather with horizons 96 to 720 in sliding windows of stride 512, context 512, median of 200 samples, normalized MAE/MSE.([Experiments (LSF benchmark), p.9](https://arxiv.org/pdf/2407.07874v2#page=9 "We evaluate with forecast lengths of 96, 192, 336, and 720 time steps, in sliding windows with stride 512, and average the results."))
- **c5** Baselines on LSF are not rerun: Toto is compared with results reported in the Moirai and TimesFM papers for zero-shot foundation models and with reported results for full-shot models.([Experiments (LSF benchmark), p.9](https://arxiv.org/pdf/2407.07874v2#page=9 "We compared Toto's performance with the reported results of other recent zero-shot foundation models [15, 19], as well as full-shot time series forecasting models [14, 16, 17, 36, 44–47]."))
- **c6** Datadog benchmark: on an in-house benchmark of 82 multivariate observability series (sMAPE, sMdAPE; other foundation models run with the sampling procedures from their papers), the authors suggest that open datasets may not provide sufficient information for observability data, highlighting training on more relevant data.([Experiments (Datadog benchmark), p.10](https://arxiv.org/pdf/2407.07874v2#page=10 "These results suggest that current open datasets may not provide suﬃcient information to extrapolate to the speciﬁc nuances of observability data, highlighting the importance of training on more relevant data as demonstrated by Toto's superior performance."))
- **c7** Affiliation/conflict of interest: this is a Datadog technical report (all authors at datadoghq.com) evaluating Datadog's own model, partly on a benchmark built from Datadog data.([Introduction, p.2](https://arxiv.org/pdf/2407.07874v2#page=2 "We present Toto, a groundbreaking time series forecasting foundation model developed by Datadog."))

