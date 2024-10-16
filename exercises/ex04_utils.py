"""Using the utility functions of lists"""

__author__ = "730735704"


def all(integers: list[int], num: int) -> bool:
    """Checks if all ints in a list match one int"""
    index: int = 0
    occurances: int = 0  # tracks number of occurances
    if len(integers) == 0:  # returns false if list is empty
        return False
    while index < len(integers):  # goes through all values in list
        if integers[index] == num:
            occurances += 1
        index += 1
    if occurances == len(integers):  # true if all occurances match
        return True
    else:
        return False


def max(integers: list[int]) -> int:
    """Returns the largest value in the list"""
    if len(integers) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index: int = 0
        largest_val: int = integers[0]  # keeps track of largest variable
        while index < len(integers):
            if integers[index] > largest_val:
                largest_val = integers[index]  # replaces largest_val with largest
            index += 1
        return largest_val


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks deep equality of two lists"""
    if len(first_list) == len(second_list):  # checks if equal lengths
        index: int = 0
        same: int = 0  # tracks number of similarities
        while index < len(first_list):
            if first_list[index] == second_list[index]:
                same += 1
            index += 1
        if same == len(first_list):  # checks if both lists are exactly equal
            return True
        else:
            return False
    else:
        return False


def extend(first_list: list[int], second_list: list[int]) -> None:
    """Appends second list to first list"""
    for value in second_list:  # for all values in second list
        first_list.append(value)  # appends every value in second list
    return None
