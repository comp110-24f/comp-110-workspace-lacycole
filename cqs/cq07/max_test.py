from CQs.cq07.find_max import find_and_remove_max

"""Unit tests for find_max"""

__author__ = "730735704"

# returns the expected value
# mutates the input in the expected way
# returns the correct value in the case of unconventialel input


def test_max_value() -> None:
    a: list[int] = [3, 4, 8, 10, 2, 10]
    assert find_and_remove_max(a) == 10


def test_mutate() -> None:
    a: list[int] = [3, 4, 8, 10, 2, 10]
    find_and_remove_max(a)
    assert a == [3, 4, 8, 2]


def test_correct_value() -> None:
    b: list[int] = []
    assert find_and_remove_max(b) == -1
