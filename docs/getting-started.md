# Getting Started

## What You Get

- route selection before execution
- project-type multi-agent orchestration
- research pipeline gates
- public templates for project scaffolding
- plugin assets for `research-autopilot`

## Quick Path

1. Clone the repo.
2. Read the root `README.md`.
3. Read [Operator Guide](./operator-guide.md) if you want the system model first.
4. Read [New Project Guide](./new-project-guide.md) if you want the fastest path to a working project.
5. Inspect `skills/catalog/` and `skills/schemas/`.
6. Initialize a demo project with `scripts/init-research-project.ps1`.
7. Run the public validators.

## Public Defaults

- plugin-first presentation
- repo-local paths
- no cloud credentials
- no private machine assumptions

## Minimal Commands

Create a project scaffold:

```powershell
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
```

Plan a research team for a literature-style project:

```powershell
python .\scripts\plan_research_team.py --project-root ".\examples\minimal-project" --route-id "literature-review" --target-item-count 20 --work-unit discovery --work-unit writing --deliverable-type literature_synthesis --sync-target zotero --sync-target obsidian
```

Validate the public stack:

```powershell
python .\scripts\validate_subagent_registry.py
python .\scripts\validate_agents_contract.py
python .\scripts\validate_research_pipeline.py
python .\scripts\validate_research_stack.py
```
