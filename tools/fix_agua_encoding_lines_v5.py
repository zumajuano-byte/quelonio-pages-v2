from pathlib import Path
import codecs

ROOT = Path("docs/01_Agua")

# señales típicas
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

# Construir reverse-map "cp1252-safe" (latin1 + overrides CP1252 definidos)
# Base latin1: byte -> chr(byte)
byte_to_char = {b: chr(b) for b in range(256)}

# Overrides CP1252 (solo los definidos)
OVR = {
    0x80: "€", 0x82: "‚", 0x83: "ƒ", 0x84: "„", 0x85: "…", 0x86: "†", 0x87: "‡",
    0x88: "ˆ", 0x89: "‰", 0x8A: "Š", 0x8B: "‹", 0x8C: "Œ", 0x8E: "Ž",
    0x91: "‘", 0x92: "’", 0x93: "“", 0x94: "”", 0x95: "•", 0x96: "–", 0x97: "—",
    0x98: "˜", 0x99: "™", 0x9A: "š", 0x9B: "›", 0x9C: "œ", 0x9E: "ž", 0x9F: "Ÿ",
}
byte_to_char.update(OVR)

# Reverse: char -> byte (si hay colisión, nos quedamos con el primero)
char_to_byte = {}
for b in range(256):
    ch = byte_to_char[b]
    char_to_byte.setdefault(ch, b)

def to_cp1252safe_bytes(s: str) -> bytes | None:
    out = bytearray()
    for ch in s:
        if ch in char_to_byte:
            out.append(char_to_byte[ch])
        else:
            o = ord(ch)
            # permitir bytes "directos" <= 255 (no debería pasar mucho, pero es seguro)
            if o <= 0xFF:
                out.append(o)
            else:
                return None
    return bytes(out)

def try_fix_line(line: str) -> str | None:
    if not any(t in line for t in TRIG) and not has_c1_controls(line):
        return None

    b = to_cp1252safe_bytes(line)
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

    # hasta 3 pasadas por si hay doble/triple mojibake en una misma línea
    for _ in range(3):
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
