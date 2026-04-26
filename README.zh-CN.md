# VELA

[English README](./README.md) | [文档](https://marcus-ai4ss.github.io/codex-research-stack/zh/)

**VELA = Versioned Evidence Lifecycle Architecture。**

公开英文副标题：**Workflow Environment Package**。中文副标题：**科研工作流环境**。

VELA 是面向 Codex 的可移植科研工作流环境。它封装项目结构、证据规则、方法检查点、交接约定和视觉语言，使研究从问题提出到交付物产出都能保留可追踪路径。它不是桌面 app，不是聊天界面，也不是黑箱论文生成器。

![VELA 视觉系统](./docs/assets/brand/vela-brand-board-reference.png)

## 产品边界

用户不安装本地看板 app，也可以把 VELA 下载到自己的 Codex 环境中使用。VELA 的核心交付物是工作流环境：文档、配置、提示词、证据模板、项目状态约定和可复现交接规则。

HELM 是可选本地科研看板的独立品牌。HELM 可以读取项目状态、展示证据和交付物、监测环境健康，并准备 Codex 上下文交接。VELA 与 HELM 是两个独立产品，共用同一套视觉语言：**可分别使用，组合后更顺手。**

## VELA 提供什么

- **版本化证据生命周期。** 材料、证据、主张、方法产物和交付物保持区分，字段和复核条件满足后才进入下一层。
- **可组合工作流阶段。** 收集、分析、验证、报告是显式阶段，缺口必须可定位、可修复。
- **Codex 交接结构。** 交给 Codex 的上下文有范围、有依据，并绑定项目状态，而不是散落在聊天记录里。
- **可移植环境包。** VELA 面向用户自己的本地 Codex 设置，不依赖 HELM 才能运行。
- **共享视觉系统。** 淡蓝与白色、分层帆形、证据路径、导航环和克制的 iOS 风格表面，形成清晰但不过度工具化的识别。

## 与 HELM 的关系

| 品牌 | 公开角色 | 是否依赖对方 |
| --- | --- | --- |
| **VELA** | 面向 Codex 科研工作的工作流环境包 | 否 |
| **HELM** | 管理项目状态、证据、交付物、环境健康和 Codex 交接的本地科研看板 | 否 |

HELM 不是 VELA 的控制器。VELA 也不是只能在 HELM 里运行的插件。两者的连接点是项目状态和交接上下文。

## 视觉语言

视觉系统保持简洁、轻、安静：淡蓝、白色、深海军蓝文字、半透明层、证据路径和导航节点。核心素材位于 [`docs/assets/brand`](./docs/assets/brand/)。

![VELA 与 HELM 关系](./docs/assets/brand/vela-helm-relationship-board-reference.png)

## 文档

- [Pages 首页](https://marcus-ai4ss.github.io/codex-research-stack/zh/)
- [快速开始](./docs/getting-started.md)
- [安装说明](./docs/installation.md)
- [工作流核心](./docs/workflow-core.md)
- [可选集成](./docs/integrations.md)
- [路线图](./docs/roadmap.md)

## 公开命名说明

从本轮品牌重构起，README 和 Pages 的公开叙事使用 **VELA** 指代科研工作流环境，使用 **HELM** 指代可选本地科研看板。历史文档或实现文件中的旧内部模块名会在后续安全迁移时逐步处理。
