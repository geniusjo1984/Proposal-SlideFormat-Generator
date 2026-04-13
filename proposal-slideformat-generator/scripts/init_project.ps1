param(
    [Parameter(Position = 0)]
    [string]$ProjectRoot,

    [string]$BasePath = ".",

    [string]$ProjectName,

    [switch]$CreateControlDocs,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$skillRoot = Split-Path -Parent $PSScriptRoot
$resolvedProjectRoot = if ($ProjectRoot) {
    if ([System.IO.Path]::IsPathRooted($ProjectRoot)) {
        [System.IO.Path]::GetFullPath($ProjectRoot)
    } else {
        [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $ProjectRoot))
    }
} else {
    if (-not $ProjectName) {
        throw "Specify either -ProjectRoot or -ProjectName."
    }

    $resolvedBasePath = if ([System.IO.Path]::IsPathRooted($BasePath)) {
        [System.IO.Path]::GetFullPath($BasePath)
    } else {
        [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $BasePath))
    }

    [System.IO.Path]::GetFullPath((Join-Path $resolvedBasePath $ProjectName))
}

$folders = @(
    "01.Input_RfP",
    "02.Reference_Templete",
    "03.Reference_Contents_Main",
    "04.Reference_Contents_Assistance",
    "05.Output_Slide"
)

$files = @(
    @{ Source = "references/design-template.md"; Destination = "DESIGN.md" },
    @{ Source = "references/task-template.md"; Destination = "TASK.md" },
    @{ Source = "references/agent-template.md"; Destination = "AGENT.md" }
)

if (-not (Test-Path -LiteralPath $resolvedProjectRoot)) {
    New-Item -ItemType Directory -Path $resolvedProjectRoot | Out-Null
}

foreach ($folder in $folders) {
    $target = Join-Path $resolvedProjectRoot $folder
    if (-not (Test-Path -LiteralPath $target)) {
        New-Item -ItemType Directory -Path $target | Out-Null
        Write-Host "[create] $target"
    }
}

$rfpPlaceholderPath = Join-Path $resolvedProjectRoot "01.Input_RfP\PUT_RFP_HERE.txt"
if ((-not (Test-Path -LiteralPath $rfpPlaceholderPath)) -or $Force) {
    @(
        "Place the source RfP or RFP document in this folder before creating TASK.md or drafting slides.",
        "The skill should stop and ask for the RfP if this folder has no source file."
    ) | Set-Content -LiteralPath $rfpPlaceholderPath -Encoding UTF8
    Write-Host "[write]  $rfpPlaceholderPath"
}

if (-not $CreateControlDocs) {
    Write-Host "[done]   Folder scaffold created."
    Write-Host "[next]   Put the source RfP into 01.Input_RfP, then rerun with -CreateControlDocs."
    return
}

$rfpFiles = Get-ChildItem -LiteralPath (Join-Path $resolvedProjectRoot "01.Input_RfP") -File |
    Where-Object { $_.Name -ne "PUT_RFP_HERE.txt" }

if ($rfpFiles.Count -eq 0) {
    throw "No source RfP found in 01.Input_RfP. Put the RfP file in that folder before using -CreateControlDocs."
}

foreach ($file in $files) {
    $sourcePath = Join-Path $skillRoot $file.Source
    $targetPath = Join-Path $resolvedProjectRoot $file.Destination

    if ((Test-Path -LiteralPath $targetPath) -and -not $Force) {
        Write-Host "[skip]   $targetPath"
        continue
    }

    $content = Get-Content -LiteralPath $sourcePath -Raw
    Set-Content -LiteralPath $targetPath -Value $content -Encoding UTF8
    Write-Host "[write]  $targetPath"
}
