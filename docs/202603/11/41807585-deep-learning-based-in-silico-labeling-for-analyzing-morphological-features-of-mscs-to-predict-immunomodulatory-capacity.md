---
title: Deep learning-based in silico labeling for analyzing morphological features of MSCs to predict immunomodulatory capacity.
title_zh: 基于深度学习的计算机模拟标记用于分析 MSCs 形态特征以预测其免疫调节能力
authors: "Zhiyu Liu, Gang An, Xiao Liang, Xumin Wu, Junyuan Hu, Haijun Wang, Jingfeng Ou, Xiuping Zeng, Zhiliang Xia, Kaixiang Hou, Wanglong Chu, Jianbin Ye, Cui Liao, Zhengmian Zhang, Muyun Liu"
date: 2026-03-10
pdf: "https://pubmed.ncbi.nlm.nih.gov/41807585/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 深度学习用于细胞形态和免疫调节能力预测
tldr: 针对间充质干细胞（MSC）质量评估中传统标记方法具有侵入性且耗时的问题，本研究开发了一种结合深度学习与机器学习的非侵入性框架。该框架利用改进的 PreAct-ResNet50 进行细胞及细胞核的高精度实例分割并提取形态学特征，随后通过 LightGBM 模型预测免疫调节生物标志物。实验证明该系统能有效评估 MSC 效力，为细胞治疗制造中的实时质量控制提供了高效工具。
selection_source: fresh_fetch
motivation: 传统的干细胞检测依赖侵入性染色，不仅会破坏细胞活性，且难以实现自动化的实时质量监测。
method: 结合 PreAct-ResNet50 实例分割模型与 LightGBM 回归模型，通过非侵入性的图像分析提取细胞形态特征并预测其免疫调节能力。
result: 该框架在细胞与细胞核分割任务中达到了高精度，并成功建立了形态学特征与 MSC 免疫标志物之间的预测关联。
conclusion: 研究验证了利用深度学习进行“计算机模拟标记”来评估干细胞效力的有效性，为细胞治疗的标准化生产提供了新工具。
---

## 摘要
细胞形态是生物学特性的关键表现，与功能密切相关。在传统的细胞检测中，侵入性标记和检测方法不仅会损害细胞活力，还涉及劳动密集型的工作流程。在此，我们提出了一种非侵入性人工智能框架，该框架集成了深度学习（DL）和机器学习（ML），通过形态分析来预测间充质干细胞（MSCs）的免疫调节能力。改进的 PreAct-ResNet50 编码器-解码器架构被用于实现细胞和细胞核的高精度实例分割，从而实现了形态特征的量化。随后，采用基于 LightGBM 的预测模型，通过形态特征预测 MSCs 的免疫调节生物标志物。性能测试表明，该双模型系统展示了令人满意的细胞分割和生物学特性预测能力。我们的方法为实时 MSCs 效力评估提供了一种高效、非侵入性的工具，可增强细胞治疗制造中的质量控制。

## Abstract
Cellular morphology, a critical manifestation of biological characteristics, is linked to functions. In traditional cell detection, invasive labeling and detection methods not only compromise cellular viability but also entail labor-intensive workflows. Here we presented a non-invasive artificial intelligence framework that integrated deep learning (DL) and machine learning (ML) to predict the immunomodulatory capacity of mesenchymal stem cells (MSCs) through morphological profiling. The improved PreAct-ResNet50 encoder-decoder architecture was used to achieve high-accuracy instance segmentation of cells and nuclei, enabling quantification of morphological features. A LightGBM-based predictive model was subsequently employed to predict MSCs immunomodulatory biomarkers through morphological features. This dual-model system demonstrated satisfactory cell segmentation and biological characteristics prediction capabilities through performance testing. Our method provided an efficient, non- invasive tool for real-time MSCs potency assessment, which could enhance quality controls in cell therapy manufacturing.