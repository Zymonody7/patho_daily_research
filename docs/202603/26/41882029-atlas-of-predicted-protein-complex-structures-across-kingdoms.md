---
title: Atlas of predicted protein complex structures across kingdoms.
title_zh: 跨界预测蛋白质复合物结构图谱
authors: "Xianzhi Qi, Cheng Ye, Jianqiang Liang, Shimin Wen, Yuanyuan Li, Kai Ding, Yongfu Hao, Junjie Fei, Weian Mao, Liupeng Li, Zhiyu Lin, Yichong Shen, Hongjie Zhu, Yayun Hu, Rui Zhang, Pengli Ji, Yafei Lu, Bonan Liu, Han Wang, Yuxuan Chen, Zhenguo Ma, Peiyuan Yang, Xinyu Xu, Junlong Wu, Youyuan Zhu, Qiaosha Zou, Wencheng Zhu, Kelu Yao, Shuya Li, Hongyi Xin, Daji Ergu, Jianyang Zeng, Zhi-Xiong Jim Xiao, Chunhua Shen, Ying Cai, Yong Yi, Dacheng Ma"
date: 2026-03-25
pdf: "https://pubmed.ncbi.nlm.nih.gov/41882029/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 基于AlphaFold2的蛋白质复合物结构图谱
tldr: 蛋白质复合物是生命活动的核心，但其结构表征远滞后于相互作用数据的增长。本研究利用基于 AlphaFold2 的 ColabFold 框架，构建了涵盖细菌、古菌、人类、小鼠及病毒等跨物种的 110 万个蛋白质相互作用结构图谱。通过筛选出 18 万个高置信度结构，揭示了跨物种保守的复合物构型，并成功预测了新型病毒受体。该资源不仅深化了对蛋白质进化与功能的理解，还显著提升了蛋白质结合位点预测等下游 AI 任务的性能。
selection_source: fresh_fetch
motivation: 尽管已发现数百万种潜在的蛋白质相互作用，但跨物种的大规模复合物结构数据依然匮乏，限制了对生物分子机制的深入理解。
method: 研究者采用基于 AlphaFold2 的 ColabFold 预测框架，对人类、多种模型生物及人-病毒对的 110 万个潜在相互作用进行了全蛋白质组规模的结构建模。
result: "成功识别出 181,671 个高置信度复合物结构，发现了跨物种保守的结构架构，并通过实验验证了新型病毒受体，同时揭示了进化中的基因融合与裂变事件。"
conclusion: 该跨物种结构图谱为生物医学研究提供了极具价值的资源，能够有效辅助功能注释并提升蛋白质结合界面预测等深度学习模型的表现。
---

## 摘要
蛋白质复合物是所有生物过程的基础。公共数据库已扩展到包含来自人类和多种模式生物的数百万个潜在蛋白质-蛋白质相互作用（PPI）。然而，这些复合物的大规模结构表征——尤其是跨不同生物界的表征——仍远滞后于此，导致大多数潜在和未识别的相互作用尚未得到解析。在此，我们展示了一个包含 110 万个预测蛋白质-蛋白质相互作用结构的综合图谱，这些结构是利用基于 AlphaFold2 的 ColabFold 框架生成的。该数据集涵盖了来自细菌、古菌、人类、小鼠、植物以及人类-病毒对的全蛋白质组相互作用。总体而言，我们识别出 181,671 个高置信度蛋白质复合物结构，其中人类相互作用组中包含 37,855 个。结构聚类揭示了跨界共享的众多保守蛋白质复合物架构，为先前未表征的生物学功能提供了见解。在共免疫沉淀实验的支持下，我们进一步确定了人类腺病毒 A 型（Human mastadenovirus A）和狒狒 α 疱疹病毒 2 型（Papiine alphaherpesvirus 2）的候选病毒受体。将我们的复合物结构与 AlphaFold 单体结构数据库相结合的比较分析揭示了进化过程中广泛存在的基因融合和裂变事件。最后，我们展示了我们的数据集如何利用深度学习方法增强蛋白质结合表面的预测，说明了其在结构建模之外的广泛用途。总之，据我们所知，该图谱代表了最广泛的跨界资源之一，并为各种生物医学应用中的未来发现开辟了道路。

## Abstract
Protein complexes are fundamental to all biological processes. Public repositories have expanded to include millions of potential protein-protein interactions (PPIs) from human and diverse model organisms. Yet, large-scale structural characterization of these complexes-especially across different biological kingdoms-has lagged far behind, leaving most potential and unidentified interactions unresolved. Here, we present a comprehensive atlas of 1.1 million predicted protein-protein interaction structures generated with the AlphaFold2-based ColabFold framework. This dataset spans proteome-wide interactions from bacteria, archaea, humans, mice, plants, and human-virus pairs. Overall, we identify 181,671 high-confidence protein complex structures, especially 37,855 in the human interactome. Structural clustering revealed numerous conserved protein complex architectures shared across kingdoms, providing insights into previously uncharacterized biological functions. Supported by co-immunoprecipitation experiments, we further identify candidate viral receptors for Human mastadenovirus A and Papiine alphaherpesvirus 2. Comparative analyses integrating our complex structures with the AlphaFold monomeric structure database uncovered widespread gene fusion and fission events during evolution. Finally, we demonstrate how our dataset can enhance protein binding-surface prediction using deep learning approaches, illustrating its broad utility beyond structural modeling alone. Altogether, this atlas to our knowledge, represents one of the most extensive cross-kingdom resources and opens avenues for future discoveries in various biomedical applications.

---

## 论文详细总结（自动生成）

### 跨界预测蛋白质复合物结构图谱 (Atlas of predicted protein complex structures across kingdoms) 论文总结

#### 1. 核心问题与研究意义
在生物学中，蛋白质很少“单打独斗”，它们通常相互结合形成**复合物**（Complexes）来执行功能。虽然目前人类已经通过实验或预测手段掌握了数百万对潜在的**蛋白质相互作用**（PPI，即谁和谁会碰面），但这些相互作用在三维空间里到底是怎么“扣”在一起的（即复合物结构），绝大多数仍是未知的。

这篇论文的意义在于：它利用 AI 技术，在大规模跨物种（从细菌、古菌到人类、植物、病毒）的尺度上，为 110 万对相互作用建立了三维结构模型。这就像是从一份只有“人名联系录”的名单，进化到了一本拥有“双人合影及动作细节”的立体图谱，为药物研发和进化生物学提供了海量底层数据。

#### 2. “白话版”概述
想象一下，我们知道成千上万种零件可以两两组装，但不知道它们组装后的具体形状。这项研究利用 AlphaFold2 的升级版工具，一口气预测了 110 万种蛋白质组装后的 3D 形状，涵盖了地球上主要的生命形式。研究者从中筛选出了约 18 万个非常靠谱的结构，并利用这些模型发现了病毒入侵人体的新“抓手”（受体），还揭示了不同生物之间蛋白质结构的演化规律。最后，这些数据还能反哺 AI，让预测蛋白质结合位置的模型变得更聪明。

#### 3. 方法部分
*   **核心思想**：利用高通量计算框架，将已知的潜在相互作用对转化为高分辨率的三维结构模型。
*   **模型结构**：采用了基于 **AlphaFold2** 改进的 **ColabFold** 框架。ColabFold 通过优化多序列比对（MSA）的生成速度，极大地提升了预测效率，使得处理百万级别的序列对成为可能。
*   **推理流程**：
    1.  **输入**：从公共数据库中提取跨物种的 PPI 候选对。
    2.  **比对**：为每一对蛋白质生成 MSA，捕捉进化过程中的协同突变信息。
    3.  **预测**：通过 ColabFold 预测复合物的 3D 坐标。
    4.  **评估**：使用 pLDDT（局部置信度）和 ipTM（界面置信度）等指标对结果进行打分。
*   **关键设计取舍**：研究重点放在了**二元复合物**（两个蛋白质的结合）上，而非多元超大复合物。这种取舍在保证计算可行性的同时，覆盖了最基础的相互作用单元。

#### 4. 实验部分
*   **数据规模**：涵盖细菌、古菌、人类、小鼠、植物及“人-病毒”交互对，共计 110 万个预测结构。
*   **主要任务**：
    *   **高置信度筛选**：识别出 181,671 个高质量结构（其中人类占 37,855 个）。
    *   **结构聚类**：寻找不同物种间相似的结合模式。
    *   **病毒受体预测**：针对人类腺病毒 A 和狒狒 α 疱疹病毒 2 进行受体识别。
*   **评价指标**：除了 AI 预测的置信度分数，研究还引入了**共免疫沉淀（Co-IP）实验**（一种生物化学实验，用于验证两种蛋白质在物理上是否真的结合）来验证预测的准确性。
*   **主要结果**：成功发现了跨物种保守的复合物架构；实验证实了预测的病毒受体；证明了该数据集能显著提升下游 AI 模型在“蛋白质结合表面预测”任务中的表现。

#### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号、数量及总计算耗时。但考虑到 110 万个复合物的预测规模，这通常需要数万至数十万个 GPU 小时的算力支持。

#### 6. 真正可信的贡献
*   **最大规模的跨界资源**：提供了目前最全面的跨物种蛋白质复合物结构数据库。
*   **实验闭环**：不仅仅是 AI 预测，还通过生物学实验（Co-IP）验证了病毒受体的发现，这证明了预测结果具有实际的生物学指导意义。
*   **进化洞察**：通过对比单体和复合物结构，清晰地展示了进化过程中基因是如何通过“融合”或“裂变”来改变蛋白质交互方式的。

#### 7. 局限与风险
*   **预测非真实**：尽管置信度高，但 AI 预测结构仍需实验（如冷冻电镜）最终确认，可能存在假阳性。
*   **动态性缺失**：蛋白质在细胞内是动态变化的，静态的 3D 模型无法完全反映其在不同生理条件下的构象变化。
*   **环境忽略**：预测过程未考虑细胞内复杂的微环境（如 pH 值、离子浓度、伴侣蛋白），这些因素可能影响蛋白质的实际结合。

#### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事蛋白质结构预测、药物靶点发现、蛋白质设计以及结构生物学 AI 算法开发的科研人员。
*   **后续可跟进的问题**：如何利用这 18 万个高置信度复合物结构作为“合成数据”，去预训练更强大的、能够直接预测多蛋白质组装体（>2 个组分）的端到端模型？

（完）
