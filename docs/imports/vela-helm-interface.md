# VELA and HELM Import Interface

VELA and HELM are separate products. VELA is the Versatile Experiment Lab & Automation package for Codex. HELM is the Hub for Evidence, Logs & Monitoring. The integration boundary is explicit local files, not app memory, telemetry, or hidden automation.

## Direction 1: VELA → HELM

HELM imports a VELA project context packet when a project exposes `vela.project.context.v1`.

Recommended path:

```text
project-root/.vela/context.json
```

Minimal packet:

```json
{
  "schema_version": "vela.project.context.v1",
  "producer": "VELA",
  "consumer": "HELM",
  "generated_at": "2026-04-30T00:00:00Z",
  "project": {
    "id": "sample-project",
    "name": "Sample Project",
    "title": "Sample Project",
    "root": ".",
    "stage": "research_design",
    "status": "initialized"
  },
  "paths": {
    "materials": "materials",
    "evidence": "evidence",
    "claims": "claims",
    "methods": "methods",
    "deliverables": "deliverables",
    "handoffs": "handoffs",
    "handoffs_helm": "handoffs/helm",
    "logs": "logs"
  },
  "truth_files": [
    { "name": "research-map.md", "path": "research-map.md", "exists": true },
    { "name": "findings-memory.md", "path": "findings-memory.md", "exists": true },
    { "name": "material-passport.yaml", "path": "material-passport.yaml", "exists": true },
    { "name": "evidence-ledger.yaml", "path": "evidence-ledger.yaml", "exists": true }
  ],
  "counts": {
    "materials": 0,
    "evidence": 0,
    "claims": 0,
    "deliverables": 0,
    "handoffs": 1
  },
  "status": {
    "phase": "research_design",
    "blocked": false,
    "last_updated": "2026-04-30T00:00:00Z"
  },
  "quality": {
    "blockers": [],
    "warnings": [],
    "validators": []
  },
  "helm": {
    "import_ready": true,
    "handoff_dir": "handoffs/helm",
    "handoff_policy": "explicit_user_export_only"
  }
}
```

HELM must treat missing fields as unknown, not as success.

## Direction 2: HELM → Codex / VELA

HELM prepares a bounded continuation task for Codex using `helm.codex.handoff.v1`. In the public HELM app this packet is copyable user-facing output, not an automatic project mutation.

There is no automatic write path. If a user explicitly saves or exports the packet for audit, use the reserved project path:

```text
project-root/handoffs/helm/2026-04-29-codex-handoff.json
```

Minimal packet:

```json
{
  "schema_version": "helm.codex.handoff.v1",
  "producer": "HELM",
  "consumer": "VELA",
  "generated_at": "2026-04-30T00:00:00Z",
  "project": { "id": "sample-project", "name": "Sample Project", "root": "." },
  "recommended_action": "Review the evidence index and identify unsupported claims.",
  "relevant_files": ["research-map.md", "evidence-ledger.yaml"],
  "constraints": ["Do not invent citations.", "Keep private paths out of deliverables."],
  "missing_inputs": ["No DOI verification has been run for new sources."],
  "validation_context": { "source": ".vela/context.json", "schema_version": "vela.project.context.v1" },
  "human_review_required": true,
  "text": "Copy this bounded task back into Codex."
}
```

VELA may store a manually saved or explicitly exported packet as a handoff record. It must not require `handoffs/helm/*.json` to exist for HELM import readiness, and it must not execute the task automatically.

## Shared Boundary Rules

- Either product can be used alone.
- VELA → HELM import is file-based through `.vela/context.json`.
- HELM → Codex / VELA handoff is copy-first. File storage is allowed only after explicit user save or export.
- The interface does not authorize cloud sync, background execution, hidden agent scheduling, or automatic citation claims.
- VELA owns workflow state. HELM owns local dashboard presentation and handoff preparation.

The machine-readable schema is [vela-helm-interface.schema.json](./vela-helm-interface.schema.json).
