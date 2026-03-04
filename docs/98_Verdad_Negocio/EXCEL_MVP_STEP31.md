# Excel MVP Step 31 - Skeleton Creation

**Objetivo**: Crear plantilla Excel MVP con hojas, tablas y validaciones básicas según EXCEL_MVP_SPEC.md

---

## Ejecución

### Requisitos Previos

1. Python 3.x instalado
2. openpyxl instalado:
   ```bash
   pip install openpyxl
   ```

### Comando de Ejecución

En Windows (PowerShell/CMD):
```powershell
.\tools\build_excel_mvp.py
```

O usando Python directamente:
```bash
python tools/build_excel_mvp.py
```

---

## Ubicación del Archivo

**Archivo generado**: `data/excel/Quelonio_Excel_MVP_Skeleton.xlsx`

**Ruta completa** (relative to repo root):
- `./data/excel/Quelonio_Excel_MVP_Skeleton.xlsx`

**Ubicación absoluta** (ejemplo):
- `C:\Users\flore\Documents\quelonio-pages-v2\data\excel\Quelonio_Excel_MVP_Skeleton.xlsx`

---

## Contenido del Excel

### Hojas Creadas (16 en total)

| # | Nombre de Hoja | Tipo | Columnas |
|---|----------------|-------|----------|
| 1 | 01_Recetas | Datos | 5 |
| 2 | 02_RecetaVersiones | Datos | 15 |
| 3 | 03_Lotes | Datos | 14 |
| 4 | 04_LoteMediciones | Datos | 5 |
| 5 | 05_ItemsInventario | Datos | 10 |
| 6 | 06_MovimientosInventario | Datos | 7 |
| 7 | 07_Proveedores | Datos | 4 |
| 8 | 08_LotesInsumo | Datos | 4 |
| 9 | 09_ConsumosLote | Datos | 7 |
| 10 | 10_Productos | Datos | 8 |
| 11 | 11_Clientes | Datos | 8 |
| 12 | 12_Ventas | Datos | 8 |
| 13 | 13_VentasLineas | Datos | 6 |
| 14 | 14_Pagos | Datos | 5 |
| 15 | 15_FulfillmentVentaLote | Datos | 6 |
| 16 | 99_Listas | Validación | N/A |

---

## Tablas Excel (Excel Tables)

Cada hoja de datos tiene una tabla Excel con las siguientes características:

- **Nombre de tabla**: `tblXXX` (ej: `tblRecetas`, `tblLotes`, etc.)
- **Formato**: TableStyleMedium9 (rayas alternadas)
- **Rango**: Dinámico (debe especificarse al crear la tabla en Excel)

**Nota**: En el script actual, las tablas se crean con el rango de la fila de cabecera (ej: `A1:E1` para Recetas). Al usar el Excel, se debe expandir la tabla manualmente o mediante Power Query.

---

## Validaciones de Datos

### Listas de Validación (Hoja 99_Listas)

Las siguientes listas están disponibles para validación:

| Nombre de Lista | Valores |
|-----------------|---------|
| LIST_RECETAS_ESTADO | activa, archivada, experimental |
| LIST_LOTES_ESTADO | planificado, coccion, fermentacion, maduracion, envasado, completado, cancelado |
| LIST_ITEMS_TIPO | insumo, producto_terminado, barril |
| LIST_ITEMS_UNIDAD_MEDIDA | kg, litros, unidades |
| LIST_ITEMS_ESTADO | activo, inactivo |
| LIST_MOVIMIENTOS_TIPO | entrada, salida, ajuste |
| LIST_CLIENTES_TIPO | minorista, mayorista, directo |
| LIST_CLIENTES_CANAL | local, evento, online |
| LIST_VENTAS_ESTADO_PAGO | pendiente, pagado_parcial, pagado |
| LIST_PAGOS_METODO | efectivo, transferencia, tarjeta |
| LIST_PRODUCTOS_ESTADO | activo, inactivo |

### Validaciones Aplicadas por Columna

Las siguientes columnas tienen validación de lista desplegable aplicada:

- **Recetas**: `estado` → LIST_RECETAS_ESTADO
- **Lotes**: `estado` → LIST_LOTES_ESTADO
- **ItemsInventario**: `tipo` → LIST_ITEMS_TIPO, `unidad_medida` → LIST_ITEMS_UNIDAD_MEDIDA, `estado` → LIST_ITEMS_ESTADO
- **MovimientosInventario**: `tipo_movimiento` → LIST_MOVIMIENTOS_TIPO
- **Clientes**: `tipo` → LIST_CLIENTES_TIPO, `canal` → LIST_CLIENTES_CANAL, `estado` → LIST_ITEMS_ESTADO
- **Ventas**: `estado_pago` → LIST_VENTAS_ESTADO_PAGO
- **Productos**: `estado` → LIST_PRODUCTOS_ESTADO
- **Pagos**: `metodo` → LIST_PAGOS_METODO

---

## Formato de Hojas

### Características Comunes

- **Fila 1**: Headers en negrita
- **Paneles congelados**: Fila 1 (los headers siempre visibles)
- **Ancho de columnas**: Auto-ajustado (heuristic basado en longitud del header, min 10, max 50 caracteres)

### Tablas Excel

Cada hoja de datos tiene una tabla Excel con:
- Estilo: TableStyleMedium9
- Filas con rayas alternadas
- Headers resaltados

---

## Campos por Hoja

### 01_Recetas (5 columnas)
1. receta_id
2. nombre
3. estado
4. fecha_creacion
5. notas

### 02_RecetaVersiones (15 columnas)
1. recipe_version_id
2. receta_id
3. version_num
4. og_target
5. fg_target
6. abv_target
7. ibu_target
8. srm_target
9. eficiencia
10. rendimiento_litros
11. merma_porcentaje
12. costo_estimado_batch
13. costo_estimado_litro
14. fecha_version
15. notas

### 03_Lotes (14 columnas)
1. batch_id
2. recipe_version_id
3. fecha_inicio
4. fecha_coccion
5. fecha_fermentacion
6. fecha_maduracion
7. fecha_envasado
8. volumen_litros
9. og_medido
10. fg_medido
11. abv_medido
12. estado
13. costo_real_batch
14. notas

### 04_LoteMediciones (5 columnas)
1. medicion_id
2. batch_id
3. tipo_medicion
4. valor
5. fecha

### 05_ItemsInventario (10 columnas)
1. item_id
2. nombre
3. tipo
4. unidad_medida
5. stock_actual
6. stock_minimo
7. costo_unitario
8. proveedor_id
9. estado
10. notas

### 06_MovimientosInventario (7 columnas)
1. movimiento_id
2. item_id
3. tipo_movimiento
4. cantidad
5. fecha
6. referencia
7. notas

### 07_Proveedores (4 columnas)
1. proveedor_id
2. nombre
3. contacto
4. email

### 08_LotesInsumo (4 columnas)
1. lote_insumo_id
2. item_id
3. proveedor_id
4. fecha_vencimiento

### 09_ConsumosLote (7 columnas)
1. consumo_id
2. batch_id
3. item_id
4. proveedor_id
5. lote_insumo_id
6. cantidad
7. fecha

### 10_Productos (8 columnas)
1. producto_id
2. nombre
3. receta_id
4. volumen_ml
5. precio_venta
6. costo_unitario
7. margen_porcentaje
8. estado

### 11_Clientes (8 columnas)
1. cliente_id
2. nombre
3. tipo
4. canal
5. contacto
6. email
7. telefono
8. estado

### 12_Ventas (8 columnas)
1. venta_id
2. cliente_id
3. fecha
4. subtotal
5. total
6. estado_pago
7. saldo
8. notas

### 13_VentasLineas (6 columnas)
1. linea_id
2. venta_id
3. producto_id
4. cantidad
5. precio_unitario
6. subtotal

### 14_Pagos (5 columnas)
1. pago_id
2. venta_id
3. fecha
4. monto
5. metodo

### 15_FulfillmentVentaLote (6 columnas)
1. fulfillment_id
2. venta_id
3. venta_linea_id
4. batch_id
5. cantidad_litros
6. fecha

### 99_Listas (Validación)
- Contiene listas de validación para columnas enum
- Cada lista tiene un nombre de rango definido (DefinedName)

---

## Próximos Pasos

### Paso 32: FK Validation

El próximo paso implementará:
- Validación de Foreign Keys (XLOOKUP)
- Formulas para calcular campos derivados (costos, márgenes)
- Dashboards con KPIs

---

## Notas Técnicas

### Dependencias

- **Python**: 3.x
- **openpyxl**: 3.1.5+

### Limitaciones Actuales

1. Las tablas Excel se crean con rango solo de headers (ej: `A1:E1`). Al agregar datos, se debe expandir manualmente la tabla o usar Power Query.
2. Las validaciones de FK no están implementadas (Paso 32).
3. Los campos calculados (costos, márgenes) no tienen fórmulas (Paso 32).

### Migración a aci-rag-starter

El archivo `.xlsx` puede moverse a `aci-rag-starter/data/excel/` o cualquier otro directorio según necesidades.

---

**Fin de Documentación**
