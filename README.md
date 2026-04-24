# Codex Research Stack

[中文 README](./README.zh-CN.md) | [Pages](https://avefield509-lang.github.io/codex-research-stack/) | [中文 Pages](https://avefield509-lang.github.io/codex-research-stack/zh/)

**A research workspace for Codex, built for social scientists.**

Codex Research Stack helps you manage the whole research path in one local-first workspace:

- start and track projects
- collect and organize sources
- move into analysis with method-aware squads
- draft, review, and prepare submission materials
- keep local integrations visible instead of hidden in scattered scripts

![Codex Research Stack Hero](./assets/social-preview.png)

## Who it is for

- researchers doing literature reviews and evidence synthesis
- computational social scientists working across text, platform data, networks, and reproducibility
- policy and communication researchers who need browser-visible source capture
- writers preparing drafts, response packs, and submission-ready materials

## What you can do

### Projects

Start a new study, track milestones and blockers, and keep the project state visible instead of burying everything in one long chat.

### Sources

Bring together literature, policy texts, websites, social evidence, and datasets in one evidence-aware workflow.

### Analysis

Move from notes and extracted claims to qualitative coding, quant analysis, network work, and project-aware research squads.

### Writing

Work on outlines, drafts, writing-quality checks, citation alignment, response packs, and submission readiness in one place.

### Settings

Detect Python, Codex, Zotero, Obsidian, Git, browser tools, and advanced research stack components without forcing every integration upfront.

## Typical workflows

- **Literature review**: define the review question, collect candidate sources, verify formal references, and turn the project into a reviewable synthesis.
- **Social-platform case study**: capture browser-visible evidence, keep provenance explicit, and prepare material for later coding and analysis.
- **Computational social science project**: coordinate literature, sources, analysis, writing, and reproducibility as one project system.
- **Writing and submission**: move from evidence and analysis into drafts, writing checks, revision packs, and final submission materials.

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

### 3. Open the desktop app or inspect the route preview

Desktop app source:

- `apps/desktop`

Preview a route from a research task:

```powershell
python .\scripts\public_app_bridge.py route_preview --payload "{\"task\":\"做一个系统文献综述，并同步 Zotero 和写作大纲。\"}"
```

## Product structure

- **Home**: workspace overview, current project, next-step guidance
- **Projects**: project list, stage flow, blockers, milestones, new project wizard
- **Sources**: literature, datasets, websites, social evidence, integration status
- **Analysis**: research squads and method-aware analysis lanes
- **Writing**: drafts, writing checks, submission readiness
- **Settings**: local setup, integrations, validators, and advanced controls

## Integrations

- **Zotero** for formal references
- **Obsidian** for long-lived knowledge notes
- **Browser-visible evidence** for social and platform cases
- **Project scripts and validators** for transparent local workflows

## Advanced users

If you want to inspect the internal research routing and orchestration layer, start here:

- [Getting Started](./docs/getting-started.md)
- [Architecture](./docs/architecture.md)
- [Use Cases](./docs/use-cases.md)
- [Integrations](./docs/integrations.md)
- [Operator Guide](./docs/operator-guide.md)

## Why this is different

This repository is not trying to be:

- a map-first literature discovery product
- a skill-install-first Codex toolbox
- a hidden one-shot agent that replaces project structure

It is trying to make the whole research workflow inspectable:

- project state
- source provenance
- method-aware collaboration
- writing quality and submission readiness

## Star this repo

If this project helps you turn Codex into a clearer research workspace, give it a star.
