# Tools — Encoding / Mojibake Fix

## Objetivo
Estos scripts corrigen **mojibake** típico en Markdown (p. ej. `soluciÃ³n`, `â€“`, `Â°C`, comillas raras)
originado por texto interpretado como **CP1252/Latin1** cuando en realidad era **UTF-8**.

El objetivo final es:
- Archivos `.md` en **UTF-8 sin BOM**
- Sin caracteres de reemplazo `�`
- Sin mojibake en contenido

---

## Script recomendado (Agua)
### `tools/fix_agua_encoding_lines_v5.py`
**Qué hace:** intenta reparar mojibake línea por línea (CP1252/Latin1 → UTF-8) y reescribe el archivo en UTF-8 sin BOM.

**Alcance:**
- Solo `docs/01_Agua/**/*.md`
- No toca `.bak`, `.bak2`, `.zip` (si están ignorados / excluidos por glob)

**Uso (desde la raíz del repo):**
```powershell
python tools/fix_agua_encoding_lines_v5.py

# Gate 1: replacement char (si aparece, es prioridad alta)
rg -n "�" docs/01_Agua --glob "!*.bak*"

# Gate 2: mojibake típico
rg -n "ï»¿|Ã|Â|â" docs/01_Agua --glob "!*.bak*"

python -m mkdocs build --strict
