<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Candidate Comparability Before Promotion: Conditional Validation in Adaptive Network Intrusion Detection

- カード: [`arxiv-2609.04388`](../../papers/arxiv-2609.04388.yaml)
- 著者: Roberto Fernández-Barrios, Iker Pastor-López, Amaia Pikatza-Huerga, Pablo García Bringas
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.04388v1)(arXiv v1、カード作成時に読んだ版)
- タグ: dataset-shift-detection, error-rate-drift-detectors, kernel-methods, stream-classification, streaming, supervised, tabular-classification, two-sample-tests, window-based-drift-detectors
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** The paper separates drift detection from model promotion: a drift alarm in an adaptive intrusion detection system detects change but does not establish that a retrained challenger should replace the deployed model.([Abstract, p.1](https://arxiv.org/pdf/2609.04388v1#page=1 "Adaptive network intrusion detection systems retrain classifiers after drift alarms, but an alarm detects change; it does not establish that a challenger should replace the deployed incumbent."))
- **c2** Main finding on construction: incumbent-owned frozen preprocessing amplified the apparent harm of promotion, and with self-contained challenger pipelines the mean full-drift harm did not persist.([Abstract, p.1](https://arxiv.org/pdf/2609.04388v1#page=1 "Incumbent-owned frozen preprocessing amplified apparent promotion harm; with self-contained challenger pipelines the mean full-drift harm did not persist."))
- **c3** Drift-monitor threshold: thresholds are set at the 0.95 quantile of detector scores over pre-drift calibration windows, and the retraining trigger requires consecutive alarms followed by a cooldown.([Experimental setup (shared protocol constants), p.8](https://arxiv.org/pdf/2609.04388v1#page=8 "thresholds are the 0.95 quantile of detector scores over 30 pre-drift calibration windows; the trigger is 3 consecutive alarms with a 10-window cooldown; windows contain 128 flows."))
- **c4** In the common-harness comparison, DDM and ADWIN (river reference implementations) were used as retraining triggers at default parameters (default DDM thresholds, ADWIN delta = 0.002) with a small number of monitoring labels per window.([Common-harness comparison, p.11](https://arxiv.org/pdf/2609.04388v1#page=11 "the river reference implementations of DDM and ADWIN [17, 29] as retraining triggers with always-deploy on fire, run at their registered reference parameters — the implementations’ default DDM thresholds and ADWIN δ = 0.002 — on 8 monitoring labels per window (800 per stream)"))
- **c5** The authors caution that DDM and ADWIN were not tuned, so their results describe that configuration only; a parameter sweep would be needed before reading them as properties of the methods.([Limitations, p.24](https://arxiv.org/pdf/2609.04388v1#page=24 "DDM and ADWIN were run at their registered reference parameters and were not tuned; their cells characterize that configuration, and a parameter sweep would be required before reading them as properties of the methods."))
- **c6** Ground-truth drift is constructed: the core drift trajectories are gradual mixing ramps between real regime pools (covariate/regime drift); a P(y|x) change is not isolated and recurrent drift is not tested.([Limitations, p.24](https://arxiv.org/pdf/2609.04388v1#page=24 "The core drift trajectories are gradual mixing ramps between real regime pools (covariate/regime drift); we do not isolate a p(y/x) change, and recurrent drift is untested."))

