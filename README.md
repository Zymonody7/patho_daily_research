# Daily Paper Reader
## 每日 AI for Bioinformatics 论文追踪与自动解读平台

* 一个开源的 **AI for Bioinformatics / Biomedical AI 论文推荐、阅读与自动解读平台**。  
* 默认订阅模板已经切到 **AI 方法优先**：生物基础模型、科研 Agent、测序 AI、病原组学中的 AI 方法。  
* Open-source daily paper recommendation, reading, and Q&A platform powered by **GitHub Actions** and **GitHub Pages**, now tuned for **AI + bioinformatics** workflows.

[在线演示](https://ziwenhahaha.github.io/daily-paper-reader) \
[5 分钟快速启动](#5-分钟快速启动)

## 你能快速得到什么

- 每日自动抓取 `arXiv + Europe PMC + PubMed + bioRxiv + medRxiv`，并做跨源去重归并
- 基于关键词、研究方向与兴趣生成个性化推荐流
- 沉浸式阅读体验，快速查看摘要、链接与核心信息
- 每次日更都自动经过 LLM 精排、总结与文档生成，也就是每日抓取、每日解读
- 自动把每日解读沉淀成站内知识库索引，方便长期积累
- AI 论文问答助手，支持边读边问
- 预置 AI 方法优先的默认订阅配置，尽量减少纯生物论文噪声
- 站内新增多论文源导航，可快速跳转 PubMed、bioRxiv、medRxiv、OpenReview、Nature Portfolio 等入口
- GitHub Actions 自动更新，无需手动维护
- GitHub Pages 一键部署，无需额外服务器
- Fork 即用，5 分钟完成初始化

## 适合谁使用

- 想持续追踪 AI for Bioinformatics、Biomedical AI、Scientific Agent、Foundation Model 新论文的学生、研究者和工程师
- 想搭建私人论文推荐站点、实验室论文主页或阅读面板的开发者
- 想把“发现论文 → 阅读论文 → 提问总结”放进同一工作流的人

## 默认研究主题

- `PathoAI`：病原组学中的基础模型、病原检测模型、宏基因组分类、AMR 预测
- `BioInfo`：AI for Bioinformatics、生物基础模型、多组学学习、科研推理
- `SeqAI`：测序基础模型、单细胞、变异检测、读段分类、纳米孔测序
- `Agent`：生物医学 Agent、科研助手、文献挖掘、检索增强

## 多论文源入口

项目的自动抓取主链路现在已经接入多源抓取，并在原始层做合并去重。默认仍然把 `arXiv` 放在 AI 方法侧的主入口，同时补足生物医学文献源：

- `arXiv`：默认抓 `cs.AI`、`cs.LG`、`cs.CL`、`stat.ML`、`q-bio.GN`、`q-bio.QM`、`eess.AS`
- `Europe PMC`
- `PubMed`
- `bioRxiv`
- `medRxiv`
- `OpenReview`：ICLR、NeurIPS、ICML、ML4H 等会议讨论页
- `Nature Portfolio / Genome Biology / Bioinformatics / NAR / Briefings in Bioinformatics`：重点期刊

你可以继续在 `config.yaml` 里精修 `intent_profiles` 和 `arxiv_paper_setting.categories`，把主题进一步压到你最关心的 AI 方向。

## 5 分钟快速启动

### 1. 提前准备两个密钥

#### 1.1 获取大模型密钥

> 不是柏拉图行不行？对比了市面上的集成平台，柏拉图是性价比最高的，柏拉图平台上有按0.001元/次的reranker模型调用，和非常便宜的gemini3 flash模型: 提示¥0.5/M tokens 补全 ¥3/M tokens，建议还是配这个，每天花费1~3毛钱。

- 打开 **柏拉图 API 平台** [https://api.bltcy.ai/](https://api.bltcy.ai/) 完成注册/登录
- 充值 5 元
- 新建密钥

#### 1.2 获取 Github 访问许可 
- 打开 [GitHub 新建 PAT 页面](https://github.com/settings/tokens/new?type=beta&scopes=repo,workflow,gist) 
- 勾选 **这三项权限**（上面链接已预勾选）：
  - `repo`
  - `workflow`
  - `gist`

### 2. Fork 本仓库 （第二步往后的操作均需要在自己仓库中点击）
Fork 该仓库到自己账号下，建议仓库名字保持原样。

### 3. 开启 Actions
进入 Fork 的仓库 → 页面上方点 `Actions` → 左边 `daily-paper-reader` 开启

### 4. 开启 GitHub Pages
- GitHub Pages 设置 点击此链接[../../settings/pages](../../settings/pages)  或者 依次点击 `Settings → Pages → Source`
- 
- 选 `Deploy from a branch`，分支 `main`，目录 `/(root)`，保存
- 静候1分钟，站点地址会显示在页面顶部

### 5. 打开站点验收
访问 `https://<你的用户名>.github.io/<仓库名>/`

此后所有操作均在网页端执行

## 版本迭代（请持续更新）

| 版本 | 日期 | 更新内容 |
| --- | --- | --- |
| v1.0.0 | 2026-02-19 | 基础功能实现完成 |
| v1.1.0 | 2026-02-28 | 优化订阅面板逻辑，不再需要手动记关键词 |
| v1.2.0 | 2026-03-04 | 优化使用体验 |

## Star 曲线（项目热度）

[![Star History Chart](https://api.star-history.com/svg?repos=ziwenhahaha/daily-paper-reader&type=Date)](https://star-history.com/#ziwenhahaha/daily-paper-reader&Date)
