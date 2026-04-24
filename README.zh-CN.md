# Codex Research Stack

[English README](./README.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**一个面向社会科学研究者的 Codex 研究工作台。**

Codex Research Stack 关注的不是“再多装几个 skill”，而是把研究项目真正放进同一条工作流里：

- 启动并跟踪项目
- 组织文献、网页、平台证据和数据
- 进入分析与研究团队协作
- 推进写作、返修和投稿准备
- 让本地集成和研究状态保持可见

![Codex Research Stack 封面](./assets/social-preview.png)

## 它适合谁

- 做文献综述和证据综合的研究者
- 做文本、平台数据、网络与复现的计算社会科学研究者
- 需要浏览器可见证据采集的平台案例研究者
- 正在写作、返修和准备投稿包的学术写作者

## 你可以用它做什么

### 项目

启动研究项目、查看阶段、跟踪阻塞点和里程碑，而不是把项目压缩成一段很长的聊天记录。

### 材料与来源

把文献、政策文本、网页、社媒证据和数据集放进同一条以证据为中心的研究流程。

### 分析与研究协作

从笔记、论点和抽取结果，进入质性编码、量化分析、网络分析，以及与项目绑定的研究团队协作。

### 写作与投稿准备

统一处理提纲、草稿、写作质量检查、引文对齐、回复材料包和投稿准备度。

### 设置与环境状态

探测 Python、Codex、Zotero、Obsidian、Git、浏览器环境，以及需要时才展开的高级设置。

## 典型工作流

- **文献综述**：先定义综述问题，再收集候选文献、核验正式引用、形成可复核的综合稿。
- **社媒或平台案例研究**：先采集浏览器可见证据，保留来源与权限边界，再进入编码和分析。
- **计算社会科学项目**：把文献、材料、分析、写作和复现串成一个项目系统。
- **写作与投稿**：从证据和分析推进到草稿、写作检查、返修包和最终投稿材料。

## 快速开始

### 1. 克隆仓库

```powershell
git clone https://github.com/avefield509-lang/codex-research-stack.git
cd codex-research-stack
```

### 2. 创建项目骨架

跨平台方式：

```powershell
python .\scripts\init_research_project.py --path ".\examples\demo-project" --route-hint "general-research"
```

Windows PowerShell 快捷方式：

```powershell
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
```

### 3. 打开桌面端或预览研究路径

桌面端源码在：

- `apps/desktop`

也可以直接从任务描述预览任务路径：

```powershell
python .\scripts\public_app_bridge.py route_preview --payload "{\"task\":\"做一个系统文献综述，并同步 Zotero 和写作大纲。\"}"
```

## 产品结构

- **首页**：工作台总览、当前项目、下一步建议
- **项目**：项目列表、阶段流、阻塞点、里程碑、新项目向导
- **材料与来源**：文献、数据、网页、社媒证据和集成状态
- **分析**：研究团队与方法工作区
- **写作**：草稿、写作检查、投稿准备度
- **设置**：本地配置、集成、校验脚本和高级项

## 集成方向

- **Zotero**：正式文献边界
- **Obsidian**：长期知识沉淀
- **浏览器可见证据**：平台案例与网页证据
- **本地脚本与校验器**：透明而可复查的本地工作流

## 高级用户入口

如果你想看底层的任务路径、项目编排、检查点和校验器，再从这里进入：

- [快速开始](./docs/getting-started.md)
- [架构说明](./docs/architecture.md)
- [典型用例](./docs/use-cases.md)
- [集成说明](./docs/integrations.md)
- [操作指南](./docs/operator-guide.md)

## 它的差异化在哪里

这个仓库不想做成：

- 一个图谱优先的文献发现产品
- 一个 skill 安装器集合
- 一个把项目结构彻底隐藏起来的一次性 agent

它更想解决的是：

- 项目状态可见
- 证据来源可追溯
- 方法工作流可执行
- 写作与投稿准备有明确检查点

## 如果你觉得有用

如果这套思路能帮助你把 Codex 变成更清楚的研究工作台，欢迎点一个 star。
