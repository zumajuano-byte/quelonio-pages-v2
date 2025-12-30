# CONTRATO MÉTODO V2 (Quelonio Pages)

## Objetivo único
Expandir la Biblia con conocimiento bibliográfico (PDFs) de forma trazable, para que el Asistente use SOLO lo publicado en la Biblia como criterio.

## Regla de oro (NO mezclar)
1 tema = 1 archivo destino por vez.
No se crean nombres nuevos “porque sí”. Si falta, se propone y se aprueba ANTES.

## Formato canónico de reglas
- IDs globales: R-0001, R-0002...
- Cada regla incluye:
  - Regla (en español claro)
  - Traducción/nota EN si ayuda (opcional)
  - Cita corta textual (<=25 palabras)
  - FuenteID + ubicación exacta (ej: B022 p88 fig12)

## Flujo por libro (sin humo)
1) Elegimos módulo + archivo destino.
2) Extraigo reglas SOLO desde páginas concretas que vos me des / o que estén ya subidas.
3) Te entrego bloque listo para pegar (mismo formato siempre).
4) Vos pegás, corrés `mkdocs build --strict`, commit + push.
5) Checkpoint en PROYECTO_BIBLIA / SESSIONS_LOG.

## Archivos maestros
- REGLAS_INDEX.md: índice de reglas (mapa).
- REGISTRO_FUENTES.md: catálogo de PDFs y FuenteID.
