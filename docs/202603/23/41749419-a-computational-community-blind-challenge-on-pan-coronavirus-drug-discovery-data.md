---
title: A Computational Community Blind Challenge on Pan-Coronavirus Drug Discovery Data.
title_zh: 一项关于泛冠状病毒药物研发数据的计算社区盲测挑战
authors: "Hugo MacDermott-Opeskin, Jenke Scheen, Cas Wognum, Joshua T Horton, Devany West, Alexander Matthew Payne, Maria A Castellanos, Sean Colby, Edward Griffen, David Cousins, Jessica Stacey, Lauren Reid, Jasmin Cara Aschenbrenner, Daren Fearon, Blake Balcomb, Peter Marples, Charles W E Tomlinson, Ryan Lithgo, Andre S Godoy, Max Winokan, Haim Barr, Noa Lahav, Michael Lavi, Shirley Duberstein, Galit Cohen, Gwendolyn Fate, Bruce Lefker, Ralph Robinson, Tamas Szommer, Nick Lynch, David D L Minh, Van Ngoc Thuy La, Lulu Kang, Kate Huddleston, Ryan Renslow, Mallory Tollefson, W Patrick Walters, Cynthia Xu, Jonny Hsu, Julien St-Laurent, Honore Etsmoberg, Lu Zhu, Andrew Quirke, Mohamed Iliyas Abdul Haleem, Irfan Alibay, Gunjan Baid, Benjamin Birnbaum, Kevin P Bishop, Hugo Bohorquez, Ashmita Bose, C J Brown, Jackson Burns, Lianjin Cai, Ruel Cedeno, Stephane de Cesco, Vladimir Chupakhin, Finlay Clark, Daniel J Cole, Carles Corbi-Verge, Muhammad Danial, Alec Davi, Wim Dehaen, Niklas Piet Doering, Alexis Dougha, Marie-Pierre Dréanic, Bryce Eakin, Anatol Ehrlich, Rokas Elijosius, Jozef Fülöp, Anthony Gitter, Kenneth Goossens, Yaowen Gu, Teresa Head-Gordon, Laurent Hoffer, Johan Hofmans, Ellena Jiang, Benjamin Kaminow, Sina Khosravi, Asma Feriel Khoualdi, Eelke Bart Lenselink, Zhirong Liu, Yue Liu, Sijie Liu, Yizhou Ma, Patrick Maher, Imke Mayer, Oscar Mendez-Lucio, Antonia S J S Mey, Julien Michel, Floriane Montanari, Taoyu Niu, Ryusei Ogino, Ashok Palaniappan, Xiaolin Pan, Auro Patnaik, Long-Hung Pham, Luis Pinto, Justin Purnomo, Alex Rich, Lars Schaaf, Christoph Schran, Rajeev Kumar Singh, Mounika Srilakshmi, Satya Pratik Srivastava, Kunyang Sun, Zhaoxi Sun, Valerij Talagayev, Balamurugan Thirukonda Subramanian Balakrishnan, Ida Titus, Alexandre Tkatchenko, Wojtek Treyde, Giovanni Tricarico, Austin Tripp, Nopsinth Vithayapalert, Yingze Wang, Azmine Toushik Wasi, Steffen Wedig, Gerhard Wolber, Bofei Xu, Weijun Zhou, Frank von Delft, Alpha Lee, Karla Kirkegaard, Peter Sjö, James S Fraser, John D Chodera"
date: 2026-03-23
pdf: "https://pubmed.ncbi.nlm.nih.gov/41749419/"
tags: ["query:pathoai"]
score: 9.0
evidence: 针对泛冠状病毒的AI驱动抗病毒药物发现计划
tldr: 针对冠状病毒药物研发中计算预测准确性难以客观评估的问题，ASAP 联盟联合 Polaris 发起了一项社区盲测挑战。该挑战利用未公开的 SARS-CoV-2 和 MERS-CoV 实验数据，要求参与者预测小分子的生化活性、配体结合姿态及 ADMET 指标。通过对全球提交方案的元分析，建立了性能基准，揭示了当前机器学习在药物发现中的优势与局限，为构建可信、可重复的 AI 辅助药物研发流程提供了实证基础。
selection_source: fresh_fetch
motivation: 旨在通过未公开的真实实验数据，客观评估计算方法在预测冠状病毒药物活性及药代动力学性质方面的实际表现。
method: 组织全球开发者针对 SARS-CoV-2 和 MERS-CoV 的主蛋白酶目标，利用 Polaris 平台进行生化效价、晶体结构姿态及多种 ADMET 终点的盲测预测。
result: 建立了性能排行榜并进行了元分析，识别出表现优异的算法策略，同时也发现了当前计算模型在处理真实世界药物优化数据时的常见误区。
conclusion: 该挑战为 AI 辅助药物发现提供了标准化的评估框架和高质量基准数据集，推动了计算药学向更具可重复性和透明度的方向发展。
---

## 摘要
计算盲测挑战为评估和加速科学进步提供了关键且公正的机会，过去十年的广泛突破证明了这一点。我们报告了一项专注于药物研发计算方法的开放科学社区盲测挑战的结果和关键见解。该挑战使用了来自 AI 驱动的结构赋能抗病毒平台发现联盟（ASAP）泛冠状病毒抗病毒发现项目的先导化合物优化数据，并与 Polaris 和 OpenADMET 项目合作。这一协作倡议邀请了来自学术界和工业界的全球参与者，开发并应用计算方法，以预测针对关键冠状病毒靶点——严重急性呼吸系统综合征冠状病毒 2 (SARS-CoV-2) 和中东呼吸综合征冠状病毒 (MERS-CoV) 主蛋白酶 (Mpro) 的小分子生化效价和晶体学配体构象，以及多个 ADMET 实验终点。该挑战使用此前未公开的全面实验药物研发数据集作为基准。通过对多项任务和化合物的提交结果进行评估，我们建立了性能排行榜，并进行了元分析，以评估方法的优势、常见陷阱和改进方向。该分析为基于社区驱动基准测试的现实世界机器学习评估最佳实践奠定了基础。我们还强调了 Polaris 等下一代平台如何实现严谨的挑战设计、嵌入式评估框架和广泛的社区参与。本文报告了挑战赛的集体研究结果，对数据、评估基础设施和表现最佳的策略进行了高层概述。我们还为本专刊中由挑战赛参与者撰写的配套论文提供了背景和支持，这些论文更深入地探讨了各自的方法。这些贡献共同旨在推进药物研发中可重复、可信且具有高影响力的计算方法，并探索未来盲测挑战设计与执行中的最佳实践和陷阱，包括 OpenADMET 项目的计划倡议。

## Abstract
Computational blind challenges offer critical, unbiased opportunities to assess and accelerate scientific progress, as demonstrated by a breadth of breakthroughs over the past decade. We report the outcomes and key insights from an open science community blind challenge focused on computational methods in drug discovery, using lead optimization data from the AI-driven Structure-enabled Antiviral Platform Discovery Consortium's pan-coronavirus antiviral discovery program, in partnership with Polaris and the OpenADMET project. This collaborative initiative invited global participants from both academia and industry to develop and apply computational methods to predict the biochemical potency and crystallographic ligand poses of small molecules against key coronavirus targets, Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2) and Middle East Respiratory Syndrome Coronavirus (MERS-CoV) main protease (Mpro), as well as multiple ADMET assay end points, using previously undisclosed comprehensive experimental drug discovery data sets as benchmarks. By evaluating submissions across multiple tasks and compounds, we established performance leaderboards and conducted meta-analyses to assess methodological strengths, common pitfalls, and areas for improvement. This analysis provides a foundation for best practices in real-world machine learning evaluation, grounded in community-driven benchmarking. We also highlight how next-generation platforms, such as Polaris, enable rigorous challenge design, embedded evaluation frameworks, and broad community engagement. This paper reports the collective findings of the challenge, offering a high-level overview of the data, evaluation infrastructure, and top-performing strategies. We further provide context and support for the accompanying papers authored by the challenge participants in this special issue, which explore individual approaches in greater depth. Together, these contributions aim to advance reproducible, trustworthy, and high-impact computational methods in drug discovery, and to explore best practices and pitfalls in future blind challenge design and execution, including planned initiatives for the OpenADMET project.

---

## 论文详细总结（自动生成）

这是一份关于论文《一项关于泛冠状病毒药物研发数据的计算社区盲测挑战》（*A Computational Community Blind Challenge on Pan-Coronavirus Drug Discovery Data*）的深度解析：

### 1. 这篇论文到底在解决什么问题，为什么值得看？
*   **核心问题**：AI 药物研发领域存在“虚假繁荣”。很多模型在公开数据集上表现惊人，但在实际实验室研发中往往失效。这是因为公开数据存在严重的**数据泄露**（训练集和测试集太像）和**回顾性偏差**。
*   **价值所在**：本文报道了一场“真刀真枪”的盲测（Blind Challenge）。组织者利用尚未公开的、真实的冠状病毒药物研发实验数据作为“考卷”，让全球 AI 团队在不知道答案的情况下进行预测。它真实反映了当前 AI 在预测药物效价、结合姿态及药代动力学（ADMET）方面的**实际天花板**。

### 2. 白话版概述
想象一场药物研发界的“高考”：出卷老师是专业的病毒研究机构（ASAP 联盟），他们手里有刚做完实验、还没发表的冠状病毒药物数据。考生是全球的 AI 模型。考试内容包括：预测这些小分子对新冠和默斯（MERS）病毒的杀伤力、预测分子在病毒蛋白里的“坐姿”（结合构象），以及预测这些药进入人体后是否容易被代谢或产生毒性。这篇论文总结了这场考试的成绩单，告诉我们哪些 AI 招式是真管用，哪些只是在“背题库”。

### 3. 方法部分：核心思想与流程
该论文本身不是介绍单一模型，而是介绍一个**评估框架**和**竞赛元分析**：
*   **核心思想**：通过“前瞻性预测”（Prospective Prediction）消除偏差。即在实验数据产生或公开之前，要求参与者提交预测结果。
*   **任务设计**：
    *   **生化效价预测**：预测小分子抑制 Mpro（主蛋白酶，病毒复制的关键酶）的强度（pIC50）。
    *   **配体姿态预测**：给定蛋白质结构，预测小分子在其中的 3D 坐标（Docking/Pose Prediction）。
    *   **ADMET 预测**：预测分子的溶解度、代谢稳定性、渗透性等指标。
*   **关键设计取舍**：使用了 **Polaris 平台**。这是一个专门为药物研发设计的基准测试平台，它解决了以往竞赛中“数据格式不统一”、“评价标准不透明”的问题，实现了代码级的可重复性。

### 4. 实验部分：数据与结果
*   **数据源**：来自 ASAP 联盟的真实研发管线，针对 SARS-CoV-2 和 MERS-CoV 的 Mpro 靶点。
*   **评价指标**：
    *   **效价**：均方根误差 (RMSE)、皮尔逊/斯皮尔曼相关系数。
    *   **姿态**：均方根偏差 (RMSD)，衡量预测位置与真实晶体结构的偏离程度。
    *   **ADMET**：分类任务用 AUC-ROC，回归任务用 MAE（平均绝对误差）。
*   **主要结果**：
    *   **性能鸿沟**：大多数模型在盲测中的表现远低于在公开数据集上的表现。
    *   **优胜策略**：表现最好的方法通常结合了**物理化学特征**（如分子动力学、自由能计算）与**深度学习集成模型**（Ensemble Methods）。
    *   **ADMET 难题**：对于复杂的生物学指标（如清除率），AI 的预测准确度依然有限，显示出实验数据的噪声对模型影响巨大。

### 5. 资源与算力
*   **文中未充分披露**。由于这是一个社区挑战赛，各参与团队（如英伟达、各类高校、药企）使用的算力各不相同，论文重点在于汇总结果而非统计各方的计算资源消耗。

### 6. 真正可信的贡献
*   **建立了高质量基准**：提供了一套经过实验验证的、针对冠状病毒 Mpro 靶点的标准化数据集。
*   **揭示了行业现状**：有力证明了“简单的端到端深度学习”在缺乏高质量、同分布数据时，难以处理真实的先导化合物优化任务。
*   **推动了透明化**：通过 Polaris 平台展示了如何进行可信、可重复的 AI 药物研发评估。

### 7. 局限与风险
*   **靶点局限性**：数据集中于 Mpro 这一种蛋白，结论未必能外推到其他类型的靶点（如 GPCR 或离子通道）。
*   **数据规模**：虽然是真实数据，但对于深度学习而言，样本量（尤其是 MERS 数据）仍然偏小，可能导致模型过拟合于特定的化学系列。
*   **真实应用障碍**：预测准确不代表能成药。盲测只关注了静态指标，未考虑药物在复杂生物系统中的动态反馈。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事分子性质预测、蛋白质-配体对接、以及试图将 AI 模型落地到药企管线的算法工程师。
*   **后续可跟进的问题**：如何利用少量、有噪声的真实实验数据进行有效的“小样本学习”或“迁移学习”，以弥补盲测中暴露出的泛化能力不足？

（完）
