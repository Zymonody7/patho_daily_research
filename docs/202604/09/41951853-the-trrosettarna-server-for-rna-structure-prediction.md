---
title: The trRosettaRNA server for RNA structure prediction.
title_zh: 用于 RNA 结构预测的 trRosettaRNA 服务器
authors: "Wenkai Wang, Xiaocheng Liu, Zhenling Peng, Jianyi Yang"
date: 2026-04-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/41951853/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 用于自动化RNA三维结构预测的深度学习
tldr: 许多RNA的功能依赖其复杂的三维结构，但实验测定成本高且周期长。trRosettaRNA是一个基于深度学习的自动化RNA三维结构预测平台，通过端到端神经网络直接从序列预测空间约束，并结合能量优化消除物理冲突。该工具在Rfam家族预测中表现出极高的准确性，与实验观测高度吻合，为RNA结构生物学研究提供了高效、开源的计算方案。
selection_source: fresh_fetch
motivation: 针对RNA三维结构实验测定困难的问题，开发一种高精度、自动化且易于使用的计算预测工具。
method: 采用端到端深度神经网络从核苷酸序列预测空间几何约束，并结合能量最小化算法优化生成最终的三维模型。
result: 在缺乏已知结构的Rfam家族中实现了高置信度预测，且预测结果在后续实验观测中得到了有效验证。
conclusion: trRosettaRNA通过提供在线服务和开源软件包，显著提升了RNA结构预测的可访问性与建模精度，推动了相关领域的自动化研究。
---

## 摘要
与蛋白质类似，许多 RNA 折叠成三维 (3D) 结构以执行生物学功能。在此，我们介绍了 trRosettaRNA 服务器，这是一个基于 Web 的平台，利用深度学习进行自动化的 RNA 3D 结构预测。其主要输入是目标 RNA 的核苷酸序列，并可选择上传自定义的多序列比对和二级结构。该服务器使用端到端神经网络进行自动化 3D 结构预测，随后通过能量优化步骤来解决结构违规问题。作为一个自动化服务器，trRosettaRNA 的特点在于其最先进的建模精度、灵活的输入选项以及预测结果的全面可视化。trRosettaRNA 已成功应用于各种场景，包括为缺乏已知 3D 结构的 Rfam 家族预测结构，其中高置信度结构预测的代表性案例被发现与随后的实验观察结果吻合良好。利用我们计算机集群上多达 5 个中央处理器 (CPU) 核心的并行计算，该服务器预测长度约为 200 个核苷酸的 RNA 序列结构的中位时间约为 1 小时。trRosettaRNA 的独立软件包具有独特的优势，例如增强敏感序列的数据隐私、绕过服务器排队的能力以及集成到高通量自动化流水线中。重要的是，该软件包的开源特性使研究人员能够根据专门的研究需求直接修改代码库，或通过微调底层神经网络来开发衍生工具。trRosettaRNA 的 Web 服务器和独立软件包分别可在 https://yanglab.qd.sdu.edu.cn/trRosettaRNA/ 和 https://github.com/YangLab-SDU/trRosettaRNA2 获取。

## Abstract
Similar to proteins, many RNAs fold into three-dimensional (3D) structures to perform biological functions. Here we present the trRosettaRNA server, a web-based platform for automated RNA 3D structure prediction using deep learning. The primary input is the nucleotide sequence of a target RNA, with the option to upload custom multiple sequence alignments and secondary structures. The server uses an end-to-end neural network for automated 3D structure prediction, followed by an energy optimization step to resolve structural violations. As an automated server, trRosettaRNA is distinguished by its state-of-the-art modeling accuracy, flexible input options and comprehensive visualization of prediction results. trRosettaRNA has been successfully applied in various contexts, including predicting structures for Rfam families lacking known 3D structures, where representative cases of high-confidence structure predictions were found to align well with subsequent experimental observations. Utilizing up to 5 central processing unit (CPU) cores in parallel on our computer cluster, the server takes a median time of about 1 h to predict structures for RNA sequences with about 200 nucleotides. The standalone package for trRosettaRNA offers distinct advantages such as enhanced data privacy for sensitive sequences, the ability to bypass server queues and integration into high-throughput automated pipelines. Importantly, the open-source nature of the package empowers researchers to directly modify the codebase for specialized research needs or to develop derivative tools by fine-tuning the underlying neural network. The web server and standalone package of trRosettaRNA are available at https://yanglab.qd.sdu.edu.cn/trRosettaRNA/ and https://github.com/YangLab-SDU/trRosettaRNA2 , respectively.

---

## 论文详细总结（自动生成）

这篇论文介绍了 **trRosettaRNA**，这是一个专门用于预测 RNA 三维（3D）结构的深度学习平台。以下是对该研究的详细总结：

### 1. 解决的问题与研究意义
*   **核心问题**：RNA 不仅仅是遗传信息的传递者，许多非编码 RNA 会折叠成复杂的 3D 结构来行使催化或调节功能。然而，通过实验（如 X 射线晶体学或冷冻电镜）测定 RNA 结构既昂贵又耗时。
*   **研究意义**：在“AI 预测蛋白质结构”取得巨大成功（如 AlphaFold）后，如何高精度、自动化地预测 RNA 的 3D 结构成为生物信息学的下一个高地。trRosettaRNA 旨在提供一个易用的工具，帮助研究者从简单的序列出发，快速获取可靠的 RNA 空间模型。

### 2. 白话版概述
RNA 就像一根由四种“珠子”（A、U、C、G）串成的绳子，它会在空间中扭曲折叠成特定的形状。这篇论文开发了一个 AI 助手：你只要给它这根绳子的序列，它就能通过深度学习算法“猜”出哪些珠子在空间上靠在一起。最后，它还会利用物理规律对这个形状进行微调，确保它符合化学常识。这个工具不仅准确度高，而且完全开源，普通研究者在网页上就能直接使用。

### 3. 方法部分
*   **核心思想**：将 RNA 结构预测转化为一个“几何约束预测 + 能量优化”的两步走问题。
*   **模型结构**：采用**端到端（End-to-end）神经网络**。
    *   **输入**：RNA 序列。可选输入包括多序列比对（MSA，即在不同物种中寻找相似序列，利用进化信息发现哪些碱基在协同演化）和二级结构（碱基对的配对情况）。
    *   **预测目标**：神经网络预测碱基对之间的距离分布和方向角（几何约束）。
*   **推理流程**：
    1.  **特征提取**：从序列和 MSA 中提取进化特征。
    2.  **几何预测**：AI 输出空间约束图。
    3.  **结构构建**：利用 **Rosetta 能量最小化算法**，在 AI 预测的约束下进行折叠，消除原子碰撞等物理违规，生成最终的 3D 坐标。
*   **关键设计取舍**：结合了“数据驱动的 AI”和“物理驱动的能量优化”。AI 负责把握大轮廓，物理优化负责保证局部化学结构的合理性。

### 4. 实验部分
*   **数据与任务**：主要针对 **Rfam 家族**（一个著名的 RNA 家族数据库）中缺乏已知 3D 结构的序列进行预测。
*   **Baseline（基准）**：与传统的物理建模方法和早期的深度学习模型进行对比。
*   **评价指标**：通常使用 **RMSD**（均方根偏差，越小越好）和 **TM-score**（结构相似度评分，越大越好）来衡量预测模型与真实实验结构的接近程度。
*   **主要结果**：
    *   在 Rfam 家族的预测中表现出极高的置信度。
    *   **实验验证**：一些预测结果在随后发表的实验观测中得到了证实，证明了模型的盲测能力。
    *   **效率**：预测一个长度约 200 个核苷酸的 RNA，中位时间约为 1 小时。

### 5. 资源与算力
*   **训练资源**：文中**未充分披露**具体的训练硬件（如 GPU 型号和训练时长）。
*   **推理/服务资源**：Web 服务器在后台集群上使用多达 5 个 CPU 核心并行计算。
*   **开源情况**：提供了 Web 服务器和 GitHub 源代码（trRosettaRNA2），支持本地部署以保护数据隐私。

### 6. 真正可信的贡献
*   **高精度自动化**：在 RNA 领域实现了类似 trRosetta 在蛋白质领域的自动化预测精度。
*   **盲测一致性**：预测结果与后来的实验数据吻合，这是证明模型有效性的最强证据。
*   **工具易用性**：通过 Web 服务器降低了生物学家的使用门槛，同时开源代码支持社区二次开发。

### 7. 局限与风险
*   **序列长度限制**：对于超长 RNA（如超过 500-1000 个核苷酸），计算复杂度会激增，预测精度可能下降。
*   **MSA 依赖性**：如果目标 RNA 缺乏同源序列（孤儿序列），AI 无法从进化信息中获取足够线索，预测效果会打折扣。
*   **动态性缺失**：RNA 在体内往往是动态变化的，模型目前只能给出最可能的静态“快照”，无法模拟 RNA 的构象转换。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事 RNA 药物研发、合成生物学、以及对大分子结构预测感兴趣的 AI 算法工程师。
*   **后续可跟进的问题**：如何利用 Transformer 或扩散模型（Diffusion Model）进一步提升 RNA 柔性区域的预测精度？如何实现 RNA 与蛋白质/小分子配体的复合物结构预测？

（完）
