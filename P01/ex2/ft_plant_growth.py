#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm {self.age} days old")

    def grow(self):
        


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.get_info()
    sunflower.get_info()
    cactus.get_info()
