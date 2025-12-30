# DEEP v1 — Recetas y Specs (definición vigente + tolerancias + versionado)

> Marco de verdad:
> - (BIBLIO) = respaldado por bibliografía (a completar cuando esté citado).
> - (HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO) = práctica operativa útil, aún no anclada a tu bibliografía.

## 0) Objetivo operativo
Que cada cerveza tenga una “definición vigente” que permita:
- Repetibilidad (mismo resultado con mismo proceso)
- Trazabilidad (qué cambió y cuándo)
- QC y liberación (criterios claros)
- Mejora continua (feedback al spec sin caos)

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

---

## 1) Entidades (mínimas) y relación
- **Receta**: fórmula + proceso objetivo (lo planificado).
- **Spec**: receta “congelada” con targets, tolerancias y gates (lo vigente).
- **Lote**: ejecución real de un spec (lo producido).
- **Registro QC**: mediciones y decisiones por etapa (lo medido/decidido).

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

---

## 2) SOP — Crear un Spec (campos obligatorios)
Un Spec “liberable” debe tener como mínimo:

### 2.1 Identidad y versionado
- Producto / Estilo
- Versión (vX.Y)
- Estado: Draft / Vigente / Deprecado
- Fecha de vigencia
- Responsable

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

### 2.2 Targets (los números que mandan)
- OG (objetivo)
- FG (objetivo)
- ABV (objetivo)
- IBU (objetivo, si aplica)
- Color/SRM (objetivo, si aplica)
- CO2 (objetivo)
- pH (si medís): mash / FV / final
- Temperaturas clave: fermentación (perfil) + envasado (rango)

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

### 2.3 Materias primas (con trazabilidad mínima)
- Maltas: tipo + % o kg + proveedor (lote si se puede)
- Lúpulos: variedad + forma + timing + g/L (lote si se puede)
- Levadura: cepa + forma (seca/líquida) + lote/fecha (si se puede)
- Agua: perfil objetivo + sales/ajustes (si aplica)

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

### 2.4 Proceso objetivo (resumen ejecutivo)
- Mash: esquema (T/tiempos) + pH objetivo (si aplica)
- Hervor: duración
- Whirlpool/hopstand: T/tiempo (si aplica)
- Enfriado: objetivo de T al inocular
- Fermentación: perfil de T por días + presión si aplica
- Dry hop: dosis + timing + T + tiempo de contacto (si aplica)
- Maduración/cold crash: objetivo + duración (si aplica)
- Empaque: método + rango de T + criterio anti-oxidación mínimo

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

### 2.5 QC y gates (mínimos)
Definir qué se mide y qué condición habilita pasar de etapa:
- Gate A (post-inoculación): OG registrada + T registrada
- Gate B (fin fermentación): FG estable (2 lecturas 24–48h) + sensorial rápido OK
- Gate C (pre-empaque): sensorial OK + plan de empaque definido + trazabilidad lista
- Gate D (liberación): criterios de liberación cumplidos

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

---

## 3) Tolerancias iniciales (placeholder)
> Estas tolerancias se completan con datos reales de tus lotes y/o bibliografía.
> Mientras tanto, quedan como HEURÍSTICA OPERATIVA y se validan por medición.

- OG: ± ___
- FG: ± ___
- ABV: ± ___
- CO2: ± ___
- pH final: ± ___ (si aplica)

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

---

## 4) Reglas de versionado (simple y anti-caos)
### 4.1 Cuándo es cambio menor (v1.0 → v1.1)
Ejemplos:
- Ajuste pequeño de timing (sin cambiar identidad sensorial esperada)
- Cambio de proveedor/lote manteniendo especificación equivalente
- Ajuste menor de dry hop (misma intención sensorial)

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

### 4.2 Cuándo es cambio mayor (v1.x → v2.0)
Ejemplos:
- Cambio de levadura (cepa distinta)
- Cambio de grist base (pilsen↔pale en proporciones relevantes)
- Cambio fuerte de carga/estrategia de lúpulo (aroma/bitterness)
- Cambio de proceso crítico (fermentación, presión, empaque)

(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

### 4.3 Regla de oro
Si el consumidor “percibiría otra cerveza”, es versión mayor.
(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

---

## 5) “Spec Sheet” (referencia a template)
Usar la plantilla canónica:
- `docs/00_Templates/TP_SpecSheet_Cerveza.md`
## Templates
- [TP — Ticket de mejora (Receta/Spec)](TP_Ticket_Mejora_Receta_Spec.md)


(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)

---

## 6) Matriz de afirmaciones (para anclaje bibliográfico posterior)
> Completar en pasada 2 con: libro → capítulo → sección/página.

| Afirmación / decisión operativa | Tag | Fuente | Métrica/validación | Estado |
|---|---|---|---|---|
| Tener spec vigente con targets y gates mejora repetibilidad y liberación | HEURÍSTICA | PENDIENTE_BIBLIO | % lotes dentro de tolerancia + retrabajos | por citar |
| FG estable (2 lecturas) como condición mínima de fin de fermentación | HEURÍSTICA | PENDIENTE_BIBLIO | evitar sobre/infra carbonatación + defectos | por citar |
| Versionado simple evita “receta ambigua” y facilita trazabilidad | HEURÍSTICA | PENDIENTE_BIBLIO | auditoría de cambios + consistencia | por citar |

---

## Feedback desde Sensorial (cierra el loop)
Las recetas y specs se ajustan con evidencia. El método oficial para transformar cata en cambios es:

➡️ [11/DEEP/20 — Pasar sensorial a Spec y Receta](../../11_Sensorial/DEEP/20_Pasar_Sensorial_a_Spec_y_Receta.md)

Registro de cata:
➡️ [11/DEEP/TP — Log de Cata y Defectos](../../11_Sensorial/DEEP/TP_Log_Cata_y_Defectos.md)
