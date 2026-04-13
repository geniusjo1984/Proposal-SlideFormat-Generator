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

$placeholders = @(
    @{
        Path = "01.Input_RfP\PUT_RFP_HERE.txt"
        Lines = @(
            "Place the source RfP or RFP document in this folder before requesting DESIGN.md, TASK.md, or slides.",
            "The skill should stop and ask for the RfP if this folder has no source file."
        )
    },
    @{
        Path = "02.Reference_Templete\PUT_TEMPLATE_REFERENCES_HERE.txt"
        Lines = @(
            "Place slide template PDFs, sample decks, or formatting references in this folder.",
            "When this folder has files, the skill should reconstruct DESIGN.md from those references."
        )
    },
    @{
        Path = "03.Reference_Contents_Main\PUT_MAIN_REFERENCES_HERE.txt"
        Lines = @(
            "Place main proposal references, benchmark materials, policy documents, or core evidence in this folder."
        )
    },
    @{
        Path = "04.Reference_Contents_Assistance\PUT_ASSISTANCE_REFERENCES_HERE.txt"
        Lines = @(
            "Place supporting references, supplemental examples, or secondary evidence in this folder."
        )
    }
)

foreach ($placeholder in $placeholders) {
    $placeholderPath = Join-Path $resolvedProjectRoot $placeholder.Path
    if ((-not (Test-Path -LiteralPath $placeholderPath)) -or $Force) {
        $placeholder.Lines | Set-Content -LiteralPath $placeholderPath -Encoding UTF8
        Write-Host "[write]  $placeholderPath"
    }
}

Write-Host "[done]   Folder scaffold created."
Write-Host "[next]   Put the RfP and references into the folders, then request baseline design generation."
