#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height = height
            print(f"Height updated: {height}cm [OK]")

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age{new_age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_info(self):
        print(f"{self.name}: {self.height}cm {self.age} days old")

    def grow(self):
        self.height = self.height + 1
        self.age = self.age + 1


if __name__ == "__main__":
    plants_data = [
        ("rose", 25, 30),
        ("sunflower", 80, 45),
        ("cactus", 15, 120),
        ("orchid", 18, 60),
        ("bamboo", 150, 200)
        ]
    plants = []
    for name, height, age in plants_data:
        plant = SecurePlant(name, height, age)
        plants.append(plant)
    print("=== Garden Security System ===")
    for plant in plants:
        print("Created:", plant.name)
        plant.set_height(-5)
        plant.set_age(-5)
        plant.set_height(25)
        plant.set_age(30)

    print(f"Total plants created: {len(plants)}")
