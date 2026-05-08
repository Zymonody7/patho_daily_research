---
title: Artificial intelligence algorithm for real-time detection and counting of Trypanosoma cruzi parasites using smartphone microscopy.
title_zh: 基于智能手机显微镜的克氏锥虫寄生虫实时检测与计数的人工智能算法
authors: "Lin Lin, Ana Valeria Solano, Fabiola Gonzales, Mary Cruz Torrico, Daniel Illanes, Nuria Díez, David Bermejo-Peláez, Elena Dacal, Ramón Vallés-López, Lucia Pastor, Roberto Mancebo-Martín, María Jesús Ledesma-Carbayo, Miguel Luengo-Oroz, Jose M Rubio, Maria Flores-Chavez"
date: 2026-05-07
pdf: "https://pubmed.ncbi.nlm.nih.gov/42096492/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于显微镜图像中病原体实时检测的AI系统
tldr: "针对资源匮乏地区克氏锥虫病诊断依赖专业人员且效率低的问题，研究者开发了一套集成智能手机的实时AI检测系统。该系统通过3D打印适配器连接显微镜，利用部署在手机端的轻量化模型（如SSD-MobileNetV2）对血液和脑脊液样本进行实时识别与计数。实验显示该系统在人类样本上达到86.5%的F1分数，且在实地测试中表现出极高的召回率（96.4%），为热带病早期筛查提供了一种低成本、可扩展的自动化方案。"
selection_source: fresh_fetch
motivation: 旨在解决克氏锥虫病在急性期诊断过度依赖专业显微镜操作人员、导致资源受限地区诊断效率低下的瓶颈。
method: 开发了一种结合3D打印显微镜适配器与智能手机端轻量化目标检测模型（SSD-MobileNetV2和YOLOv8）的实时图像分析系统。
result: "SSD-MobileNetV2模型在人类样本检测中取得了86.5%的F1分数，并在实地模拟测试中实现了96.4%的高召回率，表现出极强的筛查敏感性。"
conclusion: 该系统证明了利用移动端AI进行低成本、高灵敏度寄生虫筛查的可行性，具有推广至其他忽视热带病（NTDs）诊断的巨大潜力。
---

## 摘要
恰加斯病（Chagas disease）影响全球 600-700 万人，每年导致约 12,000 人死亡。诊断方法因疾病阶段而异，慢性期常用血清学检测，而急性期则采用显微镜检查和 PCR、LAMP 等分子技术。虽然显微镜检查在资源受限地区仍是最易获得的工具，但其有效性取决于熟练的人员，从而形成了诊断瓶颈。为克服这些局限性，我们开发了一种便携式、集成智能手机的 AI 系统，用于显微镜图像中克氏锥虫（Trypanosoma cruzi）的实时检测。该平台结合了一个 3D 打印的显微镜适配器（用于将智能手机摄像头与显微镜目镜对齐以实现图像数字化）、支持远程医疗的标注工作流，以及部署在智能手机上用于实时分析的轻量级 AI 模型（SSD-MobileNetV2、YOLOv8）。SSD-MobileNetV2 模型在包含人类样本（20 个样本的 478 张图像，包括厚/薄血涂片和脑脊液）和鼠类薄血涂片（33 个样本的 570 张图像）的多样化数据集上进行了训练，在人类样本上实现了 86% 的精确率、87% 的召回率和 86.5% 的 F1 分数，展示了在多变成像条件下的鲁棒性能。我们还利用所提系统进行了一项真实世界试点实验。用户操作基于智能手机的系统扫描了三份薄血涂片，并实时生成预测。模型输出以专家标注作为地面真值进行了基准测试。在目标层面，该算法实现了 67.1% 的精确率、96.4% 的召回率和 79.1% 的 F1 分数，显示出在操作条件下具有较高的灵敏度，其配置可能适用于筛查。该系统能够在缺乏先进基础设施的野外环境中实现快速、准确的寄生虫检测，填补了早期诊断和监测的关键空白。其模块化设计允许适配其他病原体和细胞结构，为被忽视的热带病诊断提供了一种可扩展的解决方案。通过将 AI 创新与显微镜技术相结合，该方法有望促进流行地区公平的医疗服务交付，并符合全球卫生优先事项。

## Abstract
Chagas disease affects 6-7 million people worldwide and causes approximately 12,000 deaths annually. Diagnostic methods vary by disease stage, with serological tests commonly used in the chronic phase, while microscopy and molecular techniques like PCR and LAMP are employed in the acute phase. While microscopy remains the most accessible tool in resource constrained settings, its effectiveness depends on skilled personnel, creating diagnostic bottlenecks. To overcome these limitations, we developed a portable, smartphone-integrated AI system for real-time Trypanosoma cruzi detection in microscopy images. The platform combines a 3D-printed microscope adapter which aligns the smartphone camera with the microscope ocular to digitize images, with telemedicine-enabled annotation workflows, and lightweight AI models (SSD-MobileNetV2, YOLOv8) deployed on smartphone for real-time analysis. Trained on a diverse dataset of human samples (478 images from 20 samples), including thick/thin blood smears and cerebrospinal fluid) and murine thin smears (570 images from 33 samples), the SSD-MobileNetV2 model achieved 86% precision, 87% recall, and 86.5% F1-score on human samples, demonstrating robust performance across variable imaging conditions. We additionally piloted a real-world experiment with the proposed system. Three thin blood smears were scanned by a user operating the smartphone-based system, with predictions generated in real time. Model outputs were benchmarked against expert annotations as the ground truth. At the object level, the algorithm achieved a precision of 67.1%, a recall of 96.4%, and an F1-score of 79.1%, showing high sensitivity under operational conditions with a configuration possibly suitable for screening. This system could enable rapid, accurate parasite detection in field settings without advanced infrastructure, addressing critical gaps in early diagnosis and monitoring. Its modular design allows adaptation to other pathogens and cellular structures, offering a scalable solution for neglected tropical disease diagnostics. By bridging AI innovation with microscopy, this approach holds promise for advancing equitable healthcare delivery in endemic regions and aligning with global health priorities.

---

## 论文详细总结（自动生成）

这篇论文介绍了一种利用智能手机和人工智能技术，在资源匮乏地区实时检测**克氏锥虫**（引起恰加斯病的寄生虫）的系统。

### 1. 解决的问题与研究价值
*   **核心问题**：恰加斯病（Chagas disease）在拉丁美洲等地高发，急性期诊断依赖显微镜观察血液样本。但基层医疗机构缺乏经验丰富的检验师，人工找虫子既慢又容易漏诊。
*   **研究价值**：该研究将昂贵的实验室诊断流程“平替”为“手机+3D打印适配器+轻量化AI”，实现了在手机端无需联网的实时检测。这对于全球卫生公平性、尤其是偏远地区的疾病筛查具有极高的实用价值。

### 2. 白话版概述
想象一下，在偏远的乡村诊所，医生只有一个普通的旧显微镜。研究者设计了一个塑料支架（3D打印），把智能手机固定在显微镜目镜上。手机屏幕就像“扫码”一样，在显微镜视野里实时移动，一旦发现寄生虫，AI 就会立刻画框标出并计数。这就像给显微镜装了一个“自动导航”和“目标识别”系统，让普通村医也能达到专家的诊断水平。

### 3. 方法部分
*   **核心思想**：将计算机视觉中的目标检测技术（Object Detection）迁移到移动端，通过硬件适配实现图像数字化，通过轻量化模型实现本地推理。
*   **模型结构**：
    *   采用了 **SSD-MobileNetV2** 和 **YOLOv8**。
    *   **SSD-MobileNetV2** 是核心选择，因为它在计算量（FLOPs）和检测精度之间取得了平衡，适合在手机 CPU/GPU 上跑实时推理。
*   **关键设计取舍**：
    *   **放弃云端推理**：为了适应无网络环境，模型必须足够小，能直接跑在手机上。
    *   **数据多样性**：训练集不仅包含人类的厚/薄血涂片，还包含了脑脊液样本和鼠类样本，以增强模型在不同背景噪声下的鲁棒性。
    *   **硬件适配**：开发了专门的 3D 打印适配器，解决手机镜头与显微镜光轴对齐的问题，保证成像质量。

### 4. 实验部分
*   **数据集**：
    *   人类样本：478 张图像（来自 20 个样本），涵盖血涂片和脑脊液。
    *   鼠类样本：570 张图像（来自 33 个样本）。
*   **评价指标**：精确率（Precision）、召回率（Recall）、F1 分数。
*   **主要结果**：
    *   **实验室测试**：在人类样本上，SSD-MobileNetV2 达到了 **86.5% 的 F1 分数**。
    *   **实地模拟测试**：在真实操作环境下，**召回率高达 96.4%**。这意味着模型几乎不会漏掉任何一个阳性目标，虽然会有一些“假阳性”（误报），但作为筛查工具，高召回率是最关键的。

### 5. 资源与算力
*   **训练资源**：文中未充分披露具体的训练服务器配置（如 GPU 型号或训练时长）。
*   **推理资源**：明确指出模型部署在智能手机端，利用手机本地算力实现实时分析。

### 6. 真正可信的贡献
*   **端到端的闭环方案**：不仅是跑通了算法，还解决了从硬件连接（3D 打印）、远程标注工作流到移动端部署的全过程。
*   **高敏感度的实地表现**：96.4% 的召回率证明了该系统作为“初筛工具”的可靠性，能显著降低漏诊率。
*   **多样本适应性**：证明了 AI 可以同时处理血液和脑脊液等不同背景的显微图像。

### 7. 局限与风险
*   **样本量较小**：人类样本仅来自 20 个人，数据的多样性（如不同品牌显微镜、不同染色质量）可能仍不足以覆盖所有现实情况。
*   **精确率瓶颈**：实地测试中精确率为 67.1%，意味着存在约 1/3 的误报，仍需要人工进行二次确认，无法完全脱离人类专家。
*   **硬件依赖**：3D 打印适配器的精度和不同手机摄像头的对焦特性可能会影响最终效果。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：关注边缘计算（Edge AI）、全球卫生技术、以及低成本医疗影像诊断的研究者。
*   **后续可跟进的问题**：如何通过主动学习（Active Learning）利用实地产生的误报数据自动优化模型？以及如何将该框架快速迁移到疟疾、丝虫病等其他寄生虫病的检测中？

（完）
