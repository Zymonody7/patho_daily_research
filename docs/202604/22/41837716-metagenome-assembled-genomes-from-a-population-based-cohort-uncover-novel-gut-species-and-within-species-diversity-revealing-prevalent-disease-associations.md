---
title: "Metagenome-assembled genomes from a population-based cohort uncover novel gut species and within-species diversity, revealing prevalent disease associations."
title_zh: 基于人群队列的宏基因组组装基因组揭示了新的肠道物种和种内多样性，并发现了普遍的疾病关联
authors: "Kateryna Pantiukh, Kertu Liis Krigul, Oliver Aasmets, Elin Org"
date: 2026-04-21
pdf: "https://pubmed.ncbi.nlm.nih.gov/41837716/"
tags: ["query:seqai"]
score: 8.0
evidence: 用于菌株级微生物组分析的宏基因组组装基因组
tldr: 针对宏基因组分析中参考数据库不全及难以区分菌株差异的问题，本研究通过对爱沙尼亚队列的1878份样本进行深度测序，构建了包含353个新物种的基因组集，并提出GUN指标量化种内多样性。研究成功关联了25种疾病，其中8种涉及新物种，并揭示了特定菌株与胃炎等疾病的隐藏关联，证明了基因组解析方法在精准医疗中的价值。
selection_source: fresh_fetch
motivation: 现有的宏基因组研究受限于参考基因组缺失和无法解析种内菌株差异，导致许多微生物与疾病的关联被掩盖。
method: 通过对大规模人群样本进行宏基因组组装（MAGs）构建人群特异性参考库，并引入基因组单元数（GUN）指标来量化种内异质性。
result: 识别出353个新物种，并发现Odoribacter splanchnicus种内的不同基因组单元与胃炎、心脏病等具有截然不同的关联性。
conclusion: 采用人群特异性的基因组组装和种内水平的分析框架，是揭示肠道微生物组与人类健康复杂关系的关键。
---

## 摘要
宏基因组分析推进了对微生物-宿主相互作用的理解。然而，广泛使用的基于 read 的方法受限于参考数据库的不完整以及无法解析菌株水平的变异。在此，我们提出了一个可扩展的、基因组解析的框架，该框架整合了特定人群的宏基因组组装基因组（MAGs），以发现新物种、种内多样性以及疾病关联。通过对爱沙尼亚微生物组队列（EstMB-deep）中 1,878 个深度测序样本的研究，我们重建了代表 2,257 个物种的 84,762 个 MAGs，其中包括 353 个（15.6%）此前未表征的物种，这些物种在某些个体中的相对丰度高达 30%。我们将这些 MAGs 与统一的人类胃肠道基因组集（Unified Human Gastrointestinal Genome collection）整合，创建了一个扩展的参考库（GUTrep），从而实现了对 2,509 名 EstMB 个体的分析，并测试了与 33 种常见疾病的关联。在具有显著关联的 25 种疾病中，有 8 种涉及新发现的物种，这凸显了特定人群 MAGs 的价值。为了量化种内多样性，我们开发了基因组单元数（GUN），这是一种基于 MAG 的新型指标，可为种内分析提供参考。基于归一化的 GUN，我们优先选择了内脏臭气杆菌（Odoribacter splanchnicus），这是一种具有最低种内异质性的常见物种，为种内关联研究提供了足够的效能。我们鉴定了两个主要的基因组单元 GU-N1 和 GU-N2，它们具有不同的基因库和迥异的疾病关联。值得注意的是，GU-N1 与胃炎、十二指肠炎和高血压性心脏病呈负相关，而这些关联在物种水平上未被检测到。我们的研究扩展了人类肠道参考图谱，证明了特定人群 MAGs 对于揭示新型微生物多样性的重要性，并揭示了在较高分类水平上被掩盖的种内水平新疾病关联，强调了微生物组研究中基因组解析方法的必要性。重要性：微生物组研究日益认识到，物种水平的图谱可能会掩盖与健康和疾病相关的关键种内差异。然而，我们的工作表明，肠道微生物的种内多样性差异巨大，某些物种表现出的独特种内簇数量几乎与回收的基因组数量一样多，这使得种内水平的关联研究在本质上难以进行。为解决这一问题，我们引入了基因组单元数（GUN），这是一种用于量化种内结构的可扩展指标。利用 GUN，我们证明目前只有种内多样性有限的物种（如内脏臭气杆菌）才能进行稳健的种内关联测试。这些发现强调了系统评估肠道微生物组物种结构的必要性，并呼吁开发新的计算和统计方法，以便在高度多样化的物种中进行有意义的种内分析。

## Abstract
UNLABELLED: Metagenomic profiling has advanced the understanding of microbe-host interactions. However, widely used read-based approaches are limited by incomplete reference databases and the inability to resolve strain-level variation. Here, we present a scalable, genome-resolved framework that integrates population-specific metagenome-assembled genomes (MAGs) to discover novel species, within-species diversity, and disease associations. From 1,878 deeply sequenced samples in the Estonian Microbiome Cohort (EstMB-deep), we reconstructed 84,762 MAGs representing 2,257 species, including 353 (15.6%) previously uncharacterized species reaching up to 30% relative abundances in some individuals. We integrated these MAGs with the Unified Human Gastrointestinal Genome collection to create an expanded reference (GUTrep), enabling profiling of 2,509 EstMB individuals and testing associations with 33 prevalent diseases. Of the 25 diseases with significant associations, 8 involved newly identified species, underscoring the value of population-specific MAGs. To quantify within-species diversity, we developed the genome unit number (GUN), a novel MAG-based metric that informed within-species analyses. Based on normalized GUN, we prioritized Odoribacter splanchnicus, a prevalent species with the lowest within-species heterogeneity, yielding sufficient power for a within-species association study. We identified two dominant genome units, GU-N1 and GU-N2, with distinct gene repertoires and divergent disease associations. Notably, GU-N1 was negatively associated with gastritis, duodenitis, and hypertensive heart disease, associations undetected at the species level. Our study expands the human gut reference landscape, demonstrates the importance of population-specific MAGs for uncovering novel microbial diversity, and reveals new disease associations at the within-species level obscured at higher taxonomic levels, highlighting the need for genome-resolved approaches in microbiome research. IMPORTANCE: Microbiome studies increasingly recognize that species-level profiles can mask critical within-species differences relevant to health and disease. However, our work shows that within-species diversity varies drastically across gut microbes, with some species exhibiting almost as many distinct within-species clusters as recovered genomes, making association studies at the within-species level essentially intractable. To address this, we introduce the genome unit number (GUN), a scalable metric for quantifying within-species structure. Using GUN, we demonstrate that only species with limited within-species diversity, such as Odoribacter splanchnicus, currently allow for robust within-species association testing. These findings emphasize the need to systematically evaluate species structure across the gut microbiome and call for the development of new computational and statistical approaches to enable meaningful within-species analyses in highly diverse species.

---

## 论文详细总结（自动生成）

这篇论文通过对大规模人群的肠道微生物组进行“深度解码”，揭示了现有数据库中缺失的微生物物种，并证明了同一物种内部的不同“菌株”在疾病关联上可能存在截然相反的作用。

### 1. 核心问题与研究价值
*   **核心问题**：目前的肠道微生物研究大多依赖已有的参考数据库（如 UHGG）。但这存在两个痛点：一是**“盲区”多**，很多特定人群（如爱沙尼亚人）特有的细菌不在库中；二是**“颗粒度”粗**，通常只分析到“种（Species）”这一级，忽略了种内不同菌株（Strain）的功能差异。
*   **研究价值**：论文证明了如果只看“种”，会掩盖很多关键的致病或保护机制。通过构建特定人群的基因组库，研究者能发现更多与疾病相关的“隐藏”微生物。

### 2. 白话版概述
想象肠道是一个复杂的社会，目前的分析方法只能识别出“人类”这个物种，却分不清谁是“警察”谁是“土匪”。这篇论文通过对 1878 个人的肠道样本进行深度测序，不仅找出了 353 种以前从未被记录过的新物种，还开发了一套新指标（GUN）来衡量物种内部的复杂程度。他们发现，某种细菌（内脏臭气杆菌）内部其实分成了两个阵营：一个阵营能预防胃炎和心脏病，而另一个阵营则没这个本事。如果把它们混在一起看，这种保护作用就消失了。

### 3. 方法部分：核心思想与关键设计
*   **核心思想**：采用**宏基因组组装基因组（MAGs）**技术。不同于传统的直接比对已知序列，MAGs 是从原始测序数据中“拼图”，直接还原出完整的微生物基因组，从而发现新物种。
*   **关键流程**：
    1.  **组装与聚类**：从 1878 个深度测序样本中重建了约 8.5 万个 MAGs，并将其聚类为 2257 个物种。
    2.  **构建 GUTrep 库**：将新发现的基因组与全球统一数据库整合，形成一个更全面的参考库。
    3.  **GUN 指标（Genome Unit Number）**：这是本文的原创设计。它通过计算一个物种内部基因组的异质性，量化该物种的“多样性程度”。GUN 值越低，说明该物种内部成员越相似，越适合做种内关联分析。
*   **设计取舍**：研究者意识到并非所有物种都适合做菌株级分析。对于那些 GUN 值极高（内部极其混乱）的物种，目前的统计效能不足以得出结论，因此他们优先选择了 GUN 值较低、结构清晰的物种进行深入研究。

### 4. 实验部分
*   **数据规模**：爱沙尼亚微生物组队列（EstMB），包含 1878 个深度测序样本用于组装，2509 个样本用于疾病关联分析。
*   **任务与指标**：
    *   **新物种发现**：识别出 353 个新物种，部分物种在个体中的丰度高达 30%。
    *   **疾病关联分析**：测试了 33 种常见疾病。
*   **主要结果**：
    *   在 25 种有显著关联的疾病中，有 8 种是与新发现的物种相关的。
    *   **种内差异案例**：针对*Odoribacter splanchnicus*（内脏臭气杆菌），将其分为两个基因组单元（GU-N1 和 GU-N2）。实验发现 **GU-N1 与胃炎、十二指肠炎和高血压性心脏病呈显著负相关（保护作用）**，而 GU-N2 则没有。这种关联在传统的物种水平分析中是完全不可见的。

### 5. 资源与算力
*   **文中未充分披露**具体的计算集群配置或总算力消耗。但考虑到处理了 1878 个深度宏基因组样本并进行了大规模组装（Assembly）和聚类（Clustering），这通常需要数万个 CPU 小时以及 TB 级的内存支持。

### 6. 真正可信的贡献
*   **高置信度结论**：特定人群的 MAGs 组装对于填补微生物组“暗物质”至关重要，15.6% 的新物种占比证明了全球通用数据库的局限性。
*   **方法论贡献**：提出的 **GUN 指标**为微生物组研究提供了一个量化工具，帮助研究者判断何时该做“种”水平分析，何时该深入到“菌株”水平。
*   **生物学发现**：明确了内脏臭气杆菌种内的功能分化，为精准医疗提供了潜在的益生菌或生物标志物候选者。

### 7. 局限与风险
*   **数据偏差**：样本全部来自爱沙尼亚，虽然对该地区具有代表性，但结论（尤其是新物种和疾病关联）在亚洲或非洲人群中可能不成立。
*   **统计效能限制**：对于 GUN 值极高的复杂物种（如某些拟杆菌），目前的样本量仍不足以解析其种内多样性与疾病的关系。
*   **因果性缺失**：研究主要基于相关性分析，尚无法证明这些新物种或菌株是导致疾病的原因，还是疾病导致了肠道环境改变。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事宏基因组算法开发、菌株识别工具设计、以及寻找疾病生物标志物的 AI 研究者。
*   **后续可跟进的问题**：如何利用深度学习（如对比学习或图神经网络）在 GUN 值较高的复杂物种中，更精准地划分具有功能一致性的“基因组单元（GU）”，从而在更小的样本量下实现高灵敏度的疾病关联预测？

（完）
