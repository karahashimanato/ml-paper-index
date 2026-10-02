"""候補 Issue #3 で承認された時系列異常検知の論文(18本)のカード。
各論文の主張と、評価方法(point-adjust の使用有無・指標・閾値)の記述を記録する。結果表の数値は記録しない(notes 参照)。
書誌(著者・版・年)は arXiv API の値(scratchpad で取得したもの)をそのまま書き写した。IJCAI の2本は PDF の1ページ目による。"""

import sys

sys.path.insert(0, "scripts/cards")
from _common import Paper, write_card  # noqa: E402

TSAD = ["time-series-anomaly-detection"]
NOTE = ("Approved from candidate issue #3 (2026-10-02). Results tables were not recorded; only claims, including how the paper evaluates "
        "(point-adjust or not, metrics, thresholds). Locations are topic names, not section numbers.")

SPECS = [
  {"id": "arxiv-2608.02821", "title": "What the Detector Can See: Evaluating CPS Anomaly Detectors Independently of the Decision Rule",
   "authors": None, "fam": ["deep-learning"], "par": ["unsupervised"],
   "proposes": ["Decision-rule-free evaluation of anomaly detectors via normalized residual energy"],
   "claims": [
     ("Precision/recall/F1 at one operating point mix two things: how well the detector represents the process and how well its alarm threshold is set.", "Abstract",
      "These scores mix two separate things: how well the detector represents the physical process, and how well its alarm threshold is set."),
     ("The paper evaluates the detector's residuals directly, independent of any alarm rule (threshold, CUSUM, point adjustment).", "Abstract",
      "Instead of scoring only the final alarms, we evaluate Stage 1 directly using normalized residual energy"),
     ("Detectors with similar ROC-AUC on SWaT differ by more than an order of magnitude at a common false-alarm rate.", "Abstract",
      "Although the detectors have similar ROC-AUC values on SWaT, their performance differs by more than an order of magnitude at a common false-alarm rate."),
     ("Rankings change across testbeds (e.g. TranAD first on HAI but last on SWaT).", "Abstract",
      "Rankings also change across testbeds: TranAD ranks first on HAI but last on SWaT, while NSIBF ranks first on WADI but last on HAI."),
     ("Detection failures can stem from a weak representation, poor threshold calibration, or an attack with little physical effect.", "Abstract",
      "These results show that detection failure can come from different sources: a weak representation, poor threshold calibration, or an attack with little physical effect."),
   ]},
  {"id": "arxiv-2609.39215", "title": None, "fam": ["classical-outlier-detectors", "deep-learning"], "par": ["unsupervised", "streaming"],
   "proposes": ["StrAD streaming TSAD benchmark", "TSB-drift dataset"],
   "claims": [
     ("Most streaming anomaly detection methods come from streaming outlier detection and ignore core characteristics of time-series anomalies; they are evaluated on synthetic or small benchmarks.", "Abstract",
      "most of these approaches originate from the streaming outlier detection litera- ture and largely ignore core characteristics of time series anomalies."),
     ("Contrary to common assumptions, static TSAD methods significantly outperform streaming approaches in most streaming settings.", "Abstract",
      "Our results show that, contrary to common assumptions, static TSAD methods significantly outperform streaming approaches in most streaming settings."),
     ("AUC-ROC is overly optimistic on imbalanced data, so AUC-PR is used.", "Evaluation measures",
      "Consequently, the Area Under the Precision- Recall Curve (AUC-PR) is preferred in this study."),
     ("The main limitation of streaming TSAD is its focus on point-wise outliers rather than collective anomalies.", "Conclusion",
      "The most significant limitation is the legacy focus on point-wise outliers."),
   ]},
  {"id": "arxiv-2610.01168", "title": None, "fam": ["classical-outlier-detectors", "deep-learning"], "par": ["unsupervised"],
   "proposes": ["SHAD benchmark (detection, explainability, interpretability)"],
   "claims": [
     ("Current benchmarks focus on detection accuracy; few evaluate explainability and none provides rich semantic annotations.", "Abstract",
      "One of the main reasons for this gap is that current benchmarks primarily focus on detection accuracy, and only few of them evaluate spatial explainability."),
     ("SHAD has 215 multivariate high-dimensional series from real distributed cloud storage systems, with per-dimension labels and textual annotations.", "Abstract",
      "a fully annotated benchmark composed of 215 multivariate, high-dimensional time series collected from real-world distributed cloud storage systems operated by Scality."),
     ("Detection is evaluated with threshold-independent VUS-PR.", "Experimental setup",
      "Performance is evaluated using VUS- PR (a robust, threshold-independent metric) with a 25-point buffer"),
     ("State-of-the-art detectors are accurate but not perfect; explainability is not solved by existing methods; frozen LLMs cannot correctly interpret anomalies.", "Conclusion",
      "(ii) Explanability on SHAD cannot be natively solved with existing TSAD methods, and (iii) frozen LLMs are not able to provide correct interpretations of anomalies."),
   ]},
  {"id": "arxiv-2609.38004", "title": None, "fam": ["reconstruction-based-detectors", "deep-learning"], "par": ["unsupervised"],
   "proposes": ["MSCAD (multi-scale autoencoder with bidirectional cross-scale attention)"],
   "claims": [
     ("Most TSAD methods use a single temporal granularity; MSCAD exchanges information among parallel autoencoders at different patch sizes.", "Abstract",
      "most existing TSAD methods commit to a single temporal granularity"),
     ("On TSB-AD, MSCAD reports large gains over 50 baselines (VUS-PR on univariate and multivariate splits).", "Abstract",
      "MSCAD achieves large performance gains against 50 baselines across multiple metrics"),
     ("VUS-PR is the primary metric because, unlike point-adjusted F1, it is threshold-free and not gameable by random scores.", "Evaluation",
      "unlike Point-Adjusted F1 (PA-F1) it is threshold-free and not gameable by random scores."),
     ("Thresholded F1 variants in the TSB-AD implementation are reported at the best threshold and can be sensitive to threshold selection and point adjustment.", "Evaluation metrics (appendix)",
      "These metrics are useful for diagnosing detector behavior but can be sensitive to threshold selection and, in some cases, to point-adjustment effects."),
   ]},
  {"id": "arxiv-2609.31470", "title": None, "fam": ["deep-learning"], "par": ["unsupervised"],
   "proposes": ["SBOG: Sinkhorn boundary outlier generation"],
   "claims": [
     ("SBOG generates boundary outliers in latent space using Sinkhorn optimal transport and distributionally robust boundary modeling.", "Abstract",
      "We therefore propose Sinkhorn Boundary Outlier Generation (SBOG), a structured framework for latent-space outlier generation"),
     ("For time-series anomaly detection, main tables use point-wise evaluation without point adjustment to avoid overestimation.", "Experiments",
      "our main tables use the stricter point-wise evaluation without Point Adjustment."),
   ]},
  {"id": "arxiv-2609.28022", "title": None, "fam": ["reconstruction-based-detectors"], "par": ["unsupervised"],
   "proposes": ["PISCES: physics-informed convolutional autoencoder for solar-wind anomaly detection"],
   "claims": [
     ("PISCES is trained without catalog labels under physics constraints and decomposes the anomaly score into physical contributions.", "Abstract",
      "At inference, PISCES separates the anomaly score into magnetic and plasma reconstruction errors, physics relations, and resid- ual corrections"),
     ("Evaluation uses PR-AUC because point-adjusted F1 can make random scores look competitive.", "Evaluation",
      "Point-adjusted F1 can make random anomaly scores appear competitive [41]"),
     ("Attenuating skip connections improves average precision of trained models while untrained scores stay nearly the same.", "Abstract",
      "Attenuation of the skip connections, selected on validation data, improves average precision for the trained models, while the untrained scores remain nearly the same."),
   ]},
  {"id": "arxiv-2608.01885", "title": None, "fam": ["reconstruction-based-detectors", "deep-learning"], "par": ["unsupervised"],
   "proposes": ["CARE: cascaded inference with a lightweight pre-filter"],
   "claims": [
     ("CARE routes only uncertain samples to the expensive detector, giving 2.7x-4.8x inference speedup while keeping competitive quality.", "Abstract",
      "By routing only uncertain samples to the CDM, our framework achieves 2.7× to 4.8× inference speedup compared to the most accurate SOTA approaches, while still maintaining competitive detection quality."),
     ("Detection quality is reported with Affiliated-F1 and AUC-PR.", "Experiments (Table 1 caption)",
      "Table 1: Average Aff-F (Affiliated-F1), A-P (AUC-PR) and Inference time across 8 real-world"),
   ]},
  {"id": "arxiv-2609.39489", "title": None, "fam": ["deep-learning"], "par": ["unsupervised"],
   "proposes": ["SACM: sample-adaptive capacity modulation (adaptive dropout)"],
   "claims": [
     ("SACM assigns sample-wise dropout probabilities using spectral sparsity and plugs into existing backbones.", "Abstract",
      "a task-agnostic frame- work that exploits spectral sparsity to assign sample-wise dropout probabilities along internal activation paths."),
     ("Its anomaly detection gains are reported as point-adjusted F1.", "Abstract",
      "improves classification accuracy and point-adjusted F1 by 3.04% and 17.05%, respectively"),
     ("Anomaly detection comparisons use the benchmark point-adjusted (PA) protocol.", "Anomaly detection experiments",
      "Raw and +SACM share the benchmark point-adjusted (PA) protocol [37, 39] for paired comparison"),
   ]},
  {"id": "arxiv-2609.38789", "title": None, "fam": ["reconstruction-based-detectors", "deep-learning"], "par": ["unsupervised"],
   "proposes": ["LEARN-TS: LLM-derived semantics for masked reconstruction"],
   "claims": [
     ("LEARN-TS uses a frozen language model to build semantic references without paired text.", "Abstract",
      "uses a frozen language model to construct two role separated semantic representations without requiring tempo- rally paired external text."),
     ("Across four benchmarks it achieves the highest mean performance in 13 of 16 dataset-metric comparisons.", "Abstract",
      "Across four benchmarks, LEARN-TS achieves the highest mean performance in 13 of 16 dataset–metric comparisons."),
     ("No point adjustment is applied to any metric.", "Evaluation",
      "No point adjustment is applied to any metric."),
   ]},
  {"id": "arxiv-2610.01223", "title": None, "fam": ["classical-outlier-detectors"], "par": ["unsupervised"],
   "proposes": ["LLM-driven program search for compact, interpretable detectors"],
   "claims": [
     ("An LLM is used as the author of a detector: it repeatedly edits a short NumPy program under a leakage-free objective.", "Abstract",
      "We use a large language model not as the detector but as the author of one"),
     ("The discovered compact detectors lead TSB-AD across metrics, ahead of classical, deep and foundation-model baselines, without training a network or using a GPU.", "Abstract",
      "yet they train no network and use no GPU"),
     ("On TSB-AD it reports affiliation F-measure, temporal F1, point-wise F1 and VUS-PR.", "Metrics",
      "On TSB-AD we follow the Time-RCD protocol and re- port the affiliation F-measure [11]"),
   ]},
  {"id": "arxiv-2610.00978", "title": None, "fam": ["time-series-foundation-model", "classical-outlier-detectors"], "par": ["unsupervised"],
   "proposes": ["TS-Router: routing to specialist detectors with foundation-model representations"],
   "claims": [
     ("Different datasets favor different detection criteria; TS-Router uses foundation-model representations to select specialist detectors per series.", "Abstract",
      "estimates the relative competence of heterogeneous anomaly de- tectors from pretrained temporal representations and selects suitable specialists for each target series."),
     ("Across 16 benchmarks and four metrics it achieves the best overall average rank.", "Abstract",
      "Across 16 real-world benchmarks and four complementary evaluation metrics, TS-Router achieves the best overall aver- age rank."),
     ("It reports VUS-PR, Affiliation-F1, F1T and Standard-F1.", "Metrics",
      "we report VUS-PR, Affiliation-F1, F1T, and Standard-F1"),
   ]},
  {"id": "arxiv-2609.39337", "title": None, "fam": ["deep-learning"], "par": ["unsupervised"],
   "proposes": ["WinoTS: wavelet-based self-distillation pre-training"],
   "claims": [
     ("WinoTS is a self-distillation pre-training paradigm using time-frequency augmentations.", "Abstract",
      "We introduce Wavelet-based self-distillation for time series (WinoTS), an invariance-based pre-training paradigm designed specifically for temporal signals."),
     ("Anomaly detection follows the TSLib protocol and reports point-adjusted precision, recall and F1.", "Anomaly detection experiments",
      "TSLib evaluation protocol and report point-adjusted precision, recall, and F1"),
   ]},
  {"id": "arxiv-2609.39257", "title": None, "fam": ["classical-outlier-detectors"], "par": ["unsupervised"],
   "proposes": ["TAMIS: anomaly detection in daily production forecasts at EDF"],
   "claims": [
     ("TAMIS detects anomalous days in electricity production forecasts and surfaces top-ranked anomalies for human review.", "Abstract",
      "TAMIS surfaces top-ranked anomalies through an automated daily newsletter, enabling efficient expert review and continuous monitoring."),
     ("AUC-ROC overestimates accuracy for rare anomalies, so AUC-PR (plus throughput) is used.", "Evaluation measures",
      "the Area Under the ROC curve (AUC-ROC) tends to overestimate the accuracy of detectors [30]."),
     ("On real industrial data TAMIS gives the best accuracy-efficiency trade-off among baselines.", "Abstract",
      "TAMIS achieves the best accuracy–efficiency trade-off compared to baseline methods."),
   ]},
  {"id": "arxiv-2609.36765", "title": None, "fam": ["deep-learning"], "par": ["unsupervised"],
   "proposes": ["GRASP: flow matching with a graph-spectral path"],
   "claims": [
     ("GRASP builds graph structure into the flow-matching probability path for multivariate TSAD.", "Abstract",
      "we propose GRASP, a flow matching framework with a graph-spectral path for multivariate time series anomaly detec- tion."),
     ("Evaluation uses ROC, PRC and Best-F1, where Best-F1 uses the threshold that maximizes F1.", "Experimental setup",
      "The Best-F1 score measures point-wise detection performance with the threshold that maximizes the"),
   ]},
  {"id": "arxiv-2609.29194", "title": None, "fam": ["time-series-foundation-model", "classical-outlier-detectors"], "par": ["unsupervised", "streaming"],
   "proposes": ["Teacher-student distillation from a time-series foundation model to an online MiniRocket student"],
   "claims": [
     ("A foundation-model teacher (TSPulse) labels data offline and a lightweight student runs online on the robot.", "Abstract",
      "An offline foundation model (TSPulse) generates pseudo-labels from unlabeled time series augmented with fault injections."),
     ("Evaluation uses VUS-PR, which penalizes late detections and prolonged false alarms.", "Evaluation",
      "Unlike standard point-wise metrics, VUS-PR is explicitly designed for range-based time series"),
   ]},
  {"id": "arxiv-2504.06643", "title": None, "fam": ["reconstruction-based-detectors", "deep-learning"], "par": ["unsupervised"],
   "proposes": ["AMAD: AutoMasked attention with Max-Min training and contrastive learning"],
   "claims": [
     ("Existing attention-based detectors assume specific anomaly patterns (e.g. concentrated or peak anomalies), limiting generalization.", "Abstract",
      "the sequence anomaly association assumptions underlying these models are of- ten limited to specific predefined patterns and scenarios"),
     ("It reports precision, recall and F1; the text we checked does not state whether point adjustment is applied or how the threshold is chosen.", "Experiments",
      "We report P (Precision), R (Recall), and F1 (F1-score)"),
   ]},
  {"id": "doi-10.24963_ijcai.2026_276", "title": "AnoMamba: Aligning Reconstruction with Time Series Anomaly Detection via Selective Global Dependency Modeling",
   "authors": ["Junqi Chen", "Xu Tan", "Jie Chen", "Susanto Rahardja"], "year": 2026, "venue": "IJCAI 2026",
   "doi": "10.24963/ijcai.2026/276", "pdf_url": "https://www.ijcai.org/proceedings/2026/0276.pdf",
   "fam": ["reconstruction-based-detectors", "deep-learning"], "par": ["unsupervised"],
   "proposes": ["AnoMamba: Mamba variant with global step-size reweighting"],
   "claims": [
     ("Minimizing reconstruction loss alone lets models reconstruct anomalies well by overfitting local patterns (misalignment between reconstruction and detection).", "Abstract",
      "Consequently, anomalies that violate global de- pendencies can also be reconstructed well, leading to a misalignment between reconstruction and detection."),
     ("Citing Kim et al., it avoids point-adjustment metrics and uses affiliation F1 and VUS-ROC.", "Implemented details",
      "As noted by [Kim et al., 2022], point-adjustment metrics can lead to misleading rankings"),
   ]},
  {"id": "doi-10.24963_ijcai.2026_332", "title": "Multi-View Ensemble for Time Series Anomaly Detection via Coupling Flows",
   "authors": ["Wanghui Qiu", "Chenxi Liu", "Shiyan Hu", "Zhengyu Li", "Chenjuan Guo", "Bin Yang"], "year": 2026, "venue": "IJCAI 2026",
   "doi": "10.24963/ijcai.2026/332", "pdf_url": "https://www.ijcai.org/proceedings/2026/0332.pdf",
   "fam": ["heterogeneous-ensembles", "reconstruction-based-detectors"], "par": ["unsupervised"],
   "proposes": ["FlowFuse: coupling-flow fusion of multi-view anomaly scores"],
   "claims": [
     ("Different anomaly types need different detection mechanisms; FlowFuse fuses four complementary detectors with coupling flows.", "Abstract",
      "Time series anomaly detection faces a critical chal- lenge that different anomaly types require differ- ent detection mechanisms"),
     ("Across 18 benchmarks it reports state-of-the-art performance.", "Abstract",
      "Ex- tensive experiments across 18 diverse benchmarks show that FlowFuse achieves state-of-the-art per- formance"),
     ("Main metrics are AUC-ROC and Affiliated-F1.", "Experiments (Table 3 caption)",
      "Table 3: Average AUC-ROC (A-R) and Affiliated-F1 (Aff-F) accuracy measures for all datasets."),
   ]},
]

META = __import__("json").load(open("/tmp/claude-1000/-home-manaty-algorithm-dictionary/a3a0d11f-f273-487f-98fd-58eb6466a416/scratchpad/tsad2_meta.json"))

for spec in SPECS:
    P = Paper(spec["id"])
    if spec["id"].startswith("arxiv-"):
        aid = spec["id"][len("arxiv-"):]
        m = META[aid]
        title, authors, year, version = m["title"], m["authors"], m["year"], m["version"]
        links, source_extra, venue = {"arxiv": f"https://arxiv.org/abs/{aid}"}, {}, None
    else:
        title, authors, year, version = spec["title"], spec["authors"], spec["year"], "IJCAI proceedings PDF"
        links, source_extra, venue = {"doi": f"https://doi.org/{spec['doi']}"}, {"pdf_url": spec["pdf_url"]}, spec["venue"]
    notes = NOTE
    if spec["id"] == "doi-10.24963_ijcai.2026_332":
        notes += " Five of the six authors are also authors of the TAB benchmark (arxiv-2506.18046)."
    if spec["id"] == "arxiv-2504.06643":
        notes += " The journal version is DOI 10.1016/j.knosys.2026.117110 (closed access); this card uses the arXiv v3 preprint."
    card = {
        "id": spec["id"], "title": title, "authors": authors, "year": year,
        **({"venue": venue} if venue else {}),
        "links": links,
        "source": {"version": version, "retrieved_at": "2026-10-02", "pdf_sha256": P.sha256(), **source_extra},
        "tags": {"tasks": TSAD, "method_families": spec["fam"], "paradigms": spec["par"]},
        "proposes": spec["proposes"],
        "claims": P.claims(spec["claims"]),
        "results": [], "relations": [],
        "card": {"created_at": "2026-10-02", "created_by": "claude-opus-5-5 via Claude Code", "reviewed": False, "notes": notes},
    }
    write_card(card)
    print(spec["id"], len(card["claims"]), "claims")
