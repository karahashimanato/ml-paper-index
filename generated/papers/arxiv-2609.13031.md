<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Attention Quantization for Tabular Foundation Models

- カード: [`arxiv-2609.13031`](../../papers/arxiv-2609.13031.yaml)
- 著者: Jonas M. Kübler, Benjamin Jäger, Klemens Flöge, Noah Hollmann, Frank Hutter
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.13031v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, model-compression, post-hoc, post-training-quantization, quantization, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Quantization error must be aligned between test rows and training rows; otherwise accuracy drops drastically.([Abstract, p.1](https://arxiv.org/pdf/2609.13031v1#page=1 "We find that it is crucial to align the quantization error in the test rows with the quantization error in the training rows, as otherwise the accuracy drops drastically."))
- **c2** An FP8 attention kernel speeds up attention over 16-bit kernels with no relevant accuracy loss for TabPFN-v3 and TabICLv2 on TabArena and BeyondArena.([Abstract, p.1](https://arxiv.org/pdf/2609.13031v1#page=1 "Our Triton kernel achieves a speedup up to 1.7x over regular 16-bit kernels, and we show that on TabPFN-v3 and TabICLv2 there is no relevant accuracy loss across TabArena and BeyondArena."))
- **c3** Quality is tested on the full 51-dataset TabArena suite (and later BeyondArena), over three TabPFN-v3 preprocessing seeds.([Experiments, p.3](https://arxiv.org/pdf/2609.13031v1#page=3 "We first test the quality impact of our quantization scheme and kernel on TabArena [Erickson et al., 2026], where we run the full suite consisting of 51 datasets."))
- **c4** Degradation is tested with a one-sided sign test under the assumption that post-training quantization can only make the model worse.([Experiments, p.3](https://arxiv.org/pdf/2609.13031v1#page=3 "Following Kübler et al. [2026] we assume that post-training quantization can only make the model worse and use a one-sided sign test."))
- **c5** All authors list Prior Labs as their affiliation; the evaluated models are TabPFN-v3 and TabICLv2; no conflict-of-interest statement was found in the text.([Title page, p.1](https://arxiv.org/pdf/2609.13031v1#page=1 "Correspondence: jonas@priorlabs.ai"))
- **c6** Per the reference list, author Frank Hutter is a co-author of TabArena, the benchmark used for evaluation.([References, p.5](https://arxiv.org/pdf/2609.13031v1#page=5 "Salinas, and Frank Hutter. Tabarena: A living benchmark for machine learning on tabular data."))

