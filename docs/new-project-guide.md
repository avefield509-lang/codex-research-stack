# New Project Guide

This guide answers one practical question:

- if you want to start a new research project with this stack, what should you do first?

It is intentionally procedural.

## 1. The shortest safe sequence

The stable order is:

1. create a project folder
2. initialize the project scaffold
3. let `research-autopilot` explain the route first
4. let `research-team-orchestrator` plan the project only if it becomes project-type work
5. inspect project-state and gate files as the run grows

## 2. Create a project folder

Choose a project path such as:

- `<PROJECT_ROOT>`

For a quick demo, you can also point the script at a path inside the repo.

## 3. Initialize the project scaffold

Run:

```powershell
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path "<PROJECT_ROOT>"
```

This scaffold creates:

- a Git repository
- `README.md`
- `.gitignore`
- project-level `AGENTS.md`
- project memory files
- canonical agent and gate directories

## 4. Check the project skeleton

The most important files to inspect first are:

- `AGENTS.md`
- `research-map.md`
- `findings-memory.md`
- `logs/project-state/current.json`

If these are present, the scaffold is in place.

## 5. Start with routing, not execution

The first request to Codex should ask for explanation before execution.

A good pattern is:

```text
@research-autopilot This is a new research project.
The topic is: ...
The question is: ...
The materials or data are: ...
The expected outputs are: ...
Explain the route first, then decide whether this should become project-type multi-agent work.
```

The point is to make route and scope visible before the system expands.

## 6. What happens next

### If the task stays small

You should see a route explanation card.

### If the task becomes project-type work

You should see:

1. a clarification layer
2. an agent dispatch layer

That means the stack is turning the project into a structured runtime instead of a long chat thread.

## 7. When multi-agent planning usually appears

Multi-agent planning is most likely for:

- literature synthesis projects
- computational social science projects
- platform evidence or case-dataset projects
- writing or submission-package workflows with multiple deliverables

It is less likely for:

- one-off environment fixes
- single-paper review tasks
- very small export-only tasks

## 8. Track the current state

If the project is already moving and you want to know where it is blocked, inspect:

- `logs/project-state/current.json`

The most useful fields are usually:

- `current_owner_agent_id`
- `current_owner_display_name`
- `pipeline_stage`
- `next_quality_gates`
- `blockers`
- `milestones`

## 9. Run a planning script directly

If you want to test the public project planner outside the Codex UI, run:

```powershell
python .\scripts\plan_research_team.py --project-root "<PROJECT_ROOT>" --route-id "literature-review" --target-item-count 20 --work-unit discovery --work-unit writing --deliverable-type literature_synthesis --sync-target zotero --sync-target obsidian
```

This is a public example command, not a hidden internal shortcut.

## 10. Validate before you trust the stack

Run the validators:

```powershell
python .\scripts\validate_subagent_registry.py
python .\scripts\validate_agents_contract.py
python .\scripts\validate_research_pipeline.py
python .\scripts\validate_research_stack.py
```

That keeps the public repo legible and prevents silent drift.
