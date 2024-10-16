"""Building list untility functions"""

__author__ = "730735704"


def only_evens(input: list[int]) -> list[int]:
    even_list: list[int] = []
    for number in input:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    subset: list[int] = []
    index: int = start
    if start <= 0:
        start = 0
    if end > len(input):
        end = len(input)
    if len(input) == 0 or start >= len(input) or end <= 0:
        return subset
    for index in range(start, end):
        subset.append(input[index])
        index += 1
    return subset


"""def add_at_index(input: list[int], add: int, idx: int) -> None:
    if idx > len(input) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    index: int = idx
    input.append("")"""
