# PRD v0.6 Brand Transition

## Opportunity Brief

v0.6 moves the public story from an app-centered research cockpit to two independent but related products:

- **VELA:** portable research workflow environment for Codex.
- **HELM:** optional local research board for project state, evidence, deliverables, environment health, and handoffs.

The product risk is positioning. A new user must understand that VELA can be installed into their own Codex environment without downloading HELM, while HELM remains a useful companion rather than a controller.

## Target User

- Researcher who wants a reproducible local workflow for materials, evidence, methods, claims, and deliverables.
- Codex user who needs structured project context instead of loose chat history.
- Research operator who wants a local board later, without making the board mandatory.

## Product Promise

Within a first evaluation session, a user should understand:

1. what VELA is;
2. why it is independent from HELM;
3. how materials differ from evidence;
4. how Codex handoff context is scoped;
5. how HELM can read project state when installed;
6. where public examples and visual assets live.

## Core Concepts

- **Workflow environment package:** VELA is the primary public workflow artifact.
- **Evidence lifecycle:** materials, evidence, claims, methods, and deliverables remain distinct.
- **Codex handoff:** scoped context transfer, not autonomous project execution.
- **Optional local board:** HELM is useful for visibility but not required.
- **Shared visual language:** pale blue and white surfaces, layered sail, evidence trace, navigation rings, and calm iOS-style hierarchy.

## Functional Requirements

- Public README title uses VELA.
- GitHub Pages home uses VELA and the workflow subtitle.
- HELM appears only as an independent optional companion.
- Public copy avoids app-only positioning.
- Public copy avoids older automation labels as current product brands.
- Brand assets are stored under `docs/assets/brand/`.
- Generated images are treated as visual references; final text is written in HTML, Markdown, or app code.

## Non-Goals

- Company-level trademark clearance.
- Domain purchase.
- Full app implementation changes.
- Removing historical internal identifiers before compatibility review.

## Acceptance Matrix

| Area | Acceptance |
| --- | --- |
| README | Public name is VELA and the app-only story is removed. |
| Pages | Home, Chinese home, getting started, installation, integrations, use cases, architecture, and operator pages use VELA language. |
| Boundary | VELA can be understood without HELM. |
| HELM | HELM is optional and independent. |
| Visuals | Pages reference the pale blue and white VELA/HELM boards. |
| Scan | Current public docs do not use older stack or automation names as product brands. |
