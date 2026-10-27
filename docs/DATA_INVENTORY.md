# Inventario de datos, minimización y retención

Sistema: Territorial Review DSS (Synthetic). Datos: `data/territorial_risk_synthetic.csv`, 640 filas y 9 columnas, generados con semilla fija. No contienen personas, lugares ni estadísticas oficiales reales. Este documento describe cómo se trataría un caso real y deja claro qué es una decisión de diseño.

## 1. Inventario

| Columna | Tipo | Qué es | Se usa como entrada | Clasificación | Justificación |
|---|---|---|---|---|---|
| case_id | texto | Identificador del caso (CASE-0001…) | No | Seudónimo interno | Solo trazabilidad; único en las 640 filas |
| received_date | fecha | Fecha de recepción (2026-01-01 a 2026-12-27) | No (solo para el corte temporal) | Operativo | Permite evaluar de forma temporal |
| zone | texto (4 valores) | Zona del caso | Sí | Territorial | Contexto del caso |
| protected_group | texto (G1, G2) | Grupo protegido | **No** | **Sensible** | Solo para auditar equidad |
| age_band | texto (4 valores) | Rango de edad | Sí | **Sensible** | Ver minimización |
| previous_incidents | entero (0–9) | Incidentes previos | Sí | Operativo | Señal de riesgo |
| infrastructure_score | decimal (0.03–0.98) | Índice de infraestructura | Sí | Operativo | Señal de riesgo |
| exposure | decimal (0–1) | Índice de exposición | Sí | Operativo | Señal de riesgo |
| target | 0/1 | Etiqueta de riesgo | No (es lo que se predice) | Operativo | Objetivo del modelo |

Identificadores directos prohibidos (`name`, `document_number`, `email`, `phone`): no existen en los datos y el contrato (`validate_schema`) los rechaza; la prueba `tests/test_privacy.py` lo verifica. Valores faltantes: 0.

## 2. Minimización

Principio: usar solo los datos necesarios para el propósito (priorizar casos para revisión humana).

- `protected_group` **no entra al modelo**. Se conserva únicamente para auditar. Esto reduce el riesgo, pero no elimina el sesgo indirecto: `infrastructure_score` y `exposure` promedian valores distintos entre G1 y G2 (0.566 vs 0.444 y 0.469 vs 0.559), por lo que pueden actuar como sustitutos.
- `age_band` es sensible. `scripts/minimization_check.py` entrena el mismo modelo con y sin esta columna. Resultado en `reports/lab13/minimization_check.csv`: exactitud 0.719 con ella y 0.725 sin ella; recall 0.717 en ambos casos; la brecha de recall queda en 0.138 en los dos. La brecha de FPR sube de 0.125 a 0.144 (sigue por debajo del límite de 0.16). **Quitarla no reduce el desempeño global, pero empeora un poco la brecha de FPR; por eso se propone y no se aplica sin revisión.**
- **Propuesta de minimización:** dejar de recolectar `age_band` y quitarla de `features()` en una versión futura, ya que no mejora el modelo. No se aplicó en este proyecto para no cambiar el modelo evaluado en LAB12 y LAB13; queda como acción pendiente de la Data Engineer (Responsible) y la Institutional Owner (Accountable). Mientras tanto, `age_band` sigue siendo necesaria para la auditoría interseccional de LAB12.
- Quitar columnas no corrige la brecha de recall entre grupos (con solo variables numéricas la brecha fue 0.161 en una prueba exploratoria), por lo que la mitigación se hace con monitoreo y revisión humana, no solo con minimización.

## 3. Retención

Los periodos siguientes son una **propuesta de diseño** para un caso real; no existe un mandato en los datos sintéticos y deben ser confirmados por la persona responsable.

| Dato o artefacto | Retención propuesta | Motivo | Responsable |
|---|---|---|---|
| Datos de casos (campos operativos) | Mientras dure la revisión del caso y la auditoría posterior | Necesarios para revisar y apelar | Data Engineer |
| `protected_group` y `age_band` | Solo el tiempo de auditoría; después, agregados | Datos sensibles: menor tiempo posible | Data Engineer |
| Reportes de auditoría y decisiones (`reports/`) | Conservar con la versión del modelo | Trazabilidad y rendición de cuentas | ML Engineer |
| Modelos entrenados | Conservar la versión vigente y la anterior (para rollback) | Retorno a un estado seguro | ML Engineer |
| Registros de incidentes y postmortem | Conservar junto con la evidencia | Aprendizaje y auditoría | Product Owner |

Borrado: al terminar el periodo, la Data Engineer elimina los datos individuales y deja solo agregados sin identificar a personas; la Institutional Owner confirma el cierre.
