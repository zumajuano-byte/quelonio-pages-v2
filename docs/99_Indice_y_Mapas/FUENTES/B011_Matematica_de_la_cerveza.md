# B011 — Matemática de la cerveza

**Tipo**: Manual de cálculos y relaciones (formulación, proceso y control).  
**Rol en la Biblia**: convertir diseño de receta en **cálculo trazable** (mismo input → mismo output).

> Idea clave: citar no alcanza.  
> Esta fuente se usa cuando dejamos “un set de fórmulas y procedimientos” que el asistente aplica siempre igual.

---

## 1) Cómo lo usa el asistente (pipeline de receta)

Cuando formulamos, el asistente sigue esta secuencia:

1. **Definir SPEC**: estilo (BJCP o custom) + targets (ABV/IBU/SRM/cuerpo/aroma).
2. **Volumen y eficiencia**: batch size, pérdidas, eficiencia (mash / brewhouse).
3. **Grist**: calcular masa total y distribución por rol (base, cuerpo, color, head).
4. **Amargor y aroma**: modelo de IBU + estrategia (hervor/whirlpool/dry hop).
5. **Fermentación**: pitch rate + temperatura + objetivo de atenuación.
6. **Carbonatación**: nivel de CO2 + método (priming / forzado).
7. **Validación**: BU:GU, balance, atenuación, riesgos.

---

## 2) Banco de fórmulas (mínimo operable)

### A) Densidad / atenuación / alcohol

- **Puntos de gravedad**:  
  `GU = (OG - 1) * 1000`  (ej: OG 1.060 → 60 GU)

- **Atenuación aparente (%)**:  
  `AA% = (OG - FG) / (OG - 1) * 100`

- **ABV (aprox)**:  
  `ABV% ≈ (OG - FG) * 131.25`

> Regla práctica: ABV es suficientemente buena para diseño; en QA podés usar método más preciso si hace falta.

### B) IBU (modelo Tinseth, recomendado)

- **Utilización (Tinseth)**:
  - `U = 1.65 * 0.000125^(OG - 1) * (1 - e^(-0.04 * t)) / 4.15`
  - `t` = minutos de hervor

- **IBU por adición**:
  - `IBU = (AA% * gramos_lúpulo * 1000 * U) / litros`

> Si el asistente no tiene tus AA% reales o tu volumen real post-boil, declara el supuesto.

### C) Color (SRM, aproximación de Morey)

- `MCU = (lb_malta * °L) / galones`
- `SRM ≈ 1.4922 * MCU^0.6859`

### D) Carbonatación (priming, enfoque operativo)

- Objetivo: `CO2_target (vol)` según estilo.
- Variables: temperatura de cerveza al envasar, tipo de azúcar, volumen.
- El asistente debe entregar: **gramos de azúcar** + procedimiento (disolución, sanitizado, mezcla).

> En la Biblia conviene tener una tabla rápida por temperatura (CO2 residual) y una fórmula única para gramos de azúcar.
> Si preferís, lo dejamos como “procedimiento + tabla” (menos error, más rápido).

### E) Eficiencia (para dimensionar grist)

- **Eficiencia de macerado** (según tu medición):
  - `MashEff% = (puntos_obtenidos_en_mosto_preboil) / (puntos_potenciales_del_grist) * 100`

- **Brewhouse efficiency**:
  - `BHEff% = (puntos_en_fermentador) / (puntos_potenciales_del_grist) * 100`

---

## 3) Checklist de cálculos (para evitar errores)

- ¿El volumen usado es **pre-boil**, **post-boil**, o **en fermentador**?
- ¿OG usado en Tinseth es el del hervor (aprox) o el del fermentador?
- ¿IBU objetivo es “teórico” o “percepción” (haze/whirlpool/dry hop cambian percepción)?
- ¿El cálculo de carbonatación considera CO2 residual por temperatura?
- ¿Se documentó eficiencia y pérdidas para que la receta sea replicable?

---

## 4) Cómo se refleja en la Biblia (concreto)

### A) En “Recetas / Formulación”
- Archivo: `docs/08_Recetas_Formulacion/Calculos_rapidos.md`  
  Debe tener:
  - Fórmulas mínimas (las de arriba)
  - “Inputs estándar” que el asistente pide siempre (volumen, eficiencia, AA%, temp).
  - Links a este B011.

### B) En “Specs”
- Archivo: `docs/99_Indice_y_Mapas/TEMPLATE_SPEC_V1.md`  
  Debe tener campos para:
  - OG/FG/ABV/IBU/SRM/CO2
  - tolerancias
  - supuestos de cálculo (modelo, eficiencia, AA%)

---

## 5) Referencia

- “Matemática de la cerveza” — PDF origen: `-Matematica-de-la-cerveza.pdf`
