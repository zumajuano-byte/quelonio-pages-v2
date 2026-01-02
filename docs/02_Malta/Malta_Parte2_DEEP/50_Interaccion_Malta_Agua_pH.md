# Interacción Malta–Agua–pH

## 1) El pH “sale” de dos fuerzas, no de una
En mash, el pH se define por:
1) la capacidad tampón del sistema (malta + fosfatos + bicarbonatos del agua)
2) reacciones y compuestos que aportan acidez/buffer

Tu propio módulo de agua ya fija el rango operativo típico: el mash ocurre comúnmente entre pH 5,2–5,6.

## 2) Acidez de malta: base vs especiales
Para mash con 100% malta base, una explicación citada es que la caída de pH se asocia principalmente a reacciones de calcio tipo fosfato; y que la acidez por Maillard sería pequeña en comparación.

Cuando suben maltas especiales, el mismo texto indica que melanoidinas y ácidos orgánicos pasan a ser un factor significativo.

## 3) Datos útiles: el pH varía por tipo de malta
El material compila valores de “congress mash pH” que cambian según el tipo de malta (base vs melanoidin/caramelo/roasted). 
Esto respalda una regla simple: **no existe “un pH de mash” independiente del grist.**

## 4) Implicancia práctica: ajustá con evidencia
El mismo material recomienda que, en la práctica, muchas veces es más razonable hacer un “puré de prueba” a escala reducida, medir pH y ajustar desde ahí.

## 5) Sparge y riesgo de “subir pH”
Hay una advertencia operacional: en sparge, cortar o corregir si el pH se acerca a 5,8 para evitar defectos; la mejor solución propuesta es acidificar el agua de rociado para mantener el pH del lecho por debajo de ese umbral.

## 6) Puentes recomendados
- Agua Parte 2: pH en el mash y sensibilidad (para decidir con sulfatos/cloruros).
- QA/QC Parte 2: control de pH y lógica de mash (para llevarlo a CCP/control plan).

Siguiente: [Errores comunes y tradeoffs](60_Errores_Comunes_y_Tradeoffs.md)

# Puente operativo (V2)

## Propósito
Conectar el **motor bioquímico de Malta** (modificación/enzimas/DP/fermentabilidad) con el **control de pH** del mash (Agua), sin duplicar contenido ni inventar evidencia.

## Decisiones que habilita (en práctica)
- Ajustar el pH del mash para operar el sistema enzimático (perfil de azúcares → cuerpo/sequedad).
- Diagnosticar desvíos de conversión/eficiencia distinguiendo: **molienda / COA / enzimas / pH**.

## Qué medir (mínimo)
- pH del mash (medición real, no estimada).
- Temperatura al medir (registrar).
- Si hay corrección: tipo de corrección y dosis.

## Ruta de diagnóstico (orden recomendado)
1) **Medición pH**: confirmar lectura (instrumento calibrado).
2) **COA / lote**: comparar lote actual vs anterior (extracto, DP, proteína, etc.).
3) **Molienda**: revisar síntomas de over/under milling.
4) **Sistema enzimático**: revisar DP/enzimas como capacidad de conversión del grist.
5) Recién después: cambios de receta.

## Puentes internos (no duplicar)
- Agua (pH objetivo y control): `01_Agua/...` (ver reglas del módulo Agua).
- Malta Parte 2 (enzimas/DP/fermentabilidad): `Malta_Parte2_DEEP/20_Enzimas_Amilasas_y_Proteasas.md` y `Malta_Parte2_DEEP/30_Diastatic_Power_y_Limites.md`
- COA (predicción de performance): `Malta_Parte1_DEEP/40_COA_y_Control_de_Calidad.md`

## Checklist mínimo (registro)
- [ ] pH mash medido y registrado
- [ ] lote/proveedor de malta registrado + COA guardado
- [ ] setting de molienda documentado
- [ ] síntoma observado (conversión, eficiencia, filtración, cuerpo/sequedad)
- [ ] acción tomada (si hubo) + resultado

## Notas de evidencia
- Este archivo es un **puente**: las reglas de pH viven en Agua (B022) y las reglas de malta (B004) viven en sus archivos dueños.
