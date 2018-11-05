from currency import *
import pytest

rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]

def test_converts_to_itself():
    assert convert(rates, 1, "USD", "USD") == 1

def test_one_dollar_to_euro():
    assert convert(rates, 1, "USD", "EUR") == 0.74

def test_convert_with_value():
    assert convert(rates, 2, "USD", "EUR") == 1.48

def test_one_euro_to_dollar():
    assert convert(rates, 1, "EUR", "USD") == pytest.approx(1.35, 0.1)

def test_usd_to_euro(): 
    assert convert(rates, 3, "USD", "EUR") == pytest.approx(2.22, .1)

def test_euro_to_usd():
    assert convert(rates, 2, "EUR", "USD") == pytest.approx(2.7, .1)

def test_euro_to_jpy():
    assert convert(rates, 1, "EUR", "JPY") == 145.949
    assert convert(rates, 2, "EUR", "JPY") == 145.949 * 2

def test_jpy_to_euro():
    assert convert(rates, 1, "JPY", "EUR") == 1 / 145.949 

def test_raise_error_for_unknown_rates():
    with pytest.raises(ValueError, message = "Conversion rates unknown."):
        convert(rates, 1, "JPY", "CAD") 

def test_indirect_conversion_usd_to_jpy():
    assert convert(rates, 1, "USD", "JPY") == pytest.approx(.74 * 145.949, .1)

def test_indirect_conversion_jpy_to_usd():
    assert convert(rates, 1, "JPY", "USD") == pytest.approx( (1 / 145.949) / .74 , .1)