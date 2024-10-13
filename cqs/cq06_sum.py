"""Summing the elements of a list using different loops"""

__author__ = "730735704"


def w_sum(vals: list[float]) -> float:
    """Using a while loop"""
    index: int = 0
    sum: float = 0.0  # keeps the value of the sum
    while index < len(vals):
        sum += vals[index]  # adds each value to the sum
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Using for in"""
    sum: float = 0.0
    for value in vals:  # value is each extry in the list
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Using for in range"""
    index: int = 0
    sum: float = 0.0
    for index in range(len(vals)):  # range has to relate to the index - not the values
        sum += vals[index]  # adds to sum
        index += 1
    return sum
