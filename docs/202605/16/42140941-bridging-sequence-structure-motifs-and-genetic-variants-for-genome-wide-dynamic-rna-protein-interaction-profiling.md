---
title: Bridging sequence-structure motifs and genetic variants for genome-wide dynamic RNA-protein interaction profiling.
title_zh: 连接序列-结构基序与遗传变异，用于全基因组动态 RNA-蛋白质相互作用图谱分析
authors: "Yubo Wang, Haoran Zhu, Gaoyang Hao, Yanchi Su, Zhuohan Yu, Yuning Yang, Fuzhou Wang, Xingjian Chen, Ka-Chun Wong, Xiangtao Li"
date: 2026-05-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/42140941/"
tags: ["query:bioinfo"]
score: 8.0
evidence: RNA 序列-结构基序与遗传变异的端到端统一模型
tldr: 针对RNA结合蛋白（RBP）识别受二级结构影响且在不同细胞系间具有动态性的挑战，本研究开发了BRIDGE模型。该模型通过整合RNA序列与结构特征，实现了跨细胞系的动态RBP结合预测，其性能优于现有SOTA方法且具备零样本迁移能力。BRIDGE不仅识别出数千个调控基序，还揭示了非编码遗传变异如何通过破坏RBP结合导致致病效应，为基因组功能分析提供了有力工具。
selection_source: fresh_fetch
motivation: 现有的计算模型无法有效解释RNA序列-结构基序在不同细胞系间的动态变化，以及遗传变异对这些相互作用的潜在功能影响。
method: 开发了名为BRIDGE的端到端深度学习框架，通过统一建模RNA序列与二级结构，实现对全基因组范围内动态RBP结合谱的预测与解释。
result: 该模型在静态预测任务中超越了现有最先进方法，并能无需重训练地迁移至新细胞环境，成功识别出3571个与剪接调控相关的整合基序。
conclusion: BRIDGE通过全基因组模拟扰动分析，为理解剪接区域及致病变异如何干扰RBP结合提供了可解释的视角，增强了对非编码区遗传变异的解读能力。
---

## 摘要
RNA 结合蛋白 (RBP) 通常识别复杂的 RNA 二级结构基序，且这些相互作用在不同细胞系之间可能存在差异。然而，目前的计算模型尚无法解释 RNA 序列-结构基序在多个细胞系中的动态行为，并将这些动态变化与遗传变异的功能影响联系起来。在此，我们提出了 BRIDGE，这是一个端到端的统一模型，它将序列-结构基序与非编码遗传变异的功能效应联系起来，从而实现了动态 RNA-蛋白质相互作用图谱的全基因组分析。我们的评估表明，BRIDGE 在静态单细胞系预测方面优于现有的最先进方法。在无需任何重新训练的情况下，该框架可迁移至未见的细胞环境，从而揭示了 RNA 识别中一种保守且具有适应性的语法。注意力引导的解释识别出 3,571 个综合基序，包括与剪接调节相关的基序。此外，全基因组计算机模拟扰动为不同变异类别（包括剪接区域和致病等位基因）的 RBP 结合破坏提供了可解释的视角。

## Abstract
RNA-binding proteins (RBPs) often recognize complex RNA secondary structure motifs, and these interactions can vary between cell lines. However, no current computational model can explain the dynamic behavior of RNA sequence-structure motifs across multiple cell lines and link these dynamics to the functional impact of genetic variation. Here we show BRIDGE, an end-to-end unified model that bridges sequence-structure motifs with the functional effects of noncoding genetic variants, thereby enabling genome-wide analysis of dynamic RNA-protein interaction profiles. Our evaluations demonstrate that BRIDGE outperforms existing state-of-the-art methods in static single cell line predictions. Without any retraining, the framework transfers to unseen cellular contexts, thereby revealing a conserved yet adaptable grammar of RNA recognition. Attention-guided interpretation identified 3,571 integrative motifs, including motifs associated with splicing regulation. Moreover, genome-wide in-silico perturbation provides an interpretable view of RBP-binding disruption across variant classes, including splice-region and pathogenic alleles.