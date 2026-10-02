<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Tabular Foundation Models for Multi-View Information Cascade Popularity Prediction

- カード: [`arxiv-2608.25048`](../../papers/arxiv-2608.25048.yaml)
- 著者: Wenting Zhu, Chenghua Gong, Sanchuan Guo, Chaozhuo Li, Yueyue Zhang, Xi Zhang
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.25048v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, in-context-learning, supervised, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TFM4POP is proposed as the first framework to bring tabular foundation models into cascade popularity prediction, using their pre-trained priors to model multiple heterogeneous information views jointly.([Abstract, p.1](https://arxiv.org/pdf/2608.25048v1#page=1 "we propose TFM4POP, the first framework to introduce tabular foundation models (TFMs) into popularity prediction, leveraging their pre-trained tabular priors to unify the modeling of multiple heterogeneous information views."))
- **c2** In the authors' experiments TFM4POP consistently outperforms state-of-the-art baselines across datasets and observation settings.([Abstract, p.1](https://arxiv.org/pdf/2608.25048v1#page=1 "Extensive experiments show that TFM4POP consistently outperforms state-of-the-art baselines across multiple datasets and observation settings."))
- **c3** Evaluation uses two real-world datasets, Twitter (from MMCas) and EventCas, which the authors built themselves from Sina Weibo.([Evaluation datasets, p.6](https://arxiv.org/pdf/2608.25048v1#page=6 "We conduct experiments on two real-world datasets: Twitter and EventCas."))
- **c4** The main comparison repeats every experiment with five random seeds and reports mean and standard deviation.([Experimental settings, p.7](https://arxiv.org/pdf/2608.25048v1#page=7 "All experiments are repeated five times with different random seeds, and we report the mean and standard deviation."))
- **c5** In the ablation, replacing the TabPFN backbone with a parameter-matched MLP over the same static input degrades performance the most of all variants.([Ablation study, p.8](https://arxiv.org/pdf/2608.25048v1#page=8 "replacing the TFM backbone with a parameter-matched MLP causes the largest degradation among all variants"))
- **c6** In the ablation, IA3 adaptation of the backbone outperforms full fine-tuning, LoRA and the frozen backbone.([Ablation study, p.8](https://arxiv.org/pdf/2608.25048v1#page=8 "IA3 outperforms full fine-tuning, LoRA, and the frozen backbone"))

