---
title: Construction of a multi-label odor prediction model based on molecular structures and olfactory receptor binding profiles with a novel interpretability framework.
authors: "Yuta Wakutsu, Hiromasa Kaneko"
date: 2026-04-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/41973193/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 化学信息学中的分子结构与受体结合预测
tldr: 开发了一个基于分子结构和受体结合的多阶段气味预测框架。
selection_source: fresh_fetch
motivation: 化学信息学中的分子结构与受体结合预测。
method: 方法与实现细节请参考摘要与正文。
result: 结果与对比结论请参考摘要与正文。
conclusion: 总体而言，该工作在所述任务上展示了有效性，并提供了可复用的思路或工具。
---

## Abstract
Predicting odors from molecular structures is a long-standing challenge in chemoinformatics, especially in cases where structurally similar compounds, such as optical isomers, exhibit distinct odor perceptions. To address this, we developed a multi-stage odor prediction framework that integrates both molecular structures and olfactory receptor (OR) binding information. Recognizing that human olfaction is mediated by complex receptor-ligand interactions, we divided the process into three mechanistic stages: (1) prediction of molecular binding to ORs (classification), (2) estimation of binding strength (regression), and (3) prediction of odor presence based on receptor responses (classification). We further introduced a novel interpretability metric, Positive likeness, which estimates the contribution of specific receptors to the likelihood of each odor label. Using this framework, we demonstrated the ability to distinguish odor differences between optical isomers and to identify ORs that are potentially responsible for the perception of specific odor attributes. The model also enabled extrapolative odor prediction for molecules with unknown odor annotations, leveraging receptor information and label propagation. Our results highlight the importance of receptor-level descriptors in enhancing predictive performance and biological interpretability. This study provides a foundation for receptor-guided odor modeling and supports applications in fragrance design and sensory informatics.