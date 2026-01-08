# START_HERE — Quelonio OS Boot (Determinístico)

Este archivo define **cómo arrancar una sesión** sin ambigüedad, para evitar inconsistencias entre chats.

## Regla de arranque (determinística)

**Entrada mínima recomendada (proyecto activo):**
volvemos
URL: https://zumajuano-byte.github.io/quelonio-pages-v2/
- Inventario del repo (árbol canónico): [ESTRUCTURA_REPO](ESTRUCTURA_REPO.md)



Con eso, el asistente debe:
1) Abrir este `START_HERE`.
2) Resolver **proyecto activo** usando la regla “Selección automática” (abajo).
3) Abrir el archivo del proyecto elegido (`PROYECTO_*.md`) y operar **solo desde su CURRENT_STATE**.

## Selección automática del proyecto activo

Si el usuario no especifica proyecto, el proyecto activo se determina así:

11) Abrir estos 3 archivos:
   - `99_Indice_y_Mapas/PROYECTO_BIBLIA.md`
   - `99_Indice_y_Mapas/PROYECTO_RAG_APP.md`
   - `99_Indice_y_Mapas/PROYECTO_LATAS.md`


2) Elegir como “activo” el que tenga **`last_updated` más reciente** (formato `YYYY-MM-DD`).
3) Si falta `last_updated` o hay empate, usar **Biblia** como default.

## Cambio explícito de proyecto

Para evitar cualquier duda, el usuario puede arrancar así:

- **Biblia**
volvemos
Proyecto — Biblia: [PROYECTO_BIBLIA](PROYECTO_BIBLIA.md)

- **RAG App**
volvemos
Proyecto — RAG App: [PROYECTO_RAG_APP](PROYECTO_RAG_APP.md)


- **Latas**
volvemos
Proyecto — Latas: [PROYECTO_LATAS](PROYECTO_LATAS.md)


## Protocolo de cierre (para no “manosear” muchos archivos)

Al cerrar una sesión de un proyecto:
1) Actualizar **solo** el archivo `PROYECTO_*.md` correspondiente:
   - `last_updated`
   - `CURRENT_STATE` (qué se hizo + próximo paso + hilos abiertos)
   - (Opcional) agregar una entrada breve en “LOG del proyecto”
2) No tocar `SESSIONS_LOG.md` salvo cambios de metodología / reglas globales.

## Si algo no cierra

Abrir `99_Indice_y_Mapas/LAUNCHER.md` para seleccionar proyecto manualmente o revisar reglas de operación.

## Boot operativo (terceros)

Para acceso directo a rutas operativas sin entrar en lógica de proyectos: [LAUNCHER_OPS](../LAUNCHER_OPS.md)
