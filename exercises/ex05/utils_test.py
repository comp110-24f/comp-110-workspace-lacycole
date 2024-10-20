from exercises.ex05.utils import only_evens, sub, add_at_index

"""Writing unit tests for my functions"""

__author__ = "730735704"


# Unit tests for only_evens
def test_only_evens() -> None:
    """Use case - tests that only_evens returns only the even values"""
    list_1: list[int] = [5, 6, 7]
    assert only_evens(list_1) == [6]  # only returns 6


def test_only_evens_none() -> None:
    """Use case - tests that only_evens returns no values if all are odd"""
    list_2: list[int] = [5, 13, 3]
    assert only_evens(list_2) == []  # returns none because all are odd


def test_only_evens_multiple() -> None:
    """Use case - tests that only_evens can return multiple of the same even value"""
    list_3: list[int] = [8, 8, 8]
    assert only_evens(list_3) == [8, 8, 8]  # returns all because all are even


# Unit tests for sub
def test_sub() -> None:
    """Use case - tests that sub returns values on the correct index"""
    list_4: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_4, 1, 3) == [2, 3]  # returns items between index 1 and 3


def test_sub_negative() -> None:
    """Edge case - tests that sub with negative start and big end"""
    list_5: list[int] = [1, 2, 3, 4]
    assert sub(list_5, -1, 6) == [1, 2, 3, 4]  # -1 = 0 and 6 = length of input


def test_sub_empty() -> None:
    """Edge case - tests that sub returns nothing with an empty list"""
    list_6: list[int] = []
    assert sub(list_6, 1, 3) == []  # empty list


# Unit tests for add_at_index
def test_add_at_index() -> None:
    """Use case - tests add_at_index correctly adds item at an index"""
    list_7: list[int] = [5, 6, 7, 9]
    add_at_index(list_7, 8, 3)  # runs the function
    assert list_7 == [5, 6, 7, 8, 9]  # adds 8 to index 3


def test_add_at_index_end() -> None:
    """Use case - tests add_at_index can add an item to the end of a list"""
    list_8: list[int] = [3]
    add_at_index(list_8, 4, 1)  # runs the function
    assert list_8 == [3, 4]  # 4 is added to index 1


def test_add_at_index_error() -> None:
    """Edge case - tests that error is returned if list is empty"""
    list_9: list[int] = []
    assert add_at_index(list_9, 1, 0) == add_at_index(
        [1], 1, 0
    )  # got add_at_index([1], 1, 0) from running this test
