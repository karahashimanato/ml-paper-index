<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Foundation Models for Time Series Analysis: A Tutorial and Survey

- カード: [`arxiv-2403.14735`](../../papers/arxiv-2403.14735.yaml)
- 著者: Yuxuan Liang, Haomin Wen, Yuqi Nie, Yushan Jiang, Ming Jin, Dongjin Song, Shirui Pan, Qingsong Wen
- 年・掲載: 2024
- 原論文: [PDF](https://arxiv.org/pdf/2403.14735v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, large-language-models, self-supervised, supervised, time-series-forecasting, time-series-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Survey scope: a methodology-centric taxonomy of time-series foundation models by model architecture, pre-training technique, adaptation method and data modality, covering standard time series, spatial time series, trajectories and events.([Abstract, p.1](https://arxiv.org/pdf/2403.14735v3#page=1 "To address this gap, our survey adopts a methodology-centric classification, delineating various pivotal elements of time-series FMs, including model architectures, pre-training techniques, adaptation methods, and data modalities."))
- **c2** Two routes to TSFMs are distinguished: repurposing pretrained LLMs for time series, or training a Transformer from scratch on time series.([Model architecture, p.6](https://arxiv.org/pdf/2403.14735v3#page=6 "This includes either repurposing pretrained LLMs for time series to leverage their preexisting sequence modeling strengths [102], or directly using Transformer as a base for TSFMs, training from scratch"))
- **c3** Architecture choice is unsettled: encoder-only, encoder-decoder and decoder-only TSFMs all exist, unlike the trend to decoder-only models in NLP.([Model architecture, p.6](https://arxiv.org/pdf/2403.14735v3#page=6 "The choice of foundation model framework remains debated in the realm of time series analysis, contrasting the trend towards decoder-only models in natural language processing."))
- **c4** Pre-training mechanisms are categorized by learning objective into fully-supervised, self-supervised (generative, contrastive, hybrid) and others; the authors consider self-supervised pre-training more generic and realistic than fully-supervised pre-training.([Pre-training, p.7](https://arxiv.org/pdf/2403.14735v3#page=7 "Compared with fully-supervised pre-training, it provides a more generic and realistic solution for the acquisition of a time series foundation model."))
- **c5** On zero-shot (direct) usage, the survey notes that good zero-shot performance can also indicate homogeneity between the pre-training data and the target data, especially for domain-specific foundation models.([Adaptation, p.8](https://arxiv.org/pdf/2403.14735v3#page=8 "It can also indicate the homogeneity between the pre-trained dataset and target dataset, especially for some real-world applications where a foundation model is built to fulfill domain-specific tasks [4, 13]."))

