# KIT_AUDITORIA_DATASETS

## Objetivo
Validar consistencia, links, precedencia de datos (Excel > Biblia > Supuestos), y “agua no se asume” en módulo datasets. Auditoría rápida (2 minutos) para QA/QC antes de deploy.

## Checklist (10-15 bullets)
- Todos los items referencian INCIDENCIA_ESTANDAR con link relativo correcto.
- No hay precios exactos (ARS/USD) en items; solo rangos o ausente.
- Cada item incluye “COA/Excel manda sobre Biblia. Agua no se asume.”.
- Naming/IDs siguen prefijos: MALTA__/LUPULO__/LEVADURA__.
- Links en 12_Datasets_Materias_Primas.md apuntan a items existentes.
- Regla Excel > Biblia > Supuestos aplicada en referencias.
- Items Argentina-first marcados como AR; importados como INT.
- Rangos típicos (no valores únicos) en parámetros clave.
- No hay snapshots o market data duros (solo placeholders si existen).
- Archivo COSECHA_COMPARTIDA_MINIMOS.md existe con checklist mínimo.
- Build strict pasa sin errores.
- No hay “Incidencia por estilo” residual (tablas viejas).
- Sección “Levaduras” incluye link a COSECHA_COMPARTIDA_MINIMOS.md.

## Comandos PowerShell (Listos para Copiar)
```powershell
# 1. Build strict
python -m mkdocs build --strict

# 2. Buscar tablas viejas "Incidencia por estilo"
Select-String -Pattern "Incidencia por estilo" -Path docs/12_Datasets_Materias_Primas/ -Recurse

# 3. Buscar precios duros (ARS/USD)
Select-String -Pattern "precio|ARS|USD" -Path docs/12_Datasets_Materias_Primas/ -Recurse

# 4. Listar items por categoría
Get-ChildItem docs/12_Datasets_Materias_Primas/maltas/items/ | Select-Object Name
Get-ChildItem docs/12_Datasets_Materias_Primas/lupulos/items/ | Select-Object Name
Get-ChildItem docs/12_Datasets_Materias_Primas/levaduras/items/ | Select-Object Name
```

## Criterios de Aprobación/Rechazo
- **Aprobado**: Checklist completo, comandos no devuelven resultados problemáticos, build strict OK. Dataset listo para deploy.
- **Rechazado**: Si comandos encuentran tablas viejas, precios duros, o build strict falla. Requiere corrección inmediata (e.g., remover tablas, ajustar referencias).