# SOP 06: Venta y Cobro (Excel-first)

## Propósito
Registrar una venta (documento) y su cobro, manteniendo trazabilidad y coherencia de stock.

## Alcance
- Cubre: cliente (si aplica), sale (cabecera), sale_lines, pago(s), estado (OPEN/PAID/PARTIAL/CANCELLED).
- NO cubre: facturación fiscal, conciliación bancaria completa, contabilidad.

## Requisitos Previos
- Productos/ítems vendibles definidos (product_code/SKU o item_code de packaging final; formalizar en SOP futuro de “Producto Terminado”).
- Stock disponible de producto terminado (si modelo lo contempla) o registro de salida por venta.
- Acceso al Excel 40_VENTAS_FINANZAS (hojas SALES, SALES_LINES, PAYMENTS, según DATA_CONTRACT_EXCEL_V1).
- Regla Excel-first: sale_code y payment_code se usan en Excel; sale_id / payment_id (ULID) al ingest en app.
- Formatos recomendados: sale_code SALE-{YYYYMM}-{NNNN}, payment_code PAY-{YYYYMM}-{NNNN} (según CODE_COUNTERS_V1).

## Definiciones
- sale (cabecera: cliente, fecha, total, moneda, condiciones), sale_line (líneas: product_code, qty, uom, unit_price), payment (pago: método, monto, fecha, referencia), estado del documento.

## Procedimiento Paso a Paso
### Alta de Venta
1. **Asignar sale_code**: Generar SALE-{YYYYMM}-{NNNN} (ej: SALE-202601-0001).
2. **Identificar cliente**: customer_code existente o nombre/datos básicos.
3. **Cargar cabecera**: sale_date, currency, condiciones (NET7/NET15), notas.
4. **Cargar líneas**:
   - product_code (SKU vendible), qty, uom, unit_price, currency, descuentos/impuestos (si aplica).
5. **Calcular total**: Suma líneas con redondeos si necesarios.

### Impacto en Stock (si aplica)
6. **Registrar movimiento SALIDA**: Por venta, motivo=SALE, referencia=sale_code, qty, uom, ubicación origen.
7. **Validar stock**: Si insuficiente, documentar backorder o ajustar.

### Cobro
8. **Registrar pago(s)**: Vinculado a sale_code.
   - payment_code, payment_date, method (CASH/TRANSFER/CARD/MP), amount, currency, reference (comprobante).
9. **Actualizar estado**:
   - OPEN (sin cobro), PARTIAL (parcial), PAID (total), CANCELLED (anulada).

### Cierre
10. **Confirmar saldo**: Para PAID, pagos suman = total.
11. **Notas**: Incidencias, devoluciones futuras.
12. **Guardar y exportar**: Registrar en Excel; exportar/ingest a app para asignar sale_id/payment_id.

## Controles de Calidad (QC)
- sale_code único por mes.
- líneas con qty>0, moneda definida.
- pagos suman <= total (o documentar excedente).
- estado consistente con pagos.
- reconciliación venta↔movimiento stock (si aplica).

## Errores Comunes y Corrección
- Venta sin pago marcada PAID: Corregir estado o agregar pago.
- Pago sin referencia a venta: Vincular o crear venta dummy.
- Doble salida de stock: Revisar movimientos duplicados.
- Cancelar venta sin revertir stock: Crear movimiento ENTRADA reverso.

## Output Esperado
Venta trazable + pagos registrados + stock coherente.

## Ejemplo Simple
- **sale_code**: SALE-202601-0001
- **customer**: BARX
- **currency**: ARS
- **Líneas**:
  - product_code: SKU-BOTTLE-500ML-IPA, qty: 24, uom: u, unit_price: 300
  - product_code: SKU-BOTTLE-500ML-LAGER, qty: 12, uom: u, unit_price: 280
- **Total**: 24*300 + 12*280 = 7200 + 3360 = 10560 ARS
- **Pagos**:
  - payment_code: PAY-202601-0001, method: TRANSFER, amount: 5000, reference: "Transfer 12345"
  - payment_code: PAY-202601-0002, method: CASH, amount: 5560, reference: "Efectivo"
- **Estado**: PAID
- **Movimiento SALIDA**: motivo: SALE, reference: SALE-202601-0001, qty: 36 u, ubicación: DEP01

## Checklist Rápido
- [ ] sale_code asignado
- [ ] líneas completas
- [ ] total calculado
- [ ] movimiento stock (si corresponde)
- [ ] pago(s) registrados
- [ ] estado final consistente

## Links
- [SOP 4: Compras y Alta de Stock](../SOP/04_Compras_y_Alta_de_Stock.md)
- [SOP 5: Consumo y Movimientos de Stock](../SOP/05_Consumo_y_Movimientos_de_Stock.md)
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)
- [Code Counters V1](../_schema/CODE_COUNTERS_V1.md)