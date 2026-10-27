# Declaración de uso de inteligencia artificial · Unidad 04 (LAB11–LAB12, Ejercicio 07)

## Herramientas utilizadas
Claude (Anthropic), usado como asistente paso a paso durante el ejercicio. Esta declaración cubre el uso de Claude; si en algún momento se usó otra herramienta de IA, se indicaría aquí.

## Propósito de cada uso
- Revisar el proyecto base del profesor, ejecutarlo en un entorno de prueba y encontrar errores.
- Redactar borradores de `student_inputs/lab11_impact.yml`, `stakeholders.csv`, `risk_register.csv`, `reports/lab11/DECISION_RECORD.md` y `student_inputs/lab12_decision.yml`.
- Escribir `src/inf8239_u04/intervals.py`, `scripts/lab12_intervals.py` y `tests/test_intervals.py` (intervalos de confianza de Wilson).
- Calcular, fuera de los scripts del profesor, los conteos por grupo y los intervalos que se usaron para interpretar.
- Explicarme cada comando y ayudarme a leer los resultados; redactar la síntesis del Ejercicio 07.

## Prompts o decisiones relevantes
- Pegué el mandato del Ejercicio 07, los manuales LAB11 y LAB12 y el proyecto base, y pedí avanzar paso a paso con un checklist, como si yo no supiera nada.
- Pedí que Claude redactara los borradores de los campos de la evaluación de impacto con lenguaje natural. Claude indicó que los valores del análisis son mi decisión, que quedarían declarados como borradores suyos y que yo debía revisarlos; los revisé y acepté sin cambios.
- Decisión de análisis: mantener REVIEW como decisión preliminar tras LAB11 y limitar el uso del modelo tras LAB12.
- Pegué la salida real de cada comando que ejecuté.

## Elementos verificados por mí
Marcar solo lo que se hizo de verdad:
- [x] Ejecuté en mi computadora `uv sync --frozen`, `uv run pytest -q` (13 pruebas aprobadas), `scripts/lab11_impact.py`, `scripts/lab12_audit.py` con los dos modelos, `scripts/lab12_intervals.py` y `scripts/validate_lab12_decision.py`.
- [x] Leí los borradores de propósito, interesados, riesgos y decisión, y estoy de acuerdo con ellos.
- [x] Guardé el trabajo en 6 commits y lo subí a GitHub con las etiquetas `u04-lab12` y `u04-e07`.
- [ ] Puedo explicar por qué un recall global aceptable puede esconder un recall bajo en un grupo.
- [ ] Puedo explicar qué es un intervalo de confianza de Wilson y por qué los intervalos de G1 y G2 se solapan.
- [ ] Puedo explicar la diferencia entre obligación legal, marco voluntario y recomendación ética en este caso.
- [ ] Puedo explicar por qué la decisión es REVIEW aunque las puertas automáticas puedan dar GO.

Verificaciones hechas por la IA: ejecutó el proyecto base, sus pruebas y mis scripts en su propio entorno antes de dármelos, y comprobó que sus cifras coincidieran con las de mi corrida. Verificó el texto de la Ley 172-13 en una republicación del texto legal (no en la Gaceta Oficial).

## Errores detectados y correcciones
- Dos scripts del profesor (`scripts/lab11_impact.py` y `scripts/simulate_incident.py`) tenían un error de sintaxis (saltos de línea dentro de una cadena). Claude los corrigió y además evitó que sobrescriban un registro ya redactado. El primer commit del repositorio ya incluye esta corrección; es una modificación al código del profesor.
- Al pegar los CSV, las líneas quedaron con espacios al inicio y el programa decía que faltaban columnas. Claude reprodujo el error y dio un comando de limpieza.
- Los intervalos de confianza los calculó primero Claude fuera del proyecto; para que fueran verificables se agregó un script y una prueba dentro del repositorio.
- El criterio de "mínimo de 10 casos" para interpretar un grupo lo propuso Claude; es un criterio mío aceptado, no del profesor.
- Los números de probabilidad, impacto y riesgo residual de cada fila del registro venían en la plantilla del profesor; los escenarios se redactaron para encajar con ellos.

## Responsabilidad asumida
Soy responsable del código, los resultados, las referencias y las conclusiones entregadas, y debo poder explicarlos. No se inventaron resultados ni bibliografía.

Lo que no verifiqué de forma independiente:
- El texto de la Ley 172-13 lo leí a través de la IA, en una republicación del texto y no en la Gaceta Oficial. No comprobé si hay reformas posteriores.
- Los intervalos de Wilson los escribió y comprobó la IA. Yo ejecuté el script y las pruebas, pero no deduje la fórmula por mi cuenta.
- La cita de Wilson (1927) la aportó la IA de memoria y no se comprobó en la fuente. Las demás referencias provienen del material del curso y no abrí cada una.
- Los números de probabilidad, impacto y riesgo residual de cada riesgo vinieron en la plantilla del profesor; no los recalibré.
