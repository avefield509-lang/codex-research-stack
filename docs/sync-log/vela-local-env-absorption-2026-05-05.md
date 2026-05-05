# VELA Local Environment Absorption Log

Date: 2026-05-05

Source context reviewed:

- Local environment governance updates in `skills-environment-local`, especially the schema-driven environment contract work.
- `VELA_Codex_Workflow_Wrapper_Improvement_Plan.md`, which reframes VELA as a portable Codex workflow wrapper rather than an app or automation platform.

Accepted into VELA:

- Added `package/.vela/initializer-manifest.json` as the declarative source for project directories, starter files, and default Codex project agents.
- Added `scripts/vela_initializer.py` to validate and materialize the initializer manifest with path guards.
- Reworked `scripts/init_research_project.py` into a thin orchestration wrapper instead of hard-coding project files and agents in Python.
- Added initializer and validation schemas under `schemas/`.
- Extended `vela doctor` to report initializer manifest health.
- Added `project.route_id` to `vela.project.context.v1` so HELM can read the selected workflow route from `.vela/context.json`.
- Added `VELA_ROOT` as the preferred local root override while keeping the old environment variable as compatibility fallback.
- Clarified public wording: VELA is `Versioned Evidence Lifecycle Architecture`, a Codex workflow boundary, not an automation app.

Not absorbed in this pass:

- App-specific agents and QA/release roles from private HELM or older desktop work.
- Local-only harness orchestration that would make VELA look like a hidden agent loop.
- Private machine paths, app output folders, local account traces, and C-drive backup assumptions.
- Full privacy scan, public export, evidence/claim validators, and dedicated VELA skills. These remain planned productization work.

Current code shape:

- `package/` is the starter package.
- `package/.vela/initializer-manifest.json` is the initializer source of truth.
- `scripts/vela.py` is the user-facing CLI.
- `scripts/init_research_project.py` handles Git setup, manifest materialization, starter package copy, Codex trust registration, local registry, and context export.
- `scripts/vela_initializer.py` owns schema-driven bootstrap.
- `scripts/vela_contract.py` owns `.vela/context.json` and validation.
- `schemas/` owns public machine contracts.
- `skills/` remains an optional Codex skill/profile layer, not a required app runtime.

Follow-up structure risks:

- `scripts/` still contains inherited local-environment scripts that are useful but broad. Later releases should split public core commands from optional advanced integrations.
- `docs/` currently keeps Markdown and static HTML side by side. This is workable for now, but a documentation build step would reduce drift.
- The public MVP should prioritize bounded handoffs, validation, privacy scan, and examples before adding deeper automation.
