"""Building list untility functions"""

__author__ = "730735704"


def only_evens(input: list[int]) -> list[int]:
    """Creates a new lists that contains only the even numbers from the input list"""
    even_list: list[int] = []  # creating a new list - not mutating input
    for number in input:  # goes through all items in input
        if number % 2 == 0:  # checks if the number is even
            even_list.append(number)  # adds every even number to the end of the list
    return even_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Creates a new list that is a subset of an input list"""
    subset: list[int] = []  # creating a new list - not mutating input
    index: int = start  # index for moving through the range given
    if start <= 0:
        start = 0  # negative start - starts at the beginning of the list
    if end > len(input):
        end = len(input)  # end greater than the length - ends at the end of the list
    if len(input) == 0 or start >= len(input) or end <= 0:
        return subset  # returns an empty list
    for index in range(start, end):  # cycles through items only between start and end
        subset.append(input[index])
        index += 1
    return subset


def add_at_index(input: list[int], add: int, idx: int) -> None:
    if idx > len(input) or idx < 0:  # error if index is out of range of the list length
        raise IndexError("Index is out of bounds for the input list")
    else:
        input.append(0)  # adds value to the end so everything can shift to the right
        move_to: int = len(input) - 1  # last value in the list - will be 0
        move: int = len(input) - 2  # value that will move to the right
        index: int = len(input)
        while index > idx:  # stop shifting when it reaches where the new item is added
            input[move_to] = input[move]  # changes the value - shifts items
            index -= 1
            move_to -= 1
            move -= 1
        input[idx] = add  # adds new value after shifting is finished
