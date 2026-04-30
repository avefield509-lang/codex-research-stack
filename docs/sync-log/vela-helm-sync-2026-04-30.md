# VELA / HELM Sync Log - 2026-04-30

## Scope

- VELA productization as the Versatile Experiment Lab & Automation package for Codex.
- HELM import readiness through `.vela/context.json`.

## VELA Changes

- Added `package/` starter package for `vela init`.
- Added `scripts/vela.py` CLI and install scripts.
- Added `.vela/context.json` generation with `vela.project.context.v1`.
- Added handoff and context schemas plus `examples/00-minimal-wrapper`.

## HELM Contract

- HELM should read `.vela/context.json` first.
- Legacy truth files remain a fallback path.
- HELM prepares copyable `helm.codex.handoff.v1` packets for Codex.
- HELM must not silently write `handoffs/helm/*.json`.
- If a HELM handoff packet is stored in `handoffs/helm/`, it must come from an explicit user save or export action.
