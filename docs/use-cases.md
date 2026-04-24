# Use Cases

## 1. Literature Review With Formal Citation Boundaries

Typical input:

> Review a topic, verify the references, organize them into a usable synthesis, and prepare the project for later writing.

What the stack does:

- routes into `literature-review`
- upgrades into a literature-focused squad once the task becomes project-like
- forces DOI-aware citation handling before formal use
- keeps the synthesis visible as project artifacts instead of only chat output

Why this is better than a generic agent:

- the route is explained before retrieval starts
- the synthesis can be reviewed as a project artifact
- the stack is explicit about where Zotero and writing enter the chain

## 2. Computational Social Science Project

Typical input:

> Start a new project that combines literature, platform evidence, analysis, writing, and reproducibility.

What the stack does:

- routes into `computational-social-science`
- initializes a project scaffold with `AGENTS.md`, memory files, and gate logs
- upgrades into a CSS squad instead of trying to solve everything in one thread
- keeps project state, current owner, blockers, milestones, and next gates visible

Why this matters:

- project work becomes inspectable
- the system knows the difference between routing, execution, review, and packaging
- the final output is closer to a research package than to a long answer

## 3. Social Platform Evidence

Typical input:

> Read a platform page, extract only browser-visible evidence, and package it for later analysis.

What the stack does:

- routes into `social-platform-case`
- prefers browser-visible evidence rules
- keeps platform capture separate from later synthesis claims
- can upgrade into a platform evidence squad when the task becomes a case dataset or comment-analysis report

Why this matters:

- the stack does not silently imply hidden or unverifiable evidence
- evidence capture and later interpretation are separated

## 4. Writing Before Export

Typical input:

> Prepare a draft or submission package and make sure references and writing quality are under control before export.

What the stack does:

- routes into `writing-export`
- only upgrades when the task becomes a real draft / revision / submission workflow
- forces reference capture before final export
- checks writing quality through explicit report files and gates

Why this matters:

- the repo makes writing quality a visible artifact, not a vague style promise
- export is downstream of capture and review, not a shortcut around them
