from pathlib import Path
import codecs

ROOT = Path("docs")
TRIGGERS = ("Ã", "Â", "â", "ï»¿")

def score(s: str) -> int:
    # penaliza triggers + replacement char
    return sum(s.count(t) for t in TRIGGERS) * 10 + s.count("\ufffd") * 200

def read_utf8_no_bom(p: Path) -> str:
    b = p.read_bytes()
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]
    return b.decode("utf-8", errors="strict")

# construir mapa cp1252 (incluye bytes indefinidos como U+0081 si aparecen)
CP1252_MAP = {}
for b in range(256):
    ch = bytes([b]).decode("cp1252", errors="replace")
    CP1252_MAP.setdefault(ch, b)

def to_cp1252_bytes(s: str) -> bytes | None:
    out = bytearray()
    for ch in s:
        if ch in CP1252_MAP:
            out.append(CP1252_MAP[ch])
        else:
            o = ord(ch)
            if o <= 0xFF:
                out.append(o)
            else:
                return None
    return bytes(out)

def try_fix_line(line: str) -> str | None:
    if not any(t in line for t in TRIGGERS) and "\ufffd" not in line:
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

    # hasta 2 pasadas por archivo
    for _ in range(2):
        pass_changed = False
        new_lines = []
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
