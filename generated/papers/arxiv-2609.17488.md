<!-- このファイルは scripts/generate.py が生成する。手で編集しない。 -->

# LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence

- カード: [`arxiv-2609.17488`](../../papers/arxiv-2609.17488.yaml)
- 著者: Xingxuan Zhang, Gang Ren, Hao Yuan, Hao Zou, Hongze Tan, Hui Wang, Jianhao Song, Jiansheng Li, Jiayao Zhang, Jinghan Zhang, Kaifang Li, Lang Mo, Li Mao, Mingchao Hao, Nuo Xu, Rui Ding, Ruiji Zhang, Shuyang Li, Siyu Mei, Tianyang Zhang, Weiyang Mu, Yancheng Dong, Yongxian Wei, Yuan Xue, Yuanrui Wang, Yue He, Zijia Yang, Ziyun Li, Dongzhe Li, Fuqiang Wang, Jiandong Liu, Jiawei Chen, Jiaxin Du, Kaijie Cheng, Kehan Li, Lei Sun, Linjun Zhou, Ningbo Dai, Qi Wang, Renzhe Xu, Shaoxing Du, Shumeng Yang, Wang Lu, Wenjing Chu, Xiannan Huang, Xiaoyu Lin, Xing Ai, Xinyan Han, Xuanyue Li, Xuanyue Su, Xukun Zhang, Yan Lu, Yaxin Zhang, Yi Qin, Yifei Huang, Yihan Xu, Yongle Lv, Yuanyuan Jiang, Yushan Han, Peng Cui
- 年・掲載: 2026
- 原論文: [PDF](https://arxiv.org/pdf/2609.17488v1)(arXiv v1、カード作成時に読んだ版)
- タグ: in-context-learning, tabular-attention, tabular-classification, tabular-foundation-model, tabular-regression
- 人手レビュー: 未

## 主張

出典のリンクは原論文PDFの該当ページを開く。リンクにカーソルを合わせると原文の引用が表示される。

- **c1** LimiX-2 uses the Contextual Mechanism Networks paradigm and is pretrained with Context-Conditional Masked Modeling.([Abstract, p.1](https://arxiv.org/pdf/2609.17488v1#page=1 "LimiX-2 adopts the Contextual Mechanism Networks (CMNs) paradigm and is pretrained with Context-Conditional Masked Modeling (CCMM)."))
- **c2** On TabArena, TALENT and BCCO, LimiX-2 outperforms current dataset-specific models and tabular foundation models.([Abstract, p.1](https://arxiv.org/pdf/2609.17488v1#page=1 "Evaluations on TabArena, TALENT, and BCCO show that LimiX-2 outperforms current dataset-specific models and tabular foundation models."))
- **c3** For TabArena, baseline scores are taken from the published leaderboard (accessed September 15, 2026) and Elo is computed with the official TabArena pipeline.([Experimental setup, p.10](https://arxiv.org/pdf/2609.17488v1#page=10 "We take the published leaderboard scores as the reference for existing baselines (accessed September 15, 2026) and then report the Elo rating computed by the official TabArena evaluation pipeline, ensuring direct comparability with the leaderboard results."))
- **c4** On TALENT and BCCO, models integrated in the TALENT library are run with their default configurations, including model-specific hyperparameter settings.([Experimental setup, p.11](https://arxiv.org/pdf/2609.17488v1#page=11 "For models integrated into the TALENT library, we use their default configurations, including model-specific hyperparameter settings."))
- **c5** Twelve TALENT classification datasets with more than 10 target classes are excluded, leaving 288 datasets.([Experimental setup, p.10](https://arxiv.org/pdf/2609.17488v1#page=10 "Excluding 12 classification datasets with more than 10 target classes, we perform evaluation on the remaining 288 datasets."))
- **c6** One of the three benchmarks, BCCO, is cited as a 2025 work of the LimiX Team, the same team that authors this report.([Experimental setup, p.10](https://arxiv.org/pdf/2609.17488v1#page=10 "Three widely adopted benchmarks, TabArena (Erickson et al., 2025), TALENT (Ye et al., 2024; Liu et al., 2024), and BCCO (LimiX Team, 2025), are used for evaluation."))

