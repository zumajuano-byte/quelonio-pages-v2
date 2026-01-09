# PROYECTO — Biblia (Quelonio Pages)

Este archivo es el **estado vivo** del proyecto Biblia.  
Regla: al cerrar una sesión de Biblia, **se reemplaza este archivo completo** (copiar/pegar).

Links de referencia:
- [START_HERE](START_HERE.md)
- [LAUNCHER](LAUNCHER.md)
- [SESSIONS_LOG (Regla de oro + histórico)](SESSIONS_LOG.md)
- [PROYECTO_WEB_API (Quelonio Brew OS)](PROYECTO_WEB_API.md)
- [ASISTENTE — Knowledge Map](ASISTENTE_KNOWLEDGE_MAP.md)
- [ASISTENTE — Contratos de salida](ASISTENTE_CONTRATOS.md)
- [ASISTENTE — Data Contract Brew OS](ASISTENTE_DATA_CONTRACT.md)


---

## CURRENT_STATE — Biblia (leer esto primero)

- last_updated: 2025-12-22
- project: Biblia (Quelonio Pages)
- mode_default: Operación + Iteración (post-publicación)

### objective_now (1 frase)
Mantener la Biblia “deployable sin deuda” (preflight OK siempre) y consolidar la **Pasada 2 (BIBLIO)** en 07+09 con formato canónico + ejemplos visibles, dejando trazabilidad lista para completar citas reales (cap/sección/página).

### next_3 (máx 3)
1) **Pasada 2 (BIBLIO) — Completar citas reales:** llenar “capítulo/sección/página” en BIBLIO de 07/20, 07/30 y 09/20 (mínimo 3–5 afirmaciones por doc).
2) **Extender BIBLIO a heurísticas de estabilidad/shelf-life:** sumar 1–2 docs DEEP adicionales (p.ej. shelf-life, carbonatación/CO2, DO/TPO operativo) con el mismo patrón.
3) **1 caso real end-to-end:** Spec v1.0 + 1 lote (logs mínimos) + sensorial + ajuste de Spec (registrar loop en 11/DEEP/20).

### open_threads (máx 5)
- Auditoría de redundancias/solapamientos: definir qué es canónico vs “puentes”.
- Estandarizar “BIBLIO canónico” como norma transversal (dónde vive la plantilla madre).
- Gate mínimo de liberación (umbrales medibles) en QA/QC (incluye DO/TPO/CO2 donde aplique).
- Cierre fino 11 Sensorial (opcional): Gate “Liberar / Retener / Investigar” en overview + puentes a 07/10.
- Targets operativos por familia de estilos (agua/pH, pitch/O2/temp, dry hop, DO) como “tablas de referencia”.

### truth_links (verdad vigente / stubs)
- 98 — Verdad de Negocio (Índice): `docs/98_Verdad_Negocio/98_Verdad_Negocio.md`
- Economía unitaria: `docs/98_Verdad_Negocio/01_Economia_Unitaria.md`
- Operaciones: `docs/98_Verdad_Negocio/02_Operaciones.md`
- Specs/Recetas: `docs/98_Verdad_Negocio/03_Specs_Recetas.md`
- QA/QC: `docs/98_Verdad_Negocio/04_QAQC.md`
- Branding/Comms: `docs/98_Verdad_Negocio/05_Branding_Comms.md`

---

## Checklist de publicación (canónico)

1) `git status`
2) `python -m mkdocs build --strict`
3) `git add -A` → `git commit -m "docs: update biblia <tema>"` → `git push`
4) `python -m mkdocs gh-deploy --clean`
5) Verificación rápida web: Home + módulo tocado

Notas:
- Regla APB: **no deploy** si `.\preflight.ps1` no da OK.
- Windows: vigilar LF/CRLF (ver Runbook).

---

## Runbook — “limpieza técnica” (atajos)

### A) Mojibake / encoding raro en .md (Ã â€” Â, etc.)
1) Detectar:
   - `Select-String -Path .\docs\...\**\*.md -Pattern 'Ã|â€”|Â|�' -AllMatches`
2) Fix (re-interpretar ISO-8859-1 → UTF-8) sobre lista `$files`:
   - `$latin1 = [System.Text.Encoding]::GetEncoding(28591)`
   - `$utf8   = [System.Text.Encoding]::UTF8`
   - `foreach ($f in $files) { $content = Get-Content -LiteralPath $f -Raw; $fixed = $utf8.GetString($latin1.GetBytes($content)); Set-Content -LiteralPath $f -Value $fixed -Encoding utf8 }`
3) Revalidar con `Select-String` y correr `python -m mkdocs build --strict`.

### B) Restos “:contentReference[...]”
- Detectar:
  - `Select-String -Path .\docs\**\*.md -Pattern ":contentReference" -AllMatches`
- Limpiar: borrar esos tokens/líneas y re-correr `.\preflight.ps1`.

### C) Normalización LF (Windows)
1) `.gitattributes` (ejemplo mínimo):
   - `* text=auto eol=lf`
   - `*.ps1 text eol=lf`
2) Git:
   - `git config --global core.autocrlf false`
   - `git config --global core.eol lf`
3) Renormalizar:
   - `git add --renormalize .`
   - `git commit -m "chore: renormalize line endings"`

### D) PowerShell: no usar `&&`
En PowerShell, ejecutar comandos en líneas separadas o con `;` (no `&&`).

---

## CHECKPOINT — Plantilla (copiar/pegar al cerrar sesión)

### Sesión: AAAA-MM-DD
- Objetivo (1 frase):
- Hecho (3–7 bullets):
  -
  -
- Archivos tocados (rutas):
  -
- Resultado verificable:
  - preflight: OK/NO
  - build strict: OK/NO
  - deploy: OK/NO
- Pendientes inmediatos (máx 5):
  1)
  2)
  3)
- Próximo paso recomendado (1):
  -
- Notas / decisiones:
  -

---

# CHECKPOINT (sesión de cierre)

**Fecha:** 2025-12-22  
**Objetivo de la sesión:** Consolidar Pasada 2 (BIBLIO) inicial en 07+09 y publicar sin deuda (build strict + deploy OK).

## Estado técnico (APB)
- Preflight (`.\preflight.ps1`): OK  
- Build strict (`python -m mkdocs build --strict`): OK  
- Deploy (`python -m mkdocs gh-deploy --clean`): OK  
- Sitio: https://zumajuano-byte.github.io/quelonio-pages/

## Referencias de versión (para no “perderse”)
- `main` (commit): `558cf18 docs: fix 07/30 encoding and add BIBLIO blocks in 07/20 and 09/20`
- `gh-pages` (deploy): `7ab5093` (último push por `mkdocs gh-deploy`)

## Qué quedó hecho (resumen corto)
- Se incorporó/ajustó BIBLIO como base operativa en 07/20 y 09/20 (plantilla + afirmaciones).
- Se corrigió 07/30 (encoding/estandarización) y se validó publicación completa.
- Pipeline PowerShell confirmado: commit/push en `main` + build strict + deploy limpio.

## Pendientes inmediatos (próximo bloque lógico)
1) Completar citas reales (capítulo/sección/página) en los BIBLIO ya creados (07/20, 07/30, 09/20).
2) Extender BIBLIO a 1–2 docs DEEP adicionales (shelf-life y/o CO2/estabilidad).
3) Ejecutar 1 caso real end-to-end (Spec → lote → logs → sensorial → ajuste de Spec) y registrarlo como patrón.

## Regla APB vigente
- No commitear ni deployar sin correr `.\preflight.ps1` y que dé **OK**.
- No tocar `SESSIONS_LOG.md` (solo si se decide explícitamente en una sesión).

---

# EXTENSION ESTRATEGICA — Asistente Virtual (Brew OS + Biblia)

## Idea central (1 frase)
La Biblia es la **fuente canónica** (SOT) de conocimiento cervecero y procedimientos; Brew OS es el **sistema operativo** (data + ejecución). El Asistente Virtual conecta ambos: responde, planifica y guía operaciones usando Biblia + datos del sistema.

## Objetivo del Asistente
1) Responder preguntas técnicas de cerveza basándose en la Biblia (recetas, procesos, QA/QC, sensorial).
2) Guiar el uso del sistema Brew OS (cómo cargar recetas, lotes, inventario, ventas, reportes).
3) Producir entregables operativos: Specs, checklists, planes de producción, listas de compras, logs, y “gates” (Listo para fermentar / empacar / liberar).

## Principios (no negociables)
- Fuente de verdad de contenido: **PROYECTO_BIBLIA** (docs).  
- Fuente de verdad de datos: **Brew OS DB** (recetas/lotes/stock/ventas/etc.).
- Si el asistente no puede apoyar una afirmación con Biblia (o datos), debe declararlo y proponer cómo obtenerlo.
- Los “gates” (diacetilo, DO/TPO, estabilidad, liberación) se operan como checklist reproducible (evitar magia).

## Docs canónicos del asistente (v0.1)
- [ASISTENTE — Knowledge Map](ASISTENTE_KNOWLEDGE_MAP.md)
- [ASISTENTE — Contratos de salida](ASISTENTE_CONTRATOS.md)
- [ASISTENTE — Data Contract Brew OS](ASISTENTE_DATA_CONTRACT.md)


---

## Casos de uso (MVP) — definidos

### A) Cerveza (técnico)
- Diseñar receta: estilo objetivo -> targets -> malta -> lupulo -> levadura -> agua -> proceso -> empaque.
- Ajustar receta: cambios por eficiencia, equipo, disponibilidad de insumos.
- Plan de proceso: cronograma por día (mash, boil, whirlpool, pitch, dry hop, cold crash, empaque).
- QA/QC: generar checklist de mediciones y gates (densidad, pH, diacetilo, oxigeno, CO2).
- Troubleshooting: diagnostico por sintomas (off-flavors, baja atenuación, oxidación, turbidez).

### B) Operación / Brew OS (uso del sistema)
- Cómo registrar: receta, lote, consumos, stock, compras, ventas, pagos.
- Validaciones: por qué no deja guardar / qué dato falta / cómo corregir.
- Reportes: “costeo por lote”, “rentabilidad por SKU”, “vencimientos”, “alertas”, “OEE/capacidad”.
- Auditoría: quién cambió qué, cuándo, y por qué.

### C) Entregables automáticos
- SPEC v1.0 (receta + proceso + gates + empaque + QA/QC) en formato canónico.
- Plan de producción semanal (capacidad + calendario + alertas).
- Lista de compras (BOM * lotes planificados - stock disponible).
- Log de producción (TP) y log de empaque/estabilidad.

---

## Interfaz canónica (contrato de integración)

### 1) Entradas del asistente
- Pregunta del usuario (texto).
- Contexto opcional:
  - `org_id`, `user_id`, rol
  - `recipe_id`, `batch_id`, `sku_id`
  - fecha objetivo, volumen, equipo
- Fuentes:
  - Biblia (docs navegables y/o index)
  - Brew OS (DB y entidades)

### 2) Salidas del asistente (formatos estándar)
- Respuesta explicativa + pasos operativos
- Checklist (gates) con “OK/NO” y criterio
- Plan (cronograma) con hitos y dependencias
- Exportables: Markdown / CSV / PDF (más adelante)

### 3) Reglas de citación (BIBLIO)
- Para decisiones técnicas críticas: citar sección/archivo de Biblia (y BIBLIO si existe).
- Si no hay BIBLIO en el doc, el asistente marca “Sin cita canónica aún” y propone completar.

---

## Arquitectura propuesta (alto nivel)

### Componentes
1) **Bible Indexer** (offline o job)
   - Indexa los .md (títulos, anchors, tags) y genera un índice consultable.
2) **Retriever**
   - Dado un query, selecciona pasajes de Biblia relevantes (07/09/11 etc.).
3) **Assistant Orchestrator**
   - Decide si la consulta es: (A) técnico, (B) sistema, (C) mixto.
   - Llama a Brew OS DB cuando se necesitan datos reales (stock, recetas, costos, lotes).
4) **Safety + Policies**
   - Control de permisos (RBAC).
   - Filtrado de respuestas (no inventar datos; no ejecutar acciones sin confirmación).
5) **UI Chat**
   - Panel en Brew OS: chat contextual + botones “generar checklist”, “crear spec”, “exportar”.

---

## Seguridad / Gobernanza
- RBAC: el asistente ve solo datos del `org_id`.
- Auditoría: toda respuesta que genera cambios sugeridos se registra (prompt, entidad, timestamp).
- “Modo operativo”: el asistente no cambia datos automáticamente salvo que el usuario confirme y el producto lo implemente.

---

## Definition of Done (Asistente MVP)
- Responde sobre Biblia con referencias a archivos/secciones (por lo menos 1 link interno).
- Puede generar SPEC v1.0 desde una receta y volumen objetivo.
- Puede generar checklist de gates para 07->09 (diacetilo + oxigeno + empaque).
- Puede responder “cómo hago X en Brew OS” con pasos concretos.
- No inventa datos: si falta un dato, lo pide como input o indica dónde está en el sistema.

---

## Roadmap (1-2-3)

### V1 (sin IA “profunda”)
- Chat + FAQ guiado + búsqueda en Biblia (full-text) + links.
- Plantillas automáticas (SPEC/checklists) basadas en módulos.

### V2 (asistente con retrieval)
- Retrieval sobre Biblia (pasajes + resumen).
- Contexto por entidad (recipe/batch).
- “Recomendaciones” con trazabilidad (por qué).

### V3 (asistente operativo)
- Acciones guiadas (crear receta, planificar lote, generar compra) con confirmación.
- Reportes y alertas proactivas.
- Aprendizaje: mejora de templates con feedback.

---

## Decisión de diseño
Esta Biblia se convierte oficialmente en “Knowledge Base” de Brew OS:
- Todo concepto técnico tiene un doc.
- Todo procedimiento tiene un checklist.
- Toda decisión crítica se conecta a BIBLIO.

Estado: APROBADO (a implementar cuando arranque PROYECTO_WEB_API).

# CHECKPOINT (sesión de cierre)

Fecha: 2025-12-22
Objetivo de la sesión: Consolidar “Docs P0” (datos duros) para habilitar el Asistente + corregir rutas/links para build strict.

## Estado técnico (APB)
- Build strict (`python -m mkdocs build --strict`): OK
- Deploy (`python -m mkdocs gh-deploy --clean`): OK
- Sitio: https://zumajuano-byte.github.io/quelonio-pages/

## Referencias de versión
- `main` (commit): `6f9fb13` docs: add P0 hard-data docs and fix assistant links (water/oxygenation/packaging/shelf-life)
- `gh-pages` (deploy): `e3fd2c2` (último push de gh-deploy)

## Qué quedó hecho (resumen corto)
- “Docs P0” creados y ubicados por módulo:
  - 01_Agua/DEEP/AGUA_CALCULOS_Y_LIMITES.md
  - 03_Levadura/Fermentacion_DEEP/PITCH_RATE_Y_OXIGENACION.md
  - 09_Empaque_Estabilidad/DEEP/{DO_TPO_OBJETIVOS_Y_METODO, CO2_CARBONATACION_TABLAS, SHELF_LIFE_PLAN_Y_CRITERIOS}.md
  - 99_Indice_y_Mapas/TABLAS_TARGETS_POR_ESTILO.md
- Links del Asistente corregidos para strict (sin warnings).

## Pendientes inmediatos (máx 5)
1) Pasada 2 (BIBLIO) en 07 + 09: convertir 3–5 afirmaciones críticas a citas completas.
2) Definir plantilla canónica de cita (1 bloque) y dejar 1 ejemplo completo (“Matriz de afirmaciones”).
3) Preparar el MVP Asistente v1 en PROYECTO_WEB_API (scope + endpoints + formato respuesta + fallback).

## Próximo paso recomendado (1)
Arrancar PROYECTO_WEB_API definiendo MVP v1 del asistente: “preguntas sobre cerveza + sobre el sistema”, usando los Docs P0 como fuentes preferidas.



# CHECKPOINT (sesión de cierre)

**Fecha:** 2025-12-22  
**Objetivo de la sesión:** Validar integridad de links del sitio generado (sin .md en HTML), confirmar que no hay hrefs rotos y que el build strict pasa.

## Estado técnico (APB)
- Preflight (`.\preflight.ps1`): (NO CORRIDO / OK / NO)  
- Build strict (`python -m mkdocs build --strict`): OK  
- Deploy (`python -m mkdocs gh-deploy --clean`): (OK / NO / PENDIENTE)  
- Sitio: https://zumajuano-byte.github.io/quelonio-pages/

## Referencias de versión (para no “perderse”)
- `main` (commit): `0fda720` docs: add MATRIZ_AFIRMACIONES_P0 and link from ASISTENTE_V1
- `gh-pages` (deploy): (completar con `git log -1 gh-pages --oneline`)

## Qué quedó hecho (resumen corto)
- Se confirmó que el HTML final no contiene links `.md` (MkDocs convierte a rutas/carpeta).
- Se corrigió el método de detección de links rotos: resolver `href` relativo a la carpeta del HTML, no al root del site.
- Resultado: `$broken2u.Count = 0` (no hay hrefs rotos locales) y `mkdocs build --strict` OK.

## Pendientes inmediatos (máx 5)
1) (Opcional) Correr `.\preflight.ps1` y registrar OK.
2) (Opcional) Si falta, ejecutar deploy: `python -m mkdocs gh-deploy --clean` y registrar hash `gh-pages`.
3) Seguir con “siguiente paso”: PROYECTO_WEB_API — definir MVP v1 del Asistente (retrieval desde Biblia + contratos de salida).

## Próximo paso recomendado (1)
Arrancar PROYECTO_WEB_API: definir el MVP v1 del Asistente (alcance, endpoints, formatos de respuesta y fallback), usando los Docs P0 + estructura de citación.
