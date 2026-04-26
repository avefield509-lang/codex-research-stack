param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" })
)

$ErrorActionPreference = "Stop"

# This script overwrites matching Research Autopilot skills under CODEX_HOME.
# Run it explicitly only when you want to sync the public plugin skills locally.

$repoRoot = Split-Path -Parent $PSScriptRoot
$pluginSkillsRoot = Join-Path $repoRoot "skills\plugins\research-autopilot\skills"
$targetRoot = Join-Path $CodexHome "skills"

if (-not (Test-Path $pluginSkillsRoot)) {
    throw "公开版插件技能目录不存在：$pluginSkillsRoot"
}

New-Item -ItemType Directory -Force -Path $targetRoot | Out-Null

$synced = @()
Get-ChildItem -LiteralPath $pluginSkillsRoot -Directory | ForEach-Object {
    if (-not (Test-Path (Join-Path $_.FullName "SKILL.md"))) {
        return
    }
    $target = Join-Path $targetRoot $_.Name
    if (Test-Path $target) {
        Remove-Item -LiteralPath $target -Recurse -Force
    }
    Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse -Force
    $synced += $_.Name
}

[pscustomobject]@{
    codex_home = $CodexHome
    target_root = $targetRoot
    synced_skills = $synced
} | ConvertTo-Json -Depth 5
