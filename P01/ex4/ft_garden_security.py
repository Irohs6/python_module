#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.__height = height
        self.__age = age

    def get_height(self):
        return self.height

    def set_height(self, height):
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_info(self):
        return (f"{self.name} ({self.__height}cm, {self.__age} days)")

    def grow(self):
        self.__height = self.__height + 1
        self.__age = self.__age + 1


if __name__ == "__main__":
    plants_data = [
        ("rose", 25, 30),
        ("sunflower", 80, 45),
        ("cactus", 15, 120),
        ("orchid", 18, 60),
        ("bamboo", 150, 200)
        ]

    plants = {
        name: SecurePlant(name, height, age)
        for name, height, age in plants_data
        }

    print("=== Garden Security System ===")

    for plant in plants.values():
        print("Created:", plant.name)
        plant.set_height(-5)
        plant.set_age(-5)
        plant.set_height(25)
        plant.set_age(30)
        print("\n")

    for plant in plants.values():
        print(f"Curent plant: {plant.get_info()}")
