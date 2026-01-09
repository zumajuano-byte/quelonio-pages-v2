# LAUNCHER — Selector de proyectos

## ACI-DEV — Método paso a paso (obligatorio)

Regla: en modo desarrollador se trabaja por acciones atómicas.
1) Se ejecuta 1 comando o 1 cambio.
2) Se verifica “OK” (build/test/validación).
3) Recién entonces se avanza al siguiente paso.

Si algo falla:
- detenerse
- reportar el error literal
- proponer una única corrección y reintentar

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

## Proyecto Activo
- [Biblia (Quelonio Pages) — Estado vivo](PROYECTO_BIBLIA.md)

## Boot por rol
- [LAUNCHER_BUILD](LAUNCHER_BUILD.md) — Construcción/mantenimiento (build).
- [LAUNCHER_OPS](../LAUNCHER_OPS.md) — Operación (ops).

---

## Archivados (no activos)
Referencia histórica:
- [PROYECTO_WEB_API.md](archived/PROYECTO_WEB_API.md)
- [PROYECTO_RAG_APP.md](archived/PROYECTO_RAG_APP.md)
- [PROYECTO_LATAS.md](archived/PROYECTO_LATAS.md)

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
