---
title: A systematic review and benchmarking of modern metagenomic tools for taxonomic classification.
title_zh: 现代宏基因组分类学鉴定工具的系统综述与基准测试
authors: "Inês Branco Martins, Jorge Miguel Silva, João Rafael Almeida"
date: 2026-04-15
pdf: "https://pubmed.ncbi.nlm.nih.gov/41830810/"
tags: ["query:pathoai"]
score: 9.0
evidence: 宏基因组分类工具的基准测试
tldr: 宏基因组分类工具是微生物群落研究的核心，但由于评估标准和数据库差异，工具间的横向对比十分困难。本研究系统综述了31款最新分类工具，并选取其中9款在统一的NCBI RefSeq基准数据集上进行性能评测。结果显示，领域专用工具（如针对原核生物的TAMA和针对病毒的ViWrap）在准确率上具有显著优势，而SqueezeMeta在跨领域任务中表现均衡。该研究为AI和生物信息学研究者在不同应用场景下选择最优分类算法提供了量化参考。
selection_source: fresh_fetch
motivation: 针对宏基因组分类工具缺乏统一评估标准的问题，旨在通过标准化基准测试解决研究者在工具选择上的困惑。
method: 选取9款主流分类工具，利用NCBI RefSeq标准数据集，从分类准确度、计算效率及抗突变干扰能力等多个维度进行定量对比。
result: 实验发现领域专用工具在特定类群（如原核或病毒）中准确率更高，而基于组装的工具如SqueezeMeta虽综合得分高，但在高多样性样本中受限。
conclusion: 宏基因组分类工具正向领域专业化和机器学习化发展，选择工具时需权衡目标生物领域、样本多样性及计算资源消耗。
---

## 摘要
宏基因组学的进步受到生物信息学工具持续发展的推动，特别是分类学鉴定软件，这些软件对于准确表征微生物群落至关重要。然而，由于评估指标、参考数据库和输入数据类型的差异，在这些工具之间建立直接比较仍然具有挑战性。在本研究中，我们对近期开发的宏基因组分类学鉴定工具进行了系统综述。在识别出的 31 个工具中，有 9 个满足基准测试分析的所有功能和方法学标准。我们使用源自 NCBI RefSeq 数据库的标准数据集评估了它们的准确性和计算性能。分析结果显示，大多数工具具有领域特异性，各自在特定领域表现出色。TAMA、CAMITAX 和 PhyloFlash 等工具在原核生物鉴定方面表现出更高的准确性，而 ViWrap 和 PhaBOX 在病毒分类方面准确性更高。SqueezeMeta 在大多数领域都获得了较高的 F1 分数，但其基于组装的架构限制了其在高度多样化样本上的有效性。MegaPath-Nano 受突变率增加的影响最小。各工具的执行时间差异很大，领域特异性和基于机器学习的工具通常速度更快，而像 BASTA 这样的工具运行时间较长且准确性较低。本综述综合了当前工具的性能结果，提供了其优势和计算方法的概览。

## Abstract
Advancements in metagenomics have been driven by the continuous development of bioinformatic tools, particularly taxonomic classification software, which are central to the accurate characterization of microbial communities. However, establishing direct comparisons between these tools remains challenging due to variations in evaluation metrics, reference databases, and input data types. In this study, we present a systematic review of recently developed metagenomic taxonomic classification tools. Of the 31 identified tools, nine satisfied all functional and methodological criteria for the benchmark analysis. We evaluated their accuracy and computational performance using a standardized dataset derived from the NCBI RefSeq database. Our analysis revealed that most of these tools are domain-specific, each excelling in particular areas. Tools like TAMA, CAMITAX and PhyloFlash achieved higher accuracy for prokaryotic organisms, while ViWrap and PhaBOX achieved higher accuracy for viral classifications. SqueezeMeta achieved high F1 scores across most domains, though its assembly-based architecture limits effectiveness on highly diverse samples. MegaPath-Nano was least affected by increased mutation rates. The execution time varied widely among the tools, with domain-specific and machine learning-based tools generally being faster, while tools like BASTA had longer runtimes and lower accuracy. This review synthesizes performance results for current tools, providing an overview of their strengths and computational methodologies.