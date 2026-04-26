# Getting Started

VELA is easiest to understand as a workflow environment package. Start with a real project folder, define the research question, collect materials, upgrade only verified materials into evidence, then hand scoped context to Codex when a task needs agentic work.

## 1. Create a project folder

Choose a portable project location. Avoid machine-specific paths in shared examples. Use placeholders such as `<PROJECT_ROOT>` when writing public documentation or handoff notes.

## 2. Initialize the workflow shape

A VELA project should keep these layers distinct:

- materials;
- evidence;
- candidate claims;
- method notes and artifacts;
- deliverables;
- Codex handoff context.

Materials are easy to capture. Evidence is stricter: source, access time, verification status, and rights or ethics notes must be visible before a material supports a claim.

## 3. Work through the lifecycle

Use the VELA lifecycle as the operating loop:

1. Collect sources and project materials.
2. Analyze what each material can and cannot support.
3. Validate evidence status, method assumptions, and claim bindings.
4. Report only what the project state can justify.

## 4. Use Codex deliberately

Send Codex bounded tasks: clean a dataset, draft a method note, inspect evidence gaps, prepare a reproducibility checklist, or generate a handoff summary. Keep the prompt tied to project files and expected outputs.

## 5. Add HELM only when needed

HELM is optional. Use it when you want a local board for status, evidence, deliverables, environment health, and Codex handoffs. VELA does not require HELM to run.
