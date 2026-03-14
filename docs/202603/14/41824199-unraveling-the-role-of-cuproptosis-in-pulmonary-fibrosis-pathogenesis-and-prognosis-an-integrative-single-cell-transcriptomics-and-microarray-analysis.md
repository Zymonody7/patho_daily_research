---
title: "Unraveling the role of cuproptosis in pulmonary fibrosis pathogenesis and prognosis: an integrative single-cell transcriptomics and microarray analysis."
title_zh: 揭示铜死亡在肺纤维化发病机制和预后中的作用：一项单细胞转录组学与微阵列分析的整合研究
authors: "Mengting Chen, Jialu Chen, Jiaxiang Zhang, Yong Zhu, Xiaoxiao Meng, Zhengfeng Yang, Ruilan Wang"
date: 2026-03-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/41824199/"
tags: ["query:seqai"]
score: 8.0
evidence: 整合单细胞转录组学和微阵列分析进行预后建模
tldr: "肺纤维化（PF）是一种病理机制复杂的间质性肺病。本研究通过整合单细胞转录组与大体转录组数据，利用LASSO和Cox回归筛选出4个关键的铜死亡相关基因（LIAS, LIPT1, ATP7A, PDHB），构建了预后风险模型。实验验证发现，这些基因在纤维化组织中显著下调，揭示了铜死亡与肺纤维化进展呈负相关，为临床预后评估和靶向治疗提供了新视角。"
selection_source: fresh_fetch
motivation: 旨在探究铜死亡这一新型细胞死亡方式在肺纤维化发病机制中的生物学功能，并建立有效的临床预后预测模型。
method: 整合小鼠模型单细胞测序与人类特发性肺纤维化转录组数据，通过机器学习算法筛选关键基因，并结合体外细胞实验与临床样本进行多维度验证。
result: 成功构建了由LIAS等4个基因组成的风险评分模型，发现高风险患者生存率更低，且纤维化微环境中铜死亡相关基因表达普遍受抑制。
conclusion: 研究证实了铜死亡调节失衡与肺纤维化进展密切相关，为理解铜介导的纤维化调控机制提供了分子基础。
---

## 摘要
肺纤维化（PF）是一种发病机制尚不明确的进展性间质性肺疾病，目前仍是治疗上的挑战。新兴证据表明，铜死亡（一种铜依赖性细胞死亡途径）可能在疾病进展中发挥调节作用。本研究旨在阐明铜死亡的生物学功能并建立 PF 的预后模型。通过对博来霉素（BLM）诱导的小鼠模型单细胞 RNA-seq 数据和特发性肺纤维化（IPF）患者的大体 RNA-seq 数据进行整合分析，我们利用 LASSO 回归和 Cox 回归鉴定了铜死亡相关基因（CRGs）。在 GSE70866 队列中，我们构建了一个包含 4 个 CRG（LIAS、LIPT1、ATP7A、PDHB）的新型特征模型，将患者分为不同的风险组；GO/KEGG 分析显示，高风险个体的生存率更低，且细胞外基质/脂质代谢活性增强。在 BLM 诱导的小鼠模型、TGF-β1 刺激的成纤维细胞向肌成纤维细胞转化实验以及人类 IPF 标本中进行的实验验证，通过 qRT-PCR 和免疫组化分析证实了 CRGs 的显著下调。功能实验揭示了在纤维化微环境中细胞活力受损且铜死亡标志物升高。我们的研究结果确立了铜死亡与 PF 进展之间的负相关关系，并提出了一种用于临床预后预测的稳健风险评分模型。这种多组学方法为纤维化过程中铜介导的调节机制提供了新见解。

## Abstract
Pulmonary fibrosis (PF), a progressive interstitial lung disease with elusive pathogenesis, remains a therapeutic challenge. Emerging evidence suggests cuproptosis-a copper-dependent cell death pathway-may play a regulatory role in disease progression. This study aims to elucidate cuproptosis's biological function and establish a prognostic model for PF. Through integrative analysis of single-cell RNA-seq data from bleomycin (BLM)-induced mouse models and bulk RNA-seq data from idiopathic pulmonary fibrosis (IPF) patients, we identified cuproptosis-related genes (CRGs) using LASSO regression and Cox regression. A novel 4-CRG signature (LIAS, LIPT1, ATP7A, PDHB) was constructed to stratify patients into distinct risk groups in the GSE70866 cohort, where high-risk individuals exhibited poorer survival and enhanced extracellular matrix/lipid metabolism activity via GO/KEGG analysis. Experimental validation in BLM-induced mouse models, TGF-β1-stimulated fibroblast-to-myofibroblast transition assays, and human IPF specimens demonstrated significant downregulation of CRGs through qRT-PCR and immunohistochemical analyses. Functional assays revealed impaired cell viability and elevated cuproptosis markers in fibrotic microenvironments. Our findings establish an inverse correlation between cuproptosis and PF progression, and propose a robust risk-score model for clinical prognosis prediction. This multi-omics approach provides new insights into copper-mediated regulatory mechanisms in fibrogenesis.

---

## 论文详细总结（自动生成）

这篇论文通过整合单细胞测序和临床转录组数据，探讨了**铜死亡（Cuproptosis）**这一新型细胞死亡方式在**肺纤维化（PF）**中的作用。

### 1. 这篇论文到底在解决什么问题，为什么值得看？
*   **核心问题**：肺纤维化（肺组织变厚、变硬，像结疤一样）的病理机制非常复杂，目前缺乏有效的预后预测手段。
*   **研究价值**：论文聚焦于2022年才被正式命名的“铜死亡”（一种由铜离子积累引发的特殊细胞死亡方式）。研究者想弄清楚：铜死亡相关基因是否能作为判断肺纤维化病人活多久的“风向标”，以及这些基因在疾病发展中到底扮演了什么角色。

### 2. 白话版概述
*   肺纤维化就像肺部在不断“长疤”，最终导致呼吸衰竭。
*   科学家发现细胞内铜太多会诱发一种特殊的死亡（铜死亡），这可能和肺部“长疤”有关。
*   研究者利用计算机算法从成千上万个基因中挑出了4个关键的“铜死亡基因”，并建立了一个评分模型。
*   结果发现：这4个基因表达越低，病人风险越高，寿命越短。实验也证实，在纤维化的肺组织里，这些保护性的铜死亡信号确实被减弱了。

### 3. 方法部分
*   **核心思想**：采用“干湿结合”的策略。先用公共数据库的测序数据进行生物信息学建模（干实验），再用小鼠模型和人类临床样本进行验证（湿实验）。
*   **模型构建流程**：
    1.  **筛选**：从小鼠单细胞数据（scRNA-seq）中观察哪些铜死亡基因在纤维化细胞中活跃。
    2.  **降维与回归**：利用 **LASSO 回归**（一种能从大量变量中剔除干扰项、防止过拟合的统计方法）和 **Cox 回归**（专门分析生存时间的模型），从候选基因中精炼出 4 个核心基因（LIAS, LIPT1, ATP7A, PDHB）。
    3.  **评分系统**：根据这 4 个基因的表达量加权计算出一个“风险得分”，将患者分为高风险和低风险组。
*   **关键设计取舍**：研究者没有只看人类数据，而是整合了小鼠单细胞数据，这有助于定位这些基因具体是在哪种细胞（如成纤维细胞）中起作用的。

### 4. 实验部分
*   **数据来源**：
    *   **单细胞数据**：博来霉素（BLM）诱导的小鼠肺纤维化模型。
    *   **临床数据**：GSE70866 队列（包含特发性肺纤维化患者的转录组和生存信息）。
*   **验证任务**：
    *   **生存分析**：高风险组患者的生存率显著低于低风险组。
    *   **功能富集**：高风险组表现出更强的细胞外基质（ECM）堆积和脂质代谢异常。
    *   **生物学验证**：在小鼠模型和人类 IPF 标本中，通过 **qRT-PCR**（检测 RNA 水平）和 **免疫组化 IHC**（检测蛋白质水平）确认了这 4 个基因在纤维化组织中是显著下调的。
*   **主要结果**：确立了铜死亡与肺纤维化进展之间的**负相关**关系（即铜死亡相关通路受阻可能促进了纤维化）。

### 5. 资源与算力
*   **文中未充分披露**。论文主要基于 R 语言环境下的标准生物信息学包（如 `glmnet`, `survival` 等）进行分析，此类计算通常在普通工作站即可完成，不涉及大规模深度学习算力。

### 6. 这篇论文真正可信的贡献是什么？
*   **证据链完整**：从“计算机筛选”到“小鼠实验”再到“人类临床样本验证”，证据层层递进，尤其是 4 个基因在蛋白水平（IHC）的下调证据非常直观。
*   **预后模型**：提出的 4 基因签名（LIAS, LIPT1, ATP7A, PDHB）为肺纤维化的临床预后评估提供了一个潜在的分子工具。

### 7. 局限与风险
*   **因果关系尚不明确**：虽然研究发现这些基因下调与纤维化相关，但目前还不清楚是“基因下调导致了纤维化”，还是“纤维化环境导致了基因下调”。
*   **样本量限制**：临床验证主要依赖于公开数据库，虽然有自己的临床样本验证，但样本规模仍需扩大以增强普适性。
*   **机制深度**：论文更多是在描述“现象”和“关联”，对于铜离子如何具体通过这 4 个基因调控成纤维细胞激活的分子细节挖掘较浅。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事多组学整合分析、生物标志物（Biomarker）筛选、以及对新型细胞死亡方式感兴趣的 AI 医疗研究者。
*   **后续可跟进的问题**：能否利用深度学习（如图神经网络 GNN）来模拟铜代谢通路与细胞外基质重塑之间的复杂相互作用，从而发现比线性回归模型更精准的干预靶点？

（完）
