---
status: draft
scope: fermentacion
topic: repitch
sources:
  - "White & Zainasheff — Yeast (recolección, almacenamiento, viabilidad, conicos, generaciones)"
---

# Fermentación (DEEP) — Recolección, almacenamiento y repitch

## 1) Objetivo del repitch
Reutilizar levadura no es “ahorro”; es **control de proceso**:
- reducir variabilidad entre lotes,
- mejorar previsibilidad de cinética,
- mantener perfil sensorial consistente.

La condición para que funcione: **levadura sana, fresca y con riesgo micro controlado**.

---

## 2) Recolección: timing y criterio
### 2.1 Regla general
Recolectar lo antes posible, siempre que la cerveza ya haya cumplido:
- densidad estable / fin de fermentación,
- tiempo mínimo de maduración requerido por el estilo (p.ej., diacetilo).

### 2.2 Cilindro-cónicos (punto crítico)
En cónicos, la levadura se acumula y puede degradarse más rápido. Recomendación operativa:
- Ventana típica: **1–2 días después de iniciar el enfriamiento**.
- Evitar demoras: incluso 24h extra puede impactar fuerte la viabilidad.

### 2.3 Fermentadores “planos” (balde/garrafón)
La levadura forma una capa más amplia y disipa mejor el calor; la autólisis suele ser menos crítica en el corto plazo, pero si vas a reutilizar:
- conviene recolectar relativamente pronto (misma lógica: fresca > vieja).

---

## 3) Qué fracción de la levadura conviene recolectar (cónicos)
Objetivo: quedarte con la porción más “representativa” y sana.

Procedimiento típico:
1) Sanitizar válvula inferior y conexiones.
2) Abrir y **descartar la primera fracción**: suele venir con más trub y células menos deseables.
3) Recolectar la fracción “media” (más cremosa y homogénea).
4) Evitar la fracción final si vuelve a arrastrar sólidos/exceso de compactación.

Nota térmica (cónicos):
- El cono puede tener gradiente térmico; si podés, mantener el cono más frío que la cerveza ayuda a preservar viabilidad.

---

## 4) Almacenamiento: estándar mínimo (repitch “normal”)
### 4.1 Temperatura y tiempo
Política operativa recomendada:
- almacenar entre **1–2°C**,
- ideal: **repitch el mismo día** de recolección,
- objetivo: usar dentro de **7 días**,
- máximo: **14 días** (descartar más vieja).

### 4.2 Por qué el tiempo mata
Durante almacenamiento la levadura consume reservas internas (glucógeno), se debilita y aumenta el riesgo de células rotas (nutrientes para bacterias).  
Evitar:
- almacenamiento tibio,
- congelación (cristales de hielo rompen paredes celulares).

### 4.3 Control previo a uso (gate QA/QC)
Antes de repitch, validar:
- viabilidad,
- vitalidad,
- y señales de contaminación (aunque sea con test básico/olfato + criterios de descarte).

---

## 5) Viabilidad: criterio de descarte práctico
- Si la levadura cae a viabilidades bajas, el repitch se vuelve impredecible.
- Regla conservadora: **no usar si no estás cómodo con la viabilidad/vitalidad** (y documentar para aprender).

---

## 6) Generaciones: trazabilidad y política Quelonio
La generación afecta comportamiento (p.ej., floculación y performance).  
Implementación simple:
- asignar `gen = 0` al cultivo comprado,
- `gen = 1` al primer repitch, etc.
- registrar por lote: cepa, generación, fecha recolección, condiciones de almacenamiento, y resultado del lote.

Política sugerida:
- si aparece un desvío sensorial repetido (fenoles no deseados, super-atenuación, floculación anómala, etc.), **cortar cadena** y volver a cultivo fresco/propagación limpia.

---

## 7) Checklist operativo (repitch)
- [ ] Confirmar fermentación terminada + maduración mínima (según estilo)
- [ ] Plan de recolección (sanitización + recipiente + etiquetado)
- [ ] Recolectar en ventana adecuada (cónico: no demorar)
- [ ] Descartar primera fracción con trub; recolectar fracción media
- [ ] Enfriar y almacenar 1–2°C
- [ ] Etiquetar: cepa, gen, fecha/hora, lote origen, volumen
- [ ] Antes de usar: evaluar viabilidad/vitalidad y descartar si hay dudas
- [ ] Registrar desempeño del lote (cinética, FG, sensorial) para ajustar política

## Referencias
- White & Zainasheff — *Yeast*: almacenamiento (1–2°C, 7 días ideal, 14 máximo, evitar congelación); recolección en cónicos (timing, gradiente térmico y fracciones); impacto de generación; necesidad de control de viabilidad/contaminación.
