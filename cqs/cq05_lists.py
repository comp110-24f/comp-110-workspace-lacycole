"""Mutating functions."""

__author__ = "730735704"


def manual_append(list: list[int], num: int) -> None:
    """Appends a number to the end of the list"""
    list.append(num)


def double(list: list[int]) -> None:
    """Doubles each value in a list"""
    index: int = 0
    while index < len(list):  # cycles through every value in the list
        list[index] = list[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # both are refering back to the same list(in the heap)

double(list_2)
print(list_1)  # print the double version because they are refering to the same list
print(list_2)
