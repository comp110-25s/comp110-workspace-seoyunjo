"""File to define River class."""

__author__: str = "730760820"


from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """A river ecosystem."""

    def __init__(self, num_fish: int, num_bears: int):
        """Initialize the river."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(num_fish):
            self.fish.append(Fish())
        for _ in range(num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish older than 3 days and Bears older than 5 days."""
        surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish

        surviving_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """If there are at least 5 fish in the river, bears eat 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove Bears with hunger_score less than 0."""
        hungry_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                hungry_bears.append(bear)
        self.bears = hungry_bears
        return None

    def repopulate_fish(self):
        """Add 4 new Fish for every 2 Fish."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Add 1 new Bear for every 2 Bears."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Current population in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()

        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate 7 days in river."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount):
        """Remove Fish from river."""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)
