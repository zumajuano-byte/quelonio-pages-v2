---
status: stable
operational_level: P0
last_reviewed: 2025-12-22
owner: Juan
---

# Asistente v1 (MVP Manual)

Este hub define el comportamiento del Asistente v1 y centraliza los links canónicos.

## Qué hace (IN)
- Responde sobre cerveza (recetas, proceso, QA/QC, empaque/estabilidad) usando la Biblia.
- Guía el uso del sistema Brew OS (sin ejecutar acciones).
- Entrega salidas estandarizadas (SPEC / Checklist-Gates / Plan / Troubleshooting).

## Qué NO hace (OUT)
- No crea/edita datos en tu sistema (modo guía).
- No inventa números: si falta un dato crítico, lo solicita; si usa DEFAULT, lo marca como DEFAULT.

## Documentos canónicos
- Contratos de salida: [ASISTENTE_CONTRATOS](ASISTENTE_CONTRATOS.md)
- Contrato de datos: [ASISTENTE_DATA_CONTRACT](ASISTENTE_DATA_CONTRACT.md)
- Mapa de conocimiento: [ASISTENTE_KNOWLEDGE_MAP](ASISTENTE_KNOWLEDGE_MAP.md)

## Docs P0 (datos duros preferidos)
- Targets por estilo: [TABLAS_TARGETS_POR_ESTILO](TABLAS_TARGETS_POR_ESTILO.md)
- Agua: [AGUA_CALCULOS_Y_LIMITES](../01_Agua/DEEP/AGUA_CALCULOS_Y_LIMITES.md)
- Levadura: [PITCH_RATE_Y_OXIGENACION](../03_Levadura/Fermentacion_DEEP/PITCH_RATE_Y_OXIGENACION.md)
- Empaque: [DO_TPO_OBJETIVOS_Y_METODO](../09_Empaque_Estabilidad/DEEP/DO_TPO_OBJETIVOS_Y_METODO.md)
- Empaque: [CO2_CARBONATACION_TABLAS](../09_Empaque_Estabilidad/DEEP/CO2_CARBONATACION_TABLAS.md)
- Estabilidad: [SHELF_LIFE_PLAN_Y_CRITERIOS](../09_Empaque_Estabilidad/DEEP/SHELF_LIFE_PLAN_Y_CRITERIOS.md)

## Templates (salidas estandarizadas)
- SPEC v1.0: [TEMPLATE_SPEC_V1](TEMPLATE_SPEC_V1.md)
- Checklist/Gates: [TEMPLATE_CHECKLIST_GATES_V1](TEMPLATE_CHECKLIST_GATES_V1.md)
- Plan producción: [TEMPLATE_PLAN_PRODUCCION_V1](TEMPLATE_PLAN_PRODUCCION_V1.md)
- Troubleshooting: [TEMPLATE_TROUBLESHOOTING_V1](TEMPLATE_TROUBLESHOOTING_V1.md)

## 3 comandos de uso (copy/paste)
1) **SPEC**
   - “Generá un SPEC v1.0 para una IPA Hazy de 20 L, objetivo 6.5% ABV, perfil jugoso.”
2) **CHECKLIST**
   - “Dame un Checklist/Gates para empaque en lata de cerveza muy lupulada (prioridad O2).”
3) **TROUBLE**
   - “TROUBLE: a los 10 días la IPA pierde aroma y aparece cartón leve. Diagnóstico + plan.”

## Regla de salida (mínima)
- Siempre incluir al final: **Inputs usados** y **Datos faltantes**.


- Glosario operativo: [GLOSARIO_OPERATIVO](GLOSARIO_OPERATIVO.md)
- Matriz de afirmaciones P0: [MATRIZ_AFIRMACIONES_P0](MATRIZ_AFIRMACIONES_P0.md)
