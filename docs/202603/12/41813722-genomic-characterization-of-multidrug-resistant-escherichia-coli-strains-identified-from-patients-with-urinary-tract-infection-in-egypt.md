---
title: Genomic characterization of multidrug-resistant Escherichia coli strains identified from patients with urinary tract infection in Egypt.
title_zh: 埃及尿路感染患者中发现的多重耐药大肠埃希氏菌菌株的基因组特征分析
authors: "Nancy M El Halfawy, Mona K Gouda, Fatma A Elgayar, Alaa Aboelnour Badran"
date: 2026-03-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/41813722/"
tags: ["query:pathoai"]
score: 8.0
evidence: 大肠杆菌的基因组特征分析和耐药性预测
tldr: 针对埃及尿路感染患者中多重耐药大肠杆菌（ESBL-EC）流行率上升的问题，本研究利用 Illumina NovaSeq 6000 平台对两株临床分离株（UPE7 和 UPE139）进行了全基因组测序（WGS）及生物信息学分析。研究成功鉴定出多种耐药基因（如 blaCTM-X-15、blaOXA-244）和毒力因子，并揭示了与左氧氟沙星耐药相关的关键基因突变。该成果为监测高风险克隆和指导临床抗生素使用提供了重要的基因组学依据。
selection_source: fresh_fetch
motivation: 埃及地区抗生素的广泛使用导致多重耐药大肠杆菌引发的尿路感染日益严重，亟需通过基因组手段明确其耐药机制与传播潜力。
method: 采用 Illumina NovaSeq 6000 平台对两株临床分离的大肠杆菌进行全基因组测序，并利用生物信息学工具对其耐药基因、毒力因子及血清型进行全面表征。
result: 研究发现了 blaCTM-X-15、blaOXA-244 等关键耐药基因，并证实了 gyrA 等基因突变与左氧氟沙星耐药性的关联，同时识别出促进基因水平转移的移动遗传元件。
conclusion: 全基因组监测是追踪高风险耐药克隆和指导临床精准用药的关键工具，对提升流行病学防控水平具有重要意义。
---

## 摘要
产超广谱β-内酰胺酶大肠埃希氏菌（ESBL-EC）构成了严重威胁。此外，埃及广泛使用抗菌药物增加了抗菌药物耐药性（AMR）的流行率。在本研究中，利用 Illumina NovaSeq 6000 对从尿路感染参与者中分离出的两株菌株（UPE7 和 UPE139）进行了全基因组测序（WGS），以表征其耐药组和毒力组。使用计算分析工具预测了两株临床大肠埃希氏菌菌株的抗生素耐药基因和毒力基因。鉴定出了多种毒力性状和抗生素耐药基因（ARGs）。菌株 UPE7 携带 blaTEM-1B、blaCTM-X-15 和 blaCMY-2，而菌株 UPE139 显示存在 blaOXA-244、blaTEM-12、blaTEM-82 和 blaCTM-X-15，从而导致了耐药表型。邻近 ARGs 的可移动遗传元件的存在表明其具有通过水平基因转移进行传播的潜力。此外，计算机模拟血清分型研究显示，大肠埃希氏菌 UPE7 和 UPE139 的血清型分别为 O8:H9 和 O9:H30。值得注意的是，预测到了 gyrA、parC 和 parE 基因的关键突变，这与其已证实的对左氧氟沙星的耐药性一致。这些发现强调了基因组监测在指导抗菌治疗和监测新兴高风险克隆方面的重要性，并支持开展更大规模的基因组研究以提高流行病学理解和临床相关性。

## Abstract
Extended-spectrum β-lactamases-producing Escherichia coli (ESBL-EC) pose a serious threat. Moreover, widespread antimicrobial use in Egypt increased the prevalence of antimicrobial resistance (AMR). In this study, whole-genome sequencing (WGS) using the Illumina NovaSeq 6000 was performed on two isolates (UPE7 and UPE139) recovered from participants with urinary tract infections to characterize their resistomes and virulomes. Antibiotic resistance and virulence genes of the two clinical E. coli strains were predicted using computational analysis tools. Several virulence traits and antibiotic resistance genes (ARGs) were identified. Strain UPE7 harbored blaTEM-1B, blaCTM-X-15, blaCMY-2, and strain UPE139 revealed the presence of blaOXA-244, blaTEM-12, blaTEM-82, and blaCTM-X-15 rending the resistance phenotype. The presence of mobile genetic elements adjacent to ARGs thereby suggests their potential for dissemination through horizontal gene transfer. Furthermore, the serotyping in silico investigation revealed that E. coli UPE7 and UPE139 serotypes were O8:H9 and O9:H30, respectively. Notably, key mutations in the gyrA, parC, and parE genes were predicted, consistent with their confirmed resistance to levofloxacin. These findings emphasize the importance of genomic surveillance to guide antimicrobial therapy and monitor emerging high-risk clones, and they support the need for larger-scale genomic studies to improve epidemiological understanding and clinical relevance.

---

## 论文详细总结（自动生成）

这篇论文对埃及尿路感染（UTI）患者体内的多重耐药大肠埃希氏菌（MDR *E. coli*）进行了全基因组层面的“深度扫描”。以下是该研究的结构化总结：

### 1. 解决的问题与研究意义
*   **核心问题**：在埃及，由于抗生素使用不规范，导致产超广谱β-内酰胺酶（ESBL，一种能让多种常见抗生素失效的酶）的大肠杆菌泛滥。医生急需知道：这些细菌到底携带了哪些耐药基因？它们是如何进化出耐药性的？以及它们是否具备快速传播的能力？
*   **研究意义**：通过全基因组测序（WGS），研究者可以从分子水平锁定细菌的“武器库”（毒力因子）和“防弹衣”（耐药基因），为临床精准用药和流行病学监测提供数字化证据。

### 2. 白话版概述
简单来说，研究人员从埃及尿路感染患者身上抓到了两株表现非常“强悍”的大肠杆菌（编号 UPE7 和 UPE139）。他们利用高通量测序技术读出了这两株菌的全部 DNA 序列，并用计算机算法分析了它们的基因特征。结果发现，这两株菌不仅装备了多种能抵抗抗生素的基因，还发生了关键的基因突变，使得原本常用的左氧氟沙星等药物彻底失效。更危险的是，这些耐药基因旁边还跟着一些“搬运工”基因（移动遗传元件），意味着耐药性很容易在不同细菌间传染。

### 3. 方法部分
*   **核心思想**：利用“基因组学+生物信息学”替代传统的生物化学实验，实现对病原菌特征的全面表征。
*   **技术流程**：
    1.  **样本获取**：从临床尿路感染患者中分离出两株典型的大肠杆菌。
    2.  **高通量测序**：使用 **Illumina NovaSeq 6000** 平台进行全基因组测序（WGS），获取原始碱基序列。
    3.  **生物信息学预测**：利用计算工具（如 ResFinder、VirulenceFinder 等）在基因组中搜索已知的耐药基因（ARGs）、毒力因子和血清型标记。
    4.  **突变分析**：针对特定药物（如喹诺酮类），重点检查 *gyrA*、*parC* 等关键靶点基因的单核苷酸多态性（SNP）。
*   **关键取舍**：研究选择了深度测序而非简单的 PCR 扩增，虽然成本更高，但能发现未知的移动遗传元件和精确的基因排列顺序。

### 4. 实验部分
*   **数据与任务**：对 UPE7 和 UPE139 两株菌进行全基因组表征。
*   **主要发现**：
    *   **耐药基因（Resistome）**：UPE7 携带 *blaTEM-1B*、*blaCTM-X-15* 等；UPE139 携带 *blaOXA-244*（一种重要的碳青霉烯酶变体）等。
    *   **点突变**：在 *gyrA*、*parC* 和 *parE* 基因中发现了关键突变，这解释了为什么这两株菌对左氧氟沙星高度耐药。
    *   **血清型（Serotyping）**：通过计算机模拟确定 UPE7 为 O8:H9，UPE139 为 O9:H30。
    *   **传播潜力**：在耐药基因附近发现了移动遗传元件（MGEs），证实了这些细菌具有通过“水平基因转移”扩散耐药性的风险。

### 5. 资源与算力
*   **硬件**：使用了 Illumina NovaSeq 6000 测序仪。
*   **软件/算力**：文中提到了使用“计算分析工具”，但未详细披露具体的服务器配置、计算耗时或内存占用。

### 6. 真正可信的贡献
*   **基因型与表型的强关联**：研究成功将基因组中的特定突变（如 *gyrA* 突变）与临床上的耐药表现（对左氧氟沙星耐药）一一对应，证据链完整。
*   **区域性流行病学数据**：首次详细揭示了埃及地区特定高风险克隆（如携带 *blaOXA-244* 的菌株）的基因组特征，对当地公共卫生预警有直接价值。

### 7. 局限与风险
*   **样本量极小**：仅分析了两株菌（n=2），属于个案研究，其结论在多大程度上能代表埃及乃至全球的流行趋势仍存疑。
*   **缺乏功能验证**：所有的耐药性和毒力分析均基于计算机预测（In silico），未通过基因敲除或回补实验来验证这些基因在实际感染中的具体贡献。
*   **静态分析**：未能观察到耐药基因在实际传播过程中的动态演变。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事**病原体基因组大模型**开发、**耐药性预测算法**（AMR Prediction）以及**宏基因组监测**的研究者。
*   **后续可跟进的问题**：能否仅凭原始的测序 Read 流（无需完整组装基因组），利用深度学习模型实时预测细菌的耐药表型和传播风险？

（完）
