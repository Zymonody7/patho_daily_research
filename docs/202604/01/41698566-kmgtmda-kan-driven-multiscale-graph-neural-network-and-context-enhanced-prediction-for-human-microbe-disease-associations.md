---
title: "KMGTMDA: KAN-driven multiscale graph neural network and context-enhanced prediction for human microbe-disease associations."
title_zh: KMGTMDA：用于人类微生物-疾病关联预测的 KAN 驱动多尺度图神经网络与上下文增强预测
authors: "Xiaoxin Du, Hang Sun, Bo Wang, YiPing Wang, WenLong Zhao, Tang Sun, LiSen Yang"
date: 2026-04-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41698566/"
tags: ["query:pathoai"]
score: 9.0
evidence: KAN驱动的图神经网络预测微生物与疾病关联
tldr: 针对传统微生物实验成本高、周期长的问题，本研究提出 KMGTMDA 框架用于预测人类微生物与疾病的关联。该方法融合了动态多尺度图卷积、增强上下文的图 Transformer 以及 Kolmogorov-Arnold 网络（KAN），通过捕捉多尺度拓扑特征和全局依赖关系，在预测任务中取得了 0.9779 的 AUC。该工具能有效筛选潜在致病微生物，为疾病机制研究和靶向治疗提供计算支持。
selection_source: fresh_fetch
motivation: 传统微生物实验效率低且成本高，亟需高效的计算模型来预测微生物与疾病间的潜在关联，以揭示其生物学机制。
method: 提出一种结合动态多尺度图卷积、融合局部与全局上下文的图 Transformer 以及基于 KAN 的非线性评分预测框架。
result: 在五折交叉验证中达到 0.9779 的 AUC 和 0.9786 的 AUPR，并在牙周病和细菌性阴道炎的案例研究中验证了其有效性。
conclusion: 该模型通过多尺度拓扑学习和特征上下文增强，为理解疾病发病机理和设计针对性治疗策略提供了高效的计算手段。
---

## 摘要
目的：微生物在人类代谢调节、癌症抑制和病原体拮抗等关键生理过程中发挥着不可替代的作用，但传统的基于培养的微生物实验既昂贵又耗时。因此，迫切需要开发高效的计算预测模型来优先筛选疾病相关的微生物，旨在发现潜在关联并揭示其潜在的生物学机制。方法：提出了一种名为 KMGTMDA 的新型计算框架。首先，采用动态邻接矩阵动态整合一阶邻接和高阶拓扑信息，利用属性矩阵生成网络自适应调整节点连接权重，并通过双通路图卷积融合多尺度图特征。其次，考虑到微生物和疾病节点特征的上下文关系，采用图 Transformer 通过多头注意力机制捕捉全局依赖关系。在该模型中，引入了图结构偏差和邻域 Token 提取来捕捉局部语义模式。此外，还结合了特征保留策略，从特征角度补充详细的交互表示。最后，将特征输入到 Kolmogorov-Arnold 网络（KAN）中，该网络通过可学习的基函数和分段样条构建非线性映射，从而生成关联评分。结果：通过五折交叉验证对模型进行了评估，其 AUC 和 AUPR 值分别达到 0.9779 和 0.9786。此外，案例研究证实 KMGTMDA 是筛选与牙周病和细菌性阴道病相关的潜在微生物的有效工具。结论：该方法通过多尺度动态拓扑图神经网络和特征上下文学习，高效地揭示了人类微生物与疾病之间的潜在关联。它为解释疾病发病机制和设计针对性治疗策略提供了更有效的指导，并为进一步研究潜在疾病靶点提供了新方向。

## Abstract
OBJECTIVE: Microorganisms play an irreplaceable role in critical physiological processes such as human metabolic regulation, cancer inhibition, and pathogen antagonism, yet traditional culture-based microbial experiments are expensive and time-consuming. Consequently, there is an urgent need to develop efficient computational prediction models to prioritize disease-related microbes, aiming to discover potential associations and reveal their underlying biological mechanisms. METHODS: A novel computational framework named KMGTMDA is proposed. First, a dynamic adjacency matrix is employed to dynamically integrate first-order adjacency and higher-order topological information, utilizing an attribute matrix generation network to adaptively adjust node connection weights, and incorporating multi-scale graph features through dual-pathway graph convolution. Secondly, considering the contextual relationships of microbial and disease node features, a graph Transformer is employed to capture global dependencies through a multi-head attention mechanism. In this model, graph structural bias and neighborhood token extraction are introduced to capture local semantic patterns. Moreover, a feature retention strategy is incorporated to complement detailed interaction representations from the feature perspective. Finally, the features are input into a Kolmogorov-Arnold Network (KAN), which constructs nonlinear mappings through learnable basis functions and piecewise splines to generate association scores. RESULTS: The model was evaluated through five-fold cross-validation, achieving AUC and AUPR values of 0.9779 and 0.9786, respectively. Additionally, case studies confirmed that KMGTMDA is an effective tool for screening potential microbes associated with periodontal disease and bacterial vaginosis. CONCLUSIONS: This approach efficiently reveals potential associations between human microbes and diseases through multi-scale dynamic topological graph neural networks and feature context learning. It provides more effective guidance for interpreting disease pathogenesis and designing targeted treatment strategies, and offers new directions for further research on potential disease targets.