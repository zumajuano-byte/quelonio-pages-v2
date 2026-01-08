# PROYECTO_WEB_API — Quelonio SaaS (Web App + API + DB)

# ARCHIVED — referencia histórica (no activo)

Proyecto activo único: [PROYECTO_BIBLIA.md](../PROYECTO_BIBLIA.md)

---

**Última actualización:** 2025-12-29 (AR)
**Estado:** Sprint 1.5/2 — Vertical slice multi-tenant + Inventario/Ventas (API) operativo  
**Regla de trabajo:** micro-pasos (1 paso por vez). Si un paso requiere admin, se aclara explícitamente.

---

## 0) Objetivo

Construir un **MVP tipo SaaS** para operación cervecera:
- Recetas, lotes, stock, ventas, finanzas
- Base para incorporar un **asistente IA** que responda en base a la Biblia (Quelonio Pages)

Principio de producto:
- **Excel** = modelo / plantilla / análisis (import-export, simulaciones).
- **SaaS** = operación diaria / “source of truth” (multiusuario, trazabilidad, consistencia).

Arquitectura (MVP):
- **Next.js (App Router) + TypeScript**
- **PostgreSQL**
- **Prisma**
- Endpoints API dentro de Next (`app/api/*`)

---

## 1) Repos / Ubicaciones

- **Repo Web App:** `C:\Users\flore\Documents\quelonio-saas`
- **Repo Biblia / Docs (GitHub Pages):** `C:\Users\flore\Documents\quelonio-pages`
- Plantilla oficial: [SPEC v1.0](PLANTILLAS/SPEC_v1_0.md)

Este archivo vive en **quelonio-pages** para que el “asistente” y el “método” queden publicados y versionados.

---

## 2) Estado técnico actual (CHECKPOINT REAL)

### 2.1 Node / NPM
- Node: **v20.19.0**
- npm: **10.8.2**

### 2.2 Next.js
- Next: **16.1.0**
- Dev: `npm run dev` (usa `next dev --webpack`)
- URL: `http://localhost:3000`

Notas:
- Si reiniciás `npm run dev` y el puerto está ocupado, es porque **hay otro Next corriendo**.
- Si ves: `Unable to acquire lock ... .next\dev\lock`, terminá el proceso anterior (o cerrá la terminal que lo estaba ejecutando) y volvé a correr dev.

### 2.3 PostgreSQL (Local Windows)
- Servicio: `postgresql-x64-18` **Running**
- Puerto: `localhost:5432`
- Base: `quelonio_saas`
- Usuario app: `quelonio`
- Password: `1204` (temporal; cambiar más adelante)

### 2.4 Prisma
- `npx prisma validate` OK
- `npx prisma generate` OK
- Migraciones: OK (sin pendientes)
- Migración creada para Recipes: `prisma/migrations/20251222214518_add_recipe/`

Nota importante (scripts Node):
- En este setup Prisma usa **adapter PG**. Si hacés scripts con `new PrismaClient()` “pelado”, puede fallar.
- Recomendación: en scripts, **importar el prisma centralizado** desde `lib/prisma.ts` (el mismo que usa la app).

### 2.5 Multi-tenant (estado funcional)
Vertical slice multi-tenant operativo:
- Organizations + Memberships (relación usuario↔org)
- Tenant enforcement por Membership (no confiar solo en headers)
- Cookie de “active org” (`POST /api/active-org`) recomendada
- Fallback `X-Org-Id` para smoke tests

---

## 3) Decisiones / aprendizajes del Sprint (lo importante)

### 3.1 Tenant enforcement (paso clave)
Antes: “confiar” en `X-Org-Id` (header libre) = fácil de romper.

Ahora: **enforcement por Membership**:
- Valida que el “usuario dev actual” exista.
- Valida que ese usuario tenga **Membership** en la Organization activa.
- Resultado: separación real por tenant (base de un SaaS).

### 3.2 Org activa (cookie) vs header
Caminos (en orden recomendado):

1) **Cookie (recomendado)**: `POST /api/active-org` setea la org activa (persistida en cookie del navegador / session).
2) **Header (temporal)**: `X-Org-Id` se mantiene como fallback para smoke tests rápidos.

### 3.3 Variables de entorno (pitfall detectado)
- Si aparece error: `Dev user not found: <email>`
  - Revisar `.env` → `DEV_USER_EMAIL=...`
  - Debe coincidir con un `User.email` existente en DB.
  - Si bootstrap usa `owner@quelonio.local`, lo más seguro es:
    - `DEV_USER_EMAIL=owner@quelonio.local`

### 3.4 Política de stock “estricta” (decisión)
**Regla estricta MVP:** no permitir que **ningún movimiento que reste stock** deje stock negativo.
- Aplica a:
  - `OUT` (ventas, consumo, merma)
  - `ADJUST` negativo (correcciones hacia abajo)
- Permite:
  - `IN`
  - `ADJUST` positivo

Resultado:
- Evita stock negativo “silencioso”.
- Obliga a cargar primero el stock real (o un ajuste positivo) antes de vender/consumir.

---

## 4) Endpoints actuales (resumen)

Base: `http://localhost:3000`

### Health / debug
- `GET /api/health`
- `GET /api/debug/users`

### Bootstrap / orgs / memberships
- `POST /api/bootstrap` (idempotente por email)
- `GET /api/organizations`
- `POST /api/organizations`
- `GET /api/memberships`
- `GET /api/memberships?orgId=<ORG_ID>`

### Tenant context
- `POST /api/active-org` (set cookie org activa)

### Catálogo / inventario
- `GET /api/items` (incluye `stockQty` agregado)
- `POST /api/items` (idempotente por (orgId, name))
- `GET /api/stock-moves`
- `POST /api/stock-moves` (**strict no negativos**; idempotente por (orgId, clientRef))

### Ventas (modelo contable)
- `GET /api/invoices`
- `POST /api/invoices` (idempotente por (orgId, number))
- `POST /api/payments` (idempotente opcional por (orgId, clientRef); actualiza status invoice según balance)

### Ventas (operación “1-click”)
- `POST /api/sales`
  - Transacción: invoice + (payment opcional) + stock-moves OUT por línea
  - Idempotencia: por (orgId, number) (y clientRefs derivadas)
  - Strict: si no hay stock suficiente, falla sin crear invoice/pago/moves

### Reportes
- `GET /api/reports/sales-summary?from=YYYY-MM-DD&to=YYYY-MM-DD`
- `GET /api/reports/inventory-summary?from=YYYY-MM-DD&to=YYYY-MM-DD`

---

## 5) UI (Dev Console) — lo que existe hoy

Página: `GET /` (http://localhost:3000)

Incluye (mínimo para validar APIs):
- Selector de Organization activa (persistida en `localStorage`)
- Crear Organization
- Ejecutar Bootstrap y auto-seleccionar la org creada
- Recipes CRUD (scoping por org activa)

Nota: UI final de ventas/stock todavía no; se opera por API + scripts.

---

## 6) Smoke tests útiles (PowerShell)

### 6.1 Helpers (`scripts/dev.ps1`)
Este repo usa helpers tipo:
- `Set-Org`
- `QGet`, `QPost`, `QDel`
- `QSmoke`

Regla: si un test requiere cookie/session, usar `Set-Org` primero.

---

### 6.2 Stock strict (test rápido)
1) Consultar inventario:
```powershell
$repI = QGet "/api/reports/inventory-summary"
$repI.items | ? { $_.name -like "*APA*" } | ConvertTo-Json -Depth 10
Esperado:

Primera llamada: ok=true + invoice + payment + moves

Segunda llamada: idempotentHit=true (sin duplicar side-effects)

Caso stock insuficiente:

Debe devolver 400 con error="Insufficient stock" y detalle itemId/currentStock/attemptedOut/projectedStock

No debe crear invoice nueva (verificar count antes/después)

6.4 Concurrencia (nota práctica PowerShell)

ForEach-Object -Parallel requiere PowerShell 7+.

Start-Job no “hereda” funciones como QPost (a menos que lo incluyas explícitamente o serialices invocaciones).

Conclusión: el test “parallel” desde PS puede dar errores de tooling; para stress real:

usar un script Node (fetch) o herramienta como k6/hey,

o elevar PS a 7 y usar Invoke-RestMethod con manejo explícito de cookies.

7) Regla adicional: encoding UTF-8 (Next)

Se detectó un fallo de compilación:

stream did not contain valid UTF-8 leyendo app/api/.../route.ts

Lección:

Asegurar que los .ts/.tsx queden en UTF-8 (preferible UTF-8 sin BOM).

Si aparece el error: re-escribir el archivo como UTF-8 desde PowerShell o VS Code (Save with Encoding).

8) Mapa de producto (visión simple)

Orden lógico de módulos (uno alimenta al siguiente):

Recetas (spec) ✅

Lotes (producción real) ⏭️

Inventario (movimientos) ✅ (MVP strict)

Ventas + Cobros ✅ (API: invoices/payments + /api/sales)

Compras + Pagos ⏭️

Costos + Rentabilidad ⏭️

QA/QC ⏭️

Dashboard ⏭️

9) Próximo objetivo inmediato (Sprint 2)

Dashboard UI mínimo + “Venta rápida” desde UI consumiendo:

GET /api/reports/sales-summary

GET /api/reports/inventory-summary

POST /api/sales

Entregables mínimos:

Pantalla “Dashboard” (KPIs + top items/stock)

Form “Venta rápida” (selección item + qty + price + cobro)

Validaciones UX: cuando stock insuficiente, mostrar error claro

10) Método operativo (micro-pasos)

Regla: 1 comando / 1 cambio por vez.
Vos pegás output, yo doy el siguiente paso.

Cuando hay servidores corriendo:

Abrí otra terminal (VS Code: Terminal → New Terminal).

No hace falta cortar el server para ejecutar comandos.

11) Prompt de reinicio (para retomar en un chat nuevo)

Pegá esto tal cual:

PROMPT CHECKPOINT — Quelonio SaaS (Web/API)

Contexto:

Repo app: C:\Users\flore\Documents\quelonio-saas

Repo docs: C:\Users\flore\Documents\quelonio-pages

Stack: Next 16.1 + TS + Prisma + PostgreSQL local

Multi-tenant: Organizations + Memberships + Active-Org cookie

Inventario: items + stock-moves con política strict no-negativos

Ventas: invoices/payments + endpoint /api/sales (transacción + idempotencia por number)

Regla: micro-pasos (1 paso por vez)

Qué quiero ahora:

Dashboard UI mínimo + Venta rápida desde UI

Consumir GET /api/reports/sales-summary y GET /api/reports/inventory-summary

Vista dashboard (KPIs + stock)

Form venta rápida llamando POST /api/sales

Restricciones:

No avances con 10 pasos juntos.

Si un paso requiere Admin, avisar explícitamente.

Si hay que tocar archivos, decime ruta + contenido exacto.

## Entrada 2025-12-26 — Validación UI+Reports + Seed Data + Idempotencia

**Objetivo**
- Encender Dashboard con datos reales y validar idempotencia end-to-end.

**Acciones**
- Se creó org: `cmjitsnkd0000ognk0woc5sjc`
- Se creó item `APA Test` (`cmjnhq3ir0000wwnk3bu9qh0t`, category=BEER)
- Stock IN: `POST /api/stock-moves` (shape correcto: itemId/type/qty) con `clientRef=seed-in-001`, `qty=24` (OK)
- Venta: `POST /api/sales` con `number=INV-SEED-20251226-202219` (OK, invoice PAID)
- Repeat misma venta: `POST /api/sales` con mismo `number` devolvió `idempotentHit=true` (sin duplicar side-effects)

**Resultados**
- Reporte inventario: itemsCount=1, totalStockMoves=2, stock BEER=23, topConsumed=1 u.
- Reporte ventas: invoicesCount=1, openInvoicesCount=0.
- Idempotencia `/api/sales` confirmada en repetición (idempotentHit=true).

**Próximo paso**
- Dashboard: refresco automático post-venta + UI “Venta rápida” completa (UX: errores 400 con details, y banner idempotente).


## Entrada 2025-12-29 — POS operativo + venta real + redirect a Dashboard

Objetivo
- Completar el flujo “operación 1-click”: POS → POST /api/sales → impacto en KPIs del Dashboard.

Acciones
- Se corrigió el payload del POS para ventas: `lines[0].description` (requerido por el backend).
- Se validó venta real desde UI POS (precio unitario editable).
- Se implementó redirección automática: luego de “Venta OK…”, espera 1s y navega a `/dashboard`.
- Resultado visible: POS muestra “Venta OK: INV-POS-...”, redirige al Dashboard y los KPIs reflejan la operación.
