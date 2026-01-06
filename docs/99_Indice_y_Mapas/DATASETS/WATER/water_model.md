# WATER — Modelo operativo

## Qué decidimos con datos
1) Elegir `water_source` (reporte real).
2) Elegir `water_target_family` (hoppy / malty / balanced / lager-crisp).
3) Elegir `process_profile` (mash-only vs mash+sparing).

## Qué se calcula “duro”
- Diferencias iónicas (target vs source) → propuesta de sales.
- Regla de lavado: si hay sparge, se acidifica a pH objetivo.

## Qué NO se predice perfecto (y se calibra)
- pH de mash: predicción aproximada. Se vuelve confiable con calibración.
- El dataset debe guardar:
  - pH medido (a 20°C o corregido)
  - ajustes realizados
  - resultado sensorial / estabilidad

## Inputs mínimos que conviene registrar por lote
- Agua source (ID)
- Volúmenes: agua mash y agua sparge (L)
- Sales: qué y cuánto (g)
- Ácidos: qué y cuánto (mL o g)
- pH mash (medido) + temperatura
- pH sparge (si aplica)
- Notas (sensación de aspereza, redondez, etc.)
