<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Energy and Policy Considerations for Deep Learning in NLP

- カード: [`arxiv-1906.02243`](../../papers/arxiv-1906.02243.yaml)
- 著者: Emma Strubell, Ananya Ganesh, Andrew McCallum
- 年・掲載: 2019
- 原論文: [PDF](https://arxiv.org/pdf/1906.02243v1)(arXiv v1、カード作成時に読んだ版)
- タグ: deep-learning, efficiency-evaluation
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Contribution: the paper quantifies the approximate financial and environmental costs of training a variety of recently successful neural NLP models, and proposes recommendations to reduce costs and improve equity.([Abstract, p.1](https://arxiv.org/pdf/1906.02243v1#page=1 "In this paper we bring this issue to the attention of NLP researchers by quantifying the approximate ﬁnancial and environmental costs of training a variety of recently successful neural network models for NLP."))
- **c2** Measurement: the off-the-shelf models are trained with the default settings provided (each for a maximum of 1 day, on a single NVIDIA Titan X GPU except ELMo on 3 GTX 1080 Ti GPUs) while GPU power is sampled via nvidia-smi (averaged over samples) and CPU power via Intel's RAPL interface; the full training runs are not performed.([Methods, p.2](https://arxiv.org/pdf/1906.02243v1#page=2 "We train the models described in §2.1 using the default settings provided, and sample GPU and CPU power consumption during training."))
- **c3** Extrapolation: the total training time to completion is not measured but estimated from the training times and hardware reported in the original papers; energy is then the combined GPU, CPU and DRAM power draw multiplied by that time.([Methods, p.2](https://arxiv.org/pdf/1906.02243v1#page=2 "We estimate the total time expected for models to train to completion using training times and hardware reported in the original papers."))
- **c4** Assumption: data-center overhead (mainly cooling) is accounted for with a fixed Power Usage Effectiveness coefficient equal to the 2018 global data-center average.([Methods, p.2](https://arxiv.org/pdf/1906.02243v1#page=2 "We use a PUE coefﬁcient of 1.58, the 2018 global average for data centers (Ascierto, 2018)."))
- **c5** Assumption: energy is converted to CO2e using the U.S. EPA average CO2 per kWh; the authors justify this by the U.S. energy mix being comparable to that of Amazon Web Services.([Methods, p.3](https://arxiv.org/pdf/1906.02243v1#page=3 "The U.S. breakdown of energy is comparable to that of the most popular cloud compute service, Amazon Web Services, so we believe this conversion to provide a reasonable estimate of CO2 emissions per kilowatt hour of compute energy used."))
- **c6** Limitation: for TPU-trained models only cloud compute cost is estimated; power and carbon footprint are omitted because TPU power draw is not publicly available.([Experimental results (Table 3 caption), p.4](https://arxiv.org/pdf/1906.02243v1#page=4 "Power and carbon footprint are omitted for TPUs due to lack of public information on power draw for this hardware."))
- **c7** Recommendations: report time to retrain and sensitivity to hyperparameters, give academic researchers equitable access to compute, and prioritize efficient models and hardware.([Introduction, p.2](https://arxiv.org/pdf/1906.02243v1#page=2 "(1) Time to retrain and sensitivity to hyperparameters should be reported for NLP machine learning models; (2) academic researchers need equitable access to computational resources; and (3) researchers should prioritize developing efﬁcient models and hardware."))

