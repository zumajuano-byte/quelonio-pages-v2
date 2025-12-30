---
status: stable
operational_level: P0
last_reviewed: 2025-12-22
owner: Juan
source: internal
---

# TABLAS — Targets por estilo (v0.1)

Objetivo: dar rangos operativos (targets) para que el asistente pueda:
- proponer specs baseline por estilo
- detectar desvíos (QA/QC)
- armar planes (proceso/empaque) con límites claros

Regla: estos targets son **DEFAULT**. Se ajustan por:
- equipo (eficiencia, pérdidas)
- objetivo sensorial (perfil)
- restricciones (insumos, costos)
- evidencia propia (histórico de lotes)

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
- Ale: 18–20 C (base), ramp a 20–22 C para cierre/VDK si aplica
- Lager: 9–12 C (base), descanso VDK 18–20 C, luego frío

---

## 3) “Inputs mínimos” para proponer targets
Para que el asistente proponga SPEC baseline:
- estilo/familia
- volumen final
- objetivo sensorial (seco/dulce, amargor percibido, haze, etc.)
- restricciones (insumos/costos)

---

## 4) BIBLIO (canónico) — completar
- source_id: BIB-TBL-001
- Obra: [COMPLETAR] (p.ej. BJCP / Brewers Publications / Palmer / Janish)
- Edición/Año:
- Sección/pág:
- Nota: targets de estilo y rangos recomendados.
