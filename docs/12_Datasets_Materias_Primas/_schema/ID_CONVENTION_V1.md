# ID_CONVENTION_V1

## Alcance y Propósito
Estos IDs aplican a Excel operativo, futuros imports/exports y futura WebApp/DB. Aseguran unicidad, trazabilidad e integridad de datos cerveceros sin depender de orden o posición.

## Dos Identificadores por Entidad
- ***_id** (técnico): ULID (recomendado) o UUIDv4 (alternativa documentada). Inmutable, generado automáticamente.
- ***_code** (humano): Código legible y estable para operaciones diarias.

Ambos únicos; *_id para relaciones técnicas, *_code para humanos.

## Decisión Principal (Recomendada)
Estándar v1: usar ULID para *_id.
- Reglas: *_id inmutable (nunca editar). *_code estable; evolucionar solo con reglas (registrar alias si aplica).

## Formato de *_code (Human Code)
Convención por entidad:
- item_code: ITEM-{FAMILIA}-{ESPECIFICACION} (ej: ITEM-MALT-PILS-25KG)
- recipe_code: REC-{ESTILO}-{NNN} (ej: REC-IPA-001)
- batch_code: BATCH-{YYYYMMDD}-{NN} (ej: BATCH-20260108-01)
- vendor_code/customer_code/location_code: Simples y estables (ej: VENDOR-CIBART, CUSTOMER-BARX)

## Dónde se Generan los IDs
- En Excel MVP: *_id al alta (macro asistida o script; evitar fórmulas). *_code ingresado o autogenerado bajo reglas.
- En WebApp futura: *_id en backend al crear. *_code validado por unicidad.

## Validaciones y Unicidad
- *_id único global (ULID/UUID garantiza).
- *_code único dentro entidad (ej: recipe_code único en RECIPES).
- No IDs basados en fila (ej: ROW()).
- No recalcular por ordenamiento.

## Versionado / Cambios
- recipe_version_id: ULID por versión.
- Cambios: No mutar versión vieja; crear nueva vinculada.
- Merges/renombres: Mantener *_id; *_code puede aliasar (documentar sin romper referencias).

## Ejemplos Completos
### ITEM
- item_id: 01HQ2V3X4Y5Z6A7B8C9D0E1F2G3H4I5J
- item_code: ITEM-MALT-PILS-25KG
- name: Malta Pilsen 25kg

### RECIPE
- recipe_id: 01HQ2V3X4Y5Z6A7B8C9D0E1F2G3H4I5K
- recipe_code: REC-IPA-001
- version: 1
- recipe_version_id: 01HQ2V3X4Y5Z6A7B8C9D0E1F2G3H4I5L

### BATCH
- batch_id: 01HQ2V3X4Y5Z6A7B8C9D0E1F2G3H4I5M
- batch_code: BATCH-20260108-01
- recipe_id: 01HQ2V3X4Y5Z6A7B8C9D0E1F2G3H4I5K

## Checklist Operativo
- Antes de crear entidad: Generar *_id, asignar *_code, validar unicidad, no editar *_id.
- Al versionar: Nuevo *_id para versión; linkear a original.