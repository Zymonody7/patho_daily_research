---
title: "Population-scale long-read DNA sequencing: peering under the hood of the new evolutionary genomics."
title_zh: 群体规模长读长 DNA 测序：透视新进化基因组学的底层机制
authors: "Scott V Edwards, Heng Li"
date: 2026-04-22
pdf: "https://pubmed.ncbi.nlm.nih.gov/42014088/"
tags: ["query:seqai"]
score: 7.0
evidence: 讨论了用于长读长测序、基因组组装和变异检测的计算工具
tldr: 针对传统短读长测序难以捕捉复杂结构变异的问题，本文综述了群体规模长读长测序（PLRS）与泛基因组技术在进化基因组学中的应用。通过分析鸟类等脊椎动物的二倍体组装、重复序列注释及拷贝数变异，文章展示了长读长技术如何利用泛基因组图谱精准量化变异。这一范式转变揭示了基因组中被长期忽视的复杂性，为理解物种进化提供了更完整的遗传图谱。
selection_source: fresh_fetch
motivation: 传统的短读长测序技术在解析高度重复序列和大规模结构变异方面存在瓶颈，限制了对物种进化多样性的深入理解。
method: 文章系统梳理了基于长读长数据的二倍体基因组组装、泛基因组图谱构建以及针对卫星 DNA 等复杂重复序列的计算注释方法。
result: 研究表明长读长技术能有效识别以往难以检测的基因拷贝数变异，并显著提升了对基因组中“暗物质”区域（如重复序列）的解析能力。
conclusion: 群体规模的长读长测序正引领进化基因组学进入泛基因组时代，随着计算工具的成熟，该领域的研究流程将逐步走向标准化。
---

## 摘要
群体规模长读长 DNA 测序 (PLRS) 正在迅速重塑我们对人类和非模式物种基因组变异的理解。在这篇《达尔文综述》（Darwin Review）中，我们首先回顾了过去 20 年间 PLRS 概念及其孪生范式——泛基因组（pangenome）的发展，并重点介绍了非人类脊椎动物的最新研究结果。以近期鸟类的 PLRS 研究为案例，我们探讨了 PLRS 研究的三个方面：二倍体基因组组装、重复组（repeatome）的表征与注释，以及基因拷贝数变异的检测，这些领域正受到新数据类型和计算工具的重塑。我们认为，在缺乏家系三人组数据的情况下，部分定相（partially phased）的单倍型为泛基因组分析提供了天然基础，特别是当直接从泛基因组图谱中量化结构变异时。我们指出了长读长组装中重复组注释存在的空白和差异，特别是针对卫星 DNA 和低复杂性 DNA，这些问题正通过新的计算工具得到改善。最后，我们讨论并评估了近期 PLRS 研究中揭示的基因拷贝数变异的惊人程度。当前泛基因组研究的方法论异质性可能很快会在快速发展的测序技术允许范围内，向少数核心方案收敛，从而提高研究之间的一致性。

## Abstract
Population-scale long-read DNA sequencing (PLRS) is rapidly reshaping our understanding of genomic variation in humans and non-model species. In this Darwin Review, we first recount the expansion of the PLRS concept and its twin paradigm, the pangenome, over the past 20 years, emphasizing recent results from non-human vertebrates. Using recent PLRS studies in birds as test cases, we probe three aspects of PLRS studies-diploid genome assembly, characterization and annotation of the repeatome, and detection of gene copy number variants-that are being re-shaped by new data types and computational tools. We argue that, in the absence of data from family trios, partially phased haplotypes provide a natural substrate for pangenome analysis, especially when quantifying structural variants directly from pangenome graphs. We identify gaps and discrepancies in the annotation of the repeatome of long-read assemblies, especially for satellite and low-complexity DNA, that are being ameliorated by new computational tools. Finally, we discuss and evaluate the surprising extent of gene copy number variation exposed in recent PLRS studies. The current methodological heterogeneity of pangenome studies may soon coalesce around a few core protocols to the extent allowed by rapidly changing sequencing technologies, allowing greater consistency among studies.