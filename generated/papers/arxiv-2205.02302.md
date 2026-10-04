<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# Machine Learning Operations (MLOps): Overview, Definition, and Architecture

- カード: [`arxiv-2205.02302`](../../papers/arxiv-2205.02302.yaml)
- 著者: Dominik Kreuzberger, Niklas Kühl, Sebastian Hirschl
- 年・掲載: 2022
- 原論文: [PDF](https://arxiv.org/pdf/2205.02302v3)(arXiv v3、カード作成時に読んだ版)
- タグ: automl-systems, mlops
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** Method: mixed-method study combining a structured literature review (search in May 2021: 1,864 retrieved, 194 screened in detail, 27 selected, all peer-reviewed), a tool review, and semi-structured interviews (June to August 2021) with eight experts identified via LinkedIn under a theoretical sampling approach, conducted until no new categories and concepts emerged (theoretical saturation).([Methodology, p.2](https://arxiv.org/pdf/2205.02302v3#page=2 "In total, we conduct eight interviews with experts (α - θ), whose details are depicted in Table 2 of the Appendix."))
- **c2** Definition: MLOps is a paradigm (best practices, concepts, development culture) covering end-to-end conceptualization, implementation, monitoring, deployment and scalability of ML products; the authors describe it as an engineering practice drawing on ML, software engineering (especially DevOps) and data engineering.([Conceptualization, p.8](https://arxiv.org/pdf/2205.02302v3#page=8 "MLOps (Machine Learning Operations) is a paradigm, including aspects like best practices, sets of concepts, as well as a development culture when it comes to the end-to-end conceptualization, implementation, monitoring, deployment, and scalability of machine learning products."))
- **c3** Monitoring component (C9): continuously monitors model serving performance (e.g., prediction accuracy); monitoring of ML infrastructure, CI/CD and orchestration is also required (both statements are backed in the paper by literature citations and interviewee markers). Tool examples, each attributed to interviewees, include Prometheus with Grafana, the ELK stack and TensorBoard.([Technical Components, p.4](https://arxiv.org/pdf/2205.02302v3#page=4 "The monitoring component takes care of the continuous monitoring of the model serving performance (e.g., prediction accuracy)."))
- **c4** Alert path in the proposed workflow: the monitoring component observes serving performance and infrastructure in real time, and once a threshold is reached (e.g., low prediction accuracy detected) the information is forwarded via a feedback loop to upstream receivers (experimental stage, data engineering zone, scheduler).([Architecture and Workflow, p.7](https://arxiv.org/pdf/2205.02302v3#page=7 "Once a certain threshold is reached, such as detection of low prediction accuracy, the information is forwarded via the feedback loop."))
- **c5** Retraining triggers: when the monitoring component detects drift in the data, the scheduler triggers the automated ML workflow pipeline for retraining (continuous training); drift can be detected with distribution comparisons, and retraining can also be triggered by new feature data or run periodically.([Architecture and Workflow, p.8](https://arxiv.org/pdf/2205.02302v3#page=8 "Retraining is not only triggered automatically when a statistical threshold is reached; it can also be triggered when new feature data is available, or it can be scheduled periodically."))
- **c6** Model registry and promotion: retrained models are pushed to the model registry, the metadata store records model version and status (e.g., staging or production-ready), and switching a well-performing model's status from staging to production hands it over for deployment via the continuous deployment pipeline.([Architecture and Workflow, p.7](https://arxiv.org/pdf/2205.02302v3#page=7 "Once the status of a well-performing model is switched from staging to production, it is automatically handed over to the DevOps engineer or ML engineer for model deployment."))
- **c7** Operational challenge reported (citing literature [18] and interviewee θ): a constant stream of new data forces retraining capabilities, a repetitive task requiring a high level of automation; the resulting artifacts need strong governance and versioning of data, model and code (further citations).([Open Challenges, p.8](https://arxiv.org/pdf/2205.02302v3#page=8 "Also, a constant incoming stream of new data forces retraining capabilities."))

