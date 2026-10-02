<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Axiomatic Attribution for Deep Networks

- カード: [`arxiv-1703.01365`](../../papers/arxiv-1703.01365.yaml)
- 著者: Mukund Sundararajan, Ankur Taly, Qiqi Yan
- 年・掲載: 2017
- 原論文: [PDF](https://arxiv.org/pdf/1703.01365v2)(arXiv v2、カード作成時に読んだ版)
- タグ: deep-learning, feature-attribution, model-explanation, post-hoc, saliency-maps
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper identifies two axioms (Sensitivity, Implementation Invariance) and shows that most known attribution methods do not satisfy them, which it considers a fundamental weakness of those methods.([Abstract, p.1](https://arxiv.org/pdf/1703.01365v2#page=1 "We show that they are not satisfied by most known attribution methods, which we consider to be a fundamental weakness of those methods."))
- **c2** Main contribution: Integrated Gradients, implementable with a few gradient calls and applicable to many deep networks.([Conclusion, p.8](https://arxiv.org/pdf/1703.01365v2#page=8 "The primary contribution of this paper is a method called integrated gradients that attributes the prediction of a deep network to its inputs."))
- **c3** Assumption: attributions are relative to a baseline; the authors recommend a baseline with near-zero score that conveys complete absence of signal (e.g. black image, zero embedding).([Applying Integrated Gradients, p.5](https://arxiv.org/pdf/1703.01365v2#page=5 "So we would additionally like the baseline to convey a complete absence of signal, so that the features that are apparent from the attributions are properties only of the input, and not of the baseline."))
- **c4** Critique of perturbation-based evaluation: perturbed images may be unnatural, so a score drop may reflect distribution shift rather than attribution quality; the paper therefore uses an axiomatic approach instead of an empirical benchmark.([Uniqueness of Integrated Gradients, p.3](https://arxiv.org/pdf/1703.01365v2#page=3 "However, the images resulting from pixel perturbation could be unnatural, and it could be that the scores drop simply because the network has never seen anything like it in training."))
- **c5** If averaging over multiple paths is allowed, the Shapley-Shubik method also satisfies the axioms but yields attributions different from Integrated Gradients; on a min(x1, x2) example the authors say it seems somewhat subjective to prefer one result over the other.([Integrated Gradients is Symmetry-Preserving, p.5](https://arxiv.org/pdf/1703.01365v2#page=5 "This method yields attributions that are different from integrated gradients."))
- **c6** Critique of local surrogate methods (LIME): implementation invariant but without a guarantee of sensitivity.([Other Related work, p.8](https://arxiv.org/pdf/1703.01365v2#page=8 "However, this approach does not guarantee sensitivity."))
- **c7** Stated limitation: interactions between input features and the network's logic are not addressed.([Conclusion, p.8](https://arxiv.org/pdf/1703.01365v2#page=8 "While our and other works have made some progress on understanding the relative importance of input features in a deep network, we have not addressed the interactions between the input features or the logic employed by the network."))

