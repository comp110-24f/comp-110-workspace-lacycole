"""EX02 - Chardle - a cute step toward Wordle."""

__author__ = "730735704"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """takes input of 5 letter word"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:  # valid if the word is exactly 5 characters
        return word
    else:  # not valid if word is not 5 characters
        print("Error: Word must contain 5 characters.")
        exit()  # exits program
        return word


def input_letter() -> str:
    """Takes input of 1 character"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:  # valid if letter is one character
        return letter
    else:  # not valid if more than 1 character
        print("Error: Character must be a single character.")
        exit()  # exists program
        return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if letter matches the index of the word and counts how many"""
    print("Searching for " + letter + " in " + word)
    count: int = 0  # count starts at 0
    if word[0] == letter:  # checks if letter matches 1st letter of word
        count += 1  # adds 1 to count for every instance
        print(letter + " found at index 0")
        if word[1] == letter:  # can check if there are multiple instances of the letter
            count += 1
            print(letter + " found at index 1")
            if word[2] == letter:
                count += 1
                print(letter + " found at index 2")
                if word[3] == letter:
                    count += 1
                    print(letter + " found at index 3")
                    if word[4] == letter:
                        count += 1
                        print(letter + " found at index 4")
                elif word[4] == letter:  # for multiple instances not next to eachother
                    count += 1
                    print(letter + " found at index 4")
            elif word[3] == letter:
                count += 1
                print(letter + " found at index 3")
                if word[4] == letter:  # for multiple instances not next to and next to
                    count += 1
                    print(letter + " found at index 4")
            elif word[4] == letter:
                count += 1
                print(letter + " found at index 4")
        elif word[2] == letter:
            count += 1
            print(letter + " found at index 2")
            if word[3] == letter:
                count += 1
                print(letter + " found at index 3")
            elif word[4] == letter:
                count += 1
                print(letter + " found at index 4")
        elif word[3] == letter:
            count += 1
            print(letter + " found at index 3")
            if word[4] == letter:
                count += 1
                print(letter + " found at index 4")
        elif word[4] == letter:
            count += 1
            print(letter + " found at index 4")
    elif word[1] == letter:  # checks if letter matches 2nd letter of word
        count += 1
        print(letter + " found at index 1")
        if word[2] == letter:  # for multiple instances of the letter
            count += 1
            print(letter + " found at index 2")
            if word[3] == letter:
                count += 1
                print(letter + " found at index 3")
                if word[4] == letter:
                    count += 1
                    print(letter + " found at index 4")
            elif word[4] == letter:  # if index 1, 2, and 4 = letter
                count += 1
                print(letter + " found at index 4")
        elif word[3] == letter:
            count += 1
            print(letter + " found at index 3")
            if word[4] == letter:
                count += 1
                print(letter + " found at index 4")
        elif word[4] == letter:
            count += 1
            print(letter + " found at index 4")
    elif word[2] == letter:  # 3rd letter
        count += 1
        print(letter + " found at index 2")
        if word[3] == letter:
            count += 1
            print(letter + " found at index 3")
            if word[4] == letter:
                count += 1
                print(letter + " found at index 4")
        elif word[4] == letter:
            count += 1
            print(letter + " found at index 4")
    elif word[3] == letter:  # 4th letter
        count += 1
        print(letter + " found at index 3")
        if word[4] == letter:
            count += 1
            print(letter + " found at index 4")
    elif word[4] == letter:  # 5th letter
        count += 1
        print(letter + " found at index 4")
    if count == 0:  # for if there are no instances of letter in word
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:  # prints how many instances of letter in word
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
