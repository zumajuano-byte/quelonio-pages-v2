# LAUNCHER_OPS — Boot Operativo para Terceros

Este launcher es para **terceros** que necesitan acceso rápido a rutas operativas específicas, sin entrar en la lógica de proyectos de Quelonio OS.

---

## Regla de datos jerárquica

**Excel/Sheets > Biblia > Supuestos**

- **Excel/Sheets**: datos duros del cervecero (producción, inventarios, costos reales). Fuente de verdad.
- **Biblia**: datasets teóricos/publicables. Referencia para diseño y troubleshooting.
- **Supuestos**: valores por defecto cuando no hay datos. Usar con cautela.

⚠️ **NOTA**: Agua nunca se asume. Siempre medir parámetros del agua o pedir análisis.

## Cómo decide el sistema qué datos usar

Excel/Sheets (dato duro) manda.  
Biblia (dataset teórico/publicable) como referencia.  
Supuestos (default) solo si faltan ambos.  

Nota explícita: agua no se asume; COA manda en materias primas cuando exista.

### Ejemplos concretos

**Ejemplo A (Incidencia estilo):**  
NEIPA sin costos en Excel → usar heurística (lúpulo Alto, etc.) y marcar como REFERENCIA.  
NEIPA con costos en Excel → calcular share y clasificar Bajo/Medio/Alto.

**Ejemplo B (Materias primas):**  
Lúpulo sin COA (AA% desconocido) → usar rango Biblia y marcar incertidumbre.  
Lúpulo con COA/proveedor → usar AA% real (Excel/COA) y recalcular IBU/plan.

---

## Rutas operativas

### 🍺 Recetas
- [08 Recetas y Formulación](08_Recetas_Formulacion/08_Recetas_Formulacion.md)
- [Cálculos rápidos](08_Recetas_Formulacion/Calculos_rapidos.md)
- [Datasets de materias primas](12_Datasets_Materias_Primas/12_Datasets_Materias_Primas.md)
- SOPs (operación Excel-first): ver [Índice SOP 1–7](12_Datasets_Materias_Primas/SOP/_INDEX.md)
- Contratos/IDs/counters: ver [_schema index](12_Datasets_Materias_Primas/_schema/_INDEX.md)

### 🏭 Producción
- [05 Sistemas IPA Moderna](05_Sistemas_IPA_Moderna/05_Sistemas_IPA_Moderna.md)
- [04 Lúpulo](04_Lupulo/04_Lupulo.md)
- [10 Limpieza y Sanitización](10_Limpieza_Sanitizacion/10_Limpieza_Sanitizacion.md)
- [09 Empaque y Estabilidad](09_Empaque_Estabilidad/09_Empaque_Estabilidad.md)

### 🔬 QA/QC
- [DO, TPO y Oxigenación](09_Empaque_Estabilidad/Oxidacion_y_DO.md)
- [Control CIP y Limpieza](10_Limpieza_Sanitizacion/DEEP/00_INDEX.md)

### 💰 Costos (Incidencia)
- [Eficiencia y Costos de Lúpulo](04_Lupulo/Lupulo_Parte5_DEEP/40_Eficiencia_y_Costos.md)

---

## Nota de uso

Este launcher **NO reemplaza** el boot determinístico de `START_HERE.md`. Use este archivo solo para acceso directo a rutas operativas específicas.