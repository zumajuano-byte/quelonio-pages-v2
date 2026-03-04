# STEP 30 - Checklist de Implementación Excel MVP

**Objetivo**: Guía accionable para implementar el Excel MVP según la especificación funcional.

---

## 1. Crear Estructura de Hojas

### 1.1. Hojas de Datos (Tablas)

- [ ] Crear hoja `Recetas` con tabla `tbl_Recetas`
- [ ] Crear hoja `Lotes` con tabla `tbl_Lotes`
- [ ] Crear hoja `LoteMediciones` con tabla `tbl_LoteMediciones`
- [ ] Crear hoja `ItemsInventario` con tabla `tbl_ItemsInventario`
- [ ] Crear hoja `MovimientosInventario` con tabla `tbl_MovimientosInventario`
- [ ] Crear hoja `Proveedores` con tabla `tbl_Proveedores`
- [ ] Crear hoja `LotesInsumo` con tabla `tbl_LotesInsumo`
- [ ] Crear hoja `ConsumosLote` con tabla `tbl_ConsumosLote`
- [ ] Crear hoja `Productos` con tabla `tbl_Productos`
- [ ] Crear hoja `Clientes` con tabla `tbl_Clientes`
- [ ] Crear hoja `Ventas` con tabla `tbl_Ventas`
- [ ] Crear hoja `VentasLineas` con tabla `tbl_VentasLineas`
- [ ] Crear hoja `Pagos` con tabla `tbl_Pagos`
- [ ] Crear hoja `FulfillmentVentaLote` con tabla `tbl_FulfillmentVentaLote`

### 1.2. Hojas Auxiliares

- [ ] Crear hoja `_Listas` con opciones para validaciones (estados, tipos, canales)
- [ ] Crear hoja `_Config` con constantes (porcentaje merma default, etc.)
- [ ] Crear hoja `KPIs` para indicadores clave
- [ ] Crear hoja `Dashboard_Costos`
- [ ] Crear hoja `Dashboard_StockCritico`
- [ ] Crear hoja `Dashboard_LotesEnCurso`

---

## 2. Crear Validaciones de Datos

### 2.1. Estados

- [ ] Validación en `tbl_Recetas[estado]`: activa, archivada, experimental
- [ ] Validación en `tbl_Lotes[estado]`: planificado, coccion, fermentacion, maduracion, envasado, completado, cancelado
- [ ] Validación en `tbl_ItemsInventario[estado]`: activo, inactivo
- [ ] Validación en `tbl_Productos[estado]`: activo, inactivo
- [ ] Validación en `tbl_Clientes[estado]`: activo, inactivo
- [ ] Validación en `tbl_Ventas[estado_pago]`: pendiente, pagado_parcial, pagado

### 2.2. Tipos y Canales

- [ ] Validación en `tbl_ItemsInventario[tipo]`: insumo, producto_terminado, barril
- [ ] Validación en `tbl_ItemsInventario[unidad_medida]`: kg, litros, unidades
- [ ] Validación en `tbl_Clientes[tipo]`: minorista, mayorista, directo
- [ ] Validación en `tbl_Clientes[canal]`: local, evento, online
- [ ] Validación en `tbl_MovimientosInventario[tipo_movimiento]`: entrada, salida, ajuste
- [ ] Validación en `tbl_Pagos[metodo]`: efectivo, transferencia, tarjeta

### 2.3. Referencias (Opcional Avanzado)

- [ ] Validación en `tbl_Lotes[recipe_version_id]` contra `tbl_Recetas[recipe_version_id]`
- [ ] Validación en `tbl_ConsumosLote[batch_id]` contra `tbl_Lotes[batch_id]`
- [ ] Validación en `tbl_ConsumosLote[item_id]` contra `tbl_ItemsInventario[item_id]`
- [ ] Validación en `tbl_Ventas[cliente_id]` contra `tbl_Clientes[cliente_id]`
- [ ] Validación en `tbl_VentasLineas[producto_id]` contra `tbl_Productos[producto_id]`

---

## 3. Crear KPIs

### 3.1. Hoja `KPIs` - Fórmulas

- [ ] **KPI 1: Costo por Litro**
  - Fórmula: `=SUM(tbl_Lotes[costo_real_batch]) / SUM(tbl_Lotes[volumen_litros])`
  - Formato: Moneda por litro

- [ ] **KPI 2: Margen % Promedio**
  - Fórmula: `=AVERAGE(tbl_Productos[margen_porcentaje])`
  - Formato: Porcentaje

- [ ] **KPI 3: Rotación de Stock**
  - Fórmula: Crear columna auxiliar en `tbl_ItemsInventario` con cálculo
  - Promedio de días de rotación para ítems tipo "insumo"
  - Formato: Número

- [ ] **KPI 4: Stock Crítico**
  - Fórmula: `=COUNTIF(tbl_ItemsInventario[stock_actual]; "<" & tbl_ItemsInventario[stock_minimo])`
  - Formato: Número

- [ ] **KPI 5: Lotes en Curso/Atrasados**
  - Fórmula: `=COUNTIF(tbl_Lotes[estado]; "<>completado")`
  - Formato: Número

---

## 4. Crear Dashboards

### 4.1. Dashboard Costos

- [ ] **Gráfico 1: Costo por Lote (histórico)**
  - Tipo: Línea
  - Eje X: `tbl_Lotes[batch_id]` (ordenado por `fecha_inicio`)
  - Eje Y: `tbl_Lotes[costo_real_batch]`

- [ ] **Gráfico 2: Costo por Litro por Receta**
  - Tipo: Barras
  - Fuente: Tabla dinámica o fórmula `=SUMIF(tbl_Lotes[receta_id]; ...)`
  - Eje X: `tbl_Recetas[nombre]`
  - Eje Y: Promedio de `costo_real_batch/volumen_litros`

- [ ] **Gráfico 3: Top 5 Insumos por Costo**
  - Tipo: Barras
  - Fuente: `tbl_ConsumosLote` × `tbl_ItemsInventario`
  - Eje X: Top 5 `tbl_ItemsInventario[nombre]`
  - Eje Y: Suma de `cantidad*costo_unitario`

### 4.2. Dashboard Stock Crítico

- [ ] **Gráfico 1: Ítems bajo Stock Mínimo**
  - Tipo: Tabla
  - Filtros: `stock_actual < stock_minimo`
  - Columnas: `item_id`, `nombre`, `stock_actual`, `stock_minimo`

- [ ] **Gráfico 2: Rotación de Stock**
  - Tipo: Barras
  - Eje X: `tbl_ItemsInventario[nombre]`
  - Eje Y: Días de rotación (calculados)

- [ ] **Gráfico 3: Movimientos de Inventario (últimos 30 días)**
  - Tipo: Línea
  - Fuente: `tbl_MovimientosInventario`
  - Eje X: `fecha` (filtrado últimos 30 días)
  - Eje Y: `COUNT(movimiento_id)` por `tipo_movimiento`

### 4.3. Dashboard Lotes en Curso

- [ ] **Gráfico 1: Lotes por Estado**
  - Tipo: Pie
  - Fuente: `tbl_Lotes`
  - Categorías: `estado`
  - Valores: `COUNT(batch_id)`

- [ ] **Gráfico 2: Tiempo por Etapa (promedio)**
  - Tipo: Barras
  - Fuente: Cálculo manual sobre `tbl_Lotes` (fechas)
  - Eje X: Estados (coccion→fermentación, etc.)
  - Eje Y: Días promedio por etapa

- [ ] **Gráfico 3: Cumplimiento de Especificaciones**
  - Tipo: Tabla
  - Fuente: `tbl_Lotes` × `tbl_Recetas`
  - Columnas: `receta_id`, `% lotes dentro de target OG`, `% lotes dentro de target FG`, `% lotes dentro de target ABV`

---

## 5. Pruebas de Trazabilidad

### 5.1. Prueba 1: Trazabilidad Insumo → Lote

**Escenario**:
- Proveedor "Malta Pro" entrega lote de lúpulo "L-001"
- Lote "LOTE-2024-001" consume lúpulo "L-001"

**Pasos**:
1. [ ] Crear proveedor en `tbl_Proveedores` (proveedor_id: PROV-001)
2. [ ] Crear item de inventario en `tbl_ItemsInventario` (item_id: ITEM-001, nombre: "Lúpulo Cascade")
3. [ ] Crear lote de insumo en `tbl_LotesInsumo` (lote_insumo_id: LOTEIN-001, item_id: ITEM-001, proveedor_id: PROV-001, lote: "L-001")
4. [ ] Crear lote de producción en `tbl_Lotes` (batch_id: LOTE-2024-001, recipe_version_id: REC-001-V01)
5. [ ] Registrar consumo en `tbl_ConsumosLote` (consumo_id: CONS-001, batch_id: LOTE-2024-001, item_id: ITEM-001, lote_insumo: "L-001", cantidad: 500, proveedor_id: PROV-001)
6. [ ] Verificar: Consultar `tbl_ConsumosLote` filtrado por `batch_id = LOTE-2024-001` muestra el consumo correcto

**Resultado esperado**:
- El lote "LOTE-2024-001" tiene registro de consumo de lúpulo del lote "L-001" del proveedor "PROV-001"

---

### 5.2. Prueba 2: Trazabilidad Lote → Venta

**Escenario**:
- Lote "LOTE-2024-001" produce 1000 litros
- Venta "VTA-001" vende 500 litros de cerveza de ese lote

**Pasos**:
1. [ ] Crear cliente en `tbl_Clientes` (cliente_id: CLI-001, nombre: "Bar Local")
2. [ ] Crear producto en `tbl_Productos` (producto_id: PROD-001, nombre: "Cerveza IPA 500ml")
3. [ ] Crear venta en `tbl_Ventas` (venta_id: VTA-001, cliente_id: CLI-001, total: 10000)
4. [ ] Crear línea de venta en `tbl_VentasLineas` (linea_id: LIN-001, venta_id: VTA-001, producto_id: PROD-001, cantidad: 1000, subtotal: 10000)
5. [ ] Registrar fulfillment en `tbl_FulfillmentVentaLote` (fulfillment_id: FUL-001, venta_id: VTA-001, venta_linea_id: LIN-001, batch_id: LOTE-2024-001, cantidad_litros: 500)
6. [ ] Verificar: Consultar `tbl_FulfillmentVentaLote` filtrado por `batch_id = LOTE-2024-001` muestra 500 litros asignados

**Resultado esperado**:
- La venta "VTA-001" tiene registro de que 500 litros provienen del lote "LOTE-2024-001"

---

### 5.3. Prueba 3: Trazabilidad Completa Insumo → Lote → Venta

**Escenario**:
- Insumo "Malta Pilsner" (lote "M-002", proveedor "Malta Pro")
- Lote "LOTE-2024-002" consume malta "M-002"
- Venta "VTA-002" vende cerveza del lote "LOTE-2024-002"

**Pasos**:
1. [ ] Crear/verificar proveedor "Malta Pro" en `tbl_Proveedores`
2. [ ] Crear item "Malta Pilsner" en `tbl_ItemsInventario`
3. [ ] Crear lote de insumo "M-002" en `tbl_LotesInsumo`
4. [ ] Crear lote de producción "LOTE-2024-002" en `tbl_Lotes`
5. [ ] Registrar consumo en `tbl_ConsumosLote` (batch_id: LOTE-2024-002, item_id: ITEM-MALTA, lote_insumo: "M-002")
6. [ ] Crear venta "VTA-002" en `tbl_Ventas`
7. [ ] Crear línea de venta en `tbl_VentasLineas`
8. [ ] Registrar fulfillment en `tbl_FulfillmentVentaLote` (venta_id: VTA-002, batch_id: LOTE-2024-002)
9. [ ] Verificar: Consulta conjunta muestra la cadena completa

**Resultado esperado**:
- Venta "VTA-002" → Lote "LOTE-2024-002" → Malta "M-002" → Proveedor "Malta Pro"

---

## 6. Pruebas de Import de CSV desde ACI

### 6.1. Configuración de Import

**Endpoint base**:
- URL: `http://localhost:8080/export/run` (ajustar según configuración)
- Formato: CSV
- Delimitador: semicolon (recomendado para Excel AR)

### 6.2. Prueba 1: Importar Recetas

**Comando**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=recetas&format=csv&delimiter=semicolon" -o recetas.csv
```

**Pasos**:
1. [ ] Ejecutar comando CURL o abrir URL en navegador
2. [ ] Guardar CSV como `recetas.csv`
3. [ ] Abrir Excel → Datos → Obtener datos → Desde texto/CSV
4. [ ] Seleccionar archivo `recetas.csv`
5. [ ] Configurar: Delimitador = Punto y coma, Codificación = UTF-8
6. [ ] Cargar datos en hoja `Recetas` (reemplazar o fusionar)
7. [ ] Verificar: Todos los campos de `tbl_Recetas` se importan correctamente
8. [ ] Verificar: IDs son únicos (usar condicional formatting)

**Resultado esperado**:
- Tabla `tbl_Recetas` tiene datos de ACI sin duplicados

---

### 6.3. Prueba 2: Importar Lotes

**Comando**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=lotes&format=csv&delimiter=semicolon" -o lotes.csv
```

**Pasos**:
1. [ ] Ejecutar comando CURL
2. [ ] Guardar CSV como `lotes.csv`
3. [ ] Importar en Excel (Datos → Desde texto/CSV)
4. [ ] Cargar en hoja `Lotes`
5. [ ] Verificar: `recipe_version_id` en Lotes existe en `tbl_Recetas`
6. [ ] Verificar: Estados están dentro de la lista de validación

**Resultado esperado**:
- Tabla `tbl_Lotes` tiene datos de ACI con referencias válidas

---

### 6.4. Prueba 3: Importar Inventario

**Comando**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=inventario&format=csv&delimiter=semicolon" -o inventario.csv
```

**Pasos**:
1. [ ] Ejecutar comando CURL
2. [ ] Guardar CSV como `inventario.csv`
3. [ ] Importar en Excel (Datos → Desde texto/CSV)
4. [ ] Cargar en hoja `ItemsInventario`
5. [ ] Verificar: `proveedor_id` existe en `tbl_Proveedores`
6. [ ] Verificar: Tipos (insumo, producto_terminado, barril) son válidos
7. [ ] Verificar: Unidades de medida son válidas

**Resultado esperado**:
- Tabla `tbl_ItemsInventario` tiene datos de ACI con referencias válidas

---

### 6.5. Nota sobre TABULAR flat vs saltos de línea

**Comportamiento default**:
- Endpoint `/export/run` con formato CSV exporta datos como "flat" (sin newlines embebidos)
- Esto es ideal para Excel porque evita celdas multilínea problemáticas

**Si se quiere preservar saltos de línea**:
- Usar parámetro `csv_flat=0`
- Ejemplo:
  ```bash
  curl -X GET "http://localhost:8080/export/run?entity=notas&format=csv&delimiter=semicolon&csv_flat=0" -o notas.csv
  ```
- **Advertencia**: Excel puede truncar celdas con múltiples líneas

**Recomendación**:
- Usar default (`csv_flat=1` o sin parámetro) para datos principales (Recetas, Lotes, Inventario)
- Considerar hoja auxiliar `Notas` para contenido multilínea, con `entidad_id` como clave

---

## 7. Validaciones Finales

- [ ] Todas las tablas tienen formato de "Tabla de Excel" (`tbl_*`)
- [ ] Todas las validaciones de datos funcionan correctamente
- [ ] KPIs se calculan sin errores
- [ ] Dashboards se actualizan automáticamente con nuevos datos
- [ ] Pruebas de trazabilidad completadas exitosamente
- [ ] Import de CSV desde ACI funciona con `delimiter=semicolon`
- [ ] No hay fechas en formato texto (todas en formato fecha nativo)
- [ ] No hay números en formato texto
- [ ] IDs son únicos en cada tabla
- [ ] Referencias cruzadas son válidas

---

## 8. Checklist Resumen

| Tarea | Estado | Notas |
|-------|--------|-------|
| Crear hojas de datos | ☐ | 14 tablas |
| Crear hojas auxiliares | ☐ | 4 hojas |
| Crear validaciones de datos | ☐ | Estados, tipos, referencias |
| Crear KPIs | ☐ | 5 KPIs |
| Crear dashboards | ☐ | 3 dashboards |
| Prueba trazabilidad 1 | ☐ | Insumo → Lote |
| Prueba trazabilidad 2 | ☐ | Lote → Venta |
| Prueba trazabilidad 3 | ☐ | Cadena completa |
| Import CSV Recetas | ☐ | ACI → Excel |
| Import CSV Lotes | ☐ | ACI → Excel |
| Import CSV Inventario | ☐ | ACI → Excel |
| Validaciones finales | ☐ | 10 puntos |

---

**Fin de Checklist**
