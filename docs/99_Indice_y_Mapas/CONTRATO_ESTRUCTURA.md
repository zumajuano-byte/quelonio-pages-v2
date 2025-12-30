# Contrato de estructura — Quelonio Pages (Biblia Cervecera)

Este documento define reglas estructurales del repositorio `quelonio-pages/docs/`.
Objetivo: que la Biblia sea navegable, extensible y estable; y que funcione como fuente de verdad para proyectos dependientes (Web+API y Latas).

---

## 1) Qué es canónico y qué es “puente”
**Canónico**:
- Índices, mapas, definiciones vigentes, plantillas, SOPs mínimas y criterios de QA/QC.
- Todo lo que deba sobrevivir sesiones y proyectos.

**Puente**:
- Notas auxiliares, borradores, ideas, explicaciones largas o material “en construcción” que no es necesario exponer en el menú global.

Regla: si algo impacta decisiones, specs, procesos o claims, debe “promoverse” a canónico.

---

## 2) Entry points obligatorios (OS Boot)
Estos archivos son “puertas de entrada” y deben existir siempre:

- `99_Indice_y_Mapas/START_HERE.md` (reglas del sistema + orden de lectura)
- `99_Indice_y_Mapas/SESSIONS_LOG.md` (estado vivo: CURRENT_STATE + BUSINESS_TRUTH)
- `99_Indice_y_Mapas/LAUNCHER.md` (menú solo si CURRENT_STATE está incompleto o el usuario cambia de proyecto)
- `99_Indice_y_Mapas/CONTRATO_ESTRUCTURA.md` (este documento)

Regla: **SESSIONS_LOG manda** (estado actual). LAUNCHER es fallback.

---

## 3) Reglas de carpetas y nombres

### 3.1 Módulos
- Cada módulo vive en una carpeta `NN_Nombre/` (ej: `07_Fermentacion_Maduracion/`).
- Cada módulo tiene un archivo “home” (`NN_Nombre.md`) o un índice claro.

### 3.2 DEEP (profundización)
- Todo lo DEEP vive dentro de `.../DEEP/`.
- Dentro de `DEEP/` siempre existe:
  - `00_INDEX.md` (índice canónico del DEEP)
  - `01_DEEP_<tema>_v1.md` (documento principal v1)
- Versionado: `_v1`, `_v1_1`, `_v2` según corresponda.
- Regla: **lo navegable se entra por `00_INDEX.md`**. No se linkean “archivos sueltos” desde afuera sin pasar por índice.

### 3.3 Templates
- Templates viven en `00_Templates/`.
- Se referencian desde DEEP o desde QA/QC si son operativos.

---

## 4) Regla de navegación (MkDocs nav)
- El menú (nav) muestra:
  - Home/Mapa/Glosario/Entry points
  - Módulos principales (homes)
  - Índices canónicos
- No es obligatorio que TODO archivo esté en `nav`.
  - Si un archivo no está en `nav`, igual puede ser accesible por links desde un índice.
  - Regla: lo importante es que el usuario siempre pueda llegar por un “camino canónico” (índice).

---

## 5) Regla de links
- Links siempre **relativos** (no hardcodear URLs externas del sitio).
- Preferir links a índices (`00_INDEX.md`) en vez de a hojas internas sueltas.
- Si un link es crítico (ej. desde START_HERE a Regla de Oro), fijar anchor estable si hace falta.

---

## 6) Método de publicación (referencia)
Este documento NO define comandos; eso vive en LAUNCHER (METHOD LOCK).
Regla: este contrato nunca debe contradecir el METHOD LOCK.

---

## 7) Política de cambios
- Si funciona, no se toca.
- Si se cambia estructura/rutas:
  - se registra en SESSIONS_LOG (sesión + archivos tocados + resultado verificable),
  - se valida build estricto,
  - se publica con el método canónico.

---

## 8) Definición de “listo”
Un cambio está “listo” cuando:
- Se puede navegar desde un índice canónico.
- `python -m mkdocs build --strict` no muestra warnings.
- Se publicó con el método canónico y es visible en GitHub Pages.

* * *
## Regla 9 — Citas y trazabilidad (BIBLIO vs HEURÍSTICA)

### 9.1 Tags obligatorios (en texto)
- **(BIBLIO)** = afirmación respaldada con referencia completa (fuente → edición/año → capítulo/sección → página).
- **(HEURÍSTICA OPERATIVA | PENDIENTE_BIBLIO)** = práctica útil aún no anclada.

**Regla:** si falta la referencia completa, NO puede decir **(BIBLIO)**.

### 9.2 Formato canónico de cita (cuando pasa a BIBLIO)
En la frase:
- **(BIBLIO: `<COD_FUENTE>`)**

En “Referencias” del mismo archivo (o del bloque DEEP donde se use):
- **`<COD_FUENTE>` — Autor, Título, Edición/Año, Capítulo/Sección, p. XX–YY.**

Ejemplo:
- (BIBLIO: PALMER_HTB_4ED_CH07_P145)
- PALMER_HTB_4ED_CH07_P145 — John Palmer, *How to Brew*, 4th ed., Ch. 7, p. 145.

### 9.3 Matriz de afirmaciones (obligatoria en DEEP canónicos)
Tabla mínima:
- **Afirmación | Tag | Fuente | Métrica/validación | Estado**
