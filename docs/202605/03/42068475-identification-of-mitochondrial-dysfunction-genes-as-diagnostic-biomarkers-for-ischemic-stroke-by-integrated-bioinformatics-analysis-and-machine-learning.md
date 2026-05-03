---
title: Identification of Mitochondrial Dysfunction Genes as Diagnostic Biomarkers for Ischemic Stroke by Integrated Bioinformatics Analysis and Machine Learning.
title_zh: 通过整合生物信息学分析和机器学习识别线粒体功能障碍基因作为缺血性脑卒中的诊断生物标志物
authors: "Dandan Wu, Xiaolan Huang, Jie Li, Dingmin Mo, Weiwei Lan, Zihan Song, Li Su, Jianxiong Long, Jialei Yang"
date: 2026-05-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/42068475/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 整合生物信息学分析与机器学习用于生物标志物鉴定
tldr: 针对缺血性中风（IS）诊断时效性不足的问题，本研究整合生物信息学与机器学习技术，从线粒体功能障碍角度筛选关键基因。通过分析多个公共数据集并结合WGCNA与LASSO等算法，确定了MCL1等4个核心特征基因，并构建了神经网络等诊断模型。实验证明该模型在独立验证集中表现稳定，为IS的早期分子诊断提供了高准确度的生物标志物。
selection_source: fresh_fetch
motivation: 现有的缺血性中风诊断手段在及时性和普及性上存在局限，亟需寻找更高效的分子诊断标志物。
method: 整合差异表达分析与加权基因共表达网络分析（WGCNA）筛选线粒体相关基因，并利用LASSO、随机森林和SVM等机器学习算法提取特征并构建分类模型。
result: 识别出MCL1、MRPL46、MTX3和RNASEH1四个关键特征基因，所构建的神经网络模型在验证集上达到了0.852的AUC值。
conclusion: 该研究成功建立了基于多基因的缺血性中风诊断模型，为临床早期识别中风风险提供了新的分子生物学依据。
---

## 摘要
目前缺血性脑卒中（IS）的诊断缺乏及时性和可及性，凸显了对新型分子诊断模型的需求。本研究从公共数据库中检索了包含 IS 患者和健康对照受试者的三个基因表达数据集（GSE16561、GSE22255 和 GSE58294）。从 GeneCards 和 MitoCarta3.0 数据库的交集中获取了线粒体功能障碍基因。利用 limma 和 WGCNA 软件包获取与 IS 相关的基因。通过 LASSO、RF 和 SVM 筛选特征基因，并使用 NeighborMethod、NeuralNet 和 BayesMethod 构建诊断模型。与对照组相比，在 IS 患者中鉴定出 3548 个差异表达基因（DEGs）（1538 个上调，2010 个下调）。WGCNA 分析得到了 10 个包含 1643 个基因的 IS 相关模块。DEGs、模块基因与线粒体功能障碍基因的交集共产生 100 个与 IS 相关的线粒体功能障碍基因。这些基因共同调节线粒体 ATP 合成偶联电子传递和呼吸电子传递链等生物过程，并参与活性氧和氧化磷酸化等 IS 相关信号通路。进一步的机器学习方法鉴定了 4 个特征基因，包括 MCL1、MRPL46、MTX3 和 RNASEH1。这四个基因在合并数据集中表现出稳健的诊断潜力（所有 AUC > 0.7）。机器学习模型的 AUC 值分别为 0.814（NeighborMethod）、0.852（NeuralNet）和 0.842（BayesMethod）。使用独立队列进行的外部验证证实，所有模型均保持了较高的诊断准确性（AUC 范围：0.730-0.783）。本研究建立了 IS 的多基因诊断模型，鉴定了新型分子生物标志物，旨在提高 IS 诊断的及时性和可及性。

## Abstract
Current diagnostics for ischemic stroke (IS) lack timeliness and accessibility, highlighting the need for novel molecular diagnostic models. Three gene expression datasets (GSE16561, GSE22255 and GSE58294), encompassing both IS patients and healthy control subjects, were retrieved from a public database. The mitochondrial dysfunction genes retrieve from the intersection of the GeneCards and MitoCarta3.0 databases. The limma and WGCNA package were used to obtain the genes related to IS. Feature genes were screened using LASSO, RF, SVM, and diagnostic models were constructed using NeighborMethod, NeuralNet, and BayesMethod. 3548 differentially expressed genes (DEGs) (1538 upregulated, 2010 downregulated) were identified in IS patients when compared to controls. WGCNA analysis yielded 10 IS-related modules containing 1643 genes. The intersection of DEGs, module genes, and mitochondrial dysfunction genes yielded 100 mitochondrial dysfunction genes associated with IS. These genes collectively regulate biological processes like mitochondrial ATP synthesis coupled electron transport and respiratory electron transport chain, and participate in IS-associated signaling pathways such as reactive oxygen species and oxidative phosphorylation. Further machine learning methods identified 4 feature genes, including MCL1, MRPL46, MTX3 and RNASEH1. These four genes exhibited robust diagnostic potential in the merged dataset (all AUC > 0.7). The machine learning models achieved AUC values of 0.814 (NeighborMethod), 0.852 (NeuralNet), and 0.842 (BayesMethod). External validation using an independent cohort confirmed that all models maintained high diagnostic accuracy (AUC range: 0.730-0.783). This study established a multi-gene diagnostic model for IS, identifying novel molecular biomarkers to improve the timeliness and accessibility of IS diagnosis.

---

## 论文详细总结（自动生成）

这篇论文通过整合生物信息学分析与机器学习算法，旨在寻找能够早期诊断**缺血性脑卒中（IS，俗称“中风”）**的分子标志物。

### 1. 解决的问题与研究意义
*   **核心问题**：中风的诊断讲究“时间就是大脑”，但目前的影像学检查（如CT/MRI）在基层医院普及性有限，且有时无法捕捉极早期的分子变化。
*   **研究意义**：研究者试图从**线粒体功能障碍**（线粒体是细胞的“能量工厂”，中风时由于缺氧，这些工厂会率先崩溃并释放信号）的角度，寻找血液中可检测的基因标志物，从而开发出一种更快速、低成本的分子诊断手段。

### 2. 白话版概述
想象中风发生时，大脑细胞里的“能量工厂”（线粒体）会集体发出“求救信号”。这篇论文先从海量的基因数据中筛选出那些确实在求救的基因，再利用 AI 算法从几千个信号中精准锁定了 4 个最关键的“警报灯”（特征基因）。最后，利用这些基因构建了一个分类器，只要检测这几个基因的表达水平，AI 就能判断这个人是否患有中风，准确率相当高。

### 3. 方法部分
*   **核心思想**：结合“生物学先验知识”与“数据驱动的机器学习”。
*   **技术流程**：
    1.  **差异筛选**：利用 `limma` 包找出中风患者和健康人之间表达量差异巨大的基因。
    2.  **共表达网络分析 (WGCNA)**：这是一种聚类算法，把功能相似、经常一起“出没”的基因聚成模块，找出与中风关联最紧密的基因群。
    3.  **知识库取交集**：将上述筛选出的基因与已知的线粒体功能障碍数据库（GeneCards, MitoCarta3.0）取交集，确保筛选出的基因在生物学上是有意义的。
    4.  **特征降维（关键步骤）**：使用三种机器学习算法（LASSO回归、随机森林RF、支持向量机SVM-RFE）进行交叉筛选，剔除冗余，最终只保留 4 个核心特征基因。
    5.  **模型构建**：基于这 4 个基因，对比了神经网络（NeuralNet）、贝叶斯（Bayes）和近邻法（Neighbor）三种分类模型的诊断效果。

### 4. 实验部分
*   **数据来源**：来自公共数据库 GEO 的三个数据集（GSE16561, GSE22255, GSE58294）作为训练集，另选独立数据集进行外部验证。
*   **任务**：二分类任务（中风患者 vs. 健康对照）。
*   **评价指标**：AUC（曲线下面积，越接近 1 代表分类越准）。
*   **主要结果**：
    *   锁定了 4 个核心基因：**MCL1, MRPL46, MTX3, RNASEH1**。
    *   **神经网络模型**表现最优，训练集 AUC 达到 **0.852**，外部验证集 AUC 保持在 **0.730-0.783** 之间，显示了良好的泛化能力。

### 5. 资源与算力
*   **文中未充分披露**。此类研究通常在常规工作站上使用 R 语言环境即可完成，不涉及大规模深度学习训练。

### 6. 真正可信的贡献
*   **多算法交叉验证**：它没有只依赖一种 AI 算法，而是通过 LASSO、RF、SVM 三种逻辑完全不同的算法共同筛选特征，这大大降低了“过拟合”到某个特定数据集的风险。
*   **生物学解释性强**：筛选出的 4 个基因均与线粒体呼吸链、氧化应激等中风核心病理过程高度相关，不是单纯的“黑盒”预测。

### 7. 局限与风险
*   **样本量瓶颈**：虽然整合了多个数据集，但总样本量依然在百人级别，对于 AI 模型来说数据量仍显单薄。
*   **回顾性研究**：所有数据均来自已有的数据库，缺乏临床实时采集的样本验证。
*   **落地障碍**：从“发现基因”到“临床检测试剂盒”还有很长的路，需要验证这些基因在血液中的稳定性以及检测成本。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：正在做“小样本、高维度”生物数据挖掘，或关注“可解释性 AI”的研究者。
*   **后续可跟进的问题**：能否将 WGCNA 产生的基因关联网络直接转化为**图神经网络（GNN）**的输入，从而利用基因间的拓扑关系进一步提升诊断精度？

（完）
