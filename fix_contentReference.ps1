$pattern = "\s*:contentReference\[[^\]]+\]\{index=\d+\}"

$files = Get-ChildItem -Path .\docs -Recurse -File -Filter *.md
$changedFiles = New-Object System.Collections.Generic.List[string]

foreach ($f in $files) {
  $raw = Get-Content -LiteralPath $f.FullName -Raw
  if ($raw -match ":contentReference\[" ) {
    $new = $raw -replace $pattern, ""
    if ($new -ne $raw) {
      Set-Content -LiteralPath $f.FullName -Value $new -Encoding utf8
      $changedFiles.Add($f.FullName) | Out-Null
    }
  }
}

Write-Host ("Archivos modificados: " + $changedFiles.Count)
if ($changedFiles.Count -gt 0) {
  $changedFiles | ForEach-Object { Write-Host (" - " + $_) }
}
