# Excel MVP Step 39 - CSV Pack v2: Manifest + Validaciones fuertes + Preservación Dashboard

## Objetivo
Elevar el "CSV pack round-trip" a un artefacto integrable con ACI / futuros sistemas:
1) Export genera un MANIFEST (pack_manifest.json) con metadatos, checksums y conteos.
2) Import valida: schema_version, delimiter/bom, unicidad de IDs, enums y tipos básicos (DATE/NUMBER).
3) Import NO debe tocar hojas fuera del set de tablas (01..15 + 99_Listas/Catalogos si aplica). Debe preservar 00_Home, 98_Ayuda, 20_Dashboard, 21_Calc y cualquier hoja "no-tabla".
4) Tests deterministas que prueben: manifest, checksums, validaciones y preservación.

## Cambios Implementados

### tools/export_excel_csv_pack.py (NUEVO)
- Exporta hojas de tablas (01_Recetas, 02_RecetaVersiones, etc.) a archivos CSV
- Soporta delimitadores: comma, semicolon, tab
- Soporta BOM UTF-8 opcional
- Genera pack_manifest.json con:
  - schema_version: "mvp-v1"
  - created_at: timestamp ISO
  - delimiter, bom, encoding
  - workbook_source: ruta del Excel origen
  - files: array con {name, rows, sha256} por cada CSV
  - total_files, notes

### tools/import_excel_csv_pack.py (NUEVO)
- Importa CSVs del pack al Excel
- Valida manifest si existe (schema, total_files, checksums SHA256)
- Valida unicidad de IDs por tabla (receta_id, batch_id, etc.)
- Valida enums contra Catalogos o defaults
- Valida tipos: fechas YYYY-MM-DD, números float/int
- Preserva hojas no-tabla (00_Home, 98_Ayuda, 20_Dashboard, 21_Calc, etc.)
- Modo dry-run para validación sin guardar

### tools/test_step39.py (NUEVO)
- Test 1: Export crea folder con CSVs + manifest
- Test 2: Manifest tiene estructura correcta
- Test 3: Import con manifest válido pasa (dry-run)
- Test 4: Import falla si se altera checksum de CSV
- Test 5: Import falla si hay IDs duplicados (simulado)
- Test 6: Hojas no-tabla se preservan

## Uso

### Exportar CSV Pack
```powershell
python tools/export_excel_csv_pack.py --delimiter semicolon --bom 0
```

Opciones:
- `--delimiter`: comma | semicolon | tab (default: semicolon)
- `--bom`: 0 | 1 (default: 0, sin BOM)

Salida:
- Crea folder: `data/excel/exports/csv_pack_YYYYMMDD_HHMMSS/`
- Archivos: 01_Recetas.csv, 02_RecetaVersiones.csv, ..., pack_manifest.json
- Imprime resumen con rutas

### Importar CSV Pack
```powershell
python tools/import_excel_csv_pack.py --input "data/excel/exports/csv_pack_20240115_143022" --workbook "data/excel/Quelonio_Excel_MVP_Skeleton.xlsx" --dry-run 1
```

Opciones:
- `--input`: ruta del folder del pack
- `--workbook`: ruta del Excel destino
- `--dry-run`: 0=importar realmente, 1=solo validar

Validaciones realizadas:
- Manifest: schema_version, total_files, existencia de archivos, checksums SHA256
- IDs únicos: receta_id, batch_id, item_id, etc.
- Enums: estado de lotes, tipos de items, etc. (de Catalogos o defaults)
- Tipos: fechas en YYYY-MM-DD, números parseables
- Preservación: solo escribe en hojas 01..15, ignora otras

### Ejecutar Tests
```powershell
python tools/test_step39.py
```

## Validaciones Detalladas

### Unicidad de IDs
Por cada tabla, valida que la columna ID no tenga duplicados:
- 01_Recetas.receta_id
- 02_RecetaVersiones.recipe_version_id
- 03_Lotes.batch_id
- 05_ItemsInventario.item_id
- etc.

### Enums
Valida valores contra catalogos en hoja "Catalogos" o "99_Listas":
- 03_Lotes.estado ∈ CAT_LoteEstado (o defaults: planificado, coccion, etc.)
- 06_MovimientosInventario.tipo_movimiento ∈ CAT_MovTipo
- 05_ItemsInventario.tipo ∈ CAT_ItemTipo
- 11_Clientes.tipo ∈ CAT_ClienteTipo
- 11_Clientes.canal ∈ CAT_Canal
- 12_Ventas.estado_pago ∈ CAT_PagoEstado

### Tipos Básicos
- Campos fecha (*_fecha, fecha_*): deben ser YYYY-MM-DD válidos
- Campos numéricos (volumen_litros, og_target, etc.): float/int parseable

### Preservación de Hojas
Import SOLO modifica hojas que empiecen con 01_ a 15_.
Hojas como 00_Home, 98_Ayuda, 20_Dashboard, 21_Calc, Catalogos se preservan intactas.

## Definición de DONE
- [x] Export genera manifest siempre con schema_version, checksums, etc.
- [x] Import valida manifest (schema, checksums) cuando existe
- [x] Import valida unicidad IDs con reporte claro de errores
- [x] Import valida enums contra Catalogos o defaults
- [x] Import valida tipos básicos (fechas, números)
- [x] Import preserva hojas no-tabla (00_Home, 20_Dashboard, etc.)
- [x] test_step39.py pasa todos los casos (incluyendo fallos esperados)
- [x] Documentación completa en este archivo

## Notas Técnicas
- SHA256 se calcula sobre bytes exactos del archivo CSV (incluyendo BOM si existe)
- Encoding siempre UTF-8, BOM opcional según flag
- Manifest es JSON válido, legible por humanos
- Tests usan dry-run para evitar modificar archivos en pruebas
- Compatible con Excel MVP Skeleton actual (pocas tablas, pero extensible)