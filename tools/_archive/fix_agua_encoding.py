from pathlib import Path
import codecs

ROOT = Path("docs/01_Agua")
TRIGGERS = ("Ã", "Â", "â", "ï»¿")
CP = "cp1252"

def score(s: str) -> int:
    # Menor es mejor: penaliza mojibake + reemplazos
    return sum(s.count(t) for t in TRIGGERS) * 10 + s.count("\ufffd") * 100

def try_fix(s: str, enc: str) -> str | None:
    # Interpretar el texto actual como bytes en enc (cp1252/latin1) y decodificar como UTF-8
    try:
        return s.encode(enc).decode("utf-8")
    except Exception:
        return None

def read_text_no_bom(p: Path) -> str:
    b = p.read_bytes()
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]
    # si es UTF-8 válido, usarlo; si no, fallback cp1252
    try:
        return b.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        return b.decode(CP, errors="strict")

fixed = []
processed = 0

for p in ROOT.rglob("*.md"):
    if p.name.endswith((".bak", ".bak2")):
        continue

    txt = read_text_no_bom(p)
    processed += 1

    best = txt
    best_score = score(txt)

    # Intentos de reparación típicos
    for enc in (CP, "latin1"):
        cand = try_fix(txt, enc)
        if cand is None:
            continue
        sc = score(cand)
        if sc < best_score:
            best, best_score = cand, sc

    if best is not txt:
        p.write_bytes(best.encode("utf-8"))  # UTF-8 sin BOM
        fixed.append(str(p))

print(f"OK processed={processed} fixed={len(fixed)} under {ROOT}")
for f in fixed:
    print("FIXED:", f)
