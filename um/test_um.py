from um import count
import pytest

def main():

    hidden_in_word()
    test_dot_dot()
    test_punctuation()
    test_upper()
    test_none()

def hidden_in_word():
    assert count('album') == 0
    assert count('yummy') == 0
    assert count('Um, this is yummy') == 1
    assert count(' um ')

def test_dot_dot():
    assert count('Um, did this work um... yet') == 2

def test_punctuation():
    assert count('um?') == 1

def test_upper():
    assert count('Um, How are we, um... doing?') == 2

def test_none():
    assert count('Hello, World') == 0


if __name__ == "__main__":
    main()
