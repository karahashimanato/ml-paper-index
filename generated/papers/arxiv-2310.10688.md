<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A decoder-only foundation model for time-series forecasting

- カード: [`arxiv-2310.10688`](../../papers/arxiv-2310.10688.yaml)
- 著者: Abhimanyu Das, Weihao Kong, Rajat Sen, Yichen Zhou
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.10688v4)(arXiv v4、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: TimesFM pretrains a decoder-style attention model with input patching on a large corpus of real-world and synthetic time series.([Abstract, p.1](https://arxiv.org/pdf/2310.10688v4#page=1 "Our model is based on pretraining a decoder style attention model with input patching, using a large time-series corpus comprising both real-world and synthetic datasets."))
- **c2** Pretraining data: the bulk comes from Google Trends, Wiki Pageviews and synthetic series; M4, hourly/15-min Electricity, hourly Traffic and the 10-minute Weather dataset of the Informer benchmark were also added.([Pretraining Details, p.5](https://arxiv.org/pdf/2310.10688v4#page=5 "We address this problem by sourcing the bulk of data used to train our models from three major sources: Google trends, Wiki Pageview statistics and synthetic time-series."))
- **c3** Zero-shot definition: the evaluation dataset groups (Monash, Darts, Informer/ETT) were intentionally held out from pretraining; from the Informer collection only the ETT datasets are used because a few others were used in pretraining.([Empirical Results, p.6](https://arxiv.org/pdf/2310.10688v4#page=6 "These datasets have been intentionally held out from our pretraining data."))
- **c4** Evaluation protocol: Monash is filtered (following llmtime) to 18 datasets without missing values, scored by MAE scaled by a naive last-value baseline and aggregated with a geometric mean; ETT uses horizons 96 and 192 with context 512 and, following llmtime, only the last test window.([Zero-shot Evaluation, p.7](https://arxiv.org/pdf/2310.10688v4#page=7 "Therefore, following llmtime, we compare all methods on the last test window."))
- **c5** Contamination remark about a baseline: for the Darts datasets the authors state that data contamination for llmtime (GPT-3) cannot be ruled out, and that ARIMA needed manual seasonality tuning.([Zero-shot Evaluation, p.7](https://arxiv.org/pdf/2310.10688v4#page=7 "Further, since these datasets are used in numerous time series blog posts for illustrative purposes, data contamination for llmtime cannot be ruled out."))
- **c6** Ablation finding: a PatchTST pretrained on the same data loader to the same FLOPS (PatchTST(ZS)) did not do as well on Monash but performed similarly to TimesFM(ZS) and PatchTST on ETT; the authors call both outcomes expected, citing the pretraining loader's predominant context length of 512 (vs shorter Monash contexts, plus fewer PatchTST iterations at equal FLOPS) and the 512 context used on ETT.([Appendix (Pretraining PatchTST), p.14](https://arxiv.org/pdf/2310.10688v4#page=14 "On ETT datasets, the PatchTST(ZS) model is performs similarly to TimesFM(ZS) and PatchTST."))
- **c7** Affiliation: the title page lists all four authors under Google Research (Google Trends, one of the main pretraining sources, is covered in c2).([Title page, p.1](https://arxiv.org/pdf/2310.10688v4#page=1 "Google Research"))

