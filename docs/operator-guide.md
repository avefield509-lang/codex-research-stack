# Operator Guide

This guide is the public, sanitized counterpart of the internal operating manual.

It answers one question:

- what this stack is
- what you should expect to see first
- what counts as real multi-agent execution
- which files matter when a project is running

## 1. Start from `research-autopilot`

The default entrypoint is still `research-autopilot`.

You should not start by guessing which individual skill to call.
The stack is designed to:

1. classify the task
2. choose a route
3. choose helper skills, profile, and gates
4. decide whether the work should stay single-run or upgrade into project-type orchestration

## 2. The public control chain

The visible control chain has three layers:

- `research-autopilot`
  - the only top-level router
  - chooses route, helper skills, and whether project planning is required
- `research-team-orchestrator`
  - only enters when the task becomes project-type work
  - builds clarification inputs, dispatch artifacts, reviewer mappings, and project-state traces
- execution skills
  - perform citation verification, platform evidence capture, analysis, writing, export, and sync tasks

## 3. What you normally see first

### Non-project tasks

You should first see a route explanation, not blind execution.

That explanation normally includes:

- task type
- route
- selected skills or MCP tools
- why they were selected
- which alternatives were rejected
- what happens next

### Project-type tasks

Project-type tasks should produce two visible layers before work expands:

1. a clarification card
2. an agent dispatch card

The point is simple: project work should become inspectable before it becomes large.

## 4. What counts as real multi-agent execution

This public repo does not treat role-play as multi-agent work.

A run only counts as real multi-agent execution when it has:

- distinct `agent_id` values
- separate context packets
- separate output directories
- explicit reviewer mapping
- target-specific gate files
- handoff and project-state traces

If the system only shows multiple perspectives inside one answer, that is not the same thing.

## 5. Canonical project artifacts

When you initialize a project, the scaffold is designed to make the research process inspectable.

The most important artifacts are:

- `AGENTS.md`
- `research-map.md`
- `findings-memory.md`
- `material-passport.yaml`
- `evidence-ledger.yaml`
- `.codex/agents/`
- `.codex/dispatch/`
- `.codex/context-packets/`
- `outputs/agent-runs/`
- `logs/agent-handoffs/`
- `logs/quality-gates/`
- `logs/project-state/`

These files separate project rules, project memory, runtime artifacts, and gate decisions.

## 6. Gates are part of the system, not decoration

The public stack includes an explicit research pipeline layer.

Typical checks include:

- citation integrity
- data provenance
- writing quality
- result validity
- reproducibility
- final package approval

The system is designed so that a project can be blocked by weak evidence or missing checks.

That is intentional.

## 7. The most useful files during live project work

If you only want to inspect a running project, start with these:

1. `AGENTS.md`
2. `research-map.md`
3. `findings-memory.md`
4. `material-passport.yaml`
5. `logs/project-state/current.json`
6. `logs/quality-gates/pipeline-status.json`

Those six files usually tell you:

- what the project is trying to do
- what is already known
- what stage the project is in
- who currently owns the next step
- which gates still block progress

## 8. Where to go next

- If you want the shortest path to a real project, read [New Project Guide](./new-project-guide.md).
- If you want the underlying structure, read [Architecture](./architecture.md).
