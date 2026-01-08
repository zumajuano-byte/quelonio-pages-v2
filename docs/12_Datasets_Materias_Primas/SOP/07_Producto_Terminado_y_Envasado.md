# SOP 07: Producto Terminado y Envasado (Excel-first)

## Propósito
Convertir un lote (beer) en unidades vendibles (producto terminado) mediante un “packaging run” y reflejar stock.

## Alcance
- Cubre: definición de producto/SKU, envasado, rendimientos, mermas, trazabilidad lote→pack→SKU, movimientos de inventario (entrada PT + salida beer a granel).
- NO cubre: ventas/cobros (SOP 6), compras (SOP 4).

## Requisitos Previos
- Lote existente (SOP 3) con batch_code en estado apto para envasar.
- Insumos de packaging dados de alta (SOP 1) y disponibles en stock (SOP 4–5) si se descuentan.
- Acceso al Excel 20_PRODUCCION (hoja PACKAGING_RUNS, según DATA_CONTRACT_EXCEL_V1; si no existe, usar hoja PRODUCT_PACKAGING).
- Regla Excel-first: product_code/SKU y pack_code se usan en Excel; ids ULID al ingest en app.
- Convenciones sugeridas: product_code PROD-{ESTILO}-{FORMATO}-{ML}-{NN} (estable, no correlativo); pack_run_code opcional PACK-{YYYYMMDD}-{NN} (si futuro).

## Definiciones
- Producto terminado (PT), SKU/product_code, packaging run (corrida de envasado), rendimiento (unidades), merma, lote de envasado, fecha de envasado, formato (lata/botella/barril), volumen por unidad.

## Procedimiento Paso a Paso
### Preparación
1. **Seleccionar lote fuente**: Elegir batch_code con estado PACKAGED o FERMENTING apto.
2. **Definir producto/SKU**: Asignar product_code estable (ej: PROD-IPA-CAN-473-01) y formato/volumen por unidad.
3. **Definir objetivos**: Unidades objetivo (target_units), fecha de envasado.

### Registro del Packaging Run
4. **Crear corrida**: pack_run_code opcional (ej: PACK-20260108-01), fecha, batch_code, product_code.
5. **Registrar parámetros**: Volumen total envasado, unidades producidas, unidades rechazadas/merma, notas (DO, CO2, TPO).

### Movimientos de Stock
6. **Salida de beer**: Movimiento SALIDA tipo PACKAGING (referencia pack_run_code/batch_code), qty en volumen o unidades equivalentes.
7. **Entrada de PT**: Movimiento ENTRADA de product_code, qty unidades producidas, ubicación PT.
8. **Packaging materials (opcional)**: Salidas de insumos (latas, tapas) por qty producida + merma.

### Cierre
9. **Validar reconciliación**: Volumen consumido del lote ≈ unidades * vol_unidad + merma.
10. **Marcar corrida COMPLETED**: Estado lote PACKAGED si todo envasado.

## Controles de Calidad (QC)
- product_code definido y estable (no cambiar por lote).
- trazabilidad batch_code→product_code→ventas.
- reconciliación unidades/volúmenes.
- movimientos coherentes (no doble entrada PT).
- mermas documentadas.

## Errores Comunes y Corrección
- Vender sin haber creado PT/stock: Corrección: crear entrada PT retroactiva.
- Envasar sin descontar insumos críticos: Corrección: registrar salidas faltantes.
- Cambiar product_code en corrida: Corrección: mantener código original, documentar alias.
- Confundir unidades producidas vs rechazadas: Corrección: recalcular totales.

## Output Esperado
Stock de PT listo para ventas (SOP 6) con trazabilidad a batch_code.

## Ejemplo Simple
- **batch_code**: BATCH-20260108-01
- **product_code**: PROD-IPA-CAN-473-01
- **packaging run**: PACK-20260108-01, 480 unidades producidas, 12 rechazadas, 473 ml/unidad
- **Movimientos**:
  - SALIDA: motivo PACKAGING, reference PACK-20260108-01, qty 220 l (equivalente a 468 u * 0.473 l/u), ubicación GRANEL
  - ENTRADA: product_code PROD-IPA-CAN-473-01, qty 468 u, ubicación PT
  - Merma: 12 u documentadas en notas (notas: "rechazos por CO2 bajo")

## Checklist Rápido
- [ ] batch_code elegido
- [ ] product_code/SKU definido
- [ ] corrida registrada
- [ ] entrada PT registrada
- [ ] reconciliación OK
- [ ] listo para venta

## Links
- [SOP 3: Crear Lote](../SOP/03_Crear_Lote_de_Produccion.md)
- [SOP 5: Consumo y Movimientos de Stock](../SOP/05_Consumo_y_Movimientos_de_Stock.md)
- [SOP 6: Venta y Cobro](../SOP/06_Venta_y_Cobro.md)
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)