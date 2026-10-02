<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Solving In-Table Prediction Problems by Deep Neural Networks with Performance Evaluation Using Synthetic Data

- カード: [`arxiv-2609.01262`](../../papers/arxiv-2609.01262.yaml)
- 著者: Xiao Zhao, Daniela Oelke
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.01262v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, self-supervised, tabular-attention, tabular-mlp, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper applies self-supervised learning to in-table prediction by randomly masking columns and using them as learning targets.([Abstract, p.1](https://arxiv.org/pdf/2609.01262v1#page=1 "A self-supervised learning approach is applied to address this problem by randomly selecting columns to be masked out and used as learning targets."))
- **c2** A new neural layer is proposed that embeds both numerical and empty values of continuous features.([Abstract, p.1](https://arxiv.org/pdf/2609.01262v1#page=1 "To handle missing values in continuous features, a novel neural layer is proposed to embed both numerical and empty values."))
- **c3** On the synthetic data, the attention-based network outperforms MLP and ResNet when enough training examples are available and a relatively large embedding length is chosen.([Abstract, p.1](https://arxiv.org/pdf/2609.01262v1#page=1 "We conclude that, the attention-based structure outperforms the other two networks, when a sufficiently large number of training examples is available and a relatively large embedding length is chosen."))
- **c4** Network structures and learning rate are fixed and no hyperparameter tuning of the model structures is done; early stopping uses a validation set.([Training strategy, p.6](https://arxiv.org/pdf/2609.01262v1#page=6 "Hyperparameter tuning of selected model structures is not done in this work."))
- **c5** The evaluation is limited to two synthetic three-column relationships with known dependencies, so the trends may not transfer to larger or real-world tables.([Conclusion, p.11](https://arxiv.org/pdf/2609.01262v1#page=11 "The evaluation is limited to two synthetic, three-column relationships with predefined, known dependencies."))

