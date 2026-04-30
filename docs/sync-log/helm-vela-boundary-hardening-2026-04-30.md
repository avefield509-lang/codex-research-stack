# HELM / VELA Boundary Hardening Follow-up - 2026-04-30

## Source

- Public HELM main includes `025d089 Harden HELM VELA context boundary`.
- Public HELM PR #7 superseded the earlier write-back behavior.
- The old self-use HELM draft PR was closed unmerged because it mixed historical private app payload with the smaller VELA context idea.

## Accepted Boundary

- VELA owns workflow state and writes `project-root/.vela/context.json`.
- HELM reads `vela.project.context.v1` as its preferred import surface.
- HELM prepares `helm.codex.handoff.v1` as copyable output for the user and Codex.
- HELM does not silently create `project-root/handoffs/helm/*.json`.
- VELA should only store HELM-prepared packets after an explicit user save or export action.

## VELA Follow-up

- Public docs now point to `Marcus-AI4SS/VELA` and `https://marcus-ai4ss.github.io/VELA/`.
- The import contract now marks HELM handoff storage as explicit-user-export-only.
- `.vela/context.json` now advertises `helm.handoff_policy = "explicit_user_export_only"` while preserving `helm.handoff_dir` as a reserved path.
