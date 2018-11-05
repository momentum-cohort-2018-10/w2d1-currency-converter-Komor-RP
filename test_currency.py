from currency import *

rates = [("USD", "EUR", 0.74)]

def test_converts_to_itself():
    assert convert(rates, 1, "USD", "USD") == 1

def test_one_dollar_to_euro():
    assert convert(rates, 1, "USD", "EUR") == 0.74