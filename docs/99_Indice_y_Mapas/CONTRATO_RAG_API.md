# CONTRATO — RAG API (MVP)

Este contrato define **qué expone la RAG App** y cómo se consume.  
Objetivo: mínimo viable, trazable y con citas.

## Principios
- Toda respuesta debe incluir **citas** (fuente + ubicación).
- La RAG **recupera** (no “aprende” permanentemente del material).
- Ingesta controlada: fuentes explícitas, sin mezclar “todo” por defecto.

## Entidades (conceptual)
- Source: origen (Biblia V2 / Drive PDF / carpeta / dataset)
- Document: archivo o página
- Chunk: fragmento indexado
- Citation: referencia (doc + sección/página + snippet)

## Endpoints (propuestos)

### GET /api/health
**OK** si la app y el storage están disponibles.

### POST /api/rag/ingest
Ingesta/actualiza una fuente.
**Body mínimo:**
- source_id
- source_type: "pdf_drive" | "biblia_web" | "local"
- mode: "upsert" | "rebuild"

**Respuesta:**
- docs_indexed
- chunks_indexed
- warnings (si aplica)

### POST /api/rag/query
Consulta principal.
**Body mínimo:**
- query (string)
- top_k (int)
- filters (opcional): source_id / doc_id / tags

**Respuesta:**
- answer (string)
- citations: lista de `{source, document, locator, snippet}`
- retrieval_debug (opcional): scores/metadatos

## Criterios de aceptación (MVP)
- El endpoint `/api/rag/query` devuelve siempre `citations` no vacías cuando hay match.
- Si no hay evidencia suficiente: responde “no encontrado” + sugiere qué fuente falta.
- Build/documentación del contrato no rompe `mkdocs --strict`.
