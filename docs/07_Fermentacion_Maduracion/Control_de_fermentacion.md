---
status: active
scope: operacion
sources:
  - "PENDIENTE_BIBLIO — White & Zainasheff — Yeast"
---

# Control de fermentación (hub operativo)

## Objetivo (en simple)
Hacer fermentaciones repetibles con un método corto:
- medir lo mínimo,
- decidir con 3 “gates” claros,
- y evitar envasar antes de tiempo.

---

## Entrada rápida (lo que se usa en producción)
1) **Registrar el lote (siempre)**
- TP del lote: [TP — Log Fermentación y Maduración](DEEP/TP_Log_Fermentacion_y_Maduracion.md)

2) **Si necesitás criterios y límites**
- DEEP: [10 — Targets y control mínimo](DEEP/10_Targets_y_control_minimo.md)

3) **Si algo no cierra**
- DEEP: [40 — Troubleshooting](DEEP/40_Troubleshooting_proceso.md)

---

## Rutina por turno (2 minutos)
> La idea es que cualquiera pueda hacerlo igual.

1) **Temperatura real** (no solo setpoint)
2) **Densidad** (o plato): ¿sigue bajando?
3) **Olor rápido**: ¿aparece algo raro fuera de estilo?
4) **Anotar** en el TP del lote (si no está escrito, “no pasó”).

➡️ Registrar acá: [TP — Log Fermentación y Maduración](DEEP/TP_Log_Fermentacion_y_Maduracion.md)

---

## Checklist mínimo por lote (qué no puede faltar)
- [ ] Cepa / generación (si aplica)
- [ ] Volumen + OG/°P
- [ ] Oxigenación (método; DO si medís)
- [ ] Temperatura (setpoint + lectura real)
- [ ] Densidad (serie temporal)
- [ ] pH (opcional, recomendado)
- [ ] Nota sensorial rápida (ej.: manteca / solvente / fruta rara / sulfuro)

---

## Gates (decisión simple)
### Gate 1 — Arranque
**Qué espero ver:** actividad y/o caída de densidad dentro de un rango razonable.  
Si no arranca: ir a “Qué hacer si… (densidad se plancha)”.

### Gate 2 — Fermentación activa
**Qué espero ver:** densidad bajando de forma sostenida + temperatura estable.

### Gate 3 — Cierre / maduración
**Qué espero ver:** densidad estable + tiempo suficiente + sin defecto dominante.
- Si aplica: chequear diacetilo (manteca) antes de enfriar fuerte.

Guía:
- [20 — Curva térmica y diacetilo](DEEP/20_Curva_termica_y_diacetilo.md)

---

## Qué hacer si…
### 1) “La densidad se plancha”
Primero revisar (en este orden):
1) temperatura real,
2) salud/pitch,
3) oxígeno / nutrientes,
4) contaminación (si hay señales claras).

➡️ Diagnóstico guiado: [40 — Troubleshooting](DEEP/40_Troubleshooting_proceso.md)  
Si hay sospecha fuerte de contaminación: [QA/QC — Centro de Incidentes](../06_Procesos_QA_QC/Centro_Incidentes.md)

### 2) “Aparece manteca” (diacetilo)
- No enfriar de golpe.
- Dar tiempo + curva térmica correcta.

➡️ Usar: [20 — Curva térmica y diacetilo](DEEP/20_Curva_termica_y_diacetilo.md)

### 3) “Riesgo de O₂ en crash/transfer”
- Evitar succión / headspace con aire.
- Planear transferencia lo más cerrada posible.

➡️ Usar: [30 — Transferencias / cold crash / salida](DEEP/30_Transferencias_cold_crash_y_salida.md)

---

## Puentes (módulos relacionados)
- Biología de levadura: [03 — Levadura](../03_Levadura/03_Levadura.md)
- Curva térmica/VDK (DEEP): [20 — Curva térmica y diacetilo](DEEP/20_Curva_termica_y_diacetilo.md)
- Transferencias/crash/salida (DEEP): [30 — Transferencias y salida](DEEP/30_Transferencias_cold_crash_y_salida.md)
- Troubleshooting (DEEP): [40 — Troubleshooting](DEEP/40_Troubleshooting_proceso.md)
- Empaque (cuando ya está “listo para envasar”): [09 — Empaque y estabilidad](../09_Empaque_Estabilidad/09_Empaque_Estabilidad.md)
