---
title: "Unlocking Enzyme Discovery: A High-Resolution Gene Cluster Database Powered by Phylogenetic Insights and Machine Learning."
title_zh: 开启酶发现：由系统发育见解和机器学习驱动的高分辨率基因簇数据库
authors: "Zhang S, He J, Duan X, Liu Z, Lan Z, Wang Q, Wang J, Liu W, Zhai Q, Cruz-Morales P, Wu J., Sidun Zhang, Junlong He, Xuguo Duan, Zimin Liu, Zhouge Lan, Qiong Wang, Jianyang Wang, Wenrui Liu, Qixiao Zhai, Pablo Cruz-Morales, Junjun Wu"
date: 2026-03-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41837859/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于活性预测的进化尺度蛋白质语言模型
tldr: 针对海量基因组数据中酶功能标注不足、发现效率低的问题，该研究开发了一套整合跨界系统发育数据库、蛋白质语言模型预测及残基-原子接触重评分的自动化发现框架。在r-BOX代谢途径的应用中，该方法显著提升了酶活性预测精度，成功挖掘出多种高产酶变体，并将关键酶FadB的产量从0.65 g/L提升至10.2 g/L，为高价值酶的规模化发现与功能优化提供了高效的通用工具。
selection_source: fresh_fetch
motivation: 旨在解决海量基因组数据中酶功能标注严重滞后，导致难以从庞大序列库中精准识别高价值酶的问题。
method: 建立了一套结合多位点系统发育挖掘、蛋白质语言模型活性预测以及残基-原子接触重评分的集成化发现管线。
result: 该方法在活性预测精度上超越了现有SOTA模型，将筛选效率提升16倍，并成功在实验中实现了目标产物产量的大幅增长。
conclusion: 研究证明了通过融合进化信息与深度学习模型，可以高效、精准地从全球基因组资源中挖掘并验证稀缺的高价值酶。
---

## 摘要
高通量测序产生了庞大的基因组库，但这些库仍处于注释不足的状态，阻碍了酶的发现。我们提出了一套集成流程，包括：(i) 构建高分辨率、跨界的系统发育数据库；(ii) 通过多位点系统发育挖掘候选基因；(iii) 使用进化规模的蛋白质语言模型预测活性；以及 (iv) 通过多级残基-原子接触重评分剔除假阳性。当应用于 r-BOX 途径时，该方法发现了大量此前未被记录的 FadB、BktB、Ter 和 YdiI 同源物。我们的活性模型实现了 R^2 = 0.68，且与之前的最先进技术 (SOTA) UniKP 相比，在高价值靶点上的均方根误差 (RMSE) 降低了 11%。接触评分将早期富集率 (EF1%) 提高了 16 倍。针对 FadB 的实验验证将产量从 0.65 g/L（摇瓶）提高到 1.7 g/L，并在发酵过程中达到了 10.2 g/L。总之，这些结果建立了一个稳健且通用的框架，用于大规模发现稀缺、高价值的酶并优先筛选功能变体。

## Abstract
High-throughput sequencing has generated vast genomic repositories that remain under-annotated, hampering enzyme discovery. We present an integrated pipeline that (i) builds a high-resolution, cross-kingdom phylogenetic database, (ii) mines candidates via multilocus phylogeny, (iii) predicts activities using an evolutionary-scale protein language model, and (iv) removes false positives through multilevel residue-atom contact rescoring. When applied to the r-BOX pathway, this approach uncovered numerous previously undocumented FadB, BktB, Ter, and YdiI homologues. Our activity model achieved <i>R</i><sup>2</sup> = 0.68 and reduced the RMSE on high-value targets by 11% compared to the prior SOTA (UniKP). Contact scoring improved early enrichment (EF1%) by 16-fold. Experimental validation targeting FadB increased titers from 0.65 g/L (shake flasks) to 1.7 g/L, reaching 10.2 g/L in a fermentation process. Together, these results establish a robust, generalizable framework for discovering scarce, high-value enzymes and prioritizing functional variants at scale.