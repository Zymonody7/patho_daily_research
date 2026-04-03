---
title: Fitting coarse-grained models to macroscopic experimental data via automatic differentiation.
title_zh: 通过自动微分将粗粒化模型拟合至宏观实验数据
authors: "Ryan K Krueger, Megan C Engel, Ryan Hausen, Michael P Brenner"
date: 2026-04-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/41926537/"
tags: ["query:bioinfo"]
score: 6.0
evidence: 通过自动微分拟合粗粒度DNA力场模型
tldr: 针对分子模拟中粗粒化模型参数拟合过程零散且难以复现的问题，该研究提出了一套基于自动微分（AD）的系统化框架，用于将模型参数直接拟合至宏观实验数据。通过计算低方差梯度估计，该方法实现了对DNA、RNA及蛋白质-DNA杂合模型在结构、力学和热力学性质上的跨尺度优化。该框架不仅提升了力场开发的透明度与效率，还通过多任务学习解决了多约束下的参数冲突，为构建高精度分子模型提供了通用工具。
selection_source: fresh_fetch
motivation: 传统的分子力场参数拟合依赖人工经验且过程碎片化，导致模型难以复现且难以同时满足多种宏观物理性质。
method: 利用自动微分技术计算模拟性质对参数的梯度，并结合多任务学习中的无冲突梯度算法，在增强采样和外力驱动等多种模拟场景下进行参数优化。
result: 在DNA、RNA及核酸-蛋白质复合系统上验证了该方法的有效性，成功拟合了跨越微秒至毫秒尺度的多种物理特性，并揭示了参数与物理行为间的敏感度关系。
conclusion: 该研究为分子力场的自动化、透明化开发奠定了基础，通过统一的梯度优化框架加速了生物大分子建模的演进。
---

## 摘要
开发用于分子模拟的物理模型需要将许多未知参数拟合到多样的实验数据集。传统上，这一过程是零散且难以复现的，导致了模型格局的碎片化。在本文中，我们利用近期开发的通过自动微分计算低方差梯度估计的方法，建立了一个将粗粒化分子模型拟合至宏观实验数据的系统框架。以一个经过广泛验证的 DNA 力场为例，我们开发了在多种模拟技术（包括增强采样和外力作用）下优化结构、力学和热力学性质的方法，跨越了微秒和毫秒的时间尺度。我们强调了自动微分如何实现高效的敏感性分析，从而深入了解控制物理行为的模型参数。随后，我们通过优化包括 RNA 和 DNA-蛋白质混合模型在内的多种生物分子系统，展示了这些技术的广泛适用性。我们展示了如何将多任务学习中的无冲突梯度方法进行改进，以便在不牺牲准确性的情况下同时施加多个约束。该方法为透明、可复现、社区驱动的力场开发奠定了基础，加速了分子建模领域的进展。

## Abstract
Developing physics-based models for molecular simulation requires fitting many unknown parameters to diverse experimental datasets. Traditionally, this process is piecemeal and difficult to reproduce, leading to a fragmented landscape of models. Here, we establish a systematic framework for fitting coarse-grained molecular models to macroscopic experimental data by leveraging recently developed methods for computing low-variance gradient estimates with automatic differentiation. Using a widely validated DNA force field as an exemplar, we develop methods for optimizing structural, mechanical, and thermodynamic properties across a range of simulation techniques, including enhanced sampling and external forcing, spanning micro- and millisecond timescales. We highlight how automatic differentiation enables efficient sensitivity analyses that yield insights into the model parameters governing physical behaviors. We then demonstrate the broad applicability of these techniques by optimizing diverse biomolecular systems, including RNA and DNA-protein hybrid models. We show how conflict-free gradient methods from multitask learning can be adapted to impose multiple constraints simultaneously without compromising accuracy. This approach provides a foundation for transparent, reproducible, community-driven force field development, accelerating progress in molecular modeling.