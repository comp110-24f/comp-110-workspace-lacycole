"""Creating a game of Wordle"""

__author__ = "730735704"


def input_guess(length: int) -> str:
    """Checks if input word is the correct length"""
    guess: str = input(f"Enter a {length} character word: ")  # user imputs a word
    while len(guess) != length:  # retry if input does not match correct length
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks to see if a certain character in guess appears in the secret word"""
    assert len(char_guess) == 1  # length of char_guess should be 1
    index: int = 0
    occurances: int = 0  # counts if character occurs in the word
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            occurances += 1
        index += 1
    return bool(occurances > 0)


def emojified(guess: str, secret: str) -> str:
    """Uses emojis to visualize if letters are present and/or in the correct spot"""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    index: int = 0  # allows it to check every letter
    visual: str = ""  # allows the emojis to be displayed on the same line
    while index < len(secret):
        if secret[index] == guess[index]:
            visual += green_box
        elif contains_char(secret, guess[index]) is True:  # character is present
            visual += yellow_box
        else:
            visual += white_box  # character is not present
        index += 1
    return visual


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_num: int = 1  # keeps track of what turn player is on
    win: bool = False  # checks if player has won the game
    user_guess: str = ""
    while turn_num < 7 and win is not True:
        print(f"=== Turn {turn_num}/6 ===")
        user_guess = input_guess(length=int(len(secret)))  # player guesses word
        print(emojified(user_guess, secret))  # prints the visual for the game
        if user_guess == secret:  # user won the game
            win = True
            print(f"You won in {turn_num}/6 turns!")
        else:
            turn_num += 1
            if turn_num >= 7:  # over 6 trys
                print("X/6 - Sorry, try again tomorrow!")  # user lost the game


if __name__ == "__main__":
    main(secret="codes")
