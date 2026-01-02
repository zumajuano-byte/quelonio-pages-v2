from pathlib import Path
import codecs

ROOT = Path("docs/01_Agua")
TRIGGERS = ("Ã", "Â", "â", "ï»¿")

def read_utf8_no_bom(p: Path) -> str:
    b = p.read_bytes()
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]
    return b.decode("utf-8", errors="strict")

def protect_unicode(s: str):
    # Protege chars > 255 con tokens ASCII, para permitir encode(cp1252/latin1)
    repl = {}
    out = []
    i = 0
    for ch in s:
        if ord(ch) > 255:
            key = f"[[U{i}]]"
            repl[key] = ch
            out.append(key)
            i += 1
        else:
            out.append(ch)
    return "".join(out), repl

def unprotect_unicode(s: str, repl: dict) -> str:
    for k, v in repl.items():
        s = s.replace(k, v)
    return s

def trigger_score(s: str) -> int:
    return sum(s.count(t) for t in TRIGGERS)

def fix_line(line: str) -> str:
    if not any(t in line for t in TRIGGERS):
        return line

    protected, repl = protect_unicode(line)

    best = line
    best_score = trigger_score(line)

    for enc in ("cp1252", "latin1"):
        try:
            cand = protected.encode(enc).decode("utf-8")
            cand = unprotect_unicode(cand, repl)
            sc = trigger_score(cand)
            if sc < best_score:
                best, best_score = cand, sc
                if best_score == 0:
                    break
        except Exception:
            pass

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

    for ln in lines:
        new_ln = fix_line(ln)
        if new_ln != ln:
            changed = True
            fixed_lines += 1
        new_lines.append(new_ln)

    if changed:
        p.write_bytes("".join(new_lines).encode("utf-8"))  # UTF-8 sin BOM
        fixed_files += 1
        fixed_lines_total += fixed_lines
        print(f"FIXED: {p} (lines={fixed_lines})")

print("DONE fixed_files=", fixed_files, "fixed_lines_total=", fixed_lines_total)
