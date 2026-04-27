---
title: "Suppressing viral assembly in human metapneumovirus by targeting fusion protein with natural compounds: a structural dynamics and energetics study."
title_zh: 通过天然化合物靶向融合蛋白抑制人类偏肺病毒组装：结构动力学与能量学研究
authors: "Amit Dubey, Manish Kumar, Aisha Tufail"
date: 2026-04-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/42043606/"
tags: ["query:pathoai"]
score: 8.0
evidence: 病毒靶点识别和治疗设计的计算框架
tldr: 针对人类偏肺病毒（HMPV）缺乏特效药的问题，本研究利用虚拟筛选、分子动力学模拟和密度泛函理论，从天然化合物库中筛选出能抑制病毒融合蛋白（F蛋白）的候选药物。结果发现表没食子儿茶素没食子酸酯（EGCG）、芦丁和槲皮素具有极强的结合亲和力和结构稳定性，优于临床药物利巴韦林，为开发新型抗HMPV药物提供了计算依据。
selection_source: fresh_fetch
motivation: 人类偏肺病毒（HMPV）是导致严重呼吸道感染的重要病原体，但目前临床上仍缺乏针对其融合蛋白的特效抗病毒药物。
method: 采用集成计算框架，结合虚拟筛选、1000纳秒分子动力学模拟、MM-GBSA自由能计算及密度泛函理论（DFT），对天然化合物与HMPV F蛋白的相互作用进行多尺度评估。
result: 筛选出的EGCG、芦丁和槲皮素在结合能、氢键形成及结构稳定性方面均优于对照药物利巴韦林，且具有良好的药代动力学特性。
conclusion: EGCG等天然化合物是极具潜力的HMPV融合蛋白抑制剂，为后续实验验证和抗病毒药物研发奠定了理论基础。
---

## 摘要
背景：人类偏肺病毒（HMPV）是引起急性下呼吸道感染的重要原因，尤其是在儿童、老年人和免疫功能低下人群中，目前尚无获批的针对性抗病毒疗法。病毒融合（F）糖蛋白的融合前构象（PDB ID: 5WB0）对于膜融合和病毒进入至关重要，是一个具有前景的治疗靶点。本研究系统筛选了一个结构多样的天然化合物库，旨在识别 HMPV F 蛋白的潜在抑制剂。方法：采用了一个结合了虚拟筛选、分子对接、长时程分子动力学（MD）模拟和密度泛函理论（DFT）计算的综合计算框架。使用 AutoDock Vina 进行虚拟筛选和对接，随后进行了严格的结合构象验证。对排名靠前的化合物——表没食子儿茶素没食子酸酯（EGCG）、芦丁和槲皮素——在显式溶剂条件下（TIP3P 水模型，生理离子强度）使用 GROMACS 2022 进行了 1000 ns 的 MD 模拟（重复三次）。通过 MM-GBSA 估算结合自由能，并使用 RMSD、RMSF 和动态互相关矩阵分析残基级动力学。使用 Gaussian 16 在 B3LYP/6-31G(d,p) 水平上评估电子性质，包括 HOMO-LUMO 能隙分析和分子静电势（MEP）图谱。使用 SwissADME、pkCSM 和 ProTox-II 预测药代动力学和毒性特征。结果：对接分析显示，在 F 蛋白的功能结合口袋内，受广泛的氢键、π-π 堆积和范德华相互作用驱动，EGCG、芦丁和槲皮素表现出比对照抗病毒药物利巴韦林更强的结合亲和力。MD 模拟证明了这些复合物具有增强的结构稳定性，其中 EGCG 表现出最低的构象偏差和最有利的结合自由能。相关残基运动分析进一步表明配体诱导了关键功能区域的稳定。DFT 衍生的电子描述符（包括缩小的 HOMO-LUMO 能隙和有利的静电分布）支持了所选化合物的高反应性和结合倾向。ADMET 预测表明其具有可接受的药代动力学特征和较低的预测毒性。结论：本研究确定了 EGCG、芦丁和槲皮素是具有前景的 HMPV 融合蛋白天然抑制剂，并为其结合行为和稳定性提供了机制见解。这些发现为进一步的实验验证和针对 HMPV 的合理抗病毒药物开发提供了坚实的计算基础。

## Abstract
CONTEXT: Human metapneumovirus (HMPV) is a significant cause of acute lower respiratory tract infections, particularly among pediatric, elderly, and immunocompromised populations, with no approved targeted antiviral therapy currently available. The prefusion conformation of the viral fusion (F) glycoprotein (PDB ID: 5WB0) is essential for membrane fusion and viral entry, representing a promising therapeutic target. In this study, a structurally diverse library of natural compounds was systematically screened to identify potential inhibitors of the HMPV F protein. METHODS: An integrated computational framework combining virtual screening, molecular docking, long-timescale molecular dynamics (MD) simulations, and density functional theory (DFT) calculations was employed. Virtual screening and docking were performed using AutoDock Vina, followed by rigorous binding pose validation. The top-ranked compounds-epigallocatechin gallate (EGCG), rutin, and quercetin-were subjected to 1000 ns MD simulations (in triplicate) using GROMACS 2022 with explicit solvent conditions (TIP3P water model, physiological ionic strength). Binding free energies were estimated via MM-GBSA, and residue-level dynamics were analyzed using RMSD, RMSF, and dynamic cross-correlation matrices. Electronic properties were evaluated at the B3LYP/6-31G(d,p) level using Gaussian 16, including HOMO-LUMO gap analysis and molecular electrostatic potential (MEP) mapping. Pharmacokinetic and toxicity profiles were predicted using SwissADME, pkCSM, and ProTox-II. RESULTS: Docking analysis revealed that EGCG, rutin, and quercetin exhibit stronger binding affinities than the reference antiviral ribavirin, driven by extensive hydrogen bonding, π-π stacking, and van der Waals interactions within the functional binding pocket of the F protein. MD simulations demonstrated enhanced structural stability of these complexes, with EGCG showing the lowest conformational deviation and most favorable binding free energy. Correlated residue motion analysis further indicated ligand-induced stabilization of key functional regions. DFT-derived electronic descriptors, including reduced HOMO-LUMO gaps and favorable electrostatic distributions, supported the high reactivity and binding propensity of the selected compounds. ADMET predictions suggested acceptable pharmacokinetic profiles with low predicted toxicity. CONCLUSION: This study identifies EGCG, rutin, and quercetin as promising natural inhibitors of the HMPV fusion protein, providing mechanistic insights into their binding behavior and stability. These findings offer a strong computational foundation for further experimental validation and rational antiviral drug development targeting HMPV.

---

## 论文详细总结（自动生成）

这篇论文利用计算生物学方法，针对**人类偏肺病毒（HMPV）**寻找潜在的药物。HMPV 是一种严重的呼吸道病原体，目前尚无特效药。研究的核心是寻找能“锁死”病毒**融合蛋白（F 蛋白）**的天然化合物，从而阻止病毒进入人体细胞。

### 1. 核心问题与研究价值
*   **解决的问题**：人类偏肺病毒（HMPV）是导致儿童和老人肺炎、支气管炎的主要原因之一，但临床上缺乏针对性的抗病毒药物。
*   **研究价值**：病毒进入细胞依赖其表面的“融合蛋白（F 蛋白）”发生形变。如果能找到一种分子像“胶水”一样粘在 F 蛋白上，就能阻止病毒感染。本研究通过计算机模拟，从天然产物中筛选出了比现有药物效果更好的候选分子，为新药研发节省了大量实验成本。

### 2. 白话版概述
想象病毒是一把试图打开人体细胞大门的“钥匙”，而 F 蛋白就是这把钥匙的关键部位。这项研究利用超级计算机在天然植物成分库中进行“海选”，找到了三种成分（分别来自绿茶、芸香等植物），它们能比目前的临床药物更牢固地卡住这把钥匙。研究人员不仅模拟了它们“卡”得有多紧，还模拟了它们在水中晃动 1000 纳秒（极微观的时间尺度）后是否依然稳固，结果证明这些天然成分非常有潜力。

### 3. 方法部分：核心思想与流程
研究采用了一套**多尺度计算框架**，将宏观的筛选与微观的量子力学分析结合：
*   **虚拟筛选与分子对接（Docking）**：使用 AutoDock Vina 软件，将大量天然化合物分子逐一尝试放入 F 蛋白的结合口袋中，根据能量得分评估谁“贴合”得最紧。
*   **长时程分子动力学模拟（MD Simulation）**：使用 GROMACS 软件进行了 **1000 纳秒（1 微秒）** 的模拟。这在同类研究中属于较长的时间，旨在观察在生理环境下（水溶液、离子浓度、体温），药物分子是否会从蛋白上脱落。
*   **结合自由能计算（MM-GBSA）**：精确计算药物与蛋白结合的“力道”，分解为范德华力、静电力等物理指标。
*   **密度泛函理论（DFT）**：从量子力学层面分析分子的电子云分布（HOMO-LUMO 能隙），判断分子的化学活性和稳定性。
*   **ADMET 预测**：利用 AI 模型预测这些化合物被人体吸收、代谢的情况以及是否有毒。

### 4. 实验部分：数据与结果
*   **目标蛋白**：HMPV 融合蛋白的融合前构象（PDB ID: 5WB0）。
*   **对照组（Baseline）**：利巴韦林（Ribavirin），一种临床常用的广谱抗病毒药物。
*   **主要结果**：
    *   筛选出三个核心候选物：**EGCG（表没食子儿茶素没食子酸酯，绿茶提取物）**、**芦丁（Rutin）**和**槲皮素（Quercetin）**。
    *   **结合力**：EGCG 的结合能显著优于利巴韦林，表现出更强的亲和力。
    *   **稳定性**：在 1000ns 的模拟中，EGCG 与蛋白形成的复合物波动最小（RMSD 曲线平稳），说明结合非常牢固。
    *   **安全性**：预测显示这些天然化合物具有较低的毒性和良好的药代动力学特性。

### 5. 资源与算力
*   **软件工具**：GROMACS 2022（动力学）、Gaussian 16（量子化学）、AutoDock Vina（对接）。
*   **硬件资源**：文中未明确披露具体的 CPU/GPU 核心数或计算集群规模，但提到 MD 模拟进行了三次重复以确保结果可靠。

### 6. 真正可信的贡献
*   **长时程模拟的证据链**：1000ns 的 MD 模拟提供了比常规研究（通常 100-200ns）更具说服力的动态稳定性证据。
*   **多维度验证**：结合了对接、动力学和量子化学（DFT）三个层面的数据，相互印证了 EGCG 等分子的有效性。
*   **靶点明确**：针对 F 蛋白的融合前构象（Prefusion），这是目前公认的开发中和抗体和药物的最佳位点。

### 7. 局限与风险
*   **缺乏湿实验验证**：所有的结论均来自计算机模拟（In silico），尚未在细胞实验（In vitro）或动物实验（In vivo）中验证其真实的抗病毒活性。
*   **生物利用度问题**：天然多酚类化合物（如 EGCG）在人体内往往代谢极快或吸收率低，计算机预测的 ADMET 属性与真实人体环境可能存在偏差。
*   **单一靶点**：仅考虑了对 F 蛋白的物理阻断，未考虑病毒变异可能导致的耐药性。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物筛选、蛋白质-配体相互作用、以及希望将量子化学计算引入药物设计的 AI 研究者。
*   **后续可跟进的问题**：能否利用生成式 AI（如 Diffusion Model 或 GAN）基于 EGCG 的骨架，设计出结合力更强且更易被人体吸收的人工合成衍生物？

（完）
