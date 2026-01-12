#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        return (f"{self.name} ({self.height}cm, {self.age} days)")

    def grow(self):
        self.height = self.height + 1
        self.age = self.age + 1


if __name__ == "__main__":

    plants_data = [
        ("rose", 25, 30),
        ("oak", 200, 365),
        ("cactus", 5, 90),
        ("sunflower", 80, 45),
        ("Fern", 15, 120)
        ]

    plants = {
        name: Plant(name, height, age) for name, height, age in plants_data
        }

    print("=== Plant Factory Output ===")

    for plant in plants.values():
        print("Created:", plant.get_info())

    print(f"\nTotal plants created: {len(plants)}")
