# Tools - Encoding / Mojibake Fix

## Objetivo
Estos scripts corrigen mojibake tipico en Markdown (por ejemplo: `soluciÃ³n`, `â€“`, `Â°C`, comillas raras) originado por texto interpretado como CP1252/Latin1 cuando en realidad era UTF-8.

Objetivo final:
- Archivos `.md` en UTF-8 sin BOM
- Sin caracteres de reemplazo `�`
- Sin mojibake en contenido

---

## Script recomendado (Agua)
### `tools/fix_agua_encoding_lines_v5.py`
Que hace: intenta reparar mojibake linea por linea (CP1252/Latin1 -> UTF-8) y reescribe el archivo en UTF-8 sin BOM.

Alcance:
- Solo `docs/01_Agua/**/*.md`
- No toca `.bak`, `.bak2`, `.zip` (si estan ignorados/excluidos por glob)

Uso (desde la raiz del repo):
```powershell
python tools/fix_agua_encoding_lines_v5.py

# Gate 1: replacement char (si aparece, es prioridad alta)
rg -n "�" docs/01_Agua --glob "!*.bak*"

# Gate 2: mojibake tipico
rg -n "ï»¿|Ã|Â|â" docs/01_Agua --glob "!*.bak*"

python -m mkdocs build --strict
```
