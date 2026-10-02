<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Agentic Search Spaces for Tabular Machine Learning

- カード: [`arxiv-2609.16309`](../../papers/arxiv-2609.16309.yaml)
- 著者: Renat Sergazinov, Artem Chistyakov, Sergey Pankevich, Artem Babenko
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.16309v1)(arXiv v1、カード作成時に読んだ版)
- タグ: gradient-boosted-trees, large-language-models, supervised, tabular-classification, tabular-foundation-model, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The agent-enlarged search spaces outperform the base spaces under the same tuning and ensembling budgets, i.e. at no extra tuning cost.([Abstract, p.1](https://arxiv.org/pdf/2609.16309v1#page=1 "Notably, these gains come at no extra tuning cost: the enlarged spaces outperform the base under the same tuning and ensembling budgets."))
- **c2** Tuning uses TPE with 200 trials on small and medium datasets and 100 on large ones; the best-validation configuration is evaluated on the test subset with 15 seeds.([Experimental setup, p.4](https://arxiv.org/pdf/2609.16309v1#page=4 "the budget is 200 trials on small and medium datasets and 100 on the large ones (Microsoft and TabReD), after which the configuration with the best validation score is evaluated on the held-out test subset with 15 random seeds"))
- **c3** TabICLv2 is the exception: the base model is used untuned as published, while its agentic variant is tuned with 100 trials.([Experimental setup, p.4](https://arxiv.org/pdf/2609.16309v1#page=4 "TabICLv2 is the exception: the default model is used as published, without tuning, while its agentic variant is tuned with a fixed budget of 100 trials on every dataset."))
- **c4** The 45 datasets are drawn from the TabM, TabArena and TabReD benchmarks, from 768 to over 1M rows and 5 to over 1500 features.([Experimental setup, p.3](https://arxiv.org/pdf/2609.16309v1#page=3 "We use datasets derived from TabM [2], TabArena [8], and TabReD [7] benchmarks, which span both regression and classification datasets ranging from 768 to 1M+ objects and from 5 to 1500+ features."))
- **c5** Larger search spaces can overfit the validation set.([Limitations, p.10](https://arxiv.org/pdf/2609.16309v1#page=10 "Larger spaces can overfit validation."))
- **c6** Co-author Artem Babenko is an author of TabM, one of the evaluated model families (per the reference list).([References, p.11](https://arxiv.org/pdf/2609.16309v1#page=11 "Yury Gorishniy, Akim Kotelnikov, and Artem Babenko."))

