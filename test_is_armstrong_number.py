# Unit tests for is_armstrong_number function
# Call syntax1: python -m unittest test_is_armstrong_number.py
# Call syntax2: pytest -v

import pytest
from is_armstrong_number import is_armstrong_number

def test_known_armstrong_numbers():
    for n in [153, 370, 371, 407]:
        assert is_armstrong_number(n)

def test_non_armstrong_numbers():
    for n in [100, 200, 123]:
        assert not is_armstrong_number(n)

@pytest.mark.parametrize("n", range(10))
def test_single_digit_numbers(n):
    assert is_armstrong_number(n)
