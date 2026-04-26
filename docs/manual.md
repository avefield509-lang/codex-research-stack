# VELA Manual

Updated: 2026-04-26

VELA is a portable research workflow environment for Codex. It is a file-based working method, not a desktop app and not an automation service.

## What VELA Is

VELA gives a research project a stable structure before work spreads across conversations, notes, files, references, datasets, and deliverables.

```text
my-research-project/
  materials/
  evidence/
  claims/
  methods/
  deliverables/
  handoffs/
```

Use those folders as working boundaries:

- `materials/`: collected sources, files, URLs, screenshots, datasets, notes.
- `evidence/`: verified material with source, access time, status, and rights or ethics notes.
- `claims/`: candidate claims and supported claims.
- `methods/`: assumptions, coding rules, analysis plans, reproducibility notes.
- `deliverables/`: reports, briefs, tables, figures, status notes.
- `handoffs/`: bounded tasks for Codex or collaborators.

## What VELA Is Not

- Not a chat interface.
- Not the HELM local board app.
- Not a black-box paper generator.
- Not a promise that unverified material is evidence.

## First Use

Clone or download the public repository:

```powershell
git clone REPOSITORY_URL vela
cd vela
```

`REPOSITORY_URL` is the URL of the VELA repository you are viewing. If the GitHub repository has been renamed, use the new URL shown in the browser.

Create your research project folder next to the VELA package, not inside a public copy of the repository.

## Evidence Discipline

A material becomes evidence only after the project records:

- source locator;
- access time;
- verification status;
- rights or ethics note;
- claim supported;
- explanation of how it supports that claim.

This distinction is the main reason VELA exists. It prevents a reading list, a screenshot folder, or a model summary from being treated as verified evidence.

## Codex Handoff Template

Use a small handoff before asking Codex to work:

```markdown
Task:
Relevant files:
Constraints:
Expected output:
Known gaps:
Review standard:
```

The handoff should be narrow enough that a reviewer can tell whether Codex stayed inside scope.

## Relationship To HELM

VELA and HELM are separate products:

| Product | Role | Can stand alone? |
| --- | --- | --- |
| VELA | Research workflow environment | Yes |
| HELM | Local research board | Yes |

HELM can later read VELA project state for status, evidence, deliverables, environment health, and handoff readiness. VELA remains usable without HELM.

## Repository Areas

- `docs/`: public documentation and Pages site.
- `docs/assets/brand/`: approved visual assets.
- `examples/`: small project examples.
- `scripts/`: setup and validation helpers.
- `skills/`: Codex skill, profile, schema, and template layer used by the workflow package.
