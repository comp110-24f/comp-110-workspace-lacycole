from CQs.cq07.find_max import find_and_remove_max

"""Unit tests for find_max"""

__author__ = "730735704"


def test_max_value() -> None:
    """Tests if it returns the expected max value"""
    a: list[int] = [3, 4, 8, 10, 2, 10]
    assert find_and_remove_max(a) == 10  # returns 10 - the max value


def test_mutate() -> None:
    """Tests if the input mutates in the expected way"""
    a: list[int] = [3, 4, 8, 10, 2, 10]
    find_and_remove_max(a)
    assert a == [3, 4, 8, 2]  # mutated list


def test_correct_value() -> None:
    """Tests if -1 is returned in the case of an empty list"""
    b: list[int] = []
    assert find_and_remove_max(b) == -1  # returns -1 if list is empty
