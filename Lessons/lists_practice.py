"""Basic syntax of lists."""

my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)

my_numbers.append(1.5)
my_numbers.append(2.3)

print(my_numbers)

game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying Elements
game_points[1] = 72
print(game_points)

# getting the length
print(len(game_points))

# Remove an element
game_points.pop(1)
print(game_points)

# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points!


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(game_points)
