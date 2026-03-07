# 订阅与查询配置

这个项目现在默认按 `AI 优先` 方向预置了四组 `intent_profiles`，你可以直接在 `config.yaml` 里改：

- `PathoAI`：病原组学里的基础模型、病原检测模型、AMR、传播建模
- `BioInfo`：AI for Bioinformatics、生物基础模型、科研推理、多组学学习
- `SeqAI`：测序基础模型、单细胞、变异检测、读段分类、纳米孔
- `Agent`：生物医学 Agent、科研助手、文献挖掘、RAG

`arxiv_paper_setting.categories` 也已经默认收紧到更偏 AI 的分类，避免抓太多纯生物论文。

## 配置原则

- `keywords` 负责召回，尽量写成 AI 方法词，不要把纯生物对象词当主词。
- `intent_queries` 负责语义表达，用完整意图描述你真正想看的论文。
- 一个 profile 对应一个长期主题，不要做成“今天想看什么就全塞进去”的杂糅桶。

## 推荐做法

1. 先保留默认四组 profile 跑一周。
2. 每组只保留你真正会长期跟的 5 到 10 个关键词。
3. 把噪声大的词拆掉，比如把 `pathogen foundation model surveillance` 拆回多个原子词。
4. 每周根据命中质量微调，而不是每天大改。

## 适合你课题的追加关键词例子

- `virulence factor`
- `host pathogen interaction`
- `metagenomic classification`
- `phylogenetic inference`
- `genome epidemiology`
- `antimicrobial resistance`
- `protein language model`
- `single-cell foundation model`

## 省心模式

- 默认工作流已经是每日定时运行。
- 每次运行会自动做：抓取、召回、排序、LLM 精排、日报生成。
- 如果你只想“每天打开看结果”，保持当前默认配置即可。

## 论文源怎么配合看

- 日常增量：站内自动推荐
- 方法补充：`arXiv` + `OpenReview`
- 生物医学补充：`PubMed` + `Europe PMC`
- 最新实验结果：`bioRxiv` + `medRxiv`

多源入口见：[/sources](/sources)
