param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" })
)

$ErrorActionPreference = "Stop"

$syncScript = Join-Path $PSScriptRoot "sync_research_autopilot_skills.ps1"
if (-not (Test-Path $syncScript)) {
    throw "缺少公开版同步脚本：$syncScript"
}

& $syncScript -CodexHome $CodexHome
