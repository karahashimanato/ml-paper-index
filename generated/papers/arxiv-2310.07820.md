<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Large Language Models Are Zero-Shot Time Series Forecasters

- カード: [`arxiv-2310.07820`](../../papers/arxiv-2310.07820.yaml)
- 著者: Nate Gruver, Marc Finzi, Shikai Qiu, Andrew Gordon Wilson
- 年・掲載: 2023
- 原論文: [PDF](https://arxiv.org/pdf/2310.07820v3)(arXiv v3、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, time-series-forecasting
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: time series are encoded as strings of numerical digits so that forecasting becomes next-token prediction with a pretrained LLM (GPT-3, LLaMA-2); the paper also proposes tokenization and a conversion of token distributions into continuous densities.([Abstract, p.1](https://arxiv.org/pdf/2310.07820v3#page=1 "By encoding time series as a string of numerical digits, we can frame time series forecasting as next-token prediction in text."))
- **c2** Main claim: LLMTime can exceed or match purpose-built time series methods on a range of problems in a zero-shot fashion, where zero-shot means no fine-tuning on the downstream data that the other models are trained on.([Introduction, p.2](https://arxiv.org/pdf/2310.07820v3#page=2 "we find LLMTIME can exceed or match purpose-built time series methods over a range of different problems in a zero-shot fashion, meaning that LLMTIME can be used without any fine-tuning on the downstream data used by other models."))
- **c3** Zero-shot here still involves hyperparameter selection: the rescaling parameters (percentile alpha and offset beta) are tuned on validation log likelihoods; Appendix A builds the validation series from the last observations of the training series and computes the LLM likelihood without training (on some benchmarks, e.g. Monash, fixed hyperparameters are listed instead).([LLMTime: Rescaling, p.4](https://arxiv.org/pdf/2310.07820v3#page=4 "We also experiment with an offset β based calculate as a percentile of the input data, and we tune these two parameters on validation log likelihoods (details in Appendix A)."))
- **c4** Leakage: the authors acknowledge that the LLMs' training data are undisclosed and that memorization or more benign leakage of related data could overestimate generalization; as a direct check they evaluate GPT-3 on three series recorded after its training data cutoff (September 2021).([Appendix: Addressing Memorization Concerns, p.16](https://arxiv.org/pdf/2310.07820v3#page=16 "To further address the memorization concern, we also perform a direct experiment to show GPT-3 also demonstrates strong performance when evaluated on time series recorded after its training data cutoff date, September 2021."))
- **c5** Evaluation protocol (Darts benchmark): baselines (ARIMA, TCN, N-BEATS, N-HiTS from Darts; SM-GP via GPyTorch) are grid-searched over listed hyperparameters, with default values for hyperparameters not listed; the test set is the last 20% of each series.([Appendix: Darts datasets, p.17](https://arxiv.org/pdf/2310.07820v3#page=17 "We use default values for hyperparameters not described below."))
- **c6** Evaluation protocol (Monash): GPT-3 was evaluated on a subset of 19 Monash datasets selected for tractable number of series and context length, and baseline numbers were not re-run but reported as presented in the Monash archive paper (their ref. [19]).([Appendix: Monash datasets, p.18](https://arxiv.org/pdf/2310.07820v3#page=18 "For the baselines, we report their performance as presented in [19]."))
- **c7** Negative finding: GPT-4 can perform worse than GPT-3, which the authors attribute to number tokenization and poor uncertainty calibration likely resulting from alignment interventions such as RLHF (stated as 'likely').([Abstract, p.1](https://arxiv.org/pdf/2310.07820v3#page=1 "we show GPT-4 can perform worse than GPT-3 because of how it tokenizes numbers, and poor uncertainty calibration, which is likely the result of alignment interventions such as RLHF."))

