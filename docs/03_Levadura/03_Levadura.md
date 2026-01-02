# Levadura (03) — HUB Operativo

Este módulo está orientado a **controlar fermentación y variabilidad**, y a convertir “elección de cepa” en una decisión **repetible** (setpoints + checklist + validación).

---

## Ruta sugerida (Operativa) — por prioridad de riesgo
Orden recomendado para ejecutar en producción (de mayor impacto a menor):

1) **Parte 3 — Control de fermentación (Hub operativo)**
   - Pitch / O2 / Temperatura / Nutrientes / Estrés
   - Logs + Checklist de control
2) **Parte 4 — Post-fermentación (cierre de riesgo)**
   - Limpieza (VDK/diacetilo) + floculación práctica
   - Cosecha/reutilización + estabilidad
3) **Parte 2 — Metabolismo y subproductos (para diagnosticar)**
   - Azúcares, alcohol, CO2, ésteres, alcoholes superiores, floculación
   - Interacción metabolismo ↔ receta
4) **Parte 5 — Selección de cepa (decisión completa)**
   - Marco + checklist + casos + “Limpias vs Expresivas”
5) **Parte 1 — Fundamentos (para alinear criterio)**
   - Motor del sabor, ciclo vital, necesidades, errores estructurales

---

## Accesos directos (lo que realmente vas a usar)

### Control (Parte 3)
- [Parte 3 — Índice](Levadura_Parte3_DEEP/00_Indice_Levadura_Parte3.md)
- [Pitch rate y densidad celular](Levadura_Parte3_DEEP/10_Pitch_Rate_y_Densidad_Celular.md)
- [Oxigenación del mosto](Levadura_Parte3_DEEP/20_Oxigenacion_del_Mosto.md)
- [Control de temperatura](Levadura_Parte3_DEEP/30_Control_de_Temperatura.md)
- [Nutrientes y minerales](Levadura_Parte3_DEEP/40_Nutrientes_y_Minerales.md)
- [Estrés celular y defectos](Levadura_Parte3_DEEP/50_Estres_Celular_y_Defectos.md)
- [Checklist control de fermentación](Levadura_Parte3_DEEP/60_Checklist_Control_Fermentacion.md)
- [TP Log — Pitch/O2/Temp/Nutrientes](Levadura_Parte3_DEEP/TP_Log_Pitch_O2_Temp_Nutrientes.md)

### Cierre (Parte 4)
- [Parte 4 — Índice](Levadura_Parte4_DEEP/00_Indice_Levadura_Parte4.md)
- [Diacetilo rest y limpieza](Levadura_Parte4_DEEP/10_Diacetilo_Rest_y_Limpieza.md)
- [Floculación práctica](Levadura_Parte4_DEEP/20_Floculacion_Practica.md)
- [Cosecha y reutilización](Levadura_Parte4_DEEP/30_Cosecha_y_Reutilizacion.md)
- [Viabilidad, vitalidad y mutación](Levadura_Parte4_DEEP/40_Viabilidad_Vitalidad_y_Mutacion.md)
- [Estabilidad y envejecimiento](Levadura_Parte4_DEEP/50_Estabilidad_y_Envejecimiento.md)
- [Checklist post-fermentación](Levadura_Parte4_DEEP/60_Checklist_Post_Fermentacion.md)

### Diagnóstico (Parte 2)
- [Parte 2 — Índice](Levadura_Parte2_DEEP/00_Indice_Levadura_Parte2.md)
- [Metabolismo de azúcares](Levadura_Parte2_DEEP/20_Metabolismo_de_Azucares.md)
- [Alcohol y CO2](Levadura_Parte2_DEEP/30_Produccion_de_Alcohol_y_CO2.md)
- [Ésteres y alcoholes superiores](Levadura_Parte2_DEEP/40_Esteres_y_Alcoholes_Superiores.md)
- [Floculación y sedimentación](Levadura_Parte2_DEEP/50_Floculacion_y_Sedimentacion.md)
- [Interacción metabolismo ↔ receta](Levadura_Parte2_DEEP/60_Interaccion_Metabolismo_y_Receta.md)

### Decisión de cepa (Parte 5)
- [Parte 5 — Índice](Levadura_Parte5_DEEP/00_Indice_Levadura_Parte5.md)
- [Marco de decisión selección de cepa](Levadura_Parte5_DEEP/10_Marco_Decision_Seleccion_Cepa.md)
- [Cepas limpias vs expresivas](Levadura_Parte5_DEEP/20_Cepas_Limpias_vs_Expresivas.md)
- Casos aplicados:
  - [Caso — Ale Americana](Levadura_Parte5_DEEP/30_Caso_Ale_Americana.md)
  - [Caso — Lager](Levadura_Parte5_DEEP/40_Caso_Lager.md)
  - [Caso — NEIPA](Levadura_Parte5_DEEP/50_Caso_NEIPA.md)
- [Checklist selección de cepa](Levadura_Parte5_DEEP/60_Checklist_Seleccion_Cepa.md)

### Fundamentos (Parte 1)
- [Parte 1 — Índice](Levadura_Parte1_DEEP/00_Indice_Levadura_Parte1.md)
- [Levadura como motor del sabor](Levadura_Parte1_DEEP/10_La_Levadura_como_Motor_del_Sabor.md)
- [Ciclo vital](Levadura_Parte1_DEEP/30_Ciclo_Vital_de_la_Levadura.md)
- [Necesidades básicas](Levadura_Parte1_DEEP/40_Necesidades_Basicas.md)
- [Errores estructurales comunes](Levadura_Parte1_DEEP/60_Errores_Estructurales_Comunes.md)

---

## Puentes recomendados (para evitar diagnósticos ciegos)

### Puente 1 — Malta → Fermentabilidad → Perfil final
- Si la fermentación “no cierra” como esperabas, revisá la base:
  - Malta: fermentabilidad/enzimas/temperatura-tiempo
  - Receta: azúcares fermentables vs no fermentables
- Ver: `02_Malta` (fermentabilidad y tradeoffs) + Parte 2 (metabolismo).

### Puente 2 — Agua/pH → Salud de levadura y performance
- pH de maceración / pH de mosto y minerales condicionan performance.
- Ver: `01_Agua` (control de pH y perfil) + Parte 3 (estrés/nutrientes).

### Puente 3 — Empaque/estabilidad → Oxígeno y vida útil
- Si envasás, el “cierre” define shelf life y defectos tardíos.
- Ver: `09_Empaque_Estabilidad` + Parte 4 (estabilidad/envejecimiento).

### Puente 4 — QA/QC → repetibilidad
- Si querés consistencia real: checklist + TP logs + COA/mediciones.
- Ver: `06_Procesos_QA_QC` + Parte 3/4 (logs y criterios).

---

## Cómo usar este módulo en un lote real (mínimo viable)
1) Elegí cepa con Parte 5 (marco + checklist) y dejá setpoints cerrados.
2) Ejecutá Parte 3 con log y checklist (especial foco 0–48 h).
3) Cerrá con Parte 4 (diacetilo/limpieza + decisiones finales + registro).
4) Si algo sale distinto: Parte 2 para diagnóstico.
5) Solo si querés alinear criterio o entrenar: Parte 1.

---
