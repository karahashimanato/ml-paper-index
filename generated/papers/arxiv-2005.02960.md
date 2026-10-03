<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Exploring the Loss Landscape in Neural Architecture Search

- カード: [`arxiv-2005.02960`](../../papers/arxiv-2005.02960.yaml)
- 著者: Colin White, Sam Nolen, Yash Savani
- 年・掲載: 2020
- 原論文: [PDF](https://arxiv.org/pdf/2005.02960v3)(arXiv v3、カード作成時に読んだ版)
- タグ: local-search, neural-architecture-search
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Main claim: the simplest hill-climbing algorithm is a powerful NAS baseline, and when noise in popular NAS benchmark datasets is reduced to a minimum, hill-climbing outperforms many popular state-of-the-art algorithms.([Abstract, p.1](https://arxiv.org/pdf/2005.02960v3#page=1 "In this work, we show that (1) the simplest hill-climbing algorithm is a powerful baseline for NAS, and (2), when the noise in popular NAS benchmark datasets is reduced to a minimum, hill-climbing to outperforms many popular state-of-the-art algorithms."))
- **c2** Protocol: NASBench-101, NASBench-201 (CIFAR-10, CIFAR-100, ImageNet16-120) and NASBench-301 (DARTS space); local search is compared with random search, regularized evolution, Bayesian optimization and BANANAS, each with a budget of 300 evaluations and 200 trials; 'denoising' is done artificially by averaging the three seeds (101/201) or the surrogate ensemble (301).([Experiments, p.4](https://arxiv.org/pdf/2005.02960v3#page=4 "However, for each architecture, we can average all three validation accuracies to obtain a less noisy estimate."))
- **c3** Result depends on noise: on NASBench-101 and 301 local search beats all other algorithms when noise is minimal but performs similarly to Bayesian optimization in the standard (noisy) setting.([Experiments, p.4](https://arxiv.org/pdf/2005.02960v3#page=4 "On both NASBench-101 and 301, local search outperforms all other algorithms when the noise is minimal, amd performs similarly to Bayesian optimization in the standard setting."))
- **c4** Exception: on NASBench-201 ImageNet16-120, the initial noise is so high that all NAS algorithms perform worse in the reduced-noise version.([Appendix A, p.12](https://arxiv.org/pdf/2005.02960v3#page=12 "Note that for the case of ImageNet16-120, the initial level of noise is so high that all NAS algorithms actually perform worse in the reduced noise version of the problem."))
- **c5** Theory and its assumptions: validation losses are modelled as drawn from a global distribution, with neighbours' losses drawn from a local distribution conditioned on the current loss; with fixed neighbourhood size s and a vertex-transitive neighbourhood graph, Theorem 5.1 gives the expected number of local minima and of starting points converging within epsilon of the global optimum (the authors say this makes local search similar to a Markov process and that their experiments in Figure 4.2 suggest this is a reasonable assumption in practice).([Theoretical Characterization, p.6](https://arxiv.org/pdf/2005.02960v3#page=6 "Therefore, we assume that the validation loss for a trained architecture is sampled from a global probability distribution, and for each architecture, the validation losses of its neighbors are sampled from a local probability distribution."))
- **c6** Limits of the theory: estimating the required distributions is not feasible for large search spaces; the theory is meant only to give understanding; in the simulation, it exactly predicts the uniform-random NASBench-201 variant, and on the three NASBench-201 image datasets predicts performance fairly accurately but not perfectly, which the authors attribute to their assumption that the accuracy distribution is unimodal.([Theoretical Characterization, p.7](https://arxiv.org/pdf/2005.02960v3#page=7 "We note that approximating these distributions are not feasible for large search spaces; the purpose of our theoretical results are meant only to provide a deeper understanding of local search and lay the groundwork for future studies."))
- **c7** Affiliation: the work was done while all authors were employed at Abacus.AI.([Acknowledgments, p.8](https://arxiv.org/pdf/2005.02960v3#page=8 "This work done while all authors were employed at Abacus.AI."))

