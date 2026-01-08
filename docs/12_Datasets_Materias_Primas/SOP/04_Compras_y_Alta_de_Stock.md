# SOP 04: Compras y Alta de Stock (Excel-first)

## Propósito
Registrar una compra y reflejar el ingreso a stock con trazabilidad y costos (Excel-first).

## Alcance
- Cubre: alta de proveedor (si aplica), orden/compra, recepción, movimiento de inventario (entrada), costo unitario y moneda.
- NO cubre: pago (SOP 6), ventas, producción (ya cubierto en SOP 3).

## Requisitos Previos
- Items dados de alta (SOP 1) con item_code.
- Ubicación/depósito definido (si el contrato lo contempla).
- Acceso al Excel 30_INVENTARIO_COMPRAS (hojas PURCHASES, PURCHASE_LINES, INVENTORY_MOVEMENTS, según DATA_CONTRACT_EXCEL_V1).
- Regla Excel-first: purchase_id / inv_move_id opcionales/vacíos (se generan ULID al ingest). purchase_code formato PUR-{YYYYMM}-{NNNN} (por organización y mes, según CODE_COUNTERS_V1).

## Definiciones
- purchase (cabecera: proveedor, fecha, moneda, total), purchase_line (líneas: item_code, qty, uom, unit_price), recepción parcial (received_qty < qty), vendor_lot (lote proveedor), fecha de recepción, unit_cost_final (costo real), impuestos/flete (prorrateo opcional), location (ubicación).

## Procedimiento Paso a Paso
### Preparación
1. **Confirmar item_code y UOM**: Verificar item existe (SOP 1) y UOM base.
2. **Confirmar proveedor y moneda**: Elegir vendor existente o alta básica (supplier_code).

### Registrar Compra
3. **Crear purchase_code**: Generar PUR-{YYYYMM}-{NNNN} (ej: PUR-202601-0001).
4. **Cargar cabecera**: vendor_code, purchase_date, currency, notas.
5. **Cargar líneas**: Por cada línea:
   - item_code, qty, uom, unit_price, currency, taxes (si aplica), notes (vendor_lot, vencimiento).

### Recepción
6. **Registrar recepción**: Por línea, received_qty (<= qty), received_date, location.
7. **Actualizar estado**: Si received_qty < qty, marcar PARTIAL; si = qty, RECEIVED.

### Alta de Stock (Movimiento)
8. **Crear movimiento ENTRADA**: Por cada línea recibida:
   - inv_move_type = "IN", item_code, received_qty, uom, location, move_date.
   - Calcular unit_cost_final: unit_price + prorrateo taxes/flete (si se usa; opcional en MVP).
9. **Registrar costos**: En movimiento o cabecera, unit_cost_final para costeo futuro.

### Cierre
10. **Marcar compra cerrada**: RECEIVED si completo, PARTIAL si incompleto, CANCELLED si abortado.
11. **Validar stock actualizado**: Verificar inventory_qty aumentó correctamente.

## Controles de Calidad (QC)
- item_code existe y UOM coherente.
- qty, received_qty, unit_price >0; currency definida.
- No duplicar movimientos (una recepción = un movimiento ENTRADA).
- location presente si contrato la exige.
- purchase_code único por mes.

## Errores Comunes y Corrección
- **Duplicar stock**: Registrar recepción y luego movimiento extra. Corrección: revisar movimientos y eliminar duplicado.
- **Costos sin moneda**: Olvidar currency. Corrección: agregar y recalcular.
- **UOM inconsistente**: Comprar "bolsa 25kg" pero base "kg". Corrección: convertir explícitamente.
- **Olvidar vendor_lot**: En insumos sensibles. Corrección: agregar a notes.

## Output Esperado
Compra registrada y stock disponible para consumos reales en SOP 3, costeo posterior, auditorías.

## Ejemplo Simple
- **purchase_code**: PUR-202601-0001
- **vendor_code**: VENDOR-CIBART
- **currency**: ARS
- **Líneas**:
  - item_code: ITEM-MALT-PILS-25KG, qty: 100, uom: bolsa, unit_price: 32000, received_qty: 80, received_date: 20260110, location: DEP01, unit_cost_final: 32000
  - item_code: ITEM-HOPS-CASC-PELLET-1KG, qty: 20, uom: kg, unit_price: 1500, received_qty: 0 (parcial), received_date: null, location: null
- **Movimiento ENTRADA**: item_code ITEM-MALT-PILS-25KG, qty: 80, uom: bolsa, location: DEP01, unit_cost_final: 32000
- **Estado**: PARTIAL (segunda línea pendiente).

## Checklist Rápido
- [ ] purchase registrado (cabecera + líneas)
- [ ] recepción completa o parcial
- [ ] movimiento ENTRADA creado
- [ ] costos y moneda correctos
- [ ] estado final actualizado

## Links
- [SOP 1: Alta de Item](../SOP/01_Alta_de_Item.md)
- [SOP 3: Crear Lote](../SOP/03_Crear_Lote_de_Produccion.md)
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)
- [Code Counters V1](../_schema/CODE_COUNTERS_V1.md)