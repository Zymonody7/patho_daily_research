---
title: "DeepTYLCV: An interpretable and experimentally validated AI model for predicting virulence of different tomato yellow leaf curl virus strains."
title_zh: DeepTYLCV：一种用于预测不同番茄黄化曲叶病毒株系毒力的可解释且经实验验证的人工智能模型
authors: "Nattanong Bupi, Hariharan Sangaraju, Duong Thanh Tran, Vinoth Kumar Sangaraju, Hyojin Im, Minkwan Kim, Sukchan Lee, Balachandran Manavalan"
date: 2026-05-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42063254/"
tags: ["query:pathoai"]
score: 9.0
evidence: 深度学习从病毒基因组序列预测毒力
tldr: "番茄黄化曲叶病毒（TYLCV）严重威胁全球番茄产量，但传统诊断依赖视觉症状且难以区分毒力强弱。为此，研究者开发了DeepTYLCV深度学习框架，直接利用病毒基因组的开放阅读框序列，结合蛋白质语言模型与多尺度卷积神经网络来预测病毒毒力。该模型在15个未知分离株的实验验证中达到了100%的预测准确率，并通过可解释性分析识别了关键致病基序，为全球病毒监测和抗性育种提供了高效、精准的数字化工具。"
selection_source: fresh_fetch
motivation: 传统的番茄病毒诊断依赖肉眼观察或图像识别，受环境干扰大且无法在早期准确区分不同病毒株的致病性强弱。
method: 该模型通过整合蛋白质语言模型提取的全局特征与多尺度卷积神经网络捕捉的局部序列特征，直接从病毒基因组序列中预测其毒力等级。
result: 实验验证显示，DeepTYLCV对15个代表性病毒株的毒力预测与实际植株发病情况完全一致，且能通过可视化技术定位影响毒力的关键序列片段。
conclusion: 该研究提供了一个可解释且具备全球通用性的病毒监测平台，有助于在症状出现前实现精准的病害预警和管理。
---

## 摘要
番茄黄化曲叶病毒 (TYLCV) 是全球范围内影响番茄生产的最具破坏性的病原体之一，新出现的强毒力株系正日益克服遗传抗性并引发严重的疫情。传统的田间诊断依赖于视觉检查或基于图像的人工智能模型，仍受限于对症状的依赖、环境变异性以及较差的株系级可解释性。为了应对这些挑战，我们推出了 DeepTYLCV，这是一种新型深度学习框架，可直接根据病毒基因组衍生的开放阅读框序列进行准确的毒力预测。我们首先构建了一个包含全球来源的 TYLCV 序列的综合数据集，并根据毒力标注进行了整理。DeepTYLCV 利用由 Transformer 编码器和多尺度卷积神经网络组成的混合架构，将基于蛋白质语言模型的嵌入与最优拼接的传统描述符相结合，从而能够有效提取全局和局部序列特征。基准测试分析表明，DeepTYLCV 的性能显著优于我们之前开发的 IML-TYLCV 模型，后者是在韩国分离株上训练的，缺乏全球泛化能力。重要的是，对 15 个未表征或具有代表性的 TYLCV 分离株进行的盲测预测在番茄植株中得到了实验验证，模型预测与观察到的症状严重程度之间达到了 100% 的一致性。此外，基于 1D-Grad-CAM++ 的可解释性分析显示，该模型始终关注与强毒力株系相关的序列基序，为症状严重程度提供了机制见解。DeepTYLCV 已在 https://balalab-skku.org/DeepTYLCV/ 公开发布，为番茄栽培中的早期 TYLCV 监测、抗性监控和战略性疾病管理提供了一个强大、可解释且具有全球扩展性的平台。

## Abstract
Tomato yellow leaf curl virus (TYLCV) is among the most devastating pathogens affecting tomato production worldwide, with emerging virulent strains increasingly overcoming genetic resistance and triggering severe outbreaks. Traditional field diagnosis, reliant on visual inspection or image-based AI models, remains constrained by symptom dependence, environmental variability, and poor strain-level interpretability. To address these challenges, we introduce DeepTYLCV, a novel deep learning framework for accurate virulence prediction directly from viral-genome-derived open reading frame sequences. We first constructed a comprehensive dataset of globally sourced TYLCV sequences curated by virulence annotations. DeepTYLCV integrates protein language model-based embeddings with optimal concatenated conventional descriptors using a hybrid architecture composed of a transformer encoder and a multi-scale convolutional neural network, enabling effective extraction of both global and local sequence features. Benchmark analyses demonstrate that DeepTYLCV significantly outperforms our previously developed IML-TYLCV model, which was trained on Korean isolates and lacked global generalizability. Importantly, blind predictions on 15 uncharacterized or representative TYLCV isolates were experimentally validated in tomato plants, achieving 100% concordance between model predictions and observed symptom severity. Furthermore, 1D-Grad-CAM++-based interpretability analyses revealed that the model consistently focused on relevant sequence motifs associated with severe strains, offering mechanistic insights into symptom severity. DeepTYLCV is publicly available at https://balalab-skku.org/DeepTYLCV/ and represents a powerful, interpretable, and globally scalable platform for early TYLCV surveillance, resistance monitoring, and strategic disease management in tomato cultivation.

---

## 论文详细总结（自动生成）

这篇论文介绍了一个名为 **DeepTYLCV** 的深度学习模型，旨在通过分析病毒的基因序列，精准预测**番茄黄化曲叶病毒（TYLCV）**的致病力（毒力）强弱。

### 1. 解决的问题与研究意义
*   **核心问题**：番茄黄化曲叶病毒（TYLCV）是全球番茄减产的主要元凶。虽然现在有基于图像识别的 AI 来诊断病害，但那是“马后炮”——看到症状时植物已经病重。此外，不同地区的病毒株系“毒性”不同，传统的视觉诊断无法区分哪些是强毒株，哪些是弱毒株。
*   **研究意义**：如果能直接从病毒的基因组序列（DNA/蛋白质序列）预测其毒力，就能在疫情爆发前进行预警，并帮助育种家筛选抗性更强的番茄品种。

### 2. 白话版概述
想象病毒是一段恶意代码。有些代码只是让电脑变慢（弱毒），有些则会直接格式化硬盘（强毒）。过去人们靠看电脑死机后的样子来判断病毒，而这篇论文开发了一个“智能扫描仪”。它直接阅读病毒的底层代码（蛋白质序列），结合了“理解语言的 AI”（类似 ChatGPT 的蛋白质语言模型）和“找局部特征的 AI”（卷积神经网络），在病毒还没感染植物前，就能准确算出它的破坏力有多大。

### 3. 方法部分
*   **核心思想**：将病毒的**开放阅读框（ORF，即基因中负责编码蛋白质的片段）**序列视为一种“语言”，通过融合全局语义特征和局部结构特征来判定毒力。
*   **模型结构**：
    *   **特征提取层**：采用双路并行。一路使用**蛋白质语言模型（pLM）**提取全局上下文嵌入（Embedding）；另一路使用传统的生物信息学描述符（如氨基酸组成等）。
    *   **混合架构**：使用 **Transformer 编码器**来捕捉序列中的长距离依赖关系，同时配合**多尺度卷积神经网络（Multi-scale CNN）**，利用不同大小的卷积核抓取关键的局部基序（Motifs）。
    *   **可解释性设计**：引入了 **1D-Grad-CAM++** 技术。这就像给 AI 装了热力图，能显示出序列中哪些具体的氨基酸片段导致了 AI 判定其为“强毒株”。
*   **关键取舍**：研究者放弃了单一的序列比对方法，转而采用“语言模型+传统特征”的混合模式，以克服单一模型在处理全球不同变异株时泛化能力差的问题。

### 4. 实验部分
*   **数据与任务**：构建了一个全球范围的 TYLCV 序列数据集，标注为“强毒（Severe）”或“弱毒（Mild）”。
*   **Baseline（对比基准）**：对比了该团队之前开发的 IML-TYLCV 模型（仅针对韩国株系训练）。
*   **评价指标**：准确率（Accuracy）、F1 分数、MCC（马修斯相关系数）等。
*   **主要结果**：
    *   DeepTYLCV 在各项指标上均显著优于旧模型，展现了极强的全球通用性。
    *   **盲测验证**：对 15 个未知的病毒株系进行预测，并同步在真实的番茄植株上进行接种实验。结果显示，**AI 预测结果与实验室观察到的植株发病严重程度 100% 一致**。

### 5. 资源与算力
*   文中提到该模型已部署为在线 Web 服务器（https://balalab-skku.org/DeepTYLCV/）供全球研究者使用。
*   关于具体的训练硬件（如 GPU 型号、训练时长）在摘要和提供的文本中**未充分披露**。

### 6. 论文真正可信的贡献
*   **实验闭环**：最强的证据不是交叉验证的数字，而是那 **15 个株系的湿实验（Wet-lab）验证**，证明了模型在真实生物环境下的有效性。
*   **全球泛化**：解决了以往模型只能预测特定地区（如韩国）病毒株的局限。
*   **可解释性**：定位到了与强致病性相关的关键序列基序，这为生物学家研究病毒致病机制提供了直接线索。

### 7. 局限与风险
*   **宿主多样性不足**：实验主要针对特定品种的番茄，不同番茄品种（具有不同抗性基因）对同一病毒株的反应可能不同，模型目前尚未深度整合宿主基因组信息。
*   **环境因子缺失**：病毒的致病力受温度、湿度等环境影响很大，纯序列预测在极端气候下的准确性有待观察。
*   **数据偏差**：标注数据来源于现有文献，可能存在不同实验室对“强/弱毒”定义标准不统一的系统性偏差。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事病原体监测、作物保护、蛋白质功能预测的 AI 研究者。
*   **后续可跟进的问题**：能否将此框架扩展到其他多组分病毒（如双生病毒科的其他成员）？能否通过逆向该模型，人工设计出不具致病性但能诱导植物免疫的“减毒疫苗”株系？

（完）
