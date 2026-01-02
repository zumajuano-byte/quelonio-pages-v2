from pathlib import Path
import codecs

ROOT = Path("docs/01_Agua")

TRIGGERS = ("Ã", "Â", "â", "ï»¿")
CP = "cp1252"  # mejor que latin1 para comillas “ ” etc

def trigger_count(s: str) -> int:
    return sum(s.count(t) for t in TRIGGERS)

def fix_mojibake(txt: str) -> str:
    # Reversión típica: texto mojibake (CP1252) -> bytes CP1252 -> decode UTF-8
    try:
        return txt.encode(CP).decode("utf-8")
    except Exception:
        return txt

processed = 0
fixed_files = 0

for p in ROOT.rglob("*.md"):
    if p.name.endswith((".bak", ".bak2")):
        continue

    b = p.read_bytes()

    # Strip UTF-8 BOM
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]

    # Decode (prefer UTF-8; fallback CP1252)
    try:
        txt = b.decode("utf-8", errors="strict")
    except UnicodeDecodeError:
        txt = b.decode(CP, errors="strict")

    before = trigger_count(txt)

    if before > 0:
        candidate = fix_mojibake(txt)
        after = trigger_count(candidate)

        # Solo aceptar si mejora
        if after < before:
            txt = candidate
            fixed_files += 1

    # Write UTF-8 no BOM
    p.write_bytes(txt.encode("utf-8"))
    processed += 1

print(f"OK processed={processed} fixed={fixed_files} under {ROOT}")
