# Privacy Boundaries

This public repository is intentionally filtered before publication.

## Excluded By Default

- private SSH keys and credential material
- cloud server logs and operator notes
- Codex local trust state
- local runtime blobs, caches, and outputs
- personal application documents
- user-specific repair scripts for one machine

## Redaction Rules

- replace machine-specific absolute paths with portable placeholders
- replace local usernames and private repo traces with public-facing metadata
- remove direct host, tunnel, and key references
- keep research rules and workflow structure, but not private operational details

## Public Contract

What stays public:

- routing logic
- schemas
- orchestrator and validator logic
- public-facing plugin metadata
- docs, examples, and templates

What does not stay public:

- secrets
- operator-only infra traces
- private application materials
- local-only configuration state
