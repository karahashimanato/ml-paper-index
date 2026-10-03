<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Attention, Learn to Solve Routing Problems!

- カード: [`arxiv-1803.08475`](../../papers/arxiv-1803.08475.yaml)
- 著者: Wouter Kool, Herke van Hoof, Max Welling
- 年・掲載: 2018
- 原論文: [PDF](https://arxiv.org/pdf/1803.08475v3)(arXiv v3、カード作成時に読んだ版)
- タグ: combinatorial-optimization, deep-learning, graph-neural-networks, reinforcement-learning
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: an attention-layer model with stated benefits over the Pointer Network, trained with REINFORCE and a greedy-rollout baseline that the authors find more efficient than a value function.([Abstract, p.1](https://arxiv.org/pdf/1803.08475v3#page=1 "we propose a model based on attention layers with beneﬁts over the Pointer Network and we show how to train this model using REINFORCE with a simple baseline based on a deterministic greedy rollout, which we ﬁnd is more efﬁcient than using a value function"))
- **c2** Scope of the claim: the stated goal is not to beat a specialized non-learned TSP solver such as Concorde, but to show flexibility across several routing problems of reasonable size with a single set of hyperparameters.([Introduction, p.2](https://arxiv.org/pdf/1803.08475v3#page=2 "specialized TSP algorithm such as Concorde (Applegate et al., 2006)"))
- **c3** TSP baselines: optimal results by Gurobi and by Concorde (faster, TSP-specialized), LKH3 as a state-of-the-art heuristic, plus nearest/random/farthest insertion and nearest neighbor, and previously reported learned heuristics (Bello et al., OR Tools as reported by Bello et al., Christofides + 2OPT as reported by Vinyals et al.).([Experiments, p.6](https://arxiv.org/pdf/1803.08475v3#page=6 "For the TSP, we report optimal results by Gurobi, as well as by Concorde (Applegate et al., 2006) (faster than Gurobi as it is specialized for TSP) and LKH3 (Helsgaun, 2017), a state-of-the-art heuristic solver that empirically also ﬁnds optimal solutions in time comparable to Gurobi."))
- **c4** Run-time comparison protocol: the authors note run times can differ by two orders of magnitude due to implementation and hardware; they report time to solve the 10000-instance test set on a single GPU (1080Ti) or 32 instances in parallel on a 32 virtual CPU system, and call this conservative because most baselines are single-thread CPU implementations.([Experiments, p.6](https://arxiv.org/pdf/1803.08475v3#page=6 "Run times are important but hard to compare: they can vary by two orders of magnitude as a result of implementation (Python vs C++) and hardware (GPU vs CPU)."))
- **c5** Size generalization (appendix): models tested on sizes other than trained for generalize, but quality degrades as the size difference grows; the authors read this as models specializing to the trained sizes and suggest selecting the trained model with best validation performance per size.([Appendix, p.15](https://arxiv.org/pdf/1803.08475v3#page=15 "The models generalize when tested on different sizes, although quality degrades as the difference becomes bigger, which can be expected as there is no free lunch (Wolpert & Macready, 1997)."))
- **c6** Limitation / future work: scaling to larger instances is named as an important direction; the authors also note that many practical feasibility constraints cannot be satisfied by simple masking and suggest combining heuristic learning with backtracking.([Discussion, p.9](https://arxiv.org/pdf/1803.08475v3#page=9 "Scaling to larger problem instances is an important direction for future research, where we think we have made an important ﬁrst step by using a graph based method, which can be sparsiﬁed for improved computational efﬁciency."))
- **c7** Funding / affiliation: the research was funded by ORTEC Optimization Technology (first author affiliated with University of Amsterdam and ORTEC).([Acknowledgements, p.10](https://arxiv.org/pdf/1803.08475v3#page=10 "This research was funded by ORTEC Optimization Technology."))

