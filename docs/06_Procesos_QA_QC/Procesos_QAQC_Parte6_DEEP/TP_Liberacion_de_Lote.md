# TP — Liberación de Lote (QA/QC + Sensorial + Empaque)

> Objetivo: tomar una decisión final consistente (liberar / retener / reprocesar).
> Regla: si algo no aplica, marcar **N/A**.

---

## 1) Identidad del lote
- Producto / Estilo:
- Spec (vX.Y):
- Lote ID:
- Fecha de envasado:
- Responsable:
- Tipo de envase: lata / botella / keg
- Canal destino: venta directa / distribución / guarda / otro

---

## 2) Gate A — Proceso (mínimos cumplidos)
- FG estable (2 lecturas): Sí / No / N/A
- Diacetilo resuelto (si aplica): Sí / No / N/A
- Limpieza/CIP registrado (si aplica): Sí / No / N/A
- Incidentes mayores registrados: Sí / No
  - Si Sí: link al TP Desvío/CAPA:
    - [TP — Registro Desvío + CAPA](TP_Registro_Desvio_CAPA.md)

---

## 3) Gate B — Empaque (mínimos)
- Envasado sin incidentes críticos: Sí / No
- Trazabilidad completa (lote/fecha): Sí / No
- Manejo anti-oxígeno aplicado (purga/llenado/cierre): Sí / No / N/A

Puentes (si hay dudas):
- [09 — Control de oxígeno (DO/TPO)](../../09_Empaque_Estabilidad/DEEP/20_Control_oxigeno_DO_TPO.md)
- [09 — Troubleshooting empaque](../../09_Empaque_Estabilidad/DEEP/40_Shelflife_y_troubleshooting_empaque.md)
- [09 — TP Log Envasado](../../09_Empaque_Estabilidad/DEEP/TP_Log_Envasado_y_Estabilidad.md)

---

## 4) Gate C — Sensorial (Día 0)
> No es “cata perfecta”: es “sin defecto dominante fuera de estilo”.

- Cata Día 0 realizada: Sí / No
- Resultado: OK / Dudoso / No OK

Link:
- [11 — TP Log de Cata](../../11_Sensorial/DEEP/TP_Log_Cata_y_Defectos.md)

Notas sensoriales (1–3 líneas):
- 

---

## 5) Retención mínima (si aplica)
- Set de retención guardado: Sí / No / N/A
- Condiciones:
  - Frío: Sí / No / N/A
  - Ambiente: Sí / No / N/A

Próximo punto de control:
- Día 7 / Día 14 / Día 30 / N/A

---

## 6) Decisión final (Gate D)
Marcar 1:
- [ ] Liberar
- [ ] Retener (revisar en X días)
- [ ] Reprocesar
- [ ] Descartar

Motivo (1 frase):
- 

Acción siguiente:
- 

---

## 7) Si NO se libera: ruta rápida
➡️ [Centro de Incidentes (QA/QC)](../Centro_Incidentes.md)

Si el problema es “perfil no llega al spec” (no defecto):
➡️ [11 — Pasar sensorial a Spec/Receta](../../11_Sensorial/DEEP/20_Pasar_Sensorial_a_Spec_y_Receta.md)  
➡️ [08 — Ticket de mejora](../../08_Recetas_Formulacion/DEEP/TP_Ticket_Mejora_Receta_Spec.md)
