# VELA HELM Sync Log - 2026-04-29

## Scope

- VELA repository: `Marcus-AI4SS/VELA`
- HELM public repository: `Marcus-AI4SS/HELM`
- HELM private/self-use repository verified separately: `Marcus-AI4SS/skills-app-own`

## Boundary Decision

VELA and HELM remain independent products. VELA is the portable workflow environment. HELM is the local research board. The two repositories share visual language, page structure, and import contracts, but neither product controls the other.

## Synchronized Items

- GitHub README now points to the counterpart repository and import interface.
- Pages homepage now explains the same two-brand model.
- Import contract added at `docs/imports/vela-helm-interface.md`.
- Machine-readable schema added at `docs/imports/vela-helm-interface.schema.json`.
- Shared direction names:
  - `vela.project.context.v1`: VELA to HELM project context import.
  - `helm.codex.handoff.v1`: HELM to VELA Codex handoff import.

## Local Note

The private HELM/self-use line is not the public Pages target. Public homepage and Pages work should land in `Marcus-AI4SS/HELM`, not `skills-app-own`.
