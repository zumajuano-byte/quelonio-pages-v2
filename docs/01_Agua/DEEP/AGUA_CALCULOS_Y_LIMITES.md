---
status: stable
operational_level: P0
last_reviewed: 2025-12-22
owner: Juan
source: source: internal (operativo; canon en REGLAS_INDEX + reglas R-xxxx)
---

# Agua — Cálculos y límites operativos (v0.1)

> **Autoridad / Canon**
> - Este documento es **P0 operativo**: describe *inputs, outputs y procedimiento*.
> - Los rangos y decisiones **NO son canon** salvo que estén definidos como **Reglas (R-xxxx)** con `FuenteID` + `Evidencia`.
> - El **canon** vive en: `99_Indice_y_Mapas/REGLAS_INDEX.md` + reglas dentro de cada tema.
> - Si un rango aparece acá como DEFAULT, se considera **provisional** hasta que exista su Regla (R-xxxx) citada.

Objetivo: que el asistente pueda:
- traducir un perfil de agua a acciones (sales/acidos)
- evitar errores (Na alto, alcalinidad incontrolada, etc.)
- fijar rangos por familia de estilos

---

## 1) Parámetros canónicos (qué importa)
- Ca (ppm)
- Mg (ppm)
- Na (ppm)
- Cl (ppm)
- SO4 (ppm)
- HCO3 / alcalinidad (ppm como CaCO3)
- pH mash (resultado, no input)
- RA (alcalinidad residual) como concepto operativo (no obsesión)

---

## 2) Rangos operativos (DEFAULT)

### Calcio (Ca)
- DEFAULT general: 50–100 ppm
- Límites prácticos: 30–150 ppm

### Magnesio (Mg)
- DEFAULT: 5–30 ppm
- Evitar excesos (astringencia): >40 ppm suele ser indeseable

### Sodio (Na)
- DEFAULT: 0–50 ppm
- Precaución: 70–100 ppm ya se siente; >100 ppm riesgo alto (salado/duro)

### Cloruros (Cl) y Sulfatos (SO4)
- Relación sensorial (simplificada):
  - Más Cl: redondez/cuerpo
  - Más SO4: sequedad/amargor
- DEFAULT (IPA moderna/hazy): Cl 100–200, SO4 50–150
- DEFAULT (west coast): SO4 150–300, Cl 50–100
- DEFAULT (lager/pils): ambos moderados 30–80

### Alcalinidad (como CaCO3) / HCO3
- Objetivo: compatible con grist y pH mash.
- Malta clara: alcalinidad baja (evitar pH alto)
- Maltas oscuras: toleran/pueden requerir más alcalinidad

---

## 3) Heurísticas de corrección (operativas)

### 3.1 Si pH mash está alto (>5.6)
Acciones típicas:
- reducir alcalinidad (cortar con RO/destilada)
- acidificar (ácido láctico/fosfórico) según disponibilidad
- ajustar sales (Ca ayuda a bajar pH de forma indirecta)

### 3.2 Si pH mash está bajo (<5.2)
Acciones típicas:
- subir alcalinidad (bicarbonato) o reducir acidificación
- revisar grist (maltas ácidas, proporción de oscuras)

---

## 4) Cálculos prácticos (plantilla)
Este bloque es para que el asistente produzca un “plan de agua”.

### Inputs mínimos
- volumen de agua (L) (mash + sparge si aplica)
- análisis de agua base (ppm)
- perfil objetivo (ppm) o “familia de estilo”
- pH mash medido (si ya hay)

### Output
- sales (g) por lote y por etapa (mash/sparge)
- acidificación (ml) y objetivo
- checklist medición (pH, temp, calibración)

---

## 5) Checklist de medición (para no mentirse)
- [ ] pH-metro calibrado (2 puntos) el mismo día
- [ ] muestra de pH con temp controlada (o corrección)
- [ ] registrar pH mash a 10–15 min
- [ ] registrar pH post-boil
- [ ] registrar pH final (cerveza) por estilo

---

## 6) BIBLIO (canónico) — completar
- source_id: BIB-H2O-001
- Obra: [COMPLETAR] (Palmer / Water / etc.)
- Edición/Año:
- Sección/pág:
- Nota: rangos recomendados, efectos sensoriales, metodologías de ajuste.

---

## 7) Canon relacionado (links a reglas)
> Esta sección existe para que el asistente “salte” al canon sin ambigüedad.

### Desinfectantes (cloro / cloramina) — canon ya implementado
- R-0029 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0029)
- R-0030 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0030)
- R-0031 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0031)
- R-0032 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0032)
- R-0033 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0033)
- R-0034 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0034)
- R-0035 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0035)
- R-0036 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0036)
- R-0037 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0037)
- R-0038 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0038)
- R-0039 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0039)
- R-0040 → [ver](../Agua_Parte4_DEEP/150_Desinfectantes_Cloro_Cloramina.md#r-0040)

### Rangos por estilo / targets de sales / pH — (pendiente de canonizar)
- (PENDIENTE) Perfiles IPA / Cl vs SO4 → canonizar en `Agua_Parte2_DEEP/70_Perfiles_Agua_para_IPA.md`
- (PENDIENTE) pH mash (alto/bajo) → canonizar en `Agua_Parte2_DEEP/50_pH_en_el_Mash.md` o `Agua_Parte1_DEEP/20_pH_vs_Alcalinidad.md`
