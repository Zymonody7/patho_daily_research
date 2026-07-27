---
title: Applicability of Nanopore-only whole-genome sequencing for
title_zh: 仅使用 Nanopore 的全基因组测序的适用性
authors: "J Dingemans, S Vandersanden, P Hilkens, J Godelaine, K Magerman, F Crombé, D De Geyter, A Boel, P Bruynseels, J Frans, P Vandecandelaere, A M Van den Abeele, R Cartuyvels"
date: 2026-07-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42506940/"
tags: ["query:pathoai"]
score: 10.0
evidence: 纳米孔测序用于疫情调查和耐药性预测
tldr: "针对ICU中铜绿假单胞菌爆发监测对时效性的严苛要求，本研究评估了基于最新V14化学试剂的Nanopore单平台全基因组测序流程。通过对多个医院分离株的实测，证明该方法在爆发集群识别上与Illumina金标准高度一致（等位基因差异≤1），且耐药性预测准确率达95%，为临床提供了一种快速、低成本且高精度的疫情实时监测与响应方案。"
selection_source: fresh_fetch
motivation: 临床急需一种比传统Illumina测序更快速、且能达到同等准确度的工具，用于ICU内铜绿假单胞菌爆发的实时监测和耐药性分析。
method: 采用Oxford Nanopore最新的V14测序技术对临床分离株进行全基因组测序，并结合BugSeq和MBioSEQ平台进行核心基因组多位点序列分型对比。
result: "实验结果显示Nanopore单平台测序能精准复现Illumina确认的传播集群，且在预测细菌耐药性方面与表型测试结果有95%的一致性。"
conclusion: Nanopore单平台测序在准确性上已达到临床爆发调查的要求，是提升ICU感染控制响应速度的有效技术手段。
---

## 摘要
铜绿假单胞菌（Pseudomonas aeruginosa）暴发在重症监护病房（ICU）中频繁发生。特别是需要机械通气的 ICU 患者易患铜绿假单胞菌呼吸机相关性肺炎，这与高发病率和高死亡率相关。早期阶段快速准确的基因分型对于记录和管理 ICU 中的铜绿假单胞菌暴发至关重要。在本研究中，我们评估了牛津纳米孔（Oxford Nanopore）全基因组测序（WGS）在暴发调查

## Abstract
UNLABELLED: Pseudomonas aeruginosa outbreaks frequently occur in intensive care units (ICUs). In particular, ICU patients requiring mechanical ventilation are vulnerable to P. aeruginosa ventilator-associated pneumonia, which is associated with high morbidity and mortality. Fast and accurate genotyping during the early stage is crucial to document and manage P. aeruginosa outbreaks at the ICU. In this study, we have evaluated the applicability of Oxford Nanopore whole-genome sequencing (WGS) for outbreak investigation and antimicrobial resistance (AMR) prediction. To evaluate whether a Nanopore-only WGS workflow was able to reproduce Illumina-confirmed transmission clusters, 19 P. aeruginosa isolates from ICUs at UZ Brussels (Belgium) that were previously sequenced with Illumina were sequenced using a Nanopore-only workflow based on the latest V14 chemistry, followed by bioinformatic analysis via BugSeq and MBioSEQ Ridom Typer. Although both bioinformatic platforms showed high concordance between Illumina and Nanopore data, MBioSEQ Ridom Typer yielded the lowest allelic distance (maximum one cgMLST allele), confirming all outbreak clusters. When applying the Nanopore-only workflow to longitudinally collected isolates, low genetic heterogeneity (maximum three cgMLST alleles) was observed between isolates from the same patient. WGS and subsequent outbreak analysis of 65 respiratory P. aeruginosa isolates collected from 38 different ICU patients across six Belgian hospitals during a 9-month period showed no intra- or inter-hospital transmission. When the Nanopore-only WGS data were used to predict AMR, there was high categorical agreement (95%) between AMR genotype and phenotype. These findings highlight the potential of Nanopore WGS as a rapid and accurate tool for outbreak investigation of P. aeruginosa. IMPORTANCE: In recent years, Nanopore sequencing has found its way to clinical laboratories because of its affordability, scalability, and, most importantly, its ability to obtain sequencing results in near-real time. However, despite improved raw read accuracies with the latest generation R10.4.1 flow cells, the question remains whether the achieved accuracy is sufficient for accurate bacterial outbreak investigation, particularly in high-risk settings such as intensive care units (ICUs). In this study, we show that Nanopore-only whole-genome sequencing (WGS) is able to match Illumina-only WGS in terms of accuracy for Pseudomonas aeruginosa outbreak investigation in the ICU setting, although important sequence type-dependent and even strain-specific methylation issues need to be resolved in order to guarantee this accuracy. By providing a fast and accurate workflow for reliable P. aeruginosa outbreak investigation, this study could pave the way for large-scale implementation of Nanopore-only WGS, leading to faster outbreak response times.

---

## 论文详细总结（自动生成）

这篇论文评估了最新的纳米孔（Nanopore）测序技术在重症监护病房（ICU）中追踪**铜绿假单胞菌**（一种极易产生耐药性且在医院内传播的危险细菌）爆发的可靠性。

### 1. 解决的问题与价值
*   **核心问题**：在 ICU 环境下，细菌爆发（Outbreak）的监测对速度要求极高。传统的“金标准” Illumina 测序虽然准确，但通常需要凑够一批样本才开机，耗时数天甚至数周。
*   **研究价值**：验证了仅使用 Nanopore 测序（无需 Illumina 数据辅助纠错）是否足以精准识别细菌的传播链和耐药性。这对于实现“实时监控”医院感染具有重要的临床意义。

### 2. 白话版概述
*   ICU 里的病人如果感染了同一种细菌，说明医院内部可能存在交叉感染（爆发）。
*   过去，纳米孔测序虽然快，但“读错率”较高，容易在对比细菌指纹时产生误判。
*   本研究使用了 Nanopore 最新的 V14 测序技术，发现它现在已经足够精准，能像 Illumina 一样准确地分辨出细菌是否属于同一个家族。
*   这意味着医生可以在几小时内锁定传染源，并预测细菌怕哪种药，从而救治病人。

### 3. 方法部分
*   **核心思想**：利用 Nanopore 最新的 **V14 化学试剂（R10.4.1 芯片）** 提升原始读取准确率，结合专门的生物信息学流程进行“核心基因组多位点序列分型”（cgMLST）。
*   **技术流程**：
    1.  **测序**：对临床分离的细菌进行全基因组测序（WGS）。
    2.  **分析平台**：对比了两个平台——**BugSeq**（云端分析）和 **MBioSEQ Ridom Typer**（本地/服务器分析）。
    3.  **关键指标**：**等位基因距离（Allelic Distance）**。简单说，就是对比细菌基因组中数千个核心基因，看有多少个基因长得不一样。如果差异极小（如 ≤5 个），则认为存在传播。
*   **设计取舍**：放弃了高成本、长周期的“二代+三代”混合组装，追求纯 Nanopore 流程的极致速度。

### 4. 实验部分
*   **数据规模**：
    *   19 个已知传播链的对照样本（已有 Illumina 数据）。
    *   65 个来自 6 家比利时医院、38 名 ICU 患者的临床样本。
*   **任务**：
    1.  **一致性验证**：看 Nanopore 能否复现 Illumina 发现的传播集群。
    2.  **耐药性预测**：根据基因组预测细菌对哪些抗生素耐药（AMR 预测）。
*   **主要结果**：
    *   **极高精度**：Nanopore 与 Illumina 的结果差异极小，最大仅 1 个等位基因差异（在微生物学中，这几乎可以视为完全一致）。
    *   **耐药预测**：基因预测结果与实验室药敏试验（表型）的一致性高达 **95%**。
    *   **实战监测**：在为期 9 个月的跨医院监测中，未发现明显的院际传播。

### 5. 资源与算力
*   **文中未充分披露**：论文提到了使用 BugSeq 云平台和 MBioSEQ 软件，但未详细列出具体的 GPU 型号或 Basecalling（碱基识别）所消耗的计算资源。通常此类分析需要 NVIDIA RTX 或 A 系列显卡支持高精度碱基识别。

### 6. 真正可信的贡献
*   **证据最强的结论**：Nanopore V14 测序在 **cgMLST 分型**上的表现已经达到了与 Illumina 互换的水平。
*   **贡献**：证明了在不需要 Illumina 纠错的情况下，单平台 Nanopore 流程足以支撑 ICU 级别的临床决策。

### 7. 局限与风险
*   **甲基化干扰**：论文提到，某些特定的细菌菌株存在**甲基化（DNA 化学修饰）**问题，这会干扰 Nanopore 的电信号，导致特定位点的系统性错误。
*   **软件依赖**：不同的分析软件（如 BugSeq vs MBioSEQ）得出的结果略有差异，说明生物信息流程的标准化仍是挑战。
*   **样本局限**：虽然是多中心研究，但样本主要集中在比利时，全球不同地区的菌株多样性可能带来新的挑战。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事病原体基因组学、实时诊断算法开发、以及临床决策支持系统的 AI 研究者。
*   **后续可跟进的问题**：如何利用深度学习模型更好地识别并校正由 **DNA 甲基化**引起的 Nanopore 信号偏差，从而在不依赖 Illumina 的情况下进一步提升复杂菌株的组装精度？

（完）
