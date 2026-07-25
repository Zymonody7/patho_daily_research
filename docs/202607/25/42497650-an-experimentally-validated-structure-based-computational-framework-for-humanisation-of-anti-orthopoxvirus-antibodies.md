---
title: An experimentally validated structure-based computational framework for humanisation of anti-orthopoxvirus antibodies.
title_zh: 一种经实验验证的基于结构的人源化抗正痘病毒抗体计算框架
authors: "Xuehua Yang, Xuemeng Dong, Jiahan Lu, Xiaojing Chi, Xiuying Liu, Huarui Duan, Peixiang Gao, Jing Xue, Wei Yang"
date: 2026-07-24
pdf: "https://pubmed.ncbi.nlm.nih.gov/42497650/"
tags: ["query:pathoai"]
score: 8.0
evidence: 抗正痘病毒抗体设计的计算框架
tldr: "针对正痘病毒（如猴痘）重现带来的公共卫生威胁，传统基于序列的人源化方法易导致抗体活性下降。本研究开发了一种以3D结构一致性为核心的计算人源化框架，利用Foldseek结构比对和界面残基约束，成功将两种鼠源抗体改造为POX1.1和POX2.1。实验证明，这些抗体在保持高结构相似性的同时，联合用药使感染病毒的小鼠生存率达100%，为抗病毒药物研发提供了高效的结构导向新方案。"
selection_source: fresh_fetch
motivation: 旨在克服传统序列人源化方法导致抗体结合力受损的问题，并降低鼠源抗体在临床应用中的免疫原性风险。
method: 开发了一种集成Foldseek结构比对与界面残基约束的计算框架，优先保证抗体3D结构的构象一致性而非单纯的序列相似度。
result: 人源化抗体POX1.1和POX2.1在小鼠模型中展现出极强的中和活性，联合治疗可完全保护受致死剂量病毒感染的小鼠并抑制病毒扩散。
conclusion: 该研究证明了基于结构的计算框架能高效实现抗体人源化，为应对正痘病毒大流行提供了经过实验验证的候选药物和开发工具。
---

## 摘要
背景：正痘病毒（尤其是猴痘病毒，MPXV）的再次出现构成了日益严重的全球公共卫生威胁。表征良好的鼠源抗正痘病毒抗体在临床上受到抗鼠抗体反应的限制，而传统的基于序列的人源化方法往往会损害抗原结合活性。方法：我们开发了一个经实验验证的结构指导计算人源化框架，该框架优先考虑3D结构一致性而非序列一致性，并集成了基于Foldseek的结构比对和界面残基约束。我们将该框架应用于两种鼠源抗正痘病毒抗体（7D11, A27D7）的人源化，并进行了全面的体内外验证。结果：结构叠加证实了人源化变体（POX1.1和POX2.1）与其亲本单克隆抗体之间具有高度的构象保守性，所有可变区的均方根偏差（RMSD）值均低于0.6 Å。两种人源化变体均保留了完整的表位特异性，并具有天然的人源化特征。与亲本7D11相比，POX1.1对牛痘病毒（VACV）和MPXV显示出增强的中和效力。POX2.1保留了亲本A27D7的广泛交叉反应性结合能力和细胞外包膜病毒（EEV）中和活性。在致死性VACV小鼠模型中，两种单药疗法均提供了显著的预防和治疗保护，降低了肺部病毒载量并提高了存活率。与单一抗体相比，POX1.1和POX2.1的双靶点联合用药显著提高了体内疗效，即使在挑战后2天给药，存活率仍达100%。在MPXV CAST/EiJ小鼠模型中，该联合疗法显著减轻了脾肿大，降低了血浆、脾脏和肺组织中的MPXV DNA载量，有效抑制了病毒的全身扩散。结论：这些发现表明，以结构为中心的流程能够实现表征良好的鼠源抗正痘病毒抗体的高效人源化，为支持正痘病毒大流行的应对措施开发提供了一个经过验证的框架。资助：本研究得到了国家自然科学基金、中国医学科学院医学科学创新基金、青年教师科研创新能力支持项目和国家科技重大专项的支持。

## Abstract
BACKGROUND: The re-emergence of orthopoxviruses, most notably mpox virus (MPXV), poses a growing global public health threat. Well-characterised murine anti-orthopoxvirus antibodies are clinically limited by anti-mouse antibody responses, while traditional sequence-based humanisation often impairs antigen-binding activity. METHODS: We developed an experimentally validated structure-guided computational humanisation framework prioritising 3D architectural congruence over sequence identity, integrating Foldseek-based structural alignment and interface-residue constraints. We applied this framework to humanise two murine anti-orthopoxvirus antibodies (7D11, A27D7), with comprehensive in vitro and in vivo validation. FINDINGS: Structural superimposition confirmed high conformational conservation between the humanised variants (POX1.1 and POX2.1) and their parental mAbs, with root mean square deviation (RMSD) values below 0.6 Å for all variable domains. Both humanised variants retained full epitope specificity with natural humanness profiles. POX1.1 showed enhanced neutralisation potency against vaccinia virus (VACV) and MPXV, compared with the parental 7D11. POX2.1 preserved the broad cross-reactive binding and the extracellular enveloped virion neutralising activity of the parental A27D7. In the lethal VACV mouse model, both monotherapies conferred significant prophylactic and therapeutic protection, reducing pulmonary viral loads and improving survival. The dual-targeting combination of POX1.1 and POX2.1 achieved markedly improved in vivo efficacy compared with individual antibodies, delivering 100% survival even when administered 2 days post-challenge. In the MPXV CAST/EiJ mouse model, the combination significantly reduced splenomegaly and MPXV DNA loads in plasma, spleen and lung tissues, effectively suppressing systemic viral dissemination. INTERPRETATION: These findings establish that the structure-centric workflow enables efficient humanisation of well-characterised murine anti-orthopoxvirus antibodies, providing a validated framework to support the development of countermeasures for orthopoxvirus pandemic. FUNDING: This work was supported by the National Natural Science Foundation of China, the Chinese Academy of Medical Sciences Innovation Fund for Medical Sciences, the Scientific Research Innovation Capability Support Project for Young Faculty and the National Science and Technology Major Project.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个结合结构生物学与计算科学的框架，用于将鼠源抗体“人源化”（使其更像人类抗体以减少免疫排斥），并成功应用于开发针对猴痘病毒（MPXV）等正痘病毒的治疗性抗体。

### 1. 核心问题：为什么要做这项研究？
*   **痛点**：科学家发现了很多能杀死病毒的鼠源抗体，但直接给病人用会引起严重的免疫排斥（人体会攻击这些“外来”抗体）。
*   **传统方法的局限**：传统的人源化方法主要看“序列相似度”（像不像一串字母），但这经常导致抗体在改写后“走形”，失去捕捉病毒的能力。
*   **价值**：随着猴痘等病毒的再次流行，急需一种既能保留抗体强大杀伤力，又能安全用于人体的改造技术。

### 2. 白话版概述
抗体就像一把精准的“锁”，鼠源抗体是好用的钥匙，但材质不被人类免疫系统接受。传统方法是照着钥匙的“配方列表”改材质，结果钥匙往往弯了，开不了锁。这篇论文的方法是：**先看钥匙的 3D 形状**，在人类钥匙库里找一把形状最接近的“胚子”，再把关键的齿痕（结合位点）挪过去。实验证明，这样造出的抗体不仅不被排斥，杀毒效果甚至比原版还强，在小鼠实验中实现了 100% 的存活率。

### 3. 方法部分：核心思想与流程
该框架的核心是从“序列驱动”转向“**结构驱动**”。

*   **核心思想**：优先保证抗体在三维空间里的“骨架”一致性（3D Architectural Congruence），而非简单的氨基酸序列重合。
*   **关键工具 - Foldseek**：利用 Foldseek（一种极速的结构比对算法）在海量的人类抗体结构库中搜索，寻找与鼠源抗体骨架最匹配的人源模板。
*   **约束机制**：
    *   **界面残基约束**：锁定抗体与病毒接触的关键氨基酸，确保这些位置在改造过程中不发生形变。
    *   **CDR 嫁接**：将鼠源抗体的 CDR 区（决定抗体识别病毒的“指尖”部分）移植到筛选出的人源骨架上。
*   **推理流程**：输入鼠源抗体结构 -> Foldseek 结构搜索 -> 骨架筛选与界面约束 -> 序列生成 -> 结构模拟验证（计算 RMSD，即原子位置的偏差）。

### 4. 实验部分：结果如何？
*   **实验对象**：针对两种经典的鼠源抗体（7D11 和 A27D7）进行改造，生成了 POX1.1 和 POX2.1。
*   **评价指标**：
    *   **结构相似度**：改造前后的 RMSD（均方根偏差）小于 0.6 Å（极高精度，几乎重合）。
    *   **中和活性**：POX1.1 对牛痘病毒和猴痘病毒的中和能力甚至优于原始鼠源抗体。
    *   **体内保护力**：在致死剂量的病毒挑战下，联合使用两种人源化抗体的小鼠**存活率达到 100%**，且即使在感染 2 天后给药依然有效。
*   **对比（Baseline）**：与原始鼠源抗体及传统序列人源化方法对比，新方法在保持亲和力的同时，显著提升了人源化程度。

### 5. 资源与算力
*   **文中未充分披露**：论文重点在于生物实验验证和算法逻辑，未详细列出具体的 GPU 型号或训练时长。但考虑到使用了 Foldseek 和结构模拟，该流程对算力的需求远低于从头训练大模型，更侧重于高效的结构检索和能量最小化计算。

### 6. 真正可信的贡献
*   **结构优先的验证**：证明了在抗体设计中，**3D 结构的相似性比序列相似性更能预测抗体的功能保留**。
*   **实战价值**：提供了两款经过严格动物实验验证的、可直接进入临床前研究的抗猴痘候选药物。
*   **流程通用性**：该框架不仅适用于正痘病毒，理论上可以推广到任何鼠源抗体的人源化改造。

### 7. 局限与风险
*   **样本量较小**：虽然实验非常详尽，但仅在两个抗体上进行了验证，框架的普适性仍需更多案例支撑。
*   **依赖高质量结构**：如果原始鼠源抗体没有精确的晶体结构，而是靠 AI 预测（如 AlphaFold），预测误差可能会影响后续的骨架匹配。
*   **临床转化**：小鼠模型（CAST/EiJ）虽然模拟了人类症状，但人体内的免疫反应和代谢过程仍可能与实验动物存在差异。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事蛋白质工程、抗体药物研发以及结构生物学 AI 建模的研究者。
*   **后续可跟进的问题**：能否将这种“结构约束”整合进扩散模型（Diffusion Models）或蛋白质语言模型中，实现全自动、端到端的高成功率抗体人源化生成？

（完）
