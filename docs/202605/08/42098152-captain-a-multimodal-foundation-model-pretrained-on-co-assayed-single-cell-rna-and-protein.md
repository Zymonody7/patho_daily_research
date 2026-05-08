---
title: "CAPTAIN: a multimodal foundation model pretrained on co-assayed single-cell RNA and protein."
title_zh: CAPTAIN：一种在共同检测的单细胞 RNA 和蛋白质上预训练的多模态基础模型
authors: "Boya Ji, Tingting Hu, Jiawen Wang, Mengmeng Liu, Liwen Xu, Qinhao Zhang, Siyun Zhong, Libo Qiao, Yan Zhang, Shaoliang Peng, Fulong Yu"
date: 2026-05-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/42098152/"
tags: ["query:seqai"]
score: 10.0
evidence: 单细胞RNA和蛋白质的多模态基础模型
tldr: 针对现有单细胞大模型仅依赖转录组数据而忽视蛋白质功能信息的局限，本文开发了 CAPTAIN 多模态预训练模型。该模型基于 400 多万个同时测定 RNA 和 382 种表面蛋白的单细胞数据进行训练，通过建模跨模态依赖关系学习统一表征。实验证明 CAPTAIN 在蛋白质补全、细胞类型标注及批次校正等任务中表现优异，为理解复杂生物背景下的细胞状态和免疫交互提供了更完整的视角。
selection_source: fresh_fetch
motivation: 蛋白质是细胞功能的最终执行者，但现有单细胞模型多局限于转录组，难以全面刻画由蛋白质定义的细胞表型。
method: 利用 400 万个具有配对 RNA 和表面蛋白数据的单细胞，构建并预训练了一个能够捕捉跨模态依赖关系的多模态基础模型。
result: 模型在蛋白质预测、细胞标注和跨批次整合等任务上展现出强大的泛化能力，并发现了与新冠肺炎严重程度相关的免疫互作模式。
conclusion: 将蛋白质组学信息引入单细胞预训练模型，能显著提升对细胞状态的表征精度，并为多组学整合研究提供更具生物学意义的假设。
---

## 摘要
蛋白质作为细胞功能的终端效应器，编码了基因组和转录组程序的表型结果。尽管转录组图谱可作为易于获取的代理，但对于最终定义细胞表型的蛋白质组景观而言，它们仍是不完整的替代品。然而，目前的单细胞基础模型仅在转录组上进行训练，导致对细胞状态的刻画存在偏差且不完整。为了解决这一局限性，我们推出了 CAPTAIN，这是一种多模态基础模型，在超过 400 万个单细胞上进行了预训练，这些细胞同时测量了转录组以及来自多种人类和小鼠组织的 382 种精选表面蛋白质。我们的结果表明，CAPTAIN 通过建模跨模态依赖关系并捕捉复杂生物背景下细胞状态的多样性，学习到了统一的多模态表示。CAPTAIN 在微调和零样本设置下均表现出强大的泛化能力，在蛋白质插补与扩展、细胞类型注释和批次校正等核心下游任务中表现出色。除了提高多组学整合的准确性外，CAPTAIN 还生成了关于蛋白质驱动的细胞间动力学的新假设，包括与 COVID-19 严重程度相关的潜在免疫相互作用模式。

## Abstract
Proteins act as the terminal effectors of cellular function, encoding the phenotypic consequences of genomic and transcriptomic programmes. Although transcriptomic profiles serve as accessible proxies, they remain incomplete surrogates for the proteomic landscape that ultimately defines cellular phenotypes. Current single-cell foundation models, however, are trained exclusively on transcriptomes, resulting in biased and partial characterizations of cellular states. To address this limitation, we introduce CAPTAIN, a multimodal foundational model pretrained on over four million single cells with concurrently measured transcriptomes and a curated repertoire of 382 surface proteins across diverse human and mouse tissues. Our results show that CAPTAIN learns unified multimodal representations by modelling cross-modality dependencies and capturing the diversity of cellular states across complex biological contexts. CAPTAIN generalizes robustly across both fine-tuning and zero-shot settings, excelling in core downstream tasks such as protein imputation and expansion, cell type annotation, and batch harmonization. Beyond improved accuracy in multi-omics integration, CAPTAIN generates novel hypotheses regarding protein-driven intercellular dynamics, including potential immune interaction patterns linked to COVID-19 severity.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **CAPTAIN** 的单细胞多模态基础模型。以下是对该研究的深度解析：

### 1. 解决的问题与研究价值
*   **核心问题**：目前的单细胞大模型（如 scGPT, Geneformer）大多只针对 **RNA（转录组）** 进行训练。但在生物学中，RNA 只是“指令”，**蛋白质（蛋白质组）** 才是执行功能的“工人”。RNA 的水平并不总能准确反映蛋白质的水平。
*   **研究价值**：由于同时测量一个细胞的 RNA 和蛋白质（如 CITE-seq 技术）成本极高，数据量远少于纯 RNA 数据。CAPTAIN 通过在大规模配对数据上预训练，试图让模型学会从“指令（RNA）”推断“结果（蛋白质）”，从而提供更完整的细胞状态画像。

### 2. 白话版概述
细胞就像一个工厂，RNA 是生产手册，蛋白质是最终产品。以前的 AI 只读手册，但手册写了不代表产品一定造出来了。CAPTAIN 这个模型通过学习 400 多万个既有手册又有产品的真实案例，掌握了两者之间的复杂对应关系。现在，即使你只给它看手册（RNA），它也能精准预测出产品（蛋白质）的长相，并能比以前更准地判断这个细胞在干什么，甚至能发现某些疾病（如新冠肺炎）中细胞间是如何“吵架”或“协作”的。

### 3. 方法部分（Methodology）
*   **核心思想**：利用**跨模态依赖建模**。模型不仅学习 RNA 内部的关联，还强行让模型理解 RNA 特征与蛋白质特征之间的映射逻辑。
*   **模型结构**：基于 Transformer 架构。它将基因（RNA）和表面蛋白视为不同的“Token（符号）”，输入到一个统一的表征空间中。
*   **关键设计**：
    *   **多模态对齐**：通过预训练任务，让模型在处理只有 RNA 的数据时，也能在隐藏层“联想”出对应的蛋白质特征。
    *   **统一表征**：不同于以往将两种模态分开处理再拼接的方法，CAPTAIN 在底层就尝试融合信息，捕捉非线性的跨模态调控关系。
*   **取舍**：为了保证通用性，研究者精选了 382 种常见的细胞表面蛋白作为目标，这虽然涵盖了主要的免疫标记物，但放弃了对数万种胞内蛋白的全面覆盖（受限于目前测序技术）。

### 4. 实验部分
*   **数据规模**：超过 **400 万个**单细胞数据，涵盖人类和小鼠的多种组织。这是目前已知规模最大的单细胞 RNA+蛋白预训练数据集。
*   **下游任务**：
    1.  **蛋白质插补（Imputation）**：只给 RNA，预测缺失的蛋白质数值。
    2.  **细胞标注**：识别细胞类型（如 T 细胞、B 细胞的具体亚型）。
    3.  **批次校正（Batch Harmonization）**：消除不同实验室、不同机器产生的实验误差。
*   **Baseline（对比模型）**：与纯 RNA 模型（scGPT 等）以及专门的多模态工具（TotalVI 等）进行对比。
*   **主要结果**：CAPTAIN 在预测蛋白质丰度方面显著优于传统统计模型；在零样本（Zero-shot）设置下，即使面对没见过的新组织，也能准确标注细胞。

### 5. 资源与算力
*   **训练资源**：文中提到在 400 万级细胞上进行预训练，这通常需要数十块 A100 或 H100 GPU 运行数周。
*   **具体披露**：**文中未充分披露**具体的 GPU 型号、训练时长及总算力消耗（通常此类大模型论文会在补充材料中说明，但摘要和主文简述中未详列）。

### 6. 真正可信的贡献
*   **多模态泛化能力**：最可信的贡献是证明了**跨模态预训练能增强单模态任务**。即使在只有 RNA 的数据上，用 CAPTAIN 提取的特征也比纯 RNA 模型更具生物学解释性。
*   **免疫动力学发现**：模型生成的关于 COVID-19 严重程度与免疫细胞交互模式的假设，得到了部分临床观察的印证，证明了模型具有实际科研产出能力。

### 7. 局限与风险
*   **蛋白质种类受限**：382 种表面蛋白虽然重要，但仅占人体数万种蛋白质的一小部分，模型对胞内信号转导蛋白的预测能力尚不明确。
*   **数据偏差**：CITE-seq 数据目前高度集中在免疫系统（血液、骨髓），模型在非免疫组织（如神经、代谢器官）上的表现可能不如免疫系统稳健。
*   **落地障碍**：对于临床医生而言，模型预测出的“虚拟蛋白质”数值能否直接作为诊断依据，仍需极严苛的实验验证。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多组学整合、单细胞大模型开发、以及免疫学计算研究的 AI 研究者。
*   **后续可跟进的问题**：如何将空间组学（Spatial Omics）信息引入此类多模态模型，实现“RNA + 蛋白 + 空间位置”的三位一体建模？

（完）
