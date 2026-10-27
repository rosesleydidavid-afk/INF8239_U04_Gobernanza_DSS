# Traspaso entre roles (handoff)

Complementa `student_inputs/raci.csv`. Cada traspaso indica qué se entrega, quién lo recibe y qué debe verificarse antes de aceptarlo. Si la verificación falla, el artefacto vuelve al rol que lo entrega.

| # | De (R) | A | Artefacto que se entrega | Verificación para aceptar |
|---|---|---|---|---|
| 1 | Data Engineer | Data Scientist | Datos validados y `docs/DATASET_CARD.md` | `uv run python scripts/check_environment.py` indica `dataset_status: valid`; pruebas de datos y privacidad en verde |
| 2 | Data Scientist | ML Engineer | Modelo elegido, auditoría por grupo e intervalos (`reports/lab12/`) | Recall global ≥ 0.68; brechas ≤ 0.16; filas con menos de 10 casos no interpretadas |
| 3 | ML Engineer | Product Owner | `reports/lab13/deployment_decision.json` y app Streamlit | Estado GO o REVIEW con las compuertas listadas; `uv run pytest -q` en verde |
| 4 | Product Owner | Institutional Owner | `docs/MODEL_CARD.md`, `docs/RUNBOOK.md` y la decisión propuesta | Documentos sin `REPLACE`; decisión final registrada (GO limitado) |
| 5 | ML Engineer | Institutional Owner | Alerta o incidente con evidencia preservada | Evidencia guardada antes de cambiar nada; estado REVIEW o STOP definido |
| 6 | Product Owner | Representantes de personas afectadas | Comunicación y vía de apelación | Lenguaje claro, sin datos personales; revisión humana ofrecida |

Autoridad de decisión: solo la Institutional Owner puede aprobar el despliegue o suspender el sistema (única Accountable en despliegue limitado e incidentes). El Product Owner es Accountable de calidad de datos, validación, despliegue y monitoreo.
