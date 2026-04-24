# Codex Research Stack

[中文 README](./README.zh-CN.md) | [English Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**Turn Codex into a clearer research workspace.**

Codex Research Stack is for researchers who want more than a long chat thread.
It helps you start research tasks with a clearer plan, keep project work organized,
and make reference, writing, and reproducibility checks visible.

![Codex Research Stack Hero](./assets/social-preview.png)

## What this repo helps you do

- decide what kind of task you are doing before tools start running
- turn project work into a visible workspace instead of one long conversation
- keep citations, writing quality, and reproducibility checks in view
- hand verified material into Zotero, Obsidian, and reusable project files

## Who this is for

This repo is a good fit if you work on:

- literature reviews that need citation verification before formal use
- computational social science or mixed-method projects
- platform case studies constrained to browser-visible evidence
- manuscript, revision, or submission workflows that need explicit checks

## What you get

- `research-autopilot`: explains the task route before work expands
- `research-team-orchestrator`: turns project work into visible roles, review steps, and handoffs
- project checks: blocks weak references, weak writing, and incomplete reproducibility
- project scaffolds: gives you a reusable structure instead of starting every project from scratch

## Start here first

1. Open [Getting Started](./docs/getting-started.md) to see how the public repo is organized.
2. Open [Operator Guide](./docs/operator-guide.md) to understand what the system does during a live project.
3. Open [New Project Guide](./docs/new-project-guide.md) to see how a real project begins.

## What it looks like

### Project workspace

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### Checks and stage transitions

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

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

## Learn the repo in layers

- [Getting Started](./docs/getting-started.md)
- [Operator Guide](./docs/operator-guide.md)
- [New Project Guide](./docs/new-project-guide.md)
- [Architecture](./docs/architecture.md)
- [Use Cases](./docs/use-cases.md)
- [Integrations](./docs/integrations.md)

## Why this repo exists

Many agent systems become useful only after a task is already well defined.
Research work usually breaks earlier:

- the wrong kind of task is chosen first
- project work collapses into a single conversation
- references and writing move forward without visible checks
- project files, knowledge tools, and outputs drift apart

Codex Research Stack focuses on that layer. It does not replace Codex. It makes research work easier to follow.

## Pages

- [English Pages](https://avefield509-lang.github.io/codex-research-stack/)
- [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

## If this is useful

If this repo helps you think more clearly about research work in Codex, give it a star.
