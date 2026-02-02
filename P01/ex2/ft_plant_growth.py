#!/usr/bin/env python3


class Plant:
    """Represent a plant that can grow over time."""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a plant with a name, height, and age.

        Args:
            name: Plant name.
            height: Initial height in centimeters.
            age: Initial age in days.
        """
        self.name = name.capitalize()
        self.height = height
        self.plant_age = age

    def get_info(self):
        """Return a one-line summary of the plant's state."""
        return (f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def age(self):
        """Increase age by one unit."""
        self.plant_age = self.plant_age + 1

    def grow(self):
        """Increase height by one unit."""
        self.height = self.height + 1


if __name__ == "__main__":

    plants_data = [
        ("rose", 25, 30),
        ("sunflower", 80, 45),
        ("cactus", 15, 120),
        ("orchid", 18, 60),
        ("bamboo", 150, 200)
        ]

    plants = {
        name: Plant(name, height, age) for name, height, age in plants_data
        }
    total_grow = 0

    print("=== Day 1 ===")

    for plant in plants.values():
        print(plant.get_info())

    for _ in range(6):
        total_grow += 1
        for plant in plants.values():
            plant.grow()
            plant.age()

    print("=== Day 7 ===")

    for plant in plants.values():
        print(plant.get_info())

    print(f"Growt this week: +{total_grow}cm")
