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
## hops_coa_example.json

```json
{
  "dataset_id": "hops_coa",
  "version": "0.1",
  "records": [
    {
      "id": "HCOA-0001",
      "variety": "Citra",
      "supplier": "Example Hops Co.",
      "country": "US",
      "product_form": "pellet",
      "pellet_spec": "T90",
      "crop_year": 2025,
      "lot_code": "CIT-25-12345",
      "packaging": "vacuum_foil",
      "net_weight_kg": 5.0,
      "received_date": "2026-01-05",
      "storage": {
        "temperature_c": 0,
        "oxygen_exposure": "minimized",
        "notes": "Stored frozen upon receipt"
      },
      "analysis": {
        "method": "HPLC",
        "alpha_acid_pct": 12.8,
        "beta_acid_pct": 3.9,
        "cohumulone_pct_of_alpha": 23.0,
        "total_oil_ml_per_100g": 2.4,
        "moisture_pct": 8.5,
        "hsi": 0.26
      },
      "traceability": {
        "document_ref": "COA_pdf_or_scan_path_or_link",
        "internal_batch_refs": ["INV-RAW-2026-0007"]
      },
      "notes": "Example record. Replace with real COA values."
    }
  ]
}
```

## hops_coa_defaults.json

```json
{
  "dataset_id": "hops_coa_defaults",
  "version": "0.1",
  "defaults": {
    "product_form": "pellet",
    "pellet_spec": "T90",
    "packaging": "vacuum_foil",
    "storage": {
      "temperature_c": 0,
      "oxygen_exposure": "minimized"
    },
    "analysis": {
      "method": "HPLC"
    }
  },
  "validation_rules": {
    "alpha_acid_pct": {"min": 0.5, "max": 25.0},
    "beta_acid_pct": {"min": 0.1, "max": 15.0},
    "total_oil_ml_per_100g": {"min": 0.1, "max": 6.0},
    "moisture_pct": {"min": 4.0, "max": 12.0},
    "hsi": {"min": 0.15, "max": 1.0},
    "crop_year": {"min": 2000, "max": 2100}
  }
}
```

## hops_alpha_age_model.json (opcional)

```json
{
  "dataset_id": "hops_alpha_age_model",
  "version": "0.1",
  "defaults": {
    "assume_months_since_harvest": 6,
    "temperature_factor": {"0": 0.15, "4": 0.25, "20": 1.0},
    "alpha_loss_per_month_at_20c_relative": 0.02
  },
  "notes": "Capa 2 opcional. Placeholders: calibrar con datos/bibliografía."
}
```

---

## M010 — Dataset: MALT_COA

### M010-A — `malt_coa_example.json` (Capa 1)

**Propósito:** formato canónico de entrada para un COA de malta por lote.

**Campos mínimos sugeridos:**
- `malt_lot.malt_name`
- `malt_lot.malt_type` (`base`, `specialty`, `crystal`, `roasted`, `adjunct`)
- `malt_lot.supplier`
- `malt_lot.lot_code`
- `malt_lot.analysis.moisture_pct`
- `malt_lot.analysis.extract_fine_dry_basis_pct`
- `malt_lot.analysis.color_ebc`

```json
{
  "dataset": "MALT_COA",
  "version": "1.0",
  "malt_lot": {
    "malt_name": "Pale Ale Malt",
    "malt_type": "base",
    "supplier": "Crisp Malt",
    "origin_country": "UK",
    "lot_code": "CRISP-PA-2025-11-18",
    "delivery_date": "2025-12-02",
    "tested_on": "2026-01-06",
    "packaging": {
      "form": "bag",
      "size_kg": 25
    },
    "storage": {
      "temp_c": 16,
      "notes": "lugar seco, bolsa cerrada"
    },
    "analysis": {
      "moisture_pct": 4.2,
      "extract_fine_dry_basis_pct": 80.5,
      "extract_coarse_dry_basis_pct": 79.0,
      "difference_fine_coarse_pct": 1.5,
      "color_ebc": 6.0,
      "protein_pct": 10.8,
      "soluble_protein_pct": 4.2,
      "kolbach_index_pct": 39,
      "diastatic_power_wk": 280,
      "friability_pct": 85,
      "beta_glucan_mg_l": 120,
      "fan_mg_l": 180,
      "ph": 5.8
    },
    "coa_document_ref": "COA_2025-11-18_Crisp_PaleAle.pdf",
    "notes": "Ejemplo. Completar/ajustar a tu COA real. Si no hay un campo, dejar null y usar defaults."
  }
}
```

### M010-B — `malt_coa_defaults.json` (Capa 1)

**Propósito:** defaults operativos + reglas de validación.  
Se usa para: warnings, normalización de unidades, fallbacks por tipo de malta (si algún proveedor no reporta todo).

```json
{
  "dataset": "MALT_COA_DEFAULTS",
  "version": "1.0",
  "assumptions": {
    "units": {
      "moisture_pct": "% w/w",
      "extract_*_dry_basis_pct": "% dry basis",
      "color_ebc": "EBC",
      "protein_pct": "% w/w",
      "diastatic_power_wk": "°WK (Windisch-Kolbach)",
      "beta_glucan_mg_l": "mg/L",
      "fan_mg_l": "mg/L"
    },
    "fallbacks": {
      "base_malt": {
        "moisture_pct": 4.5,
        "extract_fine_dry_basis_pct": 80.0,
        "color_ebc": 6.0,
        "protein_pct": 11.0,
        "diastatic_power_wk": 250
      },
      "pilsner_malt": {
        "moisture_pct": 4.5,
        "extract_fine_dry_basis_pct": 80.0,
        "color_ebc": 4.0,
        "protein_pct": 10.5,
        "diastatic_power_wk": 300
      },
      "wheat_malt": {
        "moisture_pct": 5.0,
        "extract_fine_dry_basis_pct": 83.0,
        "color_ebc": 4.5,
        "protein_pct": 12.5,
        "diastatic_power_wk": 250
      },
      "crystal_malt": {
        "moisture_pct": 5.0,
        "extract_fine_dry_basis_pct": 75.0,
        "diastatic_power_wk": 0
      }
    }
  },
  "validation_rules": {
    "moisture_pct": {
      "min": 2.0,
      "max": 8.0,
      "warn_if_gt": 5.5
    },
    "extract_fine_dry_basis_pct": {
      "min": 60.0,
      "max": 88.0,
      "warn_if_lt": 76.0
    },
    "extract_coarse_dry_basis_pct": {
      "min": 55.0,
      "max": 88.0
    },
    "difference_fine_coarse_pct": {
      "min": 0.0,
      "max": 5.0,
      "warn_if_gt": 2.5
    },
    "color_ebc": {
      "min": 1.0,
      "max": 2000.0
    },
    "protein_pct": {
      "min": 6.0,
      "max": 18.0,
      "warn_if_gt": 13.0
    },
    "kolbach_index_pct": {
      "min": 30,
      "max": 50,
      "warn_if_lt": 35,
      "warn_if_gt": 45
    },
    "diastatic_power_wk": {
      "min": 0,
      "max": 500,
      "warn_if_lt": 180
    },
    "friability_pct": {
      "min": 0,
      "max": 100,
      "warn_if_lt": 70
    },
    "beta_glucan_mg_l": {
      "min": 0,
      "max": 2000,
      "warn_if_gt": 250
    },
    "fan_mg_l": {
      "min": 0,
      "max": 350,
      "warn_if_lt": 120
    },
    "ph": {
      "min": 5.0,
      "max": 6.5
    }
  },
  "computed_helpers": {
    "notes": "Cálculos de rendimiento/color viven en BREW_MATH; acá solo normalizamos COA.",
    "map_to_brew_math_inputs": {
      "ppg_potential_formula_ref": "brew_math_formulas.json#potential_ppg_from_extract",
      "color_units_formula_ref": "brew_math_formulas.json#srm_from_ebc"
    }
  }
}
```

### M010-C — `malt_coa_model.json` (Capa 2 opcional)

**Propósito:** convertir COA a inputs operativos (aprox) cuando lo habilitemos.  
Si no querés “modelo” todavía, igual conviene mantener el archivo como placeholder versionado.

```json
{
  "dataset": "MALT_COA_MODEL",
  "version": "1.0",
  "purpose": "Modelo mínimo para convertir COA (extracto+humedad+color) a inputs operativos de receta.",
  "references": [
    {
      "ref": "B011_Matematica_de_la_cerveza",
      "type": "internal_biblia"
    },
    {
      "ref": "BREW_MATH_FORMULAS",
      "file": "brew_math_formulas.json"
    }
  ],
  "functions": {
    "extract_as_is_pct": {
      "description": "Convierte extracto dry-basis a as-is usando humedad.",
      "inputs": {
        "extract_fine_dry_basis_pct": "number",
        "moisture_pct": "number"
      },
      "formula": "extract_as_is = extract_dry_basis * (1 - moisture/100)"
    },
    "potential_ppg": {
      "description": "Potencial de puntos por libra/galón aprox a partir de extracto as-is.",
      "inputs": {
        "extract_as_is_pct": "number"
      },
      "formula": "ppg ≈ 46.21 * (extract_as_is_pct/100)"
    },
    "srm_from_ebc": {
      "description": "Conversión rápida EBC→SRM.",
      "formula": "srm ≈ ebc / 1.97"
    }
  },
  "calibration": {
    "note": "Estos modelos son aproximaciones. Si tenés mediciones reales (rendimiento en planta), recalibrar."
  }
}
```

## Dataset: YEAST_COA (Capa 1)
**Entidad:** lote de levadura (seca/líquida/slurry) con specs de proveedor (cuando existan).

**Campos mínimos (requeridos)**
- `supplier` (string)
- `product_name` (string)
- `lot_id` (string)
- `format` (enum: `dry | liquid | slurry`)

**Campos recomendados (opcionales)**
- `pack_date` (YYYY-MM-DD)
- `best_before` (YYYY-MM-DD)
- `storage_recommendation_c` (string o rango, ej. `"4-10"`)
- `specs.viability_percent_at_pack` (0–100)
- `specs.cell_count_billion_per_g` (dry) o `specs.cell_count_billion_per_ml` (slurry)
- `specs.moisture_percent_max` (dry)
- `specs.bacteria_cfu_per_g_max`, `specs.wild_yeast_cfu_per_g_max` (si el COA lo trae)

**Uso operativo (mínimo)**
- Trazabilidad batch↔lote de levadura.
- Alertas por vencimiento / rotación de stock.
- Base para cálculo de pitch **solo** si hay cell count/viabilidad (o supuestos registrados).

## Dataset: YEAST_COA_MODEL (Capa 2)
**Condición de uso:** solo si existe data mínima y/o supuestos explícitos guardados en el registro del lote.

- Modelo `viability_decay`: estima viabilidad por días y temperatura.
- Modelo `pitch_planning`: computa células requeridas vs disponibles.
