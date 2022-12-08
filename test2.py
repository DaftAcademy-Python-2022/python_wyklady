def add2(x):
    return x + 2

def test_add2_success():
    assert add2(3) == 5

def test_add2_fail():
    assert add2(3) == 3