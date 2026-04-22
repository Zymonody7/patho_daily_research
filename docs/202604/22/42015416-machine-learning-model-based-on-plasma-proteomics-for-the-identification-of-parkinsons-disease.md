---
title: "Machine learning model based on plasma proteomics for the identification of Parkinson's disease."
title_zh: 基于血浆蛋白质组学识别帕金森病的机器学习模型
authors: "Boluwatife Adewale, Ruth Chia, Ruin Moaddel, Natalie Landeck, Memoona Rasheed, Camille Alba, Paolo Reho, Rosario Vasta, Andrea Calvo, Cristina Moglia, Antonio Canosa, Umberto Manera, Allison Snyder, Yi-Jung Lee, Maurizio Grassano, Christine Gao, Min Zhu, Maura Brunetti, Federico Casale, Kumar Arvind, American Genome Center, Ted M Dawson, Liana S Rosenthal, Anna J Hall, Alexander Y Pantelyat, Jinhui Ding, J Raphael Gibbs, Josephine M Egan, Julián Candia, Toshiko Tanaka, Luigi Ferrucci, Adriano Chiò, Derek P Narendra, Justin Y Kwan, Debra J Ehrlich, Clifton L Dalgard, Bryan J Traynor, Sonja W Scholz"
date: 2026-04-22
pdf: "https://pubmed.ncbi.nlm.nih.gov/42015416/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 基于血浆蛋白质组学的机器学习模型
tldr: 针对帕金森病（PD）诊断中缺乏可靠生物标志物的问题，本研究利用高通量血浆蛋白质组学技术，结合 Boruta 特征筛选和 Stacking 集成学习模型，从 698 名受试者中识别出 11 种关键蛋白标志物。该模型在多个独立外部队列中表现出高准确度（AUC 最高达 0.939），不仅提升了 PD 的临床诊断精度，还通过 SHAP 解释揭示了炎症和脂质代谢等潜在病理机制。
selection_source: fresh_fetch
motivation: 旨在开发一种能够将帕金森病与健康人群及其他神经系统疾病准确区分的血浆蛋白质生物标志物面板。
method: 采用 Olink 高通量技术获取血浆蛋白谱，通过 Boruta 算法筛选出 11 种核心蛋白，并构建 Stacking 集成机器学习模型进行分类预测。
result: 模型在测试集和三个外部大型队列（如 UK Biobank）中均表现稳健，AUC 值介于 0.789 至 0.939 之间，验证了标志物的普适性。
conclusion: 该研究证明了基于血浆蛋白质组学的机器学习模型在帕金森病早期诊断和病理机制探索中的临床应用潜力。
---

## 摘要
开发能够区分帕金森病与其他神经系统疾病的可靠生物标志物，对于患者护理和科学研究都至关重要。在本研究中，我们利用高通量蛋白质组学技术和机器学习的最新进展，开发了帕金森病的候选生物标志物。利用 Olink Explore 3072 检测技术，我们获取了 698 名研究参与者的血浆蛋白质组图谱，其中包括帕金森病患者（n = 149）、神经系统健康的对照组（n = 230）以及患有其他神经系统疾病的参与者（n = 319）。研究队列被分为训练集（n = 560）和测试集（n = 138）。我们进行了蛋白质差异丰度分析和通路富集分析，随后应用 Boruta 算法识别出对帕金森病具有预测能力的差异丰度蛋白。为了构建诊断生物标志物组合，我们在训练集（包括 118 名帕金森病患者、184 名健康对照和 258 名患有其他神经系统疾病的个体）上训练了一个堆叠集成机器学习（ML）模型，并使用 11 种蛋白质（APOH、ARG1、CCN1、CXCL1、CXCL8、DDC、GRAP2、IL1RAP、OSM、PRL 和 SPRY2）作为模型特征。我们使用 Shapley Additive Explanations (SHAP) 框架和网络分析来评估 ML 模型中每种蛋白质的预测重要性和生物学相关性。该模型在留出测试集（n = 138）和三个外部队列——英国生物样本库（UK Biobank，n = 43,969）、帕金森病生物标志物项目（PDBP，n = 138）以及帕金森病进展标志物倡议（PPMI，n = 385）中均表现出高准确性，受试者工作特征曲线下面积（AUC）分别为 0.939、0.789、0.909 和 0.816。此外，网络和通路分析有助于解释模型，揭示了与炎症介质、ErbB 信号传导、T 细胞受体信号传导和脂质代谢相关的活动。我们的研究结果强调了血浆蛋白生物标志物在改善帕金森病诊断和加深对这一复杂神经系统疾病生物学理解方面的潜力。我们的模型在多个独立队列中表现出高特异性和可靠性，表明基于蛋白质组学的生物标志物具有巨大潜力，以及机器学习辅助诊断在帕金森病护理中的临床实用性。该模型还有助于阐明与帕金森病相关的潜在新型风险因素和通路。

## Abstract
Developing reliable biomarkers capable of differentiating Parkinson's disease from other neurological conditions is crucial for both patient care and research. In this study, we leveraged recent advances in high-throughput proteomic technology and machine learning to develop candidate biomarkers for Parkinson's disease. Using the Olink Explore 3072 assay, we obtained plasma proteomic profiles from 698 study participants, comprising Parkinson's disease cases (n = 149), neurologically healthy controls (n = 230), and participants with other neurological conditions (n = 319). The study cohort was split into Training Set (n = 560) and Test Set (n = 138). We conducted differential protein abundance analysis and pathway enrichment analysis, and subsequently applied the Boruta algorithm to identify differentially abundant proteins that are predictive of Parkinson's disease. To create a diagnostic biomarker panel, we trained a stacking ensemble machine learning (ML) model on the Training Set (n = 118 Parkinson's patients, n = 184 healthy controls, and n = 258 individuals with other neurological disorders) using eleven proteins (APOH, ARG1, CCN1, CXCL1, CXCL8, DDC, GRAP2, IL1RAP, OSM, PRL, and SPRY2) as model features. We used the Shapley Additive Explanations (SHAP) framework and network analysis to evaluate predictive importance and biological relevance of each protein in the ML model. The model demonstrated high accuracy in the held-out Test Set (n = 138) and three external cohorts-the UK Biobank (n = 43,969), the Parkinson's Disease Biomarkers Program (n = 138), and the Parkinson's Progression Markers Initiative (n = 385), with areas under the receiver operating characteristic curve of 0.939, 0.789, 0.909, 0.816, respectively. Additionally, network and pathway analyses helped interpret the model, revealing activity related to inflammatory mediators, ErbB signaling, T-cell receptor signaling, and lipid metabolism. Our findings highlight the potential of plasma protein biomarkers to improve Parkinson's disease diagnosis and deepen biological understanding of this complex neurological disorder. Our model demonstrates high specificity and reliability across multiple independent cohorts, indicating the significant potential of proteomics-based biomarkers and the clinical utility of ML-supported diagnosis in Parkinson's disease care. The model also helps to elucidate potential novel risk factors and pathways associated with Parkinson's disease.

---

## 论文详细总结（自动生成）

这篇论文利用高通量蛋白质组学技术和集成机器学习算法，旨在为帕金森病（PD）寻找一种可靠的血液诊断标志物。

### 1. 解决的问题与研究意义
*   **核心问题**：帕金森病（PD）目前的诊断高度依赖临床症状观察，缺乏客观的生物学指标（如抽血化验）。这导致早期诊断困难，且容易与多系统萎缩等其他神经系统疾病混淆。
*   **研究意义**：如果能通过血浆中的蛋白质“指纹”准确识别 PD，不仅能实现早期筛查，还能为药物研发提供精准的疗效评价工具。

### 2. 白话版概述
研究人员像“大海捞针”一样，从人体血浆中检测了约 3000 种蛋白质。他们利用 AI 算法从这几千个指标中筛选出了最关键的 **11 种蛋白质**。随后，他们构建了一个“模型超市”（集成学习模型），让多个算法共同投票来判断一个人是否患有帕金森病。这个模型不仅能分清健康人和病人，还能在患有其他类似神经疾病的人群中精准锁定帕金森患者。

### 3. 方法部分
*   **核心思想**：特征筛选（降维）+ 集成学习（提升鲁棒性）。
*   **特征筛选（Boruta 算法）**：这是一种基于随机森林的特征选择方法。它通过对比原始特征与随机打乱的“影子特征”，剔除掉那些表现不如随机噪声的蛋白质，最终锁定了 11 种核心蛋白（如 DDC、APOH 等）。
*   **模型结构（Stacking Ensemble）**：采用了“堆叠集成”策略。即训练多个基础分类器（Base Learners），再用一个元分类器（Meta-Learner）对它们的输出进行加权融合。这种方法比单一模型更稳定，能有效减少过拟合。
*   **可解释性设计**：引入了 **SHAP (Shapley Additive Explanations)** 框架。这在 AI 医疗中至关重要，它能告诉医生：模型判定某人患病，是因为蛋白 A 升高了多少，蛋白 B 降低了多少，让“黑盒”模型变得透明。

### 4. 实验部分
*   **数据规模**：
    *   **内部队列**：698 人（包含 PD 患者、健康对照以及其他神经疾病患者）。
    *   **外部验证**：使用了三个独立的大型数据库：UK Biobank（约 4.4 万人）、PDBP 和 PPMI。
*   **任务目标**：二分类任务（PD vs. 非 PD）。
*   **评价指标**：AUC（受试者工作特征曲线下面积，越接近 1 越准）。
*   **主要结果**：
    *   内部测试集 AUC 达到 **0.939**。
    *   在极具挑战性的外部验证集（如 UK Biobank）中，AUC 依然保持在 **0.789 - 0.909** 之间。
    *   这证明了该模型不是在“背答案”（过拟合），而是真正学到了疾病的生物学特征。

### 5. 资源与算力
*   **文中未充分披露**。考虑到蛋白质组学数据属于结构化表格数据（Tabular Data），通常不需要大规模 GPU 集群，标准的 CPU 服务器或高性能工作站即可完成训练。

### 6. 真正可信的贡献
*   **跨队列验证**：最强的证据在于该模型在 UK Biobank 等多个完全独立的外部数据集上表现稳健，证明了 11 种蛋白标志物的普适性。
*   **高特异性**：模型不仅能区分健康人，还能区分“其他神经疾病”，这解决了临床诊断中最头疼的鉴别诊断问题。
*   **生物学对齐**：筛选出的蛋白（如 DDC，与多巴胺合成直接相关）具有明确的生物学意义，增强了 AI 结论的可信度。

### 7. 局限与风险
*   **外部表现下滑**：在 UK Biobank 上的 AUC（0.789）明显低于内部集（0.939），说明不同实验室的采样方式、检测批次效应（Batch Effect）仍会对模型产生干扰。
*   **因果性模糊**：AI 发现的是“相关性”，这 11 种蛋白的变化是 PD 的**原因**还是患病后的**结果**，仍需进一步生物学实验验证。
*   **人群多样性**：虽然样本量不小，但主要集中在特定族裔，对全球不同种族人群的适用性有待观察。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事临床生物标志物开发、蛋白质组学分析、以及关注医疗 AI 可解释性的研究者。
*   **后续可跟进的问题**：能否利用图神经网络（GNN）结合文中提到的蛋白质相互作用网络（PPI），进一步提升分类精度？或者研究这 11 种蛋白在 PD 发病前数年的动态变化趋势，实现“超早期”预警？

（完）
