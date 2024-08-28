"""My first challenge question in COMP110"""

__author__ = "730735704"


def mimic(message: str) -> str:
    """Return message."""
    return message


def main() -> None:
    """Print the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
