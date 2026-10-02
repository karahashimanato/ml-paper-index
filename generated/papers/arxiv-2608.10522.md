<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Unlocking the Power of Medical Tabular Data via Semantic-Aware Multimodal Pre-training

- カード: [`arxiv-2608.10522`](../../papers/arxiv-2608.10522.yaml)
- 著者: Yingsheng Liu, Haiming Li, Jingmin Zhu, Jiajun Sun, Victoria Mar, Monika Janda, H. Peter Soyer, Zongyuan Ge, Zhen Yu
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.10522v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, tabular-attention, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes a semantic-aware multimodal pre-training framework that explicitly models the two-dimensional structure of medical tabular data.([Abstract, p.1](https://arxiv.org/pdf/2608.10522v1#page=1 "To overcome this, we propose a novel semantic-aware framework explicitly modeling the intrinsic two-dimensional structure of tabular data."))
- **c2** Experiments on dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets are reported as establishing a new state of the art.([Abstract, p.1](https://arxiv.org/pdf/2608.10522v1#page=1 "Extensive experiments across large-scale dermatology (SLICE-3D, HOP) and ophthalmology (EyePACS) datasets establish a new state-of-the-art (SOTA), demonstrating exceptional robustness and cross-domain generalizability."))
- **c3** Label-free feature importance is obtained by fitting a frozen tabular foundation model (TabPFN v2) to PCA-derived binary pseudo-labels and reading its attention weights.([Methodology, p.4](https://arxiv.org/pdf/2608.10522v1#page=4 "These pseudo-labels adapt a frozen tabular foundation model[12]."))
- **c4** On SLICE-3D, samples from 220 patients are geographically held out as an out-of-domain test set and excluded from pre-training.([Experimental setup, p.6](https://arxiv.org/pdf/2608.10522v1#page=6 "To ensure rigorous evaluation, 80,433 samples from 220 patients are geographically isolated as an Out-of-Domain (OOD) test set and strictly excluded from pre-training."))
- **c5** Baselines (including CatBoost, FT-Transformer and TabPFN v2) are stated to be reproduced under identical settings; no baseline hyperparameter-tuning procedure was found in the text.([Main results, p.7](https://arxiv.org/pdf/2608.10522v1#page=7 "As presented in Table 1, all baseline experiments were rigorously reproduced under identical experimental settings."))
- **c6** The proposed method's hyperparameters were set empirically through validation experiments.([Experimental setup, p.7](https://arxiv.org/pdf/2608.10522v1#page=7 "All hyperparameter settings were empirically established through extensive validation experiments."))

