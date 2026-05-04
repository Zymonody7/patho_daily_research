---
title: Computer-Aided Discovery of Small-Molecule Inhibitors of Pathogenic New World Arenavirus Entry and Replication.
title_zh: 计算机辅助发现致病性新世界沙状病毒进入与复制的小分子抑制剂。
authors: "Samantha Rae Wasson, Ben Matthew Flude, Martina Salerno, Kie Hoon Jung, Gilda Padalino, Salvatore Ferla, Dylan Joseph Roche-Dugmore, Connor W Bott, Andrea Brancale, Brian B Gowen, Marcella Bassetto"
date: 2026-05-04
pdf: "https://pubmed.ncbi.nlm.nih.gov/42077170/"
tags: ["query:pathoai"]
score: 9.0
evidence: 基于结构的病原体病毒抑制剂虚拟筛选
tldr: 针对致病性新世界沙状病毒（NWA）利用人类转铁蛋白受体1（hTfR1）入侵细胞的机制，研究人员通过针对MACV GP1-hTfR1界面的结构虚拟筛选，从商业化合物库中鉴定出两种具有微摩尔活性的骨架。通过类似物优化获得的化合物22f展现出跨病毒种类的广谱抑制活性，虽在小鼠模型中未表现出保护效力，但为开发新型抗沙状病毒药物提供了重要起点。
selection_source: fresh_fetch
motivation: 寻找能够阻断新世界沙状病毒（如Junín和Machupo病毒）通过hTfR1受体入侵宿主细胞的小分子抑制剂。
method: 利用基于结构的虚拟筛选技术针对病毒糖蛋白GP1与受体hTfR1的结合界面进行药物筛选，并对初步命中的骨架进行化学合成优化。
result: 筛选并优化得到了亚微摩尔级别的抑制剂22f，该化合物对多种沙状病毒具有广谱抗病毒活性，且在小鼠实验中表现出良好的耐受性。
conclusion: 尽管候选药物在动物模型中尚未实现保护作用，但该研究验证了针对病毒-受体相互作用开发广谱抗沙状病毒药物的可行性。
---

## 摘要
致病性新世界沙状病毒（NWAs），包括胡宁病毒（JUNV）和马丘波病毒（MACV），依赖于宿主-病毒进入过程，这是抗病毒干预的重要切入点。基于已知几种 NWAs 利用人转铁蛋白受体 1（hTfR1）进入细胞，我们针对 MACV GP1-hTfR1 相互作用界面进行了基于结构的虚拟筛选，以鉴定能够抑制早期感染的小分子。通过对市售类药化合物的计算机筛选，选择了 25 个候选化合物并在细胞实验中进行了测试，得到了两种化学结构截然不同且对 JUNV 具有低微摩尔活性的骨架。对主要化学型的命中化合物进行扩展，产生了 107 个新类似物，其中几种实现了对 JUNV 复制的亚微摩尔级抑制。其中，化合物 22f 在多种沙状病毒中表现出抗病毒活性，包括 hTfR1 嗜性的 NWAs 和使用替代进入途径的病毒，而对无关的裂谷热病毒没有影响。在表达 hTfR1 的 JUNV 感染小鼠模型中，22f 耐受性良好，但未提供保护作用。这些结果为进一步开发和优化能够广泛抑制致病性 NWAs 感染的高效化合物奠定了基础。

## Abstract
Pathogenic New World arenaviruses (NWAs), including Junín (JUNV) and Machupo (MACV) viruses, rely on host-virus entry processes that represent attractive points for antiviral intervention. Guided by the known use of human transferrin receptor 1 (hTfR1) by several NWAs for cell entry, we conducted a structure-based virtual screening campaign targeting the MACV GP1-hTfR1 interaction interface to identify small molecules capable of inhibiting early infection. From an in silico screen of commercially available drug-like compounds, 25 candidates were selected and tested in cell-based assays, yielding two chemically distinct scaffolds with low-micromolar activity against JUNV. Hit expansion of the primary chemotype produced 107 new analogues, several of which achieved submicromolar inhibition of JUNV replication. Among them, compound 22f demonstrated antiviral activity across multiple arenaviruses, including both hTfR1-tropic NWAs and viruses that use alternative entry pathways, while showing no effect on the unrelated Rift Valley fever virus. In an hTfR1-expressing mouse model of JUNV infection, 22f was well tolerated, but did not confer protection. These results provide the foundation for further development and optimization of potent compounds that broadly inhibit infection by the pathogenic NWAs.

---

## 论文详细总结（自动生成）

这篇论文详细介绍了如何利用计算机辅助药物设计（CADD）技术，针对致病性**新世界沙状病毒（New World Arenaviruses, NWAs）**开发新型小分子抑制剂。

### 1. 到底在解决什么问题？
新世界沙状病毒（如胡宁病毒 JUNV、马丘波病毒 MACV）会引起严重的病毒性出血热，致死率高且目前缺乏特效药。这些病毒入侵人体细胞的关键步骤是：病毒表面的**糖蛋白（GP1）**像钥匙一样，插入细胞表面的**转铁蛋白受体 1（hTfR1）**这个锁孔。

本研究的目标是：**寻找一种小分子“塞子”，精准地堵住这个锁孔（或干扰钥匙的插入），从而在源头上阻断病毒感染。**

---

### 2. 白话版概述
*   **背景**：病毒想进细胞，必须先和细胞表面的受体蛋白“握手”。
*   **策略**：研究者用电脑模拟了数百万种化学物质，看谁能最牢固地粘在受体蛋白的“握手位”上。
*   **过程**：通过电脑筛选选出 25 个候选者，在实验室测试后发现两个有潜力的“苗子”，随后对其中一个进行了大规模的化学结构优化（变出了 107 种新版本）。
*   **结果**：最终得到一个代号为 **22f** 的强力化合物，它不仅能对付胡宁病毒，还能防住好几种亲戚病毒。

---

### 3. 方法部分：核心思想与设计
*   **核心思想**：**蛋白质-蛋白质相互作用（PPI）抑制**。由于病毒 GP1 和宿主 hTfR1 的结合界面很大且相对平坦，传统药物很难找到“抓手”，研究者利用基于结构的虚拟筛选来寻找能嵌入关键缝隙的小分子。
*   **工作流程**：
    1.  **靶点确定**：利用已知的 MACV GP1 与 hTfR1 结合的晶体结构（PDB ID: 3KAS），锁定受体上与病毒接触的关键氨基酸残基。
    2.  **虚拟筛选（In silico screening）**：从商业化合物库中筛选符合“类药性”的分子，利用分子对接（Docking）软件计算每个分子与受体结合的能量。
    3.  **命中与优化**：初步筛选出 25 个分子进行细胞实验，发现两个活性骨架。随后通过**药物化学手段**，对表现最好的骨架进行“修剪”和“加装”化学基团（Hit-to-Lead 优化），合成了 107 个类似物。
*   **关键取舍**：研究者没有选择直接攻击病毒蛋白（病毒易突变），而是选择攻击宿主受体 hTfR1。这种策略的优点是病毒很难通过单点突变产生耐药性，且具有广谱潜力。

---

### 4. 实验部分：结果与评价
*   **实验数据与任务**：
    *   **体外实验**：在 Vero 细胞中测试化合物对 JUNV 病毒复制的抑制能力。
    *   **广谱性测试**：测试对 MACV、GTOV（瓜纳里托病毒）等其他沙状病毒的有效性。
*   **评价指标**：
    *   **$EC_{50}$**：半数有效浓度（越低代表药效越强）。
    *   **$CC_{50}$**：半数细胞毒性浓度（越高代表对正常细胞越安全）。
*   **主要结果**：
    *   化合物 **22f** 表现最突出，对 JUNV 的抑制活性达到了**亚微摩尔级别**（$EC_{50} < 1 \mu M$）。
    *   **广谱性验证**：22f 不仅能阻断依赖 hTfR1 受体的病毒，甚至对某些使用其他进入途径的沙状病毒也有一定抑制作用，暗示其可能存在多重抗病毒机制。
    *   **特异性**：对无关的裂谷热病毒（RVFV）无效，证明不是盲目杀伤。

---

### 5. 资源与算力
*   **文中未充分披露**。论文提到了使用 Glide (Schrödinger 软件包) 进行分子对接，但未说明具体的硬件配置（如 CPU/GPU 核心数）或总计算耗时。

---

### 6. 真正可信的贡献
*   **验证了 PPI 靶点的可行性**：证明了通过小分子干扰病毒-受体这种巨大的蛋白质界面是可行的。
*   **发现了广谱骨架**：22f 展示了跨病毒种类的抑制活性，这为开发“一种药治一类病”的广谱抗病毒药物提供了重要线索。
*   **证据强度**：体外细胞实验数据非常扎实，包含了大量的类似物对比（SAR 研究），清晰展示了化学结构改变如何影响药效。

---

### 7. 局限与风险
*   **动物实验“翻车”**：虽然 22f 在细胞里表现完美，但在小鼠感染模型中**没有表现出保护作用**。
    *   *风险分析*：可能是因为该化合物在生物体内的代谢太快（药代动力学性质差），或者在血液中与血浆蛋白结合太紧，导致无法到达感染部位。
*   **PPI 抑制的固有难度**：小分子与平坦的蛋白质界面结合力通常不如嵌入深口袋的结合力稳固，这限制了其在复杂体内环境中的表现。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事**蛋白质界面配体设计**、**分子生成模型**、以及**虚拟筛选算法开发**的 AI 研究者。
*   **后续可跟进的问题**：
    1.  **AI 优化 PPI 预测**：能否利用深度学习（如几何深度学习）更准确地预测这种“平坦界面”上的结合位点，从而提高虚拟筛选的命中率？
    2.  **多目标优化**：在 AI 生成分子时，如何同时考虑“抑制活性”和“体内药代动力学性质（PK）”，以避免出现“体外有效、体内无效”的情况？

（完）
