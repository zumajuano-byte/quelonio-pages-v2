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

### 2026-01-08 — Avances Excel-first: SOPs completos + EXCEL_PACK_V1 enlazado
- SOP 1–7 creados + SOP/_INDEX enlazado
- EXCEL_PACK_V1 creado + link en _schema/_INDEX
- LAUNCHER_OPS enlaza SOP index y schema index
- mkdocs build --strict OK
- Referencias commits:
  - c5b1006 docs(schema): link Excel Pack v1 from schema index
  - 03dc365 docs(schema): define Excel Pack v1 (workbooks + SOP mapping)
  - e815f18 docs(ops): link SOP index entrypoint
  - d7465e4 docs(sop): add SOP index entrypoint (1-7)
  - 66bee72 docs(sop): add SOP 7 producto terminado y envasado (Excel-first)
  - 788313b docs(sop): add SOP 6 venta y cobro (Excel-first)
  - e0838b3 docs(sop): add SOP 5 consumo y movimientos de stock (Excel-first)
  - 4ccf5a4 docs(sop): add SOP 4 compras y alta de stock (Excel-first)
  - de3fe2d docs(sop): add SOP 3 crear lote (Excel-first)
  - cf6edc7 docs(sop): add SOP 2 alta de receta (Excel-first)
  - 8ba6910 docs(sop): add SOP 1 alta de item (Excel-first)
  - 7aca5e8 docs(log): add master checkpoint 2026-01-08 (schema + consolidation)
  - ff90106 docs: fix archived links to pass mkdocs --strict
  - 56806df docs: consolidate single active project and archive non-core projects
  - 5218511 docs(launcher): link Excel schema index entrypoint
  - 86af448 docs(schema): add _schema index entrypoint
  - 31f5f21 docs(schema): add Excel workflow overview (Bible vs Excel vs App)
  - 43b3a0b docs(schema): define code counters v1 (correlative codes)
  - 0319c5e docs(schema): clarify Excel-first ID generation (codes now, ULIDs on ingest)
  - 67ce29d docs(schema): define ID convention v1 (ULID + human codes)
  - 6f04d71 docs(schema): add Excel data contract v1 (multi-workbook)
  - 7a433e2 docs(datasets): add AR market snapshot pilsen 25kg (2026-01-08)
  - 163ecbc docs(inventory): regenerate ESTRUCTURA_REPO
  - fb6d44c docs(datasets): link example snapshot in market_snapshots README
  - fd34765 Add EXAMPLE__snapshot_v1.md: didactic example of market snapshot v1 with placeholders, showing both range and fallback modes
  - 1581189 Implement Market Snapshots v1 without hard prices: add MARKET_SNAPSHOT_V1.md, update TEMPLATE_MARKET_SNAPSHOT.md with optional fields, add market_snapshots/README.md, and update index with links
  - 10c6774 Add KIT_AUDITORIA_DATASETS.md: quick audit kit for datasets module with checklist, PowerShell commands, and approval criteria
  - 101fb65 Improve LAUNCHER_OPS with data usage protocol (Excel > Bible > Assumptions) + 2 concrete examples
  - b9dc353 Add 3 market yeast items (US-05, S-04, Lager Dry) v1 with shared harvest minimos checklist, and update index with links
  - b1747a6 Add 4 Argentina-first hop items (Cascade, Columbus/CTZ, Hallertau Mittelfrüh, Mosaic INT) v1 without prices, and update index with links
  - 3f6e3fa Align 3 generic items to standard incidence v1...
  - 16c1a5d Align 3 generic items...
