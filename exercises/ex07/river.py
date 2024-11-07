"""File to define River class."""

__author__ = "730735704"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines a class for river."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        for _ in range(0, num_fish):  # populate the river with fish
            self.fish.append(Fish())
        for _ in range(0, num_bears):  # populate the river with bears
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of all fish and bears in the river."""
        current_fish: list[Fish] = self.fish  # fish list to be modified
        current_bears: list[Bear] = self.bears  # bear list to be modified
        current_idx: int = 0  # current idx of the cycle
        for fish in self.fish:
            if fish.age > 3:  # checks if fish age is over three
                current_fish.pop(current_idx)  # removes fish that are too old
            else:
                current_idx += 1  # moves index forward
            self.fish = current_fish  # assigns self.fish to modified list
        current_idx = 0  # resets current idx of cycle
        for bear in self.bears:
            if bear.age > 5:  # checks if bear age is over five
                current_bears.pop(current_idx)  # removes bears that are too old
            else:
                current_idx += 1  # moves index forward
            self.bears = current_bears  # assigns self.bear to modified list
        return None

    def remove_fish(self, amount: int):
        """Removes amount of fish from the front of the list."""
        remove_amount: int = amount  # number of fish to remove
        remaining_fish: list[Fish] = self.fish  # list to modify
        while remove_amount > 0:
            remaining_fish.pop(0)  # removes first fish of the list
            remove_amount -= 1  # tracks amount of fish left to remove
        return None

    def bears_eating(self):
        """Bears eat 3 fish is there are more than 5 fish."""
        for bear in self.bears:  # goes through each bear in the river
            if len(self.fish) >= 5:  # checks if there are at least 5 fish
                self.remove_fish(3)  # removes 3 fish
                bear.eat(3)  # bear eats three fish
        return None

    def check_hunger(self):
        """Removes bears from the river if they starve."""
        remaining_bears: list[Bear] = self.bears  # list to modify
        current_idx: int = 0  # current index of cycle
        for bear in self.bears:
            if bear.hunger_score < 0:  # if the bear starves
                remaining_bears.pop(current_idx)  # remove the bear
            else:
                current_idx += 1  # moves index forward
            self.bears = remaining_bears  # assigns self.bears to remaining bears
        return None

    def repopulate_fish(self):
        """Adds 4 fish for each pair of fish."""
        amount_fish: float = len(self.fish)  # finds amount of fish in river
        if amount_fish % 2 == 1:  # checks if there is an uneven amount of fish
            amount_fish -= 1  # makes amount of fish even
        fish_pairs: float = amount_fish / 2  # finds number of fish pairs
        while fish_pairs > 0:
            idx: int = 4  # amount of fish to add
            while idx > 0:
                self.fish.append(Fish())  # adds another fish to the river
                idx -= 1  # tracks amount of fish left to add
            fish_pairs -= 1  # tracks amount of pairs left to go through
        return None

    def repopulate_bears(self):
        """Adds 1 bear for each pair of bears."""
        amount_bears: float = len(self.bears)  # finds amount of bears in river
        if amount_bears % 2 == 1:  # checks if there is an uneven amount of bears
            amount_bears -= 1  # makes amount of bears even
        bear_pairs: float = amount_bears / 2  # finds number of bear pairs
        while bear_pairs > 0:
            self.bears.append(Bear())  # adds another bear to the river
            bear_pairs -= 1  # trakcs amount of pairs left to go through
        return None

    def view_river(self):
        """Prints day and number of fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")  # prints the day
        print(f"Fish population: {len(self.fish)}")  # prints the number of fish
        print(f"Bear population: {len(self.bears)}")  # prints the number of bears
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        self.day += 1  # Increase day by 1
        for bear in self.bears:  # Simulate one day for all Bears
            bear.one_day()
        for fish in self.fish:  # Simulate one day for all Fish
            fish.one_day()
        self.bears_eating()  # Simulate Bear's eating
        self.check_hunger()  # Remove hungry Bear's from River
        self.check_ages()  # Remove old Fish and Bear's from River
        self.repopulate_fish()  # Simulate Fish repopulation
        self.repopulate_bears()  # Simulate Bear repopulation
        self.view_river()  # Visualize River

    def one_river_week(self):
        """Calls one_river_day seven times."""
        idx: int = 0
        while idx < 7:  # seven times
            self.one_river_day()  # calls one_river_day
            idx += 1
        return None
