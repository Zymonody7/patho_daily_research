---
title: "FALCON2: compression-based metagenomic classification of ancient viruses."
title_zh: FALCON2：基于压缩的古病毒宏基因组分类
authors: "Marques LL, Pinho AJ, Pratas D., Luis L Marques, Armando J Pinho, Diogo Pratas"
date: 2026-03-30
pdf: "https://pubmed.ncbi.nlm.nih.gov/41913056/"
tags: ["query:pathoai"]
score: 10.0
evidence: 古病毒的宏基因组分类
tldr: 古代病毒DNA（aDNA）具有片段极短（20-100bp）且存在化学损伤的特点，导致传统基于k-mer匹配或比对的分类器在超短序列上准确率大幅下降。FALCON2 提出了一种基于压缩算法的分类框架，利用位置感知的有限上下文模型（FCM）捕捉序列特征。实验表明，在20-40bp的超短序列任务中，FALCON2 的 AUPRC 达到 0.968，远超 Kraken2 等主流工具，为古基因组学研究提供了高精度且低内存消耗的分类方案。
selection_source: fresh_fetch
motivation: 针对古代病毒DNA片段极短且伴有化学损伤，导致传统k-mer匹配方法在宏基因组分类中失效的问题。
method: 采用基于压缩算法的分类策略，通过位置感知的有限上下文模型（FCM）来提取并识别高度降解序列中的特征。
result: 在模拟病毒数据集上，FALCON2 的 AUPRC 达到 0.968，在 20-40bp 的超短序列分类表现上显著优于 Centrifuge 和 Kraken2。
conclusion: 该工具证明了压缩模型在处理极短、受损生物序列上的优越性，且仅需 4-8GB 内存即可运行，具有极高的实用价值。
---

## 摘要
动机：由于极度的碎片化（读段长度为 20-100 bp）、末端偏向的胞嘧啶脱氨作用以及高污染率，古 DNA (aDNA) 序列为分类学鉴定带来了独特挑战。基于精确 k-mer 匹配或比对的传统宏基因组分类器在处理此类短且受损的读段时会丧失判别能力，从而限制了古基因组样本的分析。结果：我们提出了 FALCON2，这是一种基于压缩的宏基因组分类器，利用位置感知的有限上下文模型在降解的古病毒上保持高准确度。FALCON2 将其前身 FALCON-meta 的功能整合到一个统一的可执行文件中，并增强了功能，包括模型持久化、直接处理压缩输入、多文件处理以及针对污染样本的可选预过滤方法。在对模拟病毒数据集进行数据库、分类学和线程对齐的受控基准测试中，FALCON2 的受试者工作特征曲线下面积 (AUC-ROC) 达到 0.999，精准率-召回率曲线下面积 (AUPRC) 为 0.968，F1 分数为 0.918，在汇总微平均指标上显著优于 Centrifuge (AUPRC = 0.625)、Kraken2 (AUPRC = 0.184) 和 CLARK-S (AUPRC = 0.013)。FALCON2 的优势在超短读段（20-40 bp）上最为显著，因为此时精确的 k-mer 变得稀疏。在阈值为 0.7 时，FALCON2 的预过滤在召回率损失微乎其微的情况下，将精确率提高了 10 个百分点。对于典型分析，FALCON2 可在 4-8 GB RAM 的系统上运行。可用性：FALCON2 在 https://github.com/cobilab/FALCON2 上根据 GPL v3 许可免费提供。基准测试数据和脚本存档于 DOI: https://doi.org/10.5281/zenodo.17291214。补充信息：补充数据可在 Bioinformatics 在线获取。

## Abstract
MOTIVATION: Ancient DNA (aDNA) sequences present unique challenges for taxonomic classification due to extreme fragmentation (reads 20-100 bp), end-biased cytosine deamination, and high contamination rates. Conventional metagenomic classifiers based on exact k-mer matching or alignment lose discriminative power on such short and damaged reads, limiting the analysis of paleogenomic samples. RESULTS: We present FALCON2, a compression-based metagenomic classifier that leverages position-aware finite-context models to maintain high accuracy on degraded viral ancient viruses. FALCON2 consolidates the capabilities of its predecessor, FALCON-meta, into a unified executable with enhanced features including model persistence, direct processing of compressed inputs, multiple file handling, and optional pre-filtering methodologies for contaminated samples. Under controlled benchmarking with database, taxonomy, and thread parity on simulated viral datasets, FALCON2 achieved an Area Under the Curve of Receiver Operating Characteristic (AUC-ROC) of 0.999, an Area Under Precision-Recall Curve (AUPRC) of 0.968, and an F1-score of 0.918, substantially outperforming Centrifuge (AUPRC = 0.625), Kraken2 (AUPRC = 0.184), and CLARK-S (AUPRC = 0.013) on pooled micro-averaged metrics. FALCON2's advantage is most pronounced on ultra-short reads (20-40 bp), where exact k-mers become sparse. FALCON2 pre-filtering at threshold 0.7 improved precision by 10 percentage points with negligible recall loss. FALCON2 runs on systems with 4-8 GB RAM for typical analyses. AVAILABILITY: FALCON2 is freely available at https://github.com/cobilab/FALCON2 under GPL v3 license. Benchmarking data and scripts are archived at DOI: https://doi.org/10.5281/zenodo.17291214. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.