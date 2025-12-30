# ASISTENTE — Contratos de salida (v0.1)

Objetivo: estandarizar outputs. Si el asistente responde, debe hacerlo en uno de estos formatos.
Regla: outputs con estructura fija -> exportables -> automatizables.

---

## CONTRATO 1 — SPEC v1.0 (receta + proceso + QA/QC)

### SPEC_ID
- spec_id:
- estilo:
- volumen:
- fecha_objetivo:

### Targets
- OG:
- FG:
- ABV:
- IBU:
- Color:
- CO2 (vols) / presion/temperatura (si aplica):
- pH objetivo (si aplica):

### Ingredientes (BOM)
- Malta: (kg, %)
- Lupulo: (g, momento, AA%)
- Levadura: (cepa, cantidad, pitch rate si aplica)
- Agua: (perfil objetivo + sales)
- Adjuntos: (si aplica)

### Proceso (alto nivel)
- Mash:
- Hervor:
- Whirlpool:
- Enfriado y oxigenacion:
- Fermentacion (temp/curva):
- Dry hop (si aplica):
- Maduracion / cold crash:
- Empaque:

### Gates (obligatorio)
- Gate 1: “Listo para transferir/enfriar” (VDK/diacetilo)
- Gate 2: “Listo para empaque” (estabilidad + O2 control)
- Gate 3: “Liberar/Retener” (sensorial + estabilidad)

### QA/QC (mediciones mínimas)
- Densidad: (cuando)
- Temp: (serie)
- pH: (cuando)
- DO/TPO: (si disponible)
- CO2: (si disponible)

### Riesgos y mitigaciones
- Riesgo:
- Mitigacion:

### Registro (artefactos)
- TP log:
- Log empaque:
- Sensorial:

---

## CONTRATO 2 — PLAN DE PRODUCCION (cronograma)

- plan_id:
- lote / recipe_id:
- fecha_inicio:
- fecha_fin_estimada:
- capacidad/equipo:

### Hitos
1) Dia X: [tarea] (duracion) -> salida verificable
2) Dia X: ...
3) Empaque: ...
4) Sensorial 7/14/30 dias: ...

### Dependencias
- (tarea A) depende de (tarea B)

### Contingencias
- Si (evento), entonces (accion)

---

## CONTRATO 3 — CHECKLIST / GATES

- checklist_id:
- lote:
- etapa:
- fecha:

### Gate: nombre
- criterio:
- metodo de verificacion:
- OK/NO:
- evidencia (dato/log):

### Acciones si NO
- accion 1:
- accion 2:

---

## CONTRATO 4 — TROUBLESHOOTING (árbol operativo)

- incident_id:
- sintoma:
- etapa:
- lote (si aplica):

### Hipotesis (ordenadas por probabilidad)
1) causa probable:
   - evidencia esperada:
   - prueba:
   - accion:
2) ...

### Prevencion (para el próximo lote)
- cambio SOP:
- cambio checklist:
- cambio spec:

---

## CONTRATO 5 — SOP “1 paso” (modo operativo)

### Objetivo
- (1 frase)

### Paso a paso (1 paso por ítem)
1) Paso:
   - accion exacta:
   - output esperado:
   - que registrar:
2) ...
