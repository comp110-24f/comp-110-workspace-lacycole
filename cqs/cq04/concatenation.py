"""Concatenation for cq04"""

__author__ = "730735704"


def concat(stringone: str, stringtwo: str) -> str:
    return stringone + stringtwo  # concatenates both strings


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":  # stops visualize from automatically printing
    print(concat(word1, word2))
