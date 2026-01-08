# DATA_CONTRACT_EXCEL_V1

## Propósito
Definir contrato operativo para gestión de datos cerveceros en Excel multi-libro. Modelo orientado a integridad, trazabilidad y separación de responsabilidades. No incluye archivos .xlsx físicos.

## Modelo Multi-Libro
- **00_CORE_MASTER**: Repositorio central de entidades base (items, proveedores, clientes). Fuente de verdad para sincronización.
- **10_RECETAS**: Formulación y specs de recetas.
- **20_PRODUCCION**: Registros de lotes y procesos de producción.
- **30_INVENTARIO_COMPRAS**: Gestión de stock y adquisiciones.
- **40_VENTAS_FINANZAS**: Ventas, costos y análisis financiero.
- **50_QA_QC** (opcional): Control de calidad y auditorías (si no se maneja en 20_PRODUCCION).

Cada libro es un archivo .xlsx independiente. No compartir fórmulas entre libros para operación diaria.

## Convención de IDs
- ***_id**: Identificador técnico único (UUID o ULID, generado automáticamente). Nunca editable por el usuario. Usado para relaciones y sincronización.
- ***_code**: Código humano-legible (ej. REC-001, ITEM-ABC, BATCH-20240101). Editable por usuario, pero único dentro de su tipo.
- Regla: El usuario nunca edita *_id. Si se copia data, preservar *_id para integridad.

Ejemplo breve:
- Receta: recipe_id = "uuid-1234-abcd", recipe_code = "REC-IPA001"
- Item: item_id = "uuid-5678-efgh", item_code = "ITEM-MALTA_PILSEN"
- Lote: batch_id = "uuid-9999-ijkl", batch_code = "BATCH-20240101-001"

## Tablas por Libro (Hojas y Columnas Mínimas)
### 00_CORE_MASTER
- **ITEMS** (Materias primas, insumos):
  - item_id, item_code, name, category (malta/lupulo/levadura/etc.), unit (kg/l/bs), supplier_id, created_at, updated_at
- **SUPPLIERS** (Proveedores):
  - supplier_id, supplier_code, name, contact, address, created_at, updated_at
- **CUSTOMERS** (Clientes):
  - customer_id, customer_code, name, contact, address, created_at, updated_at

### 10_RECETAS
- **RECIPES** (Recetas base):
  - recipe_id, recipe_code, name, style, version, created_by, created_at, updated_at
- **RECIPE_INGREDIENTS** (Ingredientes por receta):
  - recipe_ingredient_id, recipe_id, item_id, quantity, unit, stage (mash/boil/etc.), created_at

### 20_PRODUCCION
- **BATCHES** (Lotes de producción):
  - batch_id, batch_code, recipe_id, brew_date, volume_liters, status (planned/brewing/fermenting/etc.), created_at, updated_at
- **BATCH_STEPS** (Pasos del lote):
  - batch_step_id, batch_id, step_name, start_time, end_time, notes, created_at

### 30_INVENTARIO_COMPRAS
- **INVENTORY** (Stock actual):
  - inventory_id, item_id, location, quantity_on_hand, unit, last_updated
- **PURCHASE_ORDERS** (Órdenes de compra):
  - po_id, po_code, supplier_id, item_id, quantity, unit, order_date, expected_delivery, status

### 40_VENTAS_FINANZAS
- **SALES** (Ventas):
  - sale_id, sale_code, customer_id, batch_id, quantity_sold, unit, sale_date, price_per_unit, total
- **COSTS** (Costos por lote):
  - cost_id, batch_id, item_id, quantity_used, unit, cost_per_unit, total_cost, date

### 50_QA_QC (Opcional)
- **QC_TESTS** (Pruebas de calidad):
  - qc_id, batch_id, test_type, result, date, notes
- **INCIDENTS** (Incidencias):
  - incident_id, incident_code, batch_id, description, severity, date, resolution

## Reglas NO-HACER
- Prohibidos links externos por fórmulas entre workbooks para operación diaria (ej. =[OtroLibro.xlsx]Hoja!A1). Usar solo para excepcionales.
- No usar IDs basados en fila (ej. ROW() o números secuenciales editables). Siempre *_id técnico inmutable.
- No editar *_id manualmente. Si se corrige, regenerar nuevo *_id.
- No mezclar responsabilidades: un libro por dominio.

## Modo de Sincronización Recomendado
- Desde 00_CORE_MASTER hacia otros libros: Usar Power Query (Get Data > From Workbook) para importar tablas base (ITEMS, SUPPLIERS) como consultas. Refrescar manualmente o programado.
- Alternativa: Copia controlada (copy-paste valores) desde 00_CORE_MASTER a otros libros, preservando *_id.
- Evitar VLOOKUP entre libros; preferir importar data completa.
- Frecuencia: Diaria/semanal según operación. Documentar cambios en changelog por libro.