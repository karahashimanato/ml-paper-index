<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning

- カード: [`arxiv-2608.27882`](../../papers/arxiv-2608.27882.yaml)
- 著者: Hao Wang, Siyu Zhang, Wei Ma
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2608.27882v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** SOMTab is a Set-Order Mamba architecture for efficient tabular in-context learning.([Abstract, p.1](https://arxiv.org/pdf/2608.27882v1#page=1 "We introduce SOMTab, a Set-Order Mamba architecture for efficient tabular in-context learning."))
- **c2** Across tabular benchmarks, SOMTab approaches strong Transformer-based TFMs while achieving faster inference and lower GPU memory.([Abstract, p.1](https://arxiv.org/pdf/2608.27882v1#page=1 "Across tabular benchmarks, SOMTab approaches the performance of strong Transformer-based tabular foundation models while achieving faster inference and lower GPU memory usage"))
- **c3** The main evaluation covers all TALENT classification datasets using the official splits (train+validation as context, official test split).([Experimental setup, p.7](https://arxiv.org/pdf/2608.27882v1#page=7 "We evaluate SOMTab on all classification datasets in the TALENT benchmark (Ye et al., 2024)."))
- **c4** Each baseline uses its official implementation and default configuration, including default preprocessing and ensemble size.([Experimental setup, p.7](https://arxiv.org/pdf/2608.27882v1#page=7 "For each baseline, we use its official implementation and default configuration, including the default preprocessing and ensemble size."))
- **c5** TabArena results are contextual only: public TabArena baselines keep their original H100 runs while SOMTab is measured on A100/H200.([Results, p.8](https://arxiv.org/pdf/2608.27882v1#page=8 "Because the public TabArena baselines retain their original H100 configurations while SOMTab is measured on A100 and H200 GPUs, the runtime comparison provides contextual positioning rather than a hardware-matched speed ranking."))
- **c6** Ablations are run on 15 TALENT datasets selected because SOMTab performs relatively less favorably than TabICLv2 on them in the main benchmark.([Ablation studies, p.9](https://arxiv.org/pdf/2608.27882v1#page=9 "To better reveal differences between variants, we evaluate them on 15 TALENT datasets where SOMTab performs relatively less favorably than TabICLv2 in the main benchmark."))

