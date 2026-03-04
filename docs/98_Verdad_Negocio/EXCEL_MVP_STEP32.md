# Excel MVP - Paso 32: Catálogos, FKs, Validaciones y Cálculos

## Resumen

Este paso agrega funcionalidad operativa al Excel MVP, incluyendo:
- Hoja de catálogos con listas de enumeraciones
- Nombres definidos para claves foráneas (FKs)
- Validación de datos para enums y FKs
- Columnas calculadas en tablas Lotes y Ventas

## Archivos Generados/Modificados

### 1. tools/build_excel_mvp_step32.py
Script principal que genera/actualiza el Excel con las funcionalidades del Paso 32.

**Funcionalidades:**
- Crea backup automático del archivo Excel existente
- Crea hoja "Catalogos" con listas verticales de valores
- Crea nombres definidos para catálogos (lst_*)
- Crea nombres definidos para columnas ID (FK targets)
- Aplica validación de datos a columnas específicas
- Agrega columnas calculadas con fórmulas

### 2. tools/test_step32.py
Script de test determinista que verifica:
- Existencia de hoja Catalogos
- Nombres definidos para catálogos
- Nombres definidos para IDs (FKs)
- Validación de datos en columnas esperadas
- Fórmulas en columnas calculadas
- Compatibilidad con Paso 31

### 3. data/excel/Quelonio_Excel_MVP_Skeleton.xlsx
Archivo Excel modificado con nuevas funcionalidades.

### 4. tools/test_step31.py (Modificado)
Actualizado para ser compatible con Paso 32:
- Test 2: Ahora verifica que las hojas esperadas estén presentes (no exactamente)
- Test 4: Ahora verifica que los headers esperados estén presentes (no exactamente)

**Razón de la modificación:** Paso 32 agrega una nueva hoja (Catalogos) y columnas calculadas a tablas existentes. Los tests originales verificaban coincidencia exacta, lo que causaba falsos negativos. Los tests ahora verifican que lo que existía en Paso 31 se mantenga intacto.

## Cambios Realizados

### A. Hoja Catalogos + Defined Names

**Nueva hoja:** "Catalogos" con las siguientes listas verticales:

| Nombre de Catálogo | Valores |
|-------------------|---------|
| CAT_LoteEstado | planificado, coccion, fermentacion, maduracion, envasado, completado, cancelado |
| CAT_MovTipo | entrada, salida, ajuste, consumo, produccion, venta |
| CAT_PagoEstado | pendiente, pagado, parcial |
| CAT_ClienteTipo | minorista, mayorista, bar, distribuidor, otro |
| CAT_Canal | taproom, bar, distribucion, online, evento, otro |
| CAT_ItemTipo | malta, luppulo, levadura, agua, adjunto, quimico, envase, etiqueta, servicio, otro |

**Nombres definidos creados:**
- `lst_lote_estado` → Catalogos!$A$2:$A$8
- `lst_mov_tipo` → Catalogos!$A$11:$A$16
- `lst_pago_estado` → Catalogos!$A$19:$A$21
- `lst_cliente_tipo` → Catalogos!$A$24:$A$28
- `lst_canal` → Catalogos!$A$31:$A$36
- `lst_item_tipo` → Catalogos!$A$39:$A$48

### B. Defined Names para IDs (FKs)

**Nombres definidos para columnas ID:**

| Nombre | Referencia |
|--------|-----------|
| lst_receta_id | 01_Recetas!A2:A[last] |
| lst_recipe_version_id | 02_RecetaVersiones!A2:A[last] |
| lst_batch_id | 03_Lotes!A2:A[last] |
| lst_item_id | 05_ItemsInventario!A2:A[last] |
| lst_lote_insumo_id | 08_LotesInsumo!A2:A[last] |
| lst_venta_id | 12_Ventas!A2:A[last] |
| lst_linea_id | 13_VentasLineas!A2:A[last] |
| lst_producto_id | 10_Productos!A2:A[last] |

### C. Validación de Datos (Data Validation)

**Enum validations:**
- Lotes[estado] → =lst_lote_estado
- MovimientosInventario[tipo_movimiento] → =lst_mov_tipo
- ItemsInventario[tipo] → =lst_item_tipo
- Clientes[tipo] → =lst_cliente_tipo
- Clientes[canal] → =lst_canal
- Ventas[estado_pago] → =lst_pago_estado

**FK validations (listas):**
- RecetaVersiones[receta_id] → =lst_receta_id
- Lotes[recipe_version_id] → =lst_recipe_version_id
- VentasLineas[venta_id] → =lst_venta_id
- VentasLineas[producto_id] → =lst_producto_id
- Pagos[venta_id] → =lst_venta_id
- ConsumosLote[batch_id] → =lst_batch_id
- ConsumosLote[item_id] → =lst_item_id
- ConsumosLote[lote_insumo_id] → =lst_lote_insumo_id
- FulfillmentVentaLote[venta_linea_id] → =lst_linea_id
- FulfillmentVentaLote[batch_id] → =lst_batch_id

**Rango de aplicación:** Filas 2 a 5000 para todas las validaciones.

### D. Columnas Calculadas

**En tabla Lotes:**
- `abv_estimado` =IF(AND([@og_medido]<>"",[@fg_medido]<>""), ([@og_medido]-[@fg_medido])*131.25, "")

**En tabla Ventas:**
- `total_calc` =IF([@venta_id]="","",SUMIF(VentasLineas[venta_id],[@venta_id],VentasLineas[subtotal]))
- `pagos_calc` =IF([@venta_id]="","",SUMIF(Pagos[venta_id],[@venta_id],Pagos[monto]))
- `saldo_calc` =IF([@venta_id]="","",[@total_calc]-[@pagos_calc])

## Cómo Correr

### Generar/Actualizar Excel (Paso 32)

```bash
python tools/build_excel_mvp_step32.py
```

Esto:
1. Crea backup en `data/excel/_backups/` con timestamp
2. Actualiza el Excel con catálogos, validaciones y columnas calculadas
3. Guarda el archivo actualizado

### Ejecutar Tests (Paso 32)

```bash
python tools/test_step32.py
```

Verifica:
- Hoja Catalogos existe con todos los catálogos
- Nombres definidos para catálogos están presentes
- Nombres definidos para IDs están presentes
- Validaciones de datos en columnas clave
- Fórmulas correctas en columnas calculadas
- Compatibilidad con Paso 31

### Ejecutar Tests (Paso 31 - Verificación de Retrocompatibilidad)

```bash
python tools/test_step31.py
```

Verifica que todo lo del Paso 31 se mantenga intacto después del Paso 32.

## Compatibilidad

### Paso 31 Preservado

Todo lo generado en Paso 31 se mantiene:
- ✅ Todas las hojas originales (01_Recetas a 99_Listas)
- ✅ Todos los headers originales
- ✅ Todas las tablas originales
- ✅ Todos los nombres definidos originales (LIST_*)
- ✅ Validaciones de datos originales

### Adiciones del Paso 32

- ✅ Nueva hoja Catalogos
- ✅ Nuevas columnas calculadas en Lotes y Ventas
- ✅ Nuevos nombres definidos (lst_*)
- ✅ Nuevas validaciones de datos

## Estructura del Excel Final

**Total de hojas:** 17

1. 01_Recetas
2. 02_RecetaVersiones
3. 03_Lotes (con abv_estimado)
4. 04_LoteMediciones
5. 05_ItemsInventario
6. 06_MovimientosInventario
7. 07_Proveedores
8. 08_LotesInsumo
9. 09_ConsumosLote
10. 10_Productos
11. 11_Clientes
12. 12_Ventas (con total_calc, pagos_calc, saldo_calc)
13. 13_VentasLineas
14. 14_Pagos
15. 15_FulfillmentVentaLote
16. 99_Listas
17. Catalogos (NUEVO)

## Resultados de Tests

### test_step32.py: 7/7 PASSED

- ✅ File Exists
- ✅ Catalogos Sheet
- ✅ Catalog Defined Names (6)
- ✅ ID Defined Names (8)
- ✅ Data Validations (5 columnas verificadas)
- ✅ Calculated Columns (4 columnas verificadas)
- ✅ Step 31 Compatible

### test_step31.py: 7/7 PASSED

- ✅ File Exists
- ✅ Sheets Count (16 originales + 1 nueva = 17)
- ✅ Sheets Order
- ✅ Headers (todos los originales presentes)
- ✅ Defined Names (11 originales)
- ✅ Data Validation (28 total)
- ✅ Excel Tables (15)

## Backup Automático

Cada ejecución del script de build crea un backup:

```
data/excel/_backups/Quelonio_Excel_MVP_Skeleton_step32_YYYYMMDD_HHMMSS.xlsx
```

Ejemplo: `Quelonio_Excel_MVP_Skeleton_step32_20260114_190523.xlsx`

## Detalles de Implementación

### Determinismo

- ✅ El script es completamente determinista
- ✅ Same input → same output
- ✅ Tests verifican comportamiento específico

### Manejo de Errores

- ✅ Fails con error claro si falta tabla/columna esperada
- ✅ No inventa estructuras no especificadas
- ✅ Preserva estructura existente del Paso 31

### Validaciones

- ✅ Data Validation aplicada con mensajes de error en español
- ✅ Permite valores en blanco (allowBlank=True)
- ✅ Rango de validación: filas 2-5000

### Fórmulas

- ✅ Usan referencias estructuradas de tabla ([@columna])
- ✅ Validan presencia de datos antes de calcular
- ✅ Devuelven string vacío si no hay datos suficientes

## Próximos Pasos

Paso 33 podría incluir:
- Más columnas calculadas
- Validaciones cruzadas
- Fórmulas condicionales
- Formato condicional
- Dashboards básicos

## Referencias

- Especificación original: `docs/98_Verdad_Negocio/EXCEL_MVP_SPEC.md`
- Documentación Paso 31: `docs/98_Verdad_Negocio/EXCEL_MVP_STEP31.md`
- Librería openpyxl: https://openpyxl.readthedocs.io/
