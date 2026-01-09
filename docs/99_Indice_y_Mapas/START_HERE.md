# START_HERE — OS Boot (ACI)

Este repo/documentación es la base operativa del **ACI (Asesor Cervecero Inteligente)**.

## Regla crítica (cero supuestos)
Antes de responder o proponer cualquier cosa, se hace SIEMPRE este orden:
1) Leer este archivo (START_HERE).
2) Leer LAUNCHER.
3) Verificar ESTRUCTURA_REPO (inventario) antes de nombrar/crear/editar rutas.

## Entrada mínima (para que el inicio funcione siempre)
Cuando el usuario diga “volvemos”, el arranque correcto es:
- URL canónica abierta (home): `https://zumajuano-byte.github.io/quelonio-pages-v2/`
- Luego el usuario pega 1 de estos dos prompts (uno solo):
  - ACI_OPS_PROMPT (modo operacional)
  - ACI_DEV_PROMPT (modo desarrollador / correcciones)
Si NO pegó ninguno todavía: no hacer nada más. Solo pedir que lo pegue.

## Modos
### ACI-OPS (operacional)
- Rol: consultor.
- Regla: NO proponer cambios al repo.
- Si se detecta un problema: decir
  “Para corregir esto, pasemos a ACI-DEV. Pegame el ACI_DEV_PROMPT.”
  y pedir el error exacto (texto literal) si aplica.

### ACI-DEV (desarrollador)
- Rol: corregir arranque / menú / contratos mínimos.
- Regla: cambios siempre vía OpenCode.
- Regla: 1 tarea = 1 commit.
- Entrega: bloques copy/paste + lista exacta de archivos tocados + mensajes de commit.

## Selección de proyecto activo (SIN last_updated)
Prohibido seleccionar proyecto por timestamps (`last_updated`).
- Si el usuario pegó una URL directa a un PROYECTO_*.md: ese es el proyecto activo.
- Si no está claro: abrir LAUNCHER y pedir elección explícita.

## Proyectos activos (vivos)
- Biblia (Pages): `docs/99_Indice_y_Mapas/PROYECTO_BIBLIA.md`
- Web + API (MVP): `docs/99_Indice_y_Mapas/PROYECTO_WEB_API.md`
- Asistente v1: `docs/99_Indice_y_Mapas/ASISTENTE_V1.md`

## Archivados (no participan del arranque)
- Latas: `docs/99_Indice_y_Mapas/PROYECTO_LATAS.md`
- RAG App: `docs/99_Indice_y_Mapas/PROYECTO_RAG_APP.md` (integrado al ACI; no es proyecto vivo)
