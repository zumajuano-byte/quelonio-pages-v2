# DATASETS — Schema (v1)

Convenciones:
- Unidades base para reportes de agua: **ppm = mg/L**.
- Para alcalinidad: preferir **ppm como CaCO3** (y opcionalmente mEq/L si se agrega luego).
- Todo dataset incluye `meta.version` y `meta.source`.

---

## B010 — `bjcp_beer_styles_es.json`

```json
{
  "meta": {
    "version": "1.0.0",
    "source": "BJCP 2021 Guidelines (ES)",
    "last_updated": "YYYY-MM-DD",
    "notes": "Targets numéricos por estilo para uso operativo."
  },
  "styles": [
    {
      "id": "1A",
      "category": "1",
      "subcategory": "A",
      "name": "American Light Lager",
      "family": "Lager",
      "stats": {
        "og": { "min": 1.028, "max": 1.040 },
        "fg": { "min": 0.998, "max": 1.008 },
        "ibu": { "min": 8, "max": 12 },
        "srm": { "min": 2, "max": 3 },
        "abv": { "min": 2.8, "max": 4.2 }
      },
      "tags": ["clean", "light", "lager"]
    }
  ]
}
```

Capa 2 (si se agrega):
- `sensory`: descriptores (aroma/sabor/apariencia/mouthfeel).
- `commercial_examples`: lista.
- `subprofiles`: targets alternativos.

---

## B011 — `brew_math_formulas.json`

```json
{
  "meta": {
    "version": "1.0.0",
    "source": "Matemática de la cerveza",
    "last_updated": "YYYY-MM-DD"
  },
  "formulas": [
    {
      "id": "abv_basic",
      "name": "ABV (aprox.)",
      "description": "Cálculo básico a partir de OG y FG.",
      "expression": "(og - fg) * 131.25",
      "variables": [
        { "key": "og", "unit": "SG", "required": true },
        { "key": "fg", "unit": "SG", "required": true }
      ],
      "output": { "unit": "% v/v" },
      "constraints": {
        "og_min": 1.000,
        "og_max": 1.200,
        "fg_min": 0.980,
        "fg_max": 1.200
      }
    }
  ]
}
```

---

## W010-A — `water_report_example.json`

```json
{
  "meta": {
    "version": "1.0.0",
    "source": "User input template",
    "last_updated": "YYYY-MM-DD"
  },
  "report": {
    "source_name": "Proveedor / Pozo / Red",
    "report_date": "YYYY-MM-DD",
    "units": "ppm",
    "ions_ppm": {
      "ca": 0,
      "mg": 0,
      "na": 0,
      "cl": 0,
      "so4": 0,
      "hco3": 0
    },
    "alkalinity_as_caco3_ppm": 0,
    "ph": null,
    "notes": ""
  }
}
```

---

## W010-B — `water_treatment_defaults.json`

```json
{
  "meta": {
    "version": "1.0.0",
    "source": "Operational defaults",
    "last_updated": "YYYY-MM-DD",
    "scope": "Capa 1"
  },
  "salts": [
    {
      "id": "gypsum",
      "name": "Yeso",
      "chemical": "CaSO4·2H2O",
      "assumptions": {
        "purity": 1.0,
        "adds_ppm_per_g_per_10l": { "ca": 61.5, "so4": 147.4 }
      }
    }
  ],
  "acids": [
    {
      "id": "lactic_85",
      "name": "Ácido láctico 85%",
      "assumptions": {
        "strength_w_w": 0.85,
        "density_g_ml": 1.20
      },
      "notes": "Defaults; si cambia proveedor/lote, se ajusta."
    },
    {
      "id": "phosphoric_85",
      "name": "Ácido fosfórico 85%",
      "assumptions": {
        "strength_w_w": 0.85,
        "density_g_ml": 1.685
      }
    }
  ]
}
```

---

## W010-C — `water_profiles_canonical.json`

```json
{
  "meta": {
    "version": "1.0.0",
    "source": "Quelonio canonical targets",
    "last_updated": "YYYY-MM-DD",
    "scope": "Capa 1"
  },
  "profiles": [
    {
      "id": "hoppy_modern",
      "name": "Hoppy (moderno)",
      "targets_ppm": { "ca": 100, "mg": 10, "na": 20, "cl": 60, "so4": 180, "hco3": 50 },
      "notes": "Perfil inicial; ajustar por estilo y sensorial."
    }
  ]
}
```
