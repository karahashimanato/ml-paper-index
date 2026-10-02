<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# A Unified Uncertainty Representation for Graph Neural Networks via Doubly-Spectral Stochastic Expansion

- カード: [`arxiv-2609.35703`](../../papers/arxiv-2609.35703.yaml)
- 著者: Fred Xu, Thomas Markovich, Florence Regol, Yizhou Sun
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.35703v1)(arXiv v1、カード作成時に読んだ版)
- タグ: graph-neural-networks, graph-node-prediction, supervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** DSS-GNN can be used standalone or as a residual branch beside a deterministic encoder (DSS-Hybrid).([Abstract, p.1](https://arxiv.org/pdf/2609.35703v1#page=1 "DSS-GNN has two deployment modes: standalone, or as a residual branch beside a deterministic encoder (DSS-Hybrid)."))
- **c2** Main claim: the standalone model has the lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc calibration.([Abstract, p.1](https://arxiv.org/pdf/2609.35703v1#page=1 "Standalone DSS-GNN achieves the lowest Brier score among the compared uncertainty-aware baselines on all 14 node classification benchmarks without post-hoc correction"))
- **c3** OOD-detection baselines GNNSafe, GNNSafe++ and GPN are taken from the values reported by Wu et al., while Graph-EBM, MC-dropout and Deep Ensembles are run in the authors' pipeline on the same backbone.([Experiments (setup), p.6](https://arxiv.org/pdf/2609.35703v1#page=6 "against GNNSafe, GNNSafe++, and GPN [30] at the values reported by Wu et al. [36]"))
- **c4** Distribution-shift baselines on GOOD (ERM through TAR) are also copied from Zheng et al., with only G-ΔUQ run in the authors' pipeline.([Experiments (distribution-shifted classification), p.9](https://arxiv.org/pdf/2609.35703v1#page=9 "ERM through TAR as reported by Zheng et al. [38]"))
- **c5** For the standalone model under the GOOD protocol, the epoch and the configuration (BatchNorm, learning rate, hidden width, P) are selected on the GOOD OOD-validation split.([Appendix (standalone under the GOOD protocol), p.39](https://arxiv.org/pdf/2609.35703v1#page=39 "the epoch is selected by OOD-validation loss within each run and the configuration (BatchNorm on/off, learning rate, hidden width, P) on the GOOD OOD-validation split"))
- **c6** Limitation: all stochastic variation comes from one shared scalar Gaussian factor, so joint cross-node uncertainty is not modeled.([Conclusion and Limitations, p.10](https://arxiv.org/pdf/2609.35703v1#page=10 "All stochastic variation is due to one shared Gaussian factor, perfectly dependent across nodes, so the logit covariance across nodes has rank at most P."))

