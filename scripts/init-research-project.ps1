param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Path,
    [switch]$SkipCodexTrust
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$skillsRoot = Join-Path $repoRoot "skills"
$rootAgentsPath = Join-Path $skillsRoot "AGENTS.md"
$git = (Get-Command git -ErrorAction SilentlyContinue)?.Source
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$codexConfig = Join-Path $codexHome "config.toml"

if (-not $git) {
    throw "没有找到 git。请先安装 Git 并确保其已进入 PATH。"
}
if (-not (Test-Path $rootAgentsPath)) {
    throw "公开版 skills/AGENTS.md 不存在：$rootAgentsPath"
}

$resolved = if ([System.IO.Path]::IsPathRooted($Path)) { $Path } else { Join-Path (Get-Location) $Path }
$projectPath = [System.IO.Path]::GetFullPath($resolved)
$projectName = Split-Path -Leaf $projectPath

$projectAgentsDir = Join-Path $projectPath ".codex\agents"
$dispatchDir = Join-Path $projectPath ".codex\dispatch"
$contextPacketsDir = Join-Path $projectPath ".codex\context-packets"
$agentRunsDir = Join-Path $projectPath "outputs\agent-runs"
$handoffLogsDir = Join-Path $projectPath "logs\agent-handoffs"
$gateLogsDir = Join-Path $projectPath "logs\quality-gates"
$projectStateDir = Join-Path $projectPath "logs\project-state"

function Write-JsonIfMissing {
    param(
        [Parameter(Mandatory = $true)][string]$TargetPath,
        [Parameter(Mandatory = $true)]$Payload
    )
    if (-not (Test-Path $TargetPath)) {
        $dir = Split-Path -Parent $TargetPath
        if ($dir) {
            New-Item -ItemType Directory -Force -Path $dir | Out-Null
        }
        $Payload | ConvertTo-Json -Depth 10 | Set-Content -Path $TargetPath -Encoding UTF8
    }
}

New-Item -ItemType Directory -Force -Path $projectPath | Out-Null
foreach ($dir in @($projectAgentsDir, $dispatchDir, $contextPacketsDir, $agentRunsDir, $handoffLogsDir, $gateLogsDir, $projectStateDir)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
}

if (-not (Test-Path (Join-Path $projectPath ".git"))) {
    & $git init -b main $projectPath | Out-Null
}

$gitignorePath = Join-Path $projectPath ".gitignore"
if (-not (Test-Path $gitignorePath)) {
@"
.venv/
__pycache__/
.ipynb_checkpoints/
outputs/
artifacts/
*.log
*.tmp
.env
.env.*
"@ | Set-Content -Path $gitignorePath -Encoding UTF8
}

$readmePath = Join-Path $projectPath "README.md"
if (-not (Test-Path $readmePath)) {
    @(
        "# $projectName",
        '',
        'This project was initialized from VELA.',
        '',
        '## What you get',
        '',
        '- A Git repository',
        '- Project-level AGENTS.md',
        '- .codex/agents starter definitions',
        '- Canonical dispatch, handoff, gate, and project-state directories',
        '- Pipeline status and writing-quality report templates',
        '',
        '## Recommended next step',
        '',
        'Run the public orchestrator on this project:',
        '',
        '```powershell',
        'python scripts/plan_research_team.py --project-root YOUR_PROJECT_PATH --route-id literature-review --deliverable-type literature_synthesis --work-unit discovery --work-unit writing',
        '```'
    ) | Set-Content -Path $readmePath -Encoding UTF8
}

$agentsMdPath = Join-Path $projectPath "AGENTS.md"
if (-not (Test-Path $agentsMdPath)) {
    @(
        '# AGENTS',
        '',
        'This project inherits the global constraints from skills/AGENTS.md in the VELA repository.',
        'Project rules may only become stricter; they must not expand permissions or bypass the required citation, evidence, writing-capture, or reproducibility chains.',
        '',
        '```yaml',
        'agent_constraints:',
        '  forbid_skills_mcp: []',
        '  forbid_write_roots: []',
        '  max_execution_mode: null',
        '  require_review_for:',
        '    - paper_draft',
        '    - revision_package',
        '    - submission_package',
        '    - figures_tables',
        '    - reproducibility_bundle',
        '    - literature_synthesis',
        '    - case_dataset',
        '    - project_map',
        '  project_truth_sources:',
        '    - research-map.md',
        '    - findings-memory.md',
        '    - material-passport.yaml',
        '    - evidence-ledger.yaml',
        '```'
    ) | Set-Content -Path $agentsMdPath -Encoding UTF8
}

if (-not (Test-Path (Join-Path $projectPath "research-map.md"))) {
@"
# Research Map

- Research question:
- Active route:
- Current stage:
- Expected deliverables:
"@ | Set-Content -Path (Join-Path $projectPath "research-map.md") -Encoding UTF8
}

if (-not (Test-Path (Join-Path $projectPath "findings-memory.md"))) {
@"
# Findings Memory

- Confirmed facts:
- Rejected paths:
- Pending verification:
"@ | Set-Content -Path (Join-Path $projectPath "findings-memory.md") -Encoding UTF8
}

if (-not (Test-Path (Join-Path $projectPath "material-passport.yaml"))) {
@"
project_name: $projectName
route_id: null
current_stage: research_design
data_access_level: public_open
materials: []
ethics_notes: []
truth_sources:
  - research-map.md
  - findings-memory.md
  - material-passport.yaml
  - evidence-ledger.yaml
"@ | Set-Content -Path (Join-Path $projectPath "material-passport.yaml") -Encoding UTF8
}

if (-not (Test-Path (Join-Path $projectPath "evidence-ledger.yaml"))) {
@"
entries: []
"@ | Set-Content -Path (Join-Path $projectPath "evidence-ledger.yaml") -Encoding UTF8
}

Write-JsonIfMissing -TargetPath (Join-Path $gateLogsDir "pipeline-status.json") -Payload @{
    route_id = $null
    current_stage = "research_design"
    completed_stages = @()
    gate_decisions = @{}
    allowed_to_advance = $false
}

Write-JsonIfMissing -TargetPath (Join-Path $gateLogsDir "writing-quality-report.json") -Payload @{
    status = "pending"
    checked_deliverable = $null
    target_paths = @()
    checks = @{
        style_calibration = @{ decision = "pending"; notes = @() }
        argument_chain_closure = @{ decision = "pending"; notes = @() }
        citation_alignment = @{ decision = "pending"; notes = @() }
        empty_phrase_scan = @{ decision = "pending"; hits = @(); notes = @() }
    }
    banned_phrases = @("总而言之", "双刃剑", "多维度视角")
    generated_by = $null
    updated_at = $null
}

Write-JsonIfMissing -TargetPath (Join-Path $projectStateDir "current.json") -Payload @{
    project_name = $projectName
    route_id = $null
    project_type = $null
    dispatch_run_id = $null
    dispatch_stage = "planning"
    pipeline_stage = "research_design"
    status = "initialized"
    current_owner_agent_id = "project-manager"
    current_owner_display_name = "Project Manager Agent"
    blockers = @()
    next_quality_gates = @()
    selected_agents = @()
    selected_producers = @()
    selected_reviewers = @()
    review_agents = @{}
    milestones = @(@{ id = "project_initialized"; label = "Project initialized"; status = "complete" })
}

if (-not (Test-Path (Join-Path $projectStateDir "history.md"))) {
@"
# Project State History

- Project initialized.
"@ | Set-Content -Path (Join-Path $projectStateDir "history.md") -Encoding UTF8
}

$agentTemplates = @(
    @{
        File = "project-manager.json"
        Payload = @{
            agent_id = "project-manager"
            display_name = "Project Manager Agent"
            preferred_model = $null
            role = "manager"
            enabled = $true
            isolation_method = $null
            parallel_safe = $null
            integration_review_required = $null
            capability_tags_subset = $null
            allowed_skills_mcp_subset = @("research-stack-manager", "project-retrospective-evolver")
            write_scope_subset = @("outputs/agent-runs/<run_id>/<agent_id>/")
            max_execution_mode = "sequential_multi_agent_execution"
            required_inputs = @("route_id", "clarification_card", "dispatch_contract")
            expected_outputs = @("summary.md", "result.json")
            review_gate = $null
        }
    },
    @{
        File = "literature-producer.json"
        Payload = @{
            agent_id = "literature-producer"
            display_name = "Literature Agent"
            preferred_model = $null
            role = "producer"
            enabled = $false
            isolation_method = $null
            parallel_safe = $null
            integration_review_required = $null
            capability_tags_subset = $null
            allowed_skills_mcp_subset = $null
            write_scope_subset = @("outputs/agent-runs/<run_id>/<agent_id>/")
            max_execution_mode = $null
            required_inputs = @("clarification_card", "project_truth_sources")
            expected_outputs = @("summary.md", "result.json")
            review_gate = "mandatory-review-when-required"
        }
    },
    @{
        File = "social-platform-producer.json"
        Payload = @{
            agent_id = "social-platform-producer"
            display_name = "Platform Evidence Agent"
            preferred_model = $null
            role = "producer"
            enabled = $false
            isolation_method = $null
            parallel_safe = $null
            integration_review_required = $null
            capability_tags_subset = $null
            allowed_skills_mcp_subset = $null
            write_scope_subset = @("outputs/agent-runs/<run_id>/<agent_id>/")
            max_execution_mode = $null
            required_inputs = @("clarification_card", "evidence_scope")
            expected_outputs = @("summary.md", "result.json")
            review_gate = "mandatory-review-when-required"
        }
    },
    @{
        File = "analysis-producer.json"
        Payload = @{
            agent_id = "analysis-producer"
            display_name = "Analysis Agent"
            preferred_model = $null
            role = "producer"
            enabled = $false
            isolation_method = $null
            parallel_safe = $null
            integration_review_required = $null
            capability_tags_subset = $null
            allowed_skills_mcp_subset = $null
            write_scope_subset = @("outputs/agent-runs/<run_id>/<agent_id>/")
            max_execution_mode = $null
            required_inputs = @("dataset_scope", "analysis_plan")
            expected_outputs = @("summary.md", "result.json")
            review_gate = "mandatory-review-when-required"
        }
    },
    @{
        File = "writing-producer.json"
        Payload = @{
            agent_id = "writing-producer"
            display_name = "Writing Agent"
            preferred_model = $null
            role = "producer"
            enabled = $false
            isolation_method = $null
            parallel_safe = $null
            integration_review_required = $null
            capability_tags_subset = $null
            allowed_skills_mcp_subset = $null
            write_scope_subset = @("outputs/agent-runs/<run_id>/<agent_id>/")
            max_execution_mode = $null
            required_inputs = @("writing_scope", "verified_citations")
            expected_outputs = @("summary.md", "result.json")
            review_gate = "mandatory-review-when-required"
        }
    },
    @{
        File = "reviewer.json"
        Payload = @{
            agent_id = "reviewer"
            display_name = "Reviewer Agent"
            preferred_model = $null
            role = "reviewer"
            enabled = $true
            isolation_method = $null
            parallel_safe = $null
            integration_review_required = $null
            capability_tags_subset = $null
            allowed_skills_mcp_subset = @("citation-verifier", "academic-paper-review", "openalex-mcp", "semantic-scholar-mcp")
            write_scope_subset = @("outputs/agent-runs/<run_id>/<agent_id>/")
            max_execution_mode = "sequential_multi_agent_execution"
            required_inputs = @("target_agent_result", "target_agent_summary")
            expected_outputs = @("review.<target_agent_id>.md", "gate.<target_agent_id>.json")
            review_gate = "target-specific"
        }
    }
)

foreach ($template in $agentTemplates) {
    Write-JsonIfMissing -TargetPath (Join-Path $projectAgentsDir $template.File) -Payload $template.Payload
}

if (-not $SkipCodexTrust -and (Test-Path $codexConfig)) {
    $configText = Get-Content -Raw -Encoding UTF8 $codexConfig
    $header = "[projects.'$projectPath']"
    $escapedHeader = [regex]::Escape($header)
    $trustPattern = "(?ms)$escapedHeader\s*\r?\ntrust_level\s*=\s*""[^""]*"""
    $desiredBlock = "$header`r`ntrust_level = ""trusted"""
    if ($configText -match $trustPattern) {
        $configText = [regex]::Replace($configText, $trustPattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $desiredBlock })
    } elseif ($configText -match $escapedHeader) {
        $configText = [regex]::Replace($configText, $escapedHeader, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $desiredBlock })
    } else {
        $configText = $configText.TrimEnd() + "`r`n`r`n" + $desiredBlock + "`r`n"
    }
    Set-Content -Path $codexConfig -Value $configText -Encoding UTF8
}

Write-Host "Public research project initialized." -ForegroundColor Green
Write-Host "Project path: $projectPath"
Write-Host "Project agents dir: $projectAgentsDir"
Write-Host "Dispatch dir: $dispatchDir"
if (-not $SkipCodexTrust -and (Test-Path $codexConfig)) {
    Write-Host "Codex trust updated in: $codexConfig"
}
