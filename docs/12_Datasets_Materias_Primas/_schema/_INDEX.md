# _INDEX: Schema para Datasets Cerveceros

Punto de entrada único al submódulo _schema. Aquí encuentras contratos, convenciones y plantillas para operar datos cerveceros en Excel y futura WebApp.

## Usar Esto Cuando…
- Crees Excel operativo: revisa contratos y convenciones primero.
- Implementes WebApp: usa IDs, counters y flujos aquí definidos.
- Dudas sobre datos: consulta este índice para el documento correcto.

## Documentos Clave
- [EXCEL_WORKFLOW_OVERVIEW.md](EXCEL_WORKFLOW_OVERVIEW.md): Resumen claro de Biblia vs Excel vs App (leer primero).
- [DATA_CONTRACT_EXCEL_V1.md](DATA_CONTRACT_EXCEL_V1.md): Estructura multi-libro y columnas mínimas.
- [ID_CONVENTION_V1.md](ID_CONVENTION_V1.md): *_id (ULID) vs *_code (correlativo legible).
- [CODE_COUNTERS_V1.md](CODE_COUNTERS_V1.md): Generación atómica de códigos correlativos en backend.
- Excel Pack v1 (workbooks + hojas mínimas): [EXCEL_PACK_V1](EXCEL_PACK_V1.md)
- [MARKET_SNAPSHOT_V1.md](MARKET_SNAPSHOT_V1.md): Esquema para snapshots de mercado (referencia temporal).
- [TEMPLATE_MARKET_SNAPSHOT.md](TEMPLATE_MARKET_SNAPSHOT.md): Plantilla para crear snapshots.

## Nota Operativa
Biblia = cerebro (reglas fijas); Excel = datos reales (mutable por org); App asigna ULIDs al ingest para trazabilidad interna.