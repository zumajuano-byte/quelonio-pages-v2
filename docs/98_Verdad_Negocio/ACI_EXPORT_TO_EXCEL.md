# ACI Export to Excel - Guía de Comandos

**Objetivo**: Documentar comandos para exportar datos desde ACI a Excel vía CSV.

---

## Configuración Base

**Endpoint**: `/export/run`

**Parámetros obligatorios**:
- `format=csv`

**Parámetros recomendados para Excel AR**:
- `delimiter=semicolon`

**URL base**:
```
http://localhost:8080/export/run
```
(Ajustar host y puerto según configuración de ACI)

---

## Comandos de Export

### Exportar Entidad Específica

**Sintaxis**:
```
http://localhost:8080/export/run?entity={ENTIDAD}&format=csv&delimiter=semicolon
```

**Entidades disponibles**:
- `recetas`
- `lotes`
- `inventario`
- `proveedores`
- `ventas`
- `clientes`

---

### Ejemplos

#### 1. Exportar Recetas

**CURL**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=recetas&format=csv&delimiter=semicolon" -o recetas.csv
```

**Navegador**:
```
http://localhost:8080/export/run?entity=recetas&format=csv&delimiter=semicolon
```

---

#### 2. Exportar Lotes

**CURL**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=lotes&format=csv&delimiter=semicolon" -o lotes.csv
```

**Navegador**:
```
http://localhost:8080/export/run?entity=lotes&format=csv&delimiter=semicolon
```

---

#### 3. Exportar Inventario

**CURL**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=inventario&format=csv&delimiter=semicolon" -o inventario.csv
```

**Navegador**:
```
http://localhost:8080/export/run?entity=inventario&format=csv&delimiter=semicolon
```

---

#### 4. Exportar Proveedores

**CURL**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=proveedores&format=csv&delimiter=semicolon" -o proveedores.csv
```

**Navegador**:
```
http://localhost:8080/export/run?entity=proveedores&format=csv&delimiter=semicolon
```

---

#### 5. Exportar Ventas

**CURL**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=ventas&format=csv&delimiter=semicolon" -o ventas.csv
```

**Navegador**:
```
http://localhost:8080/export/run?entity=ventas&format=csv&delimiter=semicolon
```

---

#### 6. Exportar Clientes

**CURL**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=clientes&format=csv&delimiter=semicolon" -o clientes.csv
```

**Navegador**:
```
http://localhost:8080/export/run?entity=clientes&format=csv&delimiter=semicolon
```

---

## Exportar usando Presets

**Endpoint**: `/presets/run`

**Sintaxis**:
```
http://localhost:8080/presets/run?preset={PRESET}&format=csv&delimiter=semicolon
```

**Presets disponibles**:
- `produccion` (Recetas + Lotes)
- `inventario_completo` (Inventario + Proveedores)
- `ventas_completas` (Ventas + Clientes + Líneas)
- `todo` (Todas las entidades)

---

### Ejemplos con Presets

#### 1. Exportar Producción

**CURL**:
```bash
curl -X GET "http://localhost:8080/presets/run?preset=produccion&format=csv&delimiter=semicolon" -o produccion.zip
```

**Resultado**: ZIP con `recetas.csv` y `lotes.csv`

---

#### 2. Exportar Inventario Completo

**CURL**:
```bash
curl -X GET "http://localhost:8080/presets/run?preset=inventario_completo&format=csv&delimiter=semicolon" -o inventario.zip
```

**Resultado**: ZIP con `inventario.csv` y `proveedores.csv`

---

#### 3. Exportar Ventas Completas

**CURL**:
```bash
curl -X GET "http://localhost:8080/presets/run?preset=ventas_completas&format=csv&delimiter=semicolon" -o ventas.zip
```

**Resultado**: ZIP con `ventas.csv`, `clientes.csv` y `ventas_lineas.csv`

---

#### 4. Exportar Todo

**CURL**:
```bash
curl -X GET "http://localhost:8080/presets/run?preset=todo&format=csv&delimiter=semicolon" -o todo.zip
```

**Resultado**: ZIP con todas las entidades

---

## Parámetros Avanzados

### Filtrado por Fechas

**Sintaxis**:
```
...&fecha_desde=YYYY-MM-DD&fecha_hasta=YYYY-MM-DD
```

**Ejemplo**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=lotes&format=csv&delimiter=semicolon&fecha_desde=2024-01-01&fecha_hasta=2024-12-31" -o lotes_2024.csv
```

---

### Filtrado por Estado

**Sintaxis**:
```
...&estado={ESTADO}
```

**Ejemplo**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=lotes&format=csv&delimiter=semicolon&estado=completado" -o lotes_completados.csv
```

---

### Control de Formato Flat vs Saltos de Línea

**Comportamiento default**:
- `csv_flat=1` (default): Exporta datos como "flat", sin newlines embebidos
- Ideal para Excel porque evita celdas multilínea problemáticas

**Preservar saltos de línea**:
- `csv_flat=0`: Mantiene newlines embebidos en campos de texto
- **Advertencia**: Excel puede truncar celdas con múltiples líneas

**Ejemplo con saltos de línea**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=notas&format=csv&delimiter=semicolon&csv_flat=0" -o notas.csv
```

**Ejemplo forzando flat (explicit)**:
```bash
curl -X GET "http://localhost:8080/export/run?entity=recetas&format=csv&delimiter=semicolon&csv_flat=1" -o recetas_flat.csv
```

---

## Importar CSV en Excel

### Método 1: Desde la Interfaz de Excel

1. Abrir Excel
2. Ir a **Datos** → **Obtener datos** → **Desde texto/CSV**
3. Seleccionar el archivo `.csv` exportado
4. Configurar:
   - **Delimitador**: Punto y coma
   - **Codificación**: UTF-8
   - **Detectar tipos de datos**: Automático
5. Cargar en hoja existente o nueva

---

### Método 2: Arrastrar y Soltar

1. Abrir Excel
2. Arrastrar el archivo `.csv` a una celda vacía
3. Excel abrirá el asistente de importación de texto
4. Configurar delimitador = Punto y coma
5. Finalizar importación

---

## Notas Importantes

### UTF-8 BOM

Si el CSV tiene caracteres especiales (ñ, á, é, ñ, etc.):
- Asegurarse de que el archivo sea UTF-8 con BOM
- Si no funciona, usar **Datos → Obtener datos** (método 1)

---

### Excel AR (Argentina)

**Configuración regional**:
- Windows: Configuración → Región → Español (Argentina)
- Separador de listas: `;` (punto y coma)
- Por eso se recomienda `delimiter=semicolon`

**Validación**:
- Después de importar, verificar que números se reconozcan como números (no texto)
- Verificar que fechas se reconozcan como fechas (no texto)

---

### Power Query (Avanzado)

Para automatizar importaciones periódicas:

1. **Datos** → **Obtener datos** → **Desde Web**
2. Ingresar URL del endpoint ACI:
   ```
   http://localhost:8080/export/run?entity=recetas&format=csv&delimiter=semicolon
   ```
3. Configurar delimitador en el editor de Power Query
4. Cargar en tabla
5. **Clic derecho en tabla** → **Actualizar** para actualizar datos

---

## Solución de Problemas

### Problema: Números importados como texto

**Causa**: Delimitador incorrecto o configuración regional

**Solución**:
1. Verificar que se usó `delimiter=semicolon`
2. Verificar configuración regional de Windows
3. Usar **Datos → Obtener datos** (método 1) para mayor control

---

### Problema: Fechas no se reconocen

**Causa**: Formato de fecha incompatible

**Solución**:
1. Verificar que ACI exporta fechas en formato `YYYY-MM-DD`
2. Usar **Datos → Obtener datos** → Transformar datos
3. En Power Query, cambiar tipo de columna a Fecha

---

### Problema: Caracteres especiales incorrectos

**Causa**: Codificación incorrecta

**Solución**:
1. Asegurarse de que el archivo es UTF-8 con BOM
2. Usar **Datos → Obtener datos** y seleccionar codificación UTF-8
3. Si persiste, abrir el CSV en un editor de texto (Notepad++, VS Code) y guardar como UTF-8 con BOM

---

### Problema: Celdas con múltiples líneas truncadas

**Causa**: `csv_flat=0` y Excel no maneja newlines

**Solución**:
1. Usar default `csv_flat=1` (sin newlines embebidos)
2. Si se necesita contenido multilínea, crear hoja auxiliar `Notas` con `entidad_id` como clave
3. No usar Alt+Enter en celdas de datos principales

---

## Resumen de Comandos Rápidos

| Entidad | Comando CURL |
|---------|--------------|
| Recetas | `curl -X GET "http://localhost:8080/export/run?entity=recetas&format=csv&delimiter=semicolon" -o recetas.csv` |
| Lotes | `curl -X GET "http://localhost:8080/export/run?entity=lotes&format=csv&delimiter=semicolon" -o lotes.csv` |
| Inventario | `curl -X GET "http://localhost:8080/export/run?entity=inventario&format=csv&delimiter=semicolon" -o inventario.csv` |
| Proveedores | `curl -X GET "http://localhost:8080/export/run?entity=proveedores&format=csv&delimiter=semicolon" -o proveedores.csv` |
| Ventas | `curl -X GET "http://localhost:8080/export/run?entity=ventas&format=csv&delimiter=semicolon" -o ventas.csv` |
| Clientes | `curl -X GET "http://localhost:8080/export/run?entity=clientes&format=csv&delimiter=semicolon" -o clientes.csv` |
| Producción (Preset) | `curl -X GET "http://localhost:8080/presets/run?preset=produccion&format=csv&delimiter=semicolon" -o produccion.zip` |
| Inventario Completo (Preset) | `curl -X GET "http://localhost:8080/presets/run?preset=inventario_completo&format=csv&delimiter=semicolon" -o inventario.zip` |
| Ventas Completas (Preset) | `curl -X GET "http://localhost:8080/presets/run?preset=ventas_completas&format=csv&delimiter=semicolon" -o ventas.zip` |
| Todo (Preset) | `curl -X GET "http://localhost:8080/presets/run?preset=todo&format=csv&delimiter=semicolon" -o todo.zip` |

---

**Fin de Guía**
