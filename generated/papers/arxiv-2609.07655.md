<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Online Surrogate Repair: Decoupling High-Fidelity Feedback from Search Length in Closed-Loop Discovery

- カード: [`arxiv-2609.07655`](../../papers/arxiv-2609.07655.yaml)
- 著者: Xiaotang Feng, Philip Torr, Bruno Andreis
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.07655v2)(arXiv v2、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** OSR uses sparse high-fidelity evaluations to update a surrogate during a longer agent search that mostly relies on cheap surrogate feedback.([Abstract, p.1](https://arxiv.org/pdf/2609.07655v2#page=1 "We propose online surrogate repair (OSR), a closed-loop algorithm that uses sparse high-fidelity evaluations to update the surrogate throughout a longer agent search conducted primarily with inexpensive surrogate feedback."))
- **c2** In controlled synthetic environments, improving global surrogate fit does not necessarily reduce maximum regret, while Q90-UCB and EI acquisitions substantially reduce it.([Abstract, p.1](https://arxiv.org/pdf/2609.07655v2#page=1 "Across controlled synthetic environments, we demonstrate that improving global surrogate fit does not necessarily reduce maximum regret, whereas Q90-UCB and expected improvement (EI) substantially reduce regret by directing evaluations toward regions that determine the optimizer’s decisions."))
- **c3** The authors argue that TabArena (global predictive accuracy) and TabPFN's training objective do not match the maximum-regret objective of closed-loop discovery.([Static surrogate repair, p.7](https://arxiv.org/pdf/2609.07655v2#page=7 "This is a crucial result because TabArena evaluates global predictive accuracy and TabPFN is trained for global prediction, not maximum regret, creating an objective mismatch with closed-loop discovery (Erickson et al., 2025; Hollmann et al., 2025; Grinsztajn et al., 2026)."))
- **c4** Static study protocol: 40 synthetic tabular worlds, a fixed budget of oracle queries, two context draws per world, two context sizes, with TabPFN-3 and TabICLv2 as surrogates.([Static surrogate repair, p.6](https://arxiv.org/pdf/2609.07655v2#page=6 "Each acquisition rule repairs the surrogate with Q = 32 oracle queries on 40 synthetically generated tabular worlds, with two independent context draws per world, at both context sizes N = 100 and N = 1000"))
- **c5** On the MADE benchmark the 'oracle' is a stronger machine-learned potential (Orb-v3), and a weaker one (MACE) provides surrogate feedback.([MADE benchmark, p.8](https://arxiv.org/pdf/2609.07655v2#page=8 "The weaker MACE model (Batatia et al., 2025) provides surrogate feedback, while the stronger Orb-v3 model (Rhodes et al., 2025) serves as the oracle."))
- **c6** Not tested: agents with test-time training or reinforcement learning, other surrogate classes, and more advanced scheduling.([Discussions and Conclusion, p.9](https://arxiv.org/pdf/2609.07655v2#page=9 "We have not tested OSR or Online EI with agents using test-time training or reinforcement learning, with other surrogate classes, or with more advanced and optimization-aware scheduling."))

