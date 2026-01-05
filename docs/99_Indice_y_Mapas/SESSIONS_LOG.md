# SESSIONS_LOG — Bitácora global (Quelonio)

Este archivo **no** es el “estado vivo” de ningún proyecto.  
El estado vivo está en `PROYECTO_*.md` (uno por proyecto).

## Archivos canónicos (OS Boot)

- `99_Indice_y_Mapas/START_HERE.md`
- `99_Indice_y_Mapas/LAUNCHER.md`
- `99_Indice_y_Mapas/CONTRATO_ESTRUCTURA.md`
- `99_Indice_y_Mapas/PROYECTO_BIBLIA.md`
- `99_Indice_y_Mapas/PROYECTO_RAG_APP.md`
- `99_Indice_y_Mapas/CONTRATO_RAG_API.md`
- `99_Indice_y_Mapas/PROYECTO_LATAS.md`
- (Legacy) `99_Indice_y_Mapas/PROYECTO_WEB_API.md`


## Reglas globales (resumen)

- La sesión debe operar siempre desde el **CURRENT_STATE del proyecto**.
- Cierre: actualizar **solo** el `PROYECTO_*.md` del proyecto trabajado (evitar tocar muchos archivos).
- Antes de deploy: `mkdocs build --strict`.

---

## Bitácora (opcional)

> Usar solo si querés histórico transversal.  
> Si preferís “cero fricción”, logueá dentro de cada `PROYECTO_*.md`.

### Plantilla
**Fecha:** YYYY-MM-DD  
**Proyecto:** Biblia | Web+API | Latas  
**Qué se hizo (bullet points):**
- ...
**Qué quedó abierto:**
- ...
**Próximo paso (1):**
- ...
**Release:** build --strict OK / deploy OK / commit SHA


### 2025-12-22 — Checkpoint PROYECTO_WEB_API (Sprint 1 Infra OK)
- Repo app: `C:\Users\flore\Documents\quelonio-saas`
- Node v20.19.0 (nvm4w), npm 10.8.2
- Next 16.1.0 OK (cuando corre, sirve en http://localhost:3000)
- PostgreSQL local (service postgresql-x64-18) en 5432
- DB `quelonio_saas`, user `quelonio` (CREATEDB), conexión validada
- Prisma validate/generate OK; migrate dev quedó “Already in sync”
- Próximo: crear endpoints en Next App Router:
  - `app/api/health/route.ts`
  - `lib/prisma.ts`
  - endpoint DB ping / primer modelo
- Nota: warning Next por lockfile extra en `C:\Users\flore\package-lock.json` (no bloqueante)
