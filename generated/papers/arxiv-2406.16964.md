<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Are Language Models Actually Useful for Time Series Forecasting?

- カード: [`arxiv-2406.16964`](../../papers/arxiv-2406.16964.yaml)
- 著者: Mingtian Tan, Mike A. Merrill, Vinayak Gupta, Tim Althoff, Thomas Hartvigsen
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2406.16964v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, supervised, time-series-forecasting
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main finding: in ablations of three recent LLM-based forecasters, removing the LLM or replacing it with a basic attention layer does not degrade forecasting performance, and in most cases results improve.([Abstract, p.1](https://arxiv.org/pdf/2406.16964v2#page=1 "In a series of ablation studies on three recent and popular LLM-based time series forecasting methods, we find that removing the LLM component or replacing it with a basic attention layer does not degrade forecasting performance—in most cases, the results even improve!"))
- **c2** Scope: three ablations of three methods (OneFitsAll/GPT4TS, Time-LLM, CALF) on eight standard benchmark datasets used by those methods plus five Monash datasets; metrics MAE and MSE. LLMTime is not among the ablated methods.([Introduction, p.1](https://arxiv.org/pdf/2406.16964v2#page=1 "We substantiate our claim by performing three ablations of three popular and recent LLM-based forecasting methods [49, 14, 21] using eight standard benchmark datasets from reference methods"))
- **c3** Reproduction protocol: the original hyperparameters, runtime environments and code of each method were used, and error metrics from the original papers are shown alongside the replication where possible (Appendix D.2 adds that for the smaller ablations the learning rate or batch size was adjusted in some cases).([Experimental setup: Reproducibility Note, p.3](https://arxiv.org/pdf/2406.16964v2#page=3 "We used the original hyper-parameters, runtime environments, and code, including model architectures, training loops, and data-loaders."))
- **c4** Pretraining test: randomly initializing CALF's language model and training it on time series, versus using pretrained weights (with/without finetuning), led the authors to conclude that textual knowledge from pretraining provides very limited aid for forecasting.([Results: RQ3, p.8](https://arxiv.org/pdf/2406.16964v2#page=8 "In summary, textual knowledge from pretraining provides very limited aids for time series forecasting."))
- **c5** Few-shot test: training on 10% of each dataset, LLMs were not meaningfully useful: for Time-LLM (LLaMA) the LLM version and the w/o LLM ablation each performed better in the same number of cases, and for CALF (GPT-2) the ablations could perform better.([Results: RQ5, p.9](https://arxiv.org/pdf/2406.16964v2#page=9 "In this section, our evaluation demonstrates that LLMs are still not meaningfully useful in few-shot learning scenarios."))
- **c6** Simple alternative: a linear model with an encoder made of patching and attention (PAttn) achieves forecasting performance similar to LLM-based methods.([Introduction, p.2](https://arxiv.org/pdf/2406.16964v2#page=2 "We find that a simple linear model with an encoder composed of patching and attention can achieve forecasting performance similar to that of LLMs."))
- **c7** Stated limitations: only forecasting is evaluated (not classification or question answering), and only evenly spaced time series (not irregular sequences such as payment records).([Appendix: Limitations, p.14](https://arxiv.org/pdf/2406.16964v2#page=14 "Our evaluation is limited to only time-series datasets, i.e., sequences with even time-intervals."))

