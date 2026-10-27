"""Intervalos de confianza de recall y falsos positivos por grupo (LAB12).

Reproduce con el mismo corte temporal y los mismos modelos de lab12_audit.py.
Escribe reports/lab12/confidence_intervals.csv.
"""

from pathlib import Path

import pandas as pd

from inf8239_u04.data import features, load_data, temporal_split
from inf8239_u04.fairness import intersectional
from inf8239_u04.intervals import wilson_interval
from inf8239_u04.model import build_model

# Criterio propio (no del profesor): por debajo de este número de casos de la
# clase, la tasa no se interpreta.
MIN_SUPPORT = 10

df = load_data()
train, test = temporal_split(df)
rows = []
for kind in ("logistic", "tree"):
    model = build_model(kind)
    model.fit(features(train), train.target)
    scored = test.assign(pred=model.predict(features(test)))
    scored["intersection"] = intersectional(scored)
    for level, column in (("group", "protected_group"), ("intersection", "intersection")):
        for name, part in scored.groupby(column):
            positives = part[part.target == 1]
            negatives = part[part.target == 0]
            for metric, subset, hits in (
                ("recall", positives, int((positives.pred == 1).sum())),
                ("fpr", negatives, int((negatives.pred == 1).sum())),
            ):
                low, high = wilson_interval(hits, len(subset))
                rows.append(
                    {
                        "model": kind,
                        "level": level,
                        "group": name,
                        "metric": metric,
                        "hits": hits,
                        "total": len(subset),
                        "rate": hits / len(subset) if len(subset) else float("nan"),
                        "ci95_low": low,
                        "ci95_high": high,
                        "enough_support": len(subset) >= MIN_SUPPORT,
                    }
                )
out = Path("reports/lab12")
out.mkdir(parents=True, exist_ok=True)
result = pd.DataFrame(rows)
result.to_csv(out / "confidence_intervals.csv", index=False)
print(result[result.level == "group"].round(3).to_string(index=False))
print(f"\nGrupos interseccionales con poco soporte (<{MIN_SUPPORT}):")
weak = result[(result.level == "intersection") & (~result.enough_support)]
print(weak[weak.model == "logistic"][["group", "metric", "total"]].to_string(index=False))
