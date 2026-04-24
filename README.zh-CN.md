# Codex Research Stack

[English README](./README.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**把 Codex 变成一个更清楚的研究工作台。**

Codex Research Stack 适合这样的研究者：你不想把研究项目做成一段无限拉长的对话，
而是希望任务开始前先有判断，项目推进中有清楚分工，关键地方有显式检查，
最后还能把材料沉淀进 Zotero、Obsidian 和项目文件。

![Codex Research Stack 封面](./assets/social-preview.png)

## 这个仓库能帮你做什么

- 在工具真正开始跑之前，先判断这是什么任务、适合怎么做
- 把项目工作变成一个能回看的工作区，而不是一段聊天记录
- 让引文、写作质量和复现检查保持可见
- 把核验过的材料交接到 Zotero、Obsidian 和可复用的项目文件里

## 什么人会用得上

如果你常做下面这些事情，这个仓库就值得继续看：

- 需要正式引文核验的文献综述
- 计算社会科学或混合方法研究项目
- 只使用浏览器可见证据的平台案例研究
- 需要显式检查点的论文写作、返修和投稿流程

## 你实际会得到什么

- `research-autopilot`：先解释任务怎么走，再进入执行
- `research-team-orchestrator`：把项目工作变成可见分工、审查和交接
- 一套检查机制：在引文、写作和复现不合格时阻断推进
- 一套项目骨架：让你每次开新项目都不必从零搭结构

## 如果你现在只有 3 分钟

1. 先看 [Getting Started](./docs/getting-started.md)，知道公开仓库怎么组织。
2. 再看 [Operator Guide](./docs/operator-guide.md)，理解项目跑起来后系统在做什么。
3. 最后看 [New Project Guide](./docs/new-project-guide.md)，了解一个真实项目怎么开始。

## 它大概长什么样

### 项目工作区

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### 检查点与阶段推进

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

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

## 建议按这个顺序了解仓库

- [Getting Started](./docs/getting-started.md)
- [Operator Guide](./docs/operator-guide.md)
- [New Project Guide](./docs/new-project-guide.md)
- [Architecture](./docs/architecture.md)
- [Use Cases](./docs/use-cases.md)
- [Integrations](./docs/integrations.md)

## 为什么会有这个仓库

很多 agent 系统在“任务已经定义清楚之后”才开始发挥作用。
研究工作更容易在更前面出问题：

- 一开始就把任务判断错了
- 项目工作退化成一段长对话
- 引文和写作在没有显式检查的情况下往前推进
- 项目文件、知识工具和最终产物彼此脱节

Codex Research Stack 关注的就是这一层。它不替代 Codex，只是把研究工作这层整理得更清楚。

## Pages

- [English Pages](https://avefield509-lang.github.io/codex-research-stack/)
- [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

## 如果你觉得有帮助

如果这套思路对你在 Codex 里做研究更有条理，欢迎点一个 star。
