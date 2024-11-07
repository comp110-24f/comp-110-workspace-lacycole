"""File to define Bear class."""

__author__ = "730735704"


class Bear:
    """Defines a class for bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """New bear with 0 age and 0 hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Tracks age and hunger changes for one day."""
        self.age += 1  # age goes up one
        self.hunger_score -= 1  # hunger_score goes down one
        return None

    def eat(self, num_fish: int):
        """Changes hunger_score based on how many fish ate."""
        self.hunger_score += num_fish  # adds value of fish ate to hunger_score
        return None
