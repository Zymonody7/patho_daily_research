---
title: Sequence Display enables large-scale sequence-activity datasets for rapid protein evolution.
title_zh: Sequence Display 能够生成用于快速蛋白质进化的大规模序列-活性数据集
authors: "Linqi Cheng, Xinzhe Zheng, Shiyu Jason Jiang, Yu Hu, Yijie Liu, Kaiqiang Yang, Jinyan Rui, Haoxue Ding, Mengxi Zhang, Teng Yuan, Qianglan Lu, Haoxin Ye, Chen-Long Li, Yiming Guo, Zuotong Tian, Anna Qin, Boyang Zhou, Kevin K Yang, Xiongyi Huang, Han Xiao"
date: 2026-04-08
pdf: "https://pubmed.ncbi.nlm.nih.gov/41951911/"
tags: ["query:bioinfo"]
score: 9.0
evidence: 将序列-活性数据集与预训练蛋白质语言模型集成
tldr: 针对蛋白质工程中多轮筛选效率低下的难题，本研究开发了 Sequence Display 平台，可在单轮实验中生成大规模蛋白质序列-活性数据集。该平台通过多路复用技术评估变体活性，并结合预训练蛋白质语言模型构建精细的活性景观。实验证明，该方法成功进化出具有更广 PAM 识别能力的 Cas9 和新型氨酰-tRNA 合成酶，为加速生物医学功能蛋白的发现提供了高效的数据驱动方案。
selection_source: fresh_fetch
motivation: 传统的蛋白质定向进化过程通常需要耗时的多轮筛选，且难以在单次实验中获取大规模的序列与功能对应数据。
method: 研发了 Sequence Display 实验平台，通过单轮高通量实验并行测定大量蛋白质变体的活性，并利用预训练语言模型对活性景观进行建模。
result: 成功在 Cas9 核酸酶和氨酰-tRNA 合成酶等多种蛋白上生成了高质量数据集，并筛选出具有扩展识别能力的功能变体。
conclusion: Sequence Display 结合机器学习模型显著提升了蛋白质功能映射的效率，是加速蛋白质工程和药物研发的有力工具。
---

## 摘要
工程化具有所需功能的蛋白质仍然具有挑战性，通常需要多轮筛选和选择。在这里，我们介绍了 Sequence Display，这是一个能够在单轮实验中生成大规模蛋白质序列-活性数据集的平台。Sequence Display 能够在单次实验中对单个变体的活性进行多路评估，为绘制详细的序列-功能关系图谱提供了一种稳健的方法。我们通过为胞嘧啶脱氨酶、尿嘧啶糖苷酶抑制剂、氨酰-tRNA 合成酶和一种紧凑型 Cas9 核酸酶生成数据集，展示了该平台的广泛适用性。将从 Sequence Display 获得的数据集与预训练的蛋白质语言模型相结合，可以构建细粒度的、变体特异性的活性图谱。我们发现了几个具有扩展的原间隔序列临近基序（PAM）识别能力的 Cas9 变体，并进化出了能够识别不同非规范氨基酸的氨酰-tRNA 合成酶变体。总之，这项研究确立了 Sequence Display 作为绘制蛋白质活性图谱和加速发现用于生物和医学应用的优化蛋白质的强大工具。

## Abstract
Engineering proteins with desired functions remains challenging and usually requires multiple rounds of screening and selection. Here, we present Sequence Display, a platform that generates large-scale protein sequence-activity datasets in a single round. Sequence Display enables multiplexed assessment of individual variant activity within a single experiment, offering a robust approach to mapping detailed sequence-function relationships. We demonstrate the platform's broad applicability by generating datasets for cytosine deaminase, uracil glycosylase inhibitor, aminoacyl-tRNA synthetase and a compact Cas9 nuclease. Integrating these datasets obtained from Sequence Display with pretrained protein language models, fine-grained, variant-specific activity landscapes can be constructed. We discovered several Cas9 variants with expanded protospacer-adjacent motif recognition and evolved aminoacyl-tRNA synthetase variants capable of recognizing different noncanonical amino acids. Together, this study establishes Sequence Display as a powerful tool for mapping protein activity landscapes and accelerating the discovery of optimized proteins for biological and medical applications.

---

## 论文详细总结（自动生成）

这是一份关于论文《Sequence Display enables large-scale sequence-activity datasets for rapid protein evolution》的深度解析：

### 1. 解决的问题与核心价值
**解决的问题：** 传统的蛋白质工程（如定向进化）像是在黑暗中摸索。研究者通常需要进行多轮“突变-筛选-再突变”的循环，过程耗时耗力，且每次只能获取极少量变体的功能数据。这导致我们对蛋白质“序列-功能”映射关系（即适应性景观，Fitness Landscape）的理解非常碎片化。

**为什么值得看：** 该研究开发了一个名为 **Sequence Display** 的实验平台，它能像“高速摄影机”一样，在单次实验中并行测定成千上万个蛋白质变体的活性。更重要的是，它将这种高通量实验数据与 **AI 蛋白质语言模型（PLM）** 结合，实现了从“盲目筛选”到“精准预测”的跨越，极大地加速了功能蛋白（如基因编辑工具 Cas9）的改造进程。

---

### 2. 白话版概述
想象你要改良一把复杂的锁（蛋白质），传统方法是每次改一个零件试一次，效率极低。
1. **Sequence Display** 技术让你能一次性制造出几万把微小的“改版锁”，并让它们在同一个试管里去开对应的“钥匙”。
2. 通过高通量测序，你可以直接看到哪些锁开了，开了多少，从而获得一份详尽的“设计图-性能”对照表。
3. 接着，把这张表喂给 AI，AI 就能学会其中的规律，甚至预测出你还没制造出来的、性能更强的“超级锁”。

---

### 3. 方法部分：核心思想与设计
*   **核心思想：** 建立一种“物理连接”，让蛋白质的**功能表现**直接转化为**测序信号**。
*   **Sequence Display 平台：**
    *   **多路复用（Multiplexing）：** 在单细胞或单分子水平上，将蛋白质变体与其产生的生化结果（如 DNA 修饰、配体结合）绑定。
    *   **活性定量：** 通过计算测序数据中特定序列的富集程度或转化比例，给每个变体的活性打分。
*   **AI 模型集成：**
    *   **模型结构：** 使用预训练的蛋白质语言模型（如 ESM 系列，这类模型已在数亿条蛋白质序列上学习过通用规律）。
    *   **微调（Fine-tuning）：** 利用 Sequence Display 产生的高质量“序列-活性”数据集对模型进行有监督微调。
    *   **关键取舍：** 放弃了从零训练大模型，而是选择“预训练+下游微调”的策略，这在标注数据有限（相对于大模型参数量）的情况下能获得更好的泛化性能。

---

### 4. 实验部分：任务与结果
*   **实验对象：** 胞嘧啶脱氨酶、尿嘧啶糖苷酶抑制剂（UGI）、氨酰-tRNA 合成酶（aaRS）以及紧凑型 Cas9 核酸酶。
*   **关键任务：**
    1.  **Cas9 改造：** 寻找能识别更多种类 PAM（Cas9 寻找目标的“定位码”）的变体。
    2.  **aaRS 进化：** 寻找能识别非天然氨基酸的变体，用于合成新型生物材料。
*   **主要结果：**
    *   **数据规模：** 单次实验生成了包含数万个变体的高质量数据集。
    *   **预测精度：** AI 模型在测试集上的活性预测与实验观测值高度一致。
    *   **突破性发现：** 成功筛选出具有扩展 PAM 识别能力的 Cas9 变体，以及能高效处理非规范氨基酸的新型 aaRS。

---

### 5. 资源与算力
*   **文中未充分披露：** 论文重点在于实验平台的构建和生物学发现，未详细列出训练 AI 模型所消耗的具体 GPU 型号、核心数或计算时长。但基于其使用的预训练模型微调方法，通常单张高性能显卡（如 A100/H100）即可在数小时至数天内完成此类规模的微调。

---

### 6. 真正可信的贡献
1.  **高通量数据闭环：** 证明了 Sequence Display 产生的数据质量足以支撑 AI 模型的微调，实现了“湿实验数据驱动干实验预测”的闭环。
2.  **Cas9 的实际进化：** 发现的具有扩展 PAM 识别能力的 Cas9 变体具有极高的实用价值，直接拓宽了基因编辑的覆盖范围。
3.  **通用性验证：** 在四种完全不同功能的蛋白质上均取得成功，证明该方法不是“一锤子买卖”，具有普适性。

---

### 7. 局限与风险
*   **库容量限制：** 虽然是“大规模”，但相比于蛋白质近乎无限的突变空间（$20^n$），实验能覆盖的依然只是冰山一角。
*   **复杂功能难以表征：** 对于需要多步反应或复杂细胞环境配合的蛋白质功能，Sequence Display 的体外/简易系统可能无法完全模拟真实情况。
*   **外推能力风险：** AI 模型在训练数据附近的预测很准，但对于结构发生剧烈变化的“远端”突变，预测可靠性仍待验证。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事蛋白质工程、基因编辑工具开发、以及希望将实验数据与深度学习结合的 AI 研究员。
*   **后续可跟进的问题：** 如何利用**主动学习（Active Learning）**，让 AI 自动设计下一轮 Sequence Display 应该测试哪些序列，从而用最少的实验次数找到全局最优解？

（完）
