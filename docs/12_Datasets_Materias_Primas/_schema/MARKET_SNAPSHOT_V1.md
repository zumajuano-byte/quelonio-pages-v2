# MARKET_SNAPSHOT_V1

## Propósito
Referencia temporal para tendencias de mercado, sin precios duros. Útil para planeación cuando no hay datos Excel/Sheets.

## Regla de datos
Excel/Sheets > Biblia > Supuestos.

## Campos mínimos
- fecha: YYYY-MM-DD
- fuente: [proveedor, sitio, etc.]
- moneda: ARS/USD/EUR
- unidad: kg/lote/etc.
- rango o índice: rango_min/rango_max o price_index (1-10)
- confianza: alta|media|baja
- nota: [observaciones]

## No precios exactos obligatorios
Permitir price_index (1–10) o nivel (bajo/medio/alto) si no hay rango.

## Argentina-first
Preferir fuentes locales; importados: usar distribuidor/COA cuando exista.

## Cómo se usa en el sistema
Si hay Excel, se ignora; si no hay, se marca REFERENCIA.