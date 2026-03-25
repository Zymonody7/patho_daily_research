---
title: "Unlocking Enzyme Discovery: A High-Resolution Gene Cluster Database Powered by Phylogenetic Insights and Machine Learning."
title_zh: 开启酶发现：由系统发育洞察和机器学习驱动的高分辨率基因簇数据库
authors: "Sidun Zhang, Junlong He, Xuguo Duan, Zimin Liu, Zhouge Lan, Qiong Wang, Jianyang Wang, Wenrui Liu, Qixiao Zhai, Pablo Cruz-Morales, Junjun Wu"
date: 2026-03-25
pdf: "https://pubmed.ncbi.nlm.nih.gov/41837859/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于活性预测的进化规模蛋白质语言模型
tldr: 针对海量基因组数据标注不足导致酶发现困难的问题，该研究构建了一个整合跨界系统发育数据库、多位点挖掘、蛋白质语言模型（pLM）活性预测及残基-原子接触重评分的流水线。在r-BOX代谢途径应用中，该方法显著提升了活性预测精度和筛选效率，实验验证使FadB产量提升至10.2 g/L，为高价值酶的规模化挖掘提供了高效工具。
selection_source: fresh_fetch
motivation: 解决高通量测序产生的海量基因组数据中功能标注缺失、难以高效挖掘稀有高价值酶的问题。
method: 结合跨界系统发育分析、蛋白质语言模型预测活性以及多层级残基-原子接触重评分，构建了一套从基因挖掘到功能验证的集成化流水线。
result: 活性预测模型在r-BOX途径中表现优于SOTA，且通过接触评分将早期富集率提升了16倍，实验验证显著提高了目标产物的发酵产量。
conclusion: 该研究证明了结合进化洞察与机器学习的策略能有效降低酶发现的假阳性率，是加速生物合成途径优化的通用框架。
---

## 摘要
高通量测序产生了庞大的基因组库，但这些库仍处于注释不足的状态，阻碍了酶的发现。我们提出了一套集成流程，包括：(i) 构建高分辨率、跨界的系统发育数据库；(ii) 通过多位点系统发育挖掘候选基因；(iii) 使用进化规模的蛋白质语言模型预测活性；以及 (iv) 通过多级残基-原子接触重评分剔除假阳性。当应用于 r-BOX 途径时，该方法发现了大量此前未记录的 FadB、BktB、Ter 和 YdiI 同源物。我们的活性模型实现了 R2 = 0.68，与之前的最先进技术 (SOTA) UniKP 相比，在高价值靶点上的均方根误差 (RMSE) 降低了 11%。接触评分将早期富集率 (EF1%) 提高了 16 倍。针对 FadB 的实验验证将产量从 0.65 g/L（摇瓶）提高到 1.7 g/L，在发酵过程中达到了 10.2 g/L。总之，这些结果建立了一个稳健且通用的框架，用于大规模发现稀缺、高价值的酶并优先筛选功能变体。

## Abstract
High-throughput sequencing has generated vast genomic repositories that remain under-annotated, hampering enzyme discovery. We present an integrated pipeline that (i) builds a high-resolution, cross-kingdom phylogenetic database, (ii) mines candidates via multilocus phylogeny, (iii) predicts activities using an evolutionary-scale protein language model, and (iv) removes false positives through multilevel residue-atom contact rescoring. When applied to the r-BOX pathway, this approach uncovered numerous previously undocumented FadB, BktB, Ter, and YdiI homologues. Our activity model achieved R2 = 0.68 and reduced the RMSE on high-value targets by 11% compared to the prior SOTA (UniKP). Contact scoring improved early enrichment (EF1%) by 16-fold. Experimental validation targeting FadB increased titers from 0.65 g/L (shake flasks) to 1.7 g/L, reaching 10.2 g/L in a fermentation process. Together, these results establish a robust, generalizable framework for discovering scarce, high-value enzymes and prioritizing functional variants at scale.