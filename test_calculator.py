from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(6, 7) == 42

def test_divide():
    assert divide(20, 5) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)