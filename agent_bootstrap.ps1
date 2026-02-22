param(
    [switch]$SkipLlms,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$PreflightArgs
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$preflightScript = Join-Path $repoRoot "preflight_repo.ps1"
$buildScript = Join-Path $repoRoot "tools\build_llms_txt.py"
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"

Write-Host "[INFO] Agent bootstrap iniciado"

if (-not (Test-Path $preflightScript)) {
    Write-Host "[FAIL] No existe preflight script: $preflightScript"
    exit 1
}

Write-Host "[INFO] Ejecutando preflight_repo.ps1"
& powershell -NoProfile -ExecutionPolicy Bypass -File $preflightScript @PreflightArgs
$preflightExit = $LASTEXITCODE
if ($preflightExit -ne 0) {
    Write-Host "[FAIL] Preflight fallo (exit_code=$preflightExit)"
    exit $preflightExit
}
Write-Host "[PASS] Preflight OK"

if ($SkipLlms) {
    Write-Host "[INFO] -SkipLlms activo: se omite build_llms_txt"
    Write-Host "[PASS] Agent bootstrap completado"
    exit 0
}

if (-not (Test-Path $buildScript)) {
    Write-Host "[FAIL] No existe build script: $buildScript"
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

Write-Host "[INFO] Generando llms.txt/llms-full.txt"
& $pythonCmd $buildScript
$buildExit = $LASTEXITCODE
if ($buildExit -ne 0) {
    Write-Host "[FAIL] build_llms_txt fallo (exit_code=$buildExit)"
    exit $buildExit
}

Write-Host "[PASS] llms.txt y llms-full.txt generados"
Write-Host "[PASS] Agent bootstrap completado"
exit 0
