<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Attention is not not Explanation

- カード: [`arxiv-1908.04626`](../../papers/arxiv-1908.04626.yaml)
- 著者: Sarah Wiegreffe, Yuval Pinter
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1908.04626v2)(arXiv v2、カード作成時に読んだ版)
- タグ: attention-explanations, deep-learning, model-explanation, post-hoc
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper proposes four tests of when attention can serve as explanation: a uniform-weights baseline, a variance calibration over random seeds, a diagnostic framework using frozen pretrained attention weights, and end-to-end adversarial attention training.([Abstract, p.1](https://arxiv.org/pdf/1908.04626v2#page=1 "We propose four alternative tests to determine when/whether attention can be used as explanation"))
- **c2** Critique of Jain & Wallace: they detach the attention distribution and output layer from the parameters that compute them and treat each attention score as a standalone unit, and compute an independent adversarial distribution per instance.([Attention Might be Explanation, p.3](https://arxiv.org/pdf/1908.04626v2#page=3 "Jain and Wallace detach the attention distribution and output layer of their pretrained network from the parameters that compute them (see Figure 1), treating each attention score as a standalone unit independent of the model."))
- **c3** Compared with a variant whose attention is frozen to uniform weights, the attention layer appears to offer little to no improvement on three of the classification tasks; the authors conclude these datasets (notably AG News and 20 Newsgroups) are not useful test cases, since attention is not explanation if it is not needed.([Uniform as the Adversary, p.5](https://arxiv.org/pdf/1908.04626v2#page=5 "We conclude that these datasets, notably AG NEWS and 20 NEWSGROUPS, are not useful test cases for the debated question: attention is not explanation if you don’t need it."))
- **c4** Their evaluation is functionally grounded: an analysis on proxy tasks without human evaluation.([Defining Explanation, p.9](https://arxiv.org/pdf/1908.04626v2#page=9 "our proposed methods provide a functionally-grounded evaluation of attention as explanation, i.e. an analysis conducted on proxy tasks without human evaluation."))
- **c5** Whether attention is explanation depends on the definition one adopts: plausible explanations, faithful explanations, or both.([Attention is All you Need it to Be, p.9](https://arxiv.org/pdf/1908.04626v2#page=9 "Whether or not attention is explanation depends on the definition of explainability one is looking for: plausible or faithful explanations (or both)."))
- **c6** Partial agreement with Jain & Wallace: adversarial attention distributions can be found for LSTM models in some classification tasks.([Attention is All you Need it to Be, p.9](https://arxiv.org/pdf/1908.04626v2#page=9 "However, we have confirmed that adversarial distributions can be found for LSTM models in some classification tasks, as originally hypothesized by Jain and Wallace."))
- **c7** Adversarially trained attention distributions perform poorly, relative to the original attention, when used as guide weights in the diagnostic MLP.([Attention is All you Need it to Be, p.9](https://arxiv.org/pdf/1908.04626v2#page=9 "We’ve shown that alternative attention distributions found via adversarial training methods perform poorly relative to traditional attention mechanisms when used in our diagnostic MLP model."))

