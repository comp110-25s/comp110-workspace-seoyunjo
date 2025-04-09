"""plan a cozy tea party"""

__author__: str = "730760820"


def main_planner(guests: int) -> None:
    """entrypoint for orchestrating the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(2 * guests))
    print("Treats: " + str(int(tea_bags(guests) * 1.5)))
    print("Cost: " + "$" + str(2 * guests * 0.5 + tea_bags(guests) * 1.5 * 0.75))


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags needed for the tea party"""
    return 2 * people


def treats(people: int) -> int:
    """Calculate the number of treats needed for the tea party"""
    return int((tea_bags(people=people) * 1.5))


def cost(tea_count: int, treat_count: int) -> float:
    """cost to purchase teas and treats"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
