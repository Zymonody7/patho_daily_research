---
title: "MEditome: Computational Detection of RNA Edit Sites Using"
title_zh: MEditome：利用计算方法检测RNA编辑位点
authors: "Arpit Mehta, Vitalii Stebliankin, Kalai Mathee, Giri Narasimhan"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41869825/"
tags: ["query:seqai"]
score: 7.0
evidence: 微生物组中 RNA 编辑位点的计算检测
tldr: "RNA编辑对细菌适应性至关重要，但传统方法依赖参考基因组，难以检测未知菌株。MEditome 提出了一种基于从头组装（de novo assembly）的计算流程，能够直接从宏基因组和宏转录组数据中识别全微生物组的RNA编辑位点。该工具在人类肠道微生物组中发现了2,295个编辑位点，并揭示了与炎症性肠病相关的差异编辑模式，为理解微生物与宿主互动提供了新视角。"
selection_source: fresh_fetch
motivation: 传统的参考基因组比对方法在检测微生物组RNA编辑时存在偏差，无法识别数据库中缺失的新型菌株位点且搜索效率较低。
method: 开发了 MEditome 流程，利用从头组装技术构建重叠群，从而在无需预设参考基因组的情况下检测各类微生物的RNA编辑位点。
result: "在人类微生物组计划数据中成功识别出2,295个编辑位点，验证了已知的大肠杆菌编辑位点，并发现了与炎症性肠病相关的分类群特异性编辑模式。"
conclusion: MEditome 克服了参考基因组的限制，证明了RNA编辑是调节微生物适应性和宿主-微生物相互作用的重要机制。
---

## 摘要
RNA编辑是一种转录后修饰，它改变RNA链内的单核苷酸位点，从而使转录组和蛋白质组多样化并调节基因表达。虽然RNA编辑在真核生物和少数微生物中得到了较好的表征，但在整个微生物组中的研究仍未被探索。最近的研究表明，A-to-I RNA编辑有助于细菌的适应性和致病性。此前，我们开发了MetaEdit，这是一种基于参考基因组的计算流程，用于检测微生物组中的RNA编辑位点。虽然MetaEdit在人类肠道微生物组背景下成功识别了包括先前报道位点在内的大肠杆菌（Escherichia coli）RNA编辑位点，但它主要依赖于将测序序列（reads）比对到目标细菌的参考基因组。这种对参考基因组的依赖引入了潜在的偏差，因为编辑只能在参考基因组中被识别，而参考数据库中缺失的新型微生物菌株中的编辑可能会被忽视。即使对于参考基因组，编辑位点的搜索也是低效的，因为必须逐个参考基因组进行。在这里，我们介绍了MEditome，它采用从头组装（de novo assembly）来克服这些局限性。这一关键变化使得能够检测微生物组中所有微生物生物体的RNA编辑位点，包括那些缺乏完整参考基因组的新型细菌菌株。利用来自综合人类微生物组计划（Integrative Human Microbiome Project）的测序数据，MEditome在不同的细菌分类群中识别出2,295个独特的RNA编辑位点。其中一些位点与MetaEdit在hok/gef基因家族和精氨酸相关基因中检测到的先前识别的大肠杆菌编辑位点重合，提供了准确性的计算机模拟验证。我们观察到了分类群特异性的编辑模式以及与炎症性肠病相关的基因级差异编辑，强调了RNA编辑是影响微生物适应和宿主-微生物相互作用的一种潜在调节机制。

## Abstract
RNA editing is a post-transcriptional modification that alters single-nucleotide sites within RNA strands, thus diversifying transcriptomes and proteomes and modulating gene expression. While better characterized in eukaryotes and in a few microbes, the study of RNA editing in entire microbiomes remains unexplored. Recent studies have demonstrated that A-to-I RNA editing contributes to bacterial adaptation and pathogenicity. Previously, we developed MetaEdit, a reference-based computational pipeline to detect RNA edit sites in microbiomes. While MetaEdit successfully identified RNA edit sites in Escherichia coli within the context of the human gut microbiome, including previously reported loci, it relied primarily on aligning reads to reference genomes of target bacteria. This dependence on reference genomes introduced potential biases, as editing can only be identified in reference genomes, while editing in novel microbial strains missing from the reference databases could be overlooked. Even for reference genomes, the search for edit sites is inefficient since it would have to be conducted one reference genome at a time.Here, we introduce MEditome, employing de novo assembly to overcome these limitations. This crucial change enables the detection of RNA edit sites across all microbial organisms in the microbiome, including novel bacterial strains for which comprehensive reference genomes are unavailable. Using sequencing data from the Integrative Human Microbiome Project, MEditome identified 2,295 unique RNA editing sites across diverse bacterial taxa. Several of these overlaps with previously identified edits in E. coli detected by MetaEdit in hok/gef gene family and arginine-associated genes, providing in silico validation of accuracy. We observed taxon-specific editing patterns and gene-level differential editing associated with inflammatory bowel disease, highlighting RNA editing as a potential regulatory mechanism influencing microbial adaptation and host-microbe interactions.