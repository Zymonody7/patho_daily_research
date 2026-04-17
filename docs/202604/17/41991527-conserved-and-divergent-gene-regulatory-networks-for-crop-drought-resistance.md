---
title: Conserved and divergent gene regulatory networks for crop drought resistance.
title_zh: 作物抗旱性的保守与分化基因调控网络
authors: "Xianzhi Deng, Liangsheng Shi, Yu Wang, Han Qiao, Xin Wang, Jiateng Ma, Yufan Zhang, Yuanyuan Zha, Xiaolong Hu"
date: 2026-04-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41991527/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 基于图深度学习的基因调控网络推断
tldr: 针对作物抗旱机制在跨物种间保守性与差异性不明的问题，该研究利用图深度学习框架整合了5000多份转录组数据，构建了涵盖13万个基因的跨组学基因调控网络（GRN）。研究发现了TCP-PP2C等保守调控模式，并揭示了C3与C4作物在抗旱策略上的网络拓扑差异：C3作物依赖集中且剧烈重构的网络实现避旱，而C4作物则通过分布式且稳定的网络实现耐旱。这为理解作物进化适应性提供了新视角。
selection_source: fresh_fetch
motivation: 旨在揭示不同作物在应对干旱胁迫时，其基因调控网络在进化过程中的保守规律与物种特异性差异。
method: 采用图深度学习框架整合海量多组学数据，构建了覆盖禾本科、豆科等多种作物的超大规模基因调控网络。
result: 识别出跨物种保守的ABA与氧化还原调控路径，并发现C3与C4作物分别采用“集中重构型”和“分布式稳定型”的网络拓扑结构。
conclusion: 证明了作物抗旱性受基因网络拓扑结构的系统性约束，而非仅由少数关键基因决定，揭示了自然选择对网络架构的塑造作用。
---

## 摘要
理解作物抗旱机制对于增强应对日益严峻的气候变化的韧性至关重要。然而，跨物种遗传基础下保守与分化的抗旱机制仍不清楚。在本研究中，我们利用一种创新的基于图的深度学习框架，整合了超过5000个大体转录组（bulk RNA-seq）数据集，构建了主要禾本科（Poaceae）作物在转录、蛋白质组和代谢层面的大规模抗旱响应基因调控网络（GRNs），绘制了13万个基因之间的330万次相互作用。此外，还纳入了豆科（Fabaceae）和茄科（Solanaceae）的其他作物进行进一步验证。大规模数据和先进算法为抗旱GRNs提供了严谨的全基因组证据和见解。我们发现了与脱落酸和氧化还原调节相关的TCP-PP2C和ERF-2OGD的稳健保守相互作用模式。通过大规模比较网络分析，识别出了分化的机制，包括水稻/小麦谱系中的SPL-PELP和玉米/高粱谱系中的ERF-Psb28。我们提出了一个假设，即作物的抗旱性受GRNs拓扑结构的系统发育约束，而不仅仅取决于少数关键基因。具有遗传性生长相关避旱和逃旱策略的代表性C3作物的抗旱性由具有剧烈重编程特征的集中式网络控制，而具有遗传决定型耐旱策略的代表性C4作物的抗旱性则由分布式且稳定的网络控制。我们的研究结果为作物GRNs的演化动力学提供了深刻见解，揭示了基因网络架构是如何通过自然选择塑造，从而驱动遗传适应以应对气候挑战的。

## Abstract
Understanding crop drought resistance mechanisms is critical for enhancing resilience to intensifying climate change. However, the conserved and divergent drought resistance mechanisms under the genetic basis across species remain unclear. Here, using an innovative graph-based deep learning framework, we construct drought-responsive large-scale gene regulatory networks (GRNs) across transcriptional, proteomic, and metabolic layers in major Poaceae crops integrating over 5000 bulk RNA-seq datasets to map 3.3 million interactions among 130,000 genes. Other crops in Fabaceae and Solanaceae are also included for further validation. Large-scale data and advanced algorithms provide rigorous, genome-wide evidence and insights into drought GRNs. We find robustly conserved interaction patterns of TCP-PP2C and ERF-2OGD linked to abscisic acid and redox regulation. Divergent mechanisms are identified, including SPL-PELP in rice/wheat lineage and ERF-Psb28 in maize/sorghum lineage from large-scale comparative network analysis. We propose the hypothesis that drought resistance in crops is phylogenetically constrained by the topological structure of GRNs, rather than just a few key genes. Drought resistance of representative C3 crops, with inherited growth-related drought escape and avoidance strategies, is governed by a concentrated network with drastic reprogramming, while drought resistance of representative C4 crops, with genetically determined drought tolerance strategy, is governed by a distributed and stable network. Our findings offer deep insights into the evolutionary dynamics of GRNs in crops, revealing how gene network architecture has been shaped by natural selection to drive genetic adaptation in response to climate challenges.