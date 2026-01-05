# LAUNCHER — Selector de proyectos

## METHOD LOCK

Para GitHub Pages de este repo: **publicar = `python -m mkdocs gh-deploy --force` (canónico)**.  
No mezclar con otros métodos.

> Nota importante: `python -m mkdocs build --strict` es **validación** (chequeo de warnings/links).  
> No publica. La publicación real la hace `gh-deploy`.

---

## Orden de arranque (importante)

1) Primero se lee: **START_HERE** (reglas del sistema).  
2) Luego, según **la URL** con la que venís:

- Si el usuario pega la **URL de un proyecto** (ej. `.../PROYECTO_BIBLIA/`): se toma **ese** archivo como `CURRENT_STATE` del proyecto.
- Si el usuario pega la **URL home** del sitio: se continúa con lo registrado en **SESSIONS_LOG** (último proyecto activo) y/o se usa este **LAUNCHER** para elegir proyecto.

Este **LAUNCHER** se usa SOLO si:
- el usuario pide explícitamente cambiar de proyecto / crear uno nuevo / trabajar temporal, o
- el estado no está claro y hay que “seleccionar” a mano.

Links directos (sin rutas raras):
- [START_HERE](START_HERE.md)
- [SESSIONS_LOG](SESSIONS_LOG.md)
- [CONTRATO_ESTRUCTURA](CONTRATO_ESTRUCTURA.md)
- [Mapa_General_Quelonio](Mapa_General_Quelonio.md)

- Antes de crear archivos nuevos: revisar [ESTRUCTURA_REPO](ESTRUCTURA_REPO.md)

---

## Proyectos (estado vivo)

Estos archivos son el **único lugar** donde se mantiene el `CURRENT_STATE` de cada proyecto, para que al cerrar y volver solo tengas que copiar/pegar **un archivo**.

- [Biblia (Quelonio Pages) — Estado vivo](PROYECTO_BIBLIA.md)
- Proyecto — RAG App: [PROYECTO_RAG_APP](PROYECTO_RAG_APP.md)
- [Latas (Quelonio Brew) — Estado vivo](PROYECTO_LATAS.md)

Regla operativa:
- **Al cerrar trabajo de un proyecto:** se actualiza *solo* su `PROYECTO_*.md`.
- **SESSIONS_LOG:** queda como histórico/bitácora (se edita solo si querés registrar hitos o cambiar reglas globales).

---

## Contrato de dependencia — Biblia como “Source of Truth” para otros proyectos

La **Biblia (Quelonio Pages)** es el sistema de referencia vigente para:

- **RAG App**
- Proyecto — RAG App: [PROYECTO_RAG_APP](PROYECTO_RAG_APP.md)

### B) Latas (Quelonio Brew)
- Consume definiciones canónicas de: **branding/comms, mínimos de etiqueta, claims permitidos, estructura de línea**.
- La creatividad (frases por lote) vive en “Latas”, pero los **criterios** viven en Pages.

### Regla de promoción (temporal → permanente)
Si en Web+API o Latas aparece una decisión que debería quedar como verdad vigente:
1) Se documenta en el proyecto de trabajo (Web+API o Latas).
2) Se promueve a Pages (98_Verdad_Negocio o módulo técnico) con:
   - Qué queda vigente
   - Dónde quedó escrito (ruta/link)
   - Fuente (medición, planilla, cálculo, etc.)
   - Impacto/riesgo

---

## Check de release (mínimo)

Cuando hay cambios que deban verse en la web:

1) Validación (opcional pero recomendada):
- `python -m mkdocs build --strict`

2) Publicación (canónica):
- `git status`
- `git add -A`
- `git commit -m "docs: update <lo que cambió>"`
- `git push`
- `python -m mkdocs gh-deploy --force`
