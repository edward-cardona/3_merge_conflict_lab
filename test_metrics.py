"""Tests — run pytest to check your resolution."""
import numpy as np
import pandas as pd
import pytest

from metrics import daily_return, volatility, cumulative


def test_daily_return_uses_log():
    prices = pd.Series([100.0, 105.0, 110.25])
    r = daily_return(prices)
    assert r.iloc[0] == pytest.approx(np.log(105 / 100), abs=1e-6)


def test_volatility_annualizes():
    r = pd.Series([0.01, -0.01, 0.02, -0.02])
    assert volatility(r) == pytest.approx(r.std() * np.sqrt(252), abs=1e-6)


def test_cumulative_is_additive_for_log_returns():
    r = pd.Series([0.05, -0.03, 0.02])
    assert cumulative(r).iloc[-1] == pytest.approx(r.sum(), abs=1e-6)
