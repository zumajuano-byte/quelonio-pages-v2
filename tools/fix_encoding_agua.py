import codecs
from pathlib import Path

ROOT = Path("docs/01_Agua")
CP = "cp1252"  # más correcto que latin1 para comillas/tildes “ ” ’

def score(s: str) -> int:
    # disparadores típicos de mojibake
    return sum(s.count(x) for x in ("Ã", "Â", "â", "ï»¿", "\ufffd"))

changed = 0
for p in ROOT.rglob("*.md"):
    if p.name.endswith(".bak"):
        continue

    b = p.read_bytes()
    # quitar BOM UTF-8 si existe
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]

    # decode strict: UTF-8 o CP1252 si hace falta
    try:
        txt = b.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        txt = b.decode(CP, errors="strict")

    # Si parece mojibake, intentar “deshacer” CP1252->UTF8
    if any(x in txt for x in ("Ã", "Â", "â", "ï»¿")):
        try:
            fixed = txt.encode(CP).decode("utf-8")
            if score(fixed) < score(txt):
                txt = fixed
        except Exception:
            pass

    # escribir UTF-8 sin BOM
    out = txt.encode("utf-8")
    p.write_bytes(out)
    changed += 1

print(f"OK: processed {changed} files under {ROOT}")
