"""File to run a simulation."""

from exercises.EX04.river import River


def run_simulation(num_days):
    """Run the river ecosystem simulation."""
    river = River(num_fish=10, num_bears=2)

    for day in range(1, num_days + 1):
        print(f"~~~Day {day}~~~")
        river.one_river_day()
