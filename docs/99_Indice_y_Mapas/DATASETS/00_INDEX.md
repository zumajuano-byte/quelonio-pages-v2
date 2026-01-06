# DATASETS — Índice operativo (v1)

Este módulo define **datasets operativos** que el asistente y (a futuro) la app pueden usar para **decisiones repetibles** (formulación, verificación contra estilo, cálculos, water treatment).  
La regla es **2 capas**:

- **Capa 1 (segura):** estructura + defaults mínimos + ejemplos de input. Siempre usable.
- **Capa 2 (opcional/condicionada):** se activa solo si contamos con datos reales (p. ej. laboratorio, COA, densidades medidas, etc.).

---

## Tabla de datasets (Capa 1)

| Código | Dataset | Archivos | Para qué sirve |
|---|---|---|---|
| B010 | BJCP 2021 (estilos) | `bjcp_beer_styles_es.json` | Targets por estilo (OG/FG/ABV/IBU/SRM) + validación rápida de receta/lote |
| B011 | Matemática de la cerveza (fórmulas) | `brew_math_formulas.json` | Motor de cálculos (ABV, IBU, color, atenuación, CO₂, dilución, etc.) |
| W010 | Agua (reportes + tratamiento) | `water_report_example.json`, `water_treatment_defaults.json`, `water_profiles_canonical.json` | Normalizar reporte, setear objetivos y sugerir ajustes (sales/ácidos) con defaults |

> Nota: los schemas de estos archivos viven en `DATASETS_SCHEMA.md`.

---

## B010 — BJCP 2021 (estilos)

### Capa 1 (segura)
**Archivo:** `bjcp_beer_styles_es.json`

**Uso operativo:**
- Dado un estilo, recuperar **rangos objetivo** (OG/FG/ABV/IBU/SRM).
- Validar una receta/lote: “¿estoy dentro, cerca o fuera del rango?”
- Derivar objetivos iniciales para Specs (antes de afinar por ingredientes/proceso).

### Capa 2 (opcional/condicionada)
- Descriptores sensoriales extendidos y ejemplos comerciales (si los cargamos).
- Sub-perfiles (p. ej. “NEIPA: soft vs punchy”) con targets propios.

---

## B011 — Matemática de la cerveza (fórmulas)

### Capa 1 (segura)
**Archivo:** `brew_math_formulas.json`

**Uso operativo:**
- Calcular métricas estándar (ABV, atenuación, BU:GU, color, CO₂, diluciones).
- Estandarizar definiciones: variables, unidades, dominios válidos.

### Capa 2 (opcional/condicionada)
- Defaults por estilo (p. ej. CO₂ típico) o por tecnología (kettle, whirlpool, hopstand, etc.).
- Ajustes calibrados a tu planta (eficiencia real, pérdidas, correcciones por densímetro, etc.).

---

## W010 — Agua (reportes + tratamiento)

### Capa 1 (segura)
**Archivos:**
- `water_report_example.json` — **input ejemplo** (estructura de un reporte / carga manual)
- `water_treatment_defaults.json` — **defaults operativos** (sales, ácidos comunes, supuestos mínimos)
- `water_profiles_canonical.json` — **objetivos canónicos** para arrancar (perfiles target por familia de estilo)

**Uso operativo (sin “flashear”):**
1) Normalizar un reporte (ppm + alcalinidad) a una estructura única.
2) Elegir un **objetivo** (perfil canónico o uno propio).
3) Generar una **propuesta inicial** de ajuste con sales/ácidos **usando defaults** (Capa 1).
4) Si hay datos reales (concentración medida, densidades, pH medido en mash), pasar a Capa 2.

### Capa 2 (opcional/condicionada)
- Predicción de pH del mash **solo** si cargamos datos suficientes (grist, agua, temperatura, ácidos exactos, mediciones).
- Split mash/sparge con objetivos distintos y restricciones (tanicidad, extracción, etc.).
- Calibración por planta (efectos reales de ácido/sales según tus mediciones).

---

## Ubicación y navegación

**Ubicación recomendada (para evitar warnings):**
- Carpeta: `docs/99_Indice_y_Mapas/DATASETS/`
- Este archivo: `docs/99_Indice_y_Mapas/DATASETS/00_INDEX.md`

**Si tu `mkdocs.yml` lo referencia en el nav**, la ruta debe coincidir exactamente (relativa a `docs/`).  
Ejemplo correcto si DATASETS vive dentro de `99_Indice_y_Mapas`:

```yaml
- "99 — Índice y Mapas":
  - "DATASETS": 99_Indice_y_Mapas/DATASETS/00_INDEX.md
```
## HOPS_COA (Certificados de Análisis de lúpulos)

**Objetivo (operativo):** capturar COA por lote para que la formulación use **valores reales** (AA%, aceites, HSI, humedad) y para trazabilidad de insumos.

**Capa 1 (segura)**
- `hops_coa_example.json` — ejemplo de input (1 lote).
- `hops_coa_defaults.json` — defaults + reglas de validación “sanity check”.

**Capa 2 (opcional / condicionada)**
- `hops_alpha_age_model.json` — modelo simple para estimar AA% efectivo por edad/almacenamiento (placeholders, calibrar).

**Cómo se usa en receta (mínimo)**
- Si la receta dice “Citra 12% AA” y tu COA dice 10.8% AA, el sistema recalcula gramos para sostener el target de IBU/bittering.
- En dry hop, los aceites totales + HSI ayudan a decidir: “lote fresco / lote viejo” y ajustar dosis/tiempos.

---

## MALT_COA (Capa 1 segura + Capa 2 opcional)

**Objetivo:** normalizar y registrar el **COA de maltas** (por lote) para que el asistente pueda:
- Ajustar **rendimiento esperado** (extracto/points) y detectar outliers por proveedor/lote.
- Ajustar **color** y tradeoffs técnicos (proteína, beta‑glucanos, friabilidad) en función del estilo.
- Mantener trazabilidad de insumos (lote → receta → batch).

### Archivos (crear en `docs/99_Indice_y_Mapas/DATASETS/`)

**Capa 1 — referencia operativa (recomendado)**
- `malt_coa_example.json` — ejemplo de input canónico (un lote).
- `malt_coa_defaults.json` — rangos/validaciones + valores “fallback” por tipo de malta.

**Capa 2 — opcional / condicionada**
- `malt_coa_model.json` — modelo mínimo para convertir COA a inputs operativos (aprox).  
  Nota: si preferís, esto puede vivir “apagado” hasta que calibremos con datos reales (rendimientos en planta).

### Uso recomendado (operativo)
1) Cada vez que entra una malta nueva, copiás `malt_coa_example.json`, lo completás con tu COA real y guardás un archivo por lote (ej. `malt_coa_lote_CRISP-PA-2025-11-18.json`).  
2) El asistente usa `malt_coa_defaults.json` para validar y advertir (no para “adivinar”).  
3) Si habilitamos Capa 2, `malt_coa_model.json` permite estimar potencial PPG y SRM desde extracto/color.

### YEAST_COA (Capa 1 segura)
- **Propósito:** normalizar el registro de lotes de levadura (seca/líquida/slurry) para trazabilidad y cálculos básicos de pitch.
- **Archivos**
  - `DATASETS/yeast_coa_example.json` — ejemplo de input (lote + specs disponibles)
  - `DATASETS/yeast_coa_defaults.json` — defaults/validaciones mínimas (qué es requerido vs opcional)

### YEAST_COA_MODEL (Capa 2 opcional/condicionada)
- **Propósito:** estimar viabilidad/pitch cuando hay datos mínimos (y supuestos explícitos).
- **Archivo**
  - `DATASETS/yeast_coa_model.json` — parámetros/modelos (viability decay + pitch planning)
