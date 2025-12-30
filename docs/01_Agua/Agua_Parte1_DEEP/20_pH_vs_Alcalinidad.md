# pH vs Alcalinidad: el error más común

## 0) Idea central
El pH es una foto instantánea.  
La alcalinidad indica **cuánta fuerza hay que aplicar para cambiar ese pH**.

Dos aguas con el mismo pH pueden comportarse de manera opuesta en el mash.

---

## 1) pH no mide “estabilidad”
- El pH cambia fácil.
- La alcalinidad define la “resistencia” a ese cambio.

Regla:
> **El pH se mide. La alcalinidad se diseña.**

---

## 2) Alcalinidad (definición operativa)
La alcalinidad es la capacidad del agua de neutralizar ácidos.

En cervecería normalmente está dominada por:
- bicarbonatos (HCO₃⁻)

Se expresa usualmente como:
- ppm como CaCO₃

---

## 3) Implicancia práctica (qué pasa en el mash)
- pH del agua ≠ pH del mash
- Alcalinidad alta → mash resiste bajar pH → tendencia a mash alto
- Alcalinidad baja → mash responde rápido → tendencia a mash más bajo (si otros factores acompañan)

---

## 4) Alcalinidad residual (RA): el “puente” práctico
La RA es, a grandes rasgos, la parte de la alcalinidad que “queda” luego de considerar el efecto de calcio y magnesio.

Interpretación simple:
- RA positiva → empuja el pH del mash hacia arriba
- RA negativa → empuja el pH del mash hacia abajo

---

## 5) Qué hacer (procedimiento mínimo)
1) Conseguir reporte de agua (al menos: alcalinidad, Ca, Mg).
2) Definir objetivo de pH de mash (por estilo).
3) Ajustar con:
   - calcio (sales) para estructura
   - ácido (si la alcalinidad lo pide)
4) Validar midiendo pH real del mash (no solo calculando).
5) Registrar: agua + adiciones + pH real + resultado.

---

## 6) Señales típicas de problema
- Mash alto (ej. > 5.6) con cervezas pálidas → probablemente alcalinidad/RA demasiado alta o falta Ca/ácido.
- Astringencia / “té” al final del lavado → pH de runnings/lautering se fue arriba (ver módulo de Sparge en Partes siguientes).

## Reglas (B022) — pH vs Alcalinidad

<a id="r-0041"></a>
### R-0041 — El objetivo de control es el pH del mash, no el pH del agua
- FuenteID: B022
- Evidencia (B022 p42): "es el pH de la masa y no el pH del agua"
- Aplicación: No persigas un “pH perfecto” del agua. Diseñá el agua para que el pH del mash caiga en rango objetivo.
- Notas: Ver también: [pH en el mash](../Agua_Parte2_DEEP/50_pH_en_el_Mash.md)

<a id="r-0042"></a>
### R-0042 — Para entender el agua cervecera, la alcalinidad es más importante que el pH del agua
- FuenteID: B022
- Evidencia (B022 p70): "la alcalinidad del agua de infusión es más importante que su pH"
- Aplicación: Cuando haya conflicto o dudas, priorizá medir/estimar alcalinidad antes que interpretar pH del agua.
- Notas: La alcalinidad domina cómo “se defiende” el agua frente a ácidos.

<a id="r-0043"></a>
### R-0043 — La alcalinidad funciona como tampón: describe resistencia a cambios de pH
- FuenteID: B022
- Evidencia (B022 p70): "El tampón primaria en el agua potable es por lo general la alcalinidad."
- Aplicación: Usá alcalinidad como tu variable “de control” para predecir cuánto costará ajustar pH (con ácido o con sales).
- Notas: Ver también: [Sistema tampón carbonato](30_Sistema_Tampon_Carbonato.md)

<a id="r-0044"></a>
### R-0044 — Medir pH del agua sin contexto de tampones puede inducir a error
- FuenteID: B022
- Evidencia (B022 p70): "es como medir el voltaje de una batería desconocido."
- Aplicación: No tomes decisiones de ajuste solo porque el pH del agua “parece” alto o bajo.
- Notas: Si no tenés alcalinidad medida, tratala como “dato faltante” (no como suposición).

<a id="r-0045"></a>
### R-0045 — Regla por estilo/color: baja alcalinidad suele ser deseable en cervezas claras
- FuenteID: B022
- Evidencia (B022 p47): "baja alcalinidad es deseable para cervezas de color más claro"
- Aplicación: En rubias/claras (p. ej. lager clara, APA dorada), apuntá a alcalinidad baja para facilitar pH correcto y sabor limpio.
- Notas: Los valores concretos se documentan en: [Alcalinidad como CaCO3 y mEq](../Agua_Parte4_DEEP/130_Alcalinidad_Com_CaCO3_y_mEq.md)

<a id="r-0046"></a>
### R-0046 — Regla por estilo/color: aumenta la necesidad de alcalinidad con grists más oscuras/ácidas
- FuenteID: B022
- Evidencia (B022 p47): "la necesidad de alcalinidad aumenta para grists ... más oscuras"
- Aplicación: En cervezas oscuras o muy maltosas, considerá que necesitarás más alcalinidad para evitar pH de mash demasiado bajo.
- Notas: Esto no es “mejor o peor”; es un requerimiento funcional.

<a id="r-0047"></a>
### R-0047 — Decisión final: el sabor de la cerveza es el criterio guía
- FuenteID: B022
- Evidencia (B022 p47): "el sabor de la cerveza debe ser guía"
- Aplicación: Si números y teoría “cierran” pero la cerveza no, el sabor manda: revisá perfil de sales, alcalinidad, sulfato/cloruro, etc.
- Notas: Esta regla evita “optimizar” en papel y fallar en vaso.

<a id="r-0048"></a>
### R-0048 — “Alcalinidad < 50 ppm” es una generalidad histórica (no una ley universal)
- FuenteID: B022
- Evidencia (B022 p39): "La alcalinidad del agua debe ser inferior a 50 ppm."
- Aplicación: Usá esa guía como punto de partida para estilos tipo pils/lager clara, pero no la impongas a todos los estilos.
- Notas: El propio texto advierte que esas generalidades nacen de un contexto de estilos específicos.

<a id="r-0049"></a>
### R-0049 — La alcalinidad no es solo “un problema”: su nivel recomendado depende de la receta
- FuenteID: B022
- Evidencia (B022 p47): "puede variar en función de la acidez de la composición de puré"
- Aplicación: Tratá alcalinidad como variable de diseño: depende de malt bill, color, objetivo sensorial y proceso.
- Notas: Conecta directamente con formulación (malt bill) y pH del mash.

<a id="r-0050"></a>
### R-0050 — El análisis sensorial del agua puede ser una herramienta operativa real
- FuenteID: B022
- Evidencia (B022 p47): "El análisis sensorial ... de la calidad de su agua es una herramienta poderosa."
- Aplicación: Incorporá un “chequeo sensorial” del agua (olor/sabor) como rutina, sin reemplazar mediciones.
- Notas: Útil para detectar cambios de fuente, cloro/cloramina, o contaminación.

<a id="r-0051"></a>
### R-0051 — El pH del agua es una referencia, pero no una meta
- FuenteID: B022
- Evidencia (B022 p42): "el pH del agua no es la meta."
- Aplicación: Podés registrar pH del agua como dato histórico, pero el control real es: alcalinidad + pH mash.
- Notas: Evita “ajustar agua a ciegas”.

<a id="r-0052"></a>
### R-0052 — Objetivo práctico: diseñar condiciones para que el proceso ocurra “de la mejor manera”
- FuenteID: B022
- Evidencia (B022 p42): "proporcionar las condiciones bajo las cuales las operaciones ... se puede conducir de la mejor manera."
- Aplicación: La regla de oro es operacional: el agua se ajusta para mejorar maceración, fermentación, claridad y sabor, no por numerología.
- Notas: Esta regla conecta agua con todo el flujo (receta → producción → QA/QC).
