---
title: Genomic and evolutionary factors influencing the prediction accuracy of optimal growth temperature in prokaryotes.
title_zh: 影响原核生物最适生长温度预测准确性的基因组与进化因素
authors: "Seiji Toki, Motomu Matsui, Kento Tominaga, Takao K Suzuki, Takashi Tsuchimatsu, Wataru Iwasaki"
date: 2026-04-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/41930963/"
tags: ["query:pathoai"]
score: 7.0
evidence: 利用机器学习根据基因组信息预测原核生物的生长温度
tldr: "针对原核生物最适生长温度（OGT）预测中嗜冷菌准确率低的问题，本研究分析了2,869种细菌基因组，发现快速演化导致的基因组成分滞后是主因。通过整合反映长期演化的基因组成分特征与反映短期演化的基因功能（基因存在/缺失）信息，构建了新预测模型，显著提升了嗜冷菌的预测精度，为微生物表型预测提供了结合演化时间尺度的通用框架。"
selection_source: fresh_fetch
motivation: 现有的基于基因组成分的温度预测模型在嗜冷菌上表现不佳，需要探究其背后的演化原因并提升预测精度。
method: "收集了2,869种细菌的OGT与基因组数据，构建了一个结合基因组组成特征（如GC含量、密码子偏好）与基因存在/缺失信息的机器学习模型。"
result: 发现OGT快速变化的物种其基因组成分尚未完全优化，而引入特定功能基因信息能有效弥补这一预测偏差，并解释了古菌因演化保守性而更易预测的现象。
conclusion: 结合长期基因组优化与短期功能基因获取的演化视角，是提高微生物生理表型预测准确性的关键。
---

## 摘要
细菌和古菌已经进化出多种基因组适应策略，以在各种温度下生存。这些适应性包括基因组序列优化，例如 rRNA 和 tRNA 中 GC 含量的增加、密码子和氨基酸使用偏好的转变，以及获得赋予特定温度适应性的功能基因。由于最适生长温度（OGT）的实验测定仅适用于已培养物种，鉴于基因组数据的指数级增长，利用基因组信息预测 OGT 变得越来越重要。尽管之前的研究利用机器学习开发了整合基于基因组组成的多种特征的预测模型，但其准确性因目标物种而异，模型在嗜热菌中表现良好，但在嗜冷菌中准确性较低。在本研究中，我们整理了 2,869 种细菌的 OGT 和基因组数据，开发了一种新型预测模型，该模型纳入了反映向低温基因组适应的特征。我们发现，与祖先相比 OGT 发生快速转变的物种（包括嗜冷菌）在基于基因组组成的模型中表现出较低的准确性。纳入与 OGT 快速变化相关的基因存在/缺失信息，提高了对嗜冷菌的预测准确性。我们还观察到，古菌的 OGT 在系统发育上比细菌更保守，这可能导致了基因组组成的长期优化，并解释了古菌 OGT 的高可预测性。这些发现强调了在表型预测模型中整合长期和短期进化适应的重要性。重要性：利用基因组数据预测最适生长温度（OGT）有助于表征未培养微生物。本研究通过整理 2,869 种细菌的 OGT 和基因组数据开发了一种新型 OGT 预测模型，证明了通过不仅纳入反映长期温度适应的基因组组成特征，还纳入赋予短期适应的基因存在/缺失信息（特别是对于经历 OGT 快速转变的物种），可以提高预测准确性。我们的研究提供了一个通过整合长期和短期进化因素来改进表型预测模型的框架，这也可能适用于其他微生物生理表型。

## Abstract
Bacteria and archaea have evolved diverse genomic adaptations to thrive across various temperatures. These adaptations include genome sequence optimizations, such as increased GC content in rRNA and tRNA, shifts in codon and amino acid usage, and the acquisition of functional genes conferring adaptation for specific temperatures. Since the experimental determination of optimal growth temperatures (OGTs) is only possible for cultured species, predicting OGT from genomic information has become increasingly important given the exponential increase in genomic data. Although previous studies developed prediction models integrating multiple features based on genome composition using machine learning, the accuracy was variable depending on the target species, with models performing well for thermophiles but less accurately for psychrophiles. In this study, we curated the OGTs and genomic data of 2,869 bacterial species to develop a novel prediction model incorporating features reflecting genomic adaptation toward lower temperatures. We found that species with rapid OGT shifts from their ancestors, including psychrophiles, showed less accuracy in genome composition-based models. Incorporating the gene presence/absence information associated with the rapid changes in OGT improved the prediction accuracy for psychrophiles. We also observed that OGT in archaea is phylogenetically more conserved than in bacteria, which may lead to the long-term optimization of the genome composition and explain high predictability of OGT in archaea. These findings highlight the importance of integrating long- and short-term evolutionary adaptations for phenotype prediction models.IMPORTANCEPrediction of optimal growth temperature (OGT) from genomic data allows for characterizing uncultivated microbes. This study developed a novel OGT prediction model by curating OGT and genomic data of 2,869 bacterial species, demonstrating that the prediction accuracy was improved by incorporating not only genome composition features reflecting long-term temperature adaptation but also the presence/absence information of genes conferring short-term adaptation, particularly for species undergoing rapid OGT shifts. Our study provides a framework for improving phenotype prediction models by integrating long- and short-term evolutionary factors, which may also apply to other microbial physiological phenotypes.