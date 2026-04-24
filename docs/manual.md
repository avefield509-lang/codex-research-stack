# Codex Research Stack Manual

Updated: 2026-04-24

This is the single public manual for the repository.  
If you are new here and want to understand what this stack is, how to begin, and what to inspect during a real project, start with this page.

---

## Table of Contents

1. [What this manual covers](#scope)
2. [In three sentences](#what-this-repository-is)
3. [Terms you do not need to worry about at first](#plain-language-glossary)
4. [Who this is for](#who-it-is-for)
5. [What the public stack is actually made of](#components)
6. [First use: only do these three things](#getting-started)
7. [If you do not want to deal with commands yet](#no-command)
8. [How a new project begins](#starting-a-project)
9. [Why a project turns into multi-agent work](#what-counts-as-real-multi-agent-execution)
10. [What to look at during a live project](#during-a-live-project)
11. [The files that matter most](#the-files-that-matter-most)
12. [Use cases](#use-cases)
13. [Integrations](#integrations)
14. [Repository and future app](#repository-and-future-app)
15. [Public boundary](#public-boundary)
16. [If something goes wrong, where to look first](#troubleshooting)
17. [Roadmap](#roadmap)

---

<a id="scope"></a>
## 1. What this manual covers

This manual only explains the public repository:

- what it is
- who it is for
- how to begin
- what to inspect during a live project
- how the future app should relate to it

It does **not** try to explain:

- a private local workstation
- private operations or environment details
- the internal implementation of the future app

So what you are reading here is a **public, reusable user manual**, not a full dump of someone's private setup.

---

<a id="what-this-repository-is"></a>
## 2. In three sentences

First, this repository is not the chatbot itself. It is the workflow layer around research work in Codex.

Second, its goal is not to win by adding more tools. Its goal is to make research projects easier to start, inspect, and continue.

Third, it focuses on the part where research work usually becomes messy:

- how a task should begin
- how a project should stay readable as it grows
- when weak work should be stopped by checks
- how references, notes, runtime traces, and outputs should stay separated

You can think of it as a research workbench:

- you say what you are trying to do
- the system explains how the work should begin
- if the project becomes larger, it turns the process into something you can inspect later

---

<a id="plain-language-glossary"></a>
## 3. Terms you do not need to worry about at first

Many first-time readers get pushed away by the names. You can read them in plain language instead:

- `research-autopilot`
  - think of it as the front desk
  - you describe the task, and it explains how the work should begin

- `research-team-orchestrator`
  - think of it as the project manager
  - it only becomes active when work is large enough to become a project

- `gate`
  - think of it as a checkpoint
  - if something is not good enough yet, the project should not move forward

- `Zotero`
  - the formal reference library

- `Obsidian`
  - the longer-lived note and knowledge layer

If you remember only one thing, remember this:

**ask the system to explain the route before it starts doing work.**

---

<a id="who-it-is-for"></a>
## 4. Who this is for

This repository is especially useful for:

- researchers doing literature reviews and evidence synthesis
- computational social scientists working across text, platform data, networks, and reproducibility
- researchers collecting browser-visible platform or web evidence
- writers preparing drafts, revision packs, and submission-ready materials

It can still help with smaller questions.  
But it becomes most useful when you already realize: **this is no longer just one answer, it is turning into a project.**

---

<a id="components"></a>
## 5. What the public stack is actually made of

Without using technical language, you can think of the public stack as five layers:

- `Codex`
  - the front door for conversation and execution
- `research-autopilot`
  - the part that first decides what kind of task this is
- `research-team-orchestrator`
  - the part that turns larger work into structured project coordination
- `project files`
  - the place where rules, status, findings, and checks are written down
- `external tools`
  - things like Zotero, Obsidian, and browser-visible evidence capture

In simple terms:

- Codex controls how you enter
- autopilot decides how work should begin
- orchestrator decides how the project should be organized
- project files make the process inspectable later
- external tools hold references, notes, and evidence in the right places

---

<a id="getting-started"></a>
## 6. First use: only do these three things

Do not try to learn the whole system on day one.

Only do these three things:

### 1. Clone the repository

```powershell
git clone https://github.com/avefield509-lang/codex-research-stack.git
cd codex-research-stack
```

### 2. Create a demo project

```powershell
python .\scripts\init_research_project.py --path ".\examples\demo-project" --route-hint "general-research"
```

Or on Windows:

```powershell
pwsh -ExecutionPolicy Bypass -File ".\scripts\init-research-project.ps1" -Path ".\examples\demo-project"
```

### 3. Ask for route explanation before execution

A good first prompt looks like this:

```text
@research-autopilot This is a new research project.
The topic is: ...
The question is: ...
The materials or data are: ...
The expected outputs are: ...
Explain the route first, then decide whether this should become project-type multi-agent work.
```

The point is not to sound technical.  
The point is to avoid going in the wrong direction too early.

---

<a id="no-command"></a>
## 7. If you do not want to deal with commands yet

Then just remember this sentence:

**state your topic, question, materials, and expected outputs clearly, and ask the system to explain the route before it starts doing work.**

That is the core usage model.

So even if you are not ready to run scripts or inspect directories, you can still use the system in the right order.

---

<a id="starting-a-project"></a>
## 8. How a new project begins

The safest order is:

1. create a project folder
2. initialize the scaffold
3. inspect the core files
4. let the system explain the route before execution

The first files to inspect are:

- `AGENTS.md`
- `research-map.md`
- `findings-memory.md`
- `logs/project-state/current.json`

If those four files are present, the project skeleton is basically in place.

### A simpler way to think about the project skeleton

Many first-time users get nervous when they see multiple files.

But you can read them very simply:

- `AGENTS.md` = project rules
- `research-map.md` = project map
- `findings-memory.md` = what is already known
- `project-state` = current project status

In other words, the system is just taking things that would otherwise stay scattered across chat, memory, and temporary notes, and putting them in fixed places.

### In daily use, most people really do only two things

For most researchers, daily use is mostly this:

1. start a project
2. check the current state

That means:

- initialize the project
- describe the task clearly
- inspect the project map
- inspect the findings record
- inspect the current status

---

<a id="what-counts-as-real-multi-agent-execution"></a>
## 9. Why a project turns into multi-agent work

Many people hear "multi-agent" and imagine a system that immediately splits into many roles.

That is not how this repository treats it.

The more accurate rule is:

- small tasks stay on a simpler path
- only larger project-type work turns into multi-agent coordination

So multi-agent execution is not there to look impressive.  
It appears when the project actually needs:

- division of work
- handoff
- review
- written traces

### What counts as real multi-agent execution

This repository does not treat role-play as multi-agent work.

It only counts as real multi-agent execution when the project leaves behind:

- separate identities
- separate inputs
- separate output locations
- explicit reviewer links
- inspectable traces

If several viewpoints appear inside one answer, that is still not the same thing.

---

<a id="during-a-live-project"></a>
## 10. What to look at during a live project

During a live project, the most important questions are:

1. what stage the project is in
2. who owns the next step
3. what still blocks progress

The visible control chain has three layers:

### Layer 1: task choice

Handled by `research-autopilot`.

It answers:

- what kind of task this is
- which route should come first
- whether the task should stay small or become a project

### Layer 2: project coordination

If the work is no longer a small task, `research-team-orchestrator` appears.

You can think of it as the part that turns the project into a readable workspace:

- who is doing what
- what must be reviewed
- where work is blocked

### Layer 3: execution

Only then do the concrete tasks happen:

- citation verification
- evidence capture
- analysis
- writing
- export

So the most important practical rule is:

**do not start by staring at the tool list; start by looking at route choice and project state.**

---

<a id="the-files-that-matter-most"></a>
## 11. The files that matter most

If you remember only one inspection order, use this one:

1. `AGENTS.md`
2. `research-map.md`
3. `findings-memory.md`
4. `material-passport.yaml`
5. `evidence-ledger.yaml`
6. `logs/project-state/current.json`
7. `logs/quality-gates/pipeline-status.json`

These files usually answer:

- what the project is trying to do
- what is already confirmed
- what stage it is in
- who owns the next step
- what still has not passed

For many non-technical users, the first four files are the ones you will read most often.  
The later ones are more like state and checkpoint records.

---

<a id="use-cases"></a>
## 12. Use cases

### Literature review

This stack helps connect:

- the review question
- candidate literature
- formal reference checks
- a synthesis draft

### Social-platform or web case study

This stack helps connect:

- browser-visible material
- provenance
- evidence capture
- preparation for later coding and analysis

### Computational social science project

This stack helps connect:

- literature
- materials
- analysis
- writing
- reproducibility

The point is not that it can do everything.  
The point is that the whole project can move inside one readable structure.

### Writing, revision, and submission

This stack helps connect:

- drafting
- citation checks
- writing quality checks
- revision materials
- submission materials

---

<a id="integrations"></a>
## 13. Integrations

In simple terms:

- Zotero holds formal references
- Obsidian holds longer-lived notes
- the project folder holds runtime state and traces

### Zotero

Zotero is the formal reference boundary.

That means the sources that truly belong in a paper's formal reference list should eventually end up there.

### Obsidian

Obsidian is the long-lived knowledge layer.

That means reusable notes, ideas, and synthesis can move there over time.

### Browser-visible evidence

For platform and web cases, the repository stays conservative:

- prefer browser-visible material
- keep provenance explicit
- keep "what was seen" separate from "how it is interpreted"

### Local tools

A future app can detect whether the local machine has:

- Python
- Git
- Codex Home
- Zotero
- Obsidian
- browser tooling

If one of those is missing, the system should degrade gracefully rather than collapse completely.

---

<a id="repository-and-future-app"></a>
## 14. Repository and future app

The easiest way to think about the relationship is:

- this repository is the rules and documentation layer
- the future app is the easier daily interface

The repository remains responsible for:

- workflow rules
- schemas
- validators
- templates
- examples
- public documentation

The future app is responsible for:

- onboarding
- dashboards
- task-entry views
- visual project views

So the future app is not a competing rule system.  
It should sit on top of the repository, not beside it as a second source of truth.

If you want the shortest version:

**the repository is the source, the app is the interface.**

---

<a id="public-boundary"></a>
## 15. Public boundary

This repository is not a mirror of a private workstation.

It publishes:

- reusable rules
- templates
- examples
- documentation
- selected scripts

It does not publish:

- personal files
- local trust state
- private keys
- cloud operator material
- local runtime outputs

So what you see here is a **public, explainable, reusable layer**, not the full contents of one person's machine.

---

<a id="troubleshooting"></a>
## 16. If something goes wrong, where to look first

Most problems do not require debugging scripts immediately.

Use this order:

### 1. Where is the project blocked?

Look at:

- `logs/project-state/current.json`

### 2. What is the project trying to do right now?

Look at:

- `research-map.md`
- `findings-memory.md`

### 3. Did a checkpoint fail?

Look at:

- `logs/quality-gates/pipeline-status.json`

### 4. Only then ask whether the public stack itself is broken

If needed, run:

```powershell
python .\scripts\validate_research_stack.py
```

In simpler terms:

- first inspect the current state
- then inspect the project map
- then inspect the checkpoints
- only then suspect the repository itself

---

<a id="roadmap"></a>
## 17. Roadmap

Near-term work:

- better public examples
- clearer visual walkthroughs
- tighter portable defaults
- clearer integration setup notes

Later work:

- stronger public test coverage
- clearer release packaging
- optional adapter layers for heavier runtimes

---

## Final one-sentence version

If you only remember one sentence, make it this:

**tell the system what your topic, question, materials, and expected outputs are, then ask it to explain the route before it starts doing work.**
