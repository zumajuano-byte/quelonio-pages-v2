# 20 - Control de oxigeno en empaque: DO/TPO, purgas y transferencias (DEEP)

## Objetivo (en simple)
Reducir al minimo el ingreso de oxigeno desde "Listo para Empaque" hasta el cierre final del envase.

Por que importa: en esta etapa el oxigeno acorta vida util y "apaga" la cerveza (aroma mas bajo, envejecimiento acelerado).

## Navegacion rapida (para trabajar en orden)
- Entrada desde 07: 05_Preparacion_para_envasar.md
- Volver al final de 07 (antes de envasar): ../../07_Fermentacion_Maduracion/DEEP/30_Transferencias_cold_crash_y_salida.md
- Registro de corrida: TP_Log_Envasado_y_Estabilidad.md

## 1) Definiciones operativas (sin vueltas)
- DO (Dissolved Oxygen): oxigeno disuelto en la cerveza.
- TPO (Total Package Oxygen): oxigeno total en el envase (lo disuelto + lo del headspace).

Nota practica: aunque no midas DO/TPO, podes controlarlo con procedimiento:
purga + circuito cerrado + cero salpicado + envase abierto el menor tiempo posible.

## 2) Donde entra oxigeno (mapa de riesgo)
Orden tipico de riesgo (alto -> bajo):
1) Transferencias con aire (manguera sin purgar, caida libre, salpicado, espuma por turbulencia)
2) Headspace sin purgar (keg/botella/lata con aire adentro)
3) Paradas/demoras con envase abierto (llenaste y tardaste en cerrar)
4) Microfugas en conexiones/juntas/valvulas (entra poco, pero durante mucho tiempo)

## 3) Gate previo (condicion para habilitar empaque)
No se habilita empaque si:
- no esta cerrado el final del proceso (densidad estable + diacetilo resuelto), o
- no podes ejecutar transferencia sin aire (sin purga / sin circuito cerrado / con salpicado).

## 4) Estandar de transferencia cerrada (lo minimo obligatorio)
Regla simple:
la cerveza se mueve en circuito cerrado o purgado, sin caida libre y sin salpicado.

Procedimiento minimo:
1) Preparar linea/manguera sanitizada.
2) Purgar la linea con CO2 (objetivo: que NO quede aire).
3) Purgar el recipiente destino (keg/bright/llenadora) con CO2.
4) Transferir con presion controlada (sin turbulencia innecesaria).
5) Mantener headspace minimo y/o "manta" de CO2 donde aplique.

## 5) Purgas por tipo de empaque (estandar simple)

### 5.1 Keg
- Purgar el keg antes de llenar.
- Mantener CO2 en cabeza y cerrar sin "aspirar" aire.
- Registrar metodo (y ciclos si aplica).

Checklist rapido:
- [ ] Keg purgado
- [ ] Linea purgada
- [ ] Sin espuma excesiva durante llenado
- [ ] Cierre rapido

### 5.2 Botella
- Minimizar salpicado durante llenado.
- Controlar headspace (no dejar "aire de mas").
- Si purgas con CO2, estandarizar metodo (tiempo/boquilla) y registrarlo.

Checklist rapido:
- [ ] Llenado suave (sin turbulencia)
- [ ] Headspace controlado
- [ ] Cierre sin demoras

### 5.3 Lata
- Purgar envase y/o linea segun tu equipo.
- Minimizar el tiempo entre llenado y cierre.
- Evitar demoras con lata abierta.

Checklist rapido:
- [ ] Envase/linea purgados
- [ ] Cierre inmediato
- [ ] Sin paradas largas con envase abierto

## 6) Monitoreo (si medis) y proxies (si no medis)

### Si medis DO/TPO
Usa mediciones para aprender y corregir: comparar corridas, detectar donde sube y fijar estandar.

### Si NO medis DO/TPO
Usa estos SI/NO y registralos:
- purga de linea ejecutada (si/no)
- purga de envase ejecutada (si/no)
- transferencia sin caida libre (si/no)
- sin salpicado/turbulencia (si/no)
- envase abierto el menor tiempo posible (si/no)
- sensorial: aparece carton/papel temprano (si/no)

## 7) Registro minimo (para que el sistema aprenda)
Por lote y por corrida:
- temperatura de cerveza al envasar
- metodo de transferencia (cerrada / semi / abierta)
- metodo de purga (linea y envase)
- incidentes (paradas, demoras, desconexion, salpicado)
- resultado sensorial a 7 / 14 / 30 dias (nota corta)

Ver log: TP_Log_Envasado_y_Estabilidad.md

## 8) Troubleshooting rapido (oxigeno)

### Sintomas tipicos
- aroma apagado rapido (especialmente en lupuladas)
- carton/papel (envejecimiento)
- vida util corta

### Causas probables
- purga insuficiente (linea o envase)
- headspace alto
- salpicado / turbulencia / espuma excesiva
- paradas prolongadas con envase abierto
- microfugas (conexiones/juntas)

### Acciones
- Pausar corrida y re-purgar linea y envases.
- Volver al estandar de transferencia cerrada (no seguir "a medias").
- Registrar incidente y ajustar el SOP.

## BIBLIO (canonico) - plantilla minima
Regla: registrar edicion y ubicacion (capitulo/seccion/pagina).

### Fuente (1)
- source_id: BIB-09-O2-001
- Obra: How to Brew
- Autor: John Palmer
- Edicion / Ano / Editorial: [COMPLETAR]
- Capitulo / Seccion: [COMPLETAR]
- Pagina(s): [COMPLETAR]
- Nota breve: oxigeno en etapas finales/envasado como driver de vida util y "apagado" aromatico.

### Fuente (2)
- source_id: BIB-09-O2-002
- Obra: Yeast: The Practical Guide to Beer Fermentation
- Autores: Chris White; Jamil Zainasheff
- Edicion / Ano / Editorial: [COMPLETAR]
- Capitulo / Seccion: [COMPLETAR]
- Pagina(s): [COMPLETAR]
- Nota breve: riesgo de oxigeno en transferencias y efectos cuando ya hay poca levadura disponible.

### Matriz de afirmaciones (3-5)
- A1 (Oxigeno final = vida util):
  - Evidencia: BIB-09-O2-001 -> cap/seccion/pag [COMPLETAR]
  - Impacto: prioridad operacional en purgas/cierre rapido.
- A2 (TPO importa aunque no midas):
  - Evidencia: BIB-09-O2-001 -> cap/seccion/pag [COMPLETAR]
  - Impacto: estandares por tipo de envase.
- A3 (Transferencia cerrada reduce DO):
  - Evidencia: BIB-09-O2-002 -> cap/seccion/pag [COMPLETAR]
  - Impacto: gate "no envasar si no puedo transferir sin aire".
- A4 (Demoras con envase abierto elevan riesgo):
  - Evidencia: BIB-09-O2-001 -> cap/seccion/pag [COMPLETAR]
  - Impacto: regla "cerrar inmediatamente" y evitar paradas.
- A5 (Microfugas degradan a lo largo del tiempo):
  - Evidencia: BIB-09-O2-001 y/o BIB-09-O2-002 -> cap/seccion/pag [COMPLETAR]
  - Impacto: checklist de juntas/valvulas + registro de incidentes.

## Referencias (nota)
- Palmer: el oxigeno en etapas finales/envasado es critico para vida util.
- Yeast: el oxigeno en transferencias es un riesgo clave en el cierre del proceso.
