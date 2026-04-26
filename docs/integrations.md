# Integrations

VELA treats integrations as optional enhancements. The base workflow environment should still support project setup, evidence tracking, method notes, deliverable preparation, and Codex handoff structure when optional tools are absent.

## Optional Layers

- **Codex:** executes bounded tasks from scoped handoff context.
- **HELM:** reads project state, evidence status, deliverables, environment health, and handoff readiness.
- **Python:** enables richer local checks, data processing, and reproducibility scripts.
- **Zotero:** supports formal reference management.
- **Obsidian:** supports long-lived research notes.
- **OpenAI-compatible providers:** may assist with drafts or suggestions only when configured by the user.

## Boundary

No integration should silently turn a material into evidence, mark a claim as supported, or treat an unverified draft as a project fact. Missing optional tools should be visible as a gap, not hidden as a completed step.
