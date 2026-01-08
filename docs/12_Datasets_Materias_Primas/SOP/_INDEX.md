# SOPs — Operación Excel-first

Punto de entrada a los 7 SOPs canónicos para operación cervecera. Estos procedimientos operan en Excel usando contratos de la Biblia (_schema). La Biblia no guarda datos reales; eso vive en Excel/App.

## Antes de Empezar
- Revisar contratos y convenciones: [Schema Index](../_schema/_INDEX.md)

## SOPs 1–7: Orden Recomendado
1. [01_Alta_de_Item.md](01_Alta_de_Item.md) — Cuándo usar: Dar de alta nuevos items/insumos (malta, lupulo, etc.). Input: familia/categoría.
2. [02_Alta_de_Receta.md](02_Alta_de_Receta.md) — Cuándo usar: Crear/formular recetas. Input: item_codes, specs objetivo.
3. [03_Crear_Lote_de_Produccion.md](03_Crear_Lote_de_Produccion.md) — Cuándo usar: Ejecutar receta en lote real. Input: recipe_code, batch_code.
4. [04_Compras_y_Alta_de_Stock.md](04_Compras_y_Alta_de_Stock.md) — Cuándo usar: Registrar compras y entradas a stock. Input: item_codes, purchase_code.
5. [05_Consumo_y_Movimientos_de_Stock.md](05_Consumo_y_Movimientos_de_Stock.md) — Cuándo usar: Descontar consumos de lote y ajustar stock. Input: batch_code, item_codes.
6. [06_Venta_y_Cobro.md](06_Venta_y_Cobro.md) — Cuándo usar: Registrar ventas y pagos. Input: product_codes, sale_code.
7. [07_Producto_Terminado_y_Envasado.md](07_Producto_Terminado_y_Envasado.md) — Cuándo usar: Convertir lote en PT y envasar. Input: batch_code, product_code.

## Notas
- Orden recomendado: 1→7 para flujo completo. Módulos independientes posibles (ej: solo SOP 1 y 4 para compras).
- IDs/codes: Respetar convenciones (_schema/ID_CONVENTION_V1.md).
- Excel-first: Usar codes en Excel; ULIDs al ingest.