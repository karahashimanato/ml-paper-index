<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Benchmarking Attention for Tabular Foundation Models

- カード: [`arxiv-2609.31306`](../../papers/arxiv-2609.31306.yaml)
- 著者: Maximilian Schambach, Clemens Biehl, Sam Thelin
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.31306v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper builds a reproducible benchmark of attention backends (SDPA, FlashAttention-2/3/4, vLLM, SageAttention) for the row/column attention used in tabular in-context learners.([Abstract, p.1](https://arxiv.org/pdf/2609.31306v2#page=1 "we create a reproducible benchmarking setup and study the unique characteristics of tabular attention across several backends"))
- **c2** The best backend differs between column and row attention and depends on hardware and model specifics.([Abstract, p.1](https://arxiv.org/pdf/2609.31306v2#page=1 "We find that the optimal backend choice differs between column and row attention and varies across hardware as well as model specifics"))
- **c3** The benchmark measures isolated kernel latency/throughput and memory on synthetic tabular tensors, not predictive accuracy.([Benchmark setup, p.3](https://arxiv.org/pdf/2609.31306v2#page=3 "measuring latency and memory consumption for isolated kernel throughput on synthetic tabular tensors"))
- **c4** The train-test (context-query) split handled differently by TabPFN/Mitra and ConTextTab is ignored; standard full bidirectional attention is benchmarked instead.([Benchmark setup, p.4](https://arxiv.org/pdf/2609.31306v2#page=4 "Instead, we evaluate standard full bi-directional attention."))
- **c5** Stated limitation: only isolated kernels with synthetic tensors are benchmarked, not end-to-end training or inference; only bfloat16, non-causal attention and batch size 1 are used.([Limitations, p.10](https://arxiv.org/pdf/2609.31306v2#page=10 "Our benchmark focuses on isolated attention kernels with synthetic tensors rather than end-to-end model training or inference"))
- **c6** Two of the authors (SAP SE) are co-authors of ConTextTab, one of the models whose attention pattern is benchmarked; the main head configuration is taken from that model's reference.([References, p.11](https://arxiv.org/pdf/2609.31306v2#page=11 "Marco Spinaci, Marek Polewczyk, Maximilian Schambach, and Sam Thelin."))

