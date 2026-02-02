#!/usr/bin/env python3


class Plant:
    """Represent a plant with basic attributes.

    Attributes:
        name: Capitalized plant name.
        height: Height in centimeters.
        age: Age in days.
    """
    def __init__(self, name: str, height: int, age: int):
        """Initialize a new plant.

        Args:
            name: Plant name.
            height: Plant height in centimeters.
            age: Plant age in days.
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def print_plant(self):
        """Print the plant information in a human-readable line."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.print_plant()
    sunflower.print_plant()
    cactus.print_plant()
