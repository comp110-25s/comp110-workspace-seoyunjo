"""File to define Bear class."""


class Bear:
    """A Bear in the river ecosystem."""

    def __init__(self):
        """Initialize a new Bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulate one day for the Bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, amount: int):
        """Bear eats fish."""
        self.hunger_score += amount
