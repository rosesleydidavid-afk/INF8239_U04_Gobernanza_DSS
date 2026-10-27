# Model Card — Territorial Review DSS (Synthetic)

Decisión final de LAB13: **GO limitado**. El sistema solo prioriza casos para revisión humana; nunca decide por sí solo.

## Intended use
Priorizar casos sintéticos para que una persona los revise primero. La salida del modelo es una sugerencia de orden de revisión, no una decisión. El modelo es una regresión logística (con preprocesamiento) entrenada con datos sintéticos de práctica educativa. Usuarios previstos: operadores del equipo de revisión, bajo la supervisión de la Institutional Owner.

## Out-of-scope use
Prohibido (según `configs/governance.yml`): intervención automática, decisiones de elegibilidad y declaración de emergencias. Tampoco se debe usar para perfilar o hacer inferencias sobre poblaciones reales, ni con datos reales sin una nueva evaluación de impacto, auditoría y aprobación. El conjunto de datos no contiene identificadores directos (nombre, documento, correo, teléfono) y el sistema los rechaza si aparecen.

## Data and split
Conjunto sintético de 640 casos con semilla fija; no contiene personas, lugares ni estadísticas oficiales reales de la República Dominicana. Columnas usadas como entrada: zone, age_band, previous_incidents, infrastructure_score, exposure. El grupo protegido (protected_group) no se usa como entrada: solo se usa para auditar. División temporal por fecha de recepción: 480 casos para entrenar (2026-01-01 a 2026-09-24) y 160 para evaluar (2026-09-25 a 2026-12-27). En la evaluación, G1 tiene 101 casos y G2 tiene 59. Fechas y datos son sintéticos. No hay valores faltantes.

## Global and subgroup evaluation
Evaluación global (160 casos de prueba): exactitud 0.719; recall 0.717; precisión 0.776; tasa de falsos positivos (FPR) 0.279.

Por grupo (modelo logístico):

| Grupo | Casos | Recall | IC95% recall (Wilson) | FPR | IC95% FPR (Wilson) |
|---|---|---|---|---|---|
| G1 | 101 | 0.653 | 0.513–0.771 | 0.250 | 0.152–0.382 |
| G2 | 59 | 0.791 | 0.648–0.886 | 0.375 | 0.185–0.614 |

Brechas: recall 0.138 y FPR 0.125 (límite 0.16 en ambas). Compuertas de `configs/governance.yml`: recall ≥ 0.68, brecha de recall ≤ 0.16, brecha de FPR ≤ 0.16, latencia ≤ 500 ms, tamaño ≤ 1024 KB. Resultado de `scripts/lab13_governance.py`: GO (las 5 compuertas pasan).

Los intervalos de G1 y G2 se solapan, por lo que la diferencia entre grupos no se puede confirmar ni descartar con estos datos. En la auditoría interseccional, varias celdas tienen menos de 10 casos (MIN_SUPPORT = 10) y no se interpretan. El árbol de decisión se descartó: su brecha de recall (0.181) y su brecha de FPR (0.168) superan el límite de 0.16.

## Green AI evidence
Entrenamiento: 0.36 s. Tamaño del modelo: 3.6 KB. Latencia por caso: 0.09 ms. Se eligió un modelo pequeño (regresión logística) y no se necesitó hardware especial. Todo corre en una computadora personal. Se evita reentrenar sin motivo: solo se reentrena si falla una compuerta o si cambia el tipo de datos.

## Limitations, human oversight and appeal
- Datos sintéticos y pocos casos de prueba (160): los resultados son orientativos y no se pueden generalizar a casos reales.
- El recall de G1 (0.653) está por debajo del mínimo de 0.68; solo el recall global cumple. Por eso el GO es limitado y se monitorea por grupo.
- Los intervalos de confianza son amplios, sobre todo para G2 y para los grupos interseccionales.
- Los falsos negativos (casos que necesitaban revisión y no fueron priorizados) son el daño principal; el equipo debe poder revisar también casos no priorizados.
- Supervisión humana: una persona revisa siempre los casos priorizados y puede cambiar el orden. El sistema no ejecuta ninguna acción por sí mismo.
- Apelación: toda persona afectada puede pedir revisión humana de su caso. Actividad "Human review and appeals" del RACI (Responsible: Product Owner; Accountable: Institutional Owner).
- Condiciones para dejar de usar el modelo (REVIEW/STOP): falla cualquier compuerta, aparecen identificadores directos, o se propone un uso prohibido.

## Owner and review date
Responsable (Accountable): Institutional Owner. Elaborado por: Rosesleydi Nicol García David, con asistencia de IA (ver `docs/AI_USE_DECLARATION.md`). Fecha de elaboración: 2026-10-27. Próxima revisión: 2027-01-25 (90 días), o antes si falla una compuerta o cambian los datos.
