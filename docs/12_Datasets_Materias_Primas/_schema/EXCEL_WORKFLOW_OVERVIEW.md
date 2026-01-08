# EXCEL_WORKFLOW_OVERVIEW

## Qué es la Biblia vs qué es el Excel
- Biblia: cerebro del sistema. Contiene reglas, contratos, plantillas y esquemas para operar cervecería.
- Excel: herramienta operativa para datos reales. Usa contratos de la Biblia para estructurar info diaria (cuando no hay WebApp).
- Diferencia: Biblia es fija y canónica; Excel es mutable y específico por org.

## Componentes del Sistema
- [DATA_CONTRACT_EXCEL_V1.md](DATA_CONTRACT_EXCEL_V1.md): Estructura multi-libro (00_CORE_MASTER, 10_RECETAS, etc.) y columnas mínimas por hoja.
- [ID_CONVENTION_V1.md](ID_CONVENTION_V1.md): *_id (ULID, inmutable) vs *_code (correlativo legible). Excel-first: codes ahora, ULIDs al ingerir en app.
- [CODE_COUNTERS_V1.md](CODE_COUNTERS_V1.md): Generación atómica de correlativos en backend (scoping por org/día/mes).

## Flujo “Excel-first” (Paso a Paso)
1. Usuario crea/edita registros en Excel usando *_code (correlativo, ej: REC-IPA-001).
2. No genera *_id en Excel (opcional/vacío).
3. Exporta Excel o ingesta a WebApp.
4. WebApp asigna ULIDs únicos como *_id para relaciones internas.
5. WebApp genera/valida *_code correlativo via counters (atómico, por scope).
6. WebApp mantiene mapeo *_code ↔ *_id para trazabilidad.
7. Relacionamiento interno por *_id; exports usan *_code para legibilidad humana.
8. Si edición en Excel, re-importar valida y actualiza sin romper *_id.

## Qué NO Hacer
- No fórmulas con links entre workbooks para operar.
- No IDs basados en número de fila.
- No “reusar” correlativos de registros eliminados.

## Mini Glosario
- ULID: Identificador único global (como UUID, pero ordenable por tiempo).
- *_id: Técnico, inmutable (ej: 01HQ2V3X...).
- *_code: Legible, correlativo (ej: REC-IPA-001).
- counter_key: Clave para scoping (ej: "batch:20260108").
- scope: Alcance del contador (org, día, mes).
- ingest/import: Carga de Excel a WebApp.

## Checklist de Arranque
- Antes de crear Excel real: Revisar contrato + convención IDs + counters.
- Probar flujo: Crear registro en Excel → Importar → Verificar *_id y *_code generados.