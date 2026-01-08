# SOP 02: Alta de Receta (Excel-first)

## Propósito
Dar de alta una receta para diseño, costos teóricos y posterior ejecución de producción. Enfoque Excel-first: trabajar con recipe_code; recipe_id y recipe_version_id se asignan al ingest en app.

## Alcance
- Cubre: Receta base + versión, specs objetivo, lista de ingredientes por item_code.
- NO cubre: Creación de lote (SOP 3), compras/stock, items no dados de alta (usar SOP 1).

## Requisitos Previos
- Items ya dados de alta (SOP 1) con item_code válido.
- Acceso al Excel 10_RECETAS (hojas RECIPES y RECIPE_INGREDIENTS, según DATA_CONTRACT_EXCEL_V1).
- Campos obligatorios: recipe_code, name, style, version, batch_size_target.
- Regla Excel-first: recipe_id y recipe_version_id opcionales/vacíos (se generan ULID al ingest). Cambios => nueva versión (no editar anterior).

## Definiciones
- **recipe_code**: Código humano (ej: REC-IPA-001). Único por receta.
- **version**: Número entero (1,2,3...) o fecha (YYYYMMDD). Nueva versión para cambios.
- **recipe_id/recipe_version_id**: ULID inmutables (generados al ingest).
- **batch_size_target**: Tamaño objetivo del lote (l, hl).
- **specs objetivo**: OG/FG/IBU/SRM/ABV + tolerancias.
- **ingredientes**: Por líneas: item_code, qty, uom, stage, timing.

## Procedimiento Paso a Paso
1. **Elegir familia/estilo**: Definir estilo (ej: IPA, Lager) y asignar recipe_code (REC-{ESTILO}-{NNN}). Ej: REC-IPA-001.
2. **Crear versión inicial**: Setear version=1. Para cambios futuros: nueva versión (incrementar número o usar fecha).
3. **Completar metadata mínima**: name (descripción), style, batch_size_target, efficiency (rendimiento %), notes (opcional).
4. **Setear specs objetivo**: OG/FG/IBU/SRM/ABV + tolerancias (±%). Opcional pero recomendado para validación.
5. **Cargar ingredientes por líneas**: Por cada línea:
   - item_code (de items existentes)
   - qty (cantidad)
   - uom (unidad consistente con item)
   - stage (mash/boil/whirlpool/dryhop/fermentation/packaging)
   - timing (minutos/días si aplica, ej: 60 min boil)
6. **Validar unicidad**: recipe_code único. Si versión nueva, confirmar código base.
7. **Validar coherencia**: item_code existe, uom correcta, stages/timings lógicos (ej: hops en boil/dryhop, yeast en fermentation).
8. **Calcular balances básicos**: Suma de fermentables/masas razonable, IBU/SRM estimados si formulas disponibles.
9. **Marcar estado**: ACTIVE. Para discontinuar: marcar INACTIVE, no borrar.
10. **Guardar y exportar**: Registrar en Excel; exportar/ingest a app para asignar recipe_id y recipe_version_id.

## Controles de Calidad (QC)
- **Duplicados de recipe_code**: Verificar no existe (o es versión nueva).
- **Ingredientes inválidos**: item_code no existe o uom incorrecta.
- **Stages/timings mal asignados**: Ej: malta en boil, hops en mash.
- **Cambio sin versionar**: Siempre nueva versión para edits (no sobreescribir v1).

## Errores Comunes y Corrección
- **Cambiar receta editando v1**: NO. Crear v2 nueva. Corrección: duplicar hoja y editar como nueva versión.
- **Copiar/pegar rompiendo item_code**: Usar lookup o validar manualmente. Corrección: revisar líneas una por una.
- **Hops mal ubicados**: Ej: dryhop en boil. Corrección: mover a stage correcto y ajustar timing.

## Output Esperado
Receta lista para costeo teórico y para crear lote (SOP 3). Versión inmutable para trazabilidad histórica.

## Ejemplos
### Receta Simple (IPA v1)
- recipe_code: REC-IPA-001
- version: 1
- name: IPA Clásica
- style: IPA
- batch_size_target: 50 l
- specs: OG 1.065, FG 1.015, IBU 60, SRM 10, ABV 6.5%
- Ingredientes:
  - item_code: ITEM-MALT-PALE-25KG, qty: 20, uom: kg, stage: mash, timing: 60 min
  - item_code: ITEM-HOPS-CASC-PELLET-1KG, qty: 0.2, uom: kg, stage: boil, timing: 60 min
  - item_code: ITEM-HOPS-CASC-PELLET-1KG, qty: 0.1, uom: kg, stage: dryhop, timing: 5 days
  - item_code: ITEM-YEAST-US05-11G, qty: 1, uom: pack, stage: fermentation, timing: 7 days
  - item_code: ITEM-CHEM-GLYCOL-1L, qty: 0.05, uom: l, stage: fermentation, timing: day 3

### Versionado (v1 → v2)
- v1: REC-IPA-001 con IBU 60.
- Cambiar: +10 IBU con más hops.
- v2: REC-IPA-001 (mismo código base), version=2, agregar línea extra de hops en boil.

## Checklist Rápido
- [ ] recipe_code único y bien formado.
- [ ] Versión nueva si edit.
- [ ] Ingredientes por item_code válidos.
- [ ] Stages/timings correctos.
- [ ] Specs objetivo definidas.
- [ ] Exportado/ingestado a app.

## Links
- [SOP 1: Alta de Item](../SOP/01_Alta_de_Item.md)
- [Schema Index](../_schema/_INDEX.md)
- [Data Contract Excel V1](../_schema/DATA_CONTRACT_EXCEL_V1.md)
- [ID Convention V1](../_schema/ID_CONVENTION_V1.md)