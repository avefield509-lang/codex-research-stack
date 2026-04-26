<div align="center">
  <img src="./docs/assets/brand/vela-workflow-mark.png" alt="VELA 分层帆形标志" width="132">
  <h1>VELA</h1>
  <p><strong>面向 Codex 科研工作的工作流环境包</strong></p>
  <p><em>Versioned Evidence Lifecycle Architecture</em></p>
  <p>
    <a href="./README.md">English</a>
    · <a href="./docs/getting-started.md">快速开始</a>
    · <a href="./docs/workflow-core.md">工作流核心</a>
    · <a href="./docs/evidence-lifecycle.md">证据生命周期</a>
    · <a href="./docs/quality-checks.md">质量检查</a>
  </p>
</div>

![VELA 视觉系统](./docs/assets/brand/vela-brand-board-reference.png)

VELA 是一套可以放进用户自己 Codex 工作空间的可移植科研工作流环境。它给研究项目提供稳定的运行层：材料、证据、主张、方法说明、交付物和 Codex 交接保持分层、可读、可复核。

它不是桌面 app，不是聊天界面，也不是黑箱论文生成器。VELA 是工作流包；HELM 是可选本地科研看板，后续可以读取同一套项目状态。

## 五分钟开始

```powershell
git clone REPOSITORY_URL vela
cd vela
```

然后在旁边创建你的研究项目文件夹：

```text
my-research-project/
  materials/
  evidence/
  claims/
  methods/
  deliverables/
  handoffs/
```

`REPOSITORY_URL` 指当前公开 VELA 仓库地址。

## VELA 帮你解决什么

| 需求 | VELA 提供什么 |
| --- | --- |
| 启动项目时不丢结构 | 给研究问题、范围、来源和预期交付物一个清楚位置 |
| 保持证据诚实 | 区分已收集材料和已核验证据的生命周期 |
| 和 Codex 协作但不失控 | 交接提示必须说明任务、文件、约束、预期输出和已知缺口 |
| 准备可分享产物 | 在交付物离开项目之前暴露无支持主张和私人材料风险 |

## 工作流分层

| 层级 | 放什么 | 不要混同为 |
| --- | --- | --- |
| Materials | DOI、URL、文件、数据集、笔记、截图 | 证据 |
| Evidence | 带来源、访问时间、核验状态、伦理或权利说明的材料 | 阅读清单 |
| Claims | 候选主张和已有支持的主张 | 最终发现 |
| Methods | 假设、编码规则、分析计划、可复现说明 | 结果 |
| Deliverables | 报告、简报、图表、状态说明 | 原始项目状态 |
| Handoffs | 给 Codex 或合作者的有边界任务 | 整个项目外包 |

## 一个合格的 Codex 交接

```markdown
任务：
相关文件：
约束：
预期输出：
已知缺口：
复核标准：
```

交接应该足够小。Codex 需要获得完成任务所需的上下文，而不是获得重写整个项目的开放授权。

## VELA 与 HELM

| 产品 | 角色 | 能否独立存在 |
| --- | --- | --- |
| **VELA** | 面向 Codex 的科研工作流环境 | 可以 |
| **HELM** | 展示状态、证据、交付物、环境健康和交接情况的本地科研看板 | 可以 |

只需要可移植工作流时，单独使用 VELA。需要本地可视化看板时，再接入 HELM。

## 继续阅读

- [快速开始](./docs/getting-started.md)
- [工作流核心](./docs/workflow-core.md)
- [证据生命周期](./docs/evidence-lifecycle.md)
- [质量检查](./docs/quality-checks.md)
- [使用场景](./docs/use-cases.md)
- [可选集成](./docs/integrations.md)
- [FAQ](./docs/faq.md)

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| `docs/` | 公开文档、GitHub Pages 和确认后的视觉资产 |
| `examples/` | 可检查的最小项目和快速演示 |
| `scripts/` | 初始化、验证和本地维护辅助脚本 |
| `skills/` | Codex skill、profile、schema 和模板层 |

ChatGPT-image2 生成草稿应只放在本地 `image2-exports/`。该目录已被忽略，不应出现在 GitHub 根目录。

## 视觉语言

VELA 使用淡蓝与白色表面、深海军蓝文字、分层帆形、证据路径、导航环和柔和波层。品牌素材位于 [`docs/assets/brand`](./docs/assets/brand/)，公开规则位于 [`docs/brand.md`](./docs/brand.md)。
