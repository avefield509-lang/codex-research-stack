# Integrations

The public product is local-first. Integrations are meant to support a research workspace, not to dominate it.

## Zotero

Zotero is the formal reference boundary.

In practice, this means:

- formal references should be verified before they are treated as ready for writing
- Zotero is where the formal library lives
- the rest of the workspace can still track notes, evidence, and project state without pretending every source is already a formal citation

## Obsidian

Obsidian is the long-lived knowledge layer.

In practice, this means:

- reusable notes and synthesis can move into Obsidian
- project runtime logs and gate files stay in the project itself
- formal references remain separate from project memory

## Browser-visible evidence

For platform and web cases, the public workspace stays conservative:

- prefer browser-visible material
- keep provenance explicit
- keep capture separate from later interpretation

This is why the product talks about evidence capture rather than generic “scraping”.

## Local environment tools

The desktop app can detect the local presence of:

- Python
- Git
- Codex Home
- Zotero
- Obsidian
- browser tooling

Missing tools should degrade gracefully. They are optional integrations, not hard blockers for basic project use.

## Advanced stack layer

Skills, MCP servers, validators, and orchestration rules still exist in the public repo, but they are treated as an advanced layer under `Settings` and `Architecture`, not as the first thing a general researcher must learn.
