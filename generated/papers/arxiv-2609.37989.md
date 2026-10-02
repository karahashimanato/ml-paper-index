<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models

- カード: [`arxiv-2609.37989`](../../papers/arxiv-2609.37989.yaml)
- 著者: Deqing Fu, Huangyuan Su, Rajat Sen, Taman Narayan, Sujay Sanghavi, Abhimanyu Das, Weihao Kong
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.37989v1)(arXiv v1、カード作成時に読んだ版)
- タグ: automl-systems, in-context-learning, large-language-models, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** TabFM-Auto pairs the TabFM foundation model with a language-model agent that evolves the data pipeline around it.([Abstract, p.1](https://arxiv.org/pdf/2609.37989v1#page=1 "We introduce TabFM-Auto, which pairs a tabular foundation model, TabFM, with a language model agent that evolves the data pipeline around it."))
- **c2** On all 51 TabArena datasets, five TabFM-Auto configurations take the top five overall positions.([Abstract, p.1](https://arxiv.org/pdf/2609.37989v1#page=1 "Across all 51 datasets of the TabArena benchmark, five TabFM-Auto configurations with different agents and language models take the top five overall positions, and the best raises TabFM from 1785 to 2013 Elo."))
- **c3** Pipeline search runs once per dataset with 3-fold cross-validation on fold 0's training set (up to 96 evaluations or 6 hours), withholding evaluation labels; the frozen pipeline is then evaluated on all folds.([Experimental setup, p.5](https://arxiv.org/pdf/2609.37989v1#page=5 "Thus, we run pipeline search once per dataset using 3-fold cross-validation on the training set of fold 0 (up to 96 evaluations or 6 hours on one H100 GPU), allowing both inductive and transductive features while withholding evaluation labels."))
- **c4** The paper also reports a leaderboard on fold 0's held-out test split alone, where TabFM-Auto still holds the top overall, classification and regression ratings.([Results, p.8](https://arxiv.org/pdf/2609.37989v1#page=8 "On the held-out test split of fold 0 alone (Table 5), TabFM-Auto also holds the #1 Overall, Classification, and Regression Elo ratings (Appendix B.1)."))
- **c5** Candidate pipelines run in a sandbox without outbound network access and with restricted writes.([Appendix, p.16](https://arxiv.org/pdf/2609.37989v1#page=16 "The harness runs every candidate pipeline in an unprivileged bubblewrap Linux namespace sandbox that disables outbound network access, mounts system libraries read-only, and restricts writes to an ephemeral scratch directory."))
- **c6** Gains are generally smaller on anonymized tables, and pipeline search needs repeated validation evaluations per dataset.([Conclusion, p.11](https://arxiv.org/pdf/2609.37989v1#page=11 "Gains are generally smaller on anonymized tables, where the agent relies on statistical and relational features, and pipeline search requires repeated validation evaluations for each dataset."))

