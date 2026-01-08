# SESSIONS_LOG — Bitácora global (Quelonio)

> Nota: este archivo es histórico.
> La continuidad operativa se maneja con el “Prompt de Avances (V2)” en el chat.


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


### 2026-01-08 — Consolidación final: Schema Excel-first + Single Active Project
- **Hecho: Excel-first schema completado** (docs/12_Datasets_Materias_Primas/_schema/):
  - DATA_CONTRACT_EXCEL_V1.md (estructuras multi-libro + columnas mínimas)
  - ID_CONVENTION_V1.md (ULID + codes correlativos; modo Excel-first)
  - CODE_COUNTERS_V1.md (generación atómica de codes en backend)
  - EXCEL_WORKFLOW_OVERVIEW.md (resumen claro Bible vs Excel vs App)
  - _INDEX.md (punto de entrada canónico)
- **Hecho: Single active project** (solo PROYECTO_BIBLIA.md activo):
  - PROYECTO_WEB_API.md / PROYECTO_RAG_APP.md / PROYECTO_LATAS.md archivados con banner "ARCHIVED"
  - LAUNCHER.md simplificado + links directos a archived/
  - Links rotos en archived/ corregidos para mkdocs --strict
- **Hecho: Enlaces cross** (LAUNCHER_BUILD.md enlaza _schema/_INDEX.md)
- **Estado final:** mkdocs build --strict OK (sin warnings)
- **Referencias commits (tanda completa):**
  - 1581189 Implement Market Snapshots v1...
  - 101fb65 Improve LAUNCHER_OPS with data usage protocol...
  - b9dc353 Add 3 market yeast items...
  - b1747a6 Add 4 Argentina-first hop items...
  - 3f6e3fa Align 3 generic items to standard incidence v1...
  - 16c1a5d Align 3 generic items...
  - fd34765 Add EXAMPLE__snapshot_v1.md...
  - fb6d44c docs(datasets): link example snapshot...
  - 163ecbc docs(inventory): regenerate ESTRUCTURA_REPO
  - 7a433e2 docs(datasets): add AR market snapshot pilsen 25kg...
  - 6f04d71 docs(schema): add Excel data contract v1...
  - 67ce29d docs(schema): define ID convention v1...
  - 0319c5e docs(schema): clarify Excel-first ID generation...
  - 43b3a0b docs(schema): define code counters v1...
  - 31f5f21 docs(schema): add Excel workflow overview...
  - 86af448 docs(schema): add _schema index entrypoint
  - 5218511 docs(launcher): link Excel schema index entrypoint
  - 56806df docs: consolidate single active project...
  - ff90106 docs: fix archived links to pass mkdocs --strict
