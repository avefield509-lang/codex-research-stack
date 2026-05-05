param(
    [string]$ProfilePath = $(Join-Path $env:APPDATA "Zotero\Zotero\Profiles"),
    [string]$DownloadDir = $(Join-Path (Split-Path -Parent $PSScriptRoot) "artifacts\downloads")
)

$ErrorActionPreference = "Stop"

# This script downloads/stages Zotero add-ons and writes them into the selected
# Zotero profile. Run it explicitly only after confirming the profile path.

function Resolve-ZoteroProfile {
    param([string]$BasePath)
    if (Test-Path -LiteralPath (Join-Path $BasePath "extensions")) { return $BasePath }
    $candidate = Get-ChildItem -LiteralPath $BasePath -Directory -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $candidate) {
        throw "没有找到 Zotero profile。请显式传入 -ProfilePath。"
    }
    return $candidate.FullName
}

function Download-WithResume {
    param([string]$Url,[string]$TargetPath,[int64]$ExpectedSize,[int]$MaxAttempts = 6)
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $TargetPath) | Out-Null
    for ($attempt = 1; $attempt -le $MaxAttempts; $attempt++) {
        if ((Test-Path -LiteralPath $TargetPath) -and ((Get-Item -LiteralPath $TargetPath).Length -ge $ExpectedSize)) { return }
        & curl.exe -L -C - $Url -o $TargetPath | Out-Null
        if ((Test-Path -LiteralPath $TargetPath) -and ((Get-Item -LiteralPath $TargetPath).Length -ge $ExpectedSize)) { return }
        Start-Sleep -Seconds 2
    }
    throw "下载失败或文件未达到预期大小：$TargetPath"
}

$resolvedProfile = Resolve-ZoteroProfile -BasePath $ProfilePath
$addons = @(
    @{ id = "better-bibtex@iris-advies.com"; file = "zotero-better-bibtex-9.0.19.xpi"; url = "https://github.com/retorquere/zotero-better-bibtex/releases/download/v9.0.19/zotero-better-bibtex-9.0.19.xpi"; size = 34204005 },
    @{ id = "Knowledge4Zotero@windingwind.com"; file = "better-notes-for-zotero-v3.0.4.xpi"; url = "https://github.com/windingwind/zotero-better-notes/releases/download/v3.0.4/better-notes-for-zotero.xpi"; size = 5190470 },
    @{ id = "jasminum@linxzh.com"; file = "jasminum_1.1.35.xpi"; url = "https://github.com/l0o0/jasminum/releases/download/v1.1.35/jasminum_1.1.35.xpi"; size = 399781 }
)

$extensionsDir = Join-Path $resolvedProfile "extensions"
New-Item -ItemType Directory -Force -Path $extensionsDir | Out-Null

foreach ($addon in $addons) {
    $downloadTarget = Join-Path $DownloadDir $addon.file
    Download-WithResume -Url $addon.url -TargetPath $downloadTarget -ExpectedSize $addon.size
    Copy-Item -LiteralPath $downloadTarget -Destination (Join-Path $extensionsDir ("{0}.xpi" -f $addon.id)) -Force
}

[pscustomobject]@{
    profile_path = $resolvedProfile
    extensions_dir = $extensionsDir
    staged_extensions = $addons | ForEach-Object { $_.id }
    note = "插件已复制到 profile/extensions，重启 Zotero 后生效。"
} | ConvertTo-Json -Depth 5
