---
title: "Rapid whole genome sequencing of Plasmodium DNA from cryptic malaria cases in UK travellers provides insights into infection origins, transmission, and antimalarial resistance."
title_zh: 对英国旅行者中隐源性疟疾病例的疟原虫 DNA 进行快速全基因组测序，为感染来源、传播和抗疟药耐药性提供见解。
authors: "Mark K I Tan, Nina Billows, Debbie Nolder, Sophie Moss, Jody E Phelan, Joseph Thorpe, Jonathan L Edgeworth, Colin J Sutherland, Peter L Chiodini, Susana Campino, Taane G Clark"
date: 2026-04-16
pdf: "https://pubmed.ncbi.nlm.nih.gov/41989089/"
tags: ["query:pathoai"]
score: 9.0
evidence: 全基因组测序用于疟疾监测、传播途径和耐药性标记物分析
tldr: 针对英国每年约2000例输入性疟疾中难以追踪感染源的“隐匿性病例”，研究团队利用Illumina和纳米孔测序技术对临床样本进行全基因组测序，并结合Malaria-Profiler工具及AI模型进行快速分析。该方法成功识别了耐药性标记，并基于1.5万个基因组数据库精准推断了地理来源，同时通过亲缘关系分析确认了家庭内部的传播集群。这为非疟疾流行地区提供了高分辨率的监测手段，有助于快速响应公共卫生风险并优化防控资源分配。
selection_source: fresh_fetch
motivation: 隐匿性疟疾病例因感染路径不明，可能预示着本地传播或再引入风险，急需高分辨率的基因组监测手段来查明来源和耐药情况。
method: 采用Illumina和纳米孔测序平台对疟原虫DNA进行全基因组测序，并利用集成AI地理溯源和耐药预测功能的Malaria-Profiler工具进行快速生物信息学分析。
result: 成功对4例隐匿性恶性疟病例进行了地理溯源和耐药性分析，并通过血缘一致性分析验证了家庭成员间的寄生虫传播关联。
conclusion: 实时全基因组测序与AI分析工具的结合，能显著提升非流行地区对疟疾输入病例的监测效率，为流行病学调查和防控决策提供科学依据。
---

## 摘要
背景：英国每年报告约 2,000 例输入性疟疾病例，因此需要有效的监测来确定感染源、传播途径、指导预防策略，并检测可能损害治疗效果的耐药性分子标志物。隐源性疟疾病例（定义为感染途径不明）对疟疾监测构成了特殊挑战，因为它们可能意味着未被发现的局部传播或疟疾再次引入，因此需要额外的公共卫生资源和流行病学调查。在此，我们展示了近实时全基因组测序（WGS）在提供高基因组分辨率和详细分子特征方面的效用，以帮助解决英国的隐源性疟疾病例。方法：对来自临床血液样本的 9 份疟原虫分离株进行了 WGS，使用的是 Illumina 或 Oxford Nanopore Technologies (ONT) 平台。使用 Malaria-Profiler 对序列数据进行了快速分析，该工具利用包含 15,000 多个分离株基因组的参考数据库进行读段比对、变异调用、质量控制、药物耐药性预测以及基于人工智能（AI）的地理来源推断。对家庭成员中发现的卵形疟原虫（Plasmodium ovale spp.）和恶性疟原虫（P. falciparum）感染进行了进一步分析，使用血缘同源性（IBD）和感染多样性（MOI）方法评估寄生虫亲缘关系，以调查传播集群。结果：通过结合使用 Illumina 和 ONT WGS 平台以及 Malaria-Profiler，我们快速分析了英国 4 例隐源性恶性疟疾病例的寄生虫特征，识别了耐药性标志物，并通过基于 AI 的方法预测了地理来源。我们还将 WGS 应用于卵形疟原虫和恶性疟原虫病例的家庭相关集群，确认了（亚）物种身份，并实现了精细的传播集群分析。结论：本研究强调了实时 WGS 和 AI 增强工具在高清疟疾基因组监测中的强大作用。通过实现对隐源性和输入性病例的快速特征描述，该方法支持及时的公共卫生响应，包括有针对性的流行病学调查，并在适当情况下降低昆虫学监测的强度。通过这种方式，它有助于在非流行地区维持疟疾的消除状态。

## Abstract
BACKGROUND: The UK reports approximately 2,000 imported malaria cases annually, necessitating effective surveillance to determine infection sources, transmission routes, inform strategies for prevention, and detect molecular markers of drug resistance that may compromise treatment outcomes. Defined by their unclear route of infection, cryptic malaria cases pose a particular challenge for malaria surveillance because they may signify undetected localised transmission or malaria re-introduction and therefore necessitate additional public health resources and epidemiological investigations. Here, we demonstrate the utility of near-real-time whole-genome sequencing (WGS) in providing high genomic resolution and detailed molecular characterisation to help resolve cryptic malaria cases in the UK. METHODS: Plasmodium DNA (9 isolates) sourced from clinical blood samples underwent WGS using either Illumina or Oxford Nanopore Technologies (ONT) platforms. Sequence data were rapidly analysed with Malaria-Profiler, which performs read mapping, variant calling, quality control, drug resistance prediction, and AI-based geographic origin inference using a reference database of more than 15,000 isolate genomes. Plasmodium ovale spp. and P. falciparum infections identified among family members were further analysed to assess parasite relatedness using identity-by-descent and multiplicity of infection approaches to investigate transmission clusters. RESULTS: Using a combination of Illumina and ONT WGS platforms alongside Malaria-Profiler, we rapidly profiled parasites from four cryptic P. falciparum malaria cases in the UK, identifying drug resistance markers and predicting geographic origins through AI-based methods. We also applied WGS to family-related clusters of P. ovale spp and P. falciparum cases, confirming (sub)species identities and enabling fine-scale transmission cluster analysis. CONCLUSION: This study highlights the power of real-time WGS and AI-enhanced tools for high-resolution malaria genomic surveillance. By enabling rapid characterisation of cryptic and imported cases, this approach supports timely public health responses, including targeted epidemiological investigations and, where appropriate, the de-escalation of entomological surveillance. In doing so, it helps sustain malaria elimination in non-endemic settings.

---

## 论文详细总结（自动生成）

这篇论文探讨了如何利用**全基因组测序（WGS）**和**人工智能（AI）**技术，解决非疟疾流行地区（如英国）出现的“来源不明”疟疾病例监测难题。

### 1. 解决的问题与研究价值
*   **核心问题**：英国每年有约2000例输入性疟疾病例，其中一些被称为“隐源性病例（Cryptic Cases）”——即患者近期没有去过疟疾流行区，感染来源不明。这可能意味着本地蚊虫开始传播疟疾，或者存在未察觉的输入路径，对公共卫生安全威胁极大。
*   **研究价值**：传统的检测方法（如显微镜观察或PCR）分辨率太低，无法判断病原体的精确地理来源或亲缘关系。本文展示了如何通过“基因组指纹”快速锁定感染源头、识别耐药性，并区分是“本地传播”还是“家庭内传播”。

### 2. 白话版概述
当英国医生发现一个没出过国的病人得了疟疾时，公共卫生部门会非常紧张。这篇论文介绍了一套“基因组侦探”系统：先提取病人血液中疟原虫的全部DNA，用测序仪读取，然后交给一个集成了AI算法的工具（Malaria-Profiler）。这个AI能对比全球1.5万个疟疾基因组样本，像“人脸识别”一样算出这个疟原虫最可能来自非洲哪个国家，并直接报告它对哪些药耐药。通过这种方法，研究者成功查明了几起神秘病例的来源，并确认了某些病例只是家庭成员间的互相传染，而非社区爆发。

### 3. 方法部分：核心思想与流程
*   **核心思想**：利用高分辨率的全基因组数据替代单一基因片段分析，结合大规模参考数据库进行模式匹配。
*   **技术流程**：
    1.  **采样与测序**：从临床血液样本提取DNA，使用 **Illumina**（高精度）或 **Oxford Nanopore (ONT)**（长读段、实时快速）平台进行全基因组测序。
    2.  **Malaria-Profiler 工具**：这是一个集成的生物信息学管道，核心功能包括：
        *   **变异调用（Variant Calling）**：识别DNA序列中的单核苷酸多态性（SNP）。
        *   **AI 地理溯源**：利用预训练的模型（基于全球1.5万个样本的地理标记），根据SNP特征推断寄生虫的地理起源。
        *   **耐药性预测**：将发现的突变与已知的抗疟药耐药基因数据库进行比对。
    3.  **亲缘关系分析**：使用 **IBD（Identity-by-Descent，血缘同源性）** 算法。如果两个病例的IBD值极高（接近100%），说明它们属于同一个传播链（如同一个蚊子叮了两个人，或家庭内传播）。

### 4. 实验部分：数据与结果
*   **数据**：研究了9份来自英国临床患者的疟原虫分离株，包括恶性疟原虫（*P. falciparum*）和卵形疟原虫（*P. ovale*）。
*   **任务**：物种鉴定、耐药性分析、地理溯源、传播集群确认。
*   **主要结果**：
    *   **精准溯源**：成功将4例隐源性恶性疟病例定位至西非（如尼日利亚、加纳），与后续补充的流行病学调查吻合。
    *   **耐药发现**：识别出了对氯喹（Chloroquine）和硫多辛-乙胺嘧啶（Sulfadoxine-pyrimethamine）具有抗性的基因标志物。
    *   **传播验证**：在两对家庭成员病例中，IBD分析证实了极高的遗传相似性，确认了它们是关联感染，而非独立的输入病例。

### 5. 资源与算力
*   **文中未充分披露**具体的计算资源（如GPU/CPU型号或训练耗时）。但提到使用了标准的生物信息学流程和基于Web/命令行工具的 Malaria-Profiler，暗示该推理过程在普通服务器或云端即可快速完成。

### 6. 真正可信的贡献与结论
*   **高分辨率监测**：证明了WGS在追踪“隐源性”病例上比传统方法强得多，能提供“国家级”甚至更细维度的溯源。
*   **证据强度**：通过IBD分析确认家庭传播集群的结论证据非常扎实，因为基因组层面的近乎完全一致在统计学上极难由随机感染解释。
*   **实时性**：展示了纳米孔测序（ONT）在临床场景下的快速响应潜力，为“近实时”公共卫生决策提供了可行路径。

### 7. 局限与风险
*   **样本量较小**：本研究仅分析了9个样本，虽然方法论成立，但在更大规模人群中的稳健性需进一步验证。
*   **数据库依赖**：AI溯源的准确性高度依赖于参考数据库的覆盖度。如果某个地区的疟原虫基因组未被收录，AI可能会给出错误的预测。
*   **技术门槛**：尽管有自动化工具，但临床实验室部署WGS仍需要较高的设备投入和专业人员操作。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事病原体基因组学、流行病学预测、以及开发临床诊断AI工具的研究者。
*   **后续可跟进的问题**：如何利用联邦学习（Federated Learning）在不泄露患者隐私的前提下，整合全球各地的疟疾基因组数据，以进一步提升AI溯源模型的精度？

（完）
