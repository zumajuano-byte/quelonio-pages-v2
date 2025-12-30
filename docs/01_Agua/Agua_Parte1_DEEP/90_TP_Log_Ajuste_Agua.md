---
status: canonical
type: template
scope: agua
---

# TP — Log de Ajuste de Agua (Strike / Sparge / Perfil)

Este log estandariza el ajuste de agua por lote para que sea repetible y trazable.
Objetivo: registrar **fuente → mediciones → cálculo → adiciones → pH real → resultado**.

---

## 0) Identificación del lote
| Campo | Valor |
|---|---|
| Lote / ID |  |
| Estilo / Perfil objetivo |  |
| Fecha |  |
| Volumen total a preparar (L) |  |
| Strike (L) |  |
| Sparge (L) |  |
| Operador |  |

---

## 1) Fuente de agua y pretratamiento (Gate cloro/cloramina)
| Campo | Valor |
|---|---|
| Fuente | red / pozo / ósmosis / mezcla |
| ¿Se trató cloro/cloramina? | sí / no |
| Método | carbón (GAC) / metabisulfito / otro |
| Observaciones |  |

---

## 2) Reporte base (antes de ajustar)
> Completar con reporte del agua o medición propia. Unidades típicas: ppm (mg/L).

| Parámetro | Valor |
|---|---:|
| pH (si lo tenés) |  |
| Alcalinidad (como CaCO₃) |  |
| Ca (ppm) |  |
| Mg (ppm) |  |
| Na (ppm) |  |
| Cl (ppm) |  |
| SO₄ (ppm) |  |
| HCO₃ (ppm) (si lo tenés) |  |

---

## 3) Objetivo de perfil (targets)
| Parámetro | Target |
|---|---:|
| Ca (ppm) |  |
| Mg (ppm) |  |
| Na (ppm) |  |
| Cl (ppm) |  |
| SO₄ (ppm) |  |
| Alcalinidad (como CaCO₃) |  |
| Relación SO₄/Cl (si aplica) |  |

---

## 4) Cálculo operativo (RA) — si aplica
> RA en ppm como CaCO₃: **RA = Alcalinidad − [(Ca/1.4) + (Mg/1.7)]**

| Item | Valor |
|---|---:|
| Alcalinidad (CaCO₃) |  |
| Ca |  |
| Mg |  |
| RA estimada |  |
| Interpretación | RA + (sube pH) / RA − (baja pH) |

---

## 5) Adiciones (sales / ácidos) — separar Strike y Sparge
> Registrar **qué**, **cuánto**, **dónde**, y **por qué**.

### 5.1 Strike
| Adición | Dosis (g) | Dosis (g/L) | Motivo |
|---|---:|---:|---|
| CaSO₄ (yeso) |  |  |  |
| CaCl₂ |  |  |  |
| MgSO₄ |  |  |  |
| NaCl |  |  |  |
| Ácido (láctico/fosfórico) |  |  |  |
| Otros |  |  |  |

### 5.2 Sparge
| Adición | Dosis (g) | Dosis (g/L) | Motivo |
|---|---:|---:|---|
| CaSO₄ (yeso) |  |  |  |
| CaCl₂ |  |  |  |
| Ácido (láctico/fosfórico) |  |  |  |
| Otros |  |  |  |

---

## 6) Medición real (lo que manda)
> Medir pH a temperatura ambiente (consistencia histórica).

| Punto de control | Medición | Hora | Nota |
|---|---:|---|---|
| pH mash (20°C) — a los 10–15 min |  |  |  |
| pH mash (20°C) — a los 30–45 min |  |  |  |
| pH sparge / runnings (si medís) |  |  |  |
| Criterio de corte sparge | pH / densidad / volumen |  |  |

Guardrail recomendado:
- cortar sparge si pH de runnings sube demasiado (registrar umbral usado).

---

## 7) Resultado y feedback loop
| Campo | Valor |
|---|---|
| ¿Se llegó al pH objetivo? | sí / no |
| Impacto sensorial percibido |  |
| ¿Qué cambiarías la próxima vez? (1–2 líneas) |  |
| Link a TP sensorial (si aplica) |  |

---

## 8) Desvíos y acciones (CAPA rápida)
| Desvío | Causa probable | Acción | Resultado |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
