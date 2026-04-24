# Repository and Future App

## One-sentence definition

This repository is the public source of truth for the research workflow.
The future app should be a user interface built on top of that source, not a second source of truth.

## What this repository owns

This repository should continue to own:

- public docs and GitHub Pages
- workflow definitions
- route and gate rules
- schemas and templates
- validation scripts
- public examples
- public visual assets

In practice, these are the reusable assets under:

- `skills/catalog/`
- `skills/profiles/`
- `skills/schemas/`
- `skills/templates/`
- `scripts/init_research_project.py`
- `scripts/plan_research_team.py`
- `scripts/validate_*.py`

## What the future app should own

The future app should own the interaction layer, for example:

- onboarding screens
- project dashboard views
- task-entry forms
- route explanation views
- project state and gate visualization
- environment status panels
- guided project creation

That means the app is responsible for a smoother daily experience, not for redefining the workflow itself.

## What the app should read, not redefine

The future app should read this repository's public assets instead of silently duplicating them.

At minimum, it should treat these as shared contract inputs:

- catalog files
- schemas
- templates
- examples
- public validators

If the app needs a simplified UI model, that model should be derived from these assets, not invented as a separate rule system.

## What the app should not do

The future app should not:

- become a second source of truth for route logic
- hard-code gate rules that drift away from the repository
- silently fork the schemas
- treat UI state as the canonical research state
- make the repository optional for understanding how the workflow actually works

## Practical relationship

The clean relationship is:

- this repository = workflow system, contracts, docs, examples, public assets
- future app = guided interface, dashboard, and visualization layer

The repository must remain usable without the app.
The app can improve the experience, but it should not become the only way to understand or inspect the stack.

## Page linkage

The public website should eventually work like this:

- repository pages explain what the stack is, how it works, and how to inspect it
- app pages explain what the interface adds for daily use
- both sides link to each other clearly

The repository should link to the future app as:

- an optional interface layer
- a faster way to use the stack
- not a replacement for the public contracts

The future app should link back to the repository as:

- the source of workflow rules
- the place for advanced documentation
- the place for examples and validators

## Release relationship

When the app becomes real, the safest release model is:

- app releases declare which repository contract version they are compatible with
- repository releases remain independently inspectable
- app UI copy does not promise behavior that the repository contracts do not support

## Current status

Today, this repository already exists as a standalone public research stack.
The future app is still a planned interface layer.

So the correct relationship right now is:

- repository first
- app later
- app built on top of the repository, not beside it as a competing system
