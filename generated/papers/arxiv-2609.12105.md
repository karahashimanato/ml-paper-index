<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Language Is an Insufficient Substrate for Quantitative Reasoning, and Consequential Domains Need Large Quantitative Models

- カード: [`arxiv-2609.12105`](../../papers/arxiv-2609.12105.yaml)
- 著者: Reuben Vandeventer, David Imrem, David J. Wild
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.12105v1)(arXiv v1、カード作成時に読んだ版)
- タグ: large-language-models, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper's position is that the assumption that progress on consequential quantitative decisions will follow from progress in LLMs is mistaken, and that the mistake is structural rather than a matter of present capability.([Abstract, p.1](https://arxiv.org/pdf/2609.12105v1#page=1 "This paper takes the position that the assumption is mistaken, and that the mistake is structural rather than a matter of present capability."))
- **c2** Fidelity, reproducibility, lineage and calibration are argued to define a distinct model class, the Large Quantitative Model (LQM).([Abstract, p.1](https://arxiv.org/pdf/2609.12105v1#page=1 "We argue that these properties define a distinct model class, which we call the Large Quantitative Model (LQM)"))
- **c3** A tabular foundation model can be native to the quantitative data and still lack lineage and structural explicitness, because its representation of the domain lives in its weights.([Tabular and time-series foundation models, p.7](https://arxiv.org/pdf/2609.12105v1#page=7 "A tabular foundation model can be substrate-native and still fail lineage and structural explicitness, because its representation of the domain lives in weights."))
- **c4** Citing prior literature (not its own experiments), the paper states that on tabular prediction with modest datasets, gradient-boosted trees or purpose-built tabular transformers continue to outperform general-purpose deep models.([Empirical corroboration, p.5](https://arxiv.org/pdf/2609.12105v1#page=5 "In the setting closest to our own argument—tabular prediction on modest datasets—models designed for the statistical character of the data, whether gradient-boosted trees or purpose-built tabular transformers, continue to outperform general-purpose deep models"))
- **c5** The paper runs no benchmark experiments of its own; its empirical evidence is one deployed system (a security-operations architecture described by Vallabhaneni et al.), which the authors say is not a full LQM.([Evidence, p.10](https://arxiv.org/pdf/2609.12105v1#page=10 "We have one deployed test of this prediction that we can report in full."))
- **c6** Competing interests: all three authors are affiliated with Duo Dimensio LLC, which develops systems of the kind the paper describes.([Competing interests, p.13](https://arxiv.org/pdf/2609.12105v1#page=13 "R.V., D.I. and D.J.W. are affiliated with Duo Dimensio LLC, which develops systems of the kind described in Section 7."))

