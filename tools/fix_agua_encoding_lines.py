from pathlib import Path
import codecs

FILES = [
  Path("docs/01_Agua/Agua_Parte2_DEEP/80_Manejo_Ajustes_En_Plantas.md"),
  Path("docs/01_Agua/Agua_Parte2_DEEP/50_pH_en_el_Mash.md"),
  Path("docs/01_Agua/Agua_Parte2_DEEP/60_Sensibilidad_PH_y_Sulfatos.md"),
  Path("docs/01_Agua/Agua_Parte2_DEEP/70_Perfiles_Agua_para_IPA.md"),
  Path("docs/01_Agua/Agua_Parte5_DEEP/00_Indice_Agua_Parte5.md"),
  Path("docs/01_Agua/Agua_Parte6_DEEP/00_Indice_Agua_Parte6.md"),
  Path("docs/01_Agua/Agua_Parte1_DEEP/10_Naturaleza_Quimica_del_Agua.md"),
]

TRIGGERS = ("Ã", "Â", "â", "ï»¿")

def fix_mojibake_line(line: str) -> str:
    if not any(t in line for t in TRIGGERS):
        return line
    # Intentar revertir mojibake Latin1/CP1252 -> UTF-8
    for enc in ("cp1252", "latin1"):
        try:
            return line.encode(enc).decode("utf-8")
        except Exception:
            pass
    return line  # si no se puede, no tocar

def read_utf8_no_bom(p: Path) -> str:
    b = p.read_bytes()
    if b.startswith(codecs.BOM_UTF8):
        b = b[len(codecs.BOM_UTF8):]
    return b.decode("utf-8", errors="strict")

fixed_files = 0
for p in FILES:
    if not p.exists():
        print("SKIP (missing):", p)
        continue

    txt = read_utf8_no_bom(p)
    lines = txt.splitlines(True)  # conserva \n
    new_lines = [fix_mojibake_line(ln) for ln in lines]
    new_txt = "".join(new_lines)

    if new_txt != txt:
        p.write_bytes(new_txt.encode("utf-8"))  # UTF-8 sin BOM
        fixed_files += 1
        print("FIXED:", p)

print("DONE fixed_files=", fixed_files)
