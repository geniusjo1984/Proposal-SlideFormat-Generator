param(
    [Parameter(Position = 0)]
    [string]$ProjectRoot,

    [string]$BasePath = ".",

    [string]$ProjectName,

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
