---
title: Forecasting influenza activity based on internet retrieval behavior and meteorological data in four megacities of China.
title_zh: 基于互联网检索行为和气象数据的中国四个超大城市流感活动预测
authors: "Shan CX, Wang YH, Xu Q, Wang GL, Lv CL, Fang LQ., Chun-Xi Shan, Yan-He Wang, Qiang Xu, Guo-Lin Wang, Chen-Long Lv, Li-Qun Fang"
date: 2026-04-02
pdf: "https://pubmed.ncbi.nlm.nih.gov/41928100/"
tags: ["query:pathoai"]
score: 8.0
evidence: 用于流感预测和预警的深度学习模型
tldr: 针对季节性流感预警滞后的挑战，本研究整合百度指数搜索行为与气象多源数据，利用长短期记忆网络（LSTM）构建了针对北京、上海等四大城市的流感预测模型。结果显示，该模型在预测流感病毒阳性检出率方面优于传统机器学习算法，可提前1-3周发出预警，为城市公共卫生监测提供了高效的数字化工具。
selection_source: fresh_fetch
motivation: 传统流感监测存在滞后性，需要结合互联网搜索行为和气象数据来提升季节性流感预警的及时性和准确性。
method: 收集四大城市的流感监测数据、百度搜索指数及气象指标，对比评估了LSTM深度学习模型与三种传统机器学习算法的预测效能。
result: LSTM模型在各城市的预测准确率（R²最高达0.94）均优于对比模型，能提前1-3周预测流感趋势，且“达菲”等关键词搜索量被证实是核心预测指标。
conclusion: 深度学习结合多源互联网大数据能有效实现流感疫情的早期预警，为城市公共卫生决策提供可靠的技术支撑。
---

## 摘要
背景：季节性流感流行的准确且及时的预警仍然是一项关键的公共卫生挑战。利用网络数据源（如互联网搜索查询）的创新方法在及时性方面是传统实验室监测的有益补充。方法：利用2013年至2018年间北京、天津、上海和深圳四个超大城市流感样病例（ILI）中的流感病毒病原学监测数据，我们开发了基于每周百度指数数据和气象指标的预测模型。将长短期记忆（LSTM）模型与三种机器学习算法进行了比较。最优模型被用于流感活动的每周预测。结果：与三种机器学习模型（最高 R2：0.73‒0.82）相比，LSTM 模型表现出更优越的性能（各城市最高 R2：0.80‒0.94），并能有效预测四个城市提前 1-3 周的流感病毒每周阳性检出率。在所有四个城市的中期滚动预测（14-35 周）中，其准确性得到了稳健保持。尽管预测因子的显著性随地理位置而异，但“达菲”（Tamiflu）的百度指数在三个城市中始终是主要的预测因子。结论：本研究验证了整合网络大数据和深度学习算法进行流感监测的巨大潜力。所开发的 LSTM 模型为季节性流感流行的早期发现和预警提供了一个精简且有效的工具。

## Abstract
BACKGROUND: Accurate and timely early warning of seasonal influenza epidemics continues to pose a critical public health challenge. Innovative methodologies leveraging network data sources, such as internet search queries, serve as a valuable complement to traditional laboratory surveillance in terms of timeliness. This study aimed to develop and validate a deep-learning model for influenza prediction based on multi-source data. METHODS: Using etiological surveillance data of influenza viruses among influenza-like illness (ILI) cases in four megacities (Beijing, Tianjin, Shanghai, and Shenzhen) during 2013 and 2018, we developed prediction models based on weekly Baidu index data and meteorological indicators. A long short-term memory (LSTM) model was compared against three machine learning algorithms. The optimal model was used for weekly forecasting of influenza activity. RESULTS: The LSTM model exhibited superior performance (maximum R2 : 0.80‒0.94 across cities) when compared to the three machine-learning models (maximum R2: 0.73‒0.82), and effectively predicted the weekly positive detection rate of influenza viruses with a lead time of 1‒3 weeks for the four megacities. Its accuracy was robustly maintained in medium-term rolling forecasts (14‒35 weeks) across all four megacities. Although the significance of predictors varied geographically, the Baidu index for "Tamiflu" was consistently a dominant predictor in three megacities. CONCLUSIONS: This study validates the significant potential of integrating network big data and deep-learning algorithm for influenza surveillance. The developed LSTM model provides a streamlined and effective tool for the early detection and warning of seasonal influenza epidemics.

---

## 论文详细总结（自动生成）

这篇论文探讨了如何利用互联网搜索大数据和气象数据，通过深度学习模型提升流感疫情预警的及时性。以下是详细的结构化总结：

### 1. 解决的问题与研究意义
*   **核心问题**：传统的流感监测主要依赖医院实验室的采样检测（病原学监测），这种方式虽然准确，但存在 **1-2 周的滞后性**。当疾控部门拿到数据时，疫情可能已经扩散。
*   **研究意义**：流感具有季节性且传播快。如果能利用“人们生病后先上网搜索”的行为数据（百度指数）和影响病毒传播的气象数据，提前预测流感趋势，就能为公共卫生部门争取宝贵的防控窗口期。

### 2. 白话版概述
当流感来袭时，人们在去医院之前通常会先在网上搜索症状或药物（如“发烧”、“达菲”）。同时，气温和湿度的变化也会影响病毒的活跃度。这篇论文收集了北京、上海等四个大城市过去几年的搜索记录和天气数据，喂给一个擅长处理时间序列的深度学习模型（LSTM）。结果发现，这个模型能比传统方法更准地预判未来 1-3 周的流感爆发情况，准确率非常高。

### 3. 方法部分
*   **核心思想**：将流感预测看作一个**多变量时间序列预测问题**。通过整合“人的行为”（搜索）和“自然环境”（气象）两类特征，捕捉它们与流感阳性率之间的非线性关系。
*   **模型结构**：采用了 **LSTM（长短期记忆网络）**。
    *   **选择理由**：流感数据具有明显的季节性和长期依赖性，LSTM 相比普通神经网络，能更好地记住“去年这个时候发生了什么”以及“过去几周的趋势”。
*   **关键设计**：
    *   **特征筛选**：从大量百度搜索词中筛选出与流感高度相关的词（如“达菲”、“流感症状”）。
    *   **多源融合**：将每周的搜索指数、平均气温、相对湿度等数据进行归一化处理，作为模型的输入向量。
    *   **滚动预测**：模型不仅预测下一周，还进行了 14-35 周的中期滚动预测，验证其稳定性。

### 4. 实验部分
*   **数据来源**：2013-2018 年北京、天津、上海、深圳四个城市的流感样病例（ILI）监测数据、百度指数和气象指标。
*   **任务**：预测每周的“流感病毒阳性检出率”（即送检样本中真正患流感的比例）。
*   **Baseline（对比模型）**：三种传统机器学习算法（文中未逐一列举名称，通常为随机森林、XGBoost 或支持向量机等）。
*   **评价指标**：$R^2$（决定系数，越接近 1 越准）。
*   **主要结果**：
    *   **准确性**：LSTM 模型在四个城市的 $R^2$ 达到 0.80-0.94，显著优于传统机器学习模型的 0.73-0.82。
    *   **提前量**：模型能有效提前 **1-3 周** 预警流感活动。
    *   **关键特征**：**“达菲”（Tamiflu）**的搜索量在多个城市中都是最核心的预测指标。

### 5. 资源与算力
*   **文中未充分披露**。考虑到 LSTM 处理此类规模的周级时间序列数据计算量并不大，通常单张消费级显卡或主流 CPU 即可完成训练。

### 6. 真正可信的贡献
*   **多城市验证**：研究不仅在一个城市有效，在南北方四个超大城市均表现稳健，证明了模型具有较好的普适性。
*   **特征有效性**：明确了互联网搜索行为（尤其是特定药物名称）在数字流行病学中的高预测价值。
*   **工程实用性**：验证了 LSTM 在处理公共卫生监测数据时，捕捉非线性波动能力强于传统统计学或简单机器学习模型。

### 7. 局限与风险
*   **搜索行为偏差**：媒体的大规模报道可能导致搜索量激增（即“恐慌性搜索”），但这并不代表实际感染人数增加，这会干扰模型判断。
*   **数据获取门槛**：百度指数等商业数据接口的开放程度和长期可用性可能受限。
*   **地理局限**：超大城市的人群行为模式与农村或小城市可能完全不同，模型在非城市地区的迁移效果未知。
*   **病毒变异**：如果出现新型流感病毒（如 2009 年 H1N1），历史搜索模式可能失效。

### 8. 对 AI for Bioinformatics 的启发
*   **适合关注的人群**：从事数字流行病学、公共卫生预警、时空数据挖掘的 AI 研究者。
*   **后续可跟进的问题**：能否引入 Transformer 或时空图神经网络（STGNN）来捕捉城市间的疫情扩散关联？如何利用大语言模型（LLM）更精准地分析搜索意图，排除无关搜索的噪音？

（完）
