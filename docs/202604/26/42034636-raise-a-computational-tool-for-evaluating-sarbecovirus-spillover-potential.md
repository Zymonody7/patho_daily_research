---
title: "RAISE: A computational tool for evaluating sarbecovirus spillover potential."
title_zh: RAISE：一种用于评估沙贝病毒溢出潜力的计算工具
authors: "He Huang, Lupeng Kong, Yanzhi Zhu, Yue Dai, Yutong Yang, Yuyang Wang, Zhiqiang Wu, Yi Qin Gao, Lili Ren"
date: 2026-04-25
pdf: "https://pubmed.ncbi.nlm.nih.gov/42034636/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于沙贝病毒溢出潜力和受体相互作用评分的计算框架
tldr: 针对沙贝病毒（如SARS-CoV-2）通过结合hACE2受体引发跨物种传播的风险，本研究开发了RAISE计算框架。该工具通过整合结构预测与相互作用评分，将病毒分为高风险、无风险及“蓄势待发”三类。RAISE成功预测了使弱结合病毒获得感染人类能力的特定突变（如T498Y/W），并展现了在墨贝病毒中的通用性，为传染病预警提供了量化评估工具。
selection_source: fresh_fetch
motivation: 评估动物源沙贝病毒向人类跨物种传播的风险，核心难点在于准确预测其刺突蛋白与人类ACE2受体的结合能力。
method: 开发了名为RAISE的计算框架，通过整合蛋白质结构预测与分子相互作用评分，对病毒受体结合域与hACE2的亲和力进行量化评估。
result: 该模型不仅准确划分了病毒的感染潜力等级，还通过突变筛选发现了能显著增强病毒受体结合能力的关键位点，并成功推广至墨贝病毒。
conclusion: RAISE为识别高风险人畜共患病毒提供了一套可扩展的预测路线图，有助于在疫情爆发前优先配置防疫资源。
---

## 摘要
动物沙贝病毒（Sarbecoviruses）是 SARS-CoV 或 SARS-CoV-2 的近亲，由于其结合人类 ACE2 (hACE2) 受体的能力，构成了重大的动物源性威胁。为了应对评估这些威胁的挑战，我们开发了 RAISE（受体结合域-hACE2 相互作用评分评估），这是一个整合了结构预测与相互作用评分的计算框架。通过对预测的 hACE2 相互作用进行评分，我们的 RAISE 模型将沙贝病毒分为三类：高潜力（hACE2 结合）、极低潜力（hACE2 不结合）以及中间的“待发（poised）”状态（该状态定义为具有微弱结合活性或具有进化出该能力的高潜力）。利用 RAISE 对两种“hACE2 待发型”沙贝病毒 PDF-2370 和 Khosta-1 进行突变筛选，发现了如 T498Y/W 等突变，这些突变使其能够利用人类 ACE2，并扩展了它们结合更广泛物种 ACE2 受体的能力。通过对美贝病毒（Merbecoviruses）的前瞻性应用，进一步证明了该模型的泛化能力，突显了其在预先评估跨冠状病毒谱系的动物源性威胁方面的实用性。RAISE 为确定风险病毒的优先级和指导大流行防范提供了预测路线图。

## Abstract
Animal sarbecoviruses, relatives of SARS-CoV or SARS-CoV-2, pose a significant zoonotic threat driven by their ability to bind the human ACE2 (hACE2) receptor. To address challenges in evaluating these threats, we developed RAISE (Receptor binding domain-hACE2 Interaction Scoring Evaluation), a computational framework that integrates structural predictions with interaction scoring. By scoring predicted hACE2 interactions, our RAISE model categorized sarbecoviruses into three groups: high potential (hACE2-binding), negligible potential (hACE2-nonbinding), and an intermediate "poised" state (a state defined by either weak binding activity or a high potential to evolve it). Mutation screening of two "hACE2-poised" sarbecoviruses, PDF-2370 and Khosta-1 using RAISE, revealed mutations such as T498Y/W that enabled human ACE2 utilization and expanded their ability to bind to ACE2 receptors from a broader range of species. The model's generalizability was further demonstrated through prospective application to merbecoviruses, highlighting its utility in preemptively assessing zoonotic threats across coronavirus lineages. RAISE provides a predictive roadmap for prioritizing risk viruses and guiding pandemic preparedness.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **RAISE** 的计算框架，旨在预测动物源性冠状病毒（特别是沙贝病毒，如 SARS-CoV-2 的亲戚）向人类跨物种传播（溢出）的风险。

---

### 1. 解决的问题与研究价值
**核心问题：** 科学家在野外发现了成千上万种冠状病毒，但不知道哪一种会在明天突然“跳”到人身上引发大流行。
**研究价值：** 病毒能否感染人，关键看它表面的“钩子”（刺突蛋白的 RBD 区域）能否抓牢人体细胞表面的“大门锁扣”（hACE2 受体）。传统的实验室检测（如活病毒实验）速度慢、成本高且有生物安全风险。RAISE 提供了一种“数字预警”方案，能在病毒真正爆发前，通过计算手段识别出哪些病毒是“高危分子”，哪些是“潜力股”。

---

### 2. 白话版概述
想象病毒是一把钥匙，人体受体是一把锁。RAISE 就像一个高精度的“数字钥匙匹配器”：它先用 AI 模拟出钥匙插进锁里的三维样子，然后计算它们贴合得紧不紧。它不仅能识别出已经能开锁的病毒，还能揪出那些“钥匙齿痕差一点点”的病毒（即“蓄势待发”型），并预测只要变异哪一个位点，这把钥匙就能打开人体的门。

---

### 3. 方法部分：核心思想与流程
RAISE 框架结合了**结构生物学预测**与**物理/统计评分**：

*   **核心思想：** 既然实验测定结构太慢，就先用 AI 预测病毒 RBD 与人 ACE2 结合后的三维复合物结构，再量化评估其结合强度。
*   **推理流程：**
    1.  **结构建模：** 输入病毒的基因序列，利用 AlphaFold2 或类似工具预测其 RBD 蛋白与人类 ACE2 受体结合时的三维空间构型。
    2.  **相互作用评分：** 基于预测的结构，计算界面上的能量分布、氢键、疏水作用等指标，给出一个综合评分。
    3.  **风险分类：** 根据评分将病毒分为三类：
        *   **高潜力（High）：** 已经能紧密结合 hACE2。
        *   **极低潜力（Negligible）：** 结构完全不匹配。
        *   **蓄势待发（Poised）：** 目前结合弱，但处于进化边缘，极易通过 1-2 个突变获得感染人的能力。
*   **关键设计：** 引入了“突变扫描”功能，专门针对“蓄势待发”型病毒，模拟改变其氨基酸序列，看评分是否会暴增。

---

### 4. 实验部分：验证与结果
*   **数据与任务：** 研究团队收集了多种已知的沙贝病毒（Sarbecoviruses）和墨贝病毒（Merbecoviruses，如 MERS 亲戚）序列。
*   **关键发现：**
    *   **分类准确：** RAISE 成功识别了 PDF-2370 和 Khosta-1 这两种原本被认为风险较低的病毒属于“蓄势待发”型。
    *   **突变预测：** 模型预测在第 498 位点进行突变（如 T498Y 或 T498W）能显著增强结合力。
    *   **实验验证：** 随后的湿实验（实验室检测）证实，这些带有预测突变的病毒确实获得了结合人类 ACE2 的能力，验证了模型的预见性。
*   **泛化能力：** 模型在墨贝病毒（利用不同受体）上也表现良好，证明该框架具有跨病毒种类的通用潜力。

---

### 5. 资源与算力
**文中未充分披露**具体的硬件配置（如 GPU 型号或计算时长）。但基于其使用的结构预测方法（AlphaFold 衍生工具），通常需要高性能计算集群或配备 A100/H100 等显卡的服务器。

---

### 6. 真正可信的贡献
1.  **提出了“蓄势待发（Poised）”状态的概念：** 这比单纯的“能”或“不能”更具预警意义，指出了哪些病毒最值得重点监控。
2.  **精准的位点预测：** 成功锁定了 T498Y/W 等关键突变位点，并通过实验闭环验证了计算结果的真实性。
3.  **计算路线图：** 为全球公共卫生专家提供了一套标准化的流程，用于快速评估新发现病毒的威胁等级。

---

### 7. 局限与风险
*   **受体单一性：** 目前主要关注 ACE2 受体，但病毒进入人体可能还需要其他辅助因子（如 TMPRSS2 蛋白酶），模型尚未完全整合这些复杂因素。
*   **结构预测误差：** AI 预测的结构虽准，但在处理极细微的侧链翻转时仍可能有偏差，影响评分精度。
*   **外推风险：** 病毒的实际传播力还受免疫逃逸、环境稳定性等影响，结合力强并不等同于一定会引发大流行。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事蛋白质相互作用（PPI）预测、病毒进化模拟、以及药物分子设计的 AI 研究者。
*   **后续可跟进的问题：** 能否将该框架从“静态结构评分”升级为“动态模拟”，考虑病毒蛋白在真实生理环境下的柔性变化？或者利用生成式 AI 直接设计能阻断这些“高危结合界面”的广谱抗体？

（完）
