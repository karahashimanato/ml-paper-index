<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Predict Responsibly: Improving Fairness and Accuracy by Learning to Defer

- カード: [`arxiv-1711.06664`](../../papers/arxiv-1711.06664.yaml)
- 著者: David Madras, Toniann Pitassi, Richard Zemel
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1711.06664v3)(arXiv v3、カード作成時に読んだ版)
- タグ: deep-learning, model-cascades, selective-prediction, supervised, tabular-classification
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: learning to defer generalizes rejection learning by accounting for the external decision maker (DM; e.g. a human user or a proprietary black-box model) that makes the decision when the model says pass, with a learning algorithm that accounts for potential biases of that DM.([Abstract, p.1](https://arxiv.org/pdf/1711.06664v3#page=1 "We extend this concept by proposing learning to defer, which generalizes rejection learning by considering the eﬀect of other agents in the decision-making process."))
- **c2** Formal result (Theorem, Section 2.3): if the DM has constant loss on each example (e.g. is an oracle), there exist pass penalties gamma_reject, gamma_defer for which the learning-to-defer and rejection-learning objectives are equivalent; i.e. rejection learning is the special case of learning to defer with a constant-loss DM.([Why Learn to Defer?, p.5](https://arxiv.org/pdf/1711.06664v3#page=5 "The proof in Sec. 2.3 shows the central point of learning to defer: rejection learning is exactly a special case of learning to defer: a DM with constant loss α on each example."))
- **c3** Deferral signal: the post-hoc variant thresholds the model's own score (two thresholds giving a pass region), while the differentiable variant lets the deferral probability depend on the input X as well, because the DM's expected loss may vary with X differently from the model's; at test time it defers when the deferral probability exceeds 0.5.([Learning a Differentiable Model, p.6](https://arxiv.org/pdf/1711.06664v3#page=6 "This is advantageous because a DM’s actions may depend heterogenously on the data: the DM’s expected loss may change as a function of X, and it may do so diﬀerently than the model’s."))
- **c4** How the DM is obtained: semi-synthetic. Real datasets (COMPAS recidivism with race as sensitive attribute; Heritage Health Charlson Index with age) and a simulated DM trained as a separate classifier with extra information the model does not see; biased DMs are trained with a negative fairness coefficient and inconsistent DMs have predictions flipped with 30% probability on a subgroup.([Experiments, p.8](https://arxiv.org/pdf/1711.06664v3#page=8 "Due to diﬃculty obtaining and evaluating real-life decision-making data, we use “semi-synthetic data”: real datasets, and simulated DM data by training a separate classiﬁer under slightly diﬀerent conditions (see Experiment Details)."))
- **c5** Reporting protocol: results are shown across sweeps of the fairness coefficient and the defer/reject penalty, each point a median of 5 runs, and in the accuracy-fairness plots only the Pareto front is shown; all results are on held-out test sets. The Pareto front is therefore formed from test-set points; the text does not describe a separate selection set for choosing which settings are plotted.([Experiments, p.9](https://arxiv.org/pdf/1711.06664v3#page=9 "In Fig. 3, we only show the Pareto front, i.e., points for which no other point had both better accuracy and fairness."))
- **c6** Threshold selection for the post-hoc model uses the test set: 1000 random threshold combinations are sampled, the best on one half of the test set is picked, and it is evaluated on the other half.([Appendix D (Details on Optimization: Hard Thresholds), p.17](https://arxiv.org/pdf/1711.06664v3#page=17 "We sampled 1000 combinations of thresholds, picked the thresholds which minimized the loss on one half of the test set, and evaluated these thresholds on the other half of the test set."))
- **c7** Generalization across decision makers is suggested, not tested: the authors note decision data could be sampled from many DMs and cite research suggesting common trends in DM behavior, so a model trained on some DM could generalize to unseen DMs.([Why Learn to Defer?, p.5](https://arxiv.org/pdf/1711.06664v3#page=5 "Research suggests that common trends exist in DM behavior [6, 11], suggesting that a model trained on some DM could generalize to unseen DMs."))

