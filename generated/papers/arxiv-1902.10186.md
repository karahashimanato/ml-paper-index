<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Attention is not Explanation

- カード: [`arxiv-1902.10186`](../../papers/arxiv-1902.10186.yaml)
- 著者: Sarthak Jain, Byron C. Wallace
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1902.10186v3)(arXiv v3、カード作成時に読んだ版)
- タグ: attention-explanations, deep-learning, feature-attribution, model-explanation, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Across a variety of NLP tasks, learned attention weights are frequently uncorrelated with gradient-based feature importance, and very different attention distributions can yield equivalent predictions; the authors conclude standard attention modules do not provide meaningful explanations.([Abstract, p.1](https://arxiv.org/pdf/1902.10186v3#page=1 "learned attention weights are frequently uncorrelated with gradient-based measures of feature importance, and one can identify very different attention distributions that nonetheless yield equivalent predictions"))
- **c2** Assumed properties of faithful attention explanations: (i) attention should correlate with feature-importance measures and (ii) alternative (counterfactual) attention configurations should change the prediction.([Introduction, p.1](https://arxiv.org/pdf/1902.10186v3#page=1 "(i) Attention weights should correlate with feature importance measures (e.g., gradient-based measures); (ii) Alternative (or counterfactual) attention weight configurations ought to yield corresponding changes in prediction"))
- **c3** Neither property was consistently observed for a BiLSTM with a standard attention mechanism on text classification, question answering and natural language inference.([Introduction, p.1](https://arxiv.org/pdf/1902.10186v3#page=1 "We report that neither property is consistently observed by a BiLSTM with a standard attention mechanism in the context of text classification, question answering (QA), and Natural Language Inference (NLI) tasks."))
- **c4** Evaluation protocol (no ground-truth explanations): Kendall tau correlation of attention with gradient-based importance and with leave-one-out output differences, computed on test sets.([Section 4.1, p.4](https://arxiv.org/pdf/1902.10186v3#page=4 "Specifically we measure correlations between attention and: (1) gradient based measures of feature importance (τg), and, (2) differences in model output induced by leaving features out (τloo)."))
- **c5** For the adversarial attention search, the allowed change in model output (epsilon, in total variation distance) was set to 0.01 for text classification and 0.05 for QA datasets.([Adversarial Attention, p.9](https://arxiv.org/pdf/1902.10186v3#page=9 "In practice we simply set this to 0.01 for text classification and 0.05 for QA datasets."))
- **c6** Limitation: the authors do not claim that gradient or leave-one-out measures are ideal or should be treated as ground truth.([Discussion and Conclusions, p.11](https://arxiv.org/pdf/1902.10186v3#page=11 "We do not intend to imply that such alternative measures are necessarily ideal or that they should be considered ‘ground truth’."))
- **c7** Limitation: only a handful of attention variants (focused on BiLSTM encoders with attention) were considered; alternative attention specifications may lead to different conclusions.([Discussion and Conclusions, p.11](https://arxiv.org/pdf/1902.10186v3#page=11 "An additional limitation is that we have only considered a handful of attention variants, selected to reflect common module architectures for the respective tasks included in our analysis."))

