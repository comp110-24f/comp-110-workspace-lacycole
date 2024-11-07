"""File to define Fish class."""

__author__ = "730735704"


class Fish:
    """Defines a class for fish."""

    age: int

    def __init__(self):
        """New fish with age 0."""
        self.age = 0
        return None

    def one_day(self):
        """Tracks age changes for one day."""
        self.age += 1  # adds one to age each day
        return None
