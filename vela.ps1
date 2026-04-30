param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Args
)

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Python = if ($env:VELA_PYTHON) { $env:VELA_PYTHON } else { "python" }
& $Python (Join-Path $RepoRoot "scripts\vela.py") @Args
