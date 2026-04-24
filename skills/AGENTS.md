# AGENTS

本目录是研究型 Codex 工作环境的源规则层。  
项目级 `AGENTS.md` 必须继承这里的约束，并且只能继续收紧，不能扩权。

## 全局研究约束

- 正式学术引用必须基于实时核验，且同时具备：作者、年份、标题、期刊或正式来源、有效 DOI。
- 无 DOI、真实性无法确认、或证据不足的条目，不得进入正式参考文献链。
- 中文为默认协作语言。
- 涉及分析解释的文本，优先采用 `PEEL` 闭环，不使用空洞套话。
- `research-autopilot` 是唯一总入口；项目型任务进入多 agent 规划后，仍不得绕过正式核验链、社媒证据链和复现链。

## 继承规则

- 项目级 `AGENTS.md` 可以：
  - 继续增加 `forbid_skills_mcp`
  - 继续增加 `forbid_write_roots`
  - 进一步收紧 `max_execution_mode`
  - 继续增加 `require_review_for`
  - 继续补充 `project_truth_sources`
- 项目级 `AGENTS.md` 不可以：
  - 放宽这里已经定义的限制
  - 让 reviewer 直接写主产物
  - 绕过 `citation-verifier -> zotero-sync`
  - 绕过 `writing-reference-capture`
  - 绕过 `social-platform-reader / social-platform-mcp`
  - 绕过 `reproducibility-package`

```yaml
agent_constraints:
  forbid_skills_mcp: []
  forbid_write_roots: []
  max_execution_mode: null
  require_review_for:
    - paper_draft
    - revision_package
    - submission_package
    - figures_tables
    - reproducibility_bundle
    - literature_synthesis
    - case_dataset
    - project_map
  project_truth_sources:
    - research-map.md
    - findings-memory.md
    - material-passport.yaml
    - evidence-ledger.yaml
```
