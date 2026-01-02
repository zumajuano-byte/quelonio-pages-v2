# COA y control de calidad (malta)

## 1) Para qué sirve el COA
El COA te permite anticipar performance en sala de cocción (brewhouse performance).

Traducción práctica:
- no es “papel”: es un input para evitar sorpresas (eficiencia, conversión, consistencia).

---

## 2) Qué mirar (lista práctica, por categorías)

**Core (casi siempre):**
- Humedad / Moisture
- Extracto / rendimiento previsto
- DP / actividad enzimática (especialmente en base)
- Proteína total vs soluble + FAN (si está disponible)
- Color (y nota de que color↔sabor no es lineal)

**Según problema (si el proveedor lo reporta):**
- Modificación de carbohidratos (impacta filtración y extracto)
- “Assortment” / homogeneidad de kernel
- Bushel weight
- Hartong (modificación y extracto)
- Contaminantes/riesgos: DON, nitrosaminas (cuando aplique)


---

## 3) Qué registrar
Usá el TP:
- [90_TP_Log_Malta_COA_y_Molienda](90_TP_Log_Malta_COA_y_Molienda.md)

---

## 4) Señales típicas
- lote nuevo + eficiencia cambia: revisar COA y molienda antes de tocar receta.

## Reglas (B004)

<a id="r-0068"></a>
### R-0068 — Tratar el COA como herramienta de predicción de performance del brewhouse

- FuenteID: B004
- Evidencia: "Purpose of the Certificate of Analysis (COA): documenting malt production and predicting brewhouse performance."
- Ubicación: B004 p55–p56

**Regla (operativa):**
- Guardar COA por lote/proveedor y usarlo como “input” para anticipar rendimiento y consistencia.
- Cuando cambie performance, primero comparar COA del lote actual vs lote anterior.

**Aplicación / límites:**
- Aplica siempre (escala chica o grande).
- No implica que el COA “garantiza” resultados; es predictivo, no determinista.

<a id="r-0069"></a>
### R-0069 — No leer el COA como lista de números aislados: buscar interrelaciones

- FuenteID: B004
- Evidencia: "COA reveals vital data but may be overwhelming and not all information is universally useful."
- Ubicación: B004 p56

**Regla (operativa):**
- Priorizar variables relevantes al objetivo (rendimiento, filtración, fermentabilidad, estabilidad) y entender cómo se relacionan.
- Evitar “sobre-especificar” si no sabés cómo impacta en tu sistema.

**Aplicación / límites:**
- Aplica cuando definís especificaciones internas o cuando interpretás COA por primera vez.
- No reemplaza experiencia: obliga a documentar qué variables te sirvieron para predecir resultados.
