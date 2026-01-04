#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        return (f"{self.name}: {self.height}cm {self.age} days old")

    def grow(self):
        self.height = self.height + 1
        self.age = self.age + 1


if __name__ == "__main__":
    # Centralisation des valeurs initiales
    plant_data = [
        ("rose", 25, 30),
        ("sunflower", 80, 45),
        ("cactus", 15, 120),
        ("orchid", 18, 60),
        ("bamboo", 150, 200)
        ]
    # Création automatique des plantes
    plants = {
        name: Plant(name, height, age) for name, height, age in plant_data
        }
    print("=== Day 1 ===")
    for plant in plants.values():
        print(plant.get_info())
    # Faire pousser pendant 6 jours
    for _ in range(6):
        for plant in plants.values():
            plant.grow()
    print("=== Day 7 ===")
    for plant in plants.values():
        plant.get_info()
