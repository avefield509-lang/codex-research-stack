# Getting Started

## What this product is

Codex Research Stack is a local-first research workspace. Its job is to help a social science project move through:

1. project setup
2. source collection
3. analysis work
4. writing and submission preparation

You do **not** need to understand skills, MCP servers, or dispatch artifacts before you can start.

## Recommended first path

### 1. Clone the repository

```powershell
git clone https://github.com/avefield509-lang/codex-research-stack.git
cd codex-research-stack
```

### 2. Create a project

Cross-platform:

```powershell
python .\scripts\init_research_project.py --path ".\examples\demo-project" --route-hint "general-research"
```

Windows shortcut:

```powershell
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
```

### 3. Understand the future app boundary

If you want to understand how a future app should relate to this repository, read:

- [Repository and Future App](./app-relationship.md)

## What to look at first

If you are a general researcher, start with:

- `README.md`
- this page
- [Use Cases](./use-cases.md)
- [Integrations](./integrations.md)
- [Repository and Future App](./app-relationship.md)

If you are an advanced user, then continue to:

- [Architecture](./architecture.md)
- [Operator Guide](./operator-guide.md)

## Minimal validation

You only need this if you want to inspect the public stack itself:

```powershell
python .\scripts\validate_subagent_registry.py
python .\scripts\validate_agents_contract.py
python .\scripts\validate_research_pipeline.py
python .\scripts\validate_research_stack.py
```

These checks are useful, but they are **not** the main onboarding path.
