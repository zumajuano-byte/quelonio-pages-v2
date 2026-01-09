# 10 �?" Targets y control mínimo (Fermentación + Maduración)

**Objetivo:** definir un set **mínimo pero suficiente** de mediciones y límites para operar fermentación/maduración con repetibilidad.
Esto no reemplaza specs completas; es el **tablero mínimo** para decidir.

Puentes:
- QA/QC (lógica de límites): [Especificaciones vs control limits](../../06_Procesos_QA_QC/Procesos_QAQC_Parte6_DEEP/02_Especificaciones_y_Control_Limits.md)
- Biología de levadura (pitch/oxígeno/repitch): [Levadura (03)](../../03_Levadura/03_Levadura.md)
---

## Registro del lote (usar siempre)
�z�️ [TP �?" Log Fermentación y Maduración](TP_Log_Fermentacion_y_Maduracion.md)

---

## 1) Qué medir sí o sí (MVP de control)

### A. Variables �?odriver�?� (si se te van, todo se te va)

- **Temperatura (°C)** del fermentador (y del líquido, si medís directo).
- **Densidad / gravedad** (SG/°P) y su **tendencia**.
- **Presión** (si fermentás presurizado).
- **Tiempo** (días desde pitch; horas desde cambios térmicos).

### B. Variables �?ocalidad / liberación�?� (deciden salida)

- **VDK/diacetilo (pass/fail)** o proxy operable.
- **pH** (tendencia y anomalías).
- **Sensorial rápido** (olfato/sabor: azufre, solvente, manzana/acetaldehído, manteca/VDK, astringencia).
- **Claridad / turbidez** (si aplica al estilo).
- **CO�,,** (si estás capturando o carbonatando en tanque).

### C. Variables �?oriesgo�?� (contaminación, oxidación, seguridad)

- **Integridad de sello / airlock / válvulas** y riesgo de ingreso de aire.
- **Purga/CO�,, disponible** para transferencias.
- **Higiene de conexiones** (mangueras, clamps, juntas).
- **Micro (si tenés capacidad):** al menos screening en desvíos o por plan.

---

## 2) Frecuencia mínima (regla simple por fase)

- **0�?"48 h post-pitch:** más riesgo �?' controlar más seguido (temperatura + tendencia de densidad).
- **Alta fermentación:** foco en mantener curva térmica y detectar desvíos temprano.
- **Cercanía a FG / diacetilo:** foco en **VDK** + estabilidad de densidad.
- **Cold crash / transferencias:** foco en **O�,,/entrada de aire**, purgas y estabilidad.

---

## 3) Tabla operable: targets, rangos y acciones

> Nota: los rangos exactos dependen de estilo/cepa. Acá definimos **control limits operativos** (disparadores de acción).
> Para lógica formal: ver �?oEspecificaciones vs control limits�?�.

| Variable | Target típico | Control limit (dispara acción) | Frecuencia mínima | Acción inmediata (ejemplos) |
|---|---:|---:|---|---|
| Temp. fermentación (°C) | según cepa/estilo | ±1.0 °C sostenido o deriva no planificada | 2�?"4 veces/día (manual) o continuo | corregir setpoint; verificar sonda; revisar aislamiento/cooling |
| Densidad / °P | curva esperada | estancamiento temprano (>24h sin caída) | 1 vez/día (mínimo) | revisar pitch/oxígeno/nutrientes; chequear temp; descartar leak de CO�,,/medición |
| Tasa de caída de densidad | tendencia | caída demasiado rápida/lenta vs histórico | 1 vez/día | ajustar temperatura; revisar salud de levadura; evaluar nutrientes |
| pH | tendencia esperada | pH anómalo o sin descenso inicial | 1�?"2 veces por lote (mínimo) | revisar contaminación; revisar oxígeno/pitch; chequear calibración |
| VDK / diacetilo | PASS al final | FAIL al momento de planificar salida | 1 vez cerca de FG y antes de crash | extender tiempo; subir temp (diacetyl rest); esperar �?olimpieza�?� |
| Presión (si aplica) | estrategia definida | sobrepresión / subpresión no planificada | 1�?"2 veces/día | ajustar spunding; revisar válvulas; evitar suck-back en crash |
| CO�,, disuelto (si aplica) | objetivo de proceso | fuera de rango antes de transferencia/empaque | al final de maduración | corregir carbonatación o estrategia de transferencia |
| Sensorial rápido | limpio | aparición de off-flavors marcados | cada medición clave | activar troubleshooting; retener lote; test adicional |
| Claridad/turbidez (si aplica) | según estilo | fuera de objetivo antes de empaque | antes de transferir | ajustar crash/tiempo; finings/filtrado si aplica |
| Integridad de purgas/CO�,, | OK | falta de CO�,, / purga insuficiente | antes de transferencias | detener transferencia; asegurar purga; revisar conexiones |

---

## 4) Triggers de decisión (si pasa X, hacé Y)

### 4.1 Densidad no arranca (lag largo)
- Confirmar **temperatura real** (no solo setpoint).
- Confirmar **pitch rate** y condición de levadura (viabilidad/vitalidad).
- Confirmar **oxígeno** (si aplica).
- Acciones típicas: subir 1�?"2 °C, agitar suave (si es seguro), nutriente (si aplica), repitch.

### 4.2 Fermentación se �?oclava�?� (stuck / very slow)
- Verificar curva térmica y disponibilidad de nutrientes.
- Chequear pH, posibles inhibidores, presión (si fermentación presurizada).
- Acciones: ajuste térmico, rousing controlado, evaluación de repitch, plan de rescate.

### 4.3 VDK/diacetilo falla cerca del final
- No crash ni transfieras.
- Subir temperatura (descanso) + tiempo.
- Re-test hasta PASS.

### 4.4 Se planifica cold crash
- Riesgo principal: **ingreso de aire (suck-back)**.
- Asegurar estrategia: spunding/CO�,, blanket, válvulas ok, líneas purgadas, presión controlada.

---

## 5) Checklist mínimo (para imprimir mentalmente)

**Diario / por turno**
- [ ] Temp. real vs setpoint (¿deriva?).
- [ ] Densidad (y tendencia vs ayer).
- [ ] Sensorial rápido (si corresponde).
- [ ] Observaciones del fermentador (presión, blowoff, actividad).

**Antes de decidir �?osalida / crash / transferir�?�**
- [ ] Densidad estable (criterio definido).
- [ ] VDK/diacetilo PASS.
- [ ] Plan de purgas y CO�,, confirmado.
- [ ] Conexiones, mangueras, juntas: limpias / sanitizadas / listas.
- [ ] Riesgo O�,, controlado (estrategia definida).

---

## 6) Fuentes (pendiente)

- FUENTE_BIBLIO: completar con bibliografía base de fermentación + prácticas operativas.
- Notas internas Quelonio: historial de lotes y �?ocurvas esperadas�?� por cepa/estilo.


