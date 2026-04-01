---
title: "HistoGWAS: an AI-enabled framework for automated genetic analysis of tissue phenotypes in histology cohorts."
title_zh: HistoGWAS：一种用于组织学队列中组织表型自动化遗传分析的 AI 赋能框架
authors: "Shubham Chaudhary, Almut Voigts, Michael Bereket, Matthew L Albert, Kristina Schwamborn, Eleftheria Zeggini, Francesco Paolo Casale"
date: 2026-03-31
pdf: "https://pubmed.ncbi.nlm.nih.gov/41918129/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 利用基础模型进行自动性状定义和变异效应解释
tldr: 针对组织病理学图像中遗传变异如何影响组织结构的分析难题，HistoGWAS 框架整合了视觉基础模型、方差分量模型和生成模型，实现了从自动特征提取到关联分析及效应解释的全流程自动化。在 GTEx 数据集的 11 种组织中，该方法成功识别出 4 个与组织表型显著相关的遗传位点（tissueQTLs），并揭示了其与复杂性状的联系，为大规模人群队列的组织遗传学研究提供了高效工具。
selection_source: fresh_fetch
motivation: 现有的组织病理学遗传分析缺乏可扩展且通用的自动化框架，难以大规模探索基因变异对组织微观结构的影响。
method: 该框架利用视觉基础模型自动定义组织特征，结合方差分量模型进行高效的关联检测，并使用生成模型直观解释变异对表型的影响。
result: 在 GTEx 项目的 11 种组织中发现了 4 个具有全基因组显著性的组织数量性状位点（tissueQTLs），并证明了其在处理大规模队列时的扩展性。
conclusion: HistoGWAS 填补了组织图像与遗传关联分析之间的技术空白，为理解遗传变异如何通过改变组织结构进而影响复杂疾病提供了新途径。
---

## 摘要
理解遗传变异如何塑造组织结构对于疾病生物学至关重要，然而目前仍缺乏用于组织学特征遗传分析的可扩展、通用框架。我们提出了 HistoGWAS，这是一个用于组织学数据全基因组关联研究的框架，它利用基础模型进行自动化特征定义，利用方差分量模型进行高效的关联检测，并利用生成模型进行变异效应解释。通过对来自基因型-组织表达（GTEx）项目的 11 种组织进行分析，HistoGWAS 识别出四个与组织组织学相关的全基因组显著位点——即组织数量性状位点（tissueQTLs），并将其与分子变化和复杂性状联系起来。效能分析证明了该框架对人群规模组织学队列的可扩展性。

## Abstract
Understanding how genetic variation shapes tissue structure is crucial for disease biology, yet scalable, general-purpose frameworks for genetic analysis of histology traits are lacking. We present HistoGWAS, a framework for genome-wide association studies of histology data that leverages foundation models for automated trait definition, variance component models for efficient association testing, and generative models for variant effect interpretation. Applied to 11 tissues from the Genotype-Tissue Expression project, HistoGWAS identifies four genome-wide significant loci associated with tissue histology-tissue quantitative trait loci (tissueQTLs)-which we link to molecular changes and complex traits. Power analyses demonstrate scalability to population-scale histology cohorts.