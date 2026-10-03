<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Best Subset Selection via a Modern Optimization Lens

- カード: [`arxiv-1507.03133`](../../papers/arxiv-1507.03133.yaml)
- 著者: Dimitris Bertsimas, Angela King, Rahul Mazumder
- 年・掲載: 2015
- 原論文: [PDF](https://arxiv.org/pdf/1507.03133v1)(arXiv v1、カード作成時に読んだ版)
- タグ: branch-and-bound, linear-models, supervised, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: discrete first-order methods produce high-quality feasible solutions that warm-start an MIO solver, which finds provably optimal solutions; the resulting algorithm gives a suboptimality guarantee even if stopped early and accommodates side constraints and LAD loss.([Abstract, p.1](https://arxiv.org/pdf/1507.03133v1#page=1 "We develop a discrete extension of modern ﬁrst order continuous optimization methods to ﬁnd high quality feasible solutions that we use as warm starts to a MIO solver that ﬁnds provably optimal solutions."))
- **c2** Guarantee vs heuristics: MIO solvers provide feasible solutions together with lower bounds on the optimal value, so the gap certifies suboptimality when stopped early; heuristic methods give no such certificate.([Brief Background on MIO, p.8](https://arxiv.org/pdf/1507.03133v1#page=8 "In contrast, heuristic methods do not provide such a certiﬁcate of suboptimality."))
- **c3** Finding vs proving optimality: for high-dimensional problems (n in {50, 100}, p in {1000, 2000}) the approach finds near-optimal solutions in minutes, with warm starts and problem-specific information, but takes hours to prove optimality.([Introduction, p.6](https://arxiv.org/pdf/1507.03133v1#page=6 "For high-dimensional problems with n ∈{50, 100} and p ∈{1000, 2000}, with the aid of warm starts and further problem-speciﬁc information, our approach ﬁnds near optimal solutions in minutes but takes hours to prove optimality."))
- **c4** Warm starts: on the Diabetes data (n = 350, p = 64), warm starts from the discrete first-order algorithm plus problem-specific bounds let the MIO close the optimality gap significantly faster than a cold start.([Improving MIO Performance via Warm Starts, p.28](https://arxiv.org/pdf/1507.03133v1#page=28 "The ﬁgure shows that in the presence of warm starts and problem speciﬁc side information, the MIO closes the optimality gap signiﬁcantly faster."))
- **c5** Solver settings: the authors observed 2-4x speedups from tuning the solver to a problem but used default solver parameters for generality, and say the reported times are not meant as best-possible benchmarks.([MIO model training, p.32](https://arxiv.org/pdf/1507.03133v1#page=32 "We observed that it was possible to obtain speedups of a factor of 2-4 by carefully tuning the optimization solver for a particular problem, but chose to maintain generality by solving with default parameters."))
- **c6** Comparison with Lasso / Sparsenet / stepwise (n > p regime, synthetic Example 1 with n = 500, p = 100, k0 = 10, averaged over ten random instances; each method's tuning parameter chosen on a held-out validation set): MIO performs best, followed by Sparsenet and Lasso, with stepwise regression worst, though Sparsenet marginally outperforms MIO in prediction error in a few instances. In this experiment the MIO for each k was stopped at a 1% optimality gap or a 15-minute time limit (MIO model training subsection), so the 'MIO' models are not necessarily certified optimal.([Statistical Performance, p.30](https://arxiv.org/pdf/1507.03133v1#page=30 "Among the methods, MIO performs the best, followed by Sparsenet, Lasso with Step(wise) exhibiting the worst performance."))
- **c7** Qualification in the high-dimensional regime (synthetic p >> n designs; competitors Lasso, Sparsenet and the discrete first-order method alone, models selected on validation sets): for Examples 2 and 3, MIO gives predictive models similar to Lasso but much sparser, and Lasso seems to perform marginally better than MIO as a predictive model for small SNR.([The High-Dimensional Regime, p.39](https://arxiv.org/pdf/1507.03133v1#page=39 "In fact, Lasso seems to perform marginally better than MIO, as a predictive model for small values of SNR."))

