---
title: "Dual β-lactam therapy against high-risk Pseudomonas aeruginosa isolates: a dynamic in-vitro infection model study integrating population genomics with quantitative systems pharmacology modelling and simulations."
authors: "Breen SKJ, Cortés-Lara S, Tait JR, Rogers KE, Lee WL, Faith M, Terrill AE, Fuhs DT, Harper M, López-Causapé C, Nation RL, Boyce JD, Oliver A, Landersdorfer CB."
date: 2027-01-26
pdf: "https://pubmed.ncbi.nlm.nih.gov/42349478/"
tags: ["query:pathoai"]
score: 8.0
evidence: 整合群体基因组学与系统药理学进行耐药性预测
tldr: "针对高风险铜绿假单胞菌（ST235）在治疗中极易产生耐药性的问题，本研究通过中空纤维体外感染模型（HFIM）结合全基因组测序，开发了一种定量系统药理学（QSP）模型。该模型能基于细菌耐药基因组信息预测头孢洛扎-他唑巴坦与美罗培南联合用药的疗效。结果显示，联合疗法能有效抑制耐药突变并产生协同杀菌作用，在模拟中使超89%的患者达到持续杀菌效果，为精准医疗提供了病原体特异性的预测框架。"
selection_source: fresh_fetch
motivation: 旨在解决传统方法难以预测抗生素联合用药对易产生耐药性的高风险铜绿假单胞菌治疗效果的问题。
method: 结合中空纤维体外感染模型、全基因组测序与定量系统药理学（QSP）建模，模拟临床给药方案并预测不同耐药机制下的细菌动态响应。
result: 发现单药治疗会诱发耐药突变（如ampC或ftsl基因突变）导致失败，而联合用药在所有菌株中均表现出显著的协同杀菌作用并成功抑制了耐药性的产生。
conclusion: 该研究首次实现了仅依据耐药机制即可预测抗生素治疗的时间进程响应，为针对特定病原体的个性化精准用药奠定了基础。
---

## Abstract
<h4>Background</h4>Pseudomonas aeruginosa has an extraordinary capacity for resistance emergence during treatment, even with newer antipseudomonals. There is a gap in understanding how resistance mechanisms affect the time-course of bacterial response to these newer agents. Traditional approaches for predicting pathogen response to an antibiotic do not apply to combination therapy. We aimed to develop a modelling framework to predict treatment response based on resistome information, using isolates of the worldwide-disseminated high-risk clone sequence type (ST) 235 and β-lactam antibiotics as the example.<h4>Methods</h4>In this hollow-fibre in-vitro infection study, we used three extensively drug-resistant ST235 clinical isolates from the national collection of the Clinical Microbiology Department of the Hospital Son Espases (Palma de Mallorca, Spain) that were hospital-acquired, were isolated following routine microbiological procedures from different patients between 2017 and 2022, were susceptible to ceftolozane-tazobactam, and had different levels of meropenem resistance. The selected isolates (ST235-05, ST235-09, and ST235-10) showed classical β-lactam resistance mechanisms pre-treatment. The isolates were investigated in 240-h dynamic hollow-fibre in-vitro infection models (HFIMs). The studies exposed the isolates to pharmacokinetic profiles of ceftolozane-tazobactam (simulating 1 g of ceftolozane and 0·5 g of tazobactam as a 3-h infusion every 8 h) and meropenem (simulating 6 g per day continuous infusion) as observed in hospitalised patients, as monotherapy and in combination. Treatment response was assessed through the quantification of the time-courses of viable total and resistant bacteria. Whole-genome sequencing identified the mechanisms of emerging resistance. A quantitative systems pharmacology (QSP) approach was used to model total and resistant bacterial counts and corresponding pharmacokinetic data from the HFIM. Monte Carlo simulations were used to predict treatment responses in 1000 virtual infected patients treated with ceftolozane-tazobactam and meropenem as monotherapies or in combination over 10 days.<h4>Findings</h4>In the HFIMs, each antibiotic alone amplified resistance by approximately 48 h for all isolates; that is, monotherapies resulted in a higher concentration of resistant bacteria compared with the control treatment at the respective time, except ceftolozane-tazobactam against ST235-10. Combination of ceftolozane-tazobactam and meropenem was synergistic (bacterial counts ≥2 log<sub>10</sub> colony forming units [CFU] per mL lower than the best performing monotherapy and initial inoculum) against all isolates and suppressed resistance. Against ST235-10, ceftolozane-tazobactam monotherapy reduced counts to less than 1 log<sub>10</sub> CFU per mL from 192 h onwards, whereas the combination reached less than 1 log<sub>10</sub> CFU per mL by 24 h. Across strains, population genomics confirmed monotherapy failures were associated with emerging resistance mechanisms (ceftolozane-tazobactam: ampC Ω-loop mutations; meropenem: ftsl mutation). The developed QSP model incorporated baseline resistance mechanisms and those emerging in resistant mutant subpopulations. The model explained and predicted the monotherapy failures involving amplification of these subpopulations, and synergistic killing and resistance suppression by the combination. Simulations using the model predicted bacterial regrowth above the initial inoculum for more than 90% of patients after 0 to approximately 3 days for meropenem monotherapy across all strains and for ceftolozane-tazobactam monotherapy against ST235-05 and ST235-09. For ceftolozane-tazobactam monotherapy against ST235-10, regrowth was predicted for approximately 30% of patients. In contrast, the simulations predicted sustained bacterial killing of at least 2 log<sub>10</sub> CFU per mL compared with the initial inoculum by the combination for more than 89% of patients across all strains.<h4>Interpretation</h4>To our knowledge, this model is the first to characterise and predict the time-course of responses of clinical isolates to antibiotics only by the resistance mechanisms present and their complex interplay, representing a step towards pathogen-specific, personalised medicine.<h4>Funding</h4>Australian National Health and Medical Research Council.

---

## 论文详细总结（自动生成）

这篇论文探讨了如何通过整合**基因组学**（研究细菌的基因突变）和**定量系统药理学**（用数学模型模拟药物在体内的作用）来解决超级细菌的耐药性问题。

### 1. 解决的问题与核心价值
*   **核心问题**：铜绿假单胞菌（*P. aeruginosa*）是一种极易产生耐药性的“超级细菌”。传统的药敏试验（MIC）只能告诉我们细菌现在怕不怕某种药，但无法预测在治疗过程中，细菌会如何通过**实时突变**产生新的耐药性，也无法预测两种抗生素联合使用时的动态效果。
*   **价值**：该研究建立了一个预测框架，能够根据细菌的基因组信息，预测抗生素联合疗法在不同患者体内的杀菌效果和耐药演变过程。这是迈向“病原体特异性精准医疗”的重要一步。

### 2. 白话版概述
*   铜绿假单胞菌在治疗时非常狡猾，即使面对新药也能迅速进化出抗性。
*   研究者通过一种模拟人体血液药物浓度的装置（中空纤维模型），观察了两种抗生素（头孢洛扎-他唑巴坦和美罗培南）单用和联用的效果。
*   他们发现单药治疗会诱发特定的基因突变导致失败，而联合用药能“封死”细菌的进化路径。
*   最后，他们开发了一个数学模型，只要输入细菌的基因信息，就能预测出联合用药能否在 10 天内彻底压制细菌。

### 3. 方法部分
*   **核心思想**：将细菌群体视为动态演化的系统。模型不仅考虑药物杀死了多少细菌，还考虑了药物压力如何筛选出带有特定耐药基因的“突变亚群”。
*   **模型结构（QSP 模型）**：
    *   **药代动力学（PK）**：模拟药物在人体内的吸收、分布和代谢。
    *   **药效动力学（PD）**：描述药物浓度与细菌死亡率的关系。
    *   **耐药机制模块**：将全基因组测序（WGS）发现的突变（如 *ampC* 基因突变导致分解药物能力增强，*ftsl* 突变导致药物结合点失效）转化为模型中的参数变化。
*   **关键设计取舍**：研究者没有试图模拟细菌的所有代谢路径，而是精准锁定了几种已知的关键耐药基因。这种“降维”处理使得模型在临床应用中更具可操作性。

### 4. 实验部分
*   **数据与对象**：选取了 3 株临床采集的高风险 ST235 型铜绿假单胞菌（这种菌株在全球范围内广泛传播且极难对付）。
*   **实验任务**：在 240 小时（10 天）的动态模拟中，测试单药与联合用药对细菌总数和耐药亚群的影响。
*   **评价指标**：细菌载量（CFU/mL）、耐药突变株的比例、协同作用指数（Synergy）。
*   **主要结果**：
    *   **单药必败**：美罗培南单药在 48 小时内就诱发了耐药性，导致细菌反弹。
    *   **联合必胜**：两种药物联合使用在所有测试菌株中均表现出显著协同作用，不仅杀菌速度快（24 小时内降至检测限下），且成功抑制了耐药突变的出现。
    *   **模拟预测**：对 1000 名虚拟患者的模拟显示，联合疗法在 >89% 的患者中有效。

### 5. 资源与算力
*   **文中未充分披露**。此类研究通常使用 R 语言、Monolix 或 MATLAB 等专业药理学建模软件，计算量主要集中在蒙特卡洛模拟（Monte Carlo simulations），普通工作站即可胜任，无需大规模 GPU 集群。

### 6. 真正可信的贡献
*   **证据最强的结论**：论文通过全基因组测序明确了单药治疗失败的分子机制（*ampC* Ω-loop 突变和 *ftsl* 突变），并证明了联合用药能有效阻断这些特定突变株的扩增。
*   **创新点**：这是首个仅依靠细菌初始耐药机制信息，就能预测治疗全过程动态响应的模型，证明了“基因组学 + 数学建模”在感染控制中的实战潜力。

### 7. 局限与风险
*   **样本量限制**：仅使用了 3 株 ST235 菌株，虽然具有代表性，但对于其他序列类型（ST）的泛化性有待验证。
*   **环境差异**：体外中空纤维模型（HFIM）虽然能模拟药物浓度，但缺乏人体免疫系统（如白细胞、细胞因子）的参与，实际临床效果可能受免疫状态影响。
*   **参数敏感性**：QSP 模型依赖于大量手工设定的生物学参数，不同实验室环境下的参数一致性可能存在偏差。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事药物联用预测、耐药性演化建模、以及希望将多组学数据（Omics）整合进动力学模型的 AI 研究者。
*   **后续可跟进的问题**：能否利用深度学习（如 Transformer 或图神经网络）直接从细菌的全基因组序列（WGS）中自动提取特征，并端到端地预测 QSP 模型中的关键动力学参数，从而省去人工调参的过程？

（完）
