---
status: stable
operational_level: P0
last_reviewed: 2025-12-22
owner: Juan
source: internal
---

# Agua — Cálculos y límites operativos (v0.1)

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
