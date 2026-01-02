# Interacción Metabolismo ↔ Receta (Marco de decisión) — Parte 2 (V2)

Este documento conecta la bioquímica de levadura (Parte 2) con decisiones reales de diseño: **perfil de azúcares, OG, oxígeno, pitch rate, temperatura, nutrientes y timing**.  
No duplica teoría: usa como “motor” las reglas R-0097..R-0108 y baja a acciones.

---

## Objetivo operativo
Tomar decisiones que controlan:
- **Atenuación real** (seco vs lleno)
- **Perfil de subproductos** (ésteres / alcoholes superiores / limpieza)
- **Cinética** (arranque, duración, final)
- **Riesgo** (floculación temprana, defectos por estrés, variabilidad)

---

## Entradas mínimas (lo que tenés que definir antes)
1) **Perfil objetivo**
- Limpio / neutro (lager, ale limpia)
- Expresivo / frutado (NEIPA, ale inglesa, etc.)

2) **Mosto**
- OG objetivo
- Perfil de carbohidratos (simple vs complejo; dextrinas vs fermentables)
- Nutrientes esperados (si aplican) + minerales

3) **Restricciones operativas**
- Capacidad real de control de temperatura
- Método de oxigenación disponible
- Medición disponible (densidad, T°, pH, etc.)
- Si hay o no repitch / reutilización

---

## Perillas principales (orden de impacto)
### 1) Temperatura / perfil térmico
- Define velocidad y perfil de subproductos.
- Se usa como “perilla fina” de limpieza vs expresividad.

### 2) Pitch rate (densidad celular)
- Cambia cinética y balance de subproductos.
- Impacta previsibilidad y repetibilidad.

### 3) Oxígeno de arranque
- Afecta salud de membrana/esteroles y **tiende a bajar ésteres** (trade-off).
- Es ventana: arranque, no rutina tardía.

### 4) Perfil de azúcares del mosto
- No es solo OG: el tipo de azúcar cambia subproductos (p.ej. glucosa ↔ ésteres).
- Dextrinas ponen techo a la atenuación real.

### 5) Nutrientes/minerales (cuando corresponda)
- Soporte para vitalidad; no reemplaza control térmico/pitch/O₂.

### 6) Floculación (cepa + manejo)
- Si cae temprano: puede bajar atenuación y subir riesgo de defectos (diacetilo/ésteres).

---

## Matriz de decisión (acciones recomendadas)
### A) Objetivo: “LIMPIO / NEUTRO” (minimizar ésteres)
- Mantener control térmico estable (evitar picos)
- Pitch rate conservador (evitar sub/sobre-inoculación)
- Oxigenación de arranque consistente (documentada)
- Evitar cargas altas de azúcares simples si aparecen notas a solvente/fruta
- Asegurar finalización completa antes de crash (no cortar por claridad)

### B) Objetivo: “EXPRESIVO / FRUTADO” (ésteres deseados, sin solvente)
- Permitir un perfil térmico que empuje expresión sin descontrol (documentar)
- Ajustar pitch rate para no “aplanar” expresión
- Oxígeno: mínimo necesario para salud (evitar sobre-oxigenar si querés ésteres)
- Si usás azúcares simples: monitorear solvente y ajustar perillas (temp/pitch/O₂)
- Evitar estrés excesivo (estrés ≠ “expresividad”)

### C) Objetivo: “SECO / ALTA ATENUACIÓN”
- Elegir cepa (maltotriosa importa) + estrategia de mosto (menos dextrinas)
- Control térmico + pitch rate consistente para terminar bien
- Evitar floculación temprana (no clarificar/crashear antes de terminar)

### D) Objetivo: “CUERPO / FINAL LLENO”
- Diseñar mosto con dextrinas (receta/maceración) y no forzar levadura
- Elegir cepa con atenuación adecuada
- Controlar perillas para evitar solvente si hay más simples

---

## Diagnóstico rápido (síntoma → sospecha → primer control → acción)
### 1) DF más alta de lo esperado (“no bajó”)
- Sospecha: maltotriosa/cepa, floculación temprana, stress, pitch rate incorrecto
- Primero controlar: T° real, signo de caída de levadura, consistencia de inoculación
- Acción: ajustar perillas y evitar cortar temprano (crash/clarificación)

### 2) Notas a solvente / alcohol superior
- Sospecha: temperatura alta/picos, estrés, balance pitch/O₂
- Primero controlar: perfil térmico real + método de oxigenación
- Acción: estabilizar T°, corregir estrategia de oxígeno y pitch (sin sobrecorregir)

### 3) Exceso de frutado no deseado
- Sospecha: oxígeno insuficiente, glucosa alta, perillas fuera de rango
- Primero controlar: carga de simples + práctica de O₂ + T°
- Acción: re-calibrar (temp/pitch/O₂) para objetivo “limpio”

### 4) Fermentación “terminó rápido” pero quedó dulce / con defectos
- Sospecha: floculación temprana (cepa muy floculante o manejo)
- Primero controlar: sedimentación temprana + timing de cold crash
- Acción: asegurar terminación y limpieza antes de enfriar

---

## Registro mínimo (para repetir o corregir)
Registrar por lote (siempre):
- Cepa + lote + (si aplica) generación
- OG / DF / tiempo total
- T° real (promedio y picos)
- Oxígeno: método + “cuándo” + consistencia
- Pitch: método de medición (masa/volumen/estándar)
- Nutrientes: sí/no + criterio
- Observaciones sensoriales clave (ésteres/solvente/limpieza)

---

## Puentes internos (no duplicar)
- Parte 2 (bioquímica / reglas):
  - Estructura/membrana/esteroles → `10_Estructura_Celular.md`
  - Azúcares (maltotriosa/dextrinas) → `20_Metabolismo_de_Azucares.md`
  - Subproductos (ésteres) → `40_Esteres_y_Alcoholes_Superiores.md`
  - Floculación → `50_Floculacion_y_Sedimentacion.md`
- Hub operativo (Parte 3):
  - Checklist control fermentación → `../Levadura_Parte3_DEEP/60_Checklist_Control_Fermentacion.md`
  - TP Log → `../Levadura_Parte3_DEEP/TP_Log_Pitch_O2_Temp_Nutrientes.md`
- Fermentación DEEP (procedimiento):
  - O₂ + pitch → `../Fermentacion_DEEP/02_Oxigenacion_y_pitch_rate.md`
  - Curva térmica/diacetilo → `../Fermentacion_DEEP/03_Curva_termica_diacetilo_y_rampas.md`
  - Troubleshooting → `../Fermentacion_DEEP/07_Troubleshooting_sintomas_causas_acciones.md`
