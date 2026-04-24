# Codex Research Stack

[中文首页](./README.zh-CN.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**A plugin-first research operating layer for Codex.**

It focuses on the part most agent stacks leave implicit:

- route selection before execution
- real multi-agent project orchestration
- explicit research pipeline gates
- evidence-aware handoff into Zotero, Obsidian, and reproducibility artifacts

![Codex Research Stack Hero](./assets/social-preview.png)

## Why it exists

Most coding-agent systems are strongest after a task is already well defined.

Research work usually breaks earlier:

- the wrong route is chosen before execution starts
- project work is treated like one long chat instead of a structured runtime
- citations, writing, and evidence move without visible gates
- knowledge tools and runtime artifacts drift apart

Codex Research Stack addresses that layer.
It does not replace Codex.
It makes Codex legible as a research system.

## What you get

| Layer | What it does |
| --- | --- |
| `research-autopilot` | Explains the route, profile, helper skills, and next action before work expands |
| `research-team-orchestrator` | Turns project work into squads, dispatch artifacts, reviewer mappings, and project state |
| Contract + gate layer | Blocks weak handoffs through explicit schemas, canonical paths, and pipeline gates |
| Evidence + knowledge integrations | Connects citation verification, Zotero, Obsidian, social evidence, and reproducibility |

## Product tour

### Project work becomes a readable workspace

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### Pipeline and gate logic stay visible

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

### The repo still exposes a clear contract map

![Architecture Map](./assets/architecture-map.svg)

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
