<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Interpretable Synthetic Medical Tabular Data Generation for Clinical Decision Support Using Fuzzy Cognitive Maps

- カード: [`arxiv-2610.00391`](../../papers/arxiv-2610.00391.yaml)
- 著者: Michael Vasilakakis, Dimitris K. Iakovidis
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2610.00391v1)(arXiv v1、カード作成時に読んだ版)
- タグ: interpretable-models, tabular-data-generation, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper applies Fuzzy Cognitive Maps to synthetic medical tabular data generation with explicit causality and privacy preservation.([Abstract, p.1](https://arxiv.org/pdf/2610.00391v1#page=1 "This paper proposes a novel application of Fuzzy Cognitive Maps (FCMs) in a framework for synthetic medical tabular data generation with explicit causality and privacy preservation."))
- **c2** On UCI medical datasets the method is reported to be competitive under a train-on-synthetic-test-on-real protocol.([Abstract, p.1](https://arxiv.org/pdf/2610.00391v1#page=1 "Experimental evaluation on UCI medical benchmark datasets demonstrates competitive performance under a Train-on-Synthetic-Test-on-Real (TSTR) protocol."))
- **c3** All baselines (Gaussian Copula, CTGAN, TVAE) use their default SDV configurations.([Experimental setup, p.5](https://arxiv.org/pdf/2610.00391v1#page=5 "All baseline models were implemented using their default SDV configurations."))
- **c4** Each dataset uses a single 80/20 train-test split shared across methods.([Experimental setup, p.5](https://arxiv.org/pdf/2610.00391v1#page=5 "For each dataset, a consistent train–test split of 80/20 was applied across all methods."))
- **c5** Models requiring extensive GPU resources were excluded from the comparison.([Experimental setup, p.5](https://arxiv.org/pdf/2610.00391v1#page=5 "Models requiring extensive GPU resources were excluded to maintain consistent experimental conditions."))
- **c6** Gaussian Copula attains marginally higher fidelity in some cases, which the authors say is often accompanied by reduced predictive utility.([Results, p.6](https://arxiv.org/pdf/2610.00391v1#page=6 "Although Gaussian Copula achieves marginally higher fidelity in certain cases, this is often accompanied by reduced predictive utility, whereas the proposed framework maintains a balanced trade-off between realism and downstream task performance."))

