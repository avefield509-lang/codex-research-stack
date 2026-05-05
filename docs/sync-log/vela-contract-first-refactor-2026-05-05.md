# VELA Contract-First Refactor Sync Log

Date: 2026-05-05

## Scope

This VELA branch implements the public workflow wrapper refactor only. It does not modify HELM, the local private research environment, or any old C drive backup repository.

## Implemented

- Added `scripts/vela_schema.py` as the shared JSON Schema and JSON/YAML parsing layer.
- Added `scripts/vela_handoff.py` so `vela.py` stays a thin CLI adapter.
- Added `schemas/vela.validation.report.v1.schema.json`.
- Strengthened `schemas/vela.codex.handoff.v1.schema.json`.
- Changed handoff linting from marker-string checks to schema validation.
- Changed project validation and initializer manifest validation to emit `vela.validation.report.v1`.
- Kept `.vela/context.json` as the VELA -> HELM machine interface with schema `vela.project.context.v1`.
- Added `requirements.txt` and updated install shims to record the Python interpreter used at install time.

## Boundary Notes

- VELA remains a portable Codex workflow wrapper, not a desktop app.
- HELM remains optional and should read VELA state rather than own or silently mutate it.
- The local research environment may continue to incubate private harness ideas, but public VELA defaults must not depend on private local paths.

## Verification

- `python -m py_compile scripts\vela.py scripts\vela_schema.py scripts\vela_handoff.py scripts\vela_contract.py scripts\vela_initializer.py scripts\init_research_project.py`
- `python -m unittest discover -s skills\tests`
- `python scripts\vela.py doctor`
- clean temp project smoke: `init -> validate --repair-context -> handoff new -> handoff lint -> handoff render`
- install smoke with temporary `VELA_HOME`
