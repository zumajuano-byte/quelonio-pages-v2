from pathlib import Path
import re
import shutil

TARGETS = [
    Path("docs/07_Fermentacion_Maduracion/DEEP/40_Troubleshooting_proceso.md"),
    Path("docs/07_Fermentacion_Maduracion/DEEP/10_Targets_y_control_minimo.md"),
    Path("docs/07_Fermentacion_Maduracion/DEEP/01_DEEP_Fermentacion_Maduracion_v1.md"),
    Path("docs/99_Indice_y_Mapas/PROYECTO_BIBLIA.md"),
]

def backup(p: Path) -> None:
    b = p.with_suffix(p.suffix + ".bak2")
    if not b.exists():
        shutil.copy2(p, b)

def fix_text(s: str) -> str:
    # A) Rangos con U+FFFD: 0�?"48, 24�?"72, 1�?"2, 12�?"24h => en-dash
    # Captura: dígito + U+FFFD + ? + (0-2 chars no "word") + dígito
    s = re.sub(r'(\d)\ufffd\?[^\w\n]{0,2}(\d)', r'\1–\2', s)

    # B) Separador textual " �?" " (a veces es �?" con comilla) => em-dash
    s = re.sub(r'\s\ufffd\?[^\w\n]{0,2}\s', ' — ', s)

    # C) Flechas corruptas: �?' => →
    s = s.replace("\ufffd?'", "→")

    # D) Comillas corruptas típicas: �?o ... �?� => “ ... ”
    s = s.replace("\ufffd?o", "“")
    # cierre más común observado en tu salida: �?"  (FFFD + ? + ")
    s = s.replace('\ufffd?"', '”')
    # variantes por si aparecen
    s = s.replace("\ufffd?\ufffd", "”")
    s = s.replace("\ufffd?\u201d", "”")
    s = s.replace("\ufffd?\u201c", "“")

    # E) Subíndices perdidos: CO�,, / O�,, => CO₂ / O₂
    s = s.replace("CO\ufffd,,", "CO₂")
    s = s.replace("O\ufffd,,", "O₂")

    # F) Limpieza en PROYECTO_BIBLIA: evitar literales que disparan el check
    s = s.replace(
        "### A) Mojibake / encoding raro en .md (Ã â€” Â, etc.)",
        "### A) Mojibake / encoding raro en .md (tokens como \\u00C3, \\u00C2, \\u00E2, \\uFFFD)"
    )
    s = s.replace(
        "Pattern 'Ã|â€”|Â|�'",
        "Pattern '\\u00C3|\\u00E2|\\u00C2|\\uFFFD'"
    )

    return s

def process(p: Path) -> tuple[bool, int]:
    if not p.exists():
        return False, 0
    raw = p.read_text(encoding="utf-8", errors="replace")
    fixed = fix_text(raw)

    if fixed != raw:
        backup(p)
        p.write_text(fixed, encoding="utf-8", newline="\n")
        return True, 1
    return False, 0

changed = 0
for p in TARGETS:
    ch, _ = process(p)
    if ch:
        changed += 1
        print(f"FIXED: {p}")

print("DONE changed_files=", changed)
