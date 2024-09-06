"""Using functions to calculate the price of a tea party"""

__author__ = "730735704"


def main_planner(guests: int) -> None:
    """Entrypoint of the program to calculate the cost of the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )  # calls cost which then calls tea_bags and treats
    )  # saving automatically formated it this way - likely for clarity


def tea_bags(people: int) -> int:
    """Computes the number of tea bags to have 2 per person"""
    return 2 * people


def treats(people: int) -> int:
    """Computes the number of treats by multiplying the number of tea bags by 1.5"""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of treats and tea bags combined"""
    return (
        tea_count * 0.5 + treat_count * 0.75
    )  # tea_count and treat_count will use tea_bags and treats in main_planner


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """Allows an imput for number of guests and then the rest of the program runs."""
