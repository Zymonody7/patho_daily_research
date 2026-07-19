---
title: "Artificial Intelligence and Protein Design: A retrospective study on 20-year emerging trends and core research areas from bibliometric perspectives."
title_zh: 人工智能与蛋白质设计：基于文献计量学视角的20年新兴趋势与核心研究领域回顾性研究
authors: "Wenjuan Zhao, Xiuwu Pan, Wei Yang, Zichang Liu, Xiyi Wei, Anqi Lin, Bufu Tang, Lin Zhang, Mingjia Xiao, Qing Zeng, Quan Cheng, Weiming Mou, Xiaofan Lu, Kai Miao, Peng Luo, Xin-Gang Cui, Wen-Jin Chen"
date: 2026-07-18
pdf: "https://pubmed.ncbi.nlm.nih.gov/42470596/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 人工智能和深度学习在蛋白质设计中的文献计量研究
tldr: 蛋白质设计在生物医药领域至关重要，但AI如何重塑该领域尚需系统梳理。本文通过对2006-2025年间的文献进行计量学分析，揭示了2018年后由AlphaFold2等模型引发的研究爆发，识别出结构预测、定向进化和从头设计三大核心集群。研究指出，结合计算设计与实验验证的模式最具影响力，为未来解决模型泛化性及动态构象预测等挑战提供了方向。
selection_source: fresh_fetch
motivation: 旨在通过计量学手段系统性地梳理过去二十年人工智能在蛋白质设计领域的演进历程、核心研究集群及未来挑战。
method: 利用CiteSpace、VOSviewer及自定义脚本，对Web of Science数据库中近二十年的相关文献进行共引分析、关键词共现及合作网络挖掘。
result: 发现2018年后论文数量因AlphaFold2等突破而激增，形成了以结构预测和从头设计为核心的知识体系，并指出中美两国在发文量上领先，而瑞士在人均引用影响力上表现突出。
conclusion: 蛋白质设计正处于AI驱动的变革中心，未来需通过高通量实验反馈与迭代设计循环，克服模型在动态构象预测和细胞环境适应性方面的局限。
---

## 摘要
蛋白质设计在合成生物学、药物发现和生物工程中具有广泛的应用。近年来，由于人工智能的出现，该领域发生了一场革命。深度学习模型（DLMs）处于这一变革的最前沿。这些模型对设计流程的影响具有颠覆性，导致了蛋白质预测精度、功能富集和从头合成（de novo synthesis）方面的突破性进展。我们对通过针对性关键词搜索获得的 Web of Science 数据集（2006-2025年）进行了文献计量分析。我们的分析方法综合使用了 CiteSpace 和 VOSviewer 等标准工具进行共引、关键词共现和突发检测，同时利用自定义 Python 脚本为协作网络和知识重叠生成更细致的图表。基于文献计量分析，我们观察到 2018 年后出版物数量突然激增。这一时期也与 AlphaFold2 和 RoseTTAFold 等许多方法论突破的发表相吻合。分析揭示了围绕蛋白质结构预测、定向进化和蛋白质从头设计的三个主要知识集群。深度学习模型在生成功能性蛋白质序列的出版影响力中发挥着重要作用，ProteinMPNN 等框架具有显著的引用足迹。尽管中国和美国在原始出版量上占据主导地位，但引用影响力却呈现出不同的情况——瑞士在篇均影响力方面排名第二，这表明将计算设计与系统实验验证相结合的研究项目往往会产生极高的学术影响。2020 年后的国际合作努力显著增强。引用和共引分析突出了构成该领域基石的著作，包括关于 AlphaFold2、ProteinMPNN 和 RFdiffusion 的开创性工作。蛋白质设计处于人工智能革命的中心，它将数据库挖掘、计算生成和实验验证纳入了一个日益快速且相互关联的工程循环中。然而，维持这一势头需要面对该领域高被引文献在很大程度上未提及的局限性：在稳定、可结晶结构上训练的模型难以推广到其训练分布之外；静态预测无法反映控制变构和催化的构象动力学；且计算机模拟（in silico）置信度评分已被反复证明难以准确预测湿实验结果。缩小这一差距需要的不是渐进式的改进，而是高通量实验反馈与迭代“设计-测试-学习”周期的持续双向耦合，并由能够原生表示翻译后修饰（PTMs）、细胞环境和构象系综的下一代模型提供支持——这种融合有望将该领域的计算愿景转化为可靠的治疗和合成生物学成果。

## Abstract
Protein design has numerous applications in synthetic biology, drug discovery, and bioengineering. Recently, there has been a revolution in this field due to the emergence of artificial intelligence. At the forefront are deep learning models (DLMs). The impact of these models on the design pipeline is so transformative that it leads to radical advances in prediction accuracy, functional enrichment, and de novo synthesis of proteins. We performed bibliometric analysis on a Web of Science data-set (2006-2025) obtained through a targeted keyword search. Our analysis method orchestrated the use of standard tools such as CiteSpace and VOSviewer for co-citation, keyword co-occurrence, and burst detection, while we used custom python scripts to generate more nuanced plots for collaboration networks and intellectual overlap. Based on the bibliometric analysis, we observe a sudden jump in publication counts after the year 2018. This period also coincides with the publication of many methodological breakthroughs such as AlphaFold2 and RoseTTAFold. The analysis revealed three major intellectual clusters focused around protein structure prediction, directed evolution, and de novo design of proteins. DLMs play a major role in the publication impact of generating functional protein sequences, with frameworks such as ProteinMPNN having a notable citation footprint. Although China and the United States dominated in raw publication volume, citation impact told a different story-Switzerland ranked second in per-publication influence, suggesting that research programs combining computational design with systematic experimental validation tend to generate disproportionate scholarly impact. International collaborative efforts were notable after 2020. Citation and co-citation analysis highlighted works that have formed the bedrock of this field. Notable mentions include seminal works on AlphaFold2, ProteinMPNN, and RFdiffusion. Protein design stands at the center of an AI revolution that has drawn database mining, computational generation, and experimental validation into an increasingly rapid and interconnected engineering loop. Yet sustaining this momentum requires confronting limitations that the field's most cited literature has largely left unspoken: models trained on stable, crystallizable structures struggle to generalize beyond their training distributions, static predictions remain blind to the conformational dynamics governing allostery and catalysis, and in silico confidence scores have repeatedly proven poor predictors of wet-lab outcomes. Closing this gap will demand not incremental refinement but the sustained, bidirectional coupling of high-throughput experimental feedback with iterative design-test-learn cycles, supported by next-generation models that natively represent PTMs, cellular context, and conformational ensembles-a convergence that holds genuine promise for translating the field's computational ambitions into reliable therapeutic and synthetic biology outcomes.

---

## 论文详细总结（自动生成）

这是一篇关于**人工智能驱动蛋白质设计**领域的文献计量学综述研究。它通过大数据分析，梳理了过去 20 年该领域是如何从“缓慢爬行”进化到“爆发式增长”的。

### 1. 这篇论文到底在解决什么问题，为什么值得看？
*   **解决的问题**：蛋白质设计领域发展极快，AI 模型层出不穷。研究者需要知道：这个领域的“技术地图”长什么样？哪些论文是真正的基石？哪些方向是现在的热点，哪些又是尚未解决的深坑？
*   **价值**：它不是一篇技术细节论文，而是一本“行业指南”。对于 AI 研究者来说，它可以帮你快速定位该领域的核心玩家（国家、机构、模型），并看清从“结构预测”到“生成式设计”的演进逻辑。

### 2. 白话版概述
*   过去 20 年，AI 彻底重塑了蛋白质设计，尤其是 2018 年后，论文数量因 AlphaFold2 等突破而出现“断层式”激增。
*   研究重心已经从“预测蛋白质长什么样”转向了“直接设计自然界不存在的新蛋白质”。
*   虽然中美两国在论文产量上领先，但瑞士等国的研究在“实验验证”结合方面做得更好，单篇论文影响力更高。
*   目前的 AI 模型虽然在电脑上跑分很高，但在真实的实验室环境（湿实验）中经常失效，这是目前最大的瓶颈。

### 3. 方法部分：核心思想与流程
*   **核心思想**：利用**文献计量学（Bibliometric Analysis）**，通过分析数千篇论文的引用关系、关键词频率和作者网络，量化领域的发展趋势。
*   **分析流程**：
    1.  **数据抓取**：从 Web of Science 数据库提取 2006-2025 年间的相关文献。
    2.  **工具链**：使用 CiteSpace 和 VOSviewer 进行共引分析（看谁引用了谁）和关键词聚类；使用 Python 脚本处理复杂的协作网络。
    3.  **维度划分**：从发文量、国家影响力、核心技术集群、突发关键词（Burst Detection）四个维度进行挖掘。
*   **关键取舍**：研究不仅关注“谁发的论文多”，更关注“谁的论文被引用得深”，从而识别出像 ProteinMPNN 这样具有统治地位的底层框架。

### 4. 实验部分：数据与主要结果
*   **数据范围**：2006 年至 2025 年（含部分在线发表）的全球科研论文。
*   **核心发现**：
    *   **三大技术集群**：
        1.  **结构预测**（如 AlphaFold2）：解决“已知序列求结构”的问题。
        2.  **定向进化**（模拟自然选择）：通过反复突变和筛选来优化蛋白。
        3.  **从头设计**（De Novo Design）：利用生成式 AI（如 RFdiffusion）从零开始构建新蛋白。
    *   **关键节点**：2018 年是分水岭。AlphaFold2、RoseTTAFold、ProteinMPNN 和 RFdiffusion 被识别为该领域的四大支柱。
    *   **地理分布**：中国和美国是产出大户，但瑞士在“篇均引用率”上表现惊人，反映了其在计算与实验结合上的深度。

### 5. 资源与算力
*   **文中未充分披露**。由于本文是文献计量学研究，不涉及具体模型的训练过程，因此未提及算力消耗。

### 6. 真正可信的贡献与强证据结论
*   **量化了技术转型**：证据显示，研究热点已从早期的“物理化学模拟”全面转向“深度学习生成”。
*   **识别了核心工具链**：明确了 ProteinMPNN 在生成功能性序列中的核心地位。
*   **揭示了“影响力错位”**：高产出并不等同于高影响力，强调了**实验验证（Wet-lab validation）**才是提升论文含金量的关键。

### 7. 局限与风险
*   **数据滞后性**：文献计量基于已发表论文，对于正在发生的、尚未发表的最新 AI 突破（如最新的多模态大模型）存在感知延迟。
*   **静态模型的局限**：论文指出，目前大多数高引模型是基于“静态晶体结构”训练的，无法处理蛋白质的**动态构象**（蛋白质在生物体内是不断扭动的）。
*   **泛化风险**：AI 模型在训练集之外的表现往往较差，且计算机给出的“置信度评分”与实验室真实的“功能活性”之间存在严重脱节。
*   **环境缺失**：现有模型大多忽略了**翻译后修饰（PTM）**（蛋白合成后的化学加工）和复杂的细胞环境。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：准备进入蛋白质设计领域的 AI 算法工程师，以及寻找“AI+生物”落地场景的创业者。
*   **后续可跟进的问题**：如何开发能够原生支持“动态构象”和“细胞上下文环境”的下一代生成模型？如何建立更高效的“设计-测试-学习”闭环，减少对昂贵湿实验的依赖？

（完）
