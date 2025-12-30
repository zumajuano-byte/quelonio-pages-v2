---
status: active
scope: empaque_estabilidad
type: troubleshooting
sources:
  - "Palmer — How to Brew (oxidación/cartón; almacenamiento; estabilidad; vida útil depende del envasado)"
  - "White & Zainasheff — Yeast (fallas de carbonatación; sobrecarbonatación por contaminación; sanitización)"
---

# 40 — Shelf-life y troubleshooting de empaque (síntomas → causas → acciones)

## Objetivo (en simple)
Cerrar el loop de estabilidad:
- detectar temprano degradación,
- identificar causa probable (empaque vs almacenamiento vs micro),
- ejecutar acciones correctivas,
- y registrar para mejorar el proceso.

---

## Navegación rápida
- Entrada a empaque (si venís desde 07): [05 — Preparación para envasar](05_Preparacion_para_envasar.md)
- Control de oxígeno (DO/TPO): [20 — Control de oxígeno](20_Control_oxigeno_DO_TPO.md)
- Almacenamiento: [30 — Luz/temperatura/almacenamiento](30_Luz_temperatura_almacenamiento.md)
- Registro: [TP — Log de envasado y estabilidad](TP_Log_Envasado_y_Estabilidad.md)
- Final de Fermentación (previo a empaque): [07/30 — Transferencias y salida](../../07_Fermentacion_Maduracion/DEEP/30_Transferencias_cold_crash_y_salida.md)

---

## 1) Gates de estabilidad (mínimos)
### Gate A — Al cierre del envasado (día 0)
- [ ] Transferencia/purga ejecutada (ver Bloque 20)
- [ ] Headspace controlado
- [ ] Sin paradas largas con envase abierto
- [ ] Incidentes registrados (paradas, desconexiones, salpicado, etc.)

### Gate B — 7 días
- [ ] Chequeo sensorial rápido (aroma “apagado”, papel/cartón, azufre raro, solvente)
- [ ] Chequeo de carbonatación (según envase)

### Gate C — 14–30 días
- [ ] Evaluación real por estilo (especial foco en cervezas lupuladas)

---

## 2) Matriz rápida: síntoma → causa probable → chequeo → acción
> Usá esto como “primera respuesta” antes de discutir teorías.

| Síntoma (qué ves) | Causa probable (orden típico) | Chequeo simple | Acción inmediata | Prevención |
|---|---|---|---|---|
| Papel/cartón / envejecimiento acelerado | Oxígeno en empaque / transferencia / headspace + almacenamiento caliente | Revisar log: purga, paradas, demoras, headspace; revisar cómo se llenó/cerró | Detener y auditar SOP de purgas/transferencias; reducir tiempos entre llenado y cierre | Estandarizar Bloque 20 + mejorar estándar de almacenamiento (Bloque 30) |
| Aroma “apagado” rápido (hoppy) | Oxígeno + temperatura de guarda alta/fluctuante | Comparar 7 días vs 14 días; revisar frío de guarda | Reforzar circuito cerrado y purgas; enfriar guarda/logística | DO/TPO (si medís) o proxies + frío estable |
| Falta de carbonatación (botella) | Priming mal calculado / temp de acondicionamiento baja / levadura débil / sanitizante mal usado | Revisar temp real + días; revisar cálculo priming | Subir/estabilizar temp y esperar; revisar método priming | Estandarizar priming (Bloque 10) + sanitización medida |
| Sobrecabonatación / “botellas explosivas” | Exceso de azúcar / cerveza no atenuada / contaminación | Revisar densidad final y gate 07; revisar signos de contaminación | Aislar lote, enfriar, evaluar retiro; activar QA/QC | Gate estricto 07 + higiene/CIP + control de azúcar |
| Haze en frío / estabilidad visual errática | Chill haze (proteínas/polifenoles) + proceso de frío/clarificación | Comparar frío vs ambiente; ver evolución 7–30 días | Definir si es aceptable por estilo; ajustar frío/clarificación | Objetivo por estilo + disciplina de proceso (07) |

---

## 3) Casos detallados (por si necesitás bajar a tierra)
### 3.1 Oxidación / “papel-cartón”
**Qué significa:** oxidación; depende mucho de cómo se envasó y cómo se almacenó.  
**Causas típicas:** purga insuficiente, transferencia con aire, headspace alto, envase abierto mucho tiempo, almacenamiento caliente/ciclos térmicos.  
**Acciones:** auditar Bloque 20 + ajustar logística/guarda (Bloque 30).  

### 3.2 Aroma “apagado” (lupuladas)
**Causas típicas:** oxígeno + temperatura de guarda inadecuada.  
**Acción:** reforzar Bloque 20 y fijar estándar de almacenamiento por familia de cerveza.

### 3.3 Falta de carbonatación (botella)
Verificar: cálculo de priming, temperatura real de acondicionamiento, tiempo, salud de levadura y sanitización.  
➡️ Ver: [10 — Priming y carbonatación en botella](10_Priming_y_carbonatacion_en_botella.md)

### 3.4 Sobrecabonatación / “explosivas”
Causas típicas: exceso de azúcar, no terminó de fermentar, o contaminación.  
Acción: aislar lote y activar protocolo QA/QC (no seguir “como si nada”).

### 3.5 Chill haze / estabilidad visual
No siempre es “defecto” (depende del estilo), pero suele correlacionar con estabilidad más corta.  
Acción: definir objetivo por estilo y ajustar frío/clarificación si corresponde.

---

## 4) Registro mínimo (obligatorio)
Por corrida de envasado:
- fecha/hora, lote, tipo de envase
- método de purga/transferencia (sí/no + cómo)
- incidentes (paradas, desconexiones, envase abierto, salpicado)
- condición de almacenamiento (ambiente/frío) + temperatura
- checkpoints sensoriales: 7/14/30/60 días
- carbonatación (si aplica)

➡️ [TP — Log de envasado y estabilidad](TP_Log_Envasado_y_Estabilidad.md)
