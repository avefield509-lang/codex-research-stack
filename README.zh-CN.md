<div align="center">
  <img src="./docs/assets/brand/vela-workflow-mark.png" alt="VELA 分层帆形标志" width="132">
  <h1>VELA</h1>
  <p><strong>Versatile Experiment Lab &amp; Automation</strong></p>
  <p><em>面向 Codex 科研工作的便携式项目工作包</em></p>
  <p>
    <a href="./README.md">English</a>
    · <a href="https://marcus-ai4ss.github.io/VELA/">Pages</a>
    · <a href="./docs/getting-started.md">快速开始</a>
    · <a href="./docs/imports/vela-helm-interface.md">HELM 接口</a>
    · <a href="./docs/workflow-core.md">工作流核心</a>
    · <a href="./docs/evidence-lifecycle.md">证据生命周期</a>
    · <a href="./docs/quality-checks.md">质量检查</a>
  </p>
</div>

VELA = **Versatile Experiment Lab & Automation**。它给 Codex 一个有边界、证据感知、可复核的科研任务操作层，封装项目结构、`AGENTS.md` 指令、Codex 交接合约、证据台账、验证报告和 HELM 可读状态。

它不是桌面 app，不是聊天界面，不是论文生成器，也不是隐藏自动执行的 agent。VELA 准备有边界的任务，Codex 执行，用户复核；[HELM](https://github.com/Marcus-AI4SS/HELM) 是可选的 Hub for Evidence, Logs & Monitoring，可以读取同一套项目状态。

## 五分钟开始

```powershell
git clone https://github.com/Marcus-AI4SS/VELA.git vela
cd vela
.\install.ps1
.\vela.ps1 init ..\my-research-project --skip-codex-trust
cd ..\my-research-project
..\vela\vela.ps1 handoff new --template claim-check
..\vela\vela.ps1 handoff lint handoffs\H001.yaml
..\vela\vela.ps1 validate . --repair-context
```

生成的项目会包含 `materials/`、`evidence/`、`claims/`、`methods/`、`deliverables/`、`handoffs/`、`logs/`、`.codex/` 和 `.vela/context.json`。

## VELA 帮你解决什么

| 需求 | VELA 提供什么 |
| --- | --- |
| 启动项目时不丢结构 | 给研究问题、范围、来源和预期交付物一个清楚位置 |
| 保持证据诚实 | 区分已收集材料和已核验证据的生命周期 |
| 和 Codex 协作但不失控 | 交接提示必须说明任务、文件、约束、预期输出和已知缺口 |
| 接入 HELM | 通过 `.vela/context.json` 暴露 `vela.project.context.v1` |
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

```yaml
schema_version: vela.codex.handoff.v1
handoff_id: H001
scope:
  task: 检查某个 claim 是否被指定 evidence 支持
  relevant_files:
    - claims/C001.md
    - evidence/E001.yaml
constraints:
  - 不新增主张
expected_output:
  path: logs/codex-runs/H001-result.md
review_standard:
  - 每个支撑判断必须指向 evidence_id
```

交接应该足够小。Codex 需要获得完成任务所需的上下文，而不是获得重写整个项目的开放授权。

## VELA 与 HELM

| 产品 | 角色 | 能否独立存在 |
| --- | --- | --- |
| **VELA** = Versatile Experiment Lab & Automation | 便携式项目实验室、自动化边界和 Codex 工作包 | 可以 |
| **HELM** = Hub for Evidence, Logs & Monitoring | 展示状态、证据、日志、文件、本地检查和 Codex 说明的本地看板 | 可以 |

只需要可移植工作流时，单独使用 VELA。需要本地可视化看板时，再接入 HELM。

共享导入契约有两个方向：

- `vela.project.context.v1`：VELA 暴露项目状态，供 HELM 读取。
- `helm.codex.handoff.v1`：HELM 准备有边界的 Codex 交接包，供用户复制回 Codex；只有在用户显式保存或导出时，VELA 才应把它存入项目。

见 [VELA 与 HELM 导入接口](./docs/imports/vela-helm-interface.md)。

## 继续阅读

- [快速开始](./docs/getting-started.md)
- [工作流核心](./docs/workflow-core.md)
- [证据生命周期](./docs/evidence-lifecycle.md)
- [质量检查](./docs/quality-checks.md)
- [VELA 与 HELM 导入接口](./docs/imports/vela-helm-interface.md)
- [使用场景](./docs/use-cases.md)
- [可选集成](./docs/integrations.md)
- [FAQ](./docs/faq.md)

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| `docs/` | 公开文档、GitHub Pages 和确认后的视觉资产 |
| `docs/imports/` | VELA 与 HELM 的导入契约 |
| `docs/sync-log/` | 本地跨仓同步记录 |
| `examples/` | 可检查的最小项目和快速演示 |
| `package/` | `vela init` 复制到研究项目里的 starter package |
| `schemas/` | context 和 handoff 的机器可读 schema |
| `scripts/` | 初始化、验证和本地维护辅助脚本 |
| `skills/` | Codex skill、profile、schema 和模板层 |
