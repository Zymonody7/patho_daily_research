---
title: Vector Encoding of Phylogenetic Trees by Ordered Leaf Attachment.
title_zh: 通过有序叶节点附着实现系统发育树的向量编码
authors: "Richman DH, Zhang C, Matsen FA., David Harry Richman, Cheng Zhang, Frederick A Matsen"
date: 2026-03-18
pdf: "https://pubmed.ncbi.nlm.nih.gov/41848929/"
tags: ["query:pathoai"]
score: 9.0
evidence: 用于机器学习的系统发育树向量编码
tldr: 针对系统发育树在机器学习中难以向量化表示的问题，本文提出“有序叶节点附加”（OLA）方法，将二叉有根树拓扑唯一编码为整数向量。该方法实现了线性时间的编解码效率，且其向量空间定义的距离与传统的 NNI 和 SPR 距离相关，为进化树数据的自动化分析提供了高效的数学表征工具。
selection_source: fresh_fetch
motivation: 旨在为系统发育树寻找一种计算简便、唯一且能与机器学习算法兼容的向量化编码方式。
method: 通过有序地将叶节点附加到现有树结构上的过程，将树拓扑转换为符合特定约束的整数序列。
result: 证明了该编码在节点数量上呈线性时间复杂度，并分析了其诱导距离与经典树拓扑距离度量的关联。
conclusion: OLA 编码凭借其线性效率和良好的数学特性，成为连接系统发育学与现代机器学习技术的有效桥梁。
---

## 摘要
作为将系统发育学与机器学习联系起来的工作的一部分，近年来学术界对系统发育树的向量编码产生了浓厚的兴趣。我们提出了一种简单的新型“有序叶节点附着”（OLA）方法，用于将二叉有根系统发育树拓扑唯一地编码为整数向量。OLA 编码和解码的时间复杂度相对于叶节点数量呈线性，且对应于树的向量集合是整数序列中一个描述简单的子集。与其他现有编码相比，OLA 编码在具备这些特性方面具有唯一性。该整数向量编码在树集合上诱导了一种距离，我们研究了这种距离与 NNI 和 SPR 距离之间的关系。

## Abstract
As part of work to connect phylogenetics with machine learning, there has been considerable recent interest in vector encodings of phylogenetic trees. We present a simple new "ordered leaf attachment" (OLA) method for uniquely encoding a binary, rooted phylogenetic tree topology as an integer vector. OLA encoding and decoding take linear time in the number of leaf nodes, and the set of vectors corresponding to trees is a simply-described subset of integer sequences. The OLA encoding is unique compared to other existing encodings in having these properties. The integer vector encoding induces a distance on the set of trees, and we investigate this distance in relation to the NNI and SPR distances.