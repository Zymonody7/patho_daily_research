---
title: In silico design of a multiepitope vaccine against antibiotic drug-resistant Acinetobacter baumannii.
title_zh: 针对抗生素耐药性鲍曼不动杆菌的多表位疫苗计算机模拟设计
authors: "Sudeep Khadka, Muhammad Ajmal Khan, Shahid Iqbal, Amin Ullah, Ajaz Ahmad, Noor Zada Khan, Aishma Khattak"
date: 2026-04-03
pdf: "https://pubmed.ncbi.nlm.nih.gov/41932930/"
tags: ["query:pathoai"]
score: 8.0
evidence: 针对耐药鲍曼不动杆菌的多表位疫苗计算机辅助设计
tldr: 针对耐药性极强的鲍曼不动杆菌（A. baumannii），本研究利用生物信息学方法设计了一种多表位疫苗（MEV）。通过分析美罗培南耐药株的转录组数据，筛选出12个高保守且具免疫原性的蛋白质，并预测出12个CTL和7个HTL表位。分子动力学模拟和免疫仿真证明该疫苗结构稳定且能激发强烈的免疫反应，为应对多重耐药菌感染提供了新的候选方案。
selection_source: fresh_fetch
motivation: 鲍曼不动杆菌具有极强的多重耐药性且临床预后差，被世界卫生组织列为急需开发疫苗的首要病原体。
method: 通过分析耐药菌株的RNA-seq数据筛选上调基因，利用多种生物信息学工具预测高亲和力的T细胞表位，并结合分子对接与动力学模拟验证疫苗的稳定性和免疫原性。
result: 成功构建了一个由335个氨基酸组成的多表位疫苗，模拟显示其能有效激活先天性和适应性免疫系统，且与MHC分子结合稳定。
conclusion: 该研究通过计算设计为开发针对耐药鲍曼不动杆菌的疫苗奠定了理论基础，并为后续的体外和体内实验验证提供了关键候选序列。
---

## 摘要
鲍曼不动杆菌（Acinetobacter baumannii）作为 ESKAPE 病原体成员之一，每年导致约 722,000 例感染，并因其对多种抗生素迅速产生耐药性而臭名昭著，导致临床预后较差。由于耐药菌株的迅速出现和有效治疗手段的匮乏，世界卫生组织已将鲍曼不动杆菌列为疫苗研发的最高优先级病原体，凸显了对新型治疗策略的迫切需求。在本研究中，我们通过分析美罗培南耐药分离株的 RNA-seq 数据，采用计算机模拟（in silico）方法设计了一种针对多重耐药菌株的多表位疫苗（MEV）。利用 ToxinPred、VaxiJen v2.0 和 AllerTOP v2.0 工具预测了该疫苗的无毒性、潜在抗原性及非致敏性。分别使用 NetMHCpan 和 NetMHCIIpan 进行 CTL 和 HTL 表位预测。PEP-FOLD3.5 服务器预测了 T 细胞表位的三维结构。使用 HADDOCK 2.4 网络服务器将建模的表位与 MHC 结合槽进行分子对接，以评估其强结合相互作用。使用 GROMACS 2021.4 版本进行分子动力学（MD）模拟以评估 MEV 的稳定性，并进行主成分分析（PCA）以识别模拟过程中的主要构象状态。使用 C-ImmSim 服务器进行免疫反应模拟。通过对美罗培南耐药鲍曼不动杆菌菌株的 RNA-seq 分析，我们鉴定了 1,240 个与耐药机制相关的显著上调基因。从 156 个非同源蛋白中，筛选出 12 个高度保守、非致敏的抗原蛋白，并预测出 12 个 CTL 和 7 个 HTL 表位，这些表位具有较强的 HLA 结合亲和力和免疫原性潜力。分子对接和动力学模拟证实了表位与 MHC 之间稳定的相互作用以及由 335 个氨基酸组成的 MEV 构建体的结构稳定性，同时免疫模拟显示其能有效激活先天性和适应性免疫反应。这项计算机模拟研究为针对鲍曼不动杆菌的疫苗开发奠定了良好的基础，并为未来的体外和体内验证迈出了关键一步。

## Abstract
Acinetobacter baumannii, a member of the ESKAPE pathogens, causes approximately 722,000 infections annually and is notorious for rapidly developing resistance to multiple antibiotics, resulting in poor clinical outcomes. Due to the rapid emergence of drug-resistant strains and limited effective treatments, the World Health Organization has listed A. baumannii as a top-priority pathogen for vaccine development, highlighting the urgent need for novel therapeutic strategies. In this study, we employed an in silico approach to design a multiepitope vaccine (MEV) targeting multidrug-resistant strains by analyzing RNA-seq data from meropenem-resistant isolates. The vaccine non-toxicity, probably antigenic, and non-allergenic nature was predicated via ToxinPred, VaxiJen v2.0, and AllerTOP v2.0 tools. CTL and HTL epitope prediction was carried out using NetMHCpan and NetMHCIIpan respectively. PEP-FOLD3.5 server predicted T-cell epitopes 3D structure. Molecular docking of the modeled epitopes into the MHC binding grooves was performed using the HADDOCK 2.4 web server for strong binding interactions. MD simulations were carried out using GROMACS version 2021.4 for the MEV stability and PCA was performed to identify dominant conformational states during the simulation. C-ImmSim server was used for the simulation of immune response. RNA-seq analysis from meropenem resistant A. baumannii strains, we identified 1,240 significantly upregulated genes linked to resistance mechanisms. From 156 non-homologous proteins, 12 highly conserved, non-allergenic antigenic proteins were selected to predict 12 CTL and 7 HTL epitopes with strong HLA-binding affinity and immunogenic potential. Molecular docking and dynamics simulations confirmed stable epitope-MHC interactions and structural stability of the 335-amino-acid MEV construct, while immune simulations indicated robust activation of innate and adaptive responses. This in silico study lays a promising foundation for vaccine development against A. baumannii and provides a critical step toward future in vitro and in vivo validation.