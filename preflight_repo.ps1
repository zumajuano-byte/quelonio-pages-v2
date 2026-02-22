param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$ArgsPassthrough
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$scriptPath = Join-Path $repoRoot "tools\preflight_repo.py"
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $scriptPath)) {
    Write-Host "[FAIL] Script not found: $scriptPath"
    exit 1
}

$pythonCmd = $null
if (Test-Path $venvPython) {
    $pythonCmd = $venvPython
} else {
    $pythonCheck = Get-Command python -ErrorAction SilentlyContinue
    if ($null -eq $pythonCheck) {
        Write-Host "[FAIL] Python no encontrado. Activar .venv o instalar Python."
        exit 1
    }
    $pythonCmd = "python"
}

Write-Host "[INFO] Ejecutando preflight con: $pythonCmd"
& $pythonCmd $scriptPath @ArgsPassthrough
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    Write-Host "[FAIL] Preflight repo/venv fallo."
}

exit $exitCode
