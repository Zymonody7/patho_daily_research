---
title: Compressing the collective knowledge of ESM into a single protein language model.
title_zh: 将 ESM 的集体知识压缩到单个蛋白质语言模型中。
authors: "Tuan Dinh, Seon-Kyeong Jang, Noah Zaitlen, Vasilis Ntranos"
date: 2026-03-30
pdf: "https://pubmed.ncbi.nlm.nih.gov/41912799/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于变异效应预测的蛋白质语言模型
tldr: 针对蛋白质变异效应预测（VEP）中纯序列语言模型性能受限、往往需依赖结构或同源信息的问题，该研究提出一种协同蒸馏方法。通过将多个ESM模型中最具置信度的预测结果蒸馏至单一模型中，使其在不引入额外外部数据的情况下，在多个VEP基准测试上达到SOTA水平，并能准确量化生物库数据中的临床表型严重程度，为高效变异预测提供了新思路。
selection_source: fresh_fetch
motivation: 现有的高精度变异效应预测方法往往依赖结构或同源性等额外信息，增加了计算复杂性并限制了纯序列语言模型的应用。
method: 提出一种协同蒸馏方法，通过整合同一家族中多个ESM模型的高置信度预测结果，实现模型知识的自我提升与压缩。
result: 该方法在多个变异效应预测基准测试中达到了最先进水平，并能有效量化生物库数据中临床表型的严重程度。
conclusion: 研究证明了通过合理的知识蒸馏，仅凭序列信息的蛋白质语言模型即可捕获深层的进化信号，无需额外数据即可实现高精度预测。
---

## 摘要
蛋白质语言模型 (PLMs) 近期已成为下一代变异效应预测 (VEP) 的一种极具前景的方法。目前，大多数高性能的 VEP 方法通常将 PLMs 与同源性、蛋白质结构和群体遗传学数据等额外信息相结合，以提高预测准确性。然而，与仅在原始、未比对序列上训练的纯 PLMs（如进化尺度建模 ESM）相比，这种性能提升伴随着复杂性的增加或适用性的受限。在本文中，我们挑战了“仅基于序列的 PLMs 存在内在局限性”的普遍观点，并提出了一种高效的协同蒸馏 (co-distillation) 方法，使其在无需预训练捕获的进化信号之外的任何额外信息的情况下，即可实现高精度的 VEP。我们通过蒸馏同一家族中多个模型最置信的预测结果，使单个 PLM 实现自我提升，并证明 ESM 模型的协同蒸馏足以在多个 VEP 基准测试中达到最先进的性能。我们进一步表明，这种性能的提升能够对生物样本库数据中变异效应对连续临床表型影响的严重程度进行准确量化。

## Abstract
Protein language models (PLMs) have recently emerged as a promising approach for next-generation variant-effect prediction (VEP). Most high-performing VEP methods currently utilize PLMs combined with additional information, such as homology, protein structure and population genetics data to improve prediction accuracy. This performance gain, however, comes with added complexity or limited applicability compared to pure PLMs trained only on raw, unaligned sequences, such as evolutionary scale modeling (ESM). Here we challenge the prevailing view that sequence-only PLMs are intrinsically limited and present an efficient co-distillation approach to adapt them for high-accuracy VEP without requiring additional information beyond evolutionary signals captured during pretraining. We allow individual PLMs to self-improve by distilling the most confident predictions from multiple models of the same family and demonstrate that co-distillation of ESM models suffices to achieve state-of-the-art performance across multiple VEP benchmarks. We further show that this performance increase enables accurate quantification of the severity of variant effects on continuous clinical phenotypes in biobank data.