---
title: Elucidating the regulatory role of the Shine-Dalgarno sequence in structural gene expression of the malolactic enzyme operon using a GFP/mCherry model.
title_zh: 利用 GFP/mCherry 模型阐明 Shine-Dalgarno 序列在苹果酸-乳酸酶操纵子结构基因表达中的调控作用
authors: "Zixian Liu, Mingyue Ji, Fangkun Zhao, Dandan Wang, Yue Li, Yongfeng Yi, Min Wang, Jianxin Tan"
date: 2026-05-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/42101569/"
tags: ["query:pathoai"]
score: 6.0
evidence: 酒类酒球菌mRNA二级结构和翻译效率的计算预测
tldr: 针对葡萄酒发酵中 Oenococcus oeni 菌株 mleA 和 mleP 基因翻译耦合的调控机制不明问题，研究者构建了 GFP/mCherry 双荧光报告系统，对比了天然耦合与人工非耦合结构。通过对 SD2 序列进行定点突变并结合 mRNA 二级结构能值计算，发现翻译耦合系统存在非线性的调控逻辑，即过强的 SD 序列在耦合结构中反而可能抑制下游基因表达。该研究揭示了原核生物操纵子中精确的翻译后调控层级，为合成生物学中多基因比例控制提供了预测框架。
selection_source: fresh_fetch
motivation: 旨在探究葡萄酒苹果酸-乳酸发酵过程中，关键代谢基因 mleA 和 mleP 之间翻译耦合的具体后转录调控机制。
method: 利用 GFP/mCherry 报告系统模拟基因耦合与非耦合结构，结合 SD 序列突变、16S rRNA 杂交能计算及 mRNA 二级结构预测进行定量分析。
result: 实验发现在非耦合系统中 SD 序列增强会提升表达，但在翻译耦合系统中，最强的 SD 序列（GGAGG）反而显著抑制了下游基因表达，呈现出非线性的调控逻辑。
conclusion: 翻译耦合通过上游翻译活动与局部 mRNA 结构的协同作用实现蛋白质比例的精确调控，为优化发酵菌株及设计多基因合成系统提供了理论依据。
---

## 摘要
葡萄酒中的苹果酸-乳酸发酵 (MLF) 依赖于酒酒球菌 (Oenococcus oeni)，其中 mleA 和 mleP 基因在翻译水平上是偶联的。为了探索其中涉及的转录后调控，我们构建了平行的 GFP/mCherry 报告系统，分别模拟天然的重叠（翻译偶联）结构和人工构建的非重叠（非偶联）结构。通过定点 SD2 突变，并结合 16S rRNA 杂交能 (ΔG) 和 mRNA 二级结构最小自由能 (MFE) 的计算预测，我们定量分析了基因间序列特征对翻译效率的影响。在大肠杆菌 (Escherichia coli) 的翻译偶联系统中，不同变体的表达比例 (GFP/MCH) 在 3.58 到 8.58 之间变化，而在非偶联系统中，该比例范围为 1.54 到 3.09。在非偶联构建体中，下游基因的表达在独立 SD2 的控制下有所增加，这与其保守功能一致。然而，在偶联系统中，最强的 SD2 (GGAGG) 显著抑制了其表达，揭示了一种非线性的、特定于结构的调控逻辑。不同变体也在乳酸乳球菌 (Lactococcus lactis) 的翻译偶联系统中进行了表达，各变体上下游基因的表达比例模式与在大肠杆菌中观察到的结果一致。这表明 SD2 在乳酸乳球菌和大肠杆菌中对偶联基因表达比例具有相同的调控作用。我们的研究结果表明，翻译偶联通过上游翻译和局部 mRNA 结构的综合效应，建立了精确的蛋白质表达调控。这项工作阐明了原核生物操纵子中一个关键的转录后调节层，为优化 MLF 的酒酒球菌理性工程以及合成生物学中比例控制的多基因系统设计提供了一个预测框架。

## Abstract
Malolactic fermentation (MLF) in wine relies on Oenococcus oeni, in which the mleA and mleP genes are translationally coupled. To explore the post-transcriptional regulation involved, we constructed parallel GFP/mCherry reporter systems that mimic both the native overlapping (translationally coupled) structure and an engineered non-overlapping (non-coupled) structure. Through site-directed SD2 mutagenesis coupled with computational prediction of 16 S rRNA hybridization energy (ΔG) and minimum free energy (MFE) of mRNA secondary structure, we quantified the effect of intergenic sequence features on translation efficiency. In the translational coupling system of Escherichia coli, expression ratios (GFP/MCH) varied from 3.58 to 8.58 across variants, while in the non-coupled system, they ranged from 1.54 to 3.09. In non-coupled constructs, downstream gene expression increased under independent SD2 control, consistent with its conserved function. However, in the coupling system, the strongest SD2 (GGAGG) markedly suppressed it, revealing a nonlinear, architecture-specific regulatory logic. The different variants were also expressed in the translational coupling system of Lactococcus lactis, and the expression ratio patterns of the upstream and downstream genes across the variants were consistent with those observed in E. coli. This indicated that SD2 had the same regulatory effect on coupling gene expression ratios in both L. lactis and E. coli. Our findings demonstrate that translational coupling establishes precise protein expression regulation through the integrated effects of upstream translation and local mRNA structure. This work elucidates a key post-transcriptional tuning layer in prokaryotic operons, providing a predictive framework for both the rational engineering of O. oeni to optimize MLF and the design of proportionally controlled multi-gene systems in synthetic biology.