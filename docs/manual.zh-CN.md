# VELA 总说明书

更新：2026-04-26

VELA 是面向 Codex 的可移植科研工作流环境。它是一套文件化工作方法，不是桌面 app，也不是自动化服务。

## VELA 是什么

VELA 在研究工作分散到对话、笔记、文件、参考文献、数据集和交付物之前，先给项目一个稳定结构。

```text
my-research-project/
  materials/
  evidence/
  claims/
  methods/
  deliverables/
  handoffs/
```

各目录边界如下：

- `materials/`：收集到的来源、文件、URL、截图、数据集、笔记。
- `evidence/`：带来源、访问时间、核验状态、权利或伦理说明的已核验证据。
- `claims/`：候选主张和已有支持的主张。
- `methods/`：假设、编码规则、分析计划、可复现说明。
- `deliverables/`：报告、简报、表格、图、状态说明。
- `handoffs/`：给 Codex 或合作者的有边界任务。

## VELA 不是什么

- 不是聊天界面。
- 不是 HELM 本地看板 app。
- 不是黑箱论文生成器。
- 不会把未经核验的材料直接称为证据。

## 第一次使用

克隆或下载公开仓库：

```powershell
git clone REPOSITORY_URL vela
cd vela
```

`REPOSITORY_URL` 指你正在浏览的 VELA 仓库地址。如果 GitHub 仓库已经改名，以浏览器显示的新地址为准。

把你的研究项目文件夹创建在 VELA 包旁边，不要把私人研究材料放进公开仓库副本。

## 证据纪律

材料只有记录以下信息后才进入证据层：

- 来源定位；
- 访问时间；
- 核验状态；
- 权利或伦理说明；
- 支持的主张；
- 支持关系解释。

这一区分是 VELA 的核心。阅读清单、截图文件夹或模型摘要都不能直接等同于已核验证据。

## Codex 交接模板

请先写一个小范围交接，再让 Codex 工作：

```markdown
任务：
相关文件：
约束：
预期输出：
已知缺口：
复核标准：
```

交接范围应足够小，使复核者能够判断 Codex 是否越界。

## 与 HELM 的关系

VELA 与 HELM 是两个独立产品：

| 产品 | 角色 | 能否独立使用 |
| --- | --- | --- |
| VELA | 科研工作流环境 | 可以 |
| HELM | 本地科研看板 | 可以 |

HELM 后续可以读取 VELA 项目状态，用于展示状态、证据、交付物、环境健康和交接准备度。VELA 本身不依赖 HELM。

## 仓库区域

- `docs/`：公开文档和 Pages 站点。
- `docs/assets/brand/`：已确认的视觉资产。
- `examples/`：小型项目示例。
- `scripts/`：初始化和验证辅助脚本。
- `skills/`：工作流包使用的 Codex skill、profile、schema 和模板层。
