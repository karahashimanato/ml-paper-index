<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Adapting Linear-Time Architectures for Tabular In-Context Learning

- カード: [`arxiv-2609.36337`](../../papers/arxiv-2609.36337.yaml)
- 著者: David Schnurr, Felix Sarnthein, Thomas Hofmann, Imanol Schlag
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.36337v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Reading out from the final recurrent state (re-introducing non-causality) lets the linear-time model closely match a controlled softmax-attention baseline on OpenML-CC18 and TabArena.([Abstract, p.1](https://arxiv.org/pdf/2609.36337v1#page=1 "Finally, re-introducing non-causality by reading out from the final state allows us to closely match a controlled softmax attention baseline on OpenML-CC18 and TabArena."))
- **c2** DeltaNet degrades beyond roughly 2-4x the pretraining context length, and existing mitigations such as bidirectionality only defer the problem.([Abstract, p.1](https://arxiv.org/pdf/2609.36337v1#page=1 "However, it degrades beyond 2-4× the pretraining context length, and existing mitigation strategies such as bidirectionality defer the problem at best."))
- **c3** Evaluation protocol: datasets are preprocessed (feature cap; OpenML-CC18 subsampled to the pretraining size), while TabArena is used to measure length generalisation on larger datasets.([Experimental setup, p.4](https://arxiv.org/pdf/2609.36337v1#page=4 "OpenML-CC18 is further subsampled to at most n = 1000 samples to match the pretraining size, while TabArena measures real-world length generalisation on larger datasets."))
- **c4** External foundation-model baselines (TabPFN v2.5, TabICLv2, TabFlex) are the released checkpoints and are not controlled for training budget or model size.([Appendix, p.17](https://arxiv.org/pdf/2609.36337v1#page=17 "Importantly, these baselines are not controlled for training budget or model size: we evaluate the models released by their respective authors."))
- **c5** CatBoost is used untuned, as a default-configuration baseline, justified by the TabArena finding that it performs well out of the box.([Appendix, p.17](https://arxiv.org/pdf/2609.36337v1#page=17 "As shown in the TabArena evaluation by Erickson et al. (2026), CatBoost performs very well out of the box without hyperparameter tuning, supporting its use as a default configuration baseline."))
- **c6** Limitation: the study prioritises a controlled comparison over absolute performance; larger pretraining budgets and further tuning may disproportionately improve performance.([Limitations, p.10](https://arxiv.org/pdf/2609.36337v1#page=10 "Larger pretraining budgets and further tuning may disproportionately improve performance."))

