<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# The Universal Classifier for Graph Learning

- カード: [`arxiv-2609.36302`](../../papers/arxiv-2609.36302.yaml)
- 著者: Ben Finkelshtein, André Linhares, Petar Veličković, Bryan Perozzi, Mikhail Galkin
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36302v1)(arXiv v1、カード作成時に読んだ版)
- タグ: graph-neural-networks, graph-node-prediction, in-context-learning
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** UC supports arbitrary feature and class cardinalities and unifies node-, edge- and graph-level objectives under one similarity-based classification objective.([Abstract, p.1](https://arxiv.org/pdf/2609.36302v1#page=1 "In this paper, we introduce the UNIVERSAL CLASSIFIER (UC), which supports arbitrary feature and class cardinalities, unifying node-, edge-, and graph-level objectives under a single similarity-based classification objective."))
- **c2** The pre-training mixture, training code and parameter count are not released; the authors state that no evaluation dataset appears in the pre-training mixture.([Experiments, p.6](https://arxiv.org/pdf/2609.36302v1#page=6 "While organizational policy prevents us from releasing the mixture, our training code, or the parameter count, we state the property on which the validity of our results depends"))
- **c3** A single checkpoint is evaluated without error bars.([Experiments, p.6](https://arxiv.org/pdf/2609.36302v1#page=6 "so we evaluate a single fixed checkpoint and report UC results without error bars"))
- **c4** Node-classification baseline results are sourced from the respective papers; baselines include TS-Mean (Finkelshtein et al., 2025), prior work sharing the first author's name.([Node classification, p.6](https://arxiv.org/pdf/2609.36302v1#page=6 "Baseline results are sourced from the respective papers."))
- **c5** UC consistently outperforms inductive classifiers and TFM-derived baselines on node classification, and in most cases even supervised GNNs trained per graph.([Results, p.8](https://arxiv.org/pdf/2609.36302v1#page=8 "Notably, in most cases, the UC even surpasses supervised GNNs trained separately on each graph end-to-end."))
- **c6** Limitations: memory and inference overhead from 3D tensors; the evaluated checkpoint was pre-trained on node- and edge-level objectives only.([Appendix (Limitations), p.16](https://arxiv.org/pdf/2609.36302v1#page=16 "The evaluated checkpoint was pre-trained on node- and edge-level objectives only; although it already transfers zero-shot to some graph-level targets."))

