---
name: research-team-orchestrator
description: Use when a routed research task has entered project-type multi-agent planning and must be turned into a dispatch artifact, review mapping, and canonical project state.
---

# Research Team Orchestrator

This skill takes an already-selected research route and turns it into a project-level orchestration result.

## What It Does

- turns clarification data into a dispatch plan
- selects producer and reviewer roles
- creates target-specific review mappings
- writes canonical paths for dispatch, context packets, handoff logs, gate logs, and project state

## Required References

- `skills/catalog/project_scope_rules.json`
- `skills/catalog/agent_execution_modes.json`
- `skills/catalog/subagent_registry.json`
- `skills/catalog/research_team_playbooks.json`
- `skills/catalog/reviewer_allowlist.json`
- `skills/schemas/agent_dispatch_card.schema.json`
- `skills/schemas/project_agent_definition.schema.json`
- `scripts/plan_research_team.py`
- `scripts/bootstrap_agent_dispatch.py`

## Rules

1. `force_single_agent` does not remove a mandatory reviewer.
2. Mandatory-review deliverables must have target-specific review mapping.
3. Reviewers stay read-constrained and do not modify primary artifacts directly.
4. All paths must land in canonical project locations.
5. Hard chains such as citation verification and writing reference capture must not be bypassed.

## Output

Produce:

- a clarification card
- selected producers
- selected reviewers
- route-aligned squad / playbook
- review mapping
- dispatch artifact location
- project state preview
- validation result
