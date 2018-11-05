from currency import *
import pytest

rates = [("USD", "EUR", 0.74)]

def test_converts_to_itself():
    assert convert(rates, 1, "USD", "USD") == 1

def test_one_dollar_to_euro():
    assert convert(rates, 1, "USD", "EUR") == 0.74

def test_convert_with_value():
    assert convert(rates, 2, "USD", "EUR") == 1.48

def test_one_euro_to_dollar():
    assert convert(rates, 1, "EUR", "USD") == pytest.approx(1.35, 0.1)