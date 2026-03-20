---
title: In silico discovery of thioglycoside analogues as donor-site inhibitors of glycosyltransferase LgtC.
title_zh: 糖基转移酶 LgtC 供体位点抑制剂硫代糖苷类似物的计算机模拟发现
authors: "Olimpo Sierra-Hernández, Oscar Saurith-Coronell, Jackson J Alcázar, Eliceo Cortés, Maryury C Flores-Sumoza, Juan D Rodríguez-Macías, José R Mora, Yovani Marrero-Ponce, Ernesto Contreras-Torres, Edgar A Márquez Brazón"
date: 2026-03-17
pdf: "https://pubmed.ncbi.nlm.nih.gov/41844697/"
tags: ["query:pathoai"]
score: 9.0
evidence: 病原体毒力途径抑制剂的计算机发现
tldr: 针对多重耐药菌的毒力因子LgtC酶，本研究利用相似性筛选、分子对接及动力学模拟识别硫代糖苷类抑制剂。结果发现C-5和C-18等分子能比天然底物更稳定地结合在供体位点。该研究为开发干扰细菌脂寡糖合成的新型抗毒力药物提供了高潜力的先导化合物。
selection_source: fresh_fetch
motivation: 针对多重耐药菌免疫逃逸的关键酶LgtC，寻找能阻断其脂寡糖生物合成路径的小分子抑制剂以开发新型抗毒力疗法。
method: 整合了相似性筛选、药代动力学过滤、分子对接及100纳秒分子动力学模拟的计算流水线，对硫代糖苷类类似物进行评估。
result: 识别出C-5和C-18等候选分子，其结合能优于天然底物且在动力学模拟中表现出极高的结合稳定性与氢键网络。
conclusion: 筛选出的硫代糖苷骨架为后续生化测试提供了明确的先导化合物，为优化针对革兰氏阴性菌的抗毒力药物奠定了结构基础。
---

## 摘要
多重耐药革兰氏阴性病原体的日益流行，凸显了通过靶向关键毒力途径来补充传统抗生素治疗策略的紧迫需求。糖基转移酶 LgtC 是脂寡糖 (LOS) 生物合成中的关键酶，因其在细菌免疫逃逸和致病性中的核心作用，成为抗毒力策略的一个极具吸引力的靶点。在这项工作中，我们采用了一套集成的计算机模拟流程，以鉴定与代谢诱饵 FucSBn 和 BacSBn 结构相关的硫代糖苷类似物，并评估了它们结合 LgtC 的 UDP-半乳糖供体口袋的潜力。通过在 PubChem 中进行基于相似性的筛选，随后进行 ADME-Tox 过滤，共获得了 18 个候选类似物。使用 AutoDock-GPU 进行的分子对接显示，有几个候选物（尤其是 C-5 [-8.36 kcal/mol] 和 C-18 [-8.13 kcal/mol]）在供体位点内表现出良好的结合力，其平均评分值比天然供体 UDP-α-D-半乳糖 (-6.74 kcal/mol) 更负。天然配体的重对接重现了晶体学构象，证实了对接方案的可靠性。为了评估动态行为，对每个复合物进行了 100 ns 的分子动力学模拟 (AMBER14)。评分最高的类似物保持了稳定的结合构象，RMSD 值约为 2.0-3.0 Å，并保留了类似于供体的氢键网络，同时辅以 π-堆积和硫介导的接触。这些相互作用模式表明，硫代糖苷类似物可能以一种与竞争性结合相容的方式占据供体位点。虽然对接和分子动力学描述了配体识别的不同方面，但在对接中观察到的几种趋势（如 C-5 和 C-18 良好的结合评分）与其在分子动力学过程中保持稳定构象的能力大致一致。基于这种一致性和评分，硫代糖苷支架 C-5、C-14 和 C-18 脱颖而出，成为针对 LgtC 进行后续生化测试的计算优先候选物。此外，这些支架为未来旨在破坏多重耐药革兰氏阴性菌中 LOS 生物合成的硫代糖苷类似物的基于结构的优化提供了机制基础和推定的起点。

## Abstract
The growing prevalence of multidrug-resistant Gram-negative pathogens highlights the urgent need for therapeutic strategies that complement traditional antibiotics by targeting essential virulence pathways. Glycosyltransferase LgtC, a key enzyme in lipooligosaccharide (LOS) biosynthesis, represents an attractive target for antivirulence approaches because of its essential role in bacterial immune evasion and pathogenicity. In this work, we employed an integrated in silico pipeline to identify thioglycoside analogs structurally related to the metabolic decoys FucSBn and BacSBn, evaluating their potential to hit the UDP-galactose donor pocket of LgtC. A similarity-based screening in PubChem, followed by ADME-Tox filtering yield 18 candidate analogs. Molecular docking using AutoDock-GPU revealed several candidates, most notably C-5 (- 8.36 kcal/mol) and C-18 (- 8.13 kcal/mol), to bind favorably within the donor site, showing more negative mean scoring values than natural donor UDP-α-D-galactose (- 6.74 kcal/mol). Redocking of the natural ligand reproduced the crystallographic pose, supporting the reliability of the docking protocol. To assess dynamic behavior, 100 ns molecular dynamics simulations (AMBER14) were performed for each complex. The top-scoring analogs maintained stable binding poses, with RMSD values of ~ 2.0-3.0 Å and preserved donor-like hydrogen-bond networks complemented by π-stacking and sulfur-mediated contacts. These interaction patterns suggest that the thioglycoside analogs may occupy the donor site in a manner compatible with competitive binding. While docking and MD describe different aspects of ligand recognition, several trends observed in docking, such as the favorable binding scores of C-5 and C-18, are broadly consistent with their ability to maintain stable poses during MD. Based on this consistency and scoring, the thioglycoside scaffolds C-5, C-14, and C-18 emerge as computationally prioritized candidates for subsequent biochemical testing against LgtC. Furthermore, these scaffolds offer a mechanistic basis and putative starting points for future structure-based optimization of thioglycoside analogs aimed at disrupting LOS biosynthesis in multidrug-resistant Gram-negative bacteria.