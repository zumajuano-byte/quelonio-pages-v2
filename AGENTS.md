# AGENTS.md - quelonio-pages-v2

## Proposito del repo
Este repo mantiene la Biblia Quelonio como fuente de verdad editorial y operativa (MkDocs + auditorias), con foco en trazabilidad, consistencia y navegacion estable.

## Reglas de edicion
- Preservar estructura de carpetas, rutas y slugs de documentacion.
- No romper enlaces internos ni navegacion (`mkdocs.yml`).
- No duplicar contenido; preferir consolidar y enlazar.
- Respetar resultados y criterios de auditorias existentes.
- No commitear artifacts ni data temporal local.
- Hacer cambios minimos, deterministas y offline.

## Metodo PASO (resumen)
1. Definir alcance exacto del PASO (que si y que no).
2. Implementar solo lo pedido.
3. Validar con checks del PASO antes de cerrar.
4. Entregar evidencia clara (resumen + diff + estado de validacion).

## Flujo de trabajo con Codex/OpenCode
- Entregar siempre:
1. Resumen de cambios.
2. `git diff --name-only`.
3. Resultado de validaciones obligatorias (`PASS/FAIL`).
4. Confirmacion explicita: no commit/push.
- No hacer commit ni push salvo pedido explicito del usuario.

## Comandos rapidos (PowerShell)
### Activar venv
```powershell
.\.venv\Scripts\Activate.ps1
```

### Preflight repo/venv
```powershell
.\preflight_repo.ps1
```

### MkDocs serve
```powershell
mkdocs serve
```

### MkDocs build
```powershell
mkdocs build
```

### Scripts de auditoria/pruebas (ejemplos)
```powershell
python tools\test_step39.py
python tools\test_step38.py
```

## Checklist de inicio
- Confirmar que el directorio actual es `quelonio-pages-v2`.
- Ejecutar `./preflight_repo.ps1`.
- Confirmar venv local activa.
- Revisar alcance del PASO y restricciones.

## Checklist de cierre
- Ejecutar validaciones obligatorias del PASO.
- Verificar que no se rompa navegacion/enlaces.
- Entregar resumen + `git diff --name-only` + A/B.
- Confirmar sin commit/push.

## Nota VS Code
Si VS Code/Pylance muestra estado inconsistente tras cambios de estructura/imports, recargar ventana y/o reiniciar extensiones antes de diagnosticar errores.
