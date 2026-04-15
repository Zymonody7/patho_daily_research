---
title: A multi-modal diffusion model with dual-cross-attention for multi-omics data generation and translation.
title_zh: 一种具有双重交叉注意力的多模态扩散模型，用于多组学数据的生成与翻译
authors: "Erpai Luo, Lei Wei, Minsheng Hao, Xuegong Zhang, Qiao Liu"
date: 2026-04-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41980989/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于多组学数据整合的多模态扩散模型
tldr: 针对单细胞多组学实验成本高、规模受限的问题，本文开发了 scDiffusion-X 潜空间扩散模型。该模型通过创新的双交叉注意力（DCA）机制捕捉不同分子模态间的复杂关联，实现了高质量的多组学数据生成与跨模态翻译。实验证明其在保持细胞异质性的同时，能准确预测缺失模态并推断细胞类型特异性的基因调控网络，为生物医学研究提供了强有力的计算工具。
selection_source: fresh_fetch
motivation: 单细胞多组学实验在规模和成本上存在局限，亟需能整合多样化模态并生成高保真模拟数据的计算方法。
method: 提出 scDiffusion-X 潜空间扩散模型，利用双交叉注意力（DCA）模块自适应地捕捉不同组学模态间的隐藏关联。
result: 该模型在生成真实多组学数据、跨模态翻译及不确定性量化方面表现优异，并能通过梯度解释框架推断基因调控网络。
conclusion: scDiffusion-X 将生成式 AI 与生物可解释性结合，为解析细胞调控机制和加速多组学研究提供了可扩展的解决方案。
---

## 摘要
单细胞多组学技术为破译复杂的细胞机制提供了前所未有的机遇。为了克服实验在规模、成本和覆盖范围方面的局限性，强大的计算方法对于整合多种数据模态并生成高保真度的计算机模拟（in-silico）数据至关重要。在本文中，我们提出了 scDiffusion-X，这是一种用于多组学数据整合、生成和翻译的潜在扩散模型。其核心创新是一个双重交叉注意力（DCA）模块，该模块能够自适应地捕捉分子模态之间复杂且隐藏的关系，提供了一种比现有整合策略更灵活且更具可解释性的方法。广泛的基准测试实验表明，scDiffusion-X 在生成逼真的多组学数据方面表现出色，在保持细胞异质性和全局数据结构的同时具有极佳的可扩展性。除了模拟之外，scDiffusion-X 还独特地实现了准确的模态翻译，能够从一种分子模态预测另一种模态，并具有鲁棒的不确定性量化。此外，我们设计了一个基于梯度的解释框架，将 DCA 模块转化为一种发现工具，从而能够推断出全面的细胞类型特异性异质基因调控网络（GRNs）。通过将最先进的生成建模与生物可解释性相结合，scDiffusion-X 成为剖析调控关系、预测扰动响应并加速单细胞多组学研究发现的强大工具。

## Abstract
Single-cell multi-omics technologies offer unprecedented opportunities to decipher complex cellular mechanisms. To overcome experimental limitations in scale, cost, and coverage, powerful computational methods are essential for integrating diverse data modalities and generating high-fidelity in-silico data. In this paper, we present scDiffusion-X, a latent diffusion model for multi-omics data integration, generation, and translation. The core innovation is a Dual-Cross-Attention (DCA) module that adaptively captures intricate, hidden relationships between molecular modalities, offering a more flexible and interpretable approach than existing integration strategies. Extensive benchmarking experiments demonstrate that scDiffusion-X excels at generating realistic multi-omics data, preserving cellular heterogeneity and global data structures with excellent scalability. Beyond simulation, scDiffusion-X uniquely enables accurate modality translation, predicting one molecular modality from another with robust uncertainty quantification. Furthermore, we designed a gradient-based interpretation framework to transform the DCA module into a discovery tool, enabling inference of comprehensive cell-type-specific heterogeneous gene regulatory networks (GRNs). By integrating state-of-the-art generative modeling with biological interpretability, scDiffusion-X serves as a powerful tool for dissecting regulatory relationships, predicting perturbation responses, and accelerating discovery in single-cell multi-omics research.