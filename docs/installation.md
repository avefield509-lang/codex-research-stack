# Installation

VELA is a repository-based Codex workflow wrapper. There is no desktop installer; the install scripts create a local `vela` shim and a small install receipt under `~/.vela`.

## Download

```powershell
git clone https://github.com/Marcus-AI4SS/VELA.git vela
cd vela
.\install.ps1
```

You can also download the repository as a ZIP from GitHub and unpack it wherever your Codex environment can read it.

## Use With Codex

Initialize a project and then return to Codex with a bounded handoff:

```powershell
.\vela.ps1 init ..\my-research-project --skip-codex-trust
cd ..\my-research-project
..\vela\vela.ps1 handoff new --project .
..\vela\vela.ps1 validate . --repair-context
```

VELA provides `.codex/config.toml.example` and `AGENTS.md` templates, but it does not silently rewrite your global Codex configuration.

## Keep It Portable

Do not put private notes, PDFs, browser sessions, Zotero databases, Obsidian vaults, tokens, SSH keys, or machine-specific paths into files you plan to share.

## Optional HELM

HELM is a separate local board. It can make VELA project state easier to inspect, but it is not required to use VELA.
