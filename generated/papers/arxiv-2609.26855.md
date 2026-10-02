<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# QUARTET: Quad-branch cross-Attention and Random-walk Traces for Enhancing Transformers on Relational Graphs

- カード: [`arxiv-2609.26855`](../../papers/arxiv-2609.26855.yaml)
- 著者: Kyaw Hpone Myint, Nan Jiang, Xiang Li, Zhe Wu, Alexandre G. R. Day, Pranab Mohanty, Giri Iyengar
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.26855v2)(arXiv v2、カード作成時に読んだ版)
- タグ: graph-neural-networks, graph-node-prediction, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** QUARTET is a graph transformer for relational deep learning that uses full self-attention on local subgraphs plus cross-attention branches for global context.([Abstract, p.1](https://arxiv.org/pdf/2609.26855v2#page=1 "we introduce QUARTET, an expressive graph transformer architecture that applies full self-attention on local subgraphs while enriching global context through cross-attention branches"))
- **c2** The abstract claims QUARTET consistently matches or outperforms HGT and RelGT on the RelBench v1 classification tasks.([Abstract, p.1](https://arxiv.org/pdf/2609.26855v2#page=1 "Across the RELBENCH v1 classification tasks, QUARTET consistently matches or outperforms the current state-of-the-art graph transformer baselines (HGT and RelGT)."))
- **c3** The conclusion is more qualified: QUARTET matches or beats RelGT on eight of twelve tasks, and RelGT keeps an edge on a few large, stationary tasks.([Conclusion, p.10](https://arxiv.org/pdf/2609.26855v2#page=10 "matching or outperforming the original RelGT model on eight of twelve tasks and securing top test ROC-AUC on seven"))
- **c4** Evaluation: twelve binary classification tasks from seven RelBench datasets, ROC-AUC, reporting the test score of the model selected on the validation split.([Experimental Setup, p.7](https://arxiv.org/pdf/2609.26855v2#page=7 "We use ROC-AUC as the primary evaluation metric and report test ROC-AUC for the model selected on the validation split."))
- **c5** Baselines HGT and RelGT were reproduced from scratch under the shared RelBench v2 pipeline with the original authors' reported hyperparameters; baselines and QUARTET are averaged over four random seeds.([Experimental Setup, p.7](https://arxiv.org/pdf/2609.26855v2#page=7 "we reproduced both graph-transformer baselines (HGT and RelGT) from scratch under this shared v2 pipeline, utilizing the original authors’ reported hyper-parameters"))
- **c6** Baselines were not re-tuned because the RelBench v2 classification datasets are unchanged except for a leakage patch to one task.([Appendix, p.20](https://arxiv.org/pdf/2609.26855v2#page=20 "Re-tuning was deemed unnecessary because the classification datasets in RELBENCH v2 are unchanged to the prior version, aside from a patch to rel-event user-ignore that resolved temporal leakage."))

