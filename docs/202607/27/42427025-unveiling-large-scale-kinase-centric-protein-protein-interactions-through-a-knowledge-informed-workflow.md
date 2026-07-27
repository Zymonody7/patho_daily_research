---
title: Unveiling Large-Scale Kinase-Centric Protein-Protein Interactions through a Knowledge-Informed Workflow.
title_zh: 通过知识引导的工作流揭示大规模以激酶为中心的蛋白质-蛋白质相互作用
authors: "Jinyuan Hu, Shimian Li, Yue Xue, Yijie Xia, Sirui Liu, Yi Qin Gao"
date: 2026-07-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42427025/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 利用大语言模型解析文献证据以进行蛋白质相互作用建模
tldr: 针对蛋白质磷酸化中激酶-底物特异性结构数据稀缺、深度学习预测器对磷酸化位点不敏感的问题，该研究提出了一种基于贝叶斯推理的知识驱动工作流。通过大语言模型提取文献证据并转化为结构约束，引导深度学习模型 GRASP 生成高分辨率结构。在 EGFR 等激酶上验证了 336 个新候选结构，并结合 AlphaMissense 揭示了突变致病性与相互作用界面的关联，为激酶特异性研究和药物研发提供了高通量工具。
selection_source: fresh_fetch
motivation: 现有的深度学习模型难以捕捉磷酸化位点级别的底物特异性，且缺乏足够的原子级结构数据来理解激酶与底物的相互作用。
method: 将激酶-底物建模转化为贝叶斯推理问题，利用大语言模型提取生物学知识作为约束条件，引导 GRASP 模型进行结构预测并辅以分子动力学优化。
result: 成功预测了 EGFR、BRAF 和 JNK1 的 336 个磷酸化位点特异性结构，并通过虚拟肽阵列扫描揭示了识别位点与临床致病突变的关联。
conclusion: 该工作流实现了高分辨率、高通量的激酶-底物相互作用建模，为理解信号传导机制和精准药物设计提供了新路径。
---

## 摘要
蛋白质磷酸化调节信号传导，但由于结构数据稀疏以及深度学习预测器对磷酸化位点不敏感，原子水平的底物特异性仍难以捉摸。在这里，我们提出了一种将激酶-底物建模重新表述为贝叶斯推理问题的流水线。通过整合经过策划的数据集和由大语言模型解析的文献证据，我们将多样的生物学知识转化为约束引导的深度学习模型 GRASP 的结构约束。针对 EGFR、BRAF 和 JNK1，我们获得了 336 个经过分子动力学优化的新型磷酸化位点特异性结构候选物。这些模型重现了已知特征（如 JNK1 的疏水对接槽），并支持虚拟位置扫描肽阵列 (V-PSPA) 来绘制识别斑块并推导序列偏好。将预测的界面与 AlphaMissense 致病性评分进行交叉引用，结果表明相互作用类型以及与催化口袋的距离显著影响致病性评分。与临床突变数据集的比较进一步将致病突变与激酶-底物界面联系起来。这种高分辨率、高通量的流水线可广泛应用于激酶特异性研究和通用药物研发。

## Abstract
Protein phosphorylation regulates signaling, yet atomic-level substrate specificity remains elusive due to sparse structural data and phosphorylation-site-insensitive deep-learning predictors. Here we present a pipeline reformulating kinase-substrate modeling as a Bayesian inference problem. By integrating curated data sets and literature evidence parsed by Large Language Models, we converted diverse biological knowledge into structural restraints for the restraint-guided deep-learning model GRASP. For EGFR, BRAF and JNK1, we obtained 336 new phosphorylation-site-specific structure candidates refined by molecular dynamics. These models recapitulate known features, such as JNK1's hydrophobic docking groove, and enabled a Virtual Position Scanning Peptide Array (V-PSPA) to map recognition patches and derive sequence preferences. Cross-referencing predicted interfaces with AlphaMissense pathogenicity scores reveal that the interaction types and distances to the catalytic pocket significantly influence pathogenicity scores. A comparison with clinical mutation data sets further connects pathogenic mutations to the kinase-substrate interface. This high-resolution, high-throughput pipeline can be broadly applicable to kinase specificity studies and general drug discovery.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种结合大语言模型（LLM）和深度学习结构预测工具的新型工作流，旨在解决生物信号传导中一个核心难题：**激酶（Kinase）是如何精确识别并结合其底物（Substrate）的。**

以下是该研究的详细总结：

### 1. 核心问题：为什么这项研究值得关注？
在细胞内，激酶像“开关”一样通过磷酸化（给蛋白质加上磷酸基团）来传递信号。虽然我们知道很多激酶-底物对，但由于实验测定蛋白质复合体结构非常困难，**绝大多数相互作用的原子级细节是缺失的**。
*   **现有 AI 的局限：** 像 AlphaFold 这样的模型在预测单体结构上很强，但在预测激酶-底物这种“瞬时相互作用”时效果较差，且无法区分同一个蛋白质上不同磷酸化位点的细微差别。
*   **价值：** 搞清楚这些界面，就能理解癌症突变是如何破坏信号传导的，并为开发更高选择性的药物提供靶点。

### 2. 白话版概述
想象激酶是一个“印章”，底物是被盖章的“文件”。目前 AI 知道印章和文件长什么样，但不知道印章盖在文件的哪个精确位置。这篇论文找来一个“AI 秘书”（LLM）阅读了大量生物学文献，把科学家以前发现的零散线索（比如“A 零件靠近 B 零件”）收集起来。然后，这些线索被当作“强制约束条件”输入给结构预测模型，强迫 AI 按照已知事实来“拼图”。最终，研究者成功还原了数百个精确的“盖章”瞬间，并发现这些接触点上的突变往往就是导致疾病的元凶。

### 3. 方法部分：知识引导的贝叶斯推理
*   **核心思想：** 将结构预测建模为一个**贝叶斯推理问题**。即：在已知生物学知识（先验）的条件下，寻找概率最大的结构构象。
*   **工作流设计：**
    1.  **知识提取（LLM）：** 使用大语言模型从 PubMed 文献和数据库中自动抓取关于激酶-底物相互作用的实验证据（如：哪些氨基酸残基靠得近）。
    2.  **约束转化：** 将这些文本信息转化为空间距离约束（Restraints）。
    3.  **结构生成（GRASP）：** 使用 **GRASP** 模型（一种支持物理约束引导的深度学习结构预测工具），在约束条件下生成激酶-底物复合体模型。
    4.  **动力学优化（MD）：** 利用分子动力学模拟对生成的结构进行“精修”，确保原子位置在物理上是稳定的。
    5.  **虚拟扫描（V-PSPA）：** 在得到的结构基础上，进行计算机模拟的氨基酸替换，预测激酶对不同序列的偏好性。

### 4. 实验部分：从结构到临床
*   **研究对象：** 选取了 EGFR（表皮生长因子受体）、BRAF 和 JNK1 三种与癌症和炎症密切相关的核心激酶。
*   **数据规模：** 生成了 **336 个** 新型的磷酸化位点特异性复合体结构。
*   **主要结果：**
    *   **验证：** 预测结构成功重现了已知的生物学特征，例如 JNK1 的疏水对接槽（Docking Groove）。
    *   **致病性关联：** 研究者将预测的相互作用界面与 **AlphaMissense**（谷歌预测的突变致病性评分）对比，发现距离激酶催化口袋越近、相互作用越强的位点，其突变致病性评分显著更高。
    *   **临床验证：** 通过对比临床突变数据库，证实了许多致病突变恰好位于预测的激酶-底物接触界面上，解释了这些突变如何通过干扰蛋白质相互作用致病。

### 5. 资源与算力
*   **文中未充分披露**具体的 GPU 型号和总计算耗时。但考虑到涉及大规模分子动力学（MD）精修和 GRASP 推理，该工作流需要相当规模的 GPU 集群支持。

### 6. 真正可信的贡献
*   **方法论创新：** 成功展示了如何将 LLM 提取的“非结构化知识”转化为“硬性结构约束”，解决了纯数据驱动模型在稀缺数据场景下的无力感。
*   **高分辨率图谱：** 提供了 EGFR 等关键激酶的大规模位点特异性结构模型，这对于理解信号转导的特异性具有重要参考价值。
*   **突变解释力：** 强有力的证据表明，结合界面几何特征可以作为预测临床突变后果的重要指标。

### 7. 局限与风险
*   **知识偏差：** LLM 提取的信息如果来源于错误的文献或存在“幻觉”，会直接导致生成的结构错误。
*   **动态性不足：** 激酶-底物结合通常是高度动态的，静态的结构模型（即使经过 MD 优化）可能无法完全捕捉到真实的构象转换。
*   **外推限制：** 该方法高度依赖“已有证据”。对于那些完全没有研究过的、没有任何文献记载的新型激酶，该工作流的效力会大打折扣。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事蛋白质相互作用（PPI）预测、药物设计、以及试图将多模态数据（文本+结构）融合的研究者。
*   **后续可跟进的问题：** 如何在没有文献证据的情况下，利用无监督学习或迁移学习自动发现这些潜在的结构约束？

（完）
