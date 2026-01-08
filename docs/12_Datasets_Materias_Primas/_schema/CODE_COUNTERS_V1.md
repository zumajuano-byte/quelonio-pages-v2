# CODE_COUNTERS_V1

## Propósito
Definir generación de *_code correlativos en backend (no en Excel). Asegura unicidad, legibilidad y evitación de colisiones para entidades operativas.

## Entidades con Código Correlativo (v1)
- recipe_code: REC-{FAMILIA}-{NNN} (ej: REC-IPA-001)
- batch_code: BATCH-{YYYYMMDD}-{NN} (ej: BATCH-20260108-01)
- sale_code: SALE-{YYYYMM}-{NNNN} (ej: SALE-202601-0001)
- purchase_code: PUR-{YYYYMM}-{NNNN} (ej: PUR-202601-0001)
- payment_code: PAY-{YYYYMM}-{NNNN} (ej: PAY-202601-0001)

No correlativo: item_code (semántico, ej: ITEM-MALT-PILS-25KG), vendor_code, customer_code (estables, manuales).

## Alcance del Contador (Scoping)
- Base: Por organization_id (evita colisiones multi-org).
- batch_code: Además por día (YYYYMMDD) dentro de org (reinicio diario, legibilidad).
- sale_code/purchase_code/payment_code: Por mes (YYYYMM) dentro de org (reinicio mensual, control financiero).

## Reglas de Unicidad y Formato
- Padding: NNN (3 dígitos, ej: 001), NNNN (4 dígitos, ej: 0001).
- No reutilizar números (incluso si borrado/rollback).
- Reinicio por período: batch por día, ventas por mes.

## Concurrencia
Atómico: Transacción + lock/unique constraint. Reintentar si colisión.

## Tabla/Registro Conceptual de Counters
Campos conceptuales (para futura tabla DB):
- organization_id
- counter_key (ej: "recipe", "batch:20260108", "sale:202601")
- next_value (integer)
- updated_at

Nota: Mapeará a Prisma en WebApp.

## Ejemplos
- recipe_code: REC-IPA-001, REC-IPA-002
- batch_code: BATCH-20260108-01, BATCH-20260108-02
- sale_code: SALE-202601-0001, SALE-202601-0002
- purchase_code: PUR-202601-0001, PUR-202601-0002
- payment_code: PAY-202601-0001, PAY-202601-0002

## Checklist
Antes de emitir un code: Identificar scope, leer/incrementar counter atómico, formatear, validar unicidad.