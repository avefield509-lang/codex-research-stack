# Codex Research Stack

[English README](./README.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**一个以插件为中心的 Codex 研究操作层。**

它重点处理的是很多 agent 仓库默认省略的那一层：

- 执行前先做 route 判断
- 项目型任务进入真实多智能体编排
- 研究流程里有显式 gate，而不是隐式推进
- Zotero、Obsidian、证据链和复现材料之间有清楚的交接边界

![Codex Research Stack 封面](./assets/social-preview.png)

## 这个仓库解决什么问题

多数 coding agent 在“任务已经定义清楚之后”表现不错。

研究工作更容易在更前面出错：

- 一开始就走错 route
- 项目型任务被当成一段长对话，而不是结构化运行时
- 引文、写作和证据在没有 gate 的情况下直接推进
- 知识工具和运行时产物彼此脱节

Codex Research Stack 解决的正是这一层。
它不是替代 Codex，而是把 Codex 变成一个更可读、更可检查的研究系统。

## 你能拿到什么

| 层级 | 作用 |
| --- | --- |
| `research-autopilot` | 在执行前解释 route、profile、helper skills 和下一步动作 |
| `research-team-orchestrator` | 把项目型任务变成 squad、dispatch artifact、review 映射和状态板 |
| Contract + gate 层 | 用显式 schema、canonical 路径和 pipeline gate 阻止弱交接 |
| Evidence + knowledge 集成层 | 把引文核验、Zotero、Obsidian、社媒证据和复现链连起来 |

## 产品预览

### 项目工作被展开成可读的多智能体工作区

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### pipeline 和 gate 逻辑保持可见

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

### 仓库仍然保留一张清楚的 contract 地图

![Architecture Map](./assets/architecture-map.svg)

## 典型用例

- 带 DOI 核验的文献综述
- 需要 squad 级编排的计算社会科学项目
- 只使用浏览器可见证据的平台案例研究
- 写作前先捕获已用引文的工作流
- 带复现和写作质量检查的投稿包

## 快速开始

```powershell
git clone https://github.com/avefield509-lang/codex-research-stack.git
cd codex-research-stack
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
python .\scripts\validate_subagent_registry.py
python .\scripts\validate_agents_contract.py
python .\scripts\validate_research_pipeline.py
python .\scripts\validate_research_stack.py
```

## 从这里开始看

- [Getting Started](./docs/getting-started.md)
- [Operator Guide](./docs/operator-guide.md)
- [New Project Guide](./docs/new-project-guide.md)
- [Architecture](./docs/architecture.md)
- [Use Cases](./docs/use-cases.md)
- [Integrations](./docs/integrations.md)

## Pages

- [English Pages](https://avefield509-lang.github.io/codex-research-stack/)
- [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

## 如果你觉得有用

如果这套思路对你的研究自动化、Codex 编排或证据链工作流有帮助，欢迎点一个 star。
