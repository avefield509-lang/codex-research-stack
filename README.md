# Codex Research Stack

[中文首页](./README.zh-CN.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**A plugin-first research operating layer for Codex.**

Codex Research Stack makes four things explicit:

- route selection before execution
- real multi-agent project orchestration
- visible research pipeline gates
- evidence-aware handoff into Zotero, Obsidian, and reproducibility artifacts

![Codex Research Stack Hero](./assets/social-preview.png)

## Why it matters

Most agent systems are strongest after a task is already well defined.
Research work usually fails earlier:

- the wrong route is chosen first
- project work collapses into one long chat
- citations, writing, and evidence move without explicit checks
- runtime artifacts and knowledge tools drift apart

This repository addresses that layer without replacing Codex.

## What you get

- `research-autopilot` for route, profile, helper skills, and next action
- `research-team-orchestrator` for squads, dispatch artifacts, reviewer mappings, and project state
- explicit contract and gate assets for inspectable runs
- integrations for citation verification, Zotero, Obsidian, social evidence, and reproducibility

## Product tour

### Multi-agent project workspace

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### Pipeline and gate logic

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

## Typical use cases

- literature reviews with DOI verification before formal use
- computational social science projects that need coordinated squads
- social-platform case studies constrained to browser-visible evidence
- writing workflows where used references are captured before export
- submission packages with reproducibility and writing-quality checks

## Quick start

```powershell
git clone https://github.com/avefield509-lang/codex-research-stack.git
cd codex-research-stack
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
python .\scripts\validate_subagent_registry.py
python .\scripts\validate_agents_contract.py
python .\scripts\validate_research_pipeline.py
python .\scripts\validate_research_stack.py
```

## Start here

- [Getting Started](./docs/getting-started.md)
- [Operator Guide](./docs/operator-guide.md)
- [New Project Guide](./docs/new-project-guide.md)
- [Architecture](./docs/architecture.md)
- [Use Cases](./docs/use-cases.md)
- [Integrations](./docs/integrations.md)

## Pages

- [English Pages](https://avefield509-lang.github.io/codex-research-stack/)
- [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

## Star this repo

If this project helps you think more clearly about research routing, multi-agent contracts, or evidence-aware workflows in Codex, give it a star.
