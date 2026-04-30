# VELA / HELM Sync Log - 2026-04-30

## Scope

- VELA productization as a Codex workflow wrapper package.
- HELM import readiness through `.vela/context.json`.

## VELA Changes

- Added `package/` starter package for `vela init`.
- Added `scripts/vela.py` CLI and install scripts.
- Added `.vela/context.json` generation with `vela.project.context.v1`.
- Added handoff and context schemas plus `examples/00-minimal-wrapper`.

## HELM Contract

- HELM should read `.vela/context.json` first.
- Legacy truth files remain a fallback path.
- HELM handoffs should be written under `handoffs/helm/` as `helm.codex.handoff.v1`.
