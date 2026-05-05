---
title: "Rheumatic Digital Twin: Proposed Machine Learning-Based Multimodal Framework to Inform Clinical Decision-Making."
title_zh: 风湿病数字孪生：一种旨在辅助临床决策的基于机器学习的多模态框架
authors: "Daniyal Selani, Rachel Knevel, Marcel Reinders, Erik B van den Akker"
date: 2026-05-04
pdf: "https://pubmed.ncbi.nlm.nih.gov/42081548/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 整合电子健康记录、影像和组学的多模态框架
tldr: 风湿性疾病具有高度异质性和长期演变特征，传统的单次快照式评估难以捕捉其复杂病程。该研究提出了“风湿数字孪生”框架，通过整合电子病历、影像和组学等多模态数据，利用Transformer架构对患者病史进行序列建模。该框架旨在通过寻找临床特征相似的“近邻”患者，实现对疾病进展和治疗反应的精准预测，为临床决策提供动态、个性化的参考。
selection_source: fresh_fetch
motivation: 现有的风湿病临床评估多依赖于碎片化的单次检查，无法有效利用患者长期的多模态数据来应对疾病的高度复杂性。
method: 提出一种基于Transformer和领域大模型的模块化框架，将患者的各项临床事件转化为序列Token，并通过联合嵌入技术融合多源异构数据。
result: 该框架通过在潜在空间中映射患者相似性，能够识别具有相似轨迹的历史病例，从而模拟预测特定患者的治疗效果和疾病演变。
conclusion: 这种数字孪生架构为风湿病的精准医疗提供了新思路，有望通过模拟患者旅程来优化个性化治疗方案。
---

## 摘要
风湿性疾病是慢性免疫介导的疾病，其临床表现和病程具有显著的异质性。然而，目前的临床方法通常依赖于基于快照的评估，无法捕捉这些疾病复杂的纵向演变。为了解决这些局限性并支持精准医学的实施，我们提出了“风湿病数字孪生”（Rheumatic Digital Twin）的设计方案。这是一个新颖的模块化概念框架，旨在将异构多模态数据（涵盖电子健康记录、临床笔记、影像学和组学数据）整合为患者病程的动态计算表示。我们的理论架构通过多阶段方法解决了数据孤岛和数据模态可用性不一的挑战，设想利用领域特定的基础模型来独立处理不同的数据模态。为了有效模拟慢性疾病固有的时间演进，所提出的设计采用了 Transformer 架构，利用自注意力机制将患者事件（如化验结果或用药变更）视为序列数据标记。我们描述了如何随后通过联合嵌入技术融合这些单模态表示，以构建一个共享的多模态表示空间。风湿病数字孪生框架被设想为类似于推荐系统的功能，旨在将患者映射到一个潜在空间中，其中的邻近程度反映了临床和生物学上的相似性。通过识别“最近邻”（即具有相似轨迹的历史患者），该系统旨在实现计算机模拟队列研究，理论上允许临床医生根据相似同行的结果来预测关键临床事件、预测治疗反应并确定可能的疾病演变过程。

## Abstract
Rheumatic diseases are chronic, immune-mediated conditions characterized by significant heterogeneity in presentation and disease course. However, current clinical approaches often rely on snapshot-based assessments that fail to capture the complex longitudinal evolution of these conditions. To address these limitations and support the implementation of precision medicine, we present the design for the Rheumatic Digital Twin, a novel, modular conceptual framework intended to integrate heterogeneous multimodal data, ranging from electronic health records and clinical notes to imaging and omics, into a dynamic, computational representation of the patient journey. Our theoretical architecture addresses challenges related to data silos and variable availability of data modalities through a multistage approach that envisions the use of domain-specific foundation models to independently process distinct data modalities. To effectively model the temporal progression inherent in chronic diseases, the proposed design utilizes Transformer architectures, leveraging self-attention mechanisms to treat patient events, such as lab results or medication changes, as sequential data tokens. We describe how these unimodal representations would subsequently be fused via joint embedding techniques to construct a shared, multimodal representational space. Envisioned to function analogously to a recommender system, the Rheumatic Digital Twin framework is modeled to map patients into a latent space where proximity reflects clinical and biological similarity. By identifying "nearest neighbors," historical patients with comparable trajectories, the system aims to enable in silico cohorting, theoretically allowing clinicians to forecast key clinical events, predict treatment responses, and identify likely disease courses based on the outcomes of similar peers.