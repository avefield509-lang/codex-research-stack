# Installation

VELA is designed as a portable workflow environment package. The base workflow should remain usable in a user's own Codex setup without the local research board.

## Normal Use

Download or clone the public package, then place the workflow files where your Codex environment can read them. Keep project data in your own project folder, not inside generated build output.

```powershell
git clone https://github.com/Marcus-AI4SS/skills-app-github.git vela-public
cd vela-public
```

This repository currently hosts the public README, GitHub Pages, release-facing workspace, and shared brand assets while the installable VELA package is being separated from the older public app workspace.

## Optional HELM Companion

HELM is the local research board. It may read VELA project state and prepare Codex handoffs, but VELA must remain understandable and usable without HELM.

## Public Build Rule

Public packages must not include private research notes, PDFs, browser sessions, Zotero databases, Obsidian vaults, tokens, SSH keys, account traces, or machine-specific paths.
