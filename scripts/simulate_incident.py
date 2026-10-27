from datetime import UTC, datetime
from pathlib import Path

# Corregido: el original tenía saltos de línea reales dentro de una cadena
# (SyntaxError). Además, no se sobrescribe un postmortem ya redactado.
path = Path("reports/lab13/INCIDENT_POSTMORTEM.md")
path.parent.mkdir(parents=True, exist_ok=True)
if path.exists():
    print(f"{path} ya existe: no se sobrescribe.")
else:
    text = (
        "# Incident simulation\n\n"
        f"- detected_at: {datetime.now(UTC).isoformat()}\n"
        "- signal: recall gap exceeded\n"
        "- containment: REVIEW and safe baseline\n"
        "- evidence: preserved report and model version\n"
        "- communication: REPLACE\n"
        "- corrective actions, owners and dates: REPLACE\n"
    )
    path.write_text(text, encoding="utf-8")
    print(path)
