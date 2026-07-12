---
title: Real-time estimation of pathogen transmission dynamics from wastewater.
title_zh: 基于废水的病原体传播动力学实时评估
authors: "Lison A, McLeod RE, Huisman JS, Munday JD, Ort C, Julian TR, Stadler T., Adrian Lison, Rachel E McLeod, Jana S Huisman, James D Munday, Christoph Ort, Timothy R Julian, Tanja Stadler"
date: 2026-07-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42436148/"
tags: ["query:pathoai"]
score: 8.0
evidence: 基于贝叶斯模型的废水病原体传播动力学推断
tldr: 针对废水监测中非新冠病毒浓度低、噪声大且临床数据匮乏的难题，研究者开发了贝叶斯半机械模型 EpiSewer。该模型直接从原始浓度和流量数据中推断有效传染数，无需数据预处理。在瑞士多病原体监测中，它成功实现了对流感和 RSV 等低丰度病毒的稳健追踪与预测，为缺乏临床监测的传染病提供了实时预警工具。
selection_source: fresh_fetch
motivation: 现有的废水监测方法在处理流感等低浓度、高噪声病原体数据时，难以准确推断传染参数且过度依赖临床验证。
method: 提出了名为 EpiSewer 的贝叶斯半机械模型，通过整合感染动力学、排毒动力学和测量噪声模型，直接从原始废水数据中推断传染动态。
result: 在瑞士三年的实测中，该模型对流感和 RSV 的传染数估计与新冠病毒同样稳健，并能提供准确的 14 天浓度预测。
conclusion: 该方法证明了仅需每周少量废水样本即可实现对多种传染病的实时。
---

## 摘要
废水监测在 COVID-19 大流行期间被证明能有效追踪 SARS-CoV-2 的传播。然而，由于污水中浓度较低、排毒动力学不确定以及临床验证数据有限，估算其他病原体的传播参数仍然具有挑战性。在此，我们提出了 EpiSewer，这是一种贝叶斯半机械论废水模型，它综合考虑了感染动力学、病原体排毒和测量噪声（包括离群值和未检出值）。该模型能够直接从原始浓度和流量数据中推断有效再生数 (Rt) 和流行病增长率 (rt)，从而无需进行预先的平滑处理、插值或离群值剔除。我们在瑞士的 6-14 个污水处理厂，通过三个季度的多病原体废水监测（2022 年 11 月至 2025 年 5 月）对 EpiSewer 进行了评估，实时追踪了 SARS-CoV-2、甲型流感病毒 (IAV) 和呼吸道合胞病毒 (RSV) 的传播。即使 IAV 和 RSV 的浓度比 SARS-CoV-2 低 10-50 倍，Rt 估算值依然保持一致，且对测量噪声具有鲁棒性。该模型提供了校准良好的 14 天浓度预测，在不同流行阶段的偏差极小。在采样频率降低的情况下，EpiSewer 仍能保持无偏预测，同时准确反映不确定性。我们的方法仅需每周采集少量废水样本，即可对临床监测有限的低丰度病原体进行稳健的传播动力学推断。

## Abstract
Wastewater monitoring proved effective for tracking SARS-CoV-2 transmission during the COVID-19 pandemic. However, estimating transmission parameters for other pathogens remains difficult due to lower concentrations in sewage, uncertain shedding kinetics, and limited clinical validation data. Here we present EpiSewer, a Bayesian semi-mechanistic wastewater model that jointly accounts for infection dynamics, pathogen shedding, and measurement noise, including outliers and non-detects. This enables direct inference of the effective reproduction number (Rt) and epidemic growth rate (rt) from raw concentration and flow data, eliminating the need for prior smoothing, imputation, or outlier removal. We assessed EpiSewer across three seasons of multi-pathogen wastewater surveillance (Nov 2022 - May 2025) at 6-14 treatment plants in Switzerland, tracking SARS-CoV-2, influenza A virus (IAV), and respiratory syncytial virus (RSV) transmission in real time. Rt estimates were consistent and robust to measurement noise, even with IAV and RSV concentrations 10-50 times lower than SARS-CoV-2. The model provided well-calibrated fourteen-day concentration forecasts, with minimal bias across epidemic phases. Under reduced sampling frequencies, EpiSewer maintained unbiased forecasts while accurately reflecting uncertainty. Our approach enables robust inference of transmission dynamics for lower-abundance pathogens with limited clinical surveillance, using only a few wastewater samples per week.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **EpiSewer** 的数学模型框架，旨在通过分析城市下水道中的病毒浓度，实时推断传染病的传播速度和趋势。

### 1. 解决的问题与研究意义
在新冠大流行期间，废水监测（WBE）被证明是追踪疫情的利器。但当研究者想把这套方法推广到流感（IAV）或呼吸道合胞病毒（RSV）时，遇到了三大难题：
*   **信号弱：** 这些病毒在废水中的浓度通常比新冠病毒低 10 到 50 倍，极难检测。
*   **噪声大：** 废水数据充满了离群值（采样偶然性）和未检出值（浓度太低测不到）。
*   **缺乏标准：** 科学界对人体感染这些病毒后，每天排泄出多少病毒（排毒动力学）缺乏精确数据。

**研究意义：** 该论文提供了一套稳健的统计工具，让公共卫生部门即使在临床检测（如医院核酸报告）不完善的情况下，也能仅靠每周几次的废水采样，准确预判流感等多种传染病的爆发。

### 2. 白话版概述
想象城市下水道是一个巨大的“集体采样管”，每个人的排泄物都在里面。EpiSewer 模型就像一个智能过滤器：它读取废水中杂乱的病毒浓度数据，自动踢掉那些不靠谱的脏数据，并结合病毒在人体内的代谢规律，反推回城市里现在有多少人感染、病毒传播得有多快（即 $R_t$ 值）。即使废水中病毒少到几乎测不出来，它也能通过概率计算给出一个可靠的预测。

### 3. 方法部分：核心思想与模型结构
EpiSewer 采用的是**贝叶斯半机械论模型（Bayesian semi-mechanistic model）**。
*   **核心思想：** 它不只是简单的曲线拟合，而是模拟了“感染 -> 排毒 -> 运输 -> 观测”的整个物理过程。
*   **模型结构：**
    1.  **感染动力学层：** 描述病毒如何在人群中传播，核心参数是有效传染数 $R_t$（一个人平均传染几个人）。
    2.  **排毒动力学层（Shedding）：** 这是一个关键的“卷积”过程。模型考虑了人感染后并不是立刻排毒，而是在一段时间内（如 10-14 天）持续排毒，且每天排毒量不同。
    3.  **观测层：** 建立概率模型处理测量噪声。它特别设计了处理“未检出（Non-detects）”和“离群点”的机制，直接输入原始数据，不需要人工预处理。
*   **关键设计取舍：** 放弃了复杂的全机械模型（需要太多假设参数），选择了“半机械”架构，既保留了生物学规律，又保证了在数据稀疏时的计算稳定性。

### 4. 实验部分
*   **数据：** 2022 年至 2025 年间，瑞士 6 到 14 个污水处理厂的实测数据。
*   **任务：** 实时估算 $R_t$ 值，并预测未来 14 天的病毒浓度。
*   **对比目标（Baseline）：** 传统的临床监测数据（医院报告的病例数）。
*   **评价指标：** $R_t$ 的一致性、预测准确度（CRPS 评分）、偏差（Bias）。
*   **主要结果：** 
    *   即使流感和 RSV 浓度极低，模型给出的 $R_t$ 趋势与临床数据高度吻合。
    *   在采样频率从每天一次降至每周两次时，模型依然能保持无偏预测，只是置信区间（不确定性）会变大。

### 5. 资源与算力
*   **文中未充分披露：** 论文未详细列出具体的 GPU/CPU 训练时长。但基于其贝叶斯推断框架（通常使用 Stan 或类似的 MCMC/变分推断工具），该模型在普通服务器或高性能工作站上即可运行，不属于超大规模算力消耗型任务。

### 6. 真正可信的贡献
*   **端到端处理能力：** 证明了无需人工清洗数据（如平滑、插值、删离群点），直接用贝叶斯框架处理“脏数据”是可行的。
*   **低丰度病原体验证：** 证实了废水监测不仅适用于新冠，也完全适用于浓度更低、更难测的季节性流感和 RSV。
*   **不确定性量化：** 模型不仅给出一个预测值，还能告诉决策者“我有多大把握”，这在公共卫生决策中至关重要。

### 7. 局限与风险
*   **排毒参数依赖：** 模型仍需预设一个“排毒分布曲线”。如果某种新病毒的排毒规律与已知病毒完全不同，模型初期可能会有偏差。
*   **地理局限性：** 实验数据全部来自瑞士，其下水道系统和人口密度较为均衡。在基础设施较差或人口流动极大的地区，模型参数可能需要重新校准。
*   **实验室检测限：** 如果废水中病毒浓度低于实验室物理检测的极限，模型也无法“无中生有”。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事时序预测、状态空间模型、公共卫生 AI 以及环境基因组学的研究者。
*   **后续可跟进的问题：** 如何利用深度学习（如 Neural ODE 或 Transformer）来替代或增强半机械模型中的排毒卷积部分，以自动学习不同病原体的排毒特征？

（完）
