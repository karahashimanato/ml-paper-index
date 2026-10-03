<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Time-LLM: Time Series Forecasting by Reprogramming Large Language Models

- カード: [`arxiv-2310.01728`](../../papers/arxiv-2310.01728.yaml)
- 著者: Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xiaoming Shi, Pin-Yu Chen, Yuxuan Liang, Yuan-Fang Li, Shirui Pan, Qingsong Wen
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.01728v2)(arXiv v2、カード作成時に読んだ版)
- タグ: large-language-models, supervised, time-series-forecasting
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: input time series (patched) are reprogrammed with text prototypes before being fed into a frozen LLM; Prompt-as-Prefix adds context and task instructions, and LLM outputs are projected to forecasts.([Abstract, p.1](https://arxiv.org/pdf/2310.01728v2#page=1 "We begin by reprogramming the input time series with text prototypes before feeding it into the frozen LLM to align the two modalities."))
- **c2** Only the parameters of the lightweight input transformation and output projection are updated, while the backbone LLM stays frozen (the paper uses Llama-7B as the default backbone).([Methodology, p.4](https://arxiv.org/pdf/2310.01728v2#page=4 "We note that only the parameters of the lightweight input transformation and output projection are updated, while the backbone language model is frozen."))
- **c3** Main claim: Time-LLM outperforms state-of-the-art specialized forecasting models, and the abstract states it excels in few-shot and zero-shot settings.([Abstract, p.1](https://arxiv.org/pdf/2310.01728v2#page=1 "Our comprehensive evaluations demonstrate that TIME-LLM is a powerful time series learner that outperforms state-of-the-art, specialized forecasting models."))
- **c4** Definition of zero-shot: cross-domain adaptation, i.e. the model is trained (optimized) on one dataset and evaluated on another dataset whose samples it has not seen, using ETT dataset pairs under the long-term forecasting protocol; it is not a pretrained-only setting.([Zero-shot forecasting: Setups, p.8](https://arxiv.org/pdf/2310.01728v2#page=8 "we evaluate the zero-shot learning capabilities of the reprogrammed LLM within the framework of cross-domain adaptation."))
- **c5** Evaluation protocol: configurations follow Wu et al. (2023) with a unified evaluation pipeline, and baseline performance is cited (copied) from Zhou et al. (2023a, GPT4TS) where applicable; which baselines were re-run instead is not stated in the text.([Main results: Baselines, p.6](https://arxiv.org/pdf/2310.01728v2#page=6 "We compare with the SOTA time series models, and we cite their performance from (Zhou et al., 2023a) if applicable."))
- **c6** Long-term forecasting setup: ETTh1/ETTh2/ETTm1/ETTm2, Weather, Electricity, Traffic and ILI, input length 512 and horizons 96-720, metrics MSE and MAE (per Table 1 caption and Table 9, ILI uses horizons 24-60 and input length 96).([Long-term forecasting: Setups, p.6](https://arxiv.org/pdf/2310.01728v2#page=6 "The input time series length T is set as 512, and we use four different prediction horizons H ∈{96, 192, 336, 720}."))
- **c7** Affiliations: authors are from Monash University, Ant Group, IBM Research, Griffith University, Alibaba Group and HKUST (Guangzhou).([Title page, p.1](https://arxiv.org/pdf/2310.01728v2#page=1 "1Monash University 2Ant Group 3IBM Research 4Griffith University 5Alibaba Group"))

