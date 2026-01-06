# TABLAS — Targets por estilo (v0.2)

Objetivo: dar rangos operativos (targets) para que el asistente pueda:
- proponer SPEC baseline por estilo
- detectar desvíos (QA/QC)
- armar planes (proceso/empaque) con límites claros

Regla: estos targets son **DEFAULT**. Se ajustan por:
- equipo (eficiencia, pérdidas)
- objetivo sensorial (perfil)
- restricciones (insumos, costos)
- evidencia propia (histórico de lotes)

---

## 0) Cómo usa esto el asistente (motor de decisión)

### Inputs mínimos
Para proponer una SPEC baseline:
1) **Familia/estilo**
2) **Volumen final** (L)
3) Objetivo sensorial (ej.: “seco”, “más haze”, “amargor percibido bajo/alto”)
4) Restricciones (insumos/costos)

### Salidas mínimas (SPEC baseline)
- OG/FG objetivo (rango y valor nominal)
- ABV objetivo (derivado)
- IBU objetivo (rango)
- Color objetivo (SRM)
- pH final objetivo
- CO2 vols objetivo

### Reglas de resolución (cuando hay conflicto)
1) Prioridad #1: **seguridad / estabilidad / shelf life**
2) Prioridad #2: **consistencia sensorial**
3) Prioridad #3: **costo / eficiencia**
4) Si hay tradeoff explícito (ej. NEIPA expresiva vs estabilidad), el asistente debe:
   - marcar el tradeoff
   - proponer “modo estable” y “modo expresivo” como variantes (misma familia)

---

## 1) Tabla base (DEFAULT) — familias comunes

| Familia / Estilo | OG | FG | ABV % | IBU | Color (SRM) | pH cerveza final | CO2 vols |
|---|---:|---:|---:|---:|---:|---:|---:|
| Blonde / Golden Ale | 1.040–1.050 | 1.008–1.012 | 4.0–5.2 | 18–28 | 3–6 | 4.1–4.5 | 2.4–2.6 |
| Pale Ale (Am) | 1.048–1.058 | 1.010–1.014 | 4.8–6.0 | 30–45 | 5–10 | 4.1–4.6 | 2.3–2.6 |
| IPA West Coast | 1.060–1.072 | 1.008–1.014 | 6.0–7.5 | 45–70 | 5–10 | 4.1–4.6 | 2.2–2.5 |
| IPA Hazy / NEIPA | 1.060–1.075 | 1.010–1.018 | 6.0–7.8 | 20–45* | 3–7 | 4.2–4.7 | 2.3–2.6 |
| Session IPA | 1.040–1.050 | 1.008–1.012 | 4.0–5.0 | 30–50 | 4–7 | 4.2–4.7 | 2.3–2.6 |
| Lager Pale | 1.044–1.052 | 1.008–1.012 | 4.3–5.3 | 18–28 | 2–5 | 4.2–4.6 | 2.5–2.7 |
| Pils | 1.044–1.052 | 1.008–1.012 | 4.5–5.4 | 25–40 | 2–4 | 4.2–4.6 | 2.5–2.7 |
| Vienna / Amber Lager | 1.048–1.058 | 1.010–1.014 | 4.8–6.0 | 18–30 | 9–15 | 4.2–4.6 | 2.4–2.6 |
| Porter | 1.050–1.065 | 1.012–1.018 | 5.0–6.8 | 25–45 | 22–35 | 4.1–4.6 | 2.0–2.3 |
| Stout (dry) | 1.040–1.052 | 1.008–1.012 | 4.0–5.2 | 25–45 | 25–40 | 4.1–4.6 | 1.8–2.2 |
| Stout (imperial) | 1.080–1.110 | 1.018–1.030 | 8.0–11.5 | 45–80 | 30–45 | 4.1–4.7 | 1.8–2.2 |
| Saison | 1.050–1.065 | 1.002–1.008 | 5.5–7.5 | 20–35 | 4–7 | 4.0–4.5 | 2.6–3.2 |
| Sour kettle (frutada) | 1.040–1.060 | 1.006–1.012 | 4.0–6.5 | 5–15 | 2–6 | 3.1–3.6 | 2.6–3.0 |
| Wit / Wheat | 1.044–1.054 | 1.008–1.014 | 4.5–5.8 | 10–20 | 2–5 | 4.1–4.6 | 2.5–2.8 |

\* IBU en NEIPA es poco representativo por percepción/medición. Usar también g/L y perfil sensorial.

---

## 2) Targets de proceso (DEFAULT)

### pH (medición y ajuste)
- pH mash: 5.2–5.6 (medido a temperatura corregida o estándar)
- pH post-boil: 5.0–5.3
- pH final (cerveza): ver tabla por estilo

### Fermentación (curva baseline)
- Ale: 18–20 °C (base), rampa a 20–22 °C para cierre/VDK si aplica
- Lager: 9–12 °C (base), descanso VDK 18–20 °C, luego frío

---

## 3) Derivaciones rápidas (para que la tabla “decida”)

### ABV estimado (baseline)
- ABV% ≈ (OG - FG) * 131.25
  - Ej.: OG 1.060 y FG 1.012 → (0.048 * 131.25) ≈ 6.3%

Regla operativa:
- Si ABV derivado queda fuera del rango del estilo, el asistente debe:
  - proponer ajuste de OG (grist) o FG (perfil de fermentabilidad / levadura / mash)

---

## 4) Checks de desvío (QA/QC) usando estos targets

### Severidad
- **OK**: dentro del rango
- **WARNING**: fuera del rango por poco (desvío leve) → requiere nota en lote + explicación
- **FAIL**: fuera del rango de forma relevante → requiere incidente + decisión (blend, re-etiquetado, descarte)

### Reglas mínimas (aplican a cualquier estilo)
- OG: WARNING si ±0.002 fuera; FAIL si ±0.004 o más fuera
- FG: WARNING si ±0.002 fuera; FAIL si ±0.004 o más fuera
- pH final: WARNING si ±0.10 fuera; FAIL si ±0.20 o más fuera
- CO2: WARNING si ±0.2 vols fuera; FAIL si ±0.4 vols o más fuera

Nota: esto es “operativo v0.1”; luego se calibra con histórico propio (control limits reales).

---

## 5) Dónde se refleja en la Biblia (contrato interno)

Este archivo es canónico para:
- SPEC: `99_Indice_y_Mapas/TEMPLATE_SPEC_V1.md`
- Diseño/receta: `08_Recetas_Formulacion/Calculos_rapidos.md`
- QA/QC: módulo `06_Procesos_QA_QC` (límites + desvíos)

---

## 6) BIBLIO (canónico)

- source_id: BIB-TBL-001
- Qué aporta: rangos/targets por estilo (OG/FG/ABV/IBU/Color/CO2) y descriptores
- Fuente primaria: **BJCP 2021 (ES)** → ver: `../99_Indice_y_Mapas/FUENTES/B010_BJCP_2021.md`

- source_id: BIB-TBL-002
- Qué aporta: fórmulas y derivaciones (ABV, etc.) para convertir targets en decisiones numéricas
- Fuente primaria: **Matemática de la Cerveza** → ver: `../99_Indice_y_Mapas/FUENTES/B011_Matematica_de_la_cerveza.md`
