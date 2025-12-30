# Centro de Incidentes (QA/QC) — “qué hago si algo sale mal”

## Objetivo (en simple)
Cuando aparece un problema, este archivo te dice:
1) qué hacer **ya** (para no empeorar),
2) qué revisar,
3) a qué documento ir según el síntoma,
4) y cómo dejarlo registrado (para que no se repita).

---

## 1) Primeros 3 pasos (siempre iguales)
1) **Frenar el daño**
   - No mezcles, no “tapes” con químicos, no sigas en automático.
2) **Aislar**
   - Identificá el lote y separá muestras (1 botella/lata “testigo”).
3) **Anotar 5 datos**
   - lote, fecha/hora, qué pasó, dónde, y desde cuándo.

---

## 2) Elegí tu caso (síntoma → a dónde ir)

### A) Sospecha de contaminación (acidez rara, fenoles raros, sobrecarbonatación inesperada)
- Ir directo a:
  - [Árbol de decisión: contaminación](Procesos_QAQC_Parte6_DEEP/10_Arbol_Decision_Contaminacion.md)
  - [Microbio: rutas de muestreo y tests](Procesos_QAQC_Parte6_DEEP/09_Microbio_Rutas_Muestreo_y_Tests.md)
- Y revisar higiene:
  - [10 — Limpieza y sanitización (Manual)](../10_Limpieza_Sanitizacion/DEEP/01_DEEP_Limpieza_Sanitizacion_v1.md)
  - [10 — Troubleshooting CIP (Kunze)](../10_Limpieza_Sanitizacion/DEEP/20_Troubleshooting_CIP_Kunze_Nivel2.md)

---

### B) Oxidación / “cartón”, aroma apagado rápido, shelf-life muy corto
- Ir a empaque/estabilidad:
  - [09 — Control de oxígeno (DO/TPO)](../09_Empaque_Estabilidad/DEEP/20_Control_oxigeno_DO_TPO.md)
  - [09 — Luz/temperatura/almacenamiento](../09_Empaque_Estabilidad/DEEP/30_Luz_temperatura_almacenamiento.md)
  - [09 — Troubleshooting empaque](../09_Empaque_Estabilidad/DEEP/40_Shelflife_y_troubleshooting_empaque.md)
- Y (si aplica) checklist QAQC de packaging:
  - [Parte5 — Checklist Packaging QAQC](Procesos_QAQC_Parte5_DEEP/60_Checklist_Packaging_QAQC.md)

---

### C) Diacetilo (manteca), fermentación “rara”, atenuación fuera de control
- Ir a cold-side:
  - [Parte4 — Fermentación control fino](Procesos_QAQC_Parte4_DEEP/10_Fermentacion_Control_Fino.md)
  - [Parte4 — Oxígeno en cold-side](Procesos_QAQC_Parte4_DEEP/20_Oxigeno_en_ColdSide.md)
- Y a tu SOP operativo:
  - [07 — Curva térmica y diacetilo](../07_Fermentacion_Maduracion/DEEP/20_Curva_termica_y_diacetilo.md)

---

### D) Problemas de carbonatación (sub o sobre) en botella
- Ir a:
  - [09 — Priming y carbonatación en botella](../09_Empaque_Estabilidad/DEEP/10_Priming_y_carbonatacion_en_botella.md)
- Si es “sobre” y además hay sabores raros: volver a (A) contaminación.

---

### E) El lote no “da el perfil” (no es defecto: es que no llega al objetivo)
- Ir a sensorial + mejora controlada:
  - [11 — TP Log de Cata](../11_Sensorial/DEEP/TP_Log_Cata_y_Defectos.md)
  - [11 — Pasar sensorial a Spec/Receta](../11_Sensorial/DEEP/20_Pasar_Sensorial_a_Spec_y_Receta.md)
  - [08 — Ticket de mejora (1 cambio por corrida)](../08_Recetas_Formulacion/DEEP/TP_Ticket_Mejora_Receta_Spec.md)

---

## 3) Cierre (para que no se repita)
Cuando ya entendiste el problema, registrar en:
- [CAPA y gestión de desvíos](Procesos_QAQC_Parte6_DEEP/11_CAPA_y_Gestion_de_Desvios.md)
