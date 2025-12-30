# Control de temperatura

La temperatura gobierna la cinética metabólica y el balance entre:
- velocidad/atenuación
- perfil aromático (ésteres/fenoles)
- estrés (alcoholes superiores, paradas, sub-atenuación)
- limpieza final (VDK/diacetilo, acetaldehído)

---

## Objetivo
Mantener una **curva térmica planificada** (setpoints + rampas) para lograr:
- Perfil sensorial objetivo (limpio vs expresivo)
- Atenuación consistente
- Menor variabilidad lote a lote
- Reducción de “rescates” (subidas tardías, picos, fermentaciones erráticas)

---

## Inputs mínimos (para definir la curva)
- Estilo y perfil objetivo (limpio vs expresivo; ale vs lager)
- Cepa (rango recomendado por proveedor y comportamiento real en la cervecería)
- OG / °P (estándar vs alta densidad)
- Pitch rate y oxigenación (ver 10 y 20)
- Capacidad de control del tanque (camisa, cámara, free rise, etc.)
- Riesgos: picos por exo-termia, frío insuficiente, limitación de tiempo

---

## Efectos (trade-offs)
- Temperatura alta:
  - mayor cinética y atenuación (hasta cierto punto)
  - mayor producción de ésteres/fenoles (según cepa)
  - mayor estrés (más alcoholes superiores/solvente, paradas si el sistema no acompaña)
- Temperatura baja:
  - fermentación más lenta
  - riesgo de atenuación incompleta y sub-fermentación (según cepa/oxígeno/pitch)
  - puede mejorar limpieza pero aumenta tiempos y sensibilidad a fallas operativas

---

## Estrategia general (modo operativo)
1) **Arranque estable**: evitar “picos no planificados” en las primeras 24–48 h.
2) **Curva planificada**: mantener setpoint (o free rise controlado) hasta ~70–80% de atenuación.
3) **Rampa de terminación**: subir gradualmente para completar atenuación y limpiar VDK (si aplica).
4) **Estabilización**: mantener 24–48 h (según comportamiento real) antes de crash/transfer.
5) **No improvisar**: cualquier corrección térmica debe ser registrada como acción correctiva.

---

## Plantillas de curva (heurísticas; ajustar a tu realidad)
> Nota: usar como “default”, luego fijar curva canónica por cepa (bibliografía + experiencia propia).

### A) Ale “estándar” (perfil balanceado)
- Inicio: setpoint moderado (evitar pico exo-térmico)
- Medio: mantener estable
- Final: rampa suave + mantenimiento para limpieza

### B) Ale muy limpia
- Setpoint estable sin picos
- Rampa final moderada para asegurar terminación sin generar solvente

### C) Lager / frío
- Fermentación a baja temperatura (control estricto)
- Rampa final/descanso (diacetilo) según necesidad
- Maduración/cold conditioning posterior

### D) Alta densidad (high gravity)
- Evitar subir temperatura demasiado temprano (reduce estrés)
- Rampa final planificada + foco en O2/nutrientes/pitch

---

## Control y medición (qué registrar sí o sí)
**En cada lote:**
- Setpoint (°C) por día o por fase
- Temperatura real del tanque (no solo ambiente)
- Diferencial setpoint vs real (capacidad de control)
- Densidad/gravedad diaria (o puntos críticos)
- Observaciones: espuma, blow-off, aromas de estrés
- Acciones: “subí 1.0°C”, “bajé 0.5°C”, “mantuve 48 h”, etc.

---

## Señales tempranas de descontrol térmico (alertas)
- Pico no planificado en primeras 24–48 h
- Fermentación “se dispara” y luego se frena (indicador de estrés)
- Lag extendido + tanque frío (posible baja actividad / mala curva)
- Aromas: solvente/alcoholes superiores (temperatura alta + estrés)
- Sub-atenuación persistente (temperatura baja + limitaciones de O2/pitch/nutrientes)

---

## Acciones correctivas (sin improvisación)
- Si hay **pico temprano**: ajustar control para evitar repetición (mejor aislamiento, setpoint inicial, capacidad de frío).
- Si hay **fermentación lenta**:
  - revisar pitch/O2/nutrientes antes de subir temperatura
  - si se decide subir, hacerlo con rampa suave y registro
- Si hay **parada/sub-atenuación**:
  - validar mediciones, agitación/recirculación si aplica, revisar salud de levadura
  - temperatura como palanca, pero nunca sola (ver 10/20/40/50)

---

## Checklist operativo (mínimo viable)
- [ ] Definir curva térmica (setpoints + rampas) antes del pitch
- [ ] Confirmar capacidad de control (frío/calor) para sostenerla
- [ ] Monitorear primeras 24–48 h (evitar picos)
- [ ] Registrar temp real y densidad (mínimo 1 vez/día)
- [ ] Ejecutar rampa final planificada (si aplica) y mantener 24–48 h
- [ ] Documentar cualquier corrección (causa → acción → resultado)
- [ ] Linkear a troubleshooting si hay síntomas persistentes

---

## Links internos (puentes)
- Anterior: [Oxigenación del mosto](20_Oxigenacion_del_Mosto.md)
- Nutrientes: [Nutrientes y minerales](40_Nutrientes_y_Minerales.md)
- Estrés/defectos: [Estrés celular y defectos](50_Estres_Celular_y_Defectos.md)
- Pipeline completo: [Fermentación DEEP](../Fermentacion_DEEP/00_INDEX.md)
