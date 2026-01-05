# Whirlpool y Hopstand

## Objetivo
Convertir el whirlpool/hopstand en una decisión reproducible:
- cuánto aporta a **amargor**
- cuánto preserva de **aroma/sabor**
- qué riesgos abre (vegetal/polifenoles/variabilidad)
- cómo registrarlo para repetirlo

## Definiciones (operativas)
- **Whirlpool**: etapa de recirculación/rotación del mosto caliente para separación de trub y, si se agrega lúpulo, extracción en hot-side.
- **Hopstand**: pausa/control de temperatura y tiempo durante/tras whirlpool para extraer compuestos (aroma/sabor) con intención.

> En la práctica, muchos equipos hacen “whirlpool + hopstand” como un único bloque con temperatura controlada.

## Variables críticas (las que realmente cambian el resultado)
1) **Temperatura de inicio y de fin** (y si cae o se mantiene)
2) **Tiempo total de contacto** (minutos)
3) **Agitación / recirculación** (intensidad y constancia)
4) **Carga de lúpulo y forma** (pellet, flor, concentrados)
5) **Volumen y geometría** (cada tanque cambia extracción)
6) **Carga de trub** (arrastre de sólidos puede cambiar retención/extracción)

## Qué produce esta etapa (output real)
- **Amargor adicional**: puede haber contribución aun sin hervor; no tratarlo como “solo aroma”.
- **Aroma/sabor**: objetivo típico, pero está condicionado por temperatura/tiempo y por pérdidas posteriores (enfriado/fermentación/oxígeno).
- **Riesgo de “verde/vegetal”** si el contacto es excesivo o si hay mucha extracción de polifenoles.
- **Variabilidad** si no se mide y registra temperatura + tiempo.

---

<a id="r-0406"></a>
## R-0406 — Whirlpool/hopstand: se diseña como adición con impacto en amargor (no solo aroma)

**Regla (operativa):**
- Toda receta que use whirlpool/hopstand debe declarar si el objetivo es:
  - (A) aroma/sabor con amargor controlado, o
  - (B) sumar amargor además de aroma.
- En el registro del batch: siempre guardar **temperatura** y **tiempo** de esta etapa.

**Evidencia (B006):**
- FuenteID: B006
- Ubicación: sección de hot-side / whirlpool (página exacta pendiente)
- Cita (<=25 palabras): [PEGAR CITA TEXTUAL DESDE PDF que indique contribución de amargor/isomerización o impacto en IBU]

---

<a id="r-0407"></a>
## R-0407 — Whirlpool/hopstand: definir criterio de duración; evitar tiempos largos “por inercia”

**Regla (operativa):**
- El hopstand debe tener **duración objetivo** (minutos) y criterio de fin.
- No extender tiempo por defecto si no hay un objetivo sensorial/operativo explícito (riesgo: variabilidad + extracción indeseada).

**Evidencia (B006):**
- FuenteID: B006
- Ubicación: sección de whirlpool / duración / extracción (página exacta pendiente)
- Cita (<=25 palabras): [PEGAR CITA TEXTUAL DESDE PDF sobre duración / rendimientos marginales / efectos]

---

## Playbooks (decisiones rápidas por objetivo)
### A) Perfil “limpio/definido” (West Coast / claridad)
- Mantener control estricto de tiempo y temperatura.
- Priorizar reproducibilidad y minimizar vegetal/astringencia.
- Separación prolija del lúpulo/trub al final.

### B) Perfil “jugoso/tropical” (Hazy / IPA moderna)
- Diseñar el hopstand como pieza del “sistema” (se conecta con Parte 4: timing/biotransformación/tioles).
- Control fuerte del oxígeno en todo lo que viene después (si entra O₂, se pierde el beneficio aromático).

---

## SOP mínimo (paso a paso registrable)
1) **Definir objetivo** (aroma/sabor vs aroma+amargor).
2) **Registrar temperatura de inicio** (°C) y método de control (mantener / dejar caer).
3) **Iniciar cronómetro** (minutos) al comienzo de contacto real con lúpulo.
4) **Mantener agitación/recirculación** según estándar del equipo (documentar si cambió).
5) **Fin por criterio** (tiempo objetivo alcanzado o señal definida).
6) **Separación/traslado**: documentar cómo se retira/filtra/decanta para repetirlo.

## Checklist de control
- [ ] Objetivo escrito (Aroma / Aroma+Amargor)
- [ ] Temp inicio (°C) y temp fin (°C)
- [ ] Tiempo total (min)
- [ ] Método de agitación/recirculación (qué equipo y cómo)
- [ ] Lúpulos y cantidades (g/L)
- [ ] Resultado sensorial (3–5 descriptores) + observaciones de “verde/astringencia”
- [ ] Notas de estabilidad (si hubo caída rápida de aroma)

## Links internos
- Parte 3: [Hervor y amargor](10_Hervor_y_Amargor.md)
- Parte 3: [Dry hopping](40_Dry_Hopping.md)
- Parte 4 (IPA moderna): `../Lupulo_Parte4_DEEP/00_INDEX.md`

## Fuentes
- FuenteID: B006
- Política: `99_Indice_y_Mapas/POLITICA_RAG_Y_FUENTES.md`
