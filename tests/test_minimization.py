import importlib.util
from pathlib import Path

from inf8239_u04.data import load_data

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "minimization_check.py"


def _load():
    spec = importlib.util.spec_from_file_location("minimization_check", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_minimization_comparison_has_both_variants():
    result = _load().run(load_data())
    assert list(result.index) == ["con_age_band", "sin_age_band"]
    assert "age_band" not in result.loc["sin_age_band", "features"]


def test_removing_age_band_keeps_recall_above_gate():
    result = _load().run(load_data())
    assert float(result.loc["sin_age_band", "recall"]) >= 0.68
