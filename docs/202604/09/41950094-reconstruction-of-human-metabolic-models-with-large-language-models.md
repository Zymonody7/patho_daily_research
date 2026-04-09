---
title: Reconstruction of human metabolic models with large language models.
title_zh: 利用大语言模型重建人类代谢模型
authors: "Jiahao Luo, Hao Wang, Devlin Moyer, Zhetao Guo, Jonathan L Robinson, Johan Gustafsson, Mihail Anton, Yu Chen, Eduard J Kerkhoven, Jens Nielsen, Feiran Li"
date: 2026-04-14
pdf: "https://pubmed.ncbi.nlm.nih.gov/41950094/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 利用大语言模型重建人类代谢模型
tldr: 针对人类基因组规模代谢模型（GEM）构建中人工维护成本高、精度不足的问题，本研究开发了 Human2 模型。该模型利用大语言模型（LLM）和自动化工作流进行高效协作策展，支持构建不同性别、年龄及组织的特异性模型。通过整合多组学与动力学数据，Human2 实现了对全身器官间代谢物交换的动态模拟，为多尺度人类代谢研究提供了高精度的数字化工具。
selection_source: fresh_fetch
motivation: 传统人类代谢模型构建过程繁琐且难以实现多尺度、多维度的动态模拟，限制了对复杂生理状态下代谢差异的深入理解。
method: 引入大语言模型辅助模型策展，并结合 GitHub 自动化检查，整合转录组、蛋白质组及动力学数据构建全身动态代谢框架。
result: 成功识别出不同性别与年龄组在花生四烯酸等代谢途径上的显著差异，并实现了从进食到禁食状态下的跨器官代谢物交换模拟。
conclusion: 该研究证明了 LLM 在加速生物模型构建中的潜力，并为精准医疗和系统生物学提供了首个酶约束的全身动态代谢模拟资源。
---

## 摘要
基因组规模代谢模型（GEMs）已成为理解人类代谢的重要工具。在此，我们介绍了 Human2，这是一个具有更高精度和生物学相关性的共识人类 GEM，它利用大语言模型（LLMs）和 GitHub Action 检查来简化自动化、高效且协作的策展过程。Human2 支持针对特定性别和年龄的人群重建组织及器官特异性模型。通过整合转录组学、蛋白质组学和动力学数据，我们揭示了这些群体中独特的代谢特征，例如花生四烯酸和白三烯代谢的显著差异。这些特异性模型被整合到一个动态的全身框架中，形成了一个酶约束动态模型，用于模拟从进食到禁食等不同营养状态下的器官间代谢物交换。我们的工作突出了 LLMs 在 GEM 重建中的变革性作用，并引入了整合动力学数据的全身动态模拟，为多尺度人类代谢建模提供了强大的资源。

## Abstract
Genome-scale metabolic models (GEMs) have become essential tools for understanding human metabolism. Here, we introduce Human2, a consensus human GEM with enhanced precision and biological relevance, which leverages large language models (LLMs) and GitHub Action checks to streamline automated, efficient, and collaborative curation. Human2 supports the reconstruction of tissue- and organ-specific models tailored to sex- and age-specific human groups. By integrating transcriptomic, proteomic, and kinetic data, we reveal distinct metabolic features across these groups, such as significant differences in arachidonic acid and leukotriene metabolism. The specific models were integrated into a dynamic whole-body framework, marking an enzyme-constrained dynamic model that simulates interorgan metabolite exchanges under varying nutritional states, from feeding to fasting. Our work highlights the transformative role of LLMs in GEM reconstruction and introduces a whole-body dynamic simulation that integrates kinetic data, offering a powerful resource for multiscale human metabolism modeling.

---

## 论文详细总结（自动生成）

这是一份关于论文《Reconstruction of human metabolic models with large language models》（利用大语言模型重建人类代谢模型）的深度解析：

### 1. 解决的问题与研究价值
**核心问题：** 
人类基因组规模代谢模型（GEM，可以理解为描述人体内数千种化学反应的“全景地图”）的构建极其耗时耗力。传统的“共识模型”（如 Human1）依赖大量专家手动校对，更新周期长，且难以捕捉不同性别、年龄和组织之间的细微动态差异。

**研究价值：**
1. **效率革命：** 引入大语言模型（LLM）自动化处理繁琐的文献挖掘和数据校对。
2. **从静态到动态：** 首次实现了“酶约束”的全身动态模拟，能模拟人体从吃饱到饥饿过程中，不同器官之间如何“交换”能量和物质。
3. **精准医疗基础：** 为不同人群（如不同性别、年龄）提供了定制化的代谢数字孪生模型。

---

### 2. 白话版概述
想象你要绘制一张包含人体所有化学反应的超详细地图。以前需要几百个科学家画好几年，现在研究者请 AI（大语言模型）当“总编辑”，自动从海量文献中找证据、改错，并配合 GitHub 的自动化工具进行质量把控。最终生成的 **Human2** 模型不仅更准，还能像模拟器一样运行：它能展示当你没吃饭时，肝脏是如何拆东墙补西墙给大脑供能的。

---

### 3. 方法部分：核心思想与设计
*   **LLM 辅助策展（Curation）：** 研究者利用 LLM（如 GPT 系列）来识别代谢反应中的错误、补全缺失的基因-反应关联（GPR），并从非结构化文本中提取动力学参数。
*   **自动化工作流：** 借鉴软件工程思想，利用 **GitHub Actions** 建立了一套自动化检查机制。每当模型数据有更新，系统会自动运行测试脚本，确保化学平衡、电荷平衡等生物化学规则不被破坏。
*   **酶约束模型（ecGEM）：** 传统的模型只看反应“能不能发生”，而 Human2 加入了“酶”的限制（即反应速度受限于体内蛋白质的含量），这让模拟结果更接近真实生理情况。
*   **全身动态框架：** 将不同器官（肝、肌肉、大脑等）的模型通过“血液循环”连接起来，整合转录组（基因表达）和蛋白质组数据，构建出一个多器官协作的动态系统。

---

### 4. 实验部分：数据与结果
*   **数据来源：** 整合了 GTEx（组织基因表达）、HPA（人类蛋白质图谱）以及大量的生化动力学数据库。
*   **关键任务：** 
    1. **人群差异分析：** 对比不同性别和年龄组。
    2. **动态代谢模拟：** 模拟进食后 24 小时内的代谢演变。
*   **主要结果：**
    *   **发现新差异：** 识别出性别间在**花生四烯酸**（一种与炎症相关的脂肪酸）和**白三烯**代谢上的显著不同，这解释了某些药物在不同性别间效果差异的生化基础。
    *   **器官间交换：** 成功模拟了禁食状态下，肌肉释放丙氨酸、肝脏将其转化为葡萄糖的经典生理过程（甘氨酸-葡萄糖循环），且预测数值与临床观察高度吻合。

---

### 5. 资源与算力
*   **文中未充分披露：** 论文重点在于模型架构和生物学发现，未详细列出调用 LLM API 的具体消耗、Token 数量或训练底层模型所用的 GPU 算力。

---

### 6. 真正可信的贡献
*   **工程化范式：** 证明了“LLM + GitHub 自动化”是构建复杂生物知识图谱的可行路径，极大降低了维护成本。
*   **多尺度整合：** 成功将微观的酶动力学数据与宏观的全身器官代谢耦合，这是目前人类代谢建模领域最完整的数字化表示。
*   **证据强度：** 通过与已知的临床生理数据（如禁食期间血糖/氨基酸波动）对比，验证了动态模拟的准确性。

---

### 7. 局限与风险
*   **LLM 幻觉风险：** 尽管有自动化检查，但 LLM 仍可能生成看似合理实则错误的生化反应，必须依赖严格的后期验证。
*   **动力学数据稀缺：** 很多代谢反应的速率常数（Km, kcat）在人体中尚无实测值，模型中使用的部分参数可能来自推测或动物实验，存在偏差。
*   **应用障碍：** 该模型复杂度极高，普通临床医生或非计算背景的生物学家难以直接使用，需要更友好的交互界面。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 系统生物学研究者、药物研发科学家、以及探索 LLM 在结构化知识库构建中应用的 AI 工程师。
*   **后续可跟进的问题：** 如何利用多模态大模型直接从实验图表中提取代谢参数？能否将该动态模型与强化学习结合，寻找特定代谢疾病的最佳给药策略？

（完）
