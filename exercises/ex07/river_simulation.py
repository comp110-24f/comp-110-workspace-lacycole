"""File to simulate river."""

__author__ = "730735704"

from exercises.ex07.river import River

my_river: River = River(10, 2)  # creates a new river with 10 fish and 2 bears
my_river.one_river_week()  # simulates one week of the river
