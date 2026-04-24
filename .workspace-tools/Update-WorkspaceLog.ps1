Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$toolsRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $toolsRoot "..")).Path
$configPath = Join-Path $toolsRoot "workspace-log.json"
$importedHistoryPath = Join-Path $toolsRoot "imported-history.md"
$config = Get-Content -Raw -LiteralPath $configPath | ConvertFrom-Json

function Get-GitLines {
  param(
    [string]$RepoRoot,
    [string[]]$GitArgs
  )

  $output = @(& git -C $RepoRoot @GitArgs 2>$null)
  if ($LASTEXITCODE -ne 0) {
    return ,@()
  }
  return ,@($output)
}

function Join-MarkdownList {
  param([string[]]$Lines)
  if (-not $Lines -or $Lines.Count -eq 0) {
    return @("- none")
  }
  return @($Lines | ForEach-Object { "- $_" })
}

$branch = (Get-GitLines -RepoRoot $repoRoot -GitArgs @("branch","--show-current")) | Select-Object -First 1
if (-not $branch) {
  $branch = "<unknown>"
}

$head = (Get-GitLines -RepoRoot $repoRoot -GitArgs @("rev-parse","--short","HEAD")) | Select-Object -First 1
if (-not $head) {
  $head = "<no-commit>"
}

$historyRecords = Get-GitLines -RepoRoot $repoRoot -GitArgs @("log","--date=short","--pretty=format:%h%x1f%ad%x1f%s")
$historyLines = @()
if ($historyRecords.Count -eq 0) {
  $historyLines += "- no commits yet"
} else {
  foreach ($record in $historyRecords) {
    $parts = $record -split [char]0x1f
    if ($parts.Count -ge 3) {
      $historyLines += "- $($parts[1]) `$($parts[0])` $($parts[2])"
    }
  }
}

$statusLines = Get-GitLines -RepoRoot $repoRoot -GitArgs @("status","--short")
$importedHistory = Get-Content -Raw -LiteralPath $importedHistoryPath

$content = @(
  "# $($config.display_name) Workspace Log",
  "",
  "- generated_at: $(Get-Date -Format s)",
  ('- branch: `' + $branch + '`'),
  ('- HEAD: `' + $head + '`'),
  "- purpose: $($config.purpose)",
  "",
  "## Automation",
  "",
  ('- log file: `' + $config.log_file + '`'),
  "- update trigger: pre-commit, post-merge, post-checkout",
  "- hook strategy: Git hook regenerates this file automatically before new commits are finalized",
  "",
  $importedHistory,
  "",
  "## Independent Repo Commit History",
  ""
)
$content += $historyLines
$content += @(
  "",
  "## Current Working Tree Status",
  ""
)
$content += (Join-MarkdownList -Lines $statusLines)

$logPath = Join-Path $repoRoot $config.log_file
Set-Content -LiteralPath $logPath -Value ($content -join "`r`n") -Encoding utf8BOM
