"""Simple return metrics."""


def daily_return(prices):
    """Return the daily percentage change."""
    return prices.pct_change().dropna()


# ---------- volatility ----------
# Standard annualized volatility from a returns series.
# Multiply by sqrt(252) to annualize daily data.
# --------------------------------


def volatility(returns):
    """Annualized volatility (plain power)."""
    return returns.std() * (252 ** 0.5)


# ---------- cumulative ----------
# Cumulative return over the whole series.
# --------------------------------


def cumulative(returns):
    """Cumulative simple return series."""
    return (1 + returns).cumprod() - 1
