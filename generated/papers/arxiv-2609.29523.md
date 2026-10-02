<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Towards Trustworthy Biological Alignment in TabPFN-Probed Pathology Foundation Models

- カード: [`arxiv-2609.29523`](../../papers/arxiv-2609.29523.yaml)
- 著者: Ushashi Bhattacharjee, Alloy Das, Saria Hannan, Tirtho Roy, Koushik Howlader, Soumik Sarkar
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.29523v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, in-context-learning, linear-models, supervised, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper presents a training-free framework for auditing biological alignment in frozen pathology foundation models, using spatially paired histology and transcriptomics from HEST-1k (240 samples, 3 organs).([Abstract, p.1](https://arxiv.org/pdf/2609.29523v1#page=1 "We present a training-free framework for auditing biological alignment in frozen PFMs using spatially paired histology and transcriptomics from HEST-1k, evaluated on 240 samples spanning 3 organs."))
- **c2** TabPFN is used as a pretrained probe to measure how well molecular programs can be decoded from frozen embeddings without task-specific gradient updates.([Abstract, p.1](https://arxiv.org/pdf/2609.29523v1#page=1 "TabPFN serves as a pretrained probe to measure how well these molecular programs can be decoded without task-specific gradient updates."))
- **c3** The protocol uses specimen-level grouping with five-fold specimen-level cross-validation and three fixed seeds, reporting mean per-target Pearson correlation.([Method (leakage-safe protocol), p.4](https://arxiv.org/pdf/2609.29523v1#page=4 "Five-fold specimen-level cross-validation with three fixed seeds; we report mean per-target Pearson correlation (PCC)."))
- **c4** Baseline probes (mean, kNN, Ridge and a gradient-trained MLP with one fixed configuration) are run on identical folds and context. No hyperparameter search for the baselines was found in the text.([Method (baselines), p.4](https://arxiv.org/pdf/2609.29523v1#page=4 "Beyond TabPFN we run mean, kNN (cosine, distance-weighted), Ridge, and a gradient-trained MLP"))
- **c5** With the UNI encoder fixed, the training-free probes outperform the gradient-trained MLP.([Results (label efficiency), p.5](https://arxiv.org/pdf/2609.29523v1#page=5 "The training-free probes outperform the gradient-trained MLP"))
- **c6** Limitation: TabPFN is the primary probe family, and absolute PCC and especially label efficiency may remain probe-specific.([Limitations and Outlook, p.7](https://arxiv.org/pdf/2609.29523v1#page=7 "but absolute PCC and especially label efficiency can remain probe-specific."))

