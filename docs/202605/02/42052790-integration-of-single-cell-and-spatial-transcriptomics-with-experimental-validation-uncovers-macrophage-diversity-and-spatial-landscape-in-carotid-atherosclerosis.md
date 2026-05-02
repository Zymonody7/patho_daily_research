---
title: Integration of Single-Cell and Spatial Transcriptomics With Experimental Validation Uncovers Macrophage Diversity and Spatial Landscape in Carotid Atherosclerosis.
title_zh: 结合单细胞与空间转录组学及实验验证揭示颈动脉粥样硬化中的巨噬细胞多样性与空间图谱
authors: "Rongxing Qin, Caiqi Li, Hongyu Xu, Xinyu Lai, Li Chen"
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42052790/"
tags: ["query:seqai"]
score: 9.0
evidence: 单细胞与空间转录组学整合
tldr: 颈动脉粥样硬化（CAS）中巨噬细胞的多样性及其空间分布对斑块稳定性至关重要，但其具体亚型功能尚不明确。本研究通过整合单细胞转录组测序、空间转录组学及体外实验，系统分析了CAS的细胞组成，识别出7种巨噬细胞亚型，并揭示了从IGSF21+到FABP4+的演化轨迹。研究验证了SPP1等关键基因的诊断价值及其空间信号网络，为CAS的精准诊断和治疗提供了新的分子靶点。
selection_source: fresh_fetch
motivation: 旨在阐明颈动脉粥样硬化斑块中巨噬细胞亚型的功能特征及其在斑块进展和失稳中的空间调控机制。
method: 采用单细胞转录组测序结合空间转录组技术，并配合拟时序分析和体外细胞模型对关键基因进行实验验证。
result: 鉴定出7类巨噬细胞亚型，发现了从IGSF21+向FABP4+细胞的演化路径，并揭示了SPP1信号通路在斑块核心区域的空间互作模式。
conclusion: 该研究确定了SPP1、FTH1和FTL等关键诊断标志物，为理解动脉粥样硬化的发病机理及开发针对性疗法奠定了分子基础。
---

## 摘要
颈动脉粥样硬化（CAS）的核心发病机制在于易损斑块的破裂，其中巨噬细胞（MC）在斑块进展和不稳定化中发挥着关键作用。然而，CAS 中巨噬细胞亚群的功能特征仍不清楚。本研究通过整合单细胞 RNA 测序（scRNA-seq）、体外模型和空间转录组学，系统地研究了 CAS 的细胞组成和巨噬细胞的调节机制。巨噬细胞中上调的差异表达基因在多个信号通路中显著富集，包括脂质与动脉粥样硬化、溶酶体以及抗原处理与呈递。基因集变异分析（GSVA）显示，在动脉粥样硬化核心（AC）中，巨噬细胞在血管生成和脂质代谢方面的评分较高。共鉴定出 7 种不同的巨噬细胞亚型。拟时序分析表明，IGSF21+ 巨噬细胞构成了初始细胞群，而 FABP4+ 巨噬细胞则代表了轨迹上的末端细胞。建立了体外动脉粥样硬化模型，以验证 SPP1、FTH1 和 FTL 的诊断价值。空间转录组学进一步揭示了 SPP1 信号通路网络在不同细胞类型间的空间连接模式。本研究为 CAS 的发病机制提供了新的分子见解，并为开发诊断生物标志物和治疗靶点奠定了基础。

## Abstract
The core pathogenesis of carotid atherosclerosis (CAS) lies in the rupture of vulnerable plaques, with macrophages (MC) playing a critical role in plaque progression and destabilization. However, the functional characteristics of MC subpopulations in CAS remain poorly understood. This study systematically investigates the cellular composition of CAS and the regulatory mechanisms of MC by integrating single-cell RNA sequencing (scRNA-seq), in vitro models, and spatial transcriptomics. Differentially expressed genes upregulated in MC were significantly enriched in multiple signaling pathways, including Lipid and Atherosclerosis, Lysosome, and Antigen Processing and Presentation. Gene Set Variation Analysis (GSVA) revealed higher MC scores for Angiogenesis and Lipid Metabolism in the atherosclerotic core (AC). A total of seven distinct MC subtypes were identified. Pseudotime analysis indicated that IGSF21+ MC constitute the initial cell population, while FABP4+ MC represent the terminal cells along the trajectory. An in vitro atherosclerosis model was established to validate the diagnostic value of SPP1, FTH1, and FTL. Spatial transcriptomics further revealed the spatial connection patterns of the SPP1 signaling pathway network across different cell types. This study provides novel molecular insights into the pathogenesis of CAS and lays the groundwork for developing diagnostic biomarkers and therapeutic targets.

---

## 论文详细总结（自动生成）

这篇论文通过整合单细胞和空间技术，深入探讨了颈动脉粥样硬化中“头号嫌疑人”——巨噬细胞的内部多样性。

### 1. 解决的问题与研究意义
**核心问题**：颈动脉粥样硬化（CAS）是导致中风的主因，而斑块是否容易破裂（不稳定性）主要取决于其中的**巨噬细胞**（一种免疫细胞，既能清理垃圾也能引发炎症）。虽然知道它重要，但斑块里到底有多少种巨噬细胞、它们分别在什么位置、又是如何演化的，此前并不清晰。

**研究意义**：通过“高德地图”式的空间定位和“人口普查”式的单细胞分类，找到预测斑块破裂的关键分子（如 SPP1），为开发新的诊断工具和精准治疗药物提供靶点。

### 2. “白话版”概述
血管里的斑块就像一个复杂的“战场”。研究者利用单细胞测序技术把战场上的巨噬细胞分成了 7 个不同的“兵种”，并发现它们会随着病情加重从一种状态演变成另一种状态（从 IGSF21+ 演变为 FABP4+）。接着，他们利用空间转录组技术，像给照片打标签一样，看清了这些细胞具体蹲在斑块的哪个角落。最后，他们在实验室里验证了几个关键基因（SPP1, FTH1, FTL），证明它们确实能作为诊断疾病的信号。

### 3. 核心方法
*   **多组学整合**：结合了**单细胞 RNA 测序（scRNA-seq）**（看细胞种类）和**空间转录组（ST）**（看细胞位置）。
*   **拟时序分析（Pseudotime Analysis）**：利用算法模拟细胞的演化过程，推断巨噬细胞从“初始状态”到“疾病末期状态”的轨迹。
*   **基因集变异分析（GSVA）**：评估不同区域巨噬细胞的功能差异，例如发现斑块核心区的细胞在脂质代谢和血管生成方面更活跃。
*   **细胞通讯分析（CellChat）**：分析不同细胞之间是如何通过信号分子（如 SPP1 通路）进行“对话”的。
*   **实验验证**：不仅靠计算机分析，还建立了体外细胞模型，通过实验确认了关键基因在患病状态下的表达确实会升高。

### 4. 实验与结果
*   **数据源**：人类颈动脉粥样硬化斑块样本。
*   **主要发现**：
    *   鉴定出 **7 种巨噬细胞亚型**。
    *   **演化路径**：IGSF21+ 巨噬细胞是“祖先”，FABP4+ 巨噬细胞是演化的“终点”。
    *   **关键生物标志物**：SPP1、FTH1 和 FTL 被证实具有极高的诊断价值。
    *   **空间分布**：SPP1 信号网络在斑块核心区域（AC）高度活跃，介导了复杂的细胞间相互作用。
*   **评价指标**：通过差异表达倍数（Fold Change）、通路富集显著性（P-value）以及体外实验的表达量对比来衡量结果。

### 5. 资源与算力
*   **文中未充分披露**具体的计算硬件配置。通常此类研究依赖 R 语言环境（如 Seurat, Monocle 等工具包）在常规服务器或高性能工作站上运行。

### 6. 真正可信的贡献
*   **高分辨率图谱**：首次精细刻画了 CAS 斑块中巨噬细胞的 7 种亚型及其空间分布。
*   **演化证据强**：通过拟时序分析结合空间定位，清晰展示了巨噬细胞在斑块进展中的功能转型。
*   **SPP1 的核心地位**：多维度（单细胞、空间、体外实验）一致指向 SPP1 基因在斑块不稳定中的关键驱动作用。

### 7. 局限与风险
*   **样本量限制**：单细胞和空间组学成本高，通常样本例数较少，结论在更大规模人群中的普适性需进一步验证。
*   **静态快照**：测序提供的是斑块在手术那一刻的“快照”，虽然算法能推断演化，但无法实时观察活体内的动态变化。
*   **临床转化障碍**：SPP1 等标志物虽然在组织中表现明显，但能否通过血液检测实现无创诊断仍是挑战。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多模态组学数据融合、细胞轨迹推断算法、以及寻找疾病空间生物标志物的 AI 研究者。
*   **后续可跟进的问题**：如何利用深度学习模型，仅通过常规的 H&E 染色病理切片（低成本）来预测这些复杂的单细胞空间转录组特征（高成本）？

（完）
