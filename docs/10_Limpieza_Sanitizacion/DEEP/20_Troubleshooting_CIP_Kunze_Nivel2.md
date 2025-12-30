---
status: active
scope: limpieza_sanitizacion
type: troubleshooting
source_basis: "Kunze (CIP: secuencias + fallas típicas + diseño de circuito)"
---

# 20 — CIP Troubleshooting (Nivel 2, basado en Kunze)

## Objetivo (en simple)
Cuando “parece que limpiamos” pero igual aparecen olores raros, contaminación o suciedad repetida, este bloque te ayuda a:
- encontrar la causa más probable,
- corregir sin improvisar,
- y dejar registro para que no se repita.

---

## 1) La regla madre de CIP (4 perillas)
Un CIP funciona cuando controlás estas 4 cosas (si una falla, se vuelve azar):
1) **Tiempo** (no apurar)
2) **Temperatura** (si está fría, limpia peor)
3) **Concentración** (si está “a ojo”, cambia lote a lote)
4) **Caudal/acción** (si no “pega” y no arrastra, no limpia)

> Traducción práctica: si no medís al menos tiempo + temperatura + concentración, no sabés si el CIP salió bien.

---

## 2) Checklist rápido cuando “algo no cierra”
Antes de tocar químicos:
- [ ] ¿La secuencia fue siempre la misma? (pre-enjuague → cáustico → enjuague → ácido → enjuague → sanitización)
- [ ] ¿Se purgó el aire del circuito? (sin bolsas de aire)
- [ ] ¿Drenó bien todo al final? (sin “charcos” internos)
- [ ] ¿Hubo turbulencia/caudal real o fue un hilito?

Si cualquiera es “No”, ahí está tu primera corrección.

---

## 3) Tabla simple: síntoma → causa probable → acción
### A) “Sigue saliendo olor raro” (mangueras/válvulas/tanque)
Causas típicas:
- punto muerto (“zona trampa”) donde el CIP no circula bien
- válvula/acodado que retiene líquido
- manguera con interior dañado o con biofilm

Acción:
- desarmar el punto trampa (válvula, acople) y limpiar manual
- si se repite: marcar ese tramo como “zona crítica” y cambiar rutina (más frecuente) o rediseñar

---

### B) “Hay suciedad visible después del CIP”
Causas típicas:
- faltó acción (caudal bajo / no llega a la zona)
- tiempo corto
- concentración incorrecta

Acción:
- repetir ciclo, pero esta vez dejando fijo: tiempo + temperatura + concentración
- revisar cobertura (spray/retorno) y si hay “sombras” (zonas que nunca se mojan bien)

---

### C) “Espuma descontrolada / CIP inestable”
Causas típicas:
- entrada de aire (bolsas) o retorno mal diseñado
- caudal inadecuado
- químico mal preparado

Acción:
- purgar aire al inicio
- estabilizar caudal
- preparar químico con medición (no a ojo)

---

### D) “Limpia una vez, pero a los pocos usos vuelve el problema”
Causas típicas:
- no drena bien y queda humedad con restos
- se deja abierto y recontamina
- no hay rutina de desarme en puntos críticos

Acción:
- cerrar/tapar después de sanitizar
- definir frecuencia fija de desarme (válvulas, conexiones)
- registrar “qué punto” repite problemas (para atacar siempre el mismo lugar)

---

### E) “Problema de ‘piedra’ / depósitos minerales”
Causas típicas:
- falta ciclo ácido o frecuencia insuficiente
- agua dura / depósitos acumulados

Acción:
- incorporar ciclo ácido con frecuencia definida
- revisar agua y zonas de acumulación

---

## 4) Dónde se esconden los problemas (zonas trampa clásicas)
- válvulas (especialmente si no se desarman nunca)
- codos/acodados que retienen líquido
- tees y ramales “ciegos”
- conexiones rápidas con sellos gastados
- mangueras viejas (microfisuras internas)

> Regla simple: si se repite siempre en el mismo lugar, no es “mala suerte”: es diseño / rutina.

---

## 5) Gate de salida “CIP OK” (para no discutir)
Antes de declarar “listo para usar”, marcar:
- [ ] Visual OK (sin película/manchas)
- [ ] Olor OK (sin olor raro)
- [ ] Drenaje OK (no queda líquido atrapado)
- [ ] Circuito cerrado/tapado (no se recontamina)

Si algo falla, no se “compensa” con más sanitizante: se corrige limpieza/drenaje.

---

## 6) Qué registrar en el TP (para que el sistema aprenda)
En el TP_Log_Limpieza_y_CIP.md, agregar siempre:
- qué síntoma apareció (A/B/C/D/E)
- qué parte exacta del equipo era (válvula X, manguera Y, retorno Z)
- qué cambiaste (tiempo/temp/concentración/caudal/desarme)
- si se resolvió (Sí/No)

