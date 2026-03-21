---
title: High-resolution phage-host assignment through key proteins using large language models.
title_zh: 利用大语言模型通过关键蛋白质进行高分辨率噬菌体-宿主关联
authors: "Zhihua Du, Min Li, Kaihuang Lin, Bo Xing, Yuehua Ou, Zihao Lin, Wenchen Song, Jie Chen, Junhua Li, Jianqiang Li, Minfeng Xiao"
date: 2026-03-20
pdf: "https://pubmed.ncbi.nlm.nih.gov/41862452/"
tags: ["query:pathoai"]
score: 10.0
evidence: 用于噬菌体-宿主分配和病原体理解的大语言模型
tldr: 针对环境中大量病毒序列难以识别宿主的问题，本研究开发了 VirHost Hunter 框架。该框架利用蛋白质语言模型和视觉 Transformer 提取噬菌体尾部蛋白和裂解酶的深层特征，无需完整基因组即可实现高分辨率的宿主分配。实验证明该方法在肠道菌群分析中显著提升了预测精度，并成功筛选出能特异性针对肥胖相关细菌的裂解酶，为精准微生物组治疗提供了新路径。
selection_source: fresh_fetch
motivation: 传统的噬菌体宿主预测方法高度依赖基因组完整性且难以捕捉序列差异大的同源功能，限制了对复杂环境病毒组的理解。
method: 通过蛋白质语言模型和视觉 Transformer 提取噬菌体关键蛋白（尾部蛋白和裂解酶）的功能特征，绕过全基因组比对的限制。
result: 在肠道样本中将宿主分配量提升了一倍，并据此合成了一种能有效且特异性打击肥胖诱导细菌的裂解酶。
conclusion: 利用深度学习捕捉关键蛋白的功能同源性是解决病毒宿主匹配难题的高效方案，对开发新型抗菌药物具有重要价值。
---

## 摘要
不同环境中的病毒序列在很大程度上仍未被表征，这阻碍了我们对其遗传组成、生物相互作用及潜在应用的理解。这凸显了对创新分析方法的迫切需求。在此，我们提出了 VirHost Hunter 框架，该框架利用噬菌体尾部和裂解酶，绕过了对全基因组的需求，实现了高效且高分辨率的宿主分配。通过利用蛋白质语言模型（Protein Language Models）和视觉 Transformer（Vision Transformers），VirHost Hunter 能够在序列不相似的情况下捕捉蛋白质的功能同源性，从而显著提高预测准确性。在疾病相关的肠道细菌场景中，经过校准的 VirHost Hunter 超越了现有方法，使噬菌体宿主分配数量翻倍，扩大了分类学范围，并揭示了先前未表征的针对肠道细菌（包括 Akkermansia 和 Prevotella）的噬菌体。因此，我们建立了一个肠道噬菌体裂解酶数据库，从而能够合成一种有效且特异性针对促肥胖细菌的裂解酶。VirHost Hunter 的精确性和可扩展性标志着病毒组研究的重大飞跃，并为微生物组疗法提供了一条充满前景的途径。

## Abstract
Viral sequences in diverse environments remain largely uncharacterized, impeding our comprehension of their genetic makeup, biological interactions, and potential applications. This underscores an urgent need for innovative analytical methods. Here, we present the VirHost Hunter framework, which employs phage tails and lysins, bypassing the requirement for full genomes, for efficient and high-resolution host assignment. By harnessing Protein Language Models and Vision Transformers, VirHost Hunter captures protein functional homology despite sequence dissimilarity, significantly boosting prediction accuracy. In the scenario of disease-associated gut bacteria, the calibrated VirHost Hunter surpasses existing methods, doubling phage host assignments, expanding taxonomic reach, and revealing previously uncharacterized phages targeting gut bacteria, including Akkermansia and Prevotella. Therefore, we establish a gut phage lysin database, enabling the synthesis of a lysin that effectively and specifically targets an obesity-promoting bacterium. VirHost Hunter's precision and scalability mark a significant leap forward in virome research and present a promising avenue for microbiome therapies.