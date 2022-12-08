import pytest

def div_two(x):
    return 5 / x

def test_div_two_zero():
    with pytest.raises(ZeroDivisionError):
        div_two(0)