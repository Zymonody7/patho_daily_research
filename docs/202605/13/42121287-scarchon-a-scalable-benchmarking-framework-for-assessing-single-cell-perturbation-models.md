---
title: "scArchon: a scalable benchmarking framework for assessing single-cell perturbation models."
title_zh: scArchon：一个用于评估单细胞扰动模型的可扩展基准测试框架。
authors: "Jean Radig, Robin Droit, Daria Doncevic, Albert Li, Duc Thien Bui, Luis Herfurth, Thaddeus Kühn, Carl Herrmann"
date: 2026-05-12
pdf: "https://pubmed.ncbi.nlm.nih.gov/42121287/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 评估单细胞扰动模型的基准测试框架
tldr: 针对单细胞扰动反应预测工具缺乏系统评估的问题，本研究开发了基于 Snakemake 的模块化评测框架 scArchon。通过在 6 个数据集上对比 scGen、CPA 等 9 种模型，发现各工具表现差异巨大，部分模型甚至弱于线性基准，且量化高分未必能反映真实的生物学信号。该框架为该领域的标准化评估和算法优化提供了重要支撑。
selection_source: fresh_fetch
motivation: 现有的单细胞扰动反应预测工具层出不穷，但缺乏一个统一、公正且可扩展的标准来评估它们在不同数据集和指标下的真实性能。
method: 开发了名为 scArchon 的模块化评测平台，利用 Snakemake 工作流整合了 9 种主流深度学习模型，并结合统计学与生物学指标进行综合评价。
result: 实验发现 trVAE 和 scGen 等模型表现较稳健，但部分复杂模型在特定任务下甚至逊于线性基准，且发现高量化得分模型未必能准确捕捉关键的基因级生物扰动信号。
conclusion: scArchon 为单细胞扰动预测领域建立了标准化的基准测试体系，有助于研究者识别现有工具的局限性并推动更精准算法的开发。
---

## 摘要
背景：准确预测细胞对扰动（如药物治疗）的反应仍然是单细胞转录组学中的一个关键挑战。虽然已经开发了许多深度学习工具来完成这一任务，但它们在不同数据集和性能指标上的系统性基准测试仍然有限。结果：在此，我们介绍了 scArchon，这是一个基于 Snakemake 构建的可重现、模块化的基准测试平台。它旨在以公正且可扩展的方式评估扰动反应预测工具。利用六个具有代表性的单细胞 RNA-seq 数据集，我们将 scGen、CPA、trVAE、scPRAM、scVIDR、scDisInFact、SCREEN、scPreGAN 和 CellOT 等领先方法与基准线进行了比较。我们使用统计和生物学指标的综合评估模型性能。我们的分析揭示了性能的异质性。虽然 trVAE、scGen、scPRAM 和 scVIDR 等方法在多个数据集中取得了稳健的结果，但其他工具的表现偶尔甚至不如线性或对照基准线。值得注意的是，具有良好定量评分的模型可能无法保留关键的生物扰动特征，这强调了进行基因层面评估的必要性。结论：scArchon 为扰动预测工具的大规模、标准化基准测试提供了一个统一且可扩展的基础，促进了方法论的透明度，并加速了这一快速发展领域的发展。我们鼓励采用 scArchon 并共享容器化工具，以推动单细胞扰动建模的进展。

## Abstract
BACKGROUND: The accurate prediction of cellular responses to perturbations, such as drug treatments, remains a pivotal challenge in single-cell transcriptomics. While numerous deep learning tools have been developed for this task, their systematic benchmarking across diverse datasets and performance metrics has been limited. RESULTS: Here, we present scArchon, a reproducible, modular benchmarking platform built on Snakemake. It is designed to evaluate perturbation response prediction tools in an unbiased and extensible manner. Employing six representative single-cell RNA-seq datasets, we compare leading methods such as scGen, CPA, trVAE, scPRAM, scVIDR, scDisInFact, SCREEN, scPreGAN, and CellOT against baselines. We assess model performance using a composite of statistical and biological metrics. Our analysis reveals heterogeneous performance. While methods like trVAE, scGen, scPRAM, and scVIDR achieve robust results across multiple datasets, other tools occasionally underperform even compared to linear or control baselines. Notably, models with favorable quantitative scores may fail to retain key biological perturbation signatures, underscoring the need for gene-level evaluation. CONCLUSIONS: scArchon provides a unified, extensible foundation for large-scale, standardized benchmarking of perturbation prediction tools, facilitating methodological transparency and accelerating development in this rapidly evolving field. We encourage adoption of scArchon and sharing of containerized tools to drive progress in single-cell perturbation modeling.