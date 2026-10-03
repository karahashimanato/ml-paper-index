<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Graph Neural Networks are Dynamic Programmers

- カード: [`arxiv-2203.15544`](../../papers/arxiv-2203.15544.yaml)
- 著者: Andrew Dudzik, Petar Veličković
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2203.15544v3)(arXiv v3、カード作成時に読んだ版)
- タグ: algorithm-learning, dynamic-programming, graph-neural-networks, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: using category theory and abstract algebra, the authors argue for a connection between GNNs and DP that goes beyond prior observations on single algorithms such as Bellman-Ford, and report CLRS experiments.([Abstract, p.1](https://arxiv.org/pdf/2203.15544v3#page=1 "Here we show, using methods from category theory and abstract algebra, that there exists an intricate connection between GNNs and DP, going well beyond the initial observations over individual algorithms such as Bellman-Ford."))
- **c2** Critique of prior work: the authors state that the original algorithmic-alignment paper (their reference [37]) only mentioned in passing that DP seems to align with GNNs and demonstrated one example, Bellman-Ford, and that they found no concrete follow-up.([Introduction, p.2](https://arxiv.org/pdf/2203.15544v3#page=2 "Indeed, the original work of [37] merely mentions in passing that the formulation of DP algorithms seems to align with GNNs, and demonstrates one example (Bellman-Ford)."))
- **c3** Status of the formal claim: the integral transform (pullback, argument pushforward, message pushforward) is a construction; that it can be described as a polynomial functor is stated as a conjecture. No statement labelled as a theorem, proposition or lemma was found in the text (the only 'can be proved' refers to prior work's NTK-regime sample-complexity result), so the GNN-DP correspondence is a framework plus a conjecture, not a proven result.([The integral transform, p.4](https://arxiv.org/pdf/2203.15544v3#page=4 "Taken together, they form an integral transform—and we conjecture that this transform can be described as a polynomial functor, where p⊗and o⊕correspond to the dependent product and dependent sum from type theory (cf. Appendix D for details)."))
- **c4** Framework rather than theorem: in the conclusion the authors describe their work as deriving a generic integral-transform diagram and arguing that it is general enough to cover both GNN and DP computations (Bellman-Ford is derived over the min-plus semiring; MPNN as the same transform over the reals plus an MLP).([Conclusions, p.9](https://arxiv.org/pdf/2203.15544v3#page=9 "We derived a generic diagram of an integral transform (based on standard categorical concepts like pullback, pushforward and commutative monoids), and argued why it is general enough to support both GNN and DP computations."))
- **c5** Protocol: six CLRS Algorithmic Reasoning Benchmark tasks with the CLRS data generation and base model code reused exactly (small MLPs, embedding dimension 24), test results out-of-distribution; then 27 CLRS tasks with the PGN processor and 96-dimensional embeddings, comparing V^2 (edge updates without the polynomial-span correction) against the proposed V^3 messages.([Improving GNNs with edge updates, with experimental evaluation, p.8](https://arxiv.org/pdf/2203.15544v3#page=8 "We reuse exactly the data generation and base model implementations in the publicly available code for the CLRS benchmark."))
- **c6** Empirical claim: the V^3 architecture matched or outperformed V^2 on all edge-centric algorithms up to standard error, with smaller and less consistent gains on other tasks; the authors read this as directly validating their theory's predictions (an empirical reading on CLRS, not a proof).([Improving GNNs with edge updates, with experimental evaluation, p.9](https://arxiv.org/pdf/2203.15544v3#page=9 "We found that the V 3 architecture was equivalent to, or outperformed, the non-polynomial (V 2) one in all edge-centric algorithms (up to standard error)."))
- **c7** Affiliation and funding: both authors are at DeepMind and the research was funded by DeepMind.([Acknowledgments and Disclosure of Funding, p.10](https://arxiv.org/pdf/2203.15544v3#page=10 "This research was funded by DeepMind."))

