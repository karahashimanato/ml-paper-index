<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Algorithm Selection for Combinatorial Search Problems: A Survey

- カード: [`arxiv-1210.7959`](../../papers/arxiv-1210.7959.yaml)
- 著者: Lars Kotthoff
- 年・掲載: 2012
- 原論文: [PDF](https://arxiv.org/pdf/1210.7959v1)(arXiv v1、カード作成時に読んだ版)
- タグ: combinatorial-optimization, dynamic-ensemble-selection, meta-learning, model-selection
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Framework (Rice 1976, as summarized by the survey): given a problem space and an algorithm space, map each problem-algorithm pair to its performance and use the mapping to select the best algorithm; Rice's refined model adds problem features, which the survey calls the crucial difference that often makes an approach feasible.([Introduction, p.1](https://arxiv.org/pdf/1210.7959v1#page=1 "The basic model described in the paper is very simple – given a space of problems and a space of algorithms, map each problem-algorithm pair to its performance."))
- **c2** Caveat on training samples and features (the survey summarizing Rice 1976 on the difficulty of knowing the problem space): problem spaces are often sampled to evaluate algorithms empirically; if the sample is not representative or the features do not separate problem classes, there is little hope of finding the best or even a good selection mapping.([Introduction, p.4](https://arxiv.org/pdf/1210.7959v1#page=4 "If the sample is not representative, or the features do not facilitate a good separation of the problem classes in the feature space, there is little hope of ﬁnding the best or even a good selection mapping."))
- **c3** Failure mode of selecting a single algorithm per instance: a wrong selection cannot be mitigated; the system is stuck with a badly performing algorithm even if other portfolio algorithms would do much better (schedules over several algorithms are the surveyed alternative).([What to select, p.12](https://arxiv.org/pdf/1210.7959v1#page=12 "If an algorithm is chosen that exhibits bad performance on the problem, the system is “stuck” with it and no adjustments are made, even if all other portfolio algorithms would perform much better."))
- **c4** Offline vs online selection: purely offline approaches have no way of mitigating wrong choices, often do not even detect them (they do not monitor the chosen algorithm), and are inherently vulnerable to bad choices, but incur no overhead during solving; online selection allows finer decisions at the price of higher overhead.([When to select, p.13](https://arxiv.org/pdf/1210.7959v1#page=13 "Purely oﬄine approaches are inherently vulnerable to bad choices."))
- **c5** Selector cost requirement: apart from accuracy, a selector must be relatively cheap to run, since selecting is pointless if it costs more than solving the problem.([Portfolio selectors, p.15](https://arxiv.org/pdf/1210.7959v1#page=15 "Apart from accuracy, one of the main requirements for such a selector is that it is relatively cheap to run – if selecting an algorithm for solving a problem is more expensive than solving the problem, there is no point in doing so."))
- **c6** Fallback to a default algorithm (described for systems such as SATzilla, Xu et al. 2008): pre-solvers run before feature analysis, and if the predicted feature-analysis time is too high a default algorithm with reasonable performance is chosen; the survey says this matters when problems are hard to analyse but easy to solve.([Portfolio selectors, p.15](https://arxiv.org/pdf/1210.7959v1#page=15 "If the predicted required analysis time is too high, a default algorithm with reasonable performance is chosen and run on the problem."))
- **c7** No Free Lunch: the survey notes NFL would also apply to selection systems themselves (gains on one part of the problem space, losses elsewhere), but judges from the literature that, if applicable, the ramifications in practice may not be significant.([No Free Lunch theorems, p.5](https://arxiv.org/pdf/1210.7959v1#page=5 "However, a review of the literature suggests that, if the theorems are applicable, the ramiﬁcations in practice may not be signiﬁcant."))

