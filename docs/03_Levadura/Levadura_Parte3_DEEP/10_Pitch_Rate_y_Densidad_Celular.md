# Pitch rate y densidad celular

## Objetivo
Definir y calcular el **pitch rate** (células viables inoculadas) para lograr:
- Fermentación consistente (lag y cinética controlable)
- Perfil sensorial objetivo (limpio vs expresivo)
- Menor riesgo de defectos (VDK/diacetilo, alcoholes superiores, sub-atenuación)
- Menor variabilidad lote a lote

---

## Qué es el pitch rate
Cantidad de **células viables** inoculadas por unidad de volumen y extracto:
- **Pitch rate** = células viables / (mL · °P)

> Nota: en la práctica se habla en **millones de células por mL por °P**.

---

## Impactos (trade-offs)
- **Bajo pitch**: más crecimiento → más ésteres y alcoholes superiores; mayor estrés; mayor riesgo de desviaciones y lag extendido.
- **Alto pitch**: fermentación rápida; perfil más limpio; puede reducir complejidad y afectar floculación/atenuación según cepa/proceso.

(Esto ya estaba capturado en el archivo; acá lo integramos al flujo operativo.) 

---

## Inputs mínimos (para decidir bien)
1) Estilo / perfil deseado (limpio vs expresivo)
2) OG o °P del mosto
3) Volumen a fermentar (L)
4) Tipo de levadura:
   - seca (g + fecha)
   - líquida (packs/vials + fecha)
   - slurry (cosecha + densidad + viabilidad)
5) Temperatura objetivo y disponibilidad de O2 (ver 20_Oxigenacion_del_Mosto.md)
6) Restricciones operativas: tiempo, tanque, riesgo, repetibilidad

---

## Targets típicos (heurística operativa)
Usar como punto de partida y ajustar por cepa/cervecería:

| Caso | Pitch rate típico (M cel/mL/°P) | Objetivo sensorial |
|---|---:|---|
| Ale “estándar” (perfil balanceado) | 0.75 – 1.0 | balance |
| Ale muy limpia / alta repetibilidad | 1.0 – 1.25 | limpio |
| Lager / fermentación fría | 1.5 – 2.0 | limpio, baja producción de ésteres |
| Alta densidad (high gravity) | +25% a +50% sobre el target base | controlar estrés y sub-atenuación |

**Regla de decisión**: definir el target según:
- estilo
- OG (o °P)
- perfil deseado

---

## Cálculo canónico (paso a paso)
### 1) Convertir OG a °P (aprox)
Si solo tenés OG:
- **°P ≈ 259 - 259/OG** (aprox útil)

### 2) Células requeridas
**Células requeridas (millones) = PitchRate(M/mL/°P) × Volumen(mL) × °P**

Ejemplo (plantilla):
- Volumen = ____ L  → ____ mL
- OG = ____  → °P ≈ ____
- Pitch rate objetivo = ____ M/mL/°P
- **Células requeridas** = ____ millones = ____ billones (10^12)

### 3) Ajustar por viabilidad
**Células viables disponibles = Células totales × Viabilidad**

Si no medís viabilidad, asumir “TBD” y ser conservador (sobre todo en slurry y packs viejos).

---

## Cómo traducir “células requeridas” a levadura real
### A) Levadura seca
- Ventaja: más estable y repetible.
- Acción: convertir “células requeridas” a **gramos** usando tu referencia interna por marca/lote (dejar tabla propia por proveedor).

**Checklist seco (mínimo):**
- rehidratación (si aplica)
- temperatura de inoculación
- oxigenación acorde

### B) Levadura líquida (packs/vials)
- Requiere estimar células iniciales y degradación por tiempo/almacenamiento.
- Acción: si no alcanza, **starter** (o step-up) con objetivo de células viables al pitch.

### C) Slurry (cosecha y repitch)
- Requiere **densidad** (células/mL) y **viabilidad**.
- Acción: medir (hemocitómetro) o usar una tabla interna por “consistencia de slurry” + corrección por edad.

**Mínimo recomendable para slurry:**
- registrar fecha de cosecha, temperatura, número de generación, apariencia
- evitar slurry viejo sin medición

---

## Control en proceso (qué mirar para validar el pitch)
**Señales tempranas (0–24 h):**
- lag time (inicio de actividad)
- caída de densidad inicial
- temperatura y espuma (según cepa)

**Señales de control (24–96 h):**
- curva de atenuación consistente
- pH y temperatura dentro de target
- aromas “normales” vs solvente/azufre excesivo

**Post-fermentación:**
- diacetilo/VDK y necesidad de descanso
- floculación/clarificación
- atenuación final vs spec

---

## Errores comunes
- Definir pitch rate sin considerar °P (solo por litros)
- No ajustar por viabilidad/edad (packs o slurry)
- Subestimar el rol de oxígeno y nutrición (el pitch “solo” no salva el proceso)
- Overpitch para “apagar incendios” y luego culpar a la cepa por falta de perfil

---

## Checklist operativo (mínimo viable)
- [ ] Registrar: Volumen (L), OG/°P, temperatura, estilo/objetivo sensorial
- [ ] Elegir target de pitch rate (tabla “Targets típicos”)
- [ ] Calcular células requeridas (fórmula canónica)
- [ ] Estimar viabilidad (medida o supuesto conservador)
- [ ] Definir fuente: seca / líquida / slurry (y plan si no alcanza: starter)
- [ ] Ejecutar pitch + registrar hora
- [ ] Control temprano: lag + densidad + temperatura (primeras 24 h)
- [ ] Si hay desviación: activar troubleshooting (ver Fermentación_DEEP/07_Troubleshooting...)

---

## Links internos (puentes)
- Parte 3 (índice): [Levadura Parte3 DEEP](00_Indice_Levadura_Parte3.md)
- Siguiente: [Oxigenación del mosto](20_Oxigenacion_del_Mosto.md)
- Control térmico: [Control de temperatura](30_Control_de_Temperatura.md)
- Nutrientes: [Nutrientes y minerales](40_Nutrientes_y_Minerales.md)
- Estrés/defectos: [Estrés celular y defectos](50_Estres_Celular_y_Defectos.md)
- Pipeline completo: [Fermentación DEEP](../Fermentacion_DEEP/00_INDEX.md)
