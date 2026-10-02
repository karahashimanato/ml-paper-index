<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Behavioral Monitoring of JEPA World Models with Jacobian Centroids

- カード: [`arxiv-2609.33940`](../../papers/arxiv-2609.33940.yaml)
- 著者: Thomas Walker, Randall Balestriero, Richard Baraniuk
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.33940v1)(arXiv v1、カード作成時に読んだ版)
- タグ: dataset-shift-detection, deep-learning, post-hoc, reconstruction-based-detectors, saliency-maps, unsupervised
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Centroids (sub-component Jacobian row-sums) identify behavioral properties of world models and complement activation-based signals.([Abstract, p.1](https://arxiv.org/pdf/2609.33940v1#page=1 "Here, we show that centroids—sub-component Jacobian row-sums—effectively identify the behavioral properties of WMs, complementing traditional activation-based knowledge signals."))
- **c2** Main claim: centroid-based methods outperform baseline methods as distribution-shift detectors.([Abstract, p.1](https://arxiv.org/pdf/2609.33940v1#page=1 "Moreover, centroid-based methods outperform baseline methods as distribution-shift detectors."))
- **c3** Evaluation: the target is episode success/failure from environment feedback on Push-T and TwoRoom (LeWorldModel + CEM planner), scored by AUC; distribution shift is induced by a larger goal offset than in-distribution.([Centroid Signals for Failure Prediction (experimental setup), p.4](https://arxiv.org/pdf/2609.33940v1#page=4 "We evaluate on Push-T and TwoRoom using the trained LeWorldModel with a CEM planner (300 samples, 30 steps, receding-horizon K = 2), and label each episode as a success or failure based on the environment’s feedback."))
- **c4** The pre-execution gate thresholds are calibrated from in-distribution data only, without labeled failures.([Pre-Execution Gate and Adaptive Replanning, p.6](https://arxiv.org/pdf/2609.33940v1#page=6 "Both thresholds are calibrated from in-distribution data alone with no labeled failures, and yield zero in-distribution false positives on Push-T and a 1% false-alarm rate on TwoRoom."))
- **c5** Layer choice for the calibration signal is task-specific (layer 0 for Push-T, deepest layer for TwoRoom) and is reported relative to the oracle-best layer.([Appendix (signal definitions), p.9](https://arxiv.org/pdf/2609.33940v1#page=9 "Layer-0 suffices for Push-T (AUC within 0.02 of oracle in-distribution, within 0.01 out-of-distribution), whereas layer-5 (deepest) is consistently oracle-optimal across all seeds and regimes on TwoRoom."))
- **c6** Limitation: all results come from one world-model family on two tasks.([Conclusion, p.6](https://arxiv.org/pdf/2609.33940v1#page=6 "All results come from a single WM family (LeWorldModel) on two tasks."))

