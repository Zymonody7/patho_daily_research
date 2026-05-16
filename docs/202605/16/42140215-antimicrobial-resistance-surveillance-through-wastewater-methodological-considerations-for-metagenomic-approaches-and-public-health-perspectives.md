---
title: "Antimicrobial resistance surveillance through wastewater: methodological considerations for metagenomic approaches and public health perspectives."
title_zh: 通过废水进行抗生素耐药性监测：宏基因组方法的方法学考量与公共卫生视角
authors: "Naomi Hughes, Sanchutha Sathiananthamoorthy, Chrysi Sergaki"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/42140215/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于耐药性监测和公共卫生监测的宏基因组测序
tldr: 抗生素耐药性（AMR）威胁全球，宏基因组测序虽能实现高分辨率废水监测，但工作流差异影响结果可靠性。本文系统梳理了测序流程中的关键环节，探讨了标准化对数据可比性的重要性，并分析了现有检测方法的局限与复杂耐药机制，为构建科学的公共卫生监测体系提供方法论支撑。
selection_source: fresh_fetch
motivation: 针对全球抗生素耐药性危机，解决宏基因组测序在废水监测中因工作流差异导致的数据不可比和结果偏差问题。
method: 综述并对比了宏基因组测序工作流中的关键环节，包括样本采集、测序策略、表型与基因型检测方法的优劣。
result: 明确了标准化流程对获取真实耐药负担的关键作用，并识别出可能导致监测误差的复杂耐药机制和技术瓶颈。
conclusion: 建立标准化的宏基因组监测框架是实现全球公共卫生预警、准确评估环境AMR负担的必要前提。
---

## 摘要
抗生素耐药性（AMR）是公认的全球性威胁，预计将对生命、农业和经济产生重大影响。鉴于宏基因组测序能够以高分辨率进行社区层面的 AMR 分析，该技术正越来越多地被用于 AMR 的监测和检测。这一技术带动了监测工作和数据生成的爆发式增长；然而，不同工作流程之间的差异直接影响了测序结果及其解释。在本述评中，我们总结了在宏基因组研究设计过程中需要考虑的测序工作流程各方面，以实现有意义且可靠的基于人群的监测。我们探讨了标准化在获取 AMR 真实情况以及数据可比性和可重复性方面的关键作用，此外还回顾了各种表型和基因型 AMR 检测方法的局限性。我们进一步强调了复杂的抗生素耐药机制，这些机制可能会阻碍我们准确评估环境中真实 AMR 负担的能力，且在监测过程中往往被忽视。

## Abstract
Antimicrobial resistance (AMR) is a recognised global threat with substantial predicted impact on lives, agriculture, and the economy. Metagenomic sequencing is being increasingly used for AMR surveillance and detection, given its capacity for community-level AMR profiling with high-level resolution. This technology has seen an explosion of surveillance efforts and data generation; however, the variation between workflows has direct implications on the sequencing results and their interpretation. In this Personal View, we summarise aspects of the sequencing workflow that need to be considered during metagenomic study design, for meaningful and reliable population-based surveillance. We reflect on the vital role of standardisation for capturing the ground truth of AMR and data comparability and reproducibility, and in addition, review the limitations of the various phenotypic and genotypic methods of AMR detection. We further highlight complex mechanisms of resistance to antimicrobials that could hinder our ability to confidently assess the true AMR burden in the environment and those that are often overlooked during surveillance.

---

## 论文详细总结（自动生成）

这是一份关于《通过废水进行抗生素耐药性监测：宏基因组方法的方法学考量与公共卫生视角》的深度解析：

### 1. 解决的问题与研究价值
*   **核心问题**：抗生素耐药性（AMR，即细菌演化出不怕抗生素的能力）是全球健康危机。废水监测（WBS）被认为是低成本、覆盖全社区的监测手段，而**宏基因组测序**（直接测定样本中所有 DNA）是目前最强的工具。但问题在于：**全球各实验室的方法五花八门，导致数据无法互通、结果不可比，甚至可能误导公共卫生决策。**
*   **研究价值**：本文为如何建立“标准化”的废水耐药性监测工作流提供了权威指南。对于 AI 研究者来说，这揭示了生物大数据源头的“噪声”来源，是构建可靠预测模型的前提。

### 2. 白话版概述
想象废水是一个城市的“生物档案库”，里面记录了所有人排泄出的细菌信息。我们用宏基因组技术去“读”这些档案，寻找耐药基因。但如果有的实验室只读“书名”（短读长测序），有的读“全文”（长读长测序），或者有的实验室只看“活人”（表型检测），有的连“尸体”也算（DNA 残留），那得出的结论就会南辕北辙。这篇论文系统梳理了从采样到分析的每一个坑，告诉大家怎么做才能拿到“真理”。

### 3. 方法部分：核心思想与关键设计
本文是一篇综述性述评（Personal View），其核心思想是**全流程标准化**。
*   **核心流程**：
    1.  **样本采集与处理**：讨论了采样频率、地理位置以及如何从复杂的废水中浓缩微生物。
    2.  **测序策略取舍**：
        *   **短读长（Short-read）**：通量高、成本低，适合定量分析，但很难确定耐药基因到底在哪种细菌身上（基因组组装困难）。
        *   **长读长（Long-read）**：能读出完整的基因组片段，方便定位耐药基因的“宿主”和其所在的质粒（容易传播的 DNA 环），但准确率和成本曾是瓶颈。
    3.  **生物信息学分析**：强调了参考数据库（如 CARD, ResFinder）的选择对结果的影响。
*   **关键设计取舍**：论文指出，单纯“检测到基因”不等于“细菌有耐药性”。有些基因需要特定的启动子（开关）才能表达，有些则需要点突变。目前的 AI 模型往往只关注基因的存在性，忽略了这些复杂的调控机制。

### 4. 实验与结果总结
由于本文为综述，未进行新实验，但总结了现有研究的共识：
*   **数据现状**：废水中的 AMR 负担与该地区的抗生素消耗量、人口密度高度相关。
*   **主要结论**：
    *   **标准化是刚需**：没有统一的对照品（Reference Materials），不同研究之间的数据无法进行横向对比。
    *   **表型 vs 基因型差异**：基因检测（测 DNA）往往会高估耐药性，因为很多检测到的 DNA 可能来自死掉的细菌，或者该基因在环境中并未激活。
    *   **复杂机制被忽视**：目前的监测往往漏掉了“外排泵”（把药泵出细胞）等非特异性耐药机制。

### 5. 资源与算力
*   **文中未充分披露**：本文重点在于实验方法学和生物学解释，未涉及具体的计算资源消耗或算法训练细节。

### 6. 真正可信的贡献
*   **识别了“地面真值”（Ground Truth）的缺失**：明确指出目前缺乏统一的国际标准物质来校准各实验室的测序结果。
*   **厘清了监测边界**：强调了宏基因组虽然强大，但必须结合传统的细菌培养（表型）才能准确评估公共卫生风险。
*   **预警复杂机制**：提醒研究者注意点突变和异质性耐药（Heteroresistance），这些是目前自动化流程最容易出错的地方。

### 7. 局限与风险
*   **环境干扰**：废水成分复杂（含重金属、化学物质），会抑制测序反应或诱导细菌产生应激性耐药，干扰监测结果。
*   **稀释效应**：在雨季或工业废水排入时，目标耐药基因浓度会被极度稀释，导致假阴性。
*   **外推风险**：废水数据反映的是群体趋势，无法直接对应到具体的临床感染病例，存在“生态学谬误”。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事 **AMR 预测模型、宏基因组组装算法、环境 DNA（eDNA）分析**的 AI 研究员。
*   **后续可跟进的问题**：如何开发一种 AI 算法，能够整合“不完整、非标准化”的全球废水测序数据，并自动校准不同实验室之间的批次效应（Batch Effects）？

（完）
