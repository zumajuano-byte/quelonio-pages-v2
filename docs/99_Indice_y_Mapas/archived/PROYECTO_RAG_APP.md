# PROYECTO — RAG App (Soporte amplificado para Biblia + PDFs)

# ARCHIVED — referencia histórica (no activo)

Proyecto activo único: [PROYECTO_BIBLIA.md](../PROYECTO_BIBLIA.md)

---

last_updated: 2026-01-05

## CURRENT_STATE (estado vivo)

### Objetivo del proyecto
Construir una app RAG que permita consultar conocimiento desde:
- Biblia V2 (sitio MkDocs) como “cerebro operacional”
- Biblioteca de PDFs (Drive) como soporte ampliado

### Alcance (MVP)
- Ingesta de PDFs (con control de fuentes y versionado básico)
- Indexación (chunks + embeddings)
- Consulta (pregunta → recuperación → respuesta con citas)
- UI mínima (web) o endpoint API para consumir desde otras capas

### NO alcance (por ahora)
- “Entrenar” un modelo con los PDFs (no fine-tuning)
- Agentes complejos / workflows largos
- Automatizaciones de extracción masiva sin control de calidad

### Hilos abiertos
- Definir stack (local primero) y dónde se aloja el vector store
- Definir contrato de API (ver `CONTRATO_RAG_API.md`)
- Definir qué fuentes entran al MVP (PDFs prioritarios + páginas clave de Biblia)

### Próximo paso (1)
Dejar el **Contrato RAG API** cerrado y estable (endpoints + payloads + criterios de aceptación).
