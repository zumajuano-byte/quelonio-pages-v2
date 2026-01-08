# Esquema Dataset Materias Primas

## Reglas generales
- Prioridad: Datos duros de Excel/Sheets > Contenido publicado en Biblia > Supuestos teóricos.
- Agua no se incluye en datasets (manejo separado en módulo 01_Agua).
- Datasets son teóricos/publicables; no incorporar datos operativos del cervecero.

## Campos obligatorios
- Nombre genérico.
- Región (ej. AR/INT para Argentina-first).
- Notas de importación donde aplique.
- Tabla de incidencia heurística (Bajo/Medio/Alto por estilo: Lager, APA, NEIPA).

## Campos opcionales
- Market snapshot (usar plantilla TEMPLATE_MARKET_SNAPSHOT.md).
- Referencias a COA o specs.

## Validación
- Usar TEMPLATE_ITEM.md para nuevos items.
- Build strict: `python -m mkdocs build --strict`.