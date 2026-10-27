# Dataset Card

Synthetic territorial-risk dataset generated with a fixed educational seed. It contains no real persons, locations, rates or official Dominican Republic statistics. Intended only to practice contracts, temporal evaluation, subgroup auditing and governance. Prohibited: operational profiling or inference about real populations.

## Composition
- Archivo: `data/territorial_risk_synthetic.csv`; 640 filas, 9 columnas; `case_id` único; sin valores faltantes.
- Variable objetivo `target` (0/1): 55.2% de casos positivos en el total; 57.5% en el conjunto de prueba.
- Grupos para auditoría (`protected_group`): en prueba, G1 = 101 casos y G2 = 59.
- Columnas y clasificación: ver `docs/DATA_INVENTORY.md`.

## Collection and provenance
Generado de forma sintética con semilla fija para la unidad U04 (INF-8239). Procedencia: proyecto base del curso (Edwin Ramón José Nolasco, UASD). No hay recolección de personas reales.

## Splits
División temporal por `received_date`: 480 filas para entrenar (2026-01-01 a 2026-09-24) y 160 para evaluar (2026-09-25 a 2026-12-27). Las fechas son sintéticas.

## Contract and checks
`validate_schema` exige las 9 columnas, un `target` binario y rechaza identificadores directos (`name`, `document_number`, `email`, `phone`). Pruebas: `tests/test_data.py` y `tests/test_privacy.py`.

## Known limits
- Es un conjunto pequeño y artificial: los resultados no se generalizan a casos reales.
- Los grupos G1 y G2 tienen tamaños distintos (101 y 59 en prueba), así que los intervalos de confianza de G2 son más amplios.
- Los procesos que generaron los datos no se documentan más allá de la semilla; no se pueden inferir causas.

## Uses
Permitido: práctica de contratos de datos, evaluación temporal, auditoría por grupos y gobernanza. Prohibido: perfilamiento operativo o inferencias sobre poblaciones reales.

## Maintenance and owner
Responsable: Data Engineer (Responsible) e Institutional Owner (Accountable), según `student_inputs/raci.csv`. Revisión junto con el Model Card (próxima: 2027-01-25).
