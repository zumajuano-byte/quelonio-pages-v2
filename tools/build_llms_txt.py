#!/usr/bin/env python3
"""Step 306 - Build curated llms.txt files for agent-friendly onboarding."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LLMS_TXT = ROOT / "llms.txt"
LLMS_FULL_TXT = ROOT / "llms-full.txt"

SECTIONS = [
    ("agua", "docs/01_Agua/"),
    ("malta", "docs/02_Malta/"),
    ("levadura", "docs/03_Levadura/"),
    ("lupulo", "docs/04_Lupulo/"),
    ("procesos_produccion", "docs/05_Sistemas_IPA_Moderna/"),
    ("qa_qc", "docs/06_Procesos_QA_QC/"),
    ("fermentacion_maduracion", "docs/07_Fermentacion_Maduracion/"),
    ("recetas_formulacion", "docs/08_Recetas_Formulacion/"),
    ("empaque_estabilidad", "docs/09_Empaque_Estabilidad/"),
    ("limpieza_sanitizacion", "docs/10_Limpieza_Sanitizacion/"),
    ("sensorial", "docs/11_Sensorial/"),
    ("datasets_materias_primas", "docs/12_Datasets_Materias_Primas/"),
    ("negocio_verdad_negocio", "docs/98_Verdad_Negocio/"),
    ("indices_mapas", "docs/99_Indice_y_Mapas/"),
]

ENTRYPOINTS = [
    "README.md",
    "mkdocs.yml",
    "docs/99_Indice_y_Mapas/",
    "docs/01_Agua/",
    "docs/06_Procesos_QA_QC/",
    "docs/98_Verdad_Negocio/",
]


def build_llms_txt() -> str:
    lines = [
        "# Quelonio Pages - llms.txt",
        "",
        "Quelonio Pages (Biblia Quelonio) es la fuente de verdad tecnica y operativa del proyecto.",
        "Usar este repo para responder consultas de produccion, QA/QC y decision de negocio con evidencia interna.",
        "",
        "## Como usar esta Biblia",
        "1. Leer primero README.md y la navegacion en mkdocs.yml.",
        "2. Entrar por 99_Indice_y_Mapas y luego bajar a secciones canonicas.",
        "3. Citar rutas concretas de docs al responder.",
        "",
        "## Secciones principales (curadas)",
    ]
    for name, path in SECTIONS:
        lines.append(f"- {name}: {path}")

    lines.extend(
        [
            "",
            "## Convenciones de trabajo",
            "- No inventar datos: priorizar evidencia interna del repo.",
            "- Referenciar ruta exacta (y seccion cuando aplique).",
            "- Si hay conflicto entre notas deep/borradores y material canonico, priorizar secciones troncales.",
            "",
            "## Limites y prioridad",
            "Puede existir material deep, drafts o anexos auxiliares. Priorizar contenido canonico de docs y su navegacion principal.",
            "",
        ]
    )
    return "\n".join(lines)


def build_llms_full_txt() -> str:
    lines = [
        "# Quelonio Pages - llms-full.txt",
        "",
        "## Resumen del repo",
        "Repositorio de Biblia Quelonio para conocimiento tecnico-operativo, QA/QC y verdad de negocio.",
        "La fuente primaria es docs/ + navegacion declarada en mkdocs.yml.",
        "",
        "## Mapa relevante",
        "- docs/: contenido principal de referencia",
        "- mkdocs.yml: estructura de navegacion canonicamente publicada",
        "- tools/: scripts operativos, import/export y contratos de pasos",
        "- data/: artefactos de trabajo y salida de procesos",
        "",
        "## Entradas recomendadas",
    ]
    for entry in ENTRYPOINTS:
        lines.append(f"- {entry}")

    lines.extend(
        [
            "",
            "## Secciones curadas de la Biblia",
        ]
    )
    for name, path in SECTIONS:
        lines.append(f"- {name}: {path}")

    lines.extend(
        [
            "",
            "## Lectura por tipo de consulta",
            "- Produccion/proceso: 05_Sistemas_IPA_Moderna, 07_Fermentacion_Maduracion, 09_Empaque_Estabilidad.",
            "- QA/QC: 06_Procesos_QA_QC, 10_Limpieza_Sanitizacion, 11_Sensorial.",
            "- Materias primas/formulacion: 01_Agua, 02_Malta, 03_Levadura, 04_Lupulo, 08_Recetas_Formulacion.",
            "- Negocio/decision: 98_Verdad_Negocio y 99_Indice_y_Mapas.",
            "",
            "## Buenas practicas para agentes",
            "- Citar siempre ruta interna exacta al justificar una respuesta.",
            "- Si aplica, incluir nombre de seccion/encabezado para trazabilidad.",
            "- Evitar mezclar contenido canonico con borradores sin advertirlo.",
            "- Marcar explicitamente supuestos cuando no haya evidencia directa.",
            "",
            "## Nota de alcance",
            "La Biblia convive con material deep y algunos insumos auxiliares (incluyendo PDFs/fuentes de soporte).",
            "Para respuestas operativas, priorizar docs canonicos y navegacion oficial de MkDocs.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    LLMS_TXT.write_text(build_llms_txt(), encoding="utf-8")
    LLMS_FULL_TXT.write_text(build_llms_full_txt(), encoding="utf-8")
    print(f"[PASS] wrote {LLMS_TXT}")
    print(f"[PASS] wrote {LLMS_FULL_TXT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
