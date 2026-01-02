# Checklist — Control de fermentación

Checklist operativo para controlar fermentación con baja variabilidad lote a lote.
Principio: no se “rescata” con una sola palanca; se controla el sistema:
**Pitch ↔ O2 ↔ Temperatura ↔ Nutrientes**.

---

## A) Pre-pitch (antes de inocular)
### Datos mínimos registrados
- [ ] Lote / estilo / objetivo sensorial (limpio vs expresivo)
- [ ] Volumen (L) y OG o °P
- [ ] Cepa y fuente (seca / líquida / slurry) + fecha/estado

### Pitch rate
- [ ] Target definido (M cel/mL/°P) según estilo/OG/temperatura
- [ ] Células requeridas calculadas
- [ ] Viabilidad estimada/medida (si aplica)
- [ ] Plan de inoculación cerrado (cantidad real a inocular)
- Link: [Pitch rate y densidad celular](10_Pitch_Rate_y_Densidad_Celular.md)

### Oxígeno
- [ ] Método definido (equipo/tiempo/caudal) y estandarizado
- [ ] Oxigenación programada **inmediatamente antes del pitch**
- [ ] Registrado: hora O2 / hora pitch / temperatura
- Link: [Oxigenación del mosto](20_Oxigenacion_del_Mosto.md)

### Temperatura (curva térmica)
- [ ] Setpoint inicial definido (evitar picos 0–48 h)
- [ ] Curva planificada (setpoints + rampas)
- [ ] Capacidad real de control confirmada (tanque/cámara/camisa)
- Link: [Control de temperatura](30_Control_de_Temperatura.md)

### Nutrientes
- [ ] Evaluación “sí/no” (no automático)
- [ ] Si “sí”: qué / dosis / timing definidos y registrados
- Link: [Nutrientes y minerales](40_Nutrientes_y_Minerales.md)

---

## B) Ventana crítica 0–48 h (arranque)
- [ ] Confirmar que no hubo oxigenación tardía (prohibido post-inicio)
- [ ] Medir/registrar: temperatura real del tanque y densidad
- [ ] Lag time observado (inicio de actividad) y comparación vs histórico
- [ ] Control de picos exo-térmicos: registrar setpoint vs real

**Gatillos de alerta temprana**
- [ ] Lag extendido
- [ ] Pico térmico no planificado
- [ ] Densidad no cae según expectativa

Acción: revisar primero **Pitch/O2/Temp/Nutrientes** antes de “inventar” correcciones.

---

## C) Monitoreo diario (mitad de fermentación)
- [ ] Densidad diaria (o al menos puntos críticos)
- [ ] Temperatura real diaria
- [ ] Observaciones de espuma/blow-off (si aplica)
- [ ] Aromas de estrés (solvente/azufre) anotados (sí/no)
- [ ] Desviaciones registradas: causa probable → acción → resultado

Link: [Estrés celular y defectos](50_Estres_Celular_y_Defectos.md)

---

## D) Terminación y limpieza (cierre)
- [ ] Confirmar atenuación esperada vs real (densidad final en target)
- [ ] Rampa final/descanso ejecutado si aplica (registrar tiempo y setpoint)
- [ ] Señales de VDK/diacetilo: evaluar necesidad de sostener temperatura
- [ ] No hacer crash/transfer prematuro sin confirmar terminación

---

## E) Registro final (para bajar variabilidad lote a lote)
- [ ] Guardar “curva real”: densidad vs tiempo + temperatura real
- [ ] Notas: qué funcionó / qué falló / qué se ajusta en el próximo lote
- [ ] Links usados en decisiones (para trazabilidad interna)

> Registro recomendado: [TP — Log Pitch/O2/Temp/Nutrientes](TP_Log_Pitch_O2_Temp_Nutrientes.md)

---

## Links internos
- [Pitch rate y densidad celular](10_Pitch_Rate_y_Densidad_Celular.md)
- [Oxigenación del mosto](20_Oxigenacion_del_Mosto.md)
- [Control de temperatura](30_Control_de_Temperatura.md)
- [Nutrientes y minerales](40_Nutrientes_y_Minerales.md)
- [Estrés celular y defectos](50_Estres_Celular_y_Defectos.md)
- [Fermentación DEEP (pipeline)](../Fermentacion_DEEP/00_INDEX.md)

---

## Reglas operativas (Parte 3)

<a id="r-0109"></a>
### R-0109 — Prohibido oxigenar tarde (post-inicio)
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "Confirmar que no hubo oxigenación tardía (prohibido post-inicio)"
- Ubicación: Parte 3 → Checklist → Ventana crítica 0–48 h

Regla (operativa):
- Oxígeno solo en la ventana de arranque (pre-pitch/inicio). No “corregir” luego con O2.

<a id="r-0110"></a>
### R-0110 — Pitch rate siempre con target y plan cerrado
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "Target definido… Células requeridas calculadas… Plan de inoculación cerrado"
- Ubicación: Parte 3 → Checklist → Pre-pitch → Pitch rate

Regla (operativa):
- No inocular sin target + cálculo (o criterio explícito). Registrar cantidad real inoculada.

<a id="r-0111"></a>
### R-0111 — Control térmico real: setpoint ≠ realidad (registrar ambos)
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "Control de picos exo-térmicos… registrar setpoint vs real"
- Ubicación: Parte 3 → Checklist → Ventana crítica 0–48 h

Regla (operativa):
- Registrar temperatura real del tanque y setpoint. Prioridad: evitar picos 0–48 h.

<a id="r-0112"></a>
### R-0112 — Nutrientes no automáticos: decisión sí/no + dosis/timing
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "Evaluación “sí/no” (no automático)… dosis… timing definidos"
- Ubicación: Parte 3 → Checklist → Pre-pitch → Nutrientes

Regla (operativa):
- Nutriente es soporte, no parche. Siempre justificar y registrar.

<a id="r-0113"></a>
### R-0113 — Troubleshooting: primero revisar Pitch/O2/Temp/Nutrientes
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "revisar primero Pitch/O2/Temp/Nutrientes antes de “inventar” correcciones"
- Ubicación: Parte 3 → Checklist → Ventana crítica 0–48 h

Regla (operativa):
- Ante desvío, no “mover receta”: auditar las 4 palancas antes.

<a id="r-0114"></a>
### R-0114 — No crash/transfer prematuro sin confirmar terminación y limpieza
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "No hacer crash/transfer prematuro sin confirmar terminación"
- Ubicación: Parte 3 → Checklist → Terminación y limpieza

Regla (operativa):
- Confirmar DF en target + evaluación VDK/diacetilo (según tu práctica) antes de enfriar/transferir.

<a id="r-0115"></a>
### R-0115 — Guardar la curva real (densidad vs tiempo + temperatura) para reducir variabilidad
- FuenteID: Q-STD-LEVADURA (Checklist Parte 3)
- Evidencia: "Guardar “curva real”: densidad vs tiempo + temperatura real"
- Ubicación: Parte 3 → Checklist → Registro final

Regla (operativa):
- Sin curva real no hay aprendizaje reproducible. Guardar y comparar vs histórico.

