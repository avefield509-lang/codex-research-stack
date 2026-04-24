# Codex Research Stack

[English README](./README.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**一个以插件为中心的 Codex 研究操作层。**

Codex Research Stack 重点把四件事显式化：

- 执行前先做 route 判断
- 项目型任务进入真实多智能体编排
- 研究流程里有可见的 pipeline gate
- Zotero、Obsidian、证据链和复现材料之间有清楚交接

![Codex Research Stack 封面](./assets/social-preview.png)

## 为什么它有价值

很多 agent 系统在“任务已经定义清楚之后”表现不错。
研究工作更容易在更前面出错：

- 一开始就走错 route
- 项目型任务退化成一段长对话
- 引文、写作和证据在没有显式检查的情况下推进
- 运行时产物和知识工具彼此脱节

这个仓库解决的正是这一层，而且不替代 Codex。

## 你能拿到什么

- `research-autopilot`：负责 route、profile、helper skills 和下一步动作
- `research-team-orchestrator`：负责 squad、dispatch artifact、review 映射和项目状态
- 显式 contract / gate 资产：让运行过程可检查
- 与引文核验、Zotero、Obsidian、社媒证据、复现链的集成

## 产品预览

### 多智能体项目工作区

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### pipeline 与 gate 逻辑

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

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
