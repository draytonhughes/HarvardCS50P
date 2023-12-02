import bank
from bank import value

def main():

    # Call test function
    test_return_zero()
    test_return_twenty()
    test_return_hundred()


###. Functions for different tests

    # Test Return 0
def test_return_zero():
    assert value('Hello') == 0
    assert value('Hello, how are you') == 0

    # Test Retrun 20
def test_return_twenty():
    assert value('Hi, how are you') == 20
    assert value('How is the weather today') == 20

    # Test Return 100
def test_return_hundred():
    assert value('Good Morning') == 100
    assert value('Nice weather today?') == 100
    assert value('What is your account number?') == 100


if __name__ == "__main__":
    main()