Write-Host "=== PRECHECK 1/4: Wikilinks [[...]] ==="
rg -n "\[\[.*\]\]" docs
if ($LASTEXITCODE -eq 0) { throw "Hay wikilinks [[...]] en docs. Convertirlos a markdown links antes de seguir." }

Write-Host "=== PRECHECK 2/4: Restos :contentReference ==="
rg -n ":contentReference" docs
if ($LASTEXITCODE -eq 0) { throw "Hay restos :contentReference en docs. Limpiarlos antes de seguir." }

Write-Host "=== PRECHECK 3/4: Links con .MD mayúscula ==="
rg -n "\]\([^\)]*\.MD\)" docs
if ($LASTEXITCODE -eq 0) { throw "Hay links a .MD mayúscula. Deben ser .md." }

Write-Host "=== PRECHECK 4/4: MkDocs strict build ==="
python -m mkdocs build --strict
if ($LASTEXITCODE -ne 0) { throw "MkDocs build --strict falló. Corregir warnings/errores antes de commitear." }

Write-Host "OK: Preflight pasó completo."
