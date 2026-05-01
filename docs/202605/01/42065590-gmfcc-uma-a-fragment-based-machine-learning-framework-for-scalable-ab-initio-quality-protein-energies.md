---
title: "GMFCC-UMA: A Fragment-Based Machine Learning Framework for Scalable Ab Initio-Quality Protein Energies."
title_zh: GMFCC-UMA：一种用于可扩展从头算质量蛋白质能量计算的基于碎片的机器学习框架
authors: "Wan-Sheng Ren, Jin Xiao, Yingfeng Zhang, Tong Zhu, John Z H Zhang"
date: 2026-05-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/42065590/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于蛋白质能量计算的基础神经网络势能模型
tldr: 针对蛋白质从头算量子化学计算成本极高的问题，该研究提出了 GMFCC-UMA 框架。该方法将广义分子分馏法（GMFCC）与微调后的基础神经网络势能（UMA）相结合，通过将蛋白质能量分解为相邻和非相邻项，并利用神经网络替代昂贵的片段级量子力学计算。实验证明，该方法在保持从头算精度的同时实现了数量级的加速，为高通量蛋白质构象分析提供了高效且准确的能量评估手段。
selection_source: fresh_fetch
motivation: 传统的蛋白质碎片化量子化学计算虽然精度高，但受限于片段级 QM 计算的高昂成本，难以在大规模蛋白质体系中普及。
method: 将 GMFCC 框架与微调后的 UMA 神经网络势能集成，通过分层处理相邻残基、近距离接触对及远距离相互作用，实现对蛋白质总能量的快速分解与组装。
result: 在基准测试中，该方法得到的相对能量与量子力学参考值高度一致，在误差减少和相关性方面显著优于传统力场，并实现了十倍以上的计算加速。
conclusion: GMFCC-UMA 成功将神经网络推理引入碎片化计算体系，在兼顾计算效率与化学精度的前提下，为大规模蛋白质动力学模拟和构象筛选提供了新工具。
---

## 摘要
基于碎片的量子化学为实现蛋白质的从头算质量能量学提供了一条切实可行的途径，但其适用性往往受到碎片级量子力学 (QM) 计算高昂计算成本的限制。在此，我们介绍了 GMFCC-UMA，该方法将广义分子分馏共轭帽 (GMFCC) 框架与经过微调的基础神经网络势能面相结合，从而消除了对碎片 QM 计算的需求。在该方法中，蛋白质总能量被分解为相邻和非相邻相互作用分量。相邻项以与 MFCC II 一致的方式从 ACE-NME 封端的碎片中组装，而非相邻相互作用则进行分级处理：近距离接触对使用微调后的 UMA 模型进行评估，而更远距离的贡献则通过补充的分子力学 (MM) 处理来描述。底层的神经网络模型在一个大型的、以蛋白质为中心的碎片数据集上进行了微调，该数据集包括封端单体、相邻二聚体以及非相邻残基对及其相应的块，确保了 GMFCC 碎片方案所需的所有碎片类型的一致准确性。在基准蛋白质和构象系综中，GMFCC-UMA 产生的相对能量与基于量子的碎片参考值密切匹配，并在误差减少和相关性方面均系统性地优于传统力场。通过用神经网络推理取代碎片级 QM，GMFCC-UMA 在保持从头算保真度的同时实现了数量级的加速，从而为高通量构象分析及相关应用实现了可扩展且准确的蛋白质能量评估。

## Abstract
Fragmentation-based quantum chemistry offers a practical route to achieving ab initio quality energetics for proteins, but its applicability is often constrained by the high computational cost of fragment-level quantum mechanical (QM) calculations. Here, we introduce GMFCC-UMA, a method that integrates the generalized molecular fractionation with conjugate caps (GMFCC) framework with a fine-tuned foundation neural network potential, thereby eliminating the need for fragment QM calculations. In this approach, the total protein energy is decomposed into adjacent and nonadjacent interaction components. Adjacent terms are assembled in an MFCC II-consistent manner from ACE-NME-capped fragments, while nonadjacent interactions are treated hierarchically: near-contact pairs are evaluated using the fine-tuned UMA model, and longer-range contributions are described via a complementary molecular mechanics (MM) treatment. The underlying neural network model is fine-tuned on a large, protein-focused fragment data set that includes capped monomers, adjacent dimers, and nonadjacent residue pairs and corresponding blocks, ensuring consistent accuracy across all fragment types required by the GMFCC fragmentation scheme. Across benchmark proteins and conformational ensembles, GMFCC-UMA yields relative energies that closely match quantum-based fragmentation references and systematically outperforms conventional force fields in both error reduction and correlation. By replacing fragment-level QM with neural network inference, GMFCC-UMA achieves an order-of-magnitude acceleration while retaining ab initio fidelity, thereby enabling scalable and accurate protein energy evaluation for high-throughput conformational analysis and related applications.