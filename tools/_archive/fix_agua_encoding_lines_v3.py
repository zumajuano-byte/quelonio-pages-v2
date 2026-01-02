from pathlib import Path
import codecs

ROOT = Path("docs/01_Agua")
TRIGGERS = ("Ã", "Â", "â", "ï»¿")

def read_utf8_no_bom(p: Path) -> str:
    b = p.read_bytes()
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]
    return b.decode("utf-8", errors="strict")

def can_encode(s: str, enc: str) -> bool:
    try:
        s.encode(enc)
        return True
    except Exception:
        return False

def protect_unencodable(s: str, enc: str):
    # Protege solo chars que NO se pueden encodear en enc
    repl = {}
    out = []
    i = 0
    for ch in s:
        try:
            ch.encode(enc)
            out.append(ch)
        except Exception:
            key = f"[[X{i}]]"
            repl[key] = ch
            out.append(key)
            i += 1
    return "".join(out), repl

def unprotect(s: str, repl: dict) -> str:
    for k, v in repl.items():
        s = s.replace(k, v)
    return s

def trigger_score(s: str) -> int:
    return sum(s.count(t) for t in TRIGGERS)

def try_fix(s: str, enc: str) -> str | None:
    # Revertir mojibake típico: texto actual (mal interpretado cp1252/latin1) -> UTF-8 real
    if not can_encode(s, enc):
        protected, repl = protect_unencodable(s, enc)
        try:
            cand = protected.encode(enc).decode("utf-8")
            return unprotect(cand, repl)
        except Exception:
            return None
    else:
        try:
            return s.encode(enc).decode("utf-8")
        except Exception:
            return None

def fix_line(line: str) -> str:
    if not any(t in line for t in TRIGGERS):
        return line

    best = line
    best_sc = trigger_score(line)

    # probamos cp1252 primero (es el caso típico de â€œ â€ etc), luego latin1
    for enc in ("cp1252", "latin1"):
        cand = try_fix(line, enc)
        if cand is None:
            continue
        sc = trigger_score(cand)
        if sc < best_sc:
            best, best_sc = cand, sc
            if best_sc == 0:
                break

    return best

fixed_files = 0
fixed_lines_total = 0

for p in ROOT.rglob("*.md"):
    if p.name.endswith((".bak", ".bak2")):
        continue

    txt = read_utf8_no_bom(p)
    lines = txt.splitlines(True)

    new_lines = []
    changed = False
    fixed_lines = 0

    # hasta 2 pasadas por archivo (por si había doble-mojibake en una misma línea)
    for _ in range(2):
        tmp_lines = []
        tmp_changed = False
        tmp_fixed = 0

        for ln in (new_lines if new_lines else lines):
            new_ln = fix_line(ln)
            if new_ln != ln:
                tmp_changed = True
                tmp_fixed += 1
            tmp_lines.append(new_ln)

        new_lines = tmp_lines
        if tmp_changed:
            changed = True
            fixed_lines += tmp_fixed
        else:
            break

    new_txt = "".join(new_lines)
    if changed and new_txt != txt:
        p.write_bytes(new_txt.encode("utf-8"))  # UTF-8 sin BOM
        fixed_files += 1
        fixed_lines_total += fixed_lines
        print(f"FIXED: {p} (lines={fixed_lines})")

print("DONE fixed_files=", fixed_files, "fixed_lines_total=", fixed_lines_total)
