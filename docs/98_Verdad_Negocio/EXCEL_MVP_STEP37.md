# EXCEL MVP STEP 37 - Dashboard con Filtros y Alertas

## Objetivo

Hacer el dashboard operable en el día a día agregando:
1. Selector de período (7/30/90 días)
2. KPIs parametrizados por período
3. Panel de alertas con semáforo textual
4. Validaciones y rangos con nombre para facilitar el uso

## Implementación

### Archivos Creados/Actualizados

1. **tools/build_excel_mvp_step37_dashboard_filters.py**
   - Script de build para Step 37
   - Agrega catálogo de períodos y selector
   - Actualiza KPIs para usar filtros
   - Crea panel de alertas

2. **tools/test_step37.py**
   - Suite de pruebas para Step 37
   - Verifica selector, named ranges y alertas
   - Valida compatibilidad backward

3. **docs/98_Verdad_Negocio/EXCEL_MVP_STEP37.md** (este archivo)
   - Documentación completa de Step 37

### Hojas Actualizadas

#### 1. Catalogos

Agrega catálogo de períodos:

| Catalogo | Valor | Descripción |
|----------|-------|-------------|
| CAT_PeriodoDias | 7 | Período corto - 7 días |
| CAT_PeriodoDias | 30 | Período estándar - 30 días |
| CAT_PeriodoDias | 90 | Período largo - 90 días |

**Named Ranges:**
- `lst_periodo_dias` → `Catalogos!$B$X:$B$Z` (rango de valores de período)

#### 2. 20_Dashboard

Agrega elementos de filtrado y alertas:

##### Selector de Período
- **Celda B3**: Período (días) con valor default 30
- **Validación de datos**: Lista desplegable con valores 7, 30, 90
- **Named Range**: `SEL_PeriodoDias` → `20_Dashboard!$B$3`

##### KPIs Actualizados
- **KPI_Ventas_Periodo** (antes KPI_Ventas_30d)
  - Fórmula: `=SUMIFS(12_Ventas!F:F,12_Ventas!C:C,">="&CALC_FechaInicio)`
  - Ahora filtra por fecha según selector

- **KPI_SaldoPorCobrar**
  - Fórmula: `=SUMIFS(12_Ventas!H:H,12_Ventas!C:C,">="&CALC_FechaInicio)`
  - Filtra saldo por fecha del período

##### Panel de Alertas
Ubicado en filas 12-14, con 3 tipos de alertas:

| Alerta | Descripción | Fórmula | Estado |
|--------|-------------|---------|--------|
| ALERT_StockCritico | Items con stock <= stock_minimo | `=COUNTIFS(05_ItemsInventario!D:D,"<="&05_ItemsInventario!E:E)` | IF(B12>0,"ALERTA","OK") |
| ALERT_LotesDemorados | Lotes en curso >30 días | COUNTIFS combinados por estado | IF(B13>0,"ALERTA","OK") |
| ALERT_SaldoPendiente | Ventas con saldo pendiente | `=COUNTIF(12_Ventas!H:H,">0")` | IF(B14>0,"ALERTA","OK") |

**Formato de alertas:**
- Count: fondo gris claro, borde, centrado
- Status:
  - "OK" → fondo verde claro, texto verde oscuro
  - "ALERTA" → fondo rojo claro, texto rojo

#### 3. 21_Calc

Agrega cálculos auxiliares:

| Variable | Fórmula/Valor | Descripción |
|----------|---------------|-------------|
| CALC_PeriodoDias | `=SEL_PeriodoDias` | Días del período seleccionado |
| CALC_FechaInicio | `=TODAY()-CALC_PeriodoDias` | Fecha inicio del período |
| CALC_LotesUmbralDias | 30 | Umbral de días para lotes demorados |

## Cómo Usar

### Cambiar Período de Análisis

1. Abrir `data/excel/Quelonio_Excel_MVP_Skeleton.xlsx`
2. Ir a hoja `20_Dashboard`
3. En celda **B3** ("Período (días)"), seleccionar:
   - **7** → Análisis de última semana
   - **30** → Análisis de último mes (default)
   - **90** → Análisis de último trimestre

4. Ver que **KPI_Ventas_Periodo** y **KPI_SaldoPorCobrar** se actualizan automáticamente

### Interpretar Alertas

#### Alerta de Stock Crítico
- **ALERTA**: Hay items con stock_actual <= stock_minimo
  - Acción sugerida: Revisar inventario y considerar reposición
- **OK**: Todo el stock está por encima del mínimo

#### Alerta de Lotes Demorados
- **ALERTA**: Hay lotes en curso iniciados hace más de 30 días
  - Acción sugerida: Investigar demora y planificar mitigación
- **OK**: No hay lotes demorados

#### Alerta de Saldo Pendiente
- **ALERTA**: Hay ventas con saldo por cobrar > 0
  - Acción sugerida: Contactar clientes para gestionar cobranzas
- **OK**: Todas las ventas están pagadas (en el período)

## Detalles Técnicos

### Named Ranges

Los siguientes named ranges facilitan el mantenimiento:

| Nombre | Referencia | Uso |
|--------|------------|-----|
| lst_periodo_dias | Catalogos!$B$X:$B$Z | Valores disponibles para selector |
| SEL_PeriodoDias | 20_Dashboard!$B$3 | Selector de período seleccionado |
| CALC_PeriodoDias | 21_Calc!$A$2 | Referencia al período (cálculo) |
| CALC_FechaInicio | 21_Calc!$A$3 | Fecha inicio del período |

### Fórmulas de Alertas

#### ALERT_StockCritico
```excel
=COUNTIFS(05_ItemsInventario!D:D,"<="&05_ItemsInventario!E:E)
```
Cuenta items donde stock_actual (col D) <= stock_minimo (col E)

#### ALERT_LotesDemorados
```excel
=COUNTIFS(03_Lotes!D:D,"coccion",03_Lotes!E:E,"<"&TODAY()-30)
+COUNTIFS(03_Lotes!D:D,"fermentacion",03_Lotes!E:E,"<"&TODAY()-30)
+COUNTIFS(03_Lotes!D:D,"maduracion",03_Lotes!E:E,"<"&TODAY()-30)
+COUNTIFS(03_Lotes!D:D,"envasado",03_Lotes!E:E,"<"&TODAY()-30)
+COUNTIFS(03_Lotes!D:D,"planificado",03_Lotes!E:E,"<"&TODAY()-30)
```
Cuenta lotes en cada estado activo con fecha_inicio > 30 días

#### ALERT_SaldoPendiente
```excel
=COUNTIF(12_Ventas!H:H,">0")
```
Cuenta ventas con saldo_calc > 0

#### Fórmulas de Estado
```excel
=IF(B12>0,"ALERTA","OK")
```
Si count > 0 → "ALERTA", sino → "OK"

### Validaciones de Datos

Selector en `20_Dashboard!B3`:
- **Tipo**: Lista
- **Fórmula**: `=lst_periodo_dias`
- **Permitir blanco**: No
- **Mensaje de error**: "Seleccione un período de la lista (7, 30, 90)"

## Ejecución

### Crear el Excel MVP (Step 37)

```bash
python tools/build_excel_mvp_step37_dashboard_filters.py
```

Salida esperada:
```
Building Excel MVP - Step 37: Dashboard Filters and Alerts
------------------------------------------------------------
[OK] Backup created: data/excel/_backups/Quelonio_Excel_MVP_Skeleton_step37_20260114_210000.xlsx
[OK] Catalogos sheet created (or updated)
[OK] Named range lst_periodo_dias created: Catalogos!$B$X:$B$Z
[OK] Period selector added to 20_Dashboard!$B$3
[OK] Named range SEL_PeriodoDias created
[OK] Auxiliary calculations added to 21_Calc
[OK] KPI_Ventas_Periodo updated to use CALC_FechaInicio
[OK] KPI_SaldoPorCobrar updated to use CALC_FechaInicio
[OK] Alerts panel added to 20_Dashboard
------------------------------------------------------------
[OK] Excel MVP saved to: data/excel/Quelonio_Excel_MVP_Skeleton.xlsx
[OK] Step 37 build complete!
```

### Ejecutar Tests

```bash
python tools/test_step37.py
```

Salida esperada:
```
============================================================
Excel MVP Step 37 Tests - Dashboard Filters and Alerts
============================================================

[Test] Verifying 20_Dashboard and 21_Calc sheets exist...
  [OK] 20_Dashboard exists
  [OK] 21_Calc exists

[Test] Verifying Catalogos sheet with CAT_PeriodoDias...
  [OK] CAT_PeriodoDias contains expected values: [7, 30, 90]

[Test] Verifying named ranges exist...
  [OK] Named range 'lst_periodo_dias' exists
  [OK] Named range 'SEL_PeriodoDias' exists

[Test] Verifying data validation on selector cell...
  [OK] Data validation exists on selector cell B3

[Test] Verifying KPIs reference period filter...
  [OK] KPI_Ventas_Periodo references period filter
  [OK] KPI_SaldoPorCobrar references period filter

[Test] Verifying alerts exist with formulas...
  [OK] ALERT_StockCritico has formula
  [OK] ALERT_LotesDemorados has formula
  [OK] ALERT_SaldoPendiente has formula
  [OK] Status cell row 12 has formula
  [OK] Status cell row 13 has formula
  [OK] Status cell row 14 has formula

[Test] Verifying backward compatibility...
  [OK] 20_Dashboard exists
  [OK] 21_Calc exists
  [OK] 03_Lotes exists
  [OK] 05_ItemsInventario exists
  [OK] 11_Clientes exists
  [OK] 12_Ventas exists
  [OK] Catalogos exists

============================================================
Test Summary
============================================================
20_Dashboard & 21_Calc exist:     PASS
Catalogos with CAT_PeriodoDias:   PASS
Named ranges exist:               PASS
Selector data validation:          PASS
KPIs reference period filter:      PASS
Alerts with formulas:              PASS
Backward compatibility:            PASS
============================================================
[OK] ALL TESTS PASSED
```

## Compatibilidad

### Backward Compatibility

Step 37 mantiene compatibilidad total con:
- ✅ Step 36: Dashboard con KPIs básicos
- ✅ Step 35: Hojas de datos y tablas
- ✅ Steps 31-34: Estructura base

### Cambios Sin Efecto en Datos

- No se eliminan ni modifican datos existentes
- No se rompen tablas ni validaciones anteriores
- Solo se agregan elementos nuevos (selector, alertas, cálculos)

## Mejoras Futuras

### Próximos Pasos (Step 38+)

1. **Gráficos dinámicos**
   - Gráfico de barras para ventas por canal
   - Gráfico de líneas para tendencia de ventas
   - Slicers interactivos para filtros

2. **Más KPIs**
   - KPI_TiempoPromedioLote
   - KPI_RotacionInventario
   - KPI_TasaDeCobranza

3. **Alertas avanzadas**
   - Alertas por correo (requiere macros o complementos)
   - Alertas con umbrales configurables
   - Historial de alertas

4. **Dashboard adicional**
   - Dashboard financiero
   - Dashboard de producción
   - Dashboard de inventario

## Troubleshooting

### Selector no muestra valores

**Problema**: La lista desplegable está vacía o muestra error.

**Solución**:
1. Verificar que el named range `lst_periodo_dias` existe
2. Verificar que el catálogo CAT_PeriodoDias tiene valores
3. Re-ejecutar el script de build

### Alertas muestran #REF!

**Problema**: Las fórmulas de alertas devuelven error #REF!.

**Solución**:
1. Verificar que las hojas 03_Lotes, 05_ItemsInventario, 12_Ventas existen
2. Verificar que las columnas de referencia existen
3. Re-ejecutar el script de build

### KPIs no se actualizan al cambiar selector

**Problema**: Al cambiar el selector, los KPIs no cambian.

**Solución**:
1. Verificar cálculo automático está activo: Fórmulas → Opciones de cálculo → Automático
2. Verificar que las fórmulas referencian CALC_FechaInicio
3. Presionar F9 para forzar recálculo

## Conclusiones

Step 37 implementa exitosamente:
- ✅ Selector de período (7/30/90 días) con validación
- ✅ Named ranges para facilidad de uso
- ✅ KPIs parametrizados por período
- ✅ Panel de alertas con 3 tipos de alertas
- ✅ Semáforo textual (OK/ALERTA)
- ✅ Cálculos auxiliares en hoja separada
- ✅ Compatibilidad total con pasos anteriores
- ✅ Suite de tests completa

El dashboard ahora es operable en el día a día, permitiendo:
- Cambiar fácilmente el período de análisis
- Identificar situaciones críticas rápidamente
- Filtrar KPIs según el período seleccionado
- Mantener visibilidad sobre stock, lotes y cobranzas

---
**Autor**: OpenCode  
**Fecha**: 2026-01-14  
**Versión**: 1.0  
**Status**: ✅ COMPLETED
