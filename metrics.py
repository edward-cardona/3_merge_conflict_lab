"""Simple return metrics."""

import numpy as np


def daily_return(prices):
    """Return the daily log return: ln(P_t / P_{t-1})."""
    return np.log(prices).diff().dropna()


# ---------- volatility ----------
# Standard annualized volatility from a log-returns series.
# Multiply by sqrt(252) to annualize daily data.
# --------------------------------


def volatility(returns):
    """Annualized volatility (numpy sqrt)."""
    return returns.std() * np.sqrt(252)


# ---------- cumulative ----------
# Cumulative log return over the whole series.
# Log returns are additive, so a plain cumsum is enough.
# --------------------------------


def cumulative(returns):
    """Cumulative log return series."""
    return returns.cumsum()
