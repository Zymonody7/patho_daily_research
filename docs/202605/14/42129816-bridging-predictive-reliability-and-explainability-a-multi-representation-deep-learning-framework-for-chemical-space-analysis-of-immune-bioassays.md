---
title: "Bridging predictive reliability and explainability: a multi-representation deep learning framework for chemical space analysis of immune bioassays."
title_zh: 连接预测可靠性与可解释性：一种用于免疫生物测定化学空间分析的多表征深度学习框架
authors: "V A Jyothy, Maya L Pai, E Pa Sandesh, U C A Jaleel"
date: 2026-05-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/42129816/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于化学空间分析的多表征深度学习
tldr: 针对免疫靶点虚拟筛选中预测精度与可解释性难以平衡的问题，本研究构建了一个整合分子描述符、图像和图结构多模态输入的基准框架。通过对比多种机器学习与深度学习模型，发现 AttentiveFP 架构结合概念白化（Concept Whitening）技术能在保持高预测可靠性的同时，提取并对齐关键的化学领域概念。该框架不仅提升了免疫生物测定的筛选效率，还为理解配体与免疫靶点的相互作用提供了可解释的科学依据。
selection_source: fresh_fetch
motivation: 旨在解决免疫相关生物测定虚拟筛选中，分子表示、学习算法与模型可解释性之间缺乏协同作用的问题。
method: 建立了一个涵盖描述符、图像和图结构的基准框架，并将概念白化技术集成到 AttentiveFP 深度学习模型中以实现决策过程的透明化。
result: 在对比实验中，SVM 在传统模型中表现最强，而 AttentiveFP 在深度学习中表现最佳，且成功识别出支撑假设生成的潜在领域概念。
conclusion: 该研究通过多模态深度学习框架实现了预测性能与可解释性的统一，为免疫靶点药物研发提供了可靠的决策支持工具。
---

## 摘要
化学空间与生物空间向统一决策空间的融合，需要分子表征、学习算法和可解释性这三者之间的协调交互。本研究建立了一个虚拟筛选（VS）基准框架，整合了上述三要素，以实现对复杂免疫相关生物测定的一致性、预测性和可解释性建模。研究在三种分子输入模态（描述符、图像和图）中采用了广泛的机器学习（ML）和深度学习（DL）模型，同时优先考虑预测可靠性和模型可解释性。在经典机器学习模型中，支持向量机（SVM）表现出最强的综合性能，而 AttentiveFP 架构则优于其他深度学习模型。除了识别特定背景下的最优虚拟筛选网络外，本研究还推导出了潜在的学习概念，为随后关于免疫靶点与配体相互作用的假设生成和实验验证提供支持。科学贡献：本研究通过整理具有代表性的生物测定数据集，系统评估多种分子表征和学习算法，并将可解释性集成到性能最佳的模型中，建立了免疫靶点虚拟筛选的基准框架。通过将概念白化（Concept Whitening）与 AttentiveFP 架构相结合，我们引入了一个集成式可解释深度学习框架，该框架在保持预测可靠性的同时，能够实现免疫靶点虚拟筛选中领域特定概念的对齐与分离。此外，研究强调了决策级和逻辑级模型集成的潜力，识别了决策过程中特定靶点的概念相关性，并展示了数据特征与模型行为之间的关系。

## Abstract
Convergence of chemical and biological space into a unified decision space requires coordinated interactions across the triad- molecular representations, learning algorithms, and explainability. This study establishes a benchmarking framework for Virtual Screening (VS) that integrates this triad to enable consistent, predictive, and interpretable modelling of complex immune-related bioassays. The study employed a wide range of Machine Learning (ML) and Deep Learning (DL) models across three molecular input modalities-descriptors, images, and graphs-while prioritizing predictive reliability and model interpretability. Among classical ML models, Support Vector Machines (SVM) demonstrated the strongest overall performance, while the AttentiveFP architecture outperformed other DL models. Beyond identifying context-specific optimal VS networks, this study derives latent learned concepts that support subsequent hypothesis generation and experimental validation of the interaction between immune targets and ligands.Scientific contributionThis study establishes a benchmarking framework for virtual screening of immune targets by curating representative bioassay datasets, systematically evaluating multiple molecular representations and learning algorithms, and integrating explainability into the best-performing models. By combining Concept Whitening with the AttentiveFP architecture, we introduce an integrated explainable DL framework that maintains predictive reliability while enabling alignment and separation of domain-specific concepts for immune-target virtual screening. In addition, the study highlights the potential for decision- and logical-level model ensembling, identifies target-specific concept relevance in decision-making, and demonstrates the relationship between data characteristics and model behaviour.