#teste multiplicando
import pytest
def multiplicando(x:int) -> int:
    if not isinstance(x, int):
        raise ValueError("variable x must be of int type")
    return x * 5

def test_multiplicando_returns_quintuple_the_input():
    actual_result = multiplicando(x=2)
    assert actual_result == 10

def test_multiplicando_returns_zero_when_x_is_zero():
    actual_result = multiplicando(0)
    assert actual_result == 0

def test_multiplicando_returns_correct_value_for_negative_int():
    actual_result = multiplicando(-4)
    assert actual_result == -20

def test_multiplicando_raises_when_x_is_string():
    with pytest.raises(ValueError):
        multiplicando("texto")

def test_multiplicando_raises_when_x_is_float():
    with pytest.raises(ValueError):
        multiplicando(5.25)