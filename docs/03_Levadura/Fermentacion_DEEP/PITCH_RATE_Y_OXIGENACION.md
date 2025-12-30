---
status: stable
operational_level: P0
last_reviewed: 2025-12-22
owner: Juan
source: internal
---

# Levadura — Pitch rate y oxigenación (v0.1)

Objetivo: habilitar decisiones numéricas:
- cuánto inocular (pitch rate)
- cuánto oxigenar y cómo
- cómo ajustar según OG, estilo y salud de levadura

---

## 1) Definitions (canónicas)
- Pitch rate: cantidad de células por mL por grado Plato (cells/mL/°P)
- Viabilidad: % de células vivas
- Vitalidad: capacidad de fermentar “rápido y limpio”
- Oxigenación: ppm de O2 disuelto al inicio (pre-fermentación)

---

## 2) Rangos DEFAULT (baseline)

### Pitch rate
- Ale: 0.75 M cells/mL/°P (baseline)
- Lager: 1.5 M cells/mL/°P (baseline)
Ajustes:
- OG alta, frío, lager: subir
- estilos que buscan ester/expresión: ajustar con criterio (documentar)

### Oxígeno (ppm O2 disuelto)
- Ale: 6–8 ppm (baseline)
- Lager: 8–10 ppm (baseline)
- OG alta: puede requerir más, con cuidado y evidencia

Nota: si no medís O2, el asistente debe operar con “método reproducible” (tiempo/flujo/piedra) y registrar.

---

## 3) Inputs mínimos para calcular pitch
- volumen de mosto (L)
- gravedad (Plato o SG)
- familia (ale/lager)
- viabilidad estimada (si existe) o default conservador

---

## 4) Output estándar (para SPEC)
- pitch target (cells totales)
- método (starter/slurry/paquetes) y supuestos
- oxigenación: método + tiempo/flujo + objetivo
- riesgos y mitigación (sub/overpitch, stress)

---

## 5) Checklists (operativos)

### Pre-pitch
- [ ] temperatura correcta de pitch
- [ ] mosto frío y oxigenado antes de inocular
- [ ] sanitización del circuito (piedra, líneas)
- [ ] registrar hora y condiciones

### Oxigenación reproducible (si no hay medición)
- [ ] método definido (aire u O2)
- [ ] tiempo fijo
- [ ] flujo definido
- [ ] registro por lote

---

## 6) Gate “fermentación saludable” (proxy)
- densidad cae en 12–24 h (según estilo)
- no hay aromas severos early (H2S extremo, solvente)
- curva térmica controlada

---

## 7) BIBLIO (canónico) — completar
- source_id: BIB-YEAST-001
- Obra: Yeast (White & Zainasheff)
- Edición/Año:
- Sección/pág:
- Nota: pitch rate, oxigenación, stress y fermentación limpia.
