---
title: "A computer-aided drug repurposing: the antibacterial agents targeting GroEL."
title_zh: 计算机辅助药物重利用：靶向 GroEL 的抗菌药物
authors: "Dongdong Zhang, Feng-Biao Guo, Haotian Li"
date: 2026-04-01
pdf: "https://pubmed.ncbi.nlm.nih.gov/41239775/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于抗生素发现和药物重定位的计算工作流
tldr: 针对抗生素研发成本高、周期长的问题，本研究开发了一套结合靶点筛选、药物预测、分子对接及动力学模拟的计算工作流，旨在从现有药物库中寻找针对细菌伴侣蛋白 GroEL 的抗菌药物。通过实验验证，成功发现达普司他和依折麦布具有显著的抗菌活性，且与外排泵抑制剂联用可增强药效，为老药新用提供了高效的计算筛选范式。
selection_source: fresh_fetch
motivation: 旨在通过计算机辅助的老药新用策略，降低新型抗菌药物研发的成本与风险，应对日益严重的细菌耐药性挑战。
method: 构建了集成 CEG 2.0 靶点筛选、DrugBank 药物库检索、分子对接及分子动力学模拟的计算工作流，并辅以体外抗菌实验验证。
result: 筛选并证实了达普司他和依折麦布对金黄色葡萄球菌和大肠杆菌具有抑制作用，且发现外排泵抑制剂能显著提升其抗菌效力。
conclusion: 验证了该计算工作流在非抗菌药物转用方面的可行性，为开发针对革兰氏阳性和阴性菌的新型治疗方案提供了新思路。
---

## 摘要
背景与目的：药物重利用（DR）通过将已批准药物应用于新适应症，提供了比传统药物研发更具吸引力的替代方案，具有更低的风险和成本。计算方法在早期药物重利用中发挥着至关重要的作用，开发稳健的计算工作流可以加速抗生素的发现。实验方法：我们建立了一种新型计算工作流，包含三个关键步骤：靶点筛选（基于 CEG 2.0 数据库）、药物筛选（利用 DrugBank 数据库、antiBac-Pred 数据库、分子对接和分子动力学 [MD] 模拟）以及体外抗菌实验。主要结果：我们的工作流识别出多种预测靶向细菌伴侣蛋白 GroEL 的市售药物。抗菌实验表明，达普司他（daprodustat）和依折麦布（ezetimibe）均对金黄色葡萄球菌（Staphylococcus aureus）和大肠杆菌（Escherichia coli）ΔtolC 表现出疗效。值得注意的是，外排泵抑制剂 PAβN 增强了达普司他针对金黄色葡萄球菌和大肠杆菌的抗菌效力，同时特异性地增强了依折麦布针对金黄色葡萄球菌的抗菌效力。MD 模拟证实了这两种药物与金黄色葡萄球菌或大肠杆菌 GroEL 的稳定结合，这与抗菌结果一致。结论与意义：本研究验证了我们将非抗菌药物重利用为抗菌药物的计算工作流，证明了具有成本效益的计算机辅助药物重利用是识别癌症、糖尿病和 COVID-19 等疾病新治疗方法的可行策略。此外，达普司他与外排泵抑制剂（如 PAβN）联用的协同效应，代表了一种对抗革兰氏阳性菌和革兰氏阴性菌病原体的极具前景的治疗方法。

## Abstract
BACKGROUND AND PURPOSE: Drug repurposing (DR) presents a compelling alternative to traditional drug discovery, offering lower risk and cost by applying approved drugs to new indications. Computational methods play a vital role in early-stage drug repurposing and the development of robust computational workflows can accelerate antibiotic discovery. EXPERIMENTAL APPROACH: We established a novel computational workflow comprising three key steps: target screening (based on CEG 2.0 database), drug screening (utilizing DrugBank database, antiBac-Pred database, molecular docking and molecular dynamics [MD] simulation) and in vitro antibacterial experiments. KEY RESULTS: Our workflow identified numerous commercially available drugs predicted to target the bacterial chaperone GroEL. Antibacterial assays revealed that both daprodustat and ezetimibe exhibited efficacy against Staphylococcus aureus and Escherichia coli ΔtolC. Notably, the efflux pump inhibitor PAβN enhanced the antibacterial efficacy of daprodustat against both S. aureus and E. coli, while potentiating the antibacterial potency of ezetimibe specifically against S. aureus. MD simulations confirmed stable binding of both drugs to S. aureus or E. coli GroEL, aligning with the antibacterial results. CONCLUSION AND IMPLICATIONS: This study validated our computational workflow for repurposing non-antibacterial drugs as antibacterial agents, demonstrating that cost-effective, computer-aided drug repurposing is a feasible strategy for identifying new therapeutic approaches to diseases, such as cancer, diabetes and COVID-19. Furthermore, the synergistic effect of daprodustat combined with an efflux pump inhibitor (e.g. PAβN) represents a promising therapeutic approach against both Gram-positive and Gram-negative bacterial pathogens.