from seasons import check_date
import pytest

def main():

    test_check_date()



def test_check_date():
    assert check_date('1979-05-17') == ("1979", "05", "17")
    assert check_date('1979-5-17') == None
    assert check_date('January, 1 1990') == None


if __name__ == "__main__":
    main()
