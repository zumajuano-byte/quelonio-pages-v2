# ASISTENTE — Data Contract Brew OS (v0.1)

Este contrato define qué entidades y campos mínimos deben existir en Brew OS para que el asistente opere sin inventar datos.
Es un stub: se completa a medida que PROYECTO_WEB_API avance.

Regla: si un campo no existe, el asistente:
1) lo pide como input al usuario, o
2) propone crearlo en Brew OS en el sprint correspondiente.

---

## 1) Entidades (canónicas)

### Organization (org)
Campos mínimos:
- org_id
- name
- timezone
- units_system (metric/imperial)
- default_currency

### User
Campos mínimos:
- user_id
- org_id
- role (Owner/Admin/Produccion/Ventas/Lectura)
- name
- email

### Ingredient (insumo)
Campos mínimos:
- ingredient_id
- org_id
- type (malt/hop/yeast/water_additive/adjunct/packaging)
- name
- supplier (opcional)
- cost_per_unit
- unit (kg/g/L/unidad)
- attributes (JSON) (p.ej. AA% en lupulo, EBC en malta, atenuacion/cepa en levadura)

### Recipe
Campos mínimos:
- recipe_id
- org_id
- name
- style
- target_volume
- targets (OG/FG/ABV/IBU/color/CO2)
- process_profile_id (opcional)
- notes

### RecipeItem (BOM)
Campos mínimos:
- recipe_item_id
- recipe_id
- ingredient_id
- amount
- unit
- timing (si aplica: mash/boil/whirlpool/dryhop)
- notes

### Batch (lote)
Campos mínimos:
- batch_id
- org_id
- recipe_id
- planned_volume / actual_volume
- start_date
- status (planned/active/conditioning/packaging/closed)
- equipment_id (opcional)
- notes

### BatchMeasurement
Campos mínimos:
- measurement_id
- batch_id
- timestamp
- type (gravity/temp/pH/DO/TPO/CO2)
- value
- unit
- method (opcional)
- notes

### InventoryLot (stock)
Campos mínimos:
- inventory_lot_id
- org_id
- ingredient_id
- qty_on_hand
- unit
- location
- lot_code (opcional)
- expiry_date (opcional)
- cost_basis (opcional)

### SKU (producto final)
Campos mínimos:
- sku_id
- org_id
- name
- package_type (can/bottle/keg)
- volume_per_unit
- units_per_case (opcional)
- cost_packaging (opcional)

### PackagingRun (corrida de envasado)
Campos mínimos:
- packaging_run_id
- batch_id
- sku_id
- date
- qty_produced
- losses
- notes
- o2_controls (JSON) (purga linea/envase, tiempos, incidentes)

### Sale (AR)
Campos mínimos:
- sale_id
- org_id
- date
- customer
- items (sku_id, qty, price)
- payment_status

### Purchase (AP)
Campos mínimos:
- purchase_id
- org_id
- date
- supplier
- items (ingredient_id, qty, price)
- payment_status

### AuditLog
Campos mínimos:
- audit_id
- org_id
- user_id
- timestamp
- action
- entity_type
- entity_id
- diff (JSON)
- prompt_context (JSON) (si aplica al asistente)

---

## 2) Campos “obligatorios” por intent

### Intent A (Receta)
Necesita:
- Recipe + RecipeItems
- Ingredients (con atributos basicos)
- Targets definidos (o aprobados)
Si falta: el asistente propone baseline y marca “pendiente de aprobación”.

### Intent B (Proceso)
Necesita:
- Batch + status
- Equipment/capacidad (si existe) o input manual
- Plan de hitos (puede vivir en notas inicialmente)

### Intent C (QA/QC)
Necesita:
- BatchMeasurements (min densidad/temp/pH)
- PackagingRun (si paso por empaque)
Si falta medición: el asistente pide dato o crea tarea en checklist.

### Intent E (Uso del sistema)
Necesita:
- Roles + permisos
- Entidades mínimas por modulo

---

## 3) Reglas de no-invención (asistente)
- Si el dato es de sistema y falta: pedirlo o marcarlo como “GAP”.
- Si el dato es técnico y no está en Biblia: marcar “Sin cita canónica” y proponer completar BIBLIO.
- Nunca inferir costos, volúmenes, AA%, EBC, etc. sin fuente o input.

---

## 4) Checklist de preparación (antes de integrar IA real)
- [ ] Knowledge Map v1.0 operativo (este doc)
- [ ] Contratos de salida estables (ASISTENTE_CONTRATOS)
- [ ] Data Contract al menos para Recipe/Batch/Inventory/SKU/PackagingRun
- [ ] Auditoría definida (AuditLog)
