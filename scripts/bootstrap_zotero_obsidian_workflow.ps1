param(
    [string]$VaultPath = $(Join-Path $HOME "Documents\Obsidian Vault"),
    [string]$CodexResearchPath = $(Join-Path (Join-Path $HOME "Documents\Obsidian Vault") "Codex Research"),
    [string]$RepoRoot = $(Split-Path -Parent $PSScriptRoot)
)

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path $CodexResearchPath | Out-Null

$dirs = @(
    "00-系统",
    "00-模板",
    "10-项目",
    "20-文献",
    "20-文献\_zotero-sync",
    "30-方法",
    "40-综合",
    "50-面板",
    "90-归档"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path (Join-Path $CodexResearchPath $dir) | Out-Null
}

$templateRoot = Join-Path $RepoRoot "skills\templates\obsidian"
Copy-Item -LiteralPath (Join-Path $templateRoot "文献笔记模板.md") -Destination (Join-Path $CodexResearchPath "00-模板\文献笔记模板.md") -Force
Copy-Item -LiteralPath (Join-Path $templateRoot "项目地图模板.md") -Destination (Join-Path $CodexResearchPath "00-模板\项目地图模板.md") -Force
Copy-Item -LiteralPath (Join-Path $templateRoot "方法卡模板.md") -Destination (Join-Path $CodexResearchPath "00-模板\方法卡模板.md") -Force

$panelSource = Join-Path $templateRoot "panels"
Get-ChildItem -LiteralPath $panelSource -Filter *.md | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $CodexResearchPath ("50-面板\" + $_.Name)) -Force
}

& (Join-Path $PSScriptRoot "install_obsidian_research_plugins.ps1") -VaultPath $VaultPath
& (Join-Path $PSScriptRoot "install_zotero_research_addons.ps1")
& (Join-Path $PSScriptRoot "sync_research_autopilot_skills.ps1")

[pscustomobject]@{
    vault = $VaultPath
    codex_research = $CodexResearchPath
    directories = $dirs
    note = "公开版 Zotero-Obsidian 工作流骨架已完成。"
} | ConvertTo-Json -Depth 5
