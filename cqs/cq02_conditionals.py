"""A challange question using conditionals"""

__author__ = "730735704"


def guess_a_number() -> None:
    """Compares an input number to a secret number"""
    secret: int = 7  # defines the secret number
    x: str = input("Guess a number:")  # x is the input/guessed number
    print("Your guess was " + x)
    if int(x) == secret:  # guess is correct
        print("You got it!")
    elif int(x) < secret:  # guess too low
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # guess too high
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    """calls the guess_a_number function"""
    guess_a_number()
