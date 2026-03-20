---
title: "Multiscale-Aware Graph Embedding Approach Uncovers LC-61, a Potent Anti-"
title_zh: 多尺度感知图嵌入方法发现 LC-61，一种强效抗利什曼病药物
authors: "Vinícius Alexandre Fiaia Costa, Alexandra Maria Dos Santos Carvalho, Rafael Consolin Chelucci, Felipe da Silva Mendonça de Melo, Gustavo Santos Sandes Felizardo, Clarissa Alves Carneiro Bernardes, Holli-Joi Martin, Rodolpho de Campos Braga, Sébastien Charneau, Eugene N Muratov, Adriano Defini Andricopulo, Izabela Marques Dourado Bastos, Bruno Junior Neves"
date: 2026-03-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41841344/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于识别抗利什曼原虫化合物的图神经网络框架
tldr: 针对内脏利什曼病治疗药物匮乏的问题，本研究开发了一种融合多尺度感知机制的图神经网络（GNN）框架，用于提高抗利什曼原虫化合物的筛选精度。该模型在多个数据集上的预测性能显著优于传统GNN，并从130万个化合物中成功筛选出高活性分子LC-61。LC-61表现出纳摩尔级的抗原虫活性和极低的细胞毒性，为该疾病的药物研发提供了具有潜力的新型先导化合物。
selection_source: fresh_fetch
motivation: 现有的内脏利什曼病治疗方案有限，急需通过创新的计算方法加速高效、低毒的新药发现过程。
method: 提出了一种集成多尺度嵌入机制的图神经网络框架，通过捕捉分子在不同空间尺度上的结构特征来增强属性预测能力。
result: 该模型在筛选130万个化合物后发现了LC-61，其对婴儿利什曼原虫的IC50达0.076 μM，且具备良好的溶解度和渗透性。
conclusion: 这种多尺度感知的图学习方法有效加速了活性分子的发现，验证了AI在复杂寄生虫病药物筛选中的实用价值。
---

## 摘要
由婴儿利什曼原虫（Leishmania infantum）引起的内脏利什曼病仍然是一种致命疾病，且治疗选择有限，因此需要创新的计算方法和途径来加速药物研发。在此，我们提出了一种图神经网络（GNN）框架，该框架结合了成熟的多尺度机制，以提高新型抗利什曼病化合物的识别能力。在两个分类抗利什曼病数据集上，与默认 GNN 相比，我们的 GNN 在预测性能上表现出显著提升：在不平衡数据集（活性阈值：1 μM）上，受试者工作特征曲线下面积（AUC）提高了 2.2-29.2%；在平衡数据集（活性阈值：10 μM）上提高了 3.4-22.5%。随后，该框架被应用于筛选包含约 130 万个化合物的库，确定了 LC-61 是一种强效抗利什曼病药物，对细胞内婴儿利什曼原虫具有纳摩尔级活性（IC50 = 0.076 μM），且对巨噬细胞的细胞毒性极低（THP-1 CC50 = 157 μM）。全面的体外 ADME 分析显示，LC-61 兼具在酸性和生理 pH 条件下的高溶解度（>28 μg/mL）、平衡的亲脂性（eLogD = 4.07）和良好的被动渗透性（PAMPA = 4.86 × 10-6 cm/s），同时表现出较低的微粒体稳定性。总之，我们的 GNN 框架有效地加速了 LC-61 的发现，这是一种经过生物学验证的新型命中化合物，适用于从命中化合物到先导化合物（hit-to-lead）的优化。

## Abstract
Visceral leishmaniasis caused by Leishmania infantum remains a lethal disease with few therapeutic options, necessitating innovative computational methods and approaches to accelerate drug discovery. Here, we present a graph neural network (GNN) framework incorporating well-established multiscale mechanisms to improve the identification of novel antileishmanial compounds. Across two classificatory antileishmanial data sets, our GNNs demonstrated significant improvements in predictive performance, with area under the receiver operating characteristic curve (AUC) increases of 2.2-29.2% on the imbalanced data set (activity cutoff: 1 μM) and 3.4-22.5% on the balanced data set (activity cutoff: 10 μM) compared to default GNNs. Subsequently, the framework was applied to screen a library of approximately 1.3 million compounds, pinpointing LC-61 as a potent antileishmanial agent with nanomolar activity against intracellular L. infantum (IC50 = 0.076 μM) and minimal cytotoxicity to macrophages (THP-1 CC50 = 157 μM). A comprehensive in vitro ADME profiling revealed that LC-61 combines high solubility at both acidic and physiological pH (>28 μg/mL), balanced lipophilicity (eLogD = 4.07), and favorable passive permeability (PAMPA = 4.86 × 10-6 cm/s), while exhibiting lower microsomal stability. Overall, our GNN framework effectively accelerated the discovery of LC-61, a novel and biologically validated hit suitable for hit-to-lead optimization.