---
title: Combining multiplexed assays of variant effect for enhanced BRCA2 variant classification.
title_zh: 结合变异效应多重检测以增强 BRCA2 变异分类
authors: "Chunling Hu, Sounak Sahu, Wenan Chen, Melissa Galloux, Marcy E Richardson, Megan F Bishop, Rachid Karam, Tina Pesaran, Jie Na, Huaizhi Huang, Jeffrey N Weitzel, Katherine N Nathanson, Siddhartha Yadav, Nicholas J Boddicker, Susan M Domchek, Alvaro N Monteiro, Edwin S Iversen, Shyam K Sharan, Fergus J Couch"
date: 2026-04-09
pdf: "https://pubmed.ncbi.nlm.nih.gov/41957374/"
tags: ["query:seqai"]
score: 7.0
evidence: 用于基因组变异分类的复合模型
tldr: "针对 BRCA2 基因中大量意义不明变异（VUS）导致的临床评估难题，本研究整合了两项针对其 C 端 DNA 结合域的饱和基因组编辑（SGE）实验数据，构建了 Integrated VarCall 复合模型。该模型在 6383 个变异位点上实现了 98.8% 的分类准确率，优于单一研究。结合 ClinGen 临床标准，研究成功对 92.8% 的变异进行了明确的致病性或良性分类，显著提升了 BRCA2 变异的临床解读能力。"
selection_source: fresh_fetch
motivation: 旨在解决 BRCA2 基因中大量变异因缺乏功能证据而无法在临床上明确分类为致病或良性的问题。
method: 通过整合两项独立的大规模饱和基因组编辑研究的原始功能数据，构建并评估了四种用于变异分类的复合计算模型。
result: "Integrated VarCall 模型在 6383 个变异中达到 98.8% 的准确率，并协助将 5926 个变异依据 ClinGen 标准进行了明确分类。"
conclusion: 多源大规模功能实验数据的整合能有效消除单一研究的偏差，为遗传性癌症风险评估提供更高精度的变异分类证据。
---

## 摘要
确定 BRCA2 意义未明变异的临床相关性对于知情的风险管理至关重要。最近，两项饱和基因组编辑研究评估了 BRCA2 C 端 DNA 结合域中所有单核苷酸变异的功能效应。为了提高用于 ACMG/AMP 变异分类的功能数据的准确性，我们将这些研究的结果整合到四个复合模型中，并使用已知分类的变异评估了每个模型的性能。在此，我们展示了一个“集成 VarCall 模型”（Integrated VarCall Model），该模型结合了原始研究中 6383 个变异的原始功能数据，实现了 98.8% 的准确率，且表现优于原始研究和其他组合数据模型。根据 ClinGen BRCA1/2 变异管理专家小组的规范，将“集成 VarCall 模型”的功能数据与其他证据来源相结合，最终将 5926 个（92.8%）BRCA2 变异分类为致病性（n = 735）或良性（n = 5191），为携带 BRCA2 变异的个体提供了宝贵的见解。

## Abstract
Determining the clinical relevance of BRCA2 variants of uncertain significance is critical for informed risk management. Recently, two saturation genome editing studies assessed the functional effects of all single nucleotide variants in the BRCA2 C-terminal DNA Binding Domain. To improve the accuracy of functional data used for ACMG/AMP variant classification, we combined results from these studies in four composite models and evaluated the performance of each model using variants with known classifications. Here, we show that an "Integrated VarCall Model", which combined raw functional data for 6383 variants from the original studies, yielded 98.8% accuracy and out-performed the original studies and other combined data models. Incorporation of the "Integrated VarCall Model" functional data with other sources of evidence according to ClinGen BRCA1/2 variant curation expert panel specifications resulted in classification of 5926 (92.8%) BRCA2 variants as pathogenic (n = 735) or benign (n = 5191) and provides valuable insights for individuals with BRCA2 variants.