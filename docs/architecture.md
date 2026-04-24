# Architecture

This page is for advanced users who want to understand how the public workspace stays inspectable.

## Planned interface view

The future app should be treated as an interface layer above this repository.
Its job is to surface a simpler daily workflow for ordinary researchers.

That future interface can reasonably organize itself around six user-facing areas:

- `Home`
- `Projects`
- `Sources`
- `Analysis`
- `Writing`
- `Settings`

But those views should sit on top of this repository's public contracts rather than replace them.

## Internal execution view

Under that interface, the stack still keeps four technical layers:

1. **Routing**
   - decide how a task should begin
   - explain the route before execution

2. **Project orchestration**
   - decide whether the work stays single-flow or upgrades into a squad
   - keep producers, reviewers, blockers, and milestones visible

3. **Quality gates**
   - stop weak work before it moves downstream
   - cover citation integrity, evidence provenance, writing quality, and reproducibility

4. **Knowledge and export boundaries**
   - formal references -> Zotero
   - reusable notes and synthesis -> Obsidian
   - runtime traces and stage logs -> project files

## Why the architecture stays explicit

The point is not technical complexity for its own sake.

The point is that research projects often fail quietly:

- the wrong route is chosen too early
- source provenance disappears
- analysis and writing drift apart
- submission materials are prepared before the project is actually reviewable

The explicit layer exists so a human can still inspect what happened.

## Core public assets that remain reusable

- `skills/catalog/`
- `skills/profiles/`
- `skills/schemas/`
- `skills/templates/`
- `scripts/init_research_project.py`
- `scripts/plan_research_team.py`
- `scripts/validate_*.py`

## Repository and future app

The clean relationship is:

- this repository owns the workflow rules, schemas, validators, examples, and public docs
- the future app owns the guided interface, dashboards, and visual project views

The app should read from the repository's public contracts.
It should not become a second source of truth.

## What is intentionally backgrounded

The public product does **not** put these concepts on the first screen:

- skill-first onboarding
- MCP-first onboarding
- dispatch artifact paths
- validator-first workflow

They still exist, but they are treated as advanced infrastructure, not as the primary user experience.
