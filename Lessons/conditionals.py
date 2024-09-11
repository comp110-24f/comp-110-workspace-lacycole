"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")


# less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off"""
    if alarm is True:
        return "Wake up! Go to Comp 110!"
    else:
        return "Keep sleeping. You deserve it. :)"


# print(wake_up(alarm=False))

"""Practice on my own"""


def check_first_letter(word: str, letter: str) -> str:
    """checks if the first letter of the word matches the given letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="happy", letter="h"))  # should return "match!"
# print(check_first_letter(word="happy", letter="s"))  # should return "no match!"
