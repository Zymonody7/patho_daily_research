---
title: CRISPR-Cas9-Mediated Upregulation of Utrophin Ameliorates Duchenne Muscular Dystrophy.
title_zh: CRISPR-Cas9 介导的 Utrophin 上调可改善杜氏肌营养不良症
authors: "Maëlle Ralu, Simon Guiraud, Sumitava Dastidar, Paola Galbiati, Emilia Sadaoui, Fetta Mazed, Fatima Amor, Anne de Cian, Isabelle Richard, Kamel Mamchaoui, Giuseppe Ronzitti, Francesco Saverio Tedesco, Mario Amendola"
date: 2026-03-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/41877484/"
tags: ["query:bioinfo"]
score: 8.0
evidence: 用于治疗性上调的CRISPR-Cas9引导设计和基因组编辑
tldr: 杜氏肌营养不良症（DMD）因抗肌萎缩蛋白缺失导致，上调其同源蛋白 Utrophin 是潜在疗法。本研究利用 CRISPR-Cas9 技术破坏 UTRN 基因上的 Let-7c 微 RNA 抑制位点，通过产生插入/缺失突变解除表达抑制。实验证明该方法在 3D 人类骨骼肌模型和 mdx 小鼠中均能显著提升 Utrophin 表达，改善肌肉收缩功能和病理特征，为 DMD 提供了一种不依赖特定突变类型的通用基因编辑策略。
selection_source: fresh_fetch
motivation: 针对杜氏肌营养不良症（DMD），探索一种不依赖于患者具体基因突变类型的通用型 Utrophin 蛋白补偿疗法。
method: "使用 CRISPR-Cas9 系统靶向并破坏 UTRN 基因 3' UTR 区域的 Let-7c 微 RNA 结合位点，从而解除对 Utrophin 表达的抑制。"
result: 该策略在人类 3D 肌肉模型和 mdx 小鼠中成功诱导了 Utrophin 的持续上调，并显著改善了肌肉的钙离子调节、收缩力及组织病理表现。
conclusion: 证明了通过基因编辑手段上调 Utrophin 是一种安全、有效且具有普适性的 DMD 治疗新路径。
---

## 摘要
杜氏肌营养不良症（DMD）是一种由于抗肌萎缩蛋白（dystrophin）缺失引起的致死性神经肌肉疾病。上调 dystrophin 的旁系同源蛋白 utrophin 是一种极具前景的基因治疗方法。在此，我们提出了一种基于 CRISPR-Cas9 的策略，通过破坏抑制因子结合位点来增强 utrophin 的表达。利用 Cas9/gRNA 核糖核蛋白复合物，我们在 DMD 成肌细胞中破坏了数个此类位点，并确定 micro-RNA Let-7c 结合位点在解除 UTRN 基因抑制方面非常有效。有趣的是，Cas9 产生的插入缺失（indels）在提高 UTRN 表达方面与完全移除 Let-7c 结合位点同样有效，且脱靶效应极小。在 DMD 的三维组织工程人类骨骼肌模型中，该编辑策略导致了显著的 utrophin 上调，并改善了钙失调和肌肉收缩功能。最后，在 mdx 小鼠中，局部或全身递送编码 Cas9 和针对 Let-7c 结合位点 gRNA 的重组腺相关病毒，实现了 utrophin 的上调，并改善了肌肉组织病理学和功能。这些发现为一种不依赖于突变、具有潜在普适性的 DMD 基因编辑治疗策略奠定了基础。

## Abstract
Duchenne muscular dystrophy is a lethal neuromuscular disorder caused by loss of dystrophin. Upregulating utrophin, a dystrophin paralogue, is a promising gene therapy approach. Here, we present a CRISPR-Cas9-based strategy to enhance utrophin expression by disrupting repressor binding sites. Using a Cas9/gRNA ribonucleoprotein complex we disrupted several such sites in DMD myoblasts and identified micro-RNA Let-7c binding site as effective in relieving repression of the UTRN gene. Interestingly, Cas9-generated indels were as effective as the complete removal of Let-7c binding site in upregulating UTRN expression, with minimal off-target effects. In a three-dimensional tissue-engineered human skeletal muscle model of DMD, this editing strategy resulted in significant utrophin upregulation and functional improvements of calcium dysregulation and muscle contraction. Finally, in mdx mice, local or systemic delivery of recombinant adeno-associated viruses encoding Cas9 and gRNA targeting the Let-7c binding site resulted in utrophin upregulation and amelioration of muscle histopathology and function. These findings provide the foundations for a mutation-independent, potentially universal gene editing therapeutic strategy for DMD.

---

## 论文详细总结（自动生成）

### 1. 这篇论文到底在解决什么问题，为什么值得看？

**核心问题：** 杜氏肌营养不良症（DMD）是一种严重的遗传病，患者因为基因突变无法产生“抗肌萎缩蛋白（Dystrophin）”，导致肌肉萎缩并最终死亡。目前的基因疗法大多试图修复特定突变或导入缩减版的基因，但存在适用范围窄（不同患者突变位置不同）或蛋白功能不全的问题。

**研究价值：** 论文提出了一种“曲线救国”的通用方案。人体内有一种和 Dystrophin 功能非常相似的蛋白叫 **Utrophin（尿囊素蛋白）**。正常情况下，Utrophin 只在胎儿期或肌肉修复时大量表达，成年后会被一些“刹车分子”（如 microRNA）抑制。这篇论文利用 CRISPR 技术把这个“刹车”拆掉，让肌肉持续产生 Utrophin 来替代缺失的 Dystrophin。这种方法**不依赖患者具体的突变类型**，对所有 DMD 患者理论上都有效。

---

### 2. “白话版”概述

DMD 患者的肌肉像是一座缺少关键支柱（Dystrophin）的建筑。虽然人体自带一套备用支柱（Utrophin），但平时被一种叫 Let-7c 的微小 RNA 分子给“锁”住了，不让多产。研究人员用 CRISPR-Cas9 基因编辑技术，精准地在 Utrophin 基因的“锁孔”（结合位点）上剪了一刀，造成一点点破坏（突变）。结果，“锁”挂不上了，备用支柱 Utrophin 开始大量产生，成功稳固了肌肉结构，改善了小鼠和人类 3D 肌肉模型的运动功能。

---

### 3. 方法部分：核心思想与设计

*   **核心思想：** 靶向抑制。不修复受损基因，而是通过破坏基因组上的**顺式作用元件**（3' UTR 区域的抑制因子结合位点）来解除表达抑制。
*   **靶点筛选：** 研究者测试了多个潜在的抑制位点，最终锁定在 **Let-7c 微 RNA 结合位点**。实验发现，只要在这里产生微小的插入或缺失（Indels），就足以让 Let-7c 无法识别并结合，从而大幅提升 Utrophin 产量。
*   **递送系统：**
    *   **体外实验：** 使用核糖核蛋白复合物（RNP，即 Cas9 蛋白直接包裹 gRNA）电转入细胞。
    *   **体内实验：** 使用**腺相关病毒（AAV）**作为载体，将编码 Cas9 和 gRNA 的序列送入 $mdx$ 小鼠（DMD 模拟小鼠）的肌肉中。
*   **关键取舍：** 研究者发现，简单的单切割产生的随机突变（Indels）效果竟然和昂贵的片段删除一样好。这意味着治疗时不需要同时使用两个 gRNA 进行大片段切割，降低了基因编辑的复杂度和潜在风险。

---

### 4. 实验部分：验证与结果

*   **实验对象：**
    1.  **DMD 患者来源的成肌细胞：** 验证编辑效率和蛋白上调倍数。
    2.  **3D 组织工程人类骨骼肌（Bioengineered Muscle）：** 模拟真实肌肉环境，测试收缩力和钙离子调节（肌肉兴奋收缩的关键）。
    3.  **$mdx$ 小鼠模型：** 进行局部（肌肉注射）和全身（静脉注射）给药。
*   **评价指标：** Utrophin 表达量（Western Blot/免疫荧光）、肌肉收缩力、血清肌酸激酶（衡量肌肉损伤的指标）、组织病理学切片。
*   **主要结果：**
    *   编辑后的细胞中 Utrophin 显著增加。
    *   3D 肌肉模型显示，编辑后肌肉的收缩力明显增强，钙离子代谢恢复正常。
    *   $mdx$ 小鼠在接受 AAV 治疗后，肌肉炎症减轻，纤维化减少，运动能力得到改善。
    *   **脱靶分析：** 深度测序显示，在预测的脱靶位点未发现明显的非预期编辑，安全性较高。

---

### 5. 资源与算力

*   **文中未充分披露。** 论文主要侧重于湿实验（分子生物学、细胞生物学和动物实验），涉及的生物信息学分析主要是常规的 CRISPR 脱靶预测和深度的扩增子测序分析，未提及大规模计算集群或特殊 AI 模型训练资源。

---

### 6. 真正可信的贡献

1.  **确定了 Let-7c 位点的关键性：** 证明了通过破坏单个微 RNA 结合位点即可实现治疗级别的蛋白上调。
2.  **验证了 Indels 的有效性：** 证明了不需要精确修复或大片段删除，随机的非同源末端连接（NHEJ）修复产生的突变就足够有效，这极大地简化了临床转化路径。
3.  **多模型验证：** 从细胞到 3D 人类肌肉组织再到活体动物，证据链完整，功能改善数据（收缩力提升）非常扎实。

---

### 7. 局限与风险

*   **长期安全性：** AAV 载体在人体内可能引发免疫反应，且 Cas9 蛋白的长期表达可能存在潜在的基因组稳定性风险。
*   **上调幅度上限：** 虽然 Utrophin 增加了，但其功能是否能 100% 替代原生的 Dystrophin 仍有争议（通常认为能缓解症状，但难以完全治愈）。
*   **递送效率：** 全身给药时，如何让病毒高效进入全身所有肌肉（尤其是横膈肌和心肌）仍是基因治疗的共性难题。

---

### 8. 对 AI for Bioinformatics 的启发

*   **适合关注的人群：** 从事**非编码区（Non-coding region）功能预测**、**CRISPR 靶点优化**以及**调控元件发现**的 AI 研究者。
*   **后续可跟进的问题：** 能否利用深度学习模型（如 Transformer 变体）扫描整个基因的非编码区，自动寻找比 Let-7c 更高效、更安全的“抑制开关”？或者预测不同个体在编辑该位点后，产生哪种 Indel 序列对蛋白上调的效果最稳定？

（完）
