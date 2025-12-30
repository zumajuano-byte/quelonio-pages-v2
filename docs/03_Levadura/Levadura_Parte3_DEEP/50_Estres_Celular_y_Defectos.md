# Estrés celular y defectos

El “estrés” es el conjunto de condiciones que empujan a la levadura fuera de su zona de operación estable, generando:
- cinética errática (lag, paradas, sub-atenuación)
- defectos sensoriales
- mayor variabilidad lote a lote

---

## Objetivo
Detectar temprano estrés de levadura, entender causas probables y activar acciones correctivas **sin improvisación**, priorizando las palancas básicas:
**Pitch ↔ O2 ↔ Temperatura ↔ Nutrientes**.

---

## Causas típicas de estrés (drivers)
- Alcohol alto (ABV alto / high gravity)
- Osmolaridad elevada (OG alta)
- Temperatura (muy alta, muy baja o picos no planificados)
- Falta de nutrientes (mosto “pobre”, alta adjunción, etc.)

> Estas causas ya estaban en tu archivo; acá las convertimos en sistema operativo. 

---

## Defectos asociados (síntomas)
- Solvente / alcoholes superiores
- Azufre (intenso/persistente)
- Diacetilo elevado (VDK)

---

## Diagnóstico operativo (antes de “culpar a la levadura”)
1) Confirmar medición: densidad/temperatura reales (no supuestos).
2) Revisar el triángulo base:
   - Pitch rate (ver 10)
   - Oxigenación temprana (ver 20)
   - Control térmico (ver 30)
3) Revisar nutrición:
   - criterio “sí/no” (ver 40)
4) Recién después: pensar en cepa, contaminación, u otros factores.

---

## Mapa rápido: síntoma → causas probables → qué chequear
| Síntoma | Causas probables | Qué chequear (mínimo) | Acción correctiva (controlada) |
|---|---|---|---|
| Solvente / alcoholes superiores | Temp alta o pico temprano; bajo pitch; estrés por high gravity; O2/nutrientes insuficientes | curva térmica primeras 48 h; pitch planificado vs real; OG/°P; registro de O2/nutrientes | corregir curva para próximos lotes; evitar picos; ajustar pitch/O2/nutrientes en el diseño (no “rescate” tarde) |
| Azufre intenso/persistente | Estrés por limitación nutricional; fermentación fría/lenta; levadura estresada (slurry viejo); cinética irregular | lag y cinética; estado de levadura (edad); control térmico; criterio de nutrientes | estandarizar nutrición si corresponde; asegurar pitch y O2 correctos; ajustar curva (rampa final si aplica) |
| Diacetilo elevado | Fermentación incompleta; rampa final insuficiente; estrés por pitch/O2; frío temprano; alta carga de células no garantiza limpieza | atenuación real vs esperada; curva térmica final; tiempo en temperatura de terminación | planificar descanso/rampa (no improvisar); sostener tiempo suficiente; evitar crash temprano |
| Lag extendido / arranque lento | Bajo pitch; O2 insuficiente; temperatura baja; levadura débil | hora pitch vs hora oxigenación; temperatura real; fuente/viabilidad de levadura | corregir estándar pitch/O2/temperatura; evitar oxigenar tarde |
| Sub-atenuación / parada | Temp baja; falta de O2/nutrientes; high gravity; estrés acumulado; levadura fatigada | densidad vs curva; historial del lote; pitch/O2/nutrientes | corregir diseño del proceso; temperatura como palanca, pero junto con el resto (no solo “subir grados”) |

---

## Checklist operativo (mínimo viable)
- [ ] Registrar: OG/°P, volumen, cepa, fuente de levadura, pitch, oxigenación, curva térmica
- [ ] Monitoreo 0–48 h: lag + densidad + temperatura real (detectar picos)
- [ ] Si aparece síntoma: mapearlo con la tabla (evitar “acciones por reflejo”)
- [ ] Priorizar corrección en el diseño del proceso (pitch/O2/temp/nutrientes)
- [ ] Documentar: causa probable → acción → resultado (para bajar variabilidad)

---

## Links internos (puentes)
- Pitch rate: [Pitch rate y densidad celular](10_Pitch_Rate_y_Densidad_Celular.md)
- Oxigenación: [Oxigenación del mosto](20_Oxigenacion_del_Mosto.md)
- Temperatura: [Control de temperatura](30_Control_de_Temperatura.md)
- Nutrientes: [Nutrientes y minerales](40_Nutrientes_y_Minerales.md)
- Pipeline completo: [Fermentación DEEP](../Fermentacion_DEEP/00_INDEX.md)
- Troubleshooting: (ver el archivo de troubleshooting dentro de Fermentación_DEEP)
