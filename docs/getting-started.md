# Getting Started

Use VELA when you want Codex to work from a bounded project state rather than loose conversation history. VELA is a workflow wrapper package around Codex, not a desktop app or a hidden agent loop.

## 1. Download VELA

Clone or download the repository you are viewing:

```powershell
git clone https://github.com/Marcus-AI4SS/VELA.git vela
cd vela
.\install.ps1
```

On macOS or Linux:

```bash
git clone https://github.com/Marcus-AI4SS/VELA.git vela
cd vela
sh ./install.sh
```

## 2. Initialize A Project

```powershell
.\vela.ps1 init ..\my-research-project --skip-codex-trust
```

This creates:

- `materials/`
- `evidence/`
- `claims/`
- `methods/`
- `deliverables/`
- `handoffs/`
- `logs/`
- `.codex/`
- `.vela/context.json`

Keep private data in your project folder, not in the VELA repository.

## 3. Capture Materials

Save DOI records, URLs, files, datasets, platform captures, policy documents, notes, or screenshots as materials. A material is only a source clue at this point.

## 4. Upgrade Evidence Carefully

A material becomes evidence only when the project records:

- source locator;
- access time;
- verification status;
- rights or ethics note;
- the claim it supports;
- how it supports that claim.

## 5. Ask Codex For Bounded Work

Before asking Codex to work, create a handoff:

```powershell
..\vela\vela.ps1 handoff new --project .
..\vela\vela.ps1 handoff lint handoffs\H001.yaml
..\vela\vela.ps1 handoff render handoffs\H001.yaml --out handoffs\H001.prompt.md
```

This keeps Codex work reviewable and prevents a broad prompt from silently changing the research record.

## 6. Validate And Refresh HELM Context

```powershell
..\vela\vela.ps1 validate . --repair-context
```

HELM reads `.vela/context.json` when you want a local board over the same project state.

## 7. Add HELM Later If Useful

HELM is optional. Use it when you want a local board for project status, evidence, deliverables, environment health, and Codex handoffs.
