---
title: An improved dataset for predicting mammal infecting viruses from genetic sequence information.
title_zh: 一个用于根据遗传序列信息预测感染哺乳动物病毒的改进数据集
authors: "Reddy T, Schneider A, Hall AR, Witmer A, Hengartner N., Tyler Reddy, Austin Schneider, Aaron R Hall, Adam Witmer, Nick Hengartner"
date: 2026-03-27
pdf: "https://pubmed.ncbi.nlm.nih.gov/41894437/"
tags: ["query:pathoai"]
score: 9.0
evidence: 机器学习预测感染哺乳动物的病毒
tldr: 针对从基因序列预测病毒是否感染人类的任务，现有模型因数据集不统一难以比较。本研究通过扩充文献证据，构建了一个包含哺乳动物和灵长类标签的标准化数据集，并评估了8种机器学习模型。结果显示，模型表现高度依赖训练集与测试集的系统发育距离；当测试集包含全新的病毒科时，预测准确率降至随机水平。这为评估病毒跨物种传播风险提供了更严谨的基准。
selection_source: fresh_fetch
motivation: 解决现有病毒宿主预测模型因数据集、特征和评估标准不统一而导致难以直接比较和验证的问题。
method: 扩充了已有的病毒-宿主记录数据集，引入更广泛的分类标签，并对比了不同数据划分策略及k-mer特征对8种模型性能的影响。
result: 发现模型在预测更广泛的宿主类别时表现更好，但当训练集与测试集不存在病毒科重叠时，所有模型的预测表现均退化至随机水平。
conclusion: 现有的基于序列的机器学习模型在面对完全陌生的病毒家族时缺乏泛化能力，这提示在预测新兴人畜共患病毒时需谨慎对待模型结果。
---

## 摘要
已有多次尝试开发机器学习（ML）模型，以从基因组序列中识别感染人类的病毒，并取得了不同程度的成功。模型之间的直接比较存在困难，因为这些模型通常在不同的数据集上进行训练和评估，且采用了不同的数据划分方案、特征和模型性能指标。在本文中，我们提出了一个感染和非感染哺乳动物病毒病原体的标准化数据集，该数据集在 Mollentze 等人之前工作的基础上进行了改进，纳入了最新的文献证据，使社区可用的经过策划的宿主-病毒记录数量增加了一倍左右，并增加了新的宿主目标标签：灵长类动物和哺乳动物。包含新的宿主标签有几个原因，包括之前的报告显示在更广泛的分类等级上分类性能更好，以及灵长类动物感染的数据可能作为人畜共患潜力的合适代理，并能避免因缺乏证据而导致的感染人类的假阳性。基于该数据集，我们报告了八种机器学习模型在根据基因组序列预测感染哺乳动物病毒方面的性能。我们发现，与 Mollentze 等人最初的训练/测试集分配相比，在改进的数据集中随机分配案例到训练/测试集，将预测人类感染的总体平均 ROC AUC 从 0.663 ± 0.070 提高到 0.784 ± 0.013，这与训练集和测试集之间系统发育距离的减少一致（相对熵从 3.00 变为 0.08）。最广泛的宿主类别（哺乳动物感染）的预测最为可靠，达到 0.850 ± 0.020。我们分享了改进的数据集和代码，以实现预测人类宿主感染的机器学习方法的标准化比较。总的来说，我们提出了初步证据，表明病毒宿主感染的分类在更高的分类等级上更易处理；不出所料，减少训练集和测试集之间的系统发育距离可以提高预测性能；肽 k-mer 特征似乎对样本外模型性能有害；我们还面临一个问题，即考虑到病毒可能没有共同祖先的可能性，是否可以合理地预期病毒宿主预测模型在样本外场景中表现良好。与这一担忧一致的是，当对数据进行重新采样，使得训练集和测试集中的病毒科之间没有重叠时（相对熵 > 24），无论是否包含 k-mer，模型在预测人类感染方面的表现都不优于随机概率（ROC AUC 0.50 ± 0.08 或 0.50 ± 0.04）。

## Abstract
There have been several attempts to develop machine learning (ML) models to identify human infecting viruses from their genomic sequences, with varying degrees of success. Direct comparison between models is problematic, because these models are typically trained and evaluated on different datasets with alternative data splitting schemes, features, and model performance metrics. In this paper we present a standardized dataset of mammal infecting and non-infecting viral pathogens, refined from the previous work of Mollentze et al. to include the latest literature evidence, roughly doubling the number of curated host-virus records available to the community, and new host target labels, primate and mammal. The new host labels were included for several reasons, including previous reports that classification performance is better at broader taxonomic ranks and the idea that there may be more data for primate infection that might serve as a suitable proxy for zoonotic potential and avoidance of false positives for human infection due to absence of evidence. On this dataset, we report the performance of eight machine learning models for predicting mammal-infecting viruses from their genomic sequences. We find that randomly assigning cases in our improved dataset to training/testing sets, when compared to the original assignments into training/testing in Mollentze et al., increases the overall average ROC AUC of prediction of human infection from 0.663 ± 0.070 to 0.784 ± 0.013, consistent with the reduction in phylogenetic distance between train and test sets (relative entropy change from 3.00 to 0.08). The broadest host category of mammal infection can be predicted most reliably at 0.850 ± 0.020. We share our improved dataset and code to enable standardized comparisons of machine learning methods to predict human host infections. Overall, we have presented preliminary evidence that classification of virus host infection is more tractable at higher taxonomic ranks, that unsurprisingly reducing the phylogenetic distance between training and test sets can improve predictive performance, that peptide kmer features appear to be harmful to out of sample model performance, and we are left with the question of whether models for virus host prediction can reasonably be expected to perform well in out of sample scenarios given the likelihood that viruses do not share a common ancestor. Consistent with this concern, when the data is resampled such that there is no overlap between viral families in training and test sets (relative entropy > 24), models perform no better than random chance at prediction of human infection regardless of whether kmers are included (ROC AUC 0.50 ± 0.08) or not (ROC AUC 0.50 ± 0.04).

---

## 论文详细总结（自动生成）

### 1. 这篇论文在解决什么问题？
这篇论文主要解决**“如何利用病毒的基因序列准确预测其是否能感染人类或哺乳动物”**这一核心挑战。

**为什么值得看：**
*   **消除“刷榜”水分：** 现有的病毒宿主预测模型（ML）虽然号称准确率很高，但因为各家用的数据集、测试集划分方式、评价指标都不统一，导致无法公平比较。
*   **揭示泛化困境：** 论文通过严谨的实验证明，目前的 AI 模型在面对“从未见过”的病毒家族时，预测能力几乎等同于瞎猜。这对于预测未来可能出现的“X 病毒”（未知的新发传染病）具有重要的警示意义。

---

### 2. 白话版概述
想象我们要训练一个 AI 来识别哪些毒蛇会咬人。如果训练集里有“眼镜王蛇”，测试集里有“眼镜蛇”，AI 靠记忆就能拿高分。但如果测试集里出现了一种 AI 从没见过的“深海毒蛇”，它还能预测准吗？
这篇论文通过扩充数据集，对比了 8 种 AI 模型。结果发现：如果测试的病毒和训练的病毒“长得像”（亲缘关系近），AI 表现很好；但如果测试的是一个全新的病毒家族，AI 的准确率就会跌到 50%（和抛硬币随机猜没区别）。

---

### 3. 方法部分
*   **核心思想：** 构建一个标准化的“基准考试卷”（Benchmark Dataset），并测试不同“难度”的考试方式（数据划分策略）对模型性能的影响。
*   **数据集改进：** 在前人（Mollentze 等）的基础上，通过查阅最新文献，将病毒-宿主记录增加了一倍。
*   **标签设计：** 除了“是否感染人类”，还新增了“是否感染灵长类”和“是否感染哺乳动物”两个更宽泛的标签。
*   **特征工程：** 主要使用基因序列的 **k-mer**（即长度为 k 的短片段，类似文本处理中的 n-gram）。研究了核苷酸（DNA/RNA）和肽段（蛋白质）两种层面的 k-mer。
*   **关键取舍：** 论文重点对比了**“随机划分”**（训练集和测试集可能有同科病毒）和**“按科划分”**（测试集里的病毒家族在训练集中从未出现）。

---

### 4. 实验部分
*   **数据：** 包含数千条经过人工策划的病毒基因组及其宿主信息。
*   **模型：** 评估了 8 种常见的机器学习模型（如随机森林、梯度提升树等）。
*   **评价指标：** 主要使用 **ROC AUC**（衡量分类器好坏的指标，1.0 是完美，0.5 是随机）。
*   **主要结果：**
    1.  **分类等级越高越准：** 预测“是否感染哺乳动物”（AUC 0.85）比预测“是否感染人类”（AUC 0.78）更容易。
    2.  **距离决定性能：** 训练集和测试集在进化树上越近（系统发育距离小），得分越高。
    3.  **泛化性溃败：** 当强制要求测试集中的病毒属于全新的“科”（Family）时，所有模型的 AUC 均掉到 **0.5 左右**。
    4.  **特征陷阱：** 发现肽段 k-mer 特征在处理样本外数据时反而有害，可能导致模型过拟合。

---

### 5. 资源与算力
*   **文中未充分披露。** 考虑到使用的是传统的机器学习模型（非超大规模 Transformer），通常单机服务器或高性能工作站即可完成训练。

---

### 6. 真正可信的贡献
*   **高质量数据集：** 提供了一个目前最全面、经过人工校验的病毒-宿主关联数据集，并开源了代码。
*   **戳破了幻觉：** 强力证明了**目前的序列预测模型无法跨越“病毒科”进行外推**。这意味着现有的 AI 工具在预测完全新型的、跨物种传播的病毒时，可靠性极低。

---

### 7. 局限与风险
*   **数据偏差（Absence of Evidence）：** 很多病毒被标记为“不感染人类”，可能只是因为人类还没被它感染过，或者还没被发现，这会导致标签存在噪声。
*   **缺乏生物学机制：** 仅靠 k-mer 统计特征，无法捕捉病毒包膜蛋白与人类细胞受体结合的复杂物理化学过程。
*   **外推风险：** 论文明确指出，模型在面对进化起源不同的病毒时，没有学习到“通用的感染规律”。

---

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群：** 从事新发传染病预警、病毒基因组分析、以及关注 AI 模型泛化性问题的研究者。
*   **后续可跟进的问题：** 如何引入**蛋白质三维结构信息**或**宿主-病毒相互作用网络**，来打破“无法跨家族预测”的魔咒？单纯靠序列统计（k-mer）看来已经触及天花板了。

（完）
