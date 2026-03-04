# Excel MVP - Especificación Funcional para Negocio Cervecero

**Objetivo**: Documentar el modelo de datos mínimo viable para gestionar operaciones cerveceras en Excel, con trazabilidad completa y capacidad de integración con ACI vía CSV.

---

## A. Núcleo Operativo (Mínimo Viable Real)

### A1. Recetas + Versionado

**Objetivo**: Gestionar fórmulas de producción con costeo y parámetros técnicos.

**Entidad**: `Recetas`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| receta_id | TEXT | ID único de receta (ej: REC-001) | Formato: REC-XXX, único |
| nombre | TEXT | Nombre de receta | Requerido |
| estilo | TEXT | Estilo de cerveza (BJCP) | Requerido |
| estado | TEXT | Estado de receta | Lista: activa, archivada, experimental |
| fecha_creacion | DATE | Fecha de creación | Formato: YYYY-MM-DD |
| notas | TEXT | Notas adicionales | Opcional |

**Reglas de Integridad**:
- `receta_id` es único
- Una receta puede tener múltiples versiones (en tabla RecetaVersiones)
- `estado` controla visibilidad en producción

---

**Entidad**: `RecetaVersiones`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| recipe_version_id | TEXT | ID único de versión (ej: REC-001-V01) | Formato: REC-XXX-VNN, único |
| receta_id | TEXT | ID de receta (FK) | Referencia a Recetas |
| version_num | NUMBER | Número de versión | Requerido, >=1 |
| og_target | NUMBER | Densidad original objetivo | Requerido, 1.000-1.120 |
| fg_target | NUMBER | Densidad final objetivo | Requerido, 0.990-1.030 |
| abv_target | NUMBER | Alcohol por volumen objetivo | Requerido, 0-15% |
| ibu_target | NUMBER | IBUs objetivo | Requerido, 0-120 |
| srm_target | NUMBER | SRM (color) objetivo | Requerido, 0-40 |
| eficiencia | NUMBER | Eficiencia de sistema | Requerido, 50-90% |
| rendimiento_litros | NUMBER | Rendimiento esperado por batch | Requerido |
| merma_porcentaje | NUMBER | Merma esperada | Requerido, 0-15% |
| costo_estimado_batch | CURRENCY | Costo estimado por batch | Calculado |
| costo_estimado_litro | CURRENCY | Costo estimado por litro | Calculado |
| fecha_version | DATE | Fecha de la versión | Formato: YYYY-MM-DD |
| notas | TEXT | Notas de la versión | Opcional |

**Reglas de Integridad**:
- `recipe_version_id` es único por versión
- `receta_id` debe existir en tabla Recetas
- Una receta puede tener múltiples versiones activas
- Versiones posteriores invalidan versiones anteriores (opcional)

---

### A2. Lotes / Producción

**Objetivo**: Gestionar el ciclo de vida de cada lote de producción.

**Entidad**: `Lotes`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| batch_id | TEXT | ID único de lote (ej: LOTE-2024-001) | Formato: LOTE-YYYY-NNN, único |
| recipe_version_id | TEXT | ID de versión de receta (FK) | Referencia a RecetaVersiones |
| fecha_inicio | DATE | Fecha inicio producción | Requerido |
| fecha_coccion | DATE | Fecha cocción | Opcional |
| fecha_fermentacion | DATE | Fecha inicio fermentación | Opcional |
| fecha_maduracion | DATE | Fecha inicio maduración | Opcional |
| fecha_envasado | DATE | Fecha envasado | Opcional |
| volumen_litros | NUMBER | Volumen final del lote | Requerido |
| og_medido | NUMBER | Densidad original medida | Opcional |
| fg_medido | NUMBER | Densidad final medida | Opcional |
| abv_medido | NUMBER | ABV medido | Calculado o manual |
| estado | TEXT | Estado del lote | Lista: planificado, coccion, fermentacion, maduracion, envasado, completado, cancelado |
| costo_real_batch | CURRENCY | Costo real del lote | Calculado |
| notas | TEXT | Notas del lote | Opcional |

**Reglas de Integridad**:
- `batch_id` es único
- `recipe_version_id` debe existir en tabla RecetaVersiones
- Estado sigue flujo unidireccional (cocción→fermentación→maduración→envasado)

---

### A3. Inventario

**Objetivo**: Gestionar stock de insumos, producto terminado y barriles.

**Entidad**: `ItemsInventario`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| item_id | TEXT | ID único de item (ej: ITEM-001) | Formato: ITEM-XXX, único |
| nombre | TEXT | Nombre del item | Requerido |
| tipo | TEXT | Tipo de item | Lista: insumo, producto_terminado, barril |
| unidad_medida | TEXT | Unidad de medida | Lista: kg, litros, unidades |
| stock_actual | NUMBER | Stock actual | Requerido, >=0 |
| stock_minimo | NUMBER | Stock mínimo alerta | Requerido |
| costo_unitario | CURRENCY | Costo unitario | Requerido |
| proveedor_id | TEXT | ID proveedor principal | Referencia a Proveedores |
| estado | TEXT | Estado del item | Lista: activo, inactivo |
| notas | TEXT | Notas | Opcional |

**Entidad**: `MovimientosInventario`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| movimiento_id | TEXT | ID único (ej: MOV-001) | Formato: MOV-XXX, único |
| item_id | TEXT | ID del item | Referencia a ItemsInventario |
| tipo_movimiento | TEXT | Tipo de movimiento | Lista: entrada, salida, ajuste |
| cantidad | NUMBER | Cantidad (+ o -) | Requerido |
| fecha | DATE | Fecha del movimiento | Requerido |
| referencia | TEXT | Referencia (batch_id, venta_id, etc.) | Opcional |
| notas | TEXT | Notas | Opcional |

**Reglas de Integridad**:
- `item_id` debe existir en ItemsInventario
- `stock_actual` en ItemsInventario se recalcula sumando todos los movimientos
- Movimientos de salida no pueden exceder stock disponible

---

### A4. Trazabilidad (Clave)

**Objetivo**: Conectar insumos → lotes → ventas para rastreabilidad completa.

**Entidad**: `ConsumosLote`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| consumo_id | TEXT | ID único (ej: CONS-001) | Formato: CONS-XXX, único |
| batch_id | TEXT | ID del lote que consume | Referencia a Lotes |
| item_id | TEXT | ID del insumo consumido | Referencia a ItemsInventario |
| proveedor_id | TEXT | ID del proveedor del insumo | Referencia a Proveedores |
| lote_insumo_id | TEXT | ID del lote de insumo (FK) | Referencia a LotesInsumo |
| cantidad | NUMBER | Cantidad consumida | Requerido |
| fecha | DATE | Fecha de consumo | Requerido |

**Entidad**: `FulfillmentVentaLote`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| fulfillment_id | TEXT | ID único (ej: FUL-001) | Formato: FUL-XXX, único |
| venta_id | TEXT | ID de la venta | Referencia a Ventas |
| venta_linea_id | TEXT | ID de línea de venta | Referencia a VentasLineas |
| batch_id | TEXT | ID del lote que abastece | Referencia a Lotes |
| cantidad_litros | NUMBER | Cantidad en litros | Requerido |
| fecha | DATE | Fecha de fulfillment | Requerido |

**Reglas de Integridad**:
- `batch_id` debe existir en Lotes
- `item_id` debe existir en ItemsInventario (tipo=insumo)
- Suma de consumos por lote = total insumos usados
- Suma de fulfillment por venta = total litros vendidos

---

## B. Comercial/Admin (Segunda Ola)

### B1. Ventas y Clientes

**Entidad**: `Clientes`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| cliente_id | TEXT | ID único (ej: CLI-001) | Formato: CLI-XXX, único |
| nombre | TEXT | Nombre del cliente | Requerido |
| tipo | TEXT | Tipo de cliente | Lista: minorista, mayorista, directo |
| canal | TEXT | Canal de venta | Lista: local, evento, online |
| contacto | TEXT | Contacto | Opcional |
| email | TEXT | Email | Opcional |
| telefono | TEXT | Teléfono | Opcional |
| estado | TEXT | Estado | Lista: activo, inactivo |

**Entidad**: `Productos` (SKUs)

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| producto_id | TEXT | ID único (ej: PROD-001) | Formato: PROD-XXX, único |
| nombre | TEXT | Nombre del producto | Requerido |
| receta_id | TEXT | ID de receta base | Referencia a Recetas |
| volumen_ml | NUMBER | Volumen en ml | Requerido |
| precio_venta | CURRENCY | Precio de venta | Requerido |
| costo_unitario | CURRENCY | Costo unitario | Calculado |
| margen_porcentaje | NUMBER | Margen % | Calculado |
| estado | TEXT | Estado | Lista: activo, inactivo |

**Entidad**: `Ventas`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| venta_id | TEXT | ID único (ej: VTA-001) | Formato: VTA-XXX, único |
| cliente_id | TEXT | ID del cliente | Referencia a Clientes |
| fecha | DATE | Fecha de venta | Requerido |
| subtotal | CURRENCY | Subtotal | Calculado |
| total | CURRENCY | Total | Requerido |
| estado_pago | TEXT | Estado de pago | Lista: pendiente, pagado_parcial, pagado |
| saldo | CURRENCY | Saldo pendiente | Calculado |
| notas | TEXT | Notas | Opcional |

**Entidad**: `VentasLineas`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| linea_id | TEXT | ID único (ej: LIN-001) | Formato: LIN-XXX, único |
| venta_id | TEXT | ID de venta | Referencia a Ventas |
| producto_id | TEXT | ID de producto | Referencia a Productos |
| cantidad | NUMBER | Cantidad | Requerido |
| precio_unitario | CURRENCY | Precio unitario | Requerido |
| subtotal | CURRENCY | Subtotal línea | Calculado |

**Entidad**: `Pagos`

| Campo | Tipo | Descripción | Reglas |
|-------|------|-------------|--------|
| pago_id | TEXT | ID único (ej: PAG-001) | Formato: PAG-XXX, único |
| venta_id | TEXT | ID de venta | Referencia a Ventas |
| fecha | DATE | Fecha de pago | Requerido |
| monto | CURRENCY | Monto pagado | Requerido |
| metodo | TEXT | Método de pago | Lista: efectivo, transferencia, tarjeta |

---

### B2. Finanzas

**Cálculos Automatizados**:

- **Costo por lote**: Suma de consumos de insumos (from `ConsumosLote` × `costo_unitario` from `ItemsInventario`)
- **Costo por litro**: `costo_real_batch` / `volumen_litros`
- **Margen por producto**: `(precio_venta - costo_unitario) / precio_venta × 100`

---

## C. Integraciones (Tercera Ola)

### C1. CSV Hook (Primera Ola)

**Import desde ACI**:
- Endpoint: `/export/run?format=csv`
- Parámetros: `delimiter=semicolon` (recomendado para Excel AR)
- Soporte para endpoints de entidades específicas:
  - `/export/run?entity=recetas&format=csv&delimiter=semicolon`
  - `/export/run?entity=lotes&format=csv&delimiter=semicolon`

**Export desde Excel**:
- Generar CSV con `delimiter=semicolon` para compatibilidad con Excel AR
- Formato plano (flat), sin newlines embebidos
- UTF-8 BOM para compatibilidad con caracteres especiales

### C2. API Hook (Segunda Ola)

- Futura integración vía API REST de ACI
- Endpoints para CRUD de entidades
- Webhooks para sincronización bidireccional

---

## D. Modelo de Datos (Tablas del Excel)

### Tablas Mínimas y Campos

| # | Tabla | Campos Clave | Relaciones |
|---|-------|--------------|------------|
| 1 | Recetas | receta_id, nombre, estilo, estado, fecha_creacion | N/A |
| 2 | RecetaVersiones | recipe_version_id, receta_id, version_num, og_target, fg_target, abv_target, ibu_target, srm_target, costo_estimado_litro | → Recetas (receta_id) |
| 3 | Lotes | batch_id, recipe_version_id, volumen_litros, og_medido, fg_medido, estado | → RecetaVersiones (recipe_version_id) |
| 4 | LoteMediciones | medicion_id, batch_id, tipo_medicion, valor, fecha | → Lotes (batch_id) |
| 5 | ItemsInventario | item_id, nombre, tipo, stock_actual, costo_unitario, proveedor_id | → Proveedores |
| 6 | MovimientosInventario | movimiento_id, item_id, tipo_movimiento, cantidad, fecha | → ItemsInventario |
| 7 | Proveedores | proveedor_id, nombre, contacto, email | N/A |
| 8 | LotesInsumo | lote_insumo_id, item_id, proveedor_id, fecha_vencimiento | → ItemsInventario, Proveedores |
| 9 | ConsumosLote | consumo_id, batch_id, item_id, lote_insumo_id, cantidad | → Lotes, ItemsInventario, LotesInsumo |
| 10 | Productos | producto_id, nombre, receta_id, precio_venta, costo_unitario | → Recetas |
| 11 | Clientes | cliente_id, nombre, tipo, canal | N/A |
| 12 | Ventas | venta_id, cliente_id, fecha, total, estado_pago, saldo | → Clientes |
| 13 | VentasLineas | linea_id, venta_id, producto_id, cantidad, subtotal | → Ventas, Productos |
| 14 | Pagos | pago_id, venta_id, fecha, monto | → Ventas |
| 15 | FulfillmentVentaLote | fulfillment_id, venta_linea_id, batch_id, cantidad_litros | → VentasLineas, Lotes |

**Relaciones Clave**:
- `Recetas.receta_id` → `RecetaVersiones.receta_id` (1:N)
- `Lotes.recipe_version_id' → 'RecetaVersiones.recipe_version_id` (1:N)
- `Lotes.batch_id` → `LoteMediciones.batch_id` (1:N)
- `Lotes.batch_id` → `ConsumosLote.batch_id` (1:N)
- `Lotes.batch_id` → `FulfillmentVentaLote.batch_id` (1:N)
- `ItemsInventario.item_id` → `MovimientosInventario.item_id` (1:N)
- `ItemsInventario.item_id` → `ConsumosLote.item_id` (1:N)
- FK: `ConsumosLote.lote_insumo_id` → `LotesInsumo.lote_insumo_id` (N:1)
- `Ventas.venta_id` → `VentasLineas.venta_id` (1:N)
- `Ventas.venta_id` → `Pagos.venta_id` (1:N)
- `VentasLineas.linea_id` → `FulfillmentVentaLote.venta_linea_id` (1:N)

**Nota**: en Excel se validará la FK con Data Validation / XLOOKUP para evitar ids inexistentes.

---

## E. KPIs y Dashboards Mínimos

### E1. 5 KPIs Principales

| # | KPI | Descripción | Cálculo | Origen de Datos |
|---|-----|-------------|---------|-----------------|
| 1 | Costo por Litro | Costo promedio de producción por litro | `SUM(costo_real_batch) / SUM(volumen_litros)` | Lotes |
| 2 | Margen % Promedio | Margen de ganancia promedio por producto | `AVG(margen_porcentaje)` | Productos |
| 3 | Rotación de Stock | Días promedio para agotar stock actual | `stock_actual / (consumo_mensual_promedio * 30)` | ItemsInventario, MovimientosInventario |
| 4 | Stock Crítico | Ítems por debajo del mínimo | `COUNT(item_id) WHERE stock_actual < stock_minimo` | ItemsInventario |
| 5 | Lotes en Curso/Atrasados | Lotes no completados por fecha esperada | `COUNT(batch_id) WHERE estado != 'completado'` | Lotes |

### E2. 3 Dashboards Mínimos

**Dashboard 1: Costos**

| Gráfico | Tipo | Fuente | Métricas |
|---------|------|--------|----------|
| Costo por Lote (histórico) | Línea | Lotes | costo_real_batch por batch_id |
| Costo por Litro por Receta | Barras | Lotes, Recetas | AVG(costo_real_batch/volumen_litros) GROUP BY receta_id |
| Top 5 Insumos por Costo | Barras | ConsumosLote, ItemsInventario | SUM(cantidad*costo_unitario) GROUP BY item_id |

**Dashboard 2: Stock Crítico**

| Gráfico | Tipo | Fuente | Métricas |
|---------|------|--------|----------|
| Ítems bajo Stock Mínimo | Tabla | ItemsInventario | item_id, nombre, stock_actual, stock_minimo |
| Rotación de Stock | Barras | ItemsInventario | días_rotación por item_id |
| Movimientos de Inventario (últimos 30 días) | Línea | MovimientosInventario | COUNT(movimiento_id) por tipo_movimiento, fecha |

**Dashboard 3: Lotes en Curso**

| Gráfico | Tipo | Fuente | Métricas |
|---------|------|--------|----------|
| Lotes por Estado | Pie | Lotes | COUNT(batch_id) por estado |
| Tiempo por Etapa (promedio) | Barras | Lotes | AVG(fecha_siguiente - fecha_anterior) por estado |
| Cumplimiento de Especificaciones (OG/FG/ABV) | Tabla | Lotes, Recetas | % lotes dentro de target por receta_id |

---

## F. Convenciones Excel

### F1. Formato de Tablas (Excel Table)

**Convenciones**:
- Cada tabla debe ser una "Tabla de Excel" (Insertar → Tabla)
- Nombres de tablas: `tbl_` + nombre entidad (ej: `tbl_Lotes`, `tbl_ItemsInventario`)
- Sin filas vacías entre datos
- Sin filas de resumen mezcladas con datos

**Nombres de Columnas**:
- Sin espacios: usar guiones bajos o camelCase
- Idioma: español, sin acentos
- Ejemplos: `batch_id`, `nombre_receta`, `volumen_litros`

### F2. Validaciones de Datos

**Estados**:
- `Recetas.estado`: `={"activa";"archivada";"experimental"}`
- `Lotes.estado`: `={"planificado";"coccion";"fermentacion";"maduracion";"envasado";"completado";"cancelado"}`
- `ItemsInventario.estado`: `={"activo";"inactivo"}`
- `Ventas.estado_pago`: `={"pendiente";"pagado_parcial";"pagado"}`

**Tipos de Datos**:
- **Fechas**: Formato `YYYY-MM-DD`, usar validación de datos tipo fecha
- **Números**: Sin formato de texto, usar celdas numéricas
- **Texto**: Para IDs y nombres descriptivos
- **Moneda**: Formato `$#,##0.00` o `ARS`, no texto con símbolo

**Listas Desplegables**:
- Usar validación de datos → Lista → Referencia a rango con opciones
- Ejemplo: Estados en hoja auxiliar `_Listas` para centralizar opciones

### F3. Convenciones de Naming

**Mezcla ES/EN en Excel**:
- Nombres de columnas: mezcla de español e inglés aceptada (ej: `batch_id`, `nombre_receta`)
- Razonamiento: `batch_id`, `recipe_version_id`, `item_id` mantienen consistencia técnica con ACI
- Nombres de tablas: en español (`Recetas`, `Lotes`, `ItemsInventario`)
- Esta mezcla se normalizará a inglés completo en la web-app futura

**Patrones de Nombres**:
- IDs: `_id` en minúscula (ej: `receta_id`, `batch_id`)
- FKs: mismas convenciones que IDs (ej: `recipe_version_id`, `lote_insumo_id`)
- Texto descriptivo: español sin acentos (ej: `nombre`, `estado`, `tipo`)

### F4. Reglas para Evitar Errores Comunes

**Texto vs Número**:
- IDs: siempre texto (ej: `LOTE-2024-001`)
- Cantidades y valores: siempre número (ej: `123.45`, no `"123"`)
- Fechas: formato fecha nativo de Excel, no texto (ej: `2024-01-15`, no `"15/01/2024"`)

**Validación de Referencias**:
- Usar `BUSCARV` o `XLOOKUP` para validar que IDs referenciados existen
- Ejemplo: validar que `recipe_version_id` en Lotes existe en Recetas
- Opción avanzada: Power Query para cargar tablas y crear relaciones

**Evitar Newlines Embebidos**:
- No usar Alt+Enter en celdas de datos
- Si es necesario notas multilínea, usar hoja auxiliar `Notas` con `entidad_id` + `notas`

**UTF-8 BOM**:
- Al exportar a CSV, usar UTF-8 con BOM para compatibilidad con caracteres especiales
- En Excel: Guardar como → CSV UTF-8 (delimitado por comas) [ajustar delimitador si es necesario]

---

## G. Checklist Rápido de Implementación

1. ✅ Crear tablas de Excel con nombres `tbl_*`
2. ✅ Definir columnas con tipos correctos
3. ✅ Crear validaciones de datos para listas desplegables
4. ✅ Crear fórmulas para cálculos automáticos (costos, márgenes)
5. ✅ Crear hoja `KPIs` con 5 KPIs
6. ✅ Crear 3 hojas de dashboard con gráficos
7. ✅ Implementar trazabilidad insumo→lote→venta
8. ✅ Probar import CSV desde ACI (delimiter=semicolon)
9. ✅ Probar export CSV desde Excel (delimiter=semicolon)

---

**Fin de Especificación**
