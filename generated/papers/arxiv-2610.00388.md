<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# T2SPO: Trajectory-to-Step Policy Optimization for Agentic Reinforcement Learning

- カード: [`arxiv-2610.00388`](../../papers/arxiv-2610.00388.yaml)
- 著者: Bo-Wen Zhang, Junwei He, Maoqi Liu, Feiran Li, Song-Lin Lv, Wentao Ma, Rongyi Lin, Shuhan Zhong, Lan-Zhe Guo
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2610.00388v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, large-language-models, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** A pretrained TabPFN regressor, conditioned on states from past successful trajectories, estimates remaining distance to success; changes in this estimate give auxiliary step credit.([Abstract, p.1](https://arxiv.org/pdf/2610.00388v1#page=1 "Conditioned on these examples, a pretrained TabPFN regressor estimates the remaining distance to success at each state of a new rollout."))
- **c2** With 1.5B and 7B models on ALFWorld and WebShop, T2SPO consistently improves overall task success over GRPO.([Abstract, p.1](https://arxiv.org/pdf/2610.00388v1#page=1 "Experiments with 1.5B and 7B language models on ALFWorld and WebShop show that T2SPO consistently improves overall task success over GRPO."))
- **c3** All baseline results (GRPO, PPO, RLOO, GiGPO, ReAct, base model) are taken from Feng et al. (2025) rather than re-run.([Experimental setup, p.7](https://arxiv.org/pdf/2610.00388v1#page=7 "All baseline results are taken from Feng et al. (2025)."))
- **c4** In offline remaining-distance prediction on WebShop, TabPFN is compared with kNN regression; the lowest observed kNN MAE over tested k is reported for each context budget.([Comparison with Nearest Neighbors, p.8](https://arxiv.org/pdf/2610.00388v1#page=8 "We test 𝑘∈{8, 16, 𝑀/4, 𝑀/2, 𝑀} and plot the lowest observed kNN MAE at each budget (Figure 2b)."))
- **c5** Limitation: a fixed proportion of failure examples has mixed effects, motivating adaptive supervision.([Limitations, p.10](https://arxiv.org/pdf/2610.00388v1#page=10 "The mixed effects of a fixed proportion of failure examples motivate supervision that adapts to the task and the agent’s experience."))

