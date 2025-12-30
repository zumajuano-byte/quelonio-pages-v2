# ASISTENTE — Knowledge Map (v0.1)

Este archivo define el mapa “para máquinas” del Asistente Virtual:
- Qué tipos de consultas existen (intents)
- Qué documentos canónicos debe usar
- Qué outputs debe producir
- Qué gates/validaciones aplica

Regla: si falta un doc canónico para un intent, se registra como GAP y se crea.

---

## 1) Clasificación de intents (canónica)

### INTENT.A — Receta (diseño/ajuste)
- objetivos: targets de estilo, ingredientes, proceso, costos
- entradas típicas: estilo, volumen, equipo, OG/FG/ABV/IBU/Color, disponibilidad insumos
- outputs: SPEC v1.0 + BOM + plan de proceso + checklist de QA/QC

### INTENT.B — Proceso (planificación/ejecución)
- objetivos: cronograma, pasos, dependencias, controles
- entradas: receta/lote, fecha objetivo, equipo, capacidad, restricciones
- outputs: Plan de producción + SOP + checklist de gates

### INTENT.C — QA/QC + Estabilidad + Liberación
- objetivos: gates, mediciones, criterios “retener/liberar”
- entradas: lote, mediciones (densidad/pH/temp/DO/TPO/CO2), sensorial
- outputs: Checklist + decisión + acciones correctivas + registro

### INTENT.D — Troubleshooting (síntomas)
- objetivos: diagnóstico reproducible y plan de corrección
- entradas: síntoma, momento del proceso, mediciones disponibles, historial
- outputs: Árbol de causas + pruebas + acciones + prevención

### INTENT.E — Uso del sistema (Brew OS)
- objetivos: guiar operaciones en UI y validaciones
- entradas: pantalla/modulo, error, qué quiere lograr
- outputs: pasos concretos + “qué dato falta” + verificación

### INTENT.F — Mixto (técnico + sistema)
- objetivos: traducir decisión técnica a registro en Brew OS (y viceversa)
- entradas: pregunta técnica y entidades del sistema
- outputs: recomendación técnica + instrucciones de registro + auditoría

---

## 2) Mapeo canónico: intent -> docs -> outputs -> gates

| Intent | Docs canónicos (primario -> secundario) | Outputs obligatorios | Gates (si aplica) |
|---|---|---|---|
| A Receta | 01 Agua, 02 Malta, 03 Levadura, 04 Lupulo, 05 IPA (si aplica), 98 Verdad Negocio (costos/specs) | SPEC v1.0 + BOM + Plan proceso (alto nivel) | Validar inputs mínimos (volumen, estilo, targets) |
| B Proceso | 07 Fermentación/Maduración (DEEP), 06 QA/QC (si define SOP), 09 Empaque | Plan producción + SOP + Checklist | Gate 07/20 diacetilo, Gate transferencia/cold crash, Gate 09 O2 |
| C QA/QC | 06 QA/QC, 07/20, 07/30, 09/20, 11 Sensorial | Checklist + decisión + acciones | “Listo para Empaque”, “Liberar/Retener” |
| D Troubleshooting | 11 Sensorial + docs DEEP relevantes (07/09/06) | Diagnóstico + pruebas + acciones | Declarar incertidumbre si faltan datos |
| E Uso sistema | PROYECTO_WEB_API (cuando exista) + módulos Brew OS | Pasos UI + validaciones + expected output | RBAC / permisos / auditoría |
| F Mixto | Biblia + Brew OS Data Contract | Recomendación + registro en sistema | No inventar datos; pedir campos faltantes |

---

## 3) Inputs mínimos por intent (para no inventar)

### A Receta
- estilo objetivo
- volumen final
- equipo (rendimiento/eficiencia si existe)
- targets: OG, FG, ABV, IBU, color (o permitir que el asistente los proponga como “baseline”)
- restricciones: insumos disponibles, costos, fecha

### B Proceso
- receta o spec
- fecha objetivo de envasado
- capacidad/equipo (fermentador, cold crash, envasado)
- restricciones (turnos, temperaturas, dry hop window)

### C QA/QC
- lote
- mediciones disponibles (densidad, temp, pH; DO/TPO/CO2 si existen)
- resultado sensorial (si aplica)
- incidente registrado (si ocurrió)

### D Troubleshooting
- síntoma
- en qué etapa ocurrió
- mediciones y logs (si existen)
- historial del lote (pitch, temp, transfers, empaque)

### E Uso sistema
- módulo/pantalla
- acción que quiere hacer
- error textual o captura (si hay)
- rol del usuario (Owner/Admin/Producción/etc.)

---

## 4) GAP LOG (para mantenerlo operativo)

## Docs P0 agregados (v0.1)
- TABLAS: [Targets por estilo](TABLAS_TARGETS_POR_ESTILO.md)
- Agua: [Calculos y limites](../01_Agua/DEEP/AGUA_CALCULOS_Y_LIMITES.md)
- Levadura: [Pitch rate y oxigenacion](../03_Levadura/Fermentacion_DEEP/PITCH_RATE_Y_OXIGENACION.md)
- Empaque: [DO/TPO objetivos y metodo](../09_Empaque_Estabilidad/DEEP/DO_TPO_OBJETIVOS_Y_METODO.md)
- Empaque: [CO2 tablas](../09_Empaque_Estabilidad/DEEP/CO2_CARBONATACION_TABLAS.md)
- Estabilidad: [Shelf-life plan](../09_Empaque_Estabilidad/DEEP/SHELF_LIFE_PLAN_Y_CRITERIOS.md)

...
### Registrar aquí gaps detectados por el asistente

- GAP-001: [pendiente] Playbook oxidación (síntomas -> causas -> pruebas -> acciones) con gates.
- GAP-002: [resuelto] Tabla targets por estilo (OG/FG/IBU/ABV/CO2) para recetas baseline.
- GAP-003: [pendiente] Documento “Matriz end-to-end de gates 07->09->11”.
...