from pytest_learn.main import reverseString


def test_reverseString():
    assert reverseString("hello") == "olleh"

def test_reverse_for_empty_string():
    assert reverseString("") == ""
