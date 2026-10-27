# Registro de decisión · LAB11 (preliminar)

**Sistema:** Territorial Review DSS (caso sintético). Prioriza casos para revisión humana.
**Fecha:** 27 de octubre de 2026
**Quien redacta este registro:** Rosesleydi Nicol García David
**Responsable del sistema (rol):** Institutional Owner

## Decisión
**REVIEW (revisar).** Se puede continuar hacia la auditoría de equidad (LAB12), pero no se recomienda usar ni desplegar el sistema todavía. Esta decisión es preliminar y se actualiza al terminar LAB12.

## Evidencia
En el registro de riesgos (`reports/lab11/risk_register_scored.csv`) los tres de mayor prioridad son:

1. **R02 (prioridad 9):** el sistema podría fallar más con un grupo que con otro.
2. **R01 (prioridad 8):** un caso urgente podría quedar al final de la fila.
3. **R07 (prioridad 8):** una persona afectada podría quedarse sin una vía real para cuestionar la recomendación.

Los tres tienen un control y un responsable asignados. R01 y R07 conservan un riesgo residual alto porque su impacto es el más grave (4 de 4), aunque su probabilidad sea baja.

## Incertidumbre
- Todavía no se midió el desempeño ni las brechas por grupo; eso se hace en LAB12. La etapa MEASURE del marco NIST aparece pendiente en `rmf_summary.json`.
- La prioridad es probabilidad por impacto en escalas de 1 a 4. Sirve para ordenar la atención, no es una probabilidad científica.
- Los datos son sintéticos. No se pueden sacar conclusiones sobre personas ni territorios reales.

## Por qué no GO
No hay evidencia medida de que el sistema funcione de forma pareja entre grupos, y el riesgo de mayor prioridad (R02) trata justamente de eso.

## Por qué no STOP
No hay evidencia de daño, los controles propuestos son viables y la alternativa sin modelo (orden de llegada) sigue disponible para comparar.

## Condiciones para pasar a GO
- Recall mínimo de 0.68 y brechas de recall y de falsos positivos entre grupos de 0.16 o menos (límites de `configs/governance.yml`).
- Revisión humana y mecanismo de apelación funcionando.
- Resultados de LAB12 revisados por el responsable institucional.

## Condiciones de retiro (STOP)
Las del campo `withdrawal_condition` de `student_inputs/lab11_impact.yml`.

## Qué no permite concluir
Este registro no demuestra que el sistema sea justo ni injusto. Solo documenta riesgos y controles antes de medir.
