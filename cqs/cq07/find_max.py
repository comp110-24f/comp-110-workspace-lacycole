"""Challenge question that finds the max and uses unit tests"""

__author__ = "730735704"


def find_and_remove_max(input: list[int]) -> int:
    """finds and removes all instances of the max value"""
    if len(input) == 0:  # returns 0 if the list is empty
        max = -1
        return max
    max: int = input[0]  # creates the max variable
    index: int = 0
    while index < len(input):
        if max <= input[index]:
            max = input[index]  # replaces the max value with the new max value
        index += 1
    index = 0  # resets index
    while index < len(input):
        if input[index] == max:
            input.pop(index)  # removes all instances of max value
        else:
            index += 1
    return max
