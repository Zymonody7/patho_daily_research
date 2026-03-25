---
title: "NEAT-DNA: A Chemically Accurate, Sequence-Dependent Coarse-Grained Model for Large-Scale DNA Simulations."
title_zh: NEAT-DNA：一种用于大尺度 DNA 模拟的化学精确、序列依赖的粗粒化模型
authors: "Ivan Riveros, Bin Zhang"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41875330/"
tags: ["query:bioinfo"]
score: 7.0
evidence: 用于大规模DNA模拟和基因组组织的粗粒度模型
tldr: 基因组组织研究需要在大尺度上模拟DNA行为，但现有粗粒度模型常在化学准确性与计算效率间权衡，导致物理真实性不足。NEAT-DNA提出了一种结合物理能量公式与原子级模拟及实验数据统一训练的新型粗粒度模型。它在保持高效计算的同时，精准还原了DNA的序列依赖性结构与柔性，为探索染色质折叠等大规模基因组结构提供了高保真模拟工具。
selection_source: fresh_fetch
motivation: 现有的DNA粗粒度模型在处理大规模模拟时，难以兼顾计算效率与反映序列特异性的化学准确性，常导致物理构象失真。
method: 该模型通过物理原理构建能量函数，并利用原子级模拟数据与实验观测值进行统一训练，以捕捉DNA的序列依赖特性。
result: NEAT-DNA能够准确复现DNA的序列特异性结构和柔性，克服了以往模型中常见的物理扭曲问题。
conclusion: 该模型为连接分子细节与基因组尺度染色质组织提供了可靠基础，是结构基因组学预测建模的重要进展。
---

## 摘要
DNA 的物理性质在基因组组织和调控中起着核心作用，但在生物学相关尺度上模拟其行为仍然是一个主要的计算挑战。粗粒化 DNA 模型实现了更快的模拟，但它们往往牺牲了化学精确性或产生非物理构象，限制了其在研究基因组结构中的应用。一个关键难点在于构建一个既能高效进行大尺度模拟，又能忠实于 DNA 分子力学的模型。在此，我们介绍了 NEAT-DNA，这是一种新型粗粒化 DNA 模型，解决了物理真实性和参数优化方面长期存在的局限性。通过将基于物理原理的能量公式与整合了全原子模拟和实验数据的统一训练框架相结合，NEAT-DNA 在保持计算效率的同时，准确地再现了序列依赖的结构和柔性。这种方法标志着相对于以往模型的重大进步，以往模型要么缺乏序列特异性，要么引入了与实验观察不一致的扭曲。NEAT-DNA 弥补了这一差距，提供了一种高保真且易于处理的 DNA 表征，适用于探索染色质折叠。更广泛地说，它为将分子细节与基因级染色质组织相结合的大尺度模拟奠定了基础，为结构基因组学中的预测建模开辟了新途径。

## Abstract
DNA's physical properties play a central role in genome organization and regulation, but simulating its behavior across biologically relevant scales remains a major computational challenge. Coarse grained DNA models have enabled faster simulations, yet they often sacrifice chemical accuracy or produce unphysical conformations, limiting their utility for studying genome structure. A key difficulty has been constructing a model that is both efficient enough for large-scale simulations and faithful to the molecular mechanics of DNA. Here, we introduce NEAT-DNA, a new coarse-grained DNA model that resolves longstanding limitations in physical realism and parameter optimization. By combining a physically principled energy formulation with a unified training framework that integrates data from both atomistic simulations and experiments, NEAT-DNA accurately reproduces sequence-dependent structure and flexibility while remaining computationally efficient. This approach marks a significant advance over previous models, which either lacked sequence specificity or introduced distortions inconsistent with experimental observations. NEAT-DNA bridges this gap, offering a high-fidelity yet tractable representation of DNA suitable for exploring chromatin folding. More broadly, it provides a foundation for large-scale simulations that couple molecular detail with gene-level chromatin organization, opening new avenues for predictive modeling in structural genomics.