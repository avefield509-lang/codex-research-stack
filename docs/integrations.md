# Integrations

## Zotero

Zotero is treated as the formal reference boundary.

The public stack is opinionated about one thing: formal references should enter the chain only after verification logic, not as unchecked text copied into a draft.

In practice, this makes Zotero the place for:

- reference boundary
- collection structure
- citation integrity handoff

## Obsidian

Obsidian is treated as the knowledge handoff layer.

This means the stack separates:

- formal reference management
- project runtime artifacts
- reusable knowledge notes and synthesis

The public repo does not try to collapse those into one tool.

## Social Platform Evidence

The social evidence layer is intentionally conservative.

Its design bias is:

- prefer browser-visible evidence
- keep capture separate from interpretation
- make evidence artifacts inspectable later

That is why this repo emphasizes platform evidence workflows instead of generic “web scraping” language.

## Plugin Layer

`research-autopilot` is the visitor-facing plugin anchor in this repo.

The plugin is the public surface because it makes the system easier to understand:

- there is a visible entrypoint
- there is a visible route explanation layer
- there is a visible upgrade path into project squads

## Project Scripts

The public scripts are intentionally kept portable.

They are written to prefer:

- repo-relative paths
- environment variables
- public validators

instead of machine-specific assumptions.
