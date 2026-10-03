<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Green AI

- カード: [`arxiv-1907.10597`](../../papers/arxiv-1907.10597.yaml)
- 著者: Roy Schwartz, Jesse Dodge, Noah A. Smith, Oren Etzioni
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1907.10597v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Position: the paper advocates making efficiency an evaluation criterion for research alongside accuracy, and reporting the financial cost ('price tag') of developing, training and running models.([Abstract, p.1](https://arxiv.org/pdf/1907.10597v3#page=1 "This position paper advocates a practical solution by making efﬁciency an evaluation criterion for research alongside accuracy and related measures."))
- **c2** Cost model: the cost of producing a result is described as growing linearly with the cost of processing one example, the training-set size and the number of hyperparameter experiments.([Red AI, p.3](https://arxiv.org/pdf/1907.10597v3#page=3 "The total cost of producing a (R)esult in machine learning increases linearly with each of these quantities."))
- **c3** Caveat: the authors state that this equation is a simplification and that it ignores other factors such as the number of training epochs.([Red AI, p.3](https://arxiv.org/pdf/1907.10597v3#page=3 "Equation 1 is a simpliﬁcation (e.g., different hyperparameter assignments can lead to different costs for processing a single example)."))
- **c4** Survey method: for a sample of 60 papers from ACL, NeurIPS and CVPR, the authors classified whether the claimed main contribution is accuracy, efficiency, both, or other.([Red AI, p.3](https://arxiv.org/pdf/1907.10597v3#page=3 "For each paper we noted whether the authors claim their main contribution to be (a) an improvement to accuracy or some related measure, (b) an improvement to efﬁciency, (c) both, or (d) other."))
- **c5** Drawbacks of alternative measures: carbon emission, though described as appealing, is described as impractical to measure exactly and not comparable across locations or times because it depends on the local electricity infrastructure (electricity use, run time and parameter count are also discussed and judged hardware-dependent or not reflecting work done).([Measures of Efficiency, p.6](https://arxiv.org/pdf/1907.10597v3#page=6 "As a result, it is not comparable between researchers in different locations or even the same location at different times."))
- **c6** Recommendation: report the total number of floating point operations (FPO) required to generate a result; the authors argue FPO is hardware-agnostic, tied to the amount of energy consumed, and (citing Canziani et al.) strongly correlated with running time.([Measures of Efficiency, p.6](https://arxiv.org/pdf/1907.10597v3#page=6 "As a concrete measure, we suggest reporting the total number of ﬂoating point operations (FPO) required to generate a result"))
- **c7** Limitations of FPO stated by the authors: it ignores memory consumption, and the amount of work largely depends on the model implementation.([Measures of Efficiency (Discussion), p.7](https://arxiv.org/pdf/1907.10597v3#page=7 "First, it targets the electricity consumption of a model, while ignoring other potential limiting factors for researchers such as the memory consumption by the model, which can often lead to additional energy and monetary costs [24]."))

