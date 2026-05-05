# Public Export

VELA can prepare a small public export package from a project without exposing the local project root.

Commands:

```powershell
vela privacy scan .
vela export public . --out public-export
```

`privacy scan` checks text files for secret-like assignments, credential-like paths, and local absolute paths. The public export command writes:

- `VELA-PUBLIC-EXPORT-MANIFEST.json`
- `EXPORT-QUALITY-REPORT.json`
- `REDACTION-MANIFEST.md`

The export includes public-facing project surfaces such as claims, evidence, methods, deliverables, handoffs, and truth files. It excludes `.vela/context.json`, raw outputs, private notes, credentials, and HELM handoff imports by default.

Human review is still required before publishing.
