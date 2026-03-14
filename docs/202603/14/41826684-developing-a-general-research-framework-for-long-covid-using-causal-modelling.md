---
title: Developing a general research framework for long COVID using causal modelling.
title_zh: 利用因果建模开发长新冠（long COVID）的通用研究框架
authors: "Gladymar Pérez Chacón, Steven Mascaro, Marie J Estcourt, Chansavath Phetsouphanh, Ann E Nicholson, Tom Snelling, Yue Wu"
date: 2026-03-13
pdf: "https://pubmed.ncbi.nlm.nih.gov/41826684/"
tags: ["query:pathoai"]
score: 7.0
evidence: 感染相关慢性疾病的因果建模与贝叶斯网络
tldr: 针对长新冠（Long COVID）定义模糊及病理机制复杂的挑战，本研究提出了一种基于因果建模的通用研究框架。通过构建动态贝叶斯网络（DBN）和有向无环图（DAG），模拟了从急性感染到长期症状演变的生物学路径。结果显示，在急性期和感染后3-6个月均出现症状的患者，其发生持续性器官功能障碍的概率最高。该框架为长新冠的临床诊断和预后预测提供了理论支持和模拟工具。
selection_source: fresh_fetch
motivation: 长新冠的定义和病理机制存在高度不确定性，亟需一种能够整合多种假设并统一理解其演化过程的通用研究框架。
method: 采用因果工程方法构建动态贝叶斯网络，将急性感染至长期症状的生物学路径划分为四个时间阶段进行定性参数化建模。
result: 模拟实验表明，相比仅在急性期有症状的患者，在感染初期及3-6个月后持续表现出症状的群体，其发生长期器官功能障碍的风险显著更高。
conclusion: 研究证明了因果模型在处理长新冠诊断与预后问题上的有效性，为理解该病症的进展机制奠定了基础。
---

## 摘要
背景：长新冠是一种与感染相关的慢性疾病，其演变过程具有不确定性，导致病例定义模糊，且关于其病理生理学存在多种假设。尽管存在这种多样性，因果模型可能为急性后新冠肺炎（post-acute COVID-19）机制提供统一的理解。本研究旨在探讨动态贝叶斯网络是否能促进对长新冠的推断。方法：采用因果工程方法，我们开发了有向无环图，并将其定性参数化为贝叶斯网络，以一种与理论无关的方式描述长新冠的假设机制。基于文献和专家知识，我们创建了一个通用建模框架，总结了从轻度或重度新冠肺炎到四个关键时期（t1至t4）内呼吸道症状和疲劳发展的生物学路径。我们使用定性参数化进行设计和验证，并针对四种情景测试了该框架：A）t1期（急性感染开始）为轻度新冠肺炎；B）t1期为重度急性新冠肺炎；C）t1期报告症状（急性新冠肺炎疾病）；D）t1期和t3期（例如急性感染后3至6个月）均报告症状，表明存在长新冠。结果：我们在此展示，在情景A中，进展为重症并在急性新冠肺炎后1至2年出现持续性器官功能障碍的概率低于情景C。在t1和t3期报告症状的患者，在急性感染期后出现持续性器官功能障碍的概率最高。结论：我们的研究结果为更好地理解长新冠综合征的进展奠定了基础。说明性模拟支持使用因果模型来帮助解决长新冠研究中的诊断和预后问题。

## Abstract
BACKGROUND: Long COVID is an infection-associated chronic condition with uncertain evolution, leading to ambiguity in case definitions and various hypotheses about its pathophysiology. Despite this diversity, causal models may offer a unified understanding of post-acute COVID-19 mechanisms. This study aimed to examine whether dynamic Bayesian networks could facilitate inferences on long COVID. METHODS: Using a causal engineering approach, we developed directed acyclic graphs and qualitatively parametrised them as Bayesian networks to depict the hypothesised mechanisms of long COVID in a theory-agnostic manner. Based on the literature and expert knowledge, we created a general modelling framework summarising biological pathways from mild or severe COVID-19 to the development of respiratory symptoms and fatigue over four key periods (t1 to t4). We used qualitative parametrisation for design and validation, and tested the framework against four scenarios: A) mild COVID-19 at t1 (start of acute infection); B) severe acute COVID-19 at t1; C) symptoms reported at t1 (acute COVID-19 disease); and D) symptoms reported at t1 and t3 (e.g., 3-to-6 months post-acute infection), indicating long COVID. RESULTS: Here we show that, in scenario A, the probability of progressing to severe disease and developing persistent organ dysfunction 1-to-2 years post-acute COVID-19 was lower than in scenario C. Those reporting symptoms at t1 and t3 have the highest probability of developing persistent organ dysfunction beyond the acute infection period. CONCLUSIONS: Our findings lay the foundations for a better understanding of the progression of long COVID syndromes. Illustrative simulations support the use of causal models to help address both diagnostic and prognostic questions in long COVID research.