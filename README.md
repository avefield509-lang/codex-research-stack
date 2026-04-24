# Codex Research Stack

[中文 README](./README.zh-CN.md) | [Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**A clearer research workspace for Codex.**

Codex Research Stack is for researchers who want more than a long chat thread.
It helps you start with a clearer plan, keep project work organized, and keep
references, writing, and reproducibility checks visible.

![Codex Research Stack Hero](./assets/social-preview.png)

## Who it is for

- researchers doing literature reviews and evidence synthesis
- computational social scientists working across text, platform data, networks, and reproducibility
- policy and communication researchers who need browser-visible source capture
- writers preparing drafts, revision packs, and submission-ready materials

## What this repo helps you do

- decide what kind of research task you are doing before tools start running
- turn project work into a visible workspace instead of one long conversation
- keep references, writing quality, and reproducibility checks in view
- hand verified material into Zotero, Obsidian, and reusable project files

## What you get

- `research-autopilot`: explains the task path before work expands
- `research-team-orchestrator`: turns project work into visible roles, review steps, and handoffs
- project checks: blocks weak references, weak writing, and incomplete reproducibility
- project scaffolds: gives you a reusable structure instead of starting every project from scratch

## If you only want the essentials

1. Read [Getting Started](./docs/getting-started.md) for the shortest onboarding path.
2. Read [Operator Guide](./docs/operator-guide.md) to understand what happens during a live project.
3. Read [New Project Guide](./docs/new-project-guide.md) to see how a real project begins.

## Typical workflows

- **Literature review**: define a review question, collect candidate sources, verify formal references, and turn the project into a reviewable synthesis.
- **Social-platform case study**: capture browser-visible evidence, keep provenance explicit, and prepare material for later coding and analysis.
- **Computational social science project**: coordinate literature, sources, analysis, writing, and reproducibility as one project system.
- **Writing and submission**: move from evidence and analysis into drafts, writing checks, revision packs, and final submission materials.

## What it looks like

### Project workspace

![Multi-Agent Workspace](./assets/multi-agent-workspace.png)

### Checks and stage transitions

![Pipeline and Gates](./assets/pipeline-gates-overview.png)

## Quick start

### 1. Clone the repository

```powershell
git clone https://github.com/avefield509-lang/codex-research-stack.git
cd codex-research-stack
```

### 2. Create a project scaffold

Cross-platform:

```powershell
python .\scripts\init_research_project.py --path ".\examples\demo-project" --route-hint "general-research"
```

Windows PowerShell shortcut:

```powershell
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
```

### 3. Preview a task path

```powershell
python .\scripts\public_app_bridge.py route_preview --payload "{\"task\":\"做一个系统文献综述，并同步 Zotero 和写作大纲。\"}"
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

If this project helps you turn Codex into a clearer research workspace, give it a star.
