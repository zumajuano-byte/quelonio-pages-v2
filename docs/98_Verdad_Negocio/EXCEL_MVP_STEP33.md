# Excel MVP - Paso 33: UX Mínima (Home y Ayuda)

## Resumen

Este paso agrega UX mínima al Excel MVP sin modificar las tablas existentes, mejorando la usabilidad del sistema.

## Archivos Generados/Modificados

### 1. tools/build_excel_mvp_step33.py
Script principal que genera/actualiza el Excel con hojas de UX.

**Funcionalidades:**
- Crea backup automático del archivo Excel existente
- Crea hoja "00_Home" como primera hoja con navegación
- Crea hoja "98_Ayuda" con documentación del sistema
- Preserva todas las hojas y tablas existentes
- No modifica headers de tablas

### 2. tools/test_step33.py
Script de test determinista que verifica:
- Existencia y posición correcta de 00_Home
- Existencia de 98_Ayuda
- Preservación de hoja Catalogos (Step 32)
- Preservación de nombres definidos lst_* (Step 32)
- Existencia de >=10 hipervínculos internos en Home
- Conteo total de hojas >= 17
- Integridad de tablas originales

### 3. data/excel/Quelonio_Excel_MVP_Skeleton.xlsx
Archivo Excel modificado con nuevas hojas de UX.

## Cambios Realizados

### A. Hoja 00_Home (Primera hoja)

**Secciones:**

1. **Título Principal**
   - "QUELONIO - Sistema de Gestión Cervecera"
   - Fondo azul (4472C4), texto blanco, fuente grande y bold

2. **Orden de Carga**
   - Lista ordenada con bullets de los pasos recomendados para cargar datos
   - Incluye:
     1. ItemsInventario (materias primas)
     2. Proveedores
     3. LotesInsumo (lotes de materias primas)
     4. Recetas y RecetaVersiones
     5. Clientes y Productos
     6. Lotes (producción)
     7. Ventas, VentasLineas y Pagos
     8. FulfillmentVentaLote
     9. MovimientosInventario (ajustes)

3. **Accesos Rápidos**
   - Hipervínculos internos a 12 hojas clave del sistema
   - Formato: flecha (→) + nombre de hoja con hipervínculo
   - Color azul subrayado (estilo típico de hipervínculos)

**Hojas con hipervínculo:**
- 01_Recetas
- 02_RecetaVersiones
- 03_Lotes
- 05_ItemsInventario
- 08_LotesInsumo
- 09_ConsumosLote
- 10_Productos
- 11_Clientes
- 12_Ventas
- 13_VentasLineas
- 14_Pagos
- 15_FulfillmentVentaLote

### B. Hoja 98_Ayuda

**Contenido organizado en 5 secciones:**

1. **Convención de IDs**
   - Los IDs son texto y se auto-generan
   - Formato sugerido: PREFIX_XXXX (ej: RECETA_0001)
   - Usar ID cuando se necesite referencia única
   - No modificar IDs existentes para mantener integridad

2. **Orden Recomendado de Carga**
   - Lista detallada de 12 pasos en orden lógico
   - Comienza con materias primas y proveedores
   - Termina con ajustes de inventario
   - Incluye dependencias entre entidades

3. **Claves Foráneas (FKs)**
   - Explicación de concepto de FKs
   - Validación mediante listas (lst_*)
   - Ejemplo práctico de referencia
   - Actualización automática de listas

4. **Catálogos**
   - Explicación de hoja Catalogos
   - Uso para campos tipo enum
   - Validación mediante dropdown
   - Lista de 6 catálogos disponibles

5. **Columnas Calculadas**
   - `abv_estimado` en Lotes
   - `total_calc`, `pagos_calc`, `saldo_calc` en Ventas
   - Explicación de fórmulas SUMIF
   - Lógica de cálculo de saldo

### C. Estilo Visual

**Colores:**
- Título: Azul oscuro (4472C4)
- Secciones: Azul medio (5B9BD5)
- Hipervínculos: Azul con subrayado (0563C1)

**Formato:**
- Títulos: Fuente grande (18-20pt), bold, blanco
- Secciones: Fuente media (14pt), bold, blanco
- Contenido: Fuente normal (11pt)
- Alineación: Centrada para títulos, izquierda para contenido
- Wrap text habilitado para contenido largo

### D. Preservación de Estructura Existente

**Mantenido sin modificaciones:**
- ✅ Todas las hojas originales de Step 31
- ✅ Hoja Catalogos de Step 32
- ✅ Todos los headers de tablas
- ✅ Todas las columnas (incluyendo calculadas de Step 32)
- ✅ Todos los nombres definidos
- ✅ Todas las validaciones de datos
- ✅ Todas las tablas originales

## Cómo Correr

### Generar/Actualizar Excel (Paso 33)

```bash
python tools/build_excel_mvp_step33.py
```

Esto:
1. Crea backup en `data/excel/_backups/` con timestamp
2. Agrega hoja 00_Home como primera hoja
3. Agrega hoja 98_Ayuda
4. Preserva todo lo de pasos anteriores
5. Guarda el archivo actualizado

### Ejecutar Tests (Paso 33)

```bash
python tools/test_step33.py
```

Verifica:
- 00_Home existe y es primera hoja
- 98_Ayuda existe
- Catalogos existe (preservado)
- Nombres definidos Step 32 preservados
- Home tiene >=10 hipervínculos
- Total de hojas >= 17
- Tablas originales intactas

### Ejecutar Tests de Pasos Anteriores

```bash
# Test Paso 31
python tools/test_step31.py

# Test Paso 32
python tools/test_step32.py
```

## Compatibilidad

### Preservación de Pasos Anteriores

**Paso 31 - Estructura Base:**
- ✅ Todas las 15 tablas originales
- ✅ Headers de todas las tablas
- ✅ Nombres definidos LIST_*
- ✅ Validaciones de datos originales

**Paso 32 - Funcionalidad Operativa:**
- ✅ Hoja Catalogos
- ✅ Nombres definidos lst_*
- ✅ Columnas calculadas (abv_estimado, total_calc, etc.)
- ✅ Validaciones de datos adicionales

**Paso 33 - UX:**
- ✅ Hoja 00_Home (nueva, primera)
- ✅ Hoja 98_Ayuda (nueva)
- ✅ Preservación total de estructura

## Estructura del Excel Final

**Total de hojas:** 19

1. **00_Home** (NUEVA - Primera)
2. 01_Recetas
3. 02_RecetaVersiones
4. 03_Lotes
5. 04_LoteMediciones
6. 05_ItemsInventario
7. 06_MovimientosInventario
8. 07_Proveedores
9. 08_LotesInsumo
10. 09_ConsumosLote
11. 10_Productos
12. 11_Clientes
13. 12_Ventas
14. 13_VentasLineas
15. 14_Pagos
16. 15_FulfillmentVentaLote
17. 98_Ayuda (NUEVA)
18. 99_Listas
19. Catalogos

## Resultados de Tests

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
- ✅ Data Validation (28)
- ✅ Excel Tables (15)

## Backup Automático

Cada ejecución del script de build crea un backup:

```
data/excel/_backups/Quelonio_Excel_MVP_Skeleton_step33_YYYYMMDD_HHMMSS.xlsx
```

Ejemplo: `Quelonio_Excel_MVP_Skeleton_step33_20260114_191545.xlsx`

## Detalles de Implementación

### Hipervínculos Internos

**Fórmula utilizada:**
```
=HYPERLINK("#'SHEET_NAME'!A1","SHEET_NAME")
```

Ejemplo:
```
=HYPERLINK("#'01_Recetas'!A1","01_Recetas")
```

Esto crea un hipervínculo que navega a la celda A1 de la hoja especificada.

### Posicionamiento de Hojas

- `00_Home` se crea en `index=0` (primera hoja)
- `98_Ayuda` se crea al final (hoja 17, antes de 99_Listas)
- Las demás hojas mantienen su orden relativo

### Estilo Visual

- **Fuentes:** Calibri (default de Excel)
- **Colores RGB:**
  - Azul oscuro: (68, 114, 196) - #4472C4
  - Azul medio: (91, 155, 213) - #5B9BD5
  - Hipervínculo: (5, 99, 193) - #0563C1
- **Alineación:**
  - Títulos: horizontal=centrado, vertical=centrado
  - Contenido: horizontal=izquierda, vertical=centrado, wrap_text=True

### Determinismo

- ✅ El script es completamente determinista
- ✅ Mismo input → mismo output
- ✅ Tests verifican comportamiento específico

### Manejo de Errores

- ✅ Fails con error claro si no puede cargar el archivo
- ✅ Reemplaza hojas existentes si ya existen
- ✅ Verifica existencia de hojas antes de crear hipervínculos
- ✅ Preserva estructura existente sin modificaciones

## Beneficios de UX Agregada

### 00_Home

**Navegación Rápida:**
- Un punto de entrada central al archivo
- Hipervínculos directos a todas las hojas clave
- Reducción de tiempo para navegar entre hojas

**Orden de Carga:**
- Guía clara para usuarios nuevos
- Previene errores de dependencia
- Asegura integridad referencial

### 98_Ayuda

**Documentación Integrada:**
- No necesita documentación externa
- Siempre disponible en el mismo archivo
- Fácil de mantener y actualizar

**Explicación de Conceptos:**
- IDs, FKs, catálogos explicados claramente
- Ejemplos prácticos incluidos
- Reducen la curva de aprendizaje

## Flujo de Trabajo Sugerido

### Para Usuarios Nuevos:

1. Abrir el archivo Excel
2. Leer la hoja 00_Home
3. Consultar 98_Ayuda si tienen dudas
4. Seguir el orden de carga sugerido
5. Usar los accesos rápidos para navegar

### Para Usuarios Experimentados:

1. Usar 00_Home como página de inicio
2. Navegar directamente a hojas de interés
3. Consultar 98_Ayuda como referencia rápida
4. Beneficiarse de validaciones y cálculos automáticos

## Próximos Pasos

Paso 34 podría incluir:
- Formato condicional para datos problemáticos
- Dashboard básico con KPIs
- Gráficos de ventas y producción
- Vistas filtradas o segmentadas
- Macros simples para tareas repetitivas
- Integración con RAG/ACI system

## Referencias

- Especificación original: `docs/98_Verdad_Negocio/EXCEL_MVP_SPEC.md`
- Documentación Paso 31: `docs/98_Verdad_Negocio/EXCEL_MVP_STEP31.md`
- Documentación Paso 32: `docs/98_Verdad_Negocio/EXCEL_MVP_STEP32.md`
- Librería openpyxl: https://openpyxl.readthedocs.io/

## Notas Importantes

- **Sin Macros/VBA:** La UX se implementa sin usar VBA, manteniendo compatibilidad total
- **Sin modificación de tablas:** Los datos y estructura de tablas permanecen intactos
- **Retrocompatibilidad:** Tests de pasos anteriores siguen pasando
- **Determinismo:** Todo es reproducible y testeable
- **Backups automáticos:** Cada modificación crea un backup con timestamp
