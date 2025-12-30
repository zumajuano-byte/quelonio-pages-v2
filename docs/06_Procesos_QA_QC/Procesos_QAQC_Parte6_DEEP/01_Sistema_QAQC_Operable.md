# 01_Sistema_QAQC_Operable

---

## Ruta rápida (incidentes)
Si aparece un problema en producción (defecto, oxidación, contaminación, desvío, shelf-life raro):

➡️ [Centro de Incidentes (QA/QC)](../Centro_Incidentes.md)
➡️ Template: [TP — Liberación de Lote](TP_Liberacion_de_Lote.md)



## Principio de diseño
Un QA/QC útil no es “más tests”: es **tests elegidos por riesgo**, con **límites claros**, **acciones definidas**, y **evidencia trazable**.

### Mapa mínimo (en capas)
1) **Riesgo y diseño de controles**
   - FMEA (fallas del proceso) y/o HACCP (peligros de inocuidad).
   - Si no se hace formal: *mapear proceso + inputs/outputs + controles* y resumir en un **control plan**. fileciteturn23file0L27-L36

2) **Especificaciones y control limits**
   - Especificación: límites cuantificables alineados a requerimiento del cliente.
   - Control limit: límites estadísticos para detectar tendencia antes de violar especificación. fileciteturn23file1L14-L19

3) **Ejecución**
   - SOPs por operación (brew, packaging, utilities, lab).
   - Registros: lote, equipo, fecha/hora, operador, resultado, acción.
   - Entrenamiento (consistencia entre operadores).

4) **Verificación**
   - Auditorías (internas/terceros) y revisión de eficacia.
   - Calibración/ mantenimiento de equipos de medición (inline y offline). fileciteturn23file4L34-L43

5) **Respuesta**
   - Definir exactamente qué hacer cuando un límite o especificación se rompe.
   - CAPA, hold/release, segregación, re-trabajo/blending si aplica.

## Resultado esperado (salida del módulo)
- Un **Control Plan** por estilo/familia de producto y por línea de empaque.
- Un **Programa de auditorías anual** (por proceso / por área / por producto).
- Un **árbol de decisión** de contaminación + plan de muestreo.

Links:
- [04_Control_Plan_Template](04_Control_Plan_Template.md)
- [03_Auditorias_QMS](03_Auditorias_QMS.md)
- [11_CAPA_y_Gestion_de_Desvios](11_CAPA_y_Gestion_de_Desvios.md)

