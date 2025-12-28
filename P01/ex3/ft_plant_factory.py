#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm {self.age} days old")

    def grow(self):
        self.height = self.height + 1
        self.age = self.age + 1


if __name__ == "__main__":
    # Centralisation des valeurs initiales
    plants_data = [
        ("rose", 25, 30),
        ("sunflower", 80, 45),
        ("cactus", 15, 120),
        ("orchid", 18, 60),
        ("bamboo", 150, 200)
        ]
    # Création automatique des plantes
    plants = []
    for name, height, age in plants_data:
        plant = Plant(name, height, age)
        plants.append(plant)
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=" ")
        plant.get_info()
    print(f"Total plants created: {len(plants)}")
