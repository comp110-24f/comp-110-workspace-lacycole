"""Summing the elements of a list using different loops"""

__author__ = "730735704"


def w_sum(vals: list[float]) -> float:
    """Using a while loop"""
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Using for in"""
    sum: float = 0.0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Using for in range"""
    sum: float = 0.0
    for value in range(0, len(vals)):
        sum += value
    return sum
