"""Intervalos de confianza para proporciones (método de Wilson)."""

import math


def wilson_interval(successes, total, z=1.96):
    """Intervalo de Wilson al 95 % para una proporción.

    Se usa en lugar del intervalo normal simple porque funciona mejor con
    muestras pequeñas y con proporciones cercanas a 0 o a 1.
    """
    if total <= 0:
        return (float("nan"), float("nan"))
    p = successes / total
    denominator = 1 + z**2 / total
    centre = p + z**2 / (2 * total)
    margin = z * math.sqrt(p * (1 - p) / total + z**2 / (4 * total**2))
    return ((centre - margin) / denominator, (centre + margin) / denominator)
