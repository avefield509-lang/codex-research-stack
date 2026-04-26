<div align="center">
  <img src="./docs/assets/brand/vela-workflow-mark.png" alt="VELA layered sail mark" width="132">
  <h1>VELA</h1>
  <p><strong>Workflow Environment Package for Codex-based research</strong></p>
  <p><em>Versioned Evidence Lifecycle Architecture</em></p>
  <p>
    <a href="./README.zh-CN.md">中文</a>
    · <a href="https://marcus-ai4ss.github.io/codex-research-stack/">Pages</a>
    · <a href="./docs/getting-started.md">Getting started</a>
    · <a href="./docs/workflow-core.md">Workflow core</a>
    · <a href="./docs/evidence-lifecycle.md">Evidence lifecycle</a>
    · <a href="./docs/quality-checks.md">Quality checks</a>
  </p>
</div>

VELA is a portable research workflow environment you can place inside your own Codex workspace. It gives a research project a stable operating layer: materials, evidence, claims, method notes, deliverables, and Codex handoffs remain separate, readable, and reviewable.

It is not a desktop app. It is not a chat interface. It is not a black-box paper generator. VELA is the workflow package; HELM is the optional local research board that can later read the same project state.

## Start In Five Minutes

```powershell
git clone REPOSITORY_URL vela
cd vela
```

Then create your research project folder next to it:

```text
my-research-project/
  materials/
  evidence/
  claims/
  methods/
  deliverables/
  handoffs/
```

Use `REPOSITORY_URL` as the URL of the public VELA repository you are viewing.

## What VELA Helps You Do

| Need | What VELA Gives You |
| --- | --- |
| Start a project without losing structure | A clear place for question, scope, sources, and expected deliverables |
| Keep evidence honest | A lifecycle that separates collected material from verified evidence |
| Work with Codex safely | Handoff prompts that name the task, files, constraints, expected output, and known gaps |
| Prepare shareable outputs | Checks that reveal unsupported claims and private material before a deliverable leaves the project |

## The Workflow

| Layer | Keep Here | Do Not Confuse It With |
| --- | --- | --- |
| Materials | DOI records, URLs, files, datasets, notes, captures | Evidence |
| Evidence | Verified materials with source, access time, status, and ethics or rights notes | A broad reading list |
| Claims | Candidate and supported statements | Final findings |
| Methods | Assumptions, coding rules, analysis plans, reproducibility notes | Results |
| Deliverables | Reports, briefs, figures, tables, status notes | Raw project state |
| Handoffs | Bounded tasks for Codex or collaborators | Whole-project delegation |

## A Good Codex Handoff

```markdown
Task:
Relevant files:
Constraints:
Expected output:
Known gaps:
Review standard:
```

The handoff is intentionally small. Codex should receive enough context to do the task, not an unbounded invitation to rewrite the project.

## VELA And HELM

| Product | Role | Can Stand Alone? |
| --- | --- | --- |
| **VELA** | Research workflow environment for Codex | Yes |
| **HELM** | Local research board for status, evidence, deliverables, environment health, and handoffs | Yes |

Use VELA by itself when you want a portable workflow. Add HELM when you want a visual local board over the same project state.

## Read Next

- [Getting started](./docs/getting-started.md)
- [Workflow core](./docs/workflow-core.md)
- [Evidence lifecycle](./docs/evidence-lifecycle.md)
- [Quality checks](./docs/quality-checks.md)
- [Use cases](./docs/use-cases.md)
- [Integrations](./docs/integrations.md)
- [FAQ](./docs/faq.md)

## Repository Layout

| Path | Purpose |
| --- | --- |
| `docs/` | Public documentation, GitHub Pages, and approved visual assets |
| `examples/` | Minimal project and quick demo for inspection |
| `scripts/` | Setup, validation, and local maintenance helpers |
| `skills/` | Codex skill, profile, schema, and template layer |
