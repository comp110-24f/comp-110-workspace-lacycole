"""A challenge question using while loops"""

__author__ = "730735704"


def num_instances(phrase: str, search_char: str) -> int:
    """Counts the number of occurances of a character in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):  # checks all characters
        if phrase[index] == search_char:  # moving by index
            count += 1
        index += 1
    print(count)
    return count


num_instances(phrase="HelloHeLloHEllo", search_char="e")
