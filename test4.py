import pytest

data = [('2', '2', 4), ('12','3',15), ('-1', '6', 1)]

@pytest.mark.parametrize("x, y, expected", data)
def test_sum_numbers(x, y, expected):
    assert int(x) + int(y) == expected