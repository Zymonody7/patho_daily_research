---
title: "Treemble: A Graphical Tool to Generate Newick Strings from Phylogenetic Tree Images."
title_zh: Treemble：一种从系统发育树图像生成 Newick 字符串的图形化工具。
authors: "Allard JB, Kumar S., John B Allard, Sudhir Kumar"
date: 2026-04-22
pdf: "https://pubmed.ncbi.nlm.nih.gov/42018742/"
tags: ["query:pathoai"]
score: 7.0
evidence: 系统发育树转换的图形工具
tldr: 针对生物学文献中大量进化树仅以图像形式存在、缺乏机器可读 Newick 格式的问题，Treemble 推出了一款跨平台桌面应用。该工具结合深度学习节点检测模型与用户交互点击，能从矩形或圆形进化树图像中精准提取节点坐标并自动重构拓扑结构，同时支持末端标签的自动识别。这为研究者从既有文献中回收进化数据、进行超树构建和后续分析提供了高效且低误的解决方案。
selection_source: fresh_fetch
motivation: 科学文献中海量的进化树以视觉图像而非机器可读格式存储，导致这些数据难以被直接用于后续的计算分析。
method: 采用深度学习模型辅助检测图像中的节点位置，并结合用户交互与拓扑重构算法生成 Newick 格式字符串。
result: 成功开发出支持矩形和圆形进化树的图形化工具，能够自动识别节点和末端标签并导出标准数据格式。
conclusion: Treemble 降低了从图像中手动提取进化信息的门槛，是生物信息学领域数据回收和整合的实用工具。
---

## 摘要
摘要：系统发育树在生物学中无处不在且处于核心地位，但大多数已发表的树仅以视觉图表的形式存在，而非机器可读的 Newick 格式。因此，科学文献中存在成千上万个已发表的树，无法用于后续分析、比较和超树构建。专家可以轻松阅读此类图表，但从图表中手动构建 Newick 字符串既费力、易错又耗时。此前半自动化读取树图像的尝试依赖于图像处理技术。由于典型的已发表树图包含各种与分支重叠的图形元素和注释（例如内部节点上的误差棒），这些技术往往面临困难。在此，我们介绍了 Treemble，这是一个用于从树图像生成 Newick 字符串的用户友好型桌面应用程序。用户只需点击以标记节点位置，在基于深度学习的节点检测工具的辅助下，Treemble 仅根据节点坐标即可通过算法组装出树。Treemble 还支持自动读取末端名称标签，并可用于矩形和圆形树。可用性与实现：Treemble 是适用于 macOS 和 Windows 的原生桌面应用程序，可在 treemble.org 免费获取并附有文档。源代码可在 github.com/John-Allard/Treemble 获取。训练好的节点检测模型可在 huggingface.co/John-Allard/treemble-1 获取。补充信息：补充数据可在 Bioinformatics 在线版获取。

## Abstract
SUMMARY: Phylogenetic trees are ubiquitous and central to biology, but most published trees are available only as visual diagrams and not in the machine-readable Newick format. There are, thus, thousands of published trees in the scientific literature that are unavailable for follow-up analyses, comparisons, and supertree construction. Experts can easily read such diagrams, but the manual construction of a Newick string from a diagram is laborious, error prone, and time-consuming. Previous attempts to semi-automate the reading of tree images relied on image processing techniques. These often encounter difficulties as typical published tree diagrams contain various graphical elements and annotations that overlap the branches, such as error bars on internal nodes. Here we introduce Treemble, a user-friendly desktop application for generating Newick strings from tree images. The user simply clicks to mark node locations, assisted by a deep learning-based node detection tool, and Treemble algorithmically assembles the tree from the node coordinates alone. Treemble also facilitates the automatic reading of tip name labels and can be used for both rectangular and circular trees. AVAILABILITY AND IMPLEMENTATION: Treemble is a native desktop application for macOS and Windows and is freely available, with documentation, at treemble.org. Source code is available at github.com/John-Allard/Treemble. The trained node detection model is available at huggingface.co/John-Allard/treemble-1. SUPPLEMENTARY INFORMATION: Supplementary data are available at Bioinformatics online.