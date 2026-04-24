# AGENTS

This repository is the public `skills仓库管理` workspace.

## Scope

- Manage the public environment package and GitHub-facing research workspace.
- Work only inside this repository root.
- Main areas: public docs, public scripts, public skills, examples, Pages assets.
- Do not use the old monolithic `skills` directory as this thread's working root.

## Repository Map

- `skills-environment-local`: private local environment source of truth for personal runtime rules, skills, MCP profiles, Python setup, scaffolds, validators, and local manuals.
- `skills-environment-release`: this repository; public environment package, public docs, examples, Pages assets, and portable release scripts.
- `skills-app-own`: private app workspace for personal/friends desktop UI, packaging, launchers, and local UX.
- `skills-app-github`: public app workspace for the externally shared app.

The app repositories should consume this environment through explicit copy, export, or snapshot steps. They should not silently become a second source of truth for environment rules.

## Cross-Repo Boundary

- You may read, call, compare against, or copy content from `skills-environment-local`, `skills-app-own`, and `skills-app-github`.
- Do not modify any of those three repositories unless the user has explicitly approved that cross-repo change in the current thread.
- Do not add private paths, personal notes, machine-only fixes, credentials, or local-only outputs here.
- If syncing content from another repository into this one, state the source, target, reason, and file set before editing.

## Thread Rule

- The `skills仓库管理` thread should only work in this repository.
- Cross-repo reading and copying are allowed.
- Cross-repo writes require explicit user approval first; without that approval, stop and switch to the corresponding repository thread instead of editing across boundaries.
