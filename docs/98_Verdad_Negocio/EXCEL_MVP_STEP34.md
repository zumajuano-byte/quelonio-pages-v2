# Excel MVP - Paso 34: Seed Data y CSV Export

## Resumen

Este paso agrega datos demostrativos al Excel MVP y crea funcionalidad para exportar todos los datos a CSV.

## Archivos Generados/Modificados

### 1. tools/build_excel_mvp_step34_seed.py
Script que agrega datos demo consistentes con FKs y catálogos.

**Funcionalidades:**
- Crea backup automático del archivo Excel existente
- Inserta datos demo en 15 hojas de negocio
- Evita duplicados basándose en columnas ID
- Actualiza rangos de tablas automáticamente
- Mantiene todas las estructuras, validaciones y fórmulas existentes

**Datos seedeados:**
- 01_Recetas: 2 recetas (REC-001, REC-002)
- 02_RecetaVersiones: 3 versiones
- 03_Lotes: 2 lotes de producción
- 04_LoteMediciones: (sin datos)
- 05_ItemsInventario: 10 items de inventario
- 06_MovimientosInventario: (sin datos)
- 07_Proveedores: 2 proveedores
- 08_LotesInsumo: 5 lotes de insumo
- 09_ConsumosLote: 10 consumos
- 10_Productos: 2 productos
- 11_Clientes: 3 clientes
- 12_Ventas: 3 ventas
- 13_VentasLineas: 5 líneas de venta
- 14_Pagos: 3 pagos
- 15_FulfillmentVentaLote: 5 registros de fulfillment

### 2. tools/export_excel_csv_pack.py
Script que exporta todas las tablas a archivos CSV.

**Funcionalidades:**
- Exporta 15 hojas de negocio a CSV
- Crea carpeta timestamped en `data/excel/exports/`
- Usa delimitador `;` (semicolón) para Excel ES
- Codificación UTF-8 con quoting estándar
- Solo exporta rango usado (no filas vacías)

**Formato de exportación:**
- Delimitador: `;` (semicolón)
- Quote: `"` (doble comilla)
- Encoding: UTF-8
- Fechas: YYYY-MM-DD
- Headers: incluidos en primera fila

### 3. tools/test_step34.py
Script de test determinista que verifica:
- Existencia del archivo Excel
- Conteo mínimo de filas por tabla
- Integridad de claves foráneas (FKs)
- Existencia del pack de exportación CSV
- Compatibilidad con Pasos 31/32/33

### 4. data/excel/Quelonio_Excel_MVP_Skeleton.xlsx
Archivo Excel actualizado con datos demo.

### 5. data/excel/_backups/
Backups automáticos con timestamp.

### 6. data/excel/exports/STEP34_pack_YYYYMMDD_HHMMSS/
Carpeta con CSVs exportados.

## Cómo Correr

### Generar Seed Data (Paso 34)

```bash
python tools/build_excel_mvp_step34_seed.py
```

Esto:
1. Crea backup en `data/excel/_backups/` con timestamp
2. Carga el Excel existente
3. Agrega datos demo (evitando duplicados)
4. Actualiza rangos de tablas
5. Guarda el archivo

**Importante:** El script es idempotente - puede correrse múltiples veces sin duplicar datos.

### Exportar a CSV

```bash
python tools/export_excel_csv_pack.py
```

Esto:
1. Carga el Excel
2. Exporta cada hoja de negocio a CSV
3. Crea carpeta timestamped en `data/excel/exports/`
4. Imprime resumen de archivos exportados

**Resultado:** Una carpeta con 15 archivos CSV (uno por tabla).

### Ejecutar Tests (Paso 34)

```bash
python tools/test_step34.py
```

Verifica:
- Archivo Excel existe
- Conteos mínimos de filas por tabla
- Integridad de todas las FKs
- Export CSV existe y tiene >= 15 archivos
- Compatibilidad con Pasos 31/32/33

### Ejecutar Tests de Pasos Anteriores

```bash
# Test Paso 31
python tools/test_step31.py

# Test Paso 32
python tools/test_step32.py

# Test Paso 33
python tools/test_step33.py
```

## Detalles de Implementación

### Seed Data

**Consistencia de FKs:**
- Todos los FKs referencian IDs válidos
- Catálogos respetados (estados, tipos, canales)
- Proveedores linkeados correctamente
- Lotes de insumo vinculados a items y proveedores

**IDs Utilizados:**

| Entidad | IDs | Cantidad |
|---------|------|----------|
| Recetas | REC-001, REC-002 | 2 |
| RecetaVersiones | REC-001-V01, REC-001-V02, REC-002-V01 | 3 |
| Productos | PROD-001, PROD-002 | 2 |
| Proveedores | PROV-001, PROV-002 | 2 |
| ItemsInventario | ITEM-001 a ITEM-010 | 10 |
| LotesInsumo | LI-001 a LI-005 | 5 |
| Lotes | LOTE-2026-001, LOTE-2026-002 | 2 |
| ConsumosLote | C-001 a C-010 | 10 |
| Clientes | CLI-001 a CLI-003 | 3 |
| Ventas | VEN-001 a VEN-003 | 3 |
| VentasLineas | VL-001 a VL-005 | 5 |
| FulfillmentVentaLote | FF-001 a FF-005 | 5 |
| Pagos | PAG-001 a PAG-003 | 3 |

**Tipos de Items (del catálogo CAT_ItemTipo):**
- malta: ITEM-001, ITEM-005
- luppulo: ITEM-002, ITEM-009
- levadura: ITEM-003
- agua: ITEM-004
- adjunto: ITEM-005
- quimico: ITEM-006
- envase: ITEM-007, ITEM-010
- etiqueta: ITEM-008

**Estados de Lotes (del catálogo CAT_LoteEstado):**
- LOTE-2026-001: "completado"
- LOTE-2026-002: "maduracion"

**Estados de Pagos (del catálogo CAT_PagoEstado):**
- VEN-001: "pagado"
- VEN-002: "pagado"
- VEN-003: "parcial"

**Tipos de Clientes (del catálogo CAT_ClienteTipo):**
- CLI-001: "bar"
- CLI-002: "minorista"
- CLI-003: "mayorista"

**Canales de Clientes (del catálogo CAT_Canal):**
- CLI-001: "distribucion"
- CLI-002: "taproom"
- CLI-003: "distribucion"

### Export CSV

**Archivos generados:**
```
data/excel/exports/STEP34_pack_YYYYMMDD_HHMMSS/
├── 01_Recetas.csv
├── 02_RecetaVersiones.csv
├── 03_Lotes.csv
├── 04_LoteMediciones.csv
├── 05_ItemsInventario.csv
├── 06_MovimientosInventario.csv
├── 07_Proveedores.csv
├── 08_LotesInsumo.csv
├── 09_ConsumosLote.csv
├── 10_Productos.csv
├── 11_Clientes.csv
├── 12_Ventas.csv
├── 13_VentasLineas.csv
├── 14_Pagos.csv
└── 15_FulfillmentVentaLote.csv
```

**Ejemplo de CSV (01_Recetas.csv):**
```csv
receta_id;nombre;estado;fecha_creacion;notas
REC-001;IPA Clásica;activa;2026-01-01;Receta base IPA con lúpulos Americanos
REC-002;Stout Imperial;activa;2026-01-05;Stout oscura con notas de café
```

## Compatibilidad

### Preservación de Pasos Anteriores

**Paso 31 - Estructura Base:**
- ✅ Todas las 15 tablas originales
- ✅ Headers de todas las tablas (sin cambios)
- ✅ Nombres definidos LIST_*
- ✅ Validaciones de datos originales

**Paso 32 - Funcionalidad Operativa:**
- ✅ Hoja Catalogos
- ✅ Nombres definidos lst_*
- ✅ Columnas calculadas (abv_estimado, total_calc, etc.)
- ✅ Validaciones de datos adicionales

**Paso 33 - UX:**
- ✅ Hoja 00_Home (primera)
- ✅ Hoja 98_Ayuda
- ✅ Preservación total de estructura

**Paso 34 - Seed Data:**
- ✅ Datos demo consistentes
- ✅ Integridad FK completa
- ✅ Respeto a catálogos y validaciones
- ✅ Export CSV funcional

## Resultados de Tests

### test_step34.py: 5/5 PASSED

- ✅ File Exists
- ✅ Min Row Counts (15 tablas)
- ✅ FK Integrity (15 relaciones)
- ✅ CSV Export (>=15 archivos)
- ✅ Steps 31-33 Compatibility

### test_step33.py: 8/8 PASSED

- ✅ File Exists
- ✅ 00_Home First
- ✅ 98_Ayuda Exists
- ✅ Catalogos Exists
- ✅ Step 32 Names (14)
- ✅ Home Hyperlinks (12)
- ✅ Total Sheets (19)
- ✅ Tables Integrity (15)

### test_step32.py: 7/7 PASSED

- ✅ File Exists
- ✅ Catalogos Sheet
- ✅ Catalog Defined Names (6)
- ✅ ID Defined Names (8)
- ✅ Data Validations
- ✅ Calculated Columns
- ✅ Step 31 Compatible

### test_step31.py: 7/7 PASSED

- ✅ File Exists
- ✅ Sheets Count
- ✅ Sheets Order
- ✅ Headers
- ✅ Defined Names (11)
- ✅ Data Validation (60)
- ✅ Excel Tables (15)

## Backup Automático

Cada ejecución del script de seed crea un backup:

```
data/excel/_backups/Quelonio_Excel_MVP_Skeleton_step34_YYYYMMDD_HHMMSS.xlsx
```

Ejemplo: `Quelonio_Excel_MVP_Skeleton_step34_20260114_193542.xlsx`

## Determinismo

- ✅ El script es completamente determinista
- ✅ Mismo input → mismo output
- ✅ Evita duplicados por ID
- ✅ Tests verifican comportamiento específico

## Manejo de Errores

- ✅ Fails con error claro si no puede cargar el archivo
- ✅ Verifica existencia de hojas antes de insertar
- ✅ Verifica integridad de FKs en seed data
- ✅ Preserva estructura existente sin modificaciones
- ✅ Export maneja hojas vacías gracefulmente

## Flujo de Trabajo Recomendado

### Para Desarrollo/Testing:

1. **Seed inicial:**
   ```bash
   python tools/build_excel_mvp_step34_seed.py
   ```

2. **Validar seed:**
   ```bash
   python tools/test_step34.py
   ```

3. **Exportar datos:**
   ```bash
   python tools/export_excel_csv_pack.py
   ```

4. **Verificar compatibilidad:**
   ```bash
   python tools/test_step31.py
   python tools/test_step32.py
   python tools/test_step33.py
   ```

### Para Producción:

1. Usar el Excel como template
2. Cargar datos reales respetando estructura
3. Exportar periódicamente a CSV para backup
4. Validar integridad de FKs periódicamente

## Casos de Uso

### Caso 1: Demo para Usuarios
El seed data proporciona un ejemplo completo del sistema con:
- 2 recetas reales (IPA y Stout)
- Producción de 2 lotes
- Ventas a 3 clientes diferentes
- Inventario con 10 items
- Flujo completo desde materias primas hasta ventas

### Caso 2: Testing de Integración
El seed data permite:
- Probar calculados (abv_estimado, total_calc, etc.)
- Validar integridad de FKs
- Verificar validaciones de datos
- Probar export e import de datos

### Caso 3: Backup Migratorio
El export CSV permite:
- Migrar datos entre sistemas
- Versionado de snapshots
- Análisis offline
- Integración con otros sistemas

## Integridad de Datos Verificada

### FK Integrity (15 relaciones validadas):

1. 02_RecetaVersiones.receta_id → 01_Recetas.receta_id
2. 03_Lotes.recipe_version_id → 02_RecetaVersiones.recipe_version_id
3. 10_Productos.receta_id → 01_Recetas.receta_id
4. 13_VentasLineas.venta_id → 12_Ventas.venta_id
5. 13_VentasLineas.producto_id → 10_Productos.producto_id
6. 14_Pagos.venta_id → 12_Ventas.venta_id
7. 15_FulfillmentVentaLote.venta_linea_id → 13_VentasLineas.linea_id
8. 15_FulfillmentVentaLote.batch_id → 03_Lotes.batch_id
9. 09_ConsumosLote.batch_id → 03_Lotes.batch_id
10. 09_ConsumosLote.item_id → 05_ItemsInventario.item_id
11. 09_ConsumosLote.lote_insumo_id → 08_LotesInsumo.lote_insumo_id
12. 05_ItemsInventario.proveedor_id → 07_Proveedores.proveedor_id
13. 08_LotesInsumo.item_id → 05_ItemsInventario.item_id
14. 08_LotesInsumo.proveedor_id → 07_Proveedores.proveedor_id
15. 12_Ventas.cliente_id → 11_Clientes.cliente_id

## Próximos Pasos

Paso 35 podría incluir:
- Importación de CSV a Excel
- Validación de datos antes de importar
- Reportes de integridad de datos
- Macros para tareas repetitivas
- Integración con RAG/ACI system

## Referencias

- Especificación original: `docs/98_Verdad_Negocio/EXCEL_MVP_SPEC.md`
- Documentación Paso 31: `docs/98_Verdad_Negocio/EXCEL_MVP_STEP31.md`
- Documentación Paso 32: `docs/98_Verdad_Negocio/EXCEL_MVP_STEP32.md`
- Documentación Paso 33: `docs/98_Verdad_Negocio/EXCEL_MVP_STEP33.md`
- Librería openpyxl: https://openpyxl.readthedocs.io/

## Notas Importantes

- **Sin Macros/VBA:** La seed y export se implementan sin VBA
- **Sin modificación de estructura:** Headers y tablas permanecen intactos
- **Idempotente:** El script de seed puede correrse múltiples veces
- **Determinismo:** Todo es reproducible y testeable
- **Backups automáticos:** Cada modificación crea un backup
- **Compatible Excel ES:** Los CSV usan `;` como delimitador
- **UTF-8:** Los CSV usan encoding UTF-8 para compatibilidad
