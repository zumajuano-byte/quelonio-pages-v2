# EXCEL_PACK_V1

## Propósito
Especificación del “Excel Pack v1”: modelo multi-workbook para operación cervecera Excel-first. Define archivos .xlsx sugeridos, hojas mínimas y mapeo a contratos/SOPs. NO incluye archivos físicos; usa contratos para columnas.

## Principios
- **Multi-workbook**: Separación por dominio para integridad (ver DATA_CONTRACT_EXCEL_V1).
- **Excel-first**: Codes en Excel, ULIDs al ingest (ver ID_CONVENTION_V1).
- **Fuente**: Contrato + SOPs (no inventar; referenciar).

## Lista de Workbooks (v1)
| Workbook | Alcance | Hojas Mínimas | Propósito |
|----------|---------|---------------|-----------|
| 00_MASTER_CONFIG.xlsx | Configuración global | SETTINGS (parámetros, listas), CURRENCIES (monedas), LOCATIONS (ubicaciones) | Repositorio de settings y listas base. |
| 10_ITEMS_MASTER.xlsx | Items y proveedores | ITEMS, SUPPLIERS, MARKET_SNAPSHOTS (opcional) | Maestro de items, vendors y referencias de mercado. |
| 20_RECIPES.xlsx | Recetas | RECIPES, RECIPE_INGREDIENTS | Formulación y versiones de recetas. |
| 30_PRODUCTION.xlsx | Producción | BATCHES, BATCH_STEPS | Lotes, consumos reales y eventos. |
| 40_INVENTORY.xlsx | Inventario | INVENTORY_MOVEMENTS, INVENTORY_STOCK (opcional derivado) | Movimientos de stock (entradas/salidas/ajustes). |
| 50_SALES.xlsx | Ventas y finanzas | SALES, SALES_LINES, PAYMENTS | Ventas, líneas y cobros. |

## Hojas Mínimas y Campos Clave (Referencia a Contrato)
- **SETTINGS**: parámetros globales (efficiency default, tasas).
- **CURRENCIES**: currency_code, exchange_rate.
- **LOCATIONS**: location_code, description.
- **ITEMS**: item_code, name, category, unit, supplier_id (ver contrato).
- **SUPPLIERS**: supplier_code, name, contact.
- **MARKET_SNAPSHOTS**: item_code, date, min_price, max_price (ver MARKET_SNAPSHOT_V1).
- **RECIPES**: recipe_code, name, style, version, batch_size_target.
- **RECIPE_INGREDIENTS**: recipe_code, item_code, qty, uom, stage.
- **BATCHES**: batch_code, recipe_code, brew_date, batch_size_actual, status.
- **BATCH_STEPS**: batch_code, step_name, start_time, end_time.
- **INVENTORY_MOVEMENTS**: move_date, item_code, qty, uom, move_type (IN/OUT/ADJUST), reference (batch_code/purchase_code).
- **SALES**: sale_code, sale_date, customer, total, currency.
- **SALES_LINES**: sale_code, product_code, qty, unit_price.
- **PAYMENTS**: payment_code, sale_code, amount, method, date.

Campos detallados en DATA_CONTRACT_EXCEL_V1; usar para implementar hojas.

## Identificadores Usados por Workbook
- **item_code**: ITEMS_MASTER (generado Excel).
- **recipe_code**: RECIPES (generado Excel).
- **batch_code**: PRODUCTION (generado Excel, contador diario).
- **purchase_code**: INVENTORY (generado app, contador mensual).
- **sale_code**: SALES (generado app, contador mensual).
- **payment_code**: SALES (generado app, contador mensual).
- **product_code**: SALES (si aplica, generado Excel).
- Donde generar: Ver ID_CONVENTION_V1 y CODE_COUNTERS_V1.

## Mapeo SOP ↔ Workbooks
- **SOP 1 (Alta Item)**: ITEMS_MASTER (ITEMS, SUPPLIERS).
- **SOP 2 (Alta Receta)**: RECIPES (RECIPES, RECIPE_INGREDIENTS).
- **SOP 3 (Crear Lote)**: PRODUCTION (BATCHES, BATCH_STEPS).
- **SOP 4 (Compras/Stock)**: INVENTORY (INVENTORY_MOVEMENTS).
- **SOP 5 (Movimientos Stock)**: INVENTORY (INVENTORY_MOVEMENTS).
- **SOP 6 (Venta/Cobro)**: SALES (SALES, SALES_LINES, PAYMENTS).
- **SOP 7 (Producto Terminado)**: PRODUCTION + INVENTORY (BATCHES + MOVEMENTS).

## Reglas NO-HACER
- No links frágiles entre .xlsx.
- No IDs por fila.
- No borrar historial; usar INACTIVE/CANCELLED.

## Cuándo Crear los .xlsx
Cuando SOPs estén estables, contrato definido y tengas datos iniciales (items/recetas).

## Links
- [_INDEX](../_schema/_INDEX.md)
- [DATA_CONTRACT_EXCEL_V1](DATA_CONTRACT_EXCEL_V1.md)
- [ID_CONVENTION_V1](ID_CONVENTION_V1.md)
- [CODE_COUNTERS_V1](CODE_COUNTERS_V1.md)
- [SOP _INDEX](../SOP/_INDEX.md)