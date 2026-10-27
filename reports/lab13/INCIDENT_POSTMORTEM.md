# Incident simulation

**Esto fue un simulacro. No ocurrió un incidente real y ningún caso fue afectado.** El resultado real de `scripts/lab13_governance.py` fue GO (brecha de recall 0.138, límite 0.16). El simulacro ensaya qué se haría si esa brecha superara el límite.

- detected_at: 2026-10-27T15:27:32.432293+00:00
- signal: recall gap exceeded
- containment: REVIEW and safe baseline
- evidence: preserved report and model version
- communication: La Institutional Owner y el equipo (Data Scientist, Data Engineer, Legal) recibirían un resumen con qué señal falló, desde cuándo y qué se hizo. Los representantes de las personas afectadas serían informados en lenguaje claro, sin datos personales, con la oferta de revisión humana de sus casos. Redacta: Product Owner; consulta: Legal.
- corrective actions, owners and dates: (1) Suspender la priorización del modelo y revisar casos en orden de fecha de recepción: ML Engineer, el mismo día de la detección. (2) Repetir la auditoría por grupo y los intervalos de confianza para confirmar la brecha: Data Scientist, en 2 días hábiles. (3) Revisar los datos de entrada por cambios o identificadores directos: Data Engineer, en 2 días hábiles. (4) Decidir si se reentrena o se mantiene en REVIEW/STOP: Institutional Owner, tras recibir (2) y (3). (5) Cerrar este postmortem: Product Owner, en 5 días hábiles. Plazos propuestos para el simulacro; en un incidente real los fijaría la Institutional Owner.
