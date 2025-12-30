---
status: draft
operational_level: P1
last_reviewed: 2025-12-22
owner: Juan
source: internal
---

# Matriz de Afirmaciones (P0)

Objetivo: registrar las afirmaciones “operativas” que el Asistente usa con más frecuencia,
indicando **dónde viven** (Doc P0 y sección) y su tipo.

**Tipos**
- operativa: regla/criterio de proceso (aplicable aunque no cites bibliografía en esa respuesta)
- biblio: afirmación que requiere soporte explícito (referencia a fuente)
- mixed: tiene criterio operativo + soporte (ideal)

**Regla**
- Si una afirmación P0 cambia, se actualiza acá y en el Doc P0 correspondiente.
- El Asistente debe preferir estas afirmaciones antes que notas sueltas.

---

## Tabla (Afirmación → Fuente)

| ID | Afirmación (resumen) | Doc P0 | Sección / Anchor | Tipo | Confianza | Notas / Condiciones |
|---:|---|---|---|---|---|---|
| P0-01 | Cada estilo tiene un set de targets base (OG/FG/ABV/IBU/CO2/pH) y si faltan inputs se usa DEFAULT marcado como DEFAULT. | TABLAS_TARGETS_POR_ESTILO | (completar) | operativa | alta | Ajustar por equipo/mercado. |
| P0-02 | El Asistente no inventa números críticos; si falta un dato (volumen, OG, eficiencia, mediciones) lo solicita o marca DEFAULT. | ASISTENTE_DATA_CONTRACT | (completar) | operativa | alta | Regla de sistema. |
| P0-03 | Agua: existen límites y rangos operativos para formular perfil/ajustes; cambios deben respetar límites definidos. | AGUA_CALCULOS_Y_LIMITES | (completar) | mixed | media | Depende del agua base. |
| P0-04 | Pitch rate y oxigenación deben definirse para asegurar fermentación saludable; no confundir O2 de mosto con O2 post-fermentación. | PITCH_RATE_Y_OXIGENACION | (completar) | mixed | media | Ajustar por cepa/estilo. |
| P0-05 | DO y TPO son focos críticos en cervezas lupuladas; sin medición, se opera con proxies y checklist estricto, registrando condiciones. | DO_TPO_OBJETIVOS_Y_METODO | (completar) | operativa | alta | Medición mejora control. |
| P0-06 | Carbonatación (vol CO2) se define por estilo/servicio y se calcula con tablas (temperatura/presión/vol). | CO2_CARBONATACION_TABLAS | (completar) | operativa | alta | Cuidar temperatura real. |
| P0-07 | Shelf-life se gestiona con plan de checkpoints (D+7/D+14/D+30 u otro) y criterios de liberar/retener/investigar. | SHELF_LIFE_PLAN_Y_CRITERIOS | (completar) | operativa | alta | Ajustar por estilo/logística. |
| P0-08 | Para liberar a empaque, deben cumplirse gates de fermentación (densidad estable / VDK OK según método). | (referencia interna) | (completar) | operativa | media | Requiere doc P0 de VDK si se vuelve crítico. |
| P0-09 | En transferencias/cold crash hay riesgo de ingreso de O2 por vacío; se deben aplicar medidas preventivas y checklist. | DO_TPO_OBJETIVOS_Y_METODO | (completar) | operativa | media | Depende de equipo. |
| P0-10 | El output del asistente debe seguir contratos (SPEC/Checklist/Plan/Trouble) y cerrar con Inputs usados + Datos faltantes. | ASISTENTE_CONTRATOS | (completar) | operativa | alta | Estándar de respuesta. |

---

## Pendientes para completar (1 pasada)
1) Reemplazar “(completar)” por sección real o título interno de cada doc.
2) Si P0-08 se vuelve frecuente, crear Doc P0 específico para VDK/diacetilo (o elevar el existente).
3) Ajustar “Confianza” cuando haya bibliografía explícita (pasada BIBLIO).
