"""LAB13/E08: comprueba si se puede minimizar la variable age_band.

Entrena la misma regresion logistica con y sin age_band, con el mismo corte
temporal, y guarda la comparacion en reports/lab13/minimization_check.csv.
No modifica el modelo del proyecto.
"""
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from inf8239_u04.data import load_data, temporal_split
from inf8239_u04.fairness import audit, gap

NUMERIC = ["previous_incidents", "infrastructure_score", "exposure"]


def evaluate(df, categorical):
    train, test = temporal_split(df)
    cols = categorical + NUMERIC
    transformers = [("num", StandardScaler(), NUMERIC)]
    if categorical:
        transformers.insert(0, ("cat", OneHotEncoder(handle_unknown="ignore"), categorical))
    model = make_pipeline(
        ColumnTransformer(transformers),
        LogisticRegression(max_iter=1200, class_weight="balanced", random_state=42),
    )
    model.fit(train[cols], train.target)
    pred = model.predict(test[cols])
    _, by_group, _ = audit(test.target, pred, test.protected_group)
    return {
        "features": ", ".join(cols),
        "accuracy": round(float(accuracy_score(test.target, pred)), 4),
        "recall": round(float(recall_score(test.target, pred)), 4),
        "recall_gap": round(gap(by_group, "recall"), 4),
        "fpr_gap": round(gap(by_group, "fpr"), 4),
    }


def run(df):
    rows = {
        "con_age_band": evaluate(df, ["zone", "age_band"]),
        "sin_age_band": evaluate(df, ["zone"]),
    }
    return pd.DataFrame(rows).T.rename_axis("variant")


if __name__ == "__main__":
    out = Path("reports/lab13")
    out.mkdir(parents=True, exist_ok=True)
    result = run(load_data())
    result.to_csv(out / "minimization_check.csv")
    print(result.to_string())
