# SOP 03: Crear Lote de Producción (Excel-first)

## Propósito
Registrar un lote (batch) ejecutando una receta/versión, con trazabilidad y consumos reales. Enfoque Excel-first: trabajar con batch_code; batch_id se asigna al ingest en app.

## Alcance
- Cubre: Creación del batch, vínculo a recipe_code/versión, parámetros reales, consumos, eventos mínimos.
- NO cubre: Compras, ventas, cierres contables, movimientos de stock (SOP específicos para esos).

## Requisitos Previos
- Receta existente (SOP 2) con recipe_code y versión definida.
- Items existentes (SOP 1) para consumos reales.
- Acceso al Excel 20_PRODUCCION (hojas BATCHES y BATCH_STEPS, según DATA_CONTRACT_EXCEL_V1).
- Regla Excel-first: batch_id opcional/vacío (se genera ULID al ingest). batch_code formato BATCH-{YYYYMMDD}-{NN} (por organización y por día, según CODE_COUNTERS_V1).

## Definiciones
- **batch_code**: Código humano (ej: BATCH-20260108-01). Único por día.
- **brew_day**: Fecha de producción (YYYYMMDD).
- **batch_size_target vs batch_size_actual**: Tamaño planificado vs real (L o hl).
- **yield**: Rendimiento (L envasados / L fermentados).
- **losses**: Pérdidas (L perdidos en proceso).
- **“teórico” vs “real”**: Planificado vs ejecutado.
- **estado del lote**: PLANNED/IN_PROGRESS/FERMENTING/PACKAGED/CLOSED/CANCELLED.

## Procedimiento Paso a Paso
### Preparación (Plan)
1. **Elegir receta + versión**: Buscar recipe_code + version (ej: REC-IPA-001 v1).
2. **Definir brew_day**: Fecha de producción (ej: 20260108).
3. **Asignar batch_code**: Generar BATCH-{brew_day}-{NN} (NN=01,02... del día).
4. **Registrar batch_size_target**: Tamaño planificado (L), efficiency esperada.

### Ejecución (Captura Real)
5. **Registrar batch_size_actual**: Post-boil o pre-fermentación (L).
6. **Capturar OG/FG iniciales**: Gravedad original/final (si aplica).
7. **Registrar levadura y parámetros**: item_code de levadura, pitch rate, temperatura.
8. **Cargar consumos reales por líneas**:
   - item_code, qty, uom, stage (mash/boil/whirlpool/dryhop/fermentation/packaging), timing (minutos/días).
   - Ej: ITEM-MALT-PALE-25KG, 20kg, mash, 60 min.
9. **Registrar eventos mínimos**:
   - Inicio macerado, hervor, enfriado/pitch, dryhop(s), cold crash, transferencia, envasado.
   - Fecha/hora o días desde brew_day.

### Cierre del Lote
10. **Capturar FG/ABV final**: Gravedad final, alcohol estimado.
11. **Calcular yield/losses**: L envasados, pérdidas (%).
12. **Definir estado CLOSED**: Si completado. CANCELLED si abortado (motivo).
13. **Notas de calidad**: Incidencias, defectos, ajustes realizados.
14. **Guardar y exportar**: Registrar en Excel; exportar/ingest a app para asignar batch_id.

## Controles de Calidad (QC)
- **batch_code único por día**: Verificar no existe (o es el siguiente NN).
- **receta/versión referenciadas**: recipe_code/version existentes.
- **consumos reales coherentes**: UOM correcta, etapas/timings lógicas (ej: malta en mash, hops en boil).
- **estados consistentes**: No saltos (ej: PACKAGED sin FERMENTING).
- **“plan” vs “real” separados**: No mezclar campos si el contrato define separación.

## Errores Comunes y Corrección
- **batch_code duplicado**: Verificar contador del día. Corrección: incrementar NN.
- **consumo real con item_code inexistente**: Validar items (SOP 1). Corrección: alta previa.
- **olvidar etapa/timing**: Revisar líneas. Corrección: agregar al cargar.
- **cerrar lote sin volumen final**: Siempre registrar yield. Corrección: estimar y documentar.

## Output Esperado
Lote trazable, listo para mover inventario, generar producto terminado, luego ventas/pagos (SOP futuros). batch_id ULID asignado al ingest.

## Ejemplo Completo
- **recipe_code**: REC-IPA-001 v1
- **batch_code**: BATCH-20260108-01
- **brew_day**: 20260108
- **batch_size_target**: 50 L
- **batch_size_actual**: 48 L (post-boil)
- **yield**: 46 L (envasados)
- **losses**: 2 L (2% pérdida)
- **Consumos reales**:
  - item_code: ITEM-MALT-PALE-25KG, qty: 18, uom: kg, stage: mash, timing: 60 min
  - item_code: ITEM-MALT-PILS-25KG, qty: 5, uom: kg, stage: mash, timing: 60 min
  - item_code: ITEM-HOPS-CASC-PELLET-1KG, qty: 0.15, uom: kg, stage: boil, timing: 60 min
  - item_code: ITEM-HOPS-CASC-PELLET-1KG, qty: 0.08, uom: kg, stage: dryhop, timing: 5 days
  - item_code: ITEM-YEAST-US05-11G, qty: 1, uom: pack, stage: fermentation, timing: 7 days
  - item_code: ITEM-CHEM-GLYCOL-1L, qty: 0.04, uom: l, stage: fermentation, timing: day 3
- **Eventos**: Mash start 08:00, Boil start 12:00, Pitch 16:00, Dryhop day 5, Package day 12.
- **Estado**: CLOSED

## Checklist Rápido
- [ ] recipe_code + versión elegida
- [ ] batch_code asignado (único del día)
- [ ] tamaños/volúmenes registrados (target vs actual)
- [ ] consumos reales cargados (item_code válidos)
- [ ] eventos mínimos registrados
- [ ] cierre documentado (CLOSED o CANCELLED)

## Links
- [SOP 1: Alta de Item](../SOP/01_Alta_de_Item.md)
- [SOP 2: Alta de Receta](../SOP/02_Alta_de_Receta.md)
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)
- [Code Counters V1](../_schema/CODE_COUNTERS_V1.md)