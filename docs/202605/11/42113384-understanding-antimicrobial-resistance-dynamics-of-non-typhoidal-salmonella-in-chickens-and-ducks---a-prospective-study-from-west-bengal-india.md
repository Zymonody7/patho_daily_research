---
title: "Understanding antimicrobial resistance dynamics of non-typhoidal Salmonella in chickens and ducks - a prospective study from West Bengal, India."
title_zh: 了解印度西孟加拉邦鸡和鸭中非伤寒沙门氏菌的抗菌药物耐药性动态——一项前瞻性研究
authors: "Santanu Nath, Md Habib, Jaydeep Banerjee, Subhasis Batabyal, Prasad Thomas, Premanshu Dandapat, Pramod K Nanda, Arun K Das, Indranil Samanta, Arnab Sen, Samiran Bandyopadhyay"
date: 2026-05-11
pdf: "https://pubmed.ncbi.nlm.nih.gov/42113384/"
tags: ["query:pathoai"]
score: 9.0
evidence: 机器学习用于基因组抗生素耐药性预测
tldr: 针对印度西孟加拉邦家禽中非伤寒沙门氏菌的耐药性（AMR）威胁，本研究分析了446株分离株的耐药谱，发现肉类和零售环节的耐药风险显著更高。通过应用XGBoost等机器学习算法，研究成功预测了超广谱β-内酰胺酶（ESBL）的产生，并识别出采样部位和来源是关键预测因子。该研究揭示了家禽链条中耐药菌的传播风险，证明了机器学习在提升AMR监测和指导精准干预方面的潜力。
selection_source: fresh_fetch
motivation: 旨在探究印度西孟加拉邦家禽生产链中非伤寒沙门氏菌的耐药性分布特征及其对公共卫生的潜在威胁。
method: 结合传统逻辑回归分析与XGBoost、随机森林等机器学习算法，对分离自鸡鸭的沙门氏菌进行耐药表型分析及ESBL产生预测。
result: 发现鼠伤寒沙门氏菌为主要血清型，且零售环节的肉类和盲肠样本表现出极高的耐药性，其中XGBoost在预测ESBL产生方面表现最优。
conclusion: 研究强调了家禽源沙门氏菌对关键抗菌药物的耐药性正削弱临床治疗效果，并证明了集成机器学习与常规分析可有效增强耐药性监测预警。
---

## 摘要
本研究调查了采集自印度西孟加拉邦的禽源（n = 1020）肠道沙门氏菌（Salmonella enterica，n = 446）的抗菌药物耐药性（AMR）概况。鼠伤寒沙门氏菌（Salmonella Typhimurium，n = 328）是最常分离出的血清型，并发现其对四环素（72%）、氨苄西林（57%）和萘啶酸（53%）具有耐药性。逻辑回归显示，与泄殖腔拭子相比，来自肉类、肝脏和盲肠的分离株产生耐药性的几率显著更高。与其他宿主和养殖场相比，来自肉鸡和零售环节的分离株也更有可能产生耐药性。为了预测产超广谱 β-内酰胺酶（ESBL）的菌株，应用了三种机器学习算法：XGBoost、随机森林（Random Forest）和 LightGBM。XGBoost 在 ESBL 预测中表现出最高的灵敏度和整体判别力，而随机森林则提供了平衡的性能。采样部位和样本来源成为关键预测因子，其中零售市场的盲肠和肉类样本分离株与产生 ESBL 具有强相关性。基因型分析确定 blaCTX-M-1（n = 122）为主要的 ESBL 基因，此外还发现了 tetA（92%）和喹诺酮类耐药决定簇。这些研究结果强调了禽源沙门氏菌 AMR 带来的公共卫生威胁，特别是耐药菌株传播的风险。观察到的对极其重要抗菌药物的耐药性，加剧了人们对一线治疗药物疗效下降的担忧。本研究还强调了将机器学习与传统分析相结合在加强 AMR 监测和指导家禽生产系统针对性干预措施方面的效用。

## Abstract
This study investigated the antimicrobial resistance (AMR) profile of Salmonella enterica (n = 446) of poultry origin (n = 1020) collected from West Bengal, India. Salmonella Typhimurium (n = 328) were the most frequently isolated serovar and found resistant to tetracycline (72%), ampicillin (57%), and nalidixic acid (53%). Logistic regression revealed significantly higher odds of resistance in isolates from meat, liver, and cecum compared to cloacal swabs. Resistance was also more likely in isolates from broilers and from retail sources compared to other hosts and farms. To predict extended-spectrum beta-lactamase (ESBL) producers, three machine learning algorithms-XGBoost, Random Forest, and LightGBM-were applied. XGBoost demonstrated the highest sensitivity and overall discriminatory power for ESBL prediction, while Random Forest offered balanced performance. Sampling site and sample source emerged as key predictors, with isolates from cecal and meat samples in retail markets having strong association with ESBL production. Genotypic analysis identified blaCTX-M-1 (n = 122) as the predominant ESBL gene, along with tetA (92%) and quinolone resistance determinants. These findings underscore public health threats posed by AMR in poultry-associated Salmonella, particularly the risk of transmission of resistant strains. The observed resistance to critically important antimicrobials reinforces concerns regarding the diminishing efficacy of frontline therapeutic agents. This study also highlights the utility of integrating machine learning with conventional analytics to enhance AMR surveillance and guide targeted interventions in poultry production systems.