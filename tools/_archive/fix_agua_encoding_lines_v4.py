from pathlib import Path
import codecs

ROOT = Path("docs/01_Agua")

# Señales típicas (y también vamos a penalizar controles C1 que suelen quedar en estas corrupciones)
TRIG = ("Ã", "Â", "â", "ï»¿")
def has_c1_controls(s: str) -> bool:
    return any(0x80 <= ord(ch) <= 0x9F for ch in s)

def score(s: str) -> int:
    base = sum(s.count(t) for t in TRIG) * 10
    c1 = sum(1 for ch in s if 0x80 <= ord(ch) <= 0x9F) * 50
    rep = s.count("\ufffd") * 200
    return base + c1 + rep

def read_utf8_no_bom(p: Path) -> str:
    b = p.read_bytes()
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]
    return b.decode("utf-8", errors="strict")

# Mapa Unicode char -> byte CP1252 (incluye la zona 0x80..0x9F y los “undefined” como U+0081 etc)
CP1252_MAP = {}
for b in range(256):
    ch = bytes([b]).decode("cp1252", errors="strict")
    # Si hay colisiones raras, nos quedamos con la primera; para nuestro uso es suficiente
    CP1252_MAP.setdefault(ch, b)

def to_cp1252_bytes(s: str) -> bytes | None:
    out = bytearray()
    for ch in s:
        if ch in CP1252_MAP:
            out.append(CP1252_MAP[ch])
        else:
            o = ord(ch)
            # si es un byte “latin1 puro”, lo dejamos pasar (evita romper espacios normales etc.)
            if o <= 0xFF:
                out.append(o)
            else:
                return None
    return bytes(out)

def try_fix_line(line: str) -> str | None:
    # Solo intentar si hay señales reales
    if not any(t in line for t in TRIG) and not has_c1_controls(line):
        return None

    b = to_cp1252_bytes(line)
    if b is None:
        return None

    try:
        return b.decode("utf-8", errors="strict")
    except Exception:
        return None

def process_file(p: Path) -> tuple[bool, int]:
    txt = read_utf8_no_bom(p)
    lines = txt.splitlines(True)

    changed = False
    fixed_lines = 0

    # hasta 2 pasadas, por si había doble mojibake en la misma línea
    for _ in range(2):
        new_lines = []
        pass_changed = False

        for ln in lines:
            cand = try_fix_line(ln)
            if cand is not None and score(cand) < score(ln):
                new_lines.append(cand)
                pass_changed = True
                fixed_lines += 1
            else:
                new_lines.append(ln)

        lines = new_lines
        if pass_changed:
            changed = True
        else:
            break

    new_txt = "".join(lines)
    if changed and new_txt != txt:
        p.write_bytes(new_txt.encode("utf-8"))  # UTF-8 sin BOM
        return True, fixed_lines
    return False, 0

fixed_files = 0
fixed_lines_total = 0

for p in ROOT.rglob("*.md"):
    if p.name.endswith((".bak", ".bak2")):
        continue
    ch, n = process_file(p)
    if ch:
        fixed_files += 1
        fixed_lines_total += n
        print(f"FIXED: {p} (lines={n})")

print("DONE fixed_files=", fixed_files, "fixed_lines_total=", fixed_lines_total)
