from currency import *

rates = []

def test_converts_to_itself():
    assert convert(rates, 1, "USD", "USD") == 1
