---
title: NQO1-Mediated Anoikis Resistance and Immune Evasion Define a High-Risk Multi-Omic Subtype for Precision Management of T1 High-Grade Bladder Cancer.
title_zh: NQO1介导的失巢凋亡抗性和免疫逃逸定义了T1期高级别膀胱癌精准管理的高风险多组学亚型
authors: "Bin Guo, Chunru Xu, Shufan Fu, Qiang Cheng, Juan Li, Linkuo Shang, Gaojie Li, Yang Yang, Ying Wang, Yanqing Gong, Shengwei Xiong, Jian Fan, Changwei Yuan, Mei Zhang, Yifan Zuo, Elena Papaleo, Yue Shi, Yuan Liang, Xuesong Li, Hongzhao Li, Weimin Ci"
date: 2026-04-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41945867/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 癌症亚型的综合多组学分析
tldr: 针对T1期高级别膀胱癌（T1HG）预后差异大且缺乏精准分层手段的问题，本研究通过对147例样本进行多组学分析，鉴定出以NQO1介导的失巢凋亡抗性和免疫逃逸为特征的高危亚型T1HG1。该亚型进展率高且对BCG治疗反应差；研究揭示了NQO1通过抑制巨噬细胞与T细胞互作促进免疫逃逸的机制，并开发了机器学习模型T1HG-UCBguider，为患者的个体化治疗和早期膀胱全切决策提供了科学依据。
selection_source: fresh_fetch
motivation: 旨在解决T1期高级别膀胱癌在临床上难以区分高进展风险患者，导致治疗方案（如膀胱保留或全切）选择困难的问题。
method: 通过对147例肿瘤样本进行多组学整合分析鉴定分子亚型，并利用机器学习构建了融合临床、转录组和甲基化特征的风险分层框架。
result: 发现NQO1是驱动高危亚型产生失巢凋亡抗性和免疫逃逸的核心因子，其通过抑制巨噬细胞分泌CXCL9来阻碍T细胞招募。
conclusion: NQO1介导的生物学机制为T1HG膀胱癌提供了新的治疗靶点，而T1HG-UCBguider模型则实现了对患者进展风险和治疗响应的精准预测。
---

## 摘要
T1期高级别（T1HG）膀胱癌是非肌层浸润性膀胱癌（NMIBC）中具有侵袭性的子集，常出现卡介苗（BCG）治疗失败且进展风险高，然而目前的模型不足以指导早期膀胱全切术与保留膀胱治疗之间的选择。通过对147例肿瘤进行整合多组学分析，鉴定了两个临床特征截然不同的亚型。高风险亚型（T1HG1）以失巢凋亡抗性和免疫逃逸耦合为特征，表现出显著升高的进展率（>80% vs. <20%）、较差的BCG反应性以及更高的膀胱全切术可能性。研究确定NAD(P)H:醌氧化还原酶1（NQO1）是连接肿瘤内在生存与巨噬细胞-T细胞通讯抑制的核心调节因子。NQO1升高促进了失巢凋亡抗性，并将巨噬细胞重编程为免疫抑制表型，限制了CXCL9介导的T细胞招募并促进了免疫逃逸。在临床前模型中，使用黄芩素II（skullcapflavone II）对NQO1进行药理学抑制可恢复凋亡敏感性并增强顺铂疗效，从而在具有良好耐受性的情况下实现显著的肿瘤抑制。一种名为T1HG-UCBguider的T1HG尿路上皮癌（UCB）多组学机器学习框架，整合了临床、转录组和甲基化特征，实现了个体化风险分层和治疗指导。在七个独立队列中的验证表明，该框架在识别具有进展风险和BCG失败风险的患者方面具有稳健的性能。这些发现为T1HG膀胱癌的精准管理建立了一个基于生物学的框架。

## Abstract
T1 high-grade (T1HG) bladder cancer represents an aggressive subset of non-muscle-invasive bladder cancer (NMIBC) with frequent Bacillus Calmette-Guérin (BCG) failure and a high risk of progression, yet current models inadequately guide treatment selection between early cystectomy and bladder preservation. Integrative multi-omics profiling of 147 tumors identifies two clinically distinct subtypes. A high-risk subtype (T1HG1) is defined by coupled anoikis resistance and immune evasion, exhibiting markedly increased progression rates (>80% vs. <20%), poor BCG responsiveness, and a higher likelihood of cystectomy. NAD(P)H:quinone oxidoreductase 1 (NQO1) is identified as a central regulator linking tumor-intrinsic survival to suppression of macrophage-T cell crosstalk. Elevated NQO1 promotes anoikis resistance and reprograms macrophages toward an immunosuppressive phenotype, limiting CXCL9-mediated T cell recruitment and facilitating immune escape. Pharmacologic inhibition of NQO1 using skullcapflavone II restores apoptotic sensitivity and enhances cisplatin efficacy, resulting in significant tumor suppression with favorable tolerability in preclinical models. A multi-omic machine learning framework for T1HG UCB, termed T1HG-UCBguider, integrating clinical, transcriptomic, and methylation features, enables individualized risk stratification and treatment guidance. Validation across seven independent cohorts, demonstrates robust performance in identifying patients at risk of progression and BCG failure. These findings establish a biologically grounded framework for precision management of T1HG bladder cancer.