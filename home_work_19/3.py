from main import factorial
import pytest



def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive():
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)