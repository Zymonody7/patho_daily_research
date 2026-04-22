---
title: "Empowering global disease surveillance with CURED: a tool for rapid identification of unique genomic biomarkers."
title_zh: 利用 CURED 赋能全球疾病监测：一种用于快速识别独特基因组生物标志物的工具
authors: "Erin Theiller, Swetha Rajagopol, Stephanie Higgins, Dayanara I Torres, T'Nia Napper, Bianca E Galis, Arie Dash, Elizabeth Qian, Lauren Hamlette, Qianxuan She, Ceylan Tanes, Nathan L'Etoile, Andries Feder, Alice Slotfeldt Viana, Matheus Assis Côrtes Esteves, Michael C Abt, Susan E Coffin, Ericka Hayes, Robert F Potter, Joseph P Zackular, Lakshmi Srinivasan, Agnes Marie Sá Figueiredo, Paul J Planet, Ahmed M Moustafa"
date: 2026-04-21
pdf: "https://pubmed.ncbi.nlm.nih.gov/41854250/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于快速追踪新兴病原微生物的基因组生物标志物
tldr: 针对全基因组测序（WGS）在病原微生物大规模实时监测中成本高、速度慢的问题，研究者开发了 CURED 工具。该工具通过分析基因组训练集，识别具有特定限制性内切酶位点的唯一 k-mer，从而将复杂的基因组信息转化为低成本、快速的 PCR 诊断方案。实验证明 CURED 在 MRSA、鲍曼不动杆菌等多种病原体检测中表现优异，显著提升了局部爆发调查和全球疾病监测的效率与可及性。
selection_source: fresh_fetch
motivation: 现有的全基因组测序技术虽然精准，但因成本和基础设施限制，难以满足资源有限地区或大规模实时疫情监测的需求。
method: CURED 利用高效的 k-mer 搜索策略，从已知基因组中筛选出特定克隆谱系独有的、且包含限制性酶切位点的生物标志物。
result: 在 MRSA 和耐药鲍曼不动杆菌等五个数据集上的测试显示，CURED 的扩展性优于同类工具，并成功应用于新生儿重症监护室的感染预防。
conclusion: 该工具通过将基因组洞察转化为简便的 PCR 诊断，为全球和局部范围内的病原体快速监测提供了一种高性价比且可扩展的技术方案。
---

## 摘要
快速追踪新出现的病原微生物对于制定有效的治疗、感染控制和预防策略至关重要。虽然全基因组测序 (WGS) 为追踪新出现的克隆提供了必要的粒度，但在进行高分辨率实时监测所需的规模下，其成本仍然高得令人望而却步。我们提出了 CURED（利用限制性内切酶诊断进行分类），它利用已测序基因组的训练集来识别具有特定克隆谱系限制性位点的独特 k-mer。CURED 能够以极少的 WGS 使用量，为监测或暴发调查提供快速且廉价的基于 PCR 的诊断测试。与现有工具的基准测试相比，CURED 表现出色，且比其他 k-mer 搜索策略具有更高效的可扩展性。我们在五个不同的数据集上验证并测试了 CURED：(i) 此前描述的里约热内卢耐甲氧西林金黄色葡萄球菌 (MRSA) 克隆的生物标志物，(ii) USA300 MRSA 克隆中不同谱系的诊断等位基因，(iii) 广泛耐药的鲍曼不动杆菌全球克隆 1 谱系，(iv) 产毒与非产毒艰难梭菌，以及 (v) 新生儿重症监护病房 (NICU) 中传播的金黄色葡萄球菌克隆。我们将 CURED 作为 NICU 感染预防工作的一部分进行了实施，并报告了该测试在真实环境中的速度、灵敏度和特异性。CURED 是一个可扩展、多线程、内存和成本高效的流水线，专为快速克隆检测和限制性位点分析而定制。虽然 CURED 对局部暴发调查和针对性监测特别有效，但我们在全球范围内的初步工作表明，更广泛的实施是可行的。CURED 可在 https://github.com/microbialARC/CURED 免费获取。重要性：及时且具有成本效益地检测新出现的微生物克隆对于感染预防和公共卫生监测至关重要。虽然全基因组测序仍然是追踪微生物进化和传播的金标准，但其成本、基础设施要求和周转时间限制了其可扩展性，尤其是在资源有限的环境中。CURED 通过利用基因组数据开发廉价的、基于 PCR 的诊断分析方法（无需进一步测序）填补了这一空白。通过可扩展且内存高效的 k-mer 流水线识别谱系特异性限制性位点，CURED 能够将基因组规模的见解转化为可操作的诊断方法。该工具支持在局部和全球病原体监测工作中更广泛地实施基于基因组信息的诊断。

## Abstract
Rapid tracking of emerging pathogenic microorganisms is crucial for designing effective treatment, infection control, and prevention strategies. While whole-genome sequencing (WGS) offers the necessary granularity to track emerging clones, it remains prohibitively expensive at the scales needed to monitor with high resolution in real time. We present CURED (Classification Using Restriction Enzyme Diagnostics), which uses a training set of sequenced genomes to identify unique k-mers with restriction sites specific to a clonal lineage. CURED enables fast and inexpensive PCR-based diagnostic tests for surveillance or outbreak investigations with minimal use of WGS. Benchmarking against existing tools, CURED compares favorably and scales more efficiently than other k-mer search strategies. We validated and tested CURED in five distinct data sets: (i) previously identified biomarkers described for a methicillin-resistant Staphylococcus aureus (MRSA) clone in Rio de Janeiro, (ii) diagnostic alleles for different lineages in the USA300 MRSA clone, (ii) the extensively drug-resistant Acinetobacter baumannii Global Clone 1 lineage, (iv) toxigenic versus non-toxigenic Clostridioides difficile, and (v) circulating S. aureus clones in a neonatal intensive care unit (NICU). We implemented CURED as part of NICU infection prevention efforts and report the test's speed, sensitivity, and specificity in a real-world setting. CURED is a scalable, multithreaded, memory-, and cost-efficient pipeline tailored for rapid clone detection and restriction site analysis. While particularly impactful for localized outbreak investigations and targeted surveillance, our preliminary work at the global scale suggests broader implementation is feasible. CURED is freely available at https://github.com/microbialARC/CURED.IMPORTANCETimely and cost-effective detection of emerging microbial clones is essential for infection prevention and public health surveillance. While whole-genome sequencing remains the gold standard for tracking microbial evolution and transmission, its cost, infrastructure requirements, and turnaround time limit its scalability, especially in resource-limited settings. CURED addresses this gap by enabling the development of inexpensive, PCR-based diagnostic assays informed by genomic data, without requiring further sequencing. By identifying lineage-specific restriction sites through a scalable and memory-efficient k-mer pipeline, CURED enables the translation of genome-scale insights into actionable diagnostics. This tool supports broader implementation of genomic-informed diagnostics in both local and global pathogen surveillance efforts.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **CURED** 的生物信息学工具，旨在解决病原体监测中“高精度”与“低成本”难以兼得的矛盾。

### 1. 解决的问题与研究意义
在传染病爆发时，科学家需要快速锁定是哪种特定的细菌“克隆谱系”（可以理解为某种细菌的特定变异分支）在作怪。
*   **现状：** 全基因组测序（WGS）虽然最准，但太贵、太慢，且需要昂贵的设备，无法在基层医院或资源匮乏地区大规模普及。
*   **痛点：** 传统的 PCR 检测（类似新冠核酸检测）虽然快且便宜，但很难区分同一种细菌下细微的谱系差异。
*   **意义：** CURED 通过算法从海量基因组数据中挖掘出“独一无二的指纹”，并将其转化为一种极其廉价的实验方案（PCR + 酶切），让普通实验室也能实现“测序级”的精准监测。

### 2. 白话版概述
想象你要在一堆长得几乎一样的双胞胎里找出一个坏蛋。全基因组测序是给每个人做全身扫描，费时费钱。CURED 的做法是：先对比所有人的扫描数据，发现坏蛋的左耳后有一颗独特的痣，且这颗痣正好能被某种特制的药水显色。于是，以后你不需要再做全身扫描，只需要用药水涂一下大家的耳朵（PCR 扩增 + 限制性内切酶切割），变色的就是坏蛋。CURED 就是那个专门帮你找“痣”并匹配“药水”的 AI 搜索工具。

### 3. 方法部分：核心思想与流程
CURED 的核心是一个高效的 **k-mer（短碱基序列片段）搜索与过滤流水线**：
*   **核心思想：** 利用已有的基因组数据库作为训练集，寻找在“目标菌株”中普遍存在、但在“非目标菌株”中完全不存在的特定 DNA 片段。
*   **关键设计：**
    1.  **k-mer 提取：** 将基因组切成固定长度 $k$ 的片段。
    2.  **差异化筛选：** 找出目标组独有的 k-mer。
    3.  **限制性内切酶匹配：** 这是该工具的灵魂。它不仅找唯一片段，还要求这个片段必须包含**限制性内切酶位点**（即分子手术刀能识别并切割的特定序列）。
    4.  **引物设计：** 自动设计 PCR 引物，确保这段 DNA 能被扩增出来。
*   **推理逻辑：** 最终输出一个实验方案：如果 PCR 产物被某种酶切断了，就证明它是目标菌株；没切断，就不是。

### 4. 实验部分
研究者在五个极具挑战性的数据集上验证了 CURED：
*   **数据与任务：**
    *   **MRSA（耐药金黄色葡萄球菌）：** 区分里约热内卢特有克隆和 USA300 流行谱系。
    *   **鲍曼不动杆菌：** 识别全球流行的耐药克隆 GC1。
    *   **艰难梭菌：** 区分产毒素（致病）和不产毒素的菌株。
    *   **NICU（新生儿重症监护室）：** 实时监测病房内的金黄色葡萄球菌传播。
*   **Baseline（对比对象）：** 与 Neptune 等主流基因组生物标志物发现工具对比。
*   **主要结果：**
    *   **性能：** CURED 在处理大规模基因组数据时，内存占用更低，运行速度更快（具有更好的可扩展性）。
    *   **实战：** 在 NICU 的真实场景中，CURED 设计的检测方案达到了极高的灵敏度和特异性，且成本仅为测序的零头。

### 5. 资源与算力
*   **文中未充分披露**具体的硬件配置（如 GPU 型号），但强调了该工具是**多线程**且**内存高效**的，可以在普通的服务器甚至高性能工作站上运行，不需要超算集群。

### 6. 真正可信的贡献
*   **工程化落地：** 它不是一个停留在论文里的算法，而是直接产出了可以直接在生物实验室操作的“湿实验”方案。
*   **证据强度：** 最强的证据来自 **NICU 的实地应用**。研究者不仅在电脑上跑了模拟，还真正在医院环境里用这个方法追踪了病原体传播，证明了其临床实用性。

### 7. 局限与风险
*   **数据依赖：** CURED 的准确性高度依赖于“训练集”（即已有的基因组数据库）的全面性。如果数据库里没涵盖某种变异，找出来的“唯一指纹”可能就不再唯一。
*   **进化风险：** 细菌进化很快，如果目标片段发生了突变，原本有效的酶切位点可能会失效（即假阴性）。
*   **技术门槛：** 虽然比测序简单，但仍需要实验室具备基本的分子生物学操作能力。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事基因组特征工程、计算生物学工具开发、以及关注“低成本诊断技术”的 AI 研究者。
*   **后续可跟进的问题：** 能否引入深度学习模型（如 Transformer 或 CNN）来预测哪些 k-mer 片段在细菌进化过程中更稳定，从而设计出更不容易失效的“长效”生物标志物？

（完）
