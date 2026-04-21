---
title: Analytical validation of a highly accurate and reliable next-generation sequencing-based urine assay.
title_zh: 一种高准确度且可靠的基于二代测序的尿液检测方法的分析验证
authors: "Mara Couto-Rodriguez, David C Danko, Heather L Wells, Sol Rey, Xavier Jirau Serrano, Gabor Fidler, John Papciak, P Ford Combs, Anna Plourde, Michael Augenbraun, Christopher E Mason, Caitlin Otto, Niamh B O'Hara, Dorottya Nagy-Szakal"
date: 2026-04-21
pdf: "https://pubmed.ncbi.nlm.nih.gov/42012213/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于尿液宏基因组病原体检测的机器学习
tldr: "针对传统尿培养在尿路感染诊断中灵敏度低、易漏诊的问题，研究团队开发并验证了 BIOTIA-ID 临床级宏基因组测序管线。该方法结合机器学习算法过滤共生菌干扰，在 1470 份样本中实现了 97.2% 的灵敏度和 99.6% 的特异性，并能同步检测耐药基因。该技术为复杂或复发性感染提供了比传统培养更精准、全面的诊断方案，有助于优化抗生素使用并支持临床决策。"
selection_source: fresh_fetch
motivation: 传统尿培养方法灵敏度不足且耗时长，容易导致漏诊或抗生素滥用，急需一种更精准的临床级病原体检测手段。
method: 开发了基于 Illumina 测序的 BIOTIA-ID 管线，利用机器学习算法对宏基因组数据进行高强度过滤，以区分致病菌与尿道共生微生物。
result: "在大规模临床验证中，该方法对细菌和真菌的检测灵敏度极高，且与传统金标准的一致性达到 87%，并成功识别了多种关键耐药基因。"
conclusion: BIOTIA-ID 证明了宏基因组测序在尿路感染诊断中的临床可行性，是替代传统培养、提升精准医疗水平的可靠工具。
---

## 摘要
尿路感染 (UTIs) 通常根据症状诊断并经尿液培养确认，尽管培养法在灵敏度上存在局限。培养假阴性可能导致抗微生物药物的不当使用，或使高风险患者出现尿源性脓毒症。基于二代测序 (NGS) 的宏基因组学提供了一种全面且精确的替代方案，但临床应用较少。我们开发并验证了 BIOTIA-ID，这是一种用于尿液病原体检测的临床级 NGS 诊断流程。对临床剩余样本和加标尿液

## Abstract
Urinary tract infections (UTIs) are diagnosed based on symptoms and confirmed by urine culture, despite its limitations in sensitivity. False-negative cultures can lead to inappropriate antimicrobial use or urosepsis in high-risk patients. Next-generation sequencing (NGS)-based metagenomics offers a comprehensive and precise alternative but is rarely applied clinically. We developed and validated BIOTIA-ID, a clinical-grade NGS-based diagnostic pipeline for pathogen detection in urine. Remnant clinical and spiked urine samples underwent extraction, metagenomic library preparation, and Illumina NextSeq 550 sequencing. We trained and applied a bioinformatic pipeline that uses machine learning to identify pathogens and resistance markers. BIOTIA-DX was intentionally designed and trained to increase stringency and reduce false positive detection of urogenital commensals or opportunistic microbes present at colonization levels. Internal controls ensured standardized, high-stringency results. The assay was validated on 1,470 urine specimens evaluating over 14.5k analytes. The clinical validation achieved a 97.2% sensitivity and 99.6% specificity with a limit of detection (LoD) of <15,000 CFU/mL for most bacterial species and <5,000 CFU/mL for fungal species. Discordant results were reconciled by target-specific qPCR or 16S Sanger sequencing, and 87% of the NGS results were concordant with the comparator. A subset of 332 clinical specimens was tested and validated for antimicrobial resistance (AMR). sul and blaSHV genes were commonly associated with Escherichia coli and Klebsiella pneumoniae, while cfxA was found in Prevotella and Pseudomonas spp. detected by BIOTIA-ID. Overall, these data demonstrate that BIOTIA-ID is a comprehensive, highly accurate end-to-end diagnostic assay with notable advantages over current culture-based diagnostics.IMPORTANCEUrinary tract infections (UTIs) are among the most common infections, yet current diagnostic methods, including urine culture, often fail to detect pathogens accurately, leading to delayed treatment and inappropriate antimicrobial use. Clinical metagenomics offers a powerful alternative, especially in complicated cases. BIOTIA-ID is a validated, clinical-grade next-generation sequencing (NGS)-based assay that provides highly accurate pathogen identification and antimicrobial resistance profiling. By incorporating machine learning and stringent quality controls, BIOTIA-ID minimizes false positives and enhances diagnostic precision. Our study demonstrates its superior performance over culture, with potential to improve UTI diagnostics, guide targeted therapy, and support antimicrobial stewardship. The implementation of urine metagenomic diagnostics could support recurrent and complicated UTI patient management, providing a more reliable alternative to traditional methods.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种名为 **BIOTIA-ID** 的临床级尿液检测系统，旨在通过宏基因组测序（mNGS）和机器学习技术，解决传统尿液培养方法“查不准、查得慢”的问题。

### 1. 解决的问题与研究意义
*   **核心问题**：尿路感染（UTI）是全球最常见的感染之一，但目前的诊断“金标准”——**尿液培养**存在严重缺陷：灵敏度低（约 30%-50% 的感染者培养结果为阴性）、耗时长（2-3 天）、且无法检测难以培养的微生物。
*   **研究意义**：漏诊或误诊会导致抗生素滥用或引发严重的尿源性脓毒症（Urosepsis）。该研究通过大规模临床验证，证明了基于 AI 增强的测序技术可以提供比传统方法更精准、更全面的病原体及耐药基因（AMR）分析，为复杂性尿路感染的精准医疗提供了工具。

### 2. 白话版概述
传统的尿检就像是在地里“种种子”，看哪种细菌能长出来，但很多坏细菌在实验室里根本不长。这篇论文的方法是直接“提取所有 DNA”，通过二代测序把尿液里所有的遗传信息读出来。因为尿道里本来就有一些无害的正常菌群（共生菌），研究者训练了一个机器学习模型来当“质检员”，专门剔除这些干扰项，只揪出真正的致病菌。实验证明，这种方法不仅比传统培养更灵敏，还能顺便查出细菌怕哪种药。

### 3. 方法部分：核心思想与流程
*   **核心思想**：利用宏基因组测序（mNGS）捕获样本中所有微生物的 DNA，并结合机器学习算法进行高强度的“降噪”处理，区分**致病菌**与**共生微生物**（正常定植在人体内不致病的菌）。
*   **技术流程**：
    1.  **样本处理**：对尿液进行 DNA 提取，使用 Illumina NextSeq 550 平台进行宏基因组文库构建和测序。
    2.  **生物信息管线**：将测序序列与庞大的微生物数据库比对。
    3.  **机器学习过滤（关键设计）**：BIOTIA-DX 算法被设计用于提高严谨性。它通过训练识别哪些微生物在什么丰度下属于“正常背景”，从而减少因皮肤或尿道正常菌群污染导致的假阳性。
    4.  **耐药基因检测**：同步扫描样本中的抗微生物耐药（AMR）基因，预测细菌的耐药性。

### 4. 实验部分：数据与结果
*   **数据规模**：验证了 **1,470 份** 尿液样本，评估了超过 1.45 万个分析物（Analytes）。
*   **评价指标**：灵敏度（Sensitivity）、特异性（Specificity）、检出限（LoD）、一致性（Concordance）。
*   **主要结果**：
    *   **准确性**：灵敏度达到 **97.2%**，特异性达到 **99.6%**。
    *   **检出限**：大多数细菌的检出限低于 15,000 CFU/mL，真菌低于 5,000 CFU/mL（优于传统培养的阈值）。
    *   **一致性**：与传统培养方法的一致性为 87%。在不一致的样本中，通过更灵敏的 qPCR 或 16S 测序证实，mNGS 发现了很多培养法漏掉的真病原体。
    *   **耐药性**：成功识别了如 *sul*（磺胺类耐药）和 *blaSHV*（内酰胺类耐药）等关键基因。

### 5. 资源与算力
*   **硬件**：使用了 Illumina NextSeq 550 测序仪。
*   **计算资源**：文中**未充分披露**具体的计算集群配置或训练机器学习模型所需的 GPU/CPU 小时数，但提到这是一个端到端的自动化临床管线。

### 6. 真正可信的贡献
*   **大规模临床验证**：1,470 份样本的验证规模在临床宏基因组学领域是非常扎实的，证明了该技术在临床实验室环境下的可重复性和可靠性。
*   **解决“背景噪音”问题**：通过机器学习区分“定植”和“感染”，这是 mNGS 进入临床诊断的最大障碍之一，该研究给出了一个可行的工程化方案。
*   **耐药性同步检测**：在一次检测中同时完成病原体鉴定和耐药基因扫描，比传统“先培养再做药敏”的流程大幅缩短了决策时间。

### 7. 局限与风险
*   **成本问题**：mNGS 的测序成本远高于几美元一次的尿培养，限制了其在常规体检中的普及，目前更适合复杂或复发性感染。
*   **基因型不等于表型**：检测到耐药基因并不意味着细菌在体内一定表现出耐药性（基因表达受多种因素影响），临床医生在解读时仍需谨慎。
*   **数据偏差**：虽然样本量大，但主要集中在特定区域的临床中心，对于全球不同地理区域的微生物分布差异可能覆盖不足。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事临床诊断 AI、宏基因组学算法开发、以及抗生素耐药性研究的研究者。
*   **后续可跟进的问题**：如何利用 AI 进一步预测细菌的**表型耐药性**（即不仅看有没有基因，还看药到底管不管用），以及如何利用长读段测序（如 Nanopore）实现更快速的实时床旁检测。

（完）
