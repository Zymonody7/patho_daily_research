---
title: "Reconstructing ancient genomes from gene counts: A robust likelihood framework with sampling bias correction."
title_zh: 从基因计数重建古代基因组：一种具有抽样偏差校正的稳健似然框架
authors: Miklós Csűrös
date: 2026-05-12
pdf: "https://pubmed.ncbi.nlm.nih.gov/42101992/"
tags: ["query:pathoai"]
score: 7.0
evidence: 用于祖先基因组重建的系统发育增益-缺失-重复模型
tldr: 针对古基因组重建中基因树拓扑不确定性导致的计算难题，本研究提出了一种基于基因拷贝数演化的GLD似然框架。该方法利用物种树上的出生-死亡过程模拟基因的增益、丢失和重复，并引入采样偏差修正。在269个古菌基因组的重建实验中，GLD比传统序列比对方法更准确地识别了基因演化模式，揭示了微生物基因组在精简与扩张之间的动态平衡机制。
selection_source: fresh_fetch
motivation: 传统的基于基因序列比对的古基因组重建方法在处理大规模数据时，容易受到基因树拓扑不确定性和统计伪影的干扰。
method: 提出一种基于基因计数（Gene Counts）的GLD模型，通过物种树上的出生-死亡过程计算似然值，并结合采样偏差修正进行祖先状态推断。
result: 在古菌数据集上的应用表明，该框架能有效避免传统方法中因序列信号衰减导致的水平基因转移误判，更真实地还原了基因组演化历程。
conclusion: 该框架为跨界规模的基因内容演化研究提供了稳健的统计基础，揭示了微生物基因组通过模块化丢失和爆发式增益维持适应性的演化规律。
---

## 摘要
推断古代基因组的组成是进化生物学中的一个基本挑战。尽管存在跨越整个生命树的海量基因组数据集，但目前的祖先重建方法在处理大规模基因序列进化的固有歧义方面仍面临困难。在此，我们提出了一种数值稳健的计算框架，克服了基因树的拓扑不确定性。我们的系统发育获得-丢失-重复（GLD）模型并非追踪每一个单一事件，而是基于沿物种树的基因拷贝生灭过程。我们证明，在可调节的最小基因家族大小观测偏差下，可以高效地计算似然及其梯度。该框架促进了无约束的数值似然最大化和通过后验概率进行的祖先推断。我们将该框架应用于包含 269 个基因组的古菌数据集的界级重建，并证明 GLD 能以高准确度恢复祖先状态。我们将 GLD 推断与基于基因序列的系统发育调和（ALE 方法）进行了比较，结果表明 ALE 推断出的难以置信的频繁水平基因转移通常是大规模比对中系统发育信号崩溃的统计伪影。相比之下，GLD 推断揭示了两层对立的进化机制如何塑造微生物基因组：基因组精简化与瞬时基因普遍涌入之间的高频张力，以及由周期性模块化丢失和间歇性大规模获得构成的适应性制衡。GLD 框架为假设整个界多样性中的基因含量进化提供了统计学上可靠的基础。

## Abstract
Deducing the makeup of ancient genomes is a fundamental challenge in evolutionary biology. While vast genomic datasets exist that span the entire tree of life, current methods for ancestral reconstructions struggle to resolve the inherent ambiguities of gene-sequence evolution at scale. Here, we present a numerically robust computational framework that overcomes the topological uncertainty of gene trees. Instead of tracking every single event, our phylogenetic gain-loss-duplication (GLD) model is based on birth-death processes over gene copies along the species tree. We show that the likelihood and its gradient can be computed efficiently under an adjustable observation bias of minimum gene family size. The framework facilitates unconstrained numerical likelihood maximization and ancestral inference by posterior probabilities. We apply this framework to kingdom-level reconstructions over a 269-genome archaeal dataset and demonstrate that GLD recovers ancestral states with high accuracy. We compare GLD inference with phylogenetic reconciliation from gene sequences (ALE method) and show that implausibly frequent horizontal gene transfer inferred by ALE are often statistical artifacts of collapsing phylogenetic signals in large alignments. In contrast, GLD inferences reveal how two layers of opposing evolutionary mechanics shape microbial genomes: a high-frequency tension between genome streamlining and the pervasive influx of transient genes, complemented by an adaptive counterbalance of recurrent, modular losses, and punctuated massive gains. The GLD framework provides a statistically sound foundation for hypothesizing about gene content evolution across the diversity of entire kingdoms.