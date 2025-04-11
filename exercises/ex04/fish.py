"""File to define Fish class."""


class Fish:
    """A Fish in the river ecosystem."""

    def __init__(self):
        """Initialize a new Fish."""
        self.age = 0
        return None

    def one_day(self):
        """Simulate one day for the Fish."""
        self.age += 1
        return None
