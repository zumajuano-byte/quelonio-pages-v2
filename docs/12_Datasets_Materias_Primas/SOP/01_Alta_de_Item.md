# SOP 01: Alta de Item (Excel-first)

## Propósito
Dar de alta un nuevo ítem/insumo (item) para que pueda usarse en recetas, compras, stock y producción. Enfoque Excel-first: trabajar con item_code; item_id se asigna al ingest en app.

## Alcance
- Cubre: Items de materias primas (malta, lupulo, levadura), packaging, químicos, servicios.
- NO cubre: Recetas, lotes, compras, movimientos de stock (usar SOP específicos para esos).

## Requisitos Previos
- Acceso al Excel 00_CORE_MASTER (hoja ITEMS, según DATA_CONTRACT_EXCEL_V1).
- Campos obligatorios: item_code, name, category, unit, pack_size.
- Regla Excel-first: item_id opcional/vacío (se genera ULID al ingest en app, ver ID_CONVENTION_V1).

## Definiciones
- **item_code**: Código humano estable (ej: ITEM-MALT-PILS-25KG). Único por item.
- **item_id**: ULID inmutable (generado al ingest, no en Excel).
- **uom**: Unidad de medida base (kg, l, bs, u, etc.).
- **familia/categoría**: Clasificación (MALT, HOPS, YEAST, PACK, CHEM, SERVICE).
- **vendor**: Proveedor (opcional, para compras).
- **SKU**: Código del proveedor (opcional, para integración).

## Procedimiento Paso a Paso
1. **Determinar familia/categoría**: Elegir de lista estándar (MALT, HOPS, YEAST, PACK, CHEM, SERVICE). Si nueva, consultar contrato.
2. **Asignar item_code**: Usar convención ITEM-{FAMILIA}-{DESCRIPCION_CORTA}-{UOM/FORMATO}. Ej: ITEM-MALT-PILS-25KG (Pilsen 25kg), ITEM-HOPS-CASC-PELLET-1KG (Cascade pellet 1kg).
3. **Completar campos mínimos**: name (descripción completa), unit (uom base), pack_size (tamaño del pack estándar), densidad (si líquido, opcional), merma/handling (% pérdida, opcional).
4. **Agregar vendor/SKU**: Si aplica, linkear a supplier existente (supplier_code).
5. **Validar unicidad**: Verificar que item_code no existe. Si duplicado, usar alias o modificar descripción.
6. **Validar coherencia**: UOM consistente (ej: kg para sólidos, l para líquidos). pack_size >0.
7. **Marcar estado**: ACTIVE por defecto (si contrato contempla INACTIVE para discontinuados).
8. **Guardar y exportar**: Registrar en Excel; exportar o ingest a app para asignar item_id ULID.

## Controles de Calidad (QC) del Alta
- **Duplicados**: Buscar items similares (ej: Pilsen 25kg vs Pilsen 1kg). Si mismo item, no duplicar.
- **UOM incorrecta**: Verificar unidad base (ej: no kg para líquidos). Corregir antes de guardar.
- **Pack_size inconsistente**: Debe ser positivo y lógico (ej: 25kg para sacos grandes).
- **Items “parecidos”**: Comparar nombres/descripciones. Usar alias si necesario.

## Errores Comunes + Corrección
- **item_code mal formado**: Revisar convención (ITEM-{FAMILIA}-{DESCRIPCION}-{UOM}). Corregir y revalidar.
- **Cambio de nombre sin cambiar code**: Si nombre cambia, evaluar si es alias o nuevo item. Registrar en comentarios.
- **Item discontinuado**: Marcar INACTIVE, no borrar (para trazabilidad histórica).

## Output / Resultado Esperado
El ítem aparece en el maestro y puede referenciarse en recetas/compras/movs. item_id ULID asignado al ingest.

## Checklist Final
- [ ] Familia/categoría correcta.
- [ ] item_code único y bien formado.
- [ ] Campos obligatorios completos.
- [ ] UOM coherente.
- [ ] No duplicados.
- [ ] Exportado/ingestado a app.

## Links
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)
- [Excel Workflow Overview](../_schema/EXCEL_WORKFLOW_OVERVIEW.md)