# Plan de monitoreo

Las señales y los umbrales provienen de `configs/governance.yml`. Las frecuencias son una propuesta de diseño para un caso real.

| Señal | Cómo se mide | Umbral | Frecuencia propuesta | Responsable | Acción si falla |
|---|---|---|---|---|---|
| Recall global | `lab13_governance.py` | ≥ 0.68 | Cada reentrenamiento y cada mes | ML Engineer | REVIEW; revisar datos y modelo |
| Brecha de recall entre grupos | `lab13_governance.py` | ≤ 0.16 | Igual | ML Engineer | REVIEW; auditar grupos; si persiste, STOP |
| Brecha de FPR entre grupos | `lab13_governance.py` | ≤ 0.16 | Igual | ML Engineer | REVIEW |
| Latencia por caso | `lab13_governance.py` | ≤ 500 ms | Igual | ML Engineer | Revisar infraestructura |
| Tamaño del modelo | `lab13_governance.py` | ≤ 1024 KB | Igual | ML Engineer | Simplificar el modelo |
| Identificadores directos en los datos | `validate_schema` | Ninguno | En cada carga | Data Engineer | STOP y tratar como incidente alto |
| Cambio en la distribución de las entradas (deriva) | Comparar entrenamiento vs. datos nuevos, p. ej. PSI por variable | PSI < 0.10 estable; 0.10–0.25 revisar; > 0.25 actuar (convención común, no una norma) | Cada mes | Data Scientist | REVIEW y reentrenar si procede |
| Uso fuera del propósito | Revisión de usos frente a `prohibited_uses` | Ninguno | Cada trimestre | Product Owner | Detener ese uso y comunicar |

Los casos de grupos pequeños (menos de 10 casos) se informan con su intervalo de confianza y no se usan para decidir. Respuesta a una señal que falla: `docs/RUNBOOK.md`. Simulacro realizado: `reports/lab13/INCIDENT_POSTMORTEM.md`.
