# SOP 05: Consumo y Movimientos de Stock (Excel-first)

## Propósito
Registrar salidas/ajustes de inventario vinculados a producción para mantener stock real y trazabilidad.

## Alcance
- Cubre: movimientos de salida por consumo de lote, ajustes por merma, devoluciones, transferencias entre ubicaciones (si aplica).
- NO cubre: compras (SOP 4), ventas (SOP 6+), contabilidad.

## Requisitos Previos
- Lote creado (SOP 3) con batch_code y consumos reales.
- Stock ingresado (SOP 4) con ubicaciones definidas (si el contrato lo contempla).
- Acceso al Excel 30_INVENTARIO_COMPRAS (hoja INVENTORY_MOVEMENTS, según DATA_CONTRACT_EXCEL_V1).
- Regla Excel-first: se opera con batch_code + item_code; inv_move_id se asigna al ingest en app.

## Definiciones
- movimiento (OUT/SALIDA, ADJUSTMENT/AJUSTE, TRANSFER/TRANSFERENCIA)
- motivo (PRODUCTION_CONSUMPTION, LOSS/MERMA, ADJUSTMENT, TRANSFER)
- ubicación origen/destino
- stock_on_hand (existencia actual) y reservado (si aplica)

## Principios Operativos
- Fuente de verdad del consumo: registros reales del lote (SOP 3) + reflejo en movimientos.
- Evitar doble registro: no descontar stock dos veces.
- Un movimiento debe tener: fecha, motivo, item_code, qty, uom, referencia (batch_code), ubicación.

## Procedimiento Paso a Paso
### Salida por Consumo de Lote
1. **Identificar lote**: Buscar batch_code (ej: BATCH-20260108-01).
2. **Tomar consumos del lote**: Revisar líneas de consumo real en el lote (item_code, qty, uom, etapa).
3. **Consolidar por item_code+uom**: Suma total por ítem si etapa no es crítica (o mantener granular por etapa).
4. **Crear movimiento SALIDA**:
   - fecha, motivo=PRODUCTION_CONSUMPTION, batch_code, item_code, qty, uom, ubicación origen.
5. **Validar stock disponible**: Si stock_on_hand < qty, registrar ajuste y marcar inconsistencia (nota: stock negativo temporal).

### Ajustes / Mermas
6. **Registrar pérdidas**: Si derrames, vencimiento, roturas:
   - movimiento tipo ADJUSTMENT, motivo=LOSS, item_code, qty negativa, nota explicativa.

### Transferencias (si aplica)
7. **Mover entre ubicaciones**: movimiento tipo TRANSFER, origen/destino, qty igual.

### Verificación Final
8. **Recalcular stock_on_hand**: Actualizar existencia.
9. **Revisar críticos**: Top 5 ítems (malta base, lúpulo, levadura) para coherencia.
10. **Reconciliación lote**: Suma consumos del lote = suma salidas por lote (por item_code).

## Controles de Calidad (QC)
- batch_code obligatorio en consumos de producción.
- item_code existe y uom coherente.
- no movimientos sin motivo.
- no salidas sin ubicación origen (si contrato exige).
- reconciliación lote↔movimientos por ítem.

## Errores Comunes y Corrección
- **Doble descuento**: Consumir lote + salida duplicada. Corrección: revisar movimientos y eliminar duplicado.
- **Consumir ítem no en stock**: Proceder: registrar compra atrasada o ajuste. Corrección: agregar entrada previa.
- **UOM equivocada**: kg vs g. Corrección: convertir y revalidar.
- **Lote cancelado**: Revertir movimientos (movimiento positivo o reversal).

## Output Esperado
Inventario actualizado y trazable por lote.

## Ejemplo Simple
- **batch_code**: BATCH-20260108-01
- **Movimientos de salida (consumo)**:
  - motivo: PRODUCTION_CONSUMPTION, batch_code: BATCH-20260108-01, item_code: ITEM-MALT-PALE-25KG, qty: 18, uom: kg, ubicación: DEP01
  - motivo: PRODUCTION_CONSUMPTION, batch_code: BATCH-20260108-01, item_code: ITEM-HOPS-CASC-PELLET-1KG, qty: 0.15, uom: kg, ubicación: DEP01
  - motivo: PRODUCTION_CONSUMPTION, batch_code: BATCH-20260108-01, item_code: ITEM-YEAST-US05-11G, qty: 1, uom: pack, ubicación: DEP01
- **Ajuste por merma**: motivo: LOSS, item_code: ITEM-MALT-PALE-25KG, qty: 2, uom: kg, ubicación: DEP01, nota: derrame en mash
- **Resultado**: Stock actualizado, lote trazable.

## Checklist Rápido
- [ ] lote identificado con consumos
- [ ] salidas por consumo registradas
- [ ] ajustes/mermas documentados
- [ ] reconciliación lote↔movimientos OK
- [ ] stock actualizado

## Links
- [SOP 3: Crear Lote](../SOP/03_Crear_Lote_de_Produccion.md)
- [SOP 4: Compras y Alta de Stock](../SOP/04_Compras_y_Alta_de_Stock.md)
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)