from square import square
import pytest

@pytest.mark.parametrize( "value,result", [
        (-2, 4),
        (-1, 1),
        (0, 0),
        (1, 1),
        (2, 4),
        (-2.00, 4.00),
        (-1.00, 1.00),
        ( 0.00, 0.00),
        ( 1.00, 1.00),
        ( 2.00, 4.00),
    ])
def test_square(value,result):
    assert square(value) == result

@pytest.mark.parametrize( "value,wrong_result", [
        (-2, -2),
        (1, -1),
        (0, 0.000001),
        (1, -1),
        (-2.00, -4.00),
        (-1.00, -1.00),
        ( 0.00000000001, 0.00),
        ( 2.00, 2.00),
    ])
def test_square_fail(value,wrong_result):
    assert not square(value) == wrong_result