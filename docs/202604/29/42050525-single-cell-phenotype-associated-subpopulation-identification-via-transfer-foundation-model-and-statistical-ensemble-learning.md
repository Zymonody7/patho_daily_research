---
title: Single-cell phenotype-associated subpopulation identification via transfer foundation model and statistical ensemble learning.
authors: "Yuming Zhao, Xiaonan Pan, Zeyu Luo, Qiaoming Liu"
date: 2026-04-29
pdf: "https://pubmed.ncbi.nlm.nih.gov/42050525/"
tags: ["query:seqai"]
score: 9.0
evidence: 结合预训练基础模型与VAE进行单细胞表型识别
tldr: 单细胞测序虽能揭示细胞异质性，但难以直接关联复杂的临床表型。为此，研究者开发了 scPASI 工具，通过整合预训练大模型与残差变分自编码器提取特征，并利用统计集成学习量化细胞亚群与表型的关联。该方法能将细胞划分为四类表型相关组，在肿瘤状态、基因突变及预后预测等任务中表现优于现有方法，为识别疾病关键细胞亚群和治疗靶点提供了新框架。
selection_source: fresh_fetch
motivation: 旨在解决单细胞转录组数据难以直接与宏观临床表型（如疾病状态或生存期）建立直接关联的挑战。
method: 结合预训练基础模型与残差变分自编码器提取细胞特征，并利用 LASSO 和稀疏组 LASSO 回归模型推断细胞亚群与表型的关联强度。
result: 在多项数据集测试中，该方法准确识别了与肿瘤进展、基因突变及临床预后高度相关的细胞亚群，性能显著优于同类算法。
conclusion: scPASI 成功架起了单细胞异质性与宏观表型之间的桥梁，为发现疾病相关的细胞亚群及潜在治疗靶点提供了有效的计算框架。
---

## Abstract
BACKGROUND: Single-cell RNA sequencing (scRNA-seq) enables the characterization of cell types, states, and lineages within heterogeneous tissues, thereby providing unprecedented opportunities to dissect cellular heterogeneity. However, single-cell data alone cannot directly establish cell-phenotype relationships, which pose major challenges in linking cellular heterogeneity to complex traits and disease outcomes. RESULTS: Here, we introduce scPASI, which integrates single-cell and bulk-level information to uncover phenotype-associated cell subpopulations. scPASI combines a pre-trained foundation model (PFM) with a residual variational autoencoder (Res-VAE) to extract feature embeddings of cells and samples. Cell clusters are calculated using the Leiden algorithm, after which phenotype associations are inferred based on regression coefficients derived from LASSO and sparse group LASSO (SGL) models. This design enables scPASI to stratify cells into four subpopulations with different levels of phenotype association: strongly positive (SP), weakly positive (WP), strongly negative (SN), and weakly negative (WN) groups. Furthermore, scPASI characterizes phenotype-relevant genes within subpopulations and provides insights into the relationship between cellular heterogeneity and bulk phenotypes. Extensive evaluations across diverse datasets show that scPASI outperforms existing methods and generalizes well across multiple phenotype settings, including tumor status, genetic mutations, and clinical prognosis. Biological analyses demonstrate that signature genes derived from the identified subpopulations can distinguish tumor cells, genetic alterations, and survival outcomes. CONCLUSIONS: By bridging single-cell transcriptomics with phenotype information, scPASI can uncover biologically meaningful cell-phenotype associations underlying tumor biology, enabling the identification of disease-relevant subpopulations and providing a framework for potential therapeutic targeting.