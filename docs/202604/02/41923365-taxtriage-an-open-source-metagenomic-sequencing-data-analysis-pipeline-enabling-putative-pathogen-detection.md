---
title: "TaxTriage: An Open-Source Metagenomic Sequencing Data Analysis Pipeline Enabling Putative Pathogen Detection."
title_zh: TaxTriage：一种支持疑似病原体检测的开源宏基因组测序数据分析流水线
authors: "Brian Merritt, Jeremy D Ratcliff, Stanley Ta, Gunars Osis, Matthew R Mauldin, Peter M Thielen"
date: 2026-04-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41923365/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于病原体检测的宏基因组测序数据分析流程
tldr: 针对宏基因组测序中病原体识别效率与准确性问题，TaxTriage 推出了一套开源分析流程。它整合了序列分类、比对及从头组装技术，支持长短读长数据，并通过对比健康人群基准和已知病原体库来识别潜在威胁。实验证明其在保持高灵敏度的同时提升了特异性，为公共卫生和兽医临床诊断提供了灵活、可离线部署的自动化工具。
selection_source: fresh_fetch
motivation: 现有的宏基因组病原体检测工具往往依赖云端环境，且在区分正常共生菌群与真实致病菌方面存在识别困难。
method: 该流程基于 Nextflow 构建，综合利用序列分类、参考基因组比对和从头组装技术，并结合健康人群丰度基准进行置信度评分。
result: 在临床和疫情暴发数据集的评估中，该工具在保持高灵敏度的前提下，比同类云端分析流程具有更高的检测特异性。
conclusion: TaxTriage 为公共卫生和兽医领域提供了一个可定制、支持离线运行的开源方案，显著增强了复杂生物样本中病原体发现的可靠性。
---

## 摘要
动机：TaxTriage 是一个全面的病原体识别工作流，专为短读长和长读长非靶向 DNA 及 RNA 测序数据设计。通过结合读段分类、比对和从头组装方法，该工作流通过与经过整理的病原体库进行比较，并参考健康队列数据的丰度预期，来识别疑似病原体。利用 Nextflow™ (NF) 实现了灵活的安装选项，包括通过 NF Tower (Seqera Platform) 进行云端部署，以及在各种系统上进行本地安装，包括无需外部互联网访问的独立安装。最终的分析摘要被汇编成一份“生物体发现报告”（Organism Discovery Report），其中列出了可能的病原体及支持数据，包括自定义的置信度评分。结果：对已发表的计算机模拟（in silico）、临床和疫情数据集的评估表明，在检测预期病原体和合并感染方面，其性能与替代的云端处理流水线相当，具有相似的灵敏度和更高的特异性。为了支持公共卫生和兽医诊断社区，该工具整合了定制选项，以提高对特定宿主物种的检测性能。可用性与实现：TaxTriage 的源代码可在 https://github.com/jhuapl-bio/taxtriage 免费获取。TaxTriage v2.1.1 已存档于 Zenodo (https://zenodo.org/records/17081354)，以支持本手稿中所述的可重复性分析。补充信息：补充数据可在 Bioinformatics 在线获取。

## Abstract
MOTIVATION: TaxTriage is a comprehensive pathogen identification workflow designed for both short- and long-read untargeted DNA and RNA sequencing data. Combining read classification, mapping, and de novo assembly approaches, putative pathogens are identified through comparisons to curated pathogens and abundance expectations from healthy cohort data. Flexible installation options are enabled using Nextflow™ (NF), including cloud deployment via NF Tower (Seqera Platform) and local installation on a variety of systems, including standalone installations without external internet access. Final analysis summaries are compiled into an Organism Discovery Report, which lists likely pathogens and supporting data, including a custom confidence score. RESULTS: Evaluation of published in silico, clinical, and outbreak datasets identified performance comparable to alternative cloud-based processing pipelines for expected pathogen and co-infection detection with similar sensitivity and increased specificity. To support both public health and veterinary diagnostics communities, customization options have been incorporated to enable improved performance for host species of interest. AVAILABILITY AND IMPLEMENTATION: Source code for TaxTriage is freely available at https://github.com/jhuapl-bio/taxtriage. TaxTriage v2.1.1 has been archived on Zenodo at https://zenodo.org/records/17081354 to permit reproducible analysis as described in this manuscript. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.