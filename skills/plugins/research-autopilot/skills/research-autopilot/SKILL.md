---
name: research-autopilot
description: Use when a research task should be routed before execution across routes, profiles, skills, and project-type multi-agent planning.
---

# Research Autopilot

Use this skill as the default entrypoint for research work in Codex Research Stack.

## What It Does

- classify the task before execution
- pick a route instead of jumping straight into tools
- decide whether the task remains single-agent or upgrades to project-type multi-agent planning
- explain the decision before work starts

## Required References

Read these repository-local assets first:

- `skills/catalog/routing_table.json`
- `skills/catalog/conflict_matrix.json`
- `skills/catalog/project_scope_rules.json`
- `skills/catalog/agent_execution_modes.json`
- `skills/catalog/subagent_registry.json`
- `skills/catalog/reviewer_allowlist.json`
- `skills/catalog/settings.toml`
- `skills/profiles/`

## Core Rules

1. Do not invent citations.
2. Formal references must be verified before they enter the formal writing chain.
3. Project-type tasks should be reasoned about before execution, not after.
4. If the task becomes multi-agent, hand orchestration to `research-team-orchestrator`.
5. For evidence-heavy platform work, keep browser-visible evidence boundaries explicit.

## Output Requirement

Before execution, provide a route explanation card that includes:

- task type
- selected route
- selected profile
- selected skills / MCP / plugin layer
- why this route was selected
- why nearby candidates were excluded
- whether multi-agent planning is required
- what happens next

## Project Tasks

If the selected route becomes a project-type run:

- create a clarification card
- decide the project scope class
- decide whether reviewer mapping is mandatory
- invoke `research-team-orchestrator`

This skill explains the decision.  
It does not replace the actual dispatch layer.
