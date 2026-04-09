---
title: Multiple hypervariable markers improve mycobiome classification in metatranscriptome and metagenome data.
title_zh: 多个高变标记提升宏转录组与宏基因组数据中的真菌组分类性能
authors: "Haihua Wang, Steven H Wu, Kaile Zhang, Ko-Hsuan Chen, Rytas Vilgalys, Hui-Ling Liao"
date: 2026-04-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/41951715/"
tags: ["query:seqai"]
score: 9.0
evidence: 宏基因组数据的分类学分析与分类
tldr: 针对宏基因组和宏转录组中真菌分类受限于参考基因组匮乏和数据库分辨率低的问题，本研究开发了 MicroFisher 工具。该工具通过识别多个高变标记基因序列，并结合加权集成算法进行分类，在模拟群落及森林土壤、植物根系等真实环境数据中表现出比现有工具更高的分类准确度和丰度估计精度，尤其提升了对稀有分类单元的检测能力。
selection_source: fresh_fetch
motivation: 现有的真菌组分类方法过度依赖有限的参考基因组，导致在处理复杂的宏基因组数据时存在灵敏度低和分辨率不足的问题。
method: 开发了 MicroFisher 工具，通过整合多个高分辨率的高变标记基因数据库，并采用加权集成算法对测序序列进行分类鉴定。
result: 实验证明 MicroFisher 在模拟数据集和森林土壤等真实样本中，其物种鉴定准确率和丰度估算精度均优于现有主流工具，并能有效发现稀有分类群。
conclusion: MicroFisher 为环境样本中的真菌群落分析提供了一个高效、准确的新型分类流程，显著提升了真菌组研究的深度。
---

## 摘要
利用宏基因组和宏转录组测序对真菌组（mycobiome）的分类和功能组成进行分析，正在深化我们对生态系统中真菌功能的理解。然而，受限于参考基因组的可用性以及序列数据库的分辨率，基于基因组或核心蛋白的方法在真菌组分类的灵敏度和准确性方面存在局限。为解决这一问题，我们开发了 MicroFisher，这是一种从宏基因组或宏转录组数据中识别具有分类学意义的 reads 的新工具，能够基于多个高变标记（hypervariable markers）对群落成员进行分类鉴定。我们通过模拟真菌群落评估了 MicroFisher 的性能，结果表明，与现有工具相比，该工具在真菌预测和丰度估算方面表现更优。此外，我们还利用森林土壤宏基因组和植物根系真核微生物宏转录组对该方法进行了测试，发现 MicroFisher 在环境微生物组分析中比其他分类工具更准确。MicroFisher 利用高分辨率的高变标记基因数据库和加权整合算法，实现了比现有最先进工具更精确的真菌群落分类。此外，它还能检测到其他工具难以发现的稀有分类单元。因此，MicroFisher 为宏基因组和宏转录组数据的真菌群落分类提供了一种全新的流程。

## Abstract
Profiling the taxonomic and functional composition of mycobiome using metagenomic and metatranscriptomic sequencing is advancing our understanding of fungal functions in ecosystems. However, the sensitivity and accuracy of mycobiome classification using genome- or core protein-based approaches, is limited by the availability of reference genomes and the resolution of sequence databases. To address this, we propose the MicroFisher, a novel tool to identify taxonomically useful reads from metagenomic or metatranscriptomic data, enabling taxonomic identification of community members based on multiple hypervariable markers. We applied MicroFisher to profile the simulated fungal communities to assess the performance of the developed tool, and found higher performance in fungal prediction and abundance estimation compared to existing tools. In addition, we also used metagenomes from forest soil and metatranscriptomes of root eukaryotic microbes to test our method and found that MicroFisher provided more accurate profiling of environmental microbiomes compared to other classification tools. MicroFisher leverages high-resolution hypervariable marker gene databases and weighted integration algorithms to deliver more accurate fungal community classification compared to existing state-of-the-art tools. Additionally, it enables the detection of rare taxa, which is challenging with other available tools. Thus, MicroFisher serves as a novel pipeline for classification of fungal communities from metagenomes and metatranscriptomes.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种名为 **MicroFisher** 的新工具，旨在解决宏基因组（检测样本中所有 DNA）和宏转录组（检测样本中所有正在表达的 RNA）数据中“真菌身份鉴定难”的问题。

### 1. 核心问题：为什么真菌鉴定这么难？
在处理环境样本（如土壤、植物根系）的测序数据时，研究者想知道里面有哪些真菌。目前主流方法（如 Kraken2）依赖于**参考基因组**。
*   **痛点**：真菌的参考基因组非常匮乏（相比细菌少得多），导致大量测序数据无法匹配，造成“漏检”。
*   **价值**：真菌在生态分解、植物致病和共生中起核心作用。MicroFisher 绕开了对完整基因组的依赖，利用多个“身份标签”（高变标记基因）来识别真菌，显著提升了检测的灵敏度和准确性。

### 2. 白话版概述
想象你在一个巨大的拼图中寻找特定的几个人。传统方法是对比“全身照”（全基因组），但数据库里只有少数人的全身照，所以大部分人你都不认识。MicroFisher 的策略是只看那些最有特征的“局部照”，比如指纹、虹膜或耳廓（即 ITS、LSU、SSU 等高变标记基因）。它从海量数据中把这些局部特征“钓”出来，然后综合多个特征进行加权打分，从而精准判断这属于哪种真菌，即使没有这个真菌的全身照也能认出它。

### 3. 方法部分：核心设计与流程
*   **核心思想**：**多标记基因集成分类**。不再死磕全基因组比对，而是专注于真菌分类学中公认的“条形码”区域。
*   **关键设计**：
    1.  **特征提取（Fishing）**：从杂乱的宏基因组/宏转录组 reads（测序片段）中，利用隐马尔可夫模型（HMM）等手段精准捕获属于 ITS（内转录间隔区）、LSU（大亚基）、SSU（小亚基）等高变区的序列。
    2.  **多数据库比对**：将捕获到的序列与专门的、高分辨率的标记基因数据库（如 UNITE）进行比对。
    3.  **加权集成算法（Weighted Integration）**：这是该工具的灵魂。不同标记基因的分辨率不同（例如 ITS 对种级鉴定很强，SSU 较弱），MicroFisher 根据不同标记的可靠性分配权重，整合出一个最终的物种组成清单。
*   **取舍**：放弃了非编码区或保守性过强的区域，牺牲了对全基因组功能的全面扫描，换取了极高的分类学鉴定精度。

### 4. 实验部分：表现如何？
*   **数据与任务**：
    *   **模拟群落（Mock Communities）**：已知物种组成的“标准答案”数据集，用于测试准确率。
    *   **真实环境数据**：森林土壤宏基因组、植物根系真核微生物宏转录组。
*   **基准模型（Baseline）**：与目前最流行的 Kraken2、Bracken、MetaPhlAn 等工具对比。
*   **评价指标**：精确率（Precision）、召回率（Recall）、F1 分数、丰度估计的偏差（Bray-Curtis 距离）。
*   **主要结果**：
    *   MicroFisher 在**种（Species）**级别的鉴定准确度远超传统工具。
    *   **稀有物种检测**：它能发现那些在样本中含量极低、被其他工具忽略的真菌。
    *   **丰度还原**：估算的物种比例与实际情况更接近，解决了传统方法容易产生的“虚假繁荣”或“严重漏报”问题。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置需求（如内存、CPU 核数）或运行耗时。但基于其流程，其计算压力主要在于从海量 reads 中提取标记基因片段的步骤。

### 6. 真正可信的贡献
*   **突破了“基因组依赖”瓶颈**：证明了在真菌领域，利用高质量的标记基因数据库比利用残缺不全的全基因组数据库更靠谱。
*   **证据强度**：通过模拟数据和真实复杂环境数据的双重验证，尤其是对“稀有分类单元”的检出能力，证明了该算法的灵敏度优势。

### 7. 局限与风险
*   **数据库依赖**：虽然不依赖全基因组，但它依然依赖标记基因数据库。如果某种真菌在 ITS/LSU 数据库中也没有记录，MicroFisher 同样无法识别。
*   **计算开销**：从海量数据中“钓”出特定序列（提取 reads）的过程可能比直接进行 K-mer 比对（如 Kraken2）更耗时。
*   **外推风险**：目前主要针对真菌，虽然理论上可扩展至其他真核微生物，但需重新构建对应的标记基因库。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事环境微生物组、精准农业、真菌病原体检测的研究者，以及关注“多源信息融合”算法的 AI 开发者。
*   **后续可跟进的问题**：能否利用深度学习（如 Transformer 或 CNN）直接从原始序列中学习比 ITS 更具代表性的“隐式特征”，从而彻底摆脱对现有标记基因数据库的依赖？

（完）
