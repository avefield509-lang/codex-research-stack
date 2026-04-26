# Architecture

VELA is a local-first workflow environment. Its architecture is a portable project state, an evidence lifecycle, and bounded Codex handoff context. HELM may read that state, but VELA should not require HELM to exist.

## User-Facing Model

The public workflow is organized around:

- project question and scope;
- materials;
- evidence;
- candidate and supported claims;
- method notes and artifacts;
- deliverables;
- environment checks;
- Codex handoffs.

## Local Storage Model

Project files should remain portable and inspectable. Public examples must use placeholders such as `<PROJECT_ROOT>` and `<CODEX_HOME>` rather than private machine paths.

## Safety Boundary

VELA should not hide autonomous execution behind product language. Codex receives bounded tasks and scoped context. Generated suggestions require review before they change project facts.
