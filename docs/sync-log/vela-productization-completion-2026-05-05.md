# VELA Productization Completion Sync Log

Date: 2026-05-05

## Scope

This update continues the VELA productization branch after the contract-first refactor. It keeps VELA independent from HELM and from the private local research environment.

## Completed

- Moved legacy research-autopilot, harness, Zotero/Obsidian, and multi-agent routing assets into `archive/legacy-research-stack/`.
- Reduced the active `scripts/` surface to VELA runtime, validation, initialization, privacy, export, and contract modules.
- Replaced the public `skills/` surface with five VELA-specific Codex skills.
- Added project-scoped Codex profile templates under `package/.codex/profiles/`.
- Added `vela privacy scan`.
- Added `vela export public`.
- Added `vela.public_export.manifest.v1`.
- Moved VELA runtime tests to top-level `tests/`.

## Boundary Notes

- VELA still prepares prompts and validates files; it does not run hidden Codex execution.
- HELM remains a reader and optional dashboard, not a required dependency.
- Archived files are historical reference only and must not become runtime dependencies without a new schema, command, and test.
