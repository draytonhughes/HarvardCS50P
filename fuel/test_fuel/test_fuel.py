import fuel
import pytest


from fuel import convert
from fuel import gauge


def main():
    test_correct()
    test_zero()
    test_value()

# Call the test function

# test ZeroDivsion Error

def test_zero():
    with pytest.raises(ZeroDivisionError):
            assert convert('1/0')

# test ValueError
def test_value():
    with pytest.raises(ValueError):
            assert convert('cat/dog')


# test Correct Input

def test_correct():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

if __name__ == "__main__":
    main()