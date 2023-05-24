from square import square

def test_square_zero():
    assert square(0) == 0

def test_square_identity():
    assert square(1) == 1
    assert square(1.0) == 1.0
    assert square(1e0) == 1.0

def test_square_values():
    assert square(2) == 4
