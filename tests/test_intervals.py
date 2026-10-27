import math

import pytest

from inf8239_u04.intervals import wilson_interval


def test_wilson_half_of_ten():
    low, high = wilson_interval(5, 10)
    assert low == pytest.approx(0.2366, abs=1e-3)
    assert high == pytest.approx(0.7634, abs=1e-3)


def test_wilson_stays_inside_zero_one():
    low, high = wilson_interval(0, 10)
    assert low == pytest.approx(0.0, abs=1e-9)
    assert 0 < high < 0.35
    low, high = wilson_interval(10, 10)
    assert high == pytest.approx(1.0, abs=1e-9)


def test_wilson_without_cases_is_nan():
    low, high = wilson_interval(0, 0)
    assert math.isnan(low) and math.isnan(high)
