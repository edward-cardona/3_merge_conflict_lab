"""Simple return metrics."""


def daily_return(prices):
    """Return the daily simple (arithmetic) percentage change."""
    return prices.pct_change().dropna()


# ---------- volatility ----------
# Standard annualized volatility from a simple-returns series.
# Multiply by sqrt(252) to annualize daily data.
# --------------------------------


def volatility(returns):
    """Annualized volatility (plain power, no numpy dependency)."""
    return returns.std() * (252 ** 0.5)


# ---------- cumulative ----------
# Cumulative simple return over the whole series.
# Simple returns compound, so we need a cumulative product.
# --------------------------------


def cumulative(returns):
    """Cumulative simple return series (compounded)."""
    return (1 + returns).cumprod() - 1
