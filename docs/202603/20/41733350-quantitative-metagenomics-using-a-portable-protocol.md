---
title: Quantitative metagenomics using a portable protocol.
title_zh: 使用便携式方案的定量宏基因组学
authors: "Kaiqin Bian, Andrea Busch, John Norton, Charles Bott, Raul Gonzalez, Kyle Curtis, Dienye Tolofari, Wendell Khunjar, Katherine E Graham, Ameet J Pinto"
date: 2026-03-18
pdf: "https://pubmed.ncbi.nlm.nih.gov/41733350/"
tags: ["query:seqai"]
score: 9.0
evidence: 用于定量宏基因组学和监测的纳米孔测序
tldr: 针对环境微生物定量分析依赖复杂设备、耗时长的难题，本研究开发了名为 rD+rQ 的便携式工作流。该方案利用纳米孔测序技术，结合多物种基因组内标校准法（BSINC），实现了对环境样本中微生物群落的实时绝对定量。实验证明其精度可媲美数字 PCR，为水质监控和污水流行病学调查提供了快速、现场化的决策支持。
selection_source: fresh_fetch
motivation: 现有的微生物定量技术通常需要大型实验室设备且分析周期长，无法满足水处理现场实时监控和快速响应的需求。
method: 开发了一种集成高分子量 DNA 提取与多物种基因组内标校准（BSINC）的纳米孔测序流程，通过实时数据处理实现绝对定量。
result: 该工作流在环境样本中实现了种水平的精准识别，其定量结果的准确性与金标准数字 PCR 技术相当。
conclusion: 这种便携且易用的定量宏基因组分析方案，显著提升了环境微生物监测的效率，适用于生物工艺控制和污水流行病学等领域。
---

## 摘要
一种用于定量微生物群落分析的现场可部署 DNA 测序方法，可以为水务领域的各种应用（从过程控制到废水监测）提供快速响应。目前的定量方法需要复杂的仪器，且 DNA 回收和绝对定量的周转时间较长。在本研究中，我们报告了一种现场可部署的快速检测和快速绝对定量 (rD+rQ) 工作流程，该流程利用实时纳米孔 (Nanopore) 测序进行定量宏基因组学研究。该工作流程整合了针对水务领域相关多种环境基质的高分子量 DNA 回收方案，以及带有条形码内标校准 (BSINC) 的多路纳米孔测序。与使用单一 DNA 片段或单一生物体内标控制的传统方法相比，使用多物种基因组内标控制的 BSINC 表现出显著更高的校准准确度。基于测序基因组的覆盖比例和重复样本间基因组拷贝数的变异系数，建立了动态检测和定量限，以提高微生物定量的准确度和精确度。rD+rQ 工作流程在环境样本中实现了物种级鉴定和与数字 PCR (digital PCR) 相当的绝对定量结果。这种便携式实验室且易于使用的 rD+rQ 工作流程应有助于水行业的快速决策。重要性：微生物群落的快速实时监测对于环境微生物学和生物技术的广泛应用至关重要。虽然便携式测序技术及相关工作流程的最新进展使现场分析成为可能，但这些方法无法提供微生物浓度的定量数据。在本研究中，我们提出了一种能够进行非靶向和定量微生物群落分析的样本和数据处理工作流程，并证明了其在复杂环境样本中的有效性。这种获取定量数据的方法可以推动从生物过程控制到基于废水的流行病学的快速决策。

## Abstract
A field-deployable DNA sequencing approach for quantitative microbial community profiling can enable rapid responses for a range of applications in the water sector-from process control to wastewater surveillance. Current quantitative approaches require complex instrumentation and have long turnaround times for DNA recovery and absolute quantitation. In this study, we report a field-deployable rapid detection and rapid absolute quantitation (rD+rQ) workflow that leverages real-time Nanopore sequencing for quantitative metagenomics. This workflow integrates a high-molecular-weight DNA recovery protocol for diverse environmental matrices of relevance to the water sector, and multiplexed Nanopore sequencing with barcoded spike-in-based calibration (BSINC). BSINC using multispecies genomic spike-in controls exhibits significantly higher calibration accuracy compared to conventional approaches that utilize either a single DNA fragment or single organism spike-in controls. Dynamic detection and quantitation limits were established based on the coverage fraction of sequenced genomes and the coefficient of variation of genome copy numbers across replicates to enhance the accuracy and precision of microbial quantitation. The rD+rQ workflow achieves species-level identification and absolute quantitative results comparable to digital PCR in environmental samples. This portable laboratory and easy-to-use rD+rQ workflow should facilitate rapid decision-making for the water industry.IMPORTANCERapid and real-time monitoring of microbial communities is critical for a vast array of applications in environmental microbiology and biotechnology. While recent developments in portable sequencing technologies and associated workflows make onsite analysis possible, these approaches do not provide quantitative data on microbial concentrations. In this study, we present a sample and data processing workflow that enables nontargeted and quantitative microbial community profiling and demonstrate its validity on complex environmental samples. This approach for acquiring quantitative data can drive rapid decision-making from bioprocess control to wastewater-based epidemiology.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种名为 **rD+rQ**（快速检测+快速绝对定量）的新型工作流，旨在解决环境微生物监测中“既要快、又要准、还要能现场操作”的难题。

### 1. 核心问题：从“比例”到“绝对数量”的跨越
在水质监测（如污水处理、病毒监控）中，研究者不仅想知道某种细菌占总量的百分之几（相对丰度），更需要知道每毫升水里到底有多少个细菌（绝对浓度）。
*   **现状：** 传统的定量方法（如数字 PCR）虽然准，但需要昂贵的实验室设备，且只能针对特定几种微生物；宏基因组测序（Metagenomics）能看全貌，但通常只能给比例，且分析周期长。
*   **痛点：** 现有的便携式测序仪（如 Nanopore）虽然能现场用，但由于测序过程存在偏差，很难直接给出准确的绝对定量数据。

### 2. 白话版概述
想象你在一个装满各种球的大池子里，想知道红球的具体个数。你先往池子里扔进 100 个自带标记的蓝球、绿球和黄球（这就是“内标”）。然后你随机抓出一把球，发现抓到了 10 个标记球和 5 个红球。通过这个比例，你就能推算出池子里红球的总数。
这篇论文就是把这个逻辑用在了 DNA 测序上：通过在样本中加入一组已知浓度的多种微生物 DNA（内标），利用便携式纳米孔测序仪实时读取数据，并根据内标的表现来校准并计算出样本中所有微生物的精确数量。

### 3. 方法部分：核心设计与取舍
*   **核心思想（BSINC）：** 采用“带条形码的内标校准法”（Barcoded Spike-In-based Calibration）。不同于以往只加一种 DNA 片段作为参考，该方法加入了**多种微生物的完整基因组**作为内标。
*   **关键设计：**
    *   **多物种内标：** 覆盖了不同基因组大小、GC 含量（DNA 的一种化学特征）的物种，这样可以更全面地模拟和抵消测序过程中的化学偏差。
    *   **动态过滤（LOD/LOQ）：** 设定了“检测限”和“定量限”。系统会根据基因组的覆盖程度（Coverage Fraction）和重复样本间的变异系数（CV）自动判断哪些数据是可信的，剔除掉那些因为太稀少而测不准的噪声。
*   **流程：** 现场提取高分子量 DNA -> 加入内标 -> 纳米孔测序 -> 实时分类与校准计算 -> 输出绝对定量结果。
*   **取舍：** 放弃了追求极高精度的实验室大型测序平台，选择了便携但错误率稍高的 Nanopore，通过算法和内标设计来弥补硬件的精度损失。

### 4. 实验部分
*   **数据与任务：** 实验使用了人工合成的微生物群落（Mock Community）以及真实的污水处理厂样本（活性污泥、二级出水）。
*   **Baseline（对比基准）：** 
    1.  **数字 PCR (dPCR)：** 目前生物定量领域的“金标准”。
    2.  **单一内标法：** 传统的只加一种参考物质的方法。
*   **评价指标：** 线性回归的 $R^2$ 值（相关性）、基因组拷贝数（绝对浓度）、检测限（LOD）。
*   **主要结果：** 
    *   rD+rQ 算出的微生物数量与金标准 dPCR 的结果高度一致（$R^2 > 0.9$）。
    *   使用多物种内标的准确度显著高于单一内标。
    *   在物种级别（Species-level）实现了精准的身份识别和定量。

### 5. 资源与算力
*   **硬件：** 使用了 Oxford Nanopore 的 MinION（便携式）或 GridION 测序仪。
*   **算力：** 论文侧重于实验流程和校准算法，未提及大规模深度学习训练，主要涉及实时的碱基识别（Basecalling）和序列比对。
*   **文中未充分披露：** 具体实时分析所需的笔记本电脑配置或云端算力消耗细节。

### 6. 真正可信的贡献
*   **BSINC 校准模型：** 证明了在宏基因组测序中，使用“复杂内标”比“简单内标”更能有效消除系统误差。
*   **现场化闭环：** 成功打通了从采样到获得绝对定量结果的现场全流程，将原本需要数天的周期缩短至几小时。
*   **证据强度：** 通过与 dPCR 的直接对比，证明了该便携方案在复杂环境样本（如成分复杂的污泥）中依然稳健。

### 7. 局限与风险
*   **成本问题：** 纳米孔测序的耗材（流路胞）价格较高，大规模日常监测的经济性有待评估。
*   **灵敏度瓶颈：** 对于极低浓度的病原体（如污水中极少量的病毒），该方法的检测限可能不如针对性的 qPCR。
*   **内标依赖：** 定量的准确性高度依赖于所添加内标物质的质量和浓度准确性。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事**实时生物传感器数据处理**、**噪声信号校准**以及**环境基因组学**的 AI 研究者。
*   **后续可跟进的问题：** 能否开发一种机器学习模型，在不添加物理内标的情况下，仅根据序列特征（如 GC 含量、k-mer 分布）自动预测并修正测序偏差，实现“无内标”的绝对定量？

（完）
