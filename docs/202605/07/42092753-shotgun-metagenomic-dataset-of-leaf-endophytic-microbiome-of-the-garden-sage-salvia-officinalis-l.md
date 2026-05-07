---
title: Shotgun metagenomic dataset of leaf endophytic microbiome of the garden sage (Salvia officinalis L.).
title_zh: 药用鼠尾草（Salvia officinalis L.）叶片内生微生物组的鸟枪法宏基因组数据集
authors: "Mouliraj Palanisamy, Olubukola Oluranti Babalola, Sathishkumar Ramalingam"
date: 2026-05-06
pdf: "https://pubmed.ncbi.nlm.nih.gov/42092753/"
tags: ["query:seqai"]
score: 6.0
evidence: 包含细菌和病毒的内生微生物组鸟枪法宏基因组数据集
tldr: 药用鼠尾草因其丰富的生物活性代谢物而具有重要药用价值，但其叶片内生微生物群落的多样性此前缺乏系统研究。本研究采用鸟枪法宏基因组测序技术，对三个生物重复样本进行深度测序，并利用 BWA-MEM 算法剔除宿主基因组干扰，最终通过 Kraken2 分类器构建了包含细菌、真菌、古菌和病毒的高质量数据集。该成果为解析植物-微生物相互作用及其对次生代谢产物的影响提供了公开的数据资源。
selection_source: fresh_fetch
motivation: 针对药用鼠尾草叶片内生微生物群落组成信息匮乏的问题，旨在系统性地探索其微生物多样性。
method: 利用鸟枪法宏基因组测序技术获取数据，并通过生物信息学手段剔除宿主污染及进行物种分类鉴定。
result: 产出并公开了一套涵盖药用鼠尾草叶片内生细菌、真菌、古菌和病毒的高质量宏基因组数据集。
conclusion: 该研究通过提供标准化的微生物组数据，为后续研究药用植物内生菌的功能及其生物学意义奠定了基础。
---

## 摘要
目的：药用鼠尾草（Salvia officinalis L.）是一种以富含生物活性次生代谢产物而闻名的传统药用植物。然而，关于其内生微生物群落（包括细菌、真菌、古菌和病毒）多样性的信息目前还很有限。因此，本研究采用鸟枪法宏基因组学技术，生成并公开了一个代表药用鼠尾草叶片内生微生物组的数据集。数据描述：从采集的三个生物学重复的药用鼠尾草叶片中提取宏基因组 DNA，并使用 Illumina NovaSeq X 平台进行测序。通过使用 BWA-MEM 将 reads 比对到药用鼠尾草参考基因组，去除了宿主来源和污染序列。对生成的高质量 FASTQ 文件进行了分析，并利用基于 Kraken2 的分类方法对内生微生物组的分类组成进行了表征。

## Abstract
OBJECTIVES: Garden sage (Salvia officinalis L.) is a traditional medicinal plant known for its rich bioactive secondary metabolites. However, there is limited information about the diversity of endophytic microbial communities, including bacteria, fungi, archaea, and viruses. Therefore, the study employs shotgun metagenomics to generate and make publicly available a dataset representing the leaf endophytic microbiome of Salvia officinalis. DATA DESCRIPTION: Metagenomic DNA was extracted from leaves of S. officinalis collected as three biological replicates and sequenced using the Illumina NovaSeq X platform. Host-derived and contaminant sequences were removed by mapping reads to the S. officinalis reference genome using BWA-MEM. The resulting high-quality FASTQ files were analyzed to characterize the taxonomic composition of the endophytic microbiome using Kraken2-based classification.