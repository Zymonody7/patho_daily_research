---
title: Transcriptomic Plasticity Is a Hallmark of Metastatic Pancreatic Cancer.
title_zh: 转录组塑性是转移性胰腺癌的一个显著特征。
authors: "Alejandro Jiménez-Sánchez, Sitara Persad, Akimasa Hayashi, Shigeaki Umeda, Roshan Sharma, Yubin Xie, Arnav Mehta, Wungki Park, Ignas Masilionis, Tinyi Chu, Feiyang Zhu, Jungeui Hong, Ronan Chaligne, Eileen M O'Reilly, Linas Mazutis, Tal Nawy, Itsik Pe'er, Christine A Iacobuzio-Donahue, Dana Pe'er"
date: 2026-04-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/41379552/"
tags: ["query:seqai"]
score: 6.0
evidence: 单细胞转录组图谱及基于测序数据的系统发育推断
tldr: 胰腺癌转移是导致死亡的主因，但癌细胞如何适应不同器官环境尚不明确。本研究通过对一名胰腺癌患者的多个转移灶进行单细胞转录组测序，并开发了 PICASSO 算法来推断克隆演化路径。研究发现，转移灶的表型差异主要由环境诱导的转录组可塑性决定，而非遗传克隆背景。这一发现揭示了环境对高度可塑性癌细胞的强力塑造作用，为针对性治疗转移性癌症提供了新视角。
selection_source: fresh_fetch
motivation: 旨在探究胰腺癌细胞在向不同器官转移过程中，是如何通过基因表达调整来适应截然不同的局部环境的。
method: 利用快速尸检获取的单细胞转录组数据，结合新开发的 PICASSO 概率推断算法，将细胞的克隆演化背景与其转录组表型进行关联分析。
result: 发现不同转移部位（如肝、胃壁等）的癌细胞展现出独特的基因程序，且这些表型差异与细胞的遗传克隆结构几乎无关。
conclusion: 胰腺癌的转移过程主要受环境驱动的转录组可塑性主导，而非特定遗传克隆的选择性扩张。
---

## 摘要
转移是癌症死亡的主要原因。为了制定拦截转移进展的策略，需要更好地理解肿瘤细胞如何适应截然不同的器官环境。为了研究这一问题，研究人员通过对一名接受快速尸检的胰腺导管腺癌患者的原发肿瘤和多种转移样本（肝脏、大网膜、腹膜、胃壁、淋巴结和横膈膜）进行分析，生成了单细胞转录组图谱。利用无监督原型分析，识别出了共有和位点特异性的基因程序，包括分别在腹膜和胃壁病变中普遍存在的脂质代谢和胃肠道程序。我们开发了 PICASSO（从单细胞测序观察中的拷贝数变异进行系统发育推断），这是一种从单细胞和匹配的全外显子组测序数据中推断克隆系统发育的概率方法。将 PICASSO 生成的克隆结构与表型特征进行比较后发现，胰腺癌细胞在适应局部环境时，克隆基因型的贡献极小。我们的结果提出了一种范式，即在转移扩散过程中，高度塑性的癌细胞会受到强烈的环境影响。意义：通过对一名胰腺癌患者快速尸检样本的原发肿瘤和转移灶进行单细胞转录组分析，并结合 PICASSO 的概率克隆推断，揭示了转移细胞中显著的转录组塑性。本文是专题系列“利用计算研究、数据科学和机器学习/人工智能驱动癌症发现”的一部分。

## Abstract
UNLABELLED: Metastasis is the leading cause of cancer deaths. To develop strategies for intercepting metastatic progression, a better understanding of how tumor cells adapt to vastly different organ contexts is needed. To investigate this question, a single-cell transcriptomic atlas of primary tumors and diverse metastatic samples (liver, omentum, peritoneum, stomach wall, lymph node, and diaphragm) from a patient with pancreatic ductal adenocarcinoma who underwent rapid autopsy was generated. Using unsupervised archetype analysis, both shared and site-specific gene programs were identified, including lipid metabolism and gastrointestinal programs prevalent in peritoneal and stomach wall lesions, respectively. We developed phylogenetic inference from copy-number alterations in single-cell sequencing observations (PICASSO) as a probabilistic approach for inferring clonal phylogeny from single-cell and matched whole-exome sequencing data. Comparison of PICASSO-generated clonal structure with phenotypic signatures revealed that pancreatic cancer cells adapted to local environments with minimal contribution from clonal genotype. Our results suggest a paradigm whereby strong environmental effects are imposed on highly plastic cancer cells during metastatic dissemination. SIGNIFICANCE: Single-cell transcriptional profiling of primary tumor and metastases from rapid autopsy samples of an individual with pancreatic cancer, combined with probabilistic clonal inference by PICASSO, reveals substantial transcriptomic plasticity in metastatic cells. This article is part of a special series: Driving Cancer Discoveries with Computational Research, Data Science, and Machine Learning/AI .