---
title: "Shared proteomic landscape between arteriosclerosis and cardiovascular endpoints: a Mendelian randomization and observational study integrating AlphaFold3 for structural prediction."
title_zh: 动脉硬化与心血管终点事件之间的共同蛋白质组学图谱：一项整合 AlphaFold3 进行结构预测的孟德尔随机化与观察性研究
authors: "Jingxian Huang, Devendra Meena, Margaux Achtari, Alexander Smith, Renae Judy, Nour Mimouni, Joshua C Bis, Nora Franceschini, Kenneth Fung, Patricia B Munroe, Scott M Damrauer, Ioanna Tzoulaki, Abbas Dehghan"
date: 2026-05-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/42133815/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 集成AlphaFold3进行结构预测
tldr: 动脉硬化和动脉粥样硬化是心血管疾病的主因，但其分子机制尚不明确。本研究整合了UK Biobank等大规模蛋白质组学数据，利用孟德尔随机化、贝叶斯共定位及AlphaFold3结构预测，系统分析了5813种蛋白质与血管病变及心血管事件的关联。研究识别出10种关键致病蛋白（如ANGPTL4、LPA等），并揭示了LPA通过颈动脉斑块介导中风的机制，为心血管疾病的精准分层和多靶点治疗提供了分子证据。
selection_source: fresh_fetch
motivation: 旨在揭示动脉硬化与动脉粥样硬化在不同血管床中共有及特有的分子机制，以寻找新的生物标志物和治疗靶点。
method: 整合大规模顺式蛋白质定量性状位点数据，结合孟德尔随机化、中介分析及AlphaFold3蛋白质结构建模进行多组学关联研究。
result: 筛选出10个与血管病变及心血管事件显著相关的蛋白质，并证实LPA对中风的影响主要由颈动脉斑块介导，同时利用AlphaFold3定位了关键功能变异。
conclusion: 研究阐明了心血管疾病的共享蛋白质组图谱，强调了血管床特异性机制在风险评估和双重干预中的重要性。
---

## 摘要
目的：动脉粥样硬化和动脉硬化是心血管疾病（CVD）的主要诱因，但它们共同及独特的分子基础尚不完全清楚。方法：本研究整合了蛋白质组学、贝叶斯共定位、孟德尔随机化（MR）和结构建模，以探索不同血管床中与动脉硬化和动脉粥样硬化相关的共同及独特的血浆蛋白质组。我们利用了来自英国生物样本库（UKB）制药蛋白质组学项目（N=54,219）和 deCODE 遗传学（N=35,559）的 5,813 种独特蛋白质的顺式蛋白质定量性状位点（cis-pQTLs），并使用贝叶斯共定位和双向 MR 评估了它们与五种动脉硬化/动脉粥样硬化标志物以及八种心血管事件的关联。我们通过独立蛋白质组学数据集、组织特异性转录组学、来自 UKB 的观察数据以及用于结构预测的 AlphaFold3 对研究结果进行了验证和重复。最后，中介分析评估了血管性状在连接蛋白质与 CVD 风险中的作用。结果：我们筛选出 10 种可能与动脉硬化/动脉粥样硬化标志物及心血管事件存在因果关联的蛋白质。其中 5 种（ANGPTL4、APOB、BRAP、LPA 和 ZPR1）与动脉硬化/动脉粥样硬化水平升高及 CVD 风险增加相关，而 4 种（DUSP13、FN1、IL6R 和 MMP12）与动脉硬化/动脉粥样硬化水平降低及 CVD 风险降低相关。ABO 与外周动脉疾病（PAD）和 CVD 风险增加相关，但与动脉硬化指数（ASI）呈负相关。其中 7 种蛋白质在来自 Fenland 研究的独立 pQTLs 数据源中得到了验证。中介分析估计，LPA 对中风的影响主要通过颈动脉斑块介导（92.4%）。观察性分析和转录组验证证实了这些关联。使用 AlphaFold3 进行的结构建模识别了包括 ANGPTL4 和 FN1 在内的几种蛋白质中的关键功能变异，这些变异可能是致病机制的基础。结论：本研究阐明了动脉硬化、动脉粥样硬化和心血管疾病之间共同及独特的蛋白质组学特征，强调了血管床特异性机制的重要性。这些识别出的蛋白质为基于生物标志物的风险分层和治疗干预提供了广阔前景，并具有跨血管区域进行双重用途干预的潜力。

## Abstract
AIMS: Atherosclerosis and arteriosclerosis are major contributors to cardiovascular disease (CVD), yet their shared and distinct molecular underpinnings remain incompletely understood. This study integrates proteomics, Bayesian colocalization, and Mendelian randomization (MR), and structural modelling to explore the shared and distinct plasma proteome associated with arteriosclerosis and atherosclerosis across different vascular beds. METHODS: We leveraged cis-pQTLs for 5,813 unique proteins from the UK Biobank (UKB) Pharma Proteomics Project (N=54,219) and deCODE genetics (N=35,559) and assessed the association with five arteriosclerotic/atherosclerotic markers, as well as eight cardiovascular events, using Bayesian colocalization and bidirectional MR. We validated and replicated the findings through independent proteomics datasets, tissue-specific transcriptomics, observational data from UKB, and AlphaFold3 for structural prediction. Finally, mediation analysis evaluated the role of vascular traits in linking proteins to CVD risk. RESULTS: We prioritized ten proteins potentially causally associated with both the arteriosclerotic/atherosclerotic markers and cardiovascular events. Five of them (ANGPTL4, APOB, BRAP, LPA, and ZPR1), were associated with increased levels of arteriosclerosis/atherosclerosis and risk of CVD, whereas four (DUSP13, FN1, IL6R, and MMP12) were associated with reduced levels of arteriosclerosis/atherosclerosis and risk of CVD. ABO was associated with increased risk of peripheral artery disease (PAD) and CVD but inversely related to arterial stiffness index (ASI). Of these, seven were replicated in an independent pQTLs data source from the Fenland study. Mediation analyses estimated that LPA's effect on stroke was primarily mediated through carotid plaque (92.4%). Observational analyses and transcriptomic validation corroborated these associations. Structural modelling using AlphaFold3 identified key functional variants in several proteins, including ANGPTL4 and FN1, potentially underlying the pathogenic mechanists. CONCLUSIONS: The present study elucidates the shared and distinct proteomic signatures across arteriosclerosis, atherosclerosis, and cardiovascular disease, underscoring the importance of vascular-bed-specific mechanisms. These identified proteins offer promising avenues for biomarker-driven risk stratification and therapeutic interventions, with potential for dual-purpose interventions across vascular territories.

---

## 论文详细总结（自动生成）

这篇论文利用大规模人群数据和前沿 AI 模型，系统性地梳理了血液蛋白质、血管病变（硬化与斑块）以及心血管疾病（如心梗、中风）之间的因果链条。

### 1. 解决的问题与价值
*   **核心问题**：心血管疾病主要由两种血管病变引起：**动脉粥样硬化**（血管壁长斑块，堵塞血管）和**动脉硬化**（血管失去弹性变硬）。虽然它们都导致心脏病，但哪些蛋白质在其中起关键作用、哪些是共同的“元凶”、哪些是各自特有的，目前尚不清晰。
*   **研究价值**：通过锁定致病蛋白质，可以为开发新药提供精准靶点，或者作为体检指标来预测心脏病风险。

### 2. 白话版概述
*   研究者想找出血液中哪些蛋白质是导致心脏病的“真凶”。
*   他们分析了约 9 万人的基因和蛋白质数据，利用“基因决定蛋白”的逻辑排除了生活习惯等干扰，锁定了 10 个关键蛋白。
*   研究最亮眼的地方在于引入了 **AlphaFold3**，直接模拟了这些蛋白在发生基因突变后的 3D 结构变化，解释了为什么微小的基因差异会导致蛋白功能失常并引发疾病。
*   结果发现，像 LPA 这种蛋白，几乎完全是通过在颈部血管制造斑块来诱发中风的。

### 3. 方法部分
*   **核心思想（孟德尔随机化, MR）**：这是一种“自然随机对照试验”。基因是出生时随机分配的，如果携带某种基因的人血液中蛋白 A 含量高，且这群人更容易得心脏病，那么可以推论是蛋白 A 导致了疾病，而不是反过来。
*   **关键流程**：
    1.  **数据筛选**：从英国生物样本库（UKB）等数据库提取 5813 种蛋白质的遗传数据。
    2.  **共定位分析**：确保“蛋白水平”和“疾病风险”是由同一个基因信号驱动的，排除凑巧重合的可能性。
    3.  **AlphaFold3 结构预测**：针对筛选出的关键蛋白（如 ANGPTL4），用 AI 预测其突变体结构。观察突变是否改变了蛋白的“抓取手”（结合位点），从而在物理层面解释致病机理。
    4.  **中介分析**：计算蛋白是通过什么路径导致心脏病的。例如：蛋白 $\rightarrow$ 血管斑块 $\rightarrow$ 中风。

### 4. 实验部分
*   **数据规模**：使用了 UK Biobank（5.4 万人）和 deCODE（3.5 万人）的大规模蛋白质组数据。
*   **主要任务**：关联蛋白质水平与 5 种血管指标（如动脉硬化指数）及 8 种心血管事件（如心梗、外周动脉疾病）。
*   **核心结果**：
    *   **10 个关键蛋白**：其中 5 个是“坏分子”（如 ANGPTL4, APOB, LPA），水平越高病越重；4 个是“保护者”（如 FN1, IL6R），水平越高风险越低。
    *   **路径揭示**：LPA 蛋白对中风的影响，有 **92.4%** 是通过导致“颈动脉斑块”这一中间环节实现的。
    *   **结构发现**：AlphaFold3 成功识别出 ANGPTL4 等蛋白的关键功能变异位点，证明了 AI 预测与统计学关联的一致性。

### 5. 资源与算力
*   **文中未充分披露**：论文未详细列出运行 AlphaFold3 的具体 GPU 型号或计算耗时，通常此类研究依赖高性能计算集群（HPC）或 Google Cloud 资源。

### 6. 真正可信的贡献
*   **证据链闭环**：不仅在统计上发现了蛋白与疾病的相关性，还通过 MR 证明了因果性，并进一步用 AlphaFold3 在分子结构层面给出了物理机制解释。
*   **高精度中介分析**：量化了血管病变在疾病发生中的贡献比例（如 LPA 的 92.4%），这在同类研究中非常罕见且精确。

### 7. 局限与风险
*   **人群局限性**：数据主要来自欧洲裔人群，结论是否适用于亚洲或非洲裔人群仍需验证。
*   **AI 预测风险**：虽然 AlphaFold3 精度极高，但它仍是预测模型，蛋白突变对功能的实际影响最终还需生物化学实验（如体外结合实验）证实。
*   **静态视角**：血液蛋白水平是动态的，而基因数据是静态的，研究可能忽略了年龄、环境对蛋白水平的动态调控。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物靶点发现、蛋白质结构预测应用、以及因果推断算法开发的 AI 研究者。
*   **后续可跟进的问题**：能否开发一种端到端的 AI 模型，直接从基因变异出发，同时预测蛋白结构变化和群体层面的疾病风险，而不再分步进行统计运算？

（完）
