#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        return (f"{self.name}: {self.height}cm {self.age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return (
            f"{self.name} (Flower): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.diam = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {self.diam * 2} square meters of shade")

    def get_info(self):
        return (
            f"{self.name} (Tree): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.diam} cm diameter"
            )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ):
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutri_val = nutritional_value

    def get_nutri(self):
        return (
            f"{self.name} is rich in {self.nutri_val}"
        )

    def get_info(self):
        return (
            f"{self.name} (Vegetable):"
            f"{self.height}cm,"
            f"{self.age} days,"
            f"{self.season} harvest"
            )


if __name__ == "__main__":
    rose = Flower("rose", 25, 30, "red")
    tulipe = Flower("Tulipe", 30, 15, "Yellow")

    oak = Tree("oak", 300, 100, 75)
    pine = Tree("pin", 400, 80, 50)

    tomato = Vegetable("tomato", 15, 25, "Summer", "Vitamin C")
    carrot = Vegetable("carrot", 10, 5, "Summer", "Vitamin A")
    print(" === Garden Plant Types === ")
    print(rose.get_info())
    rose.bloom()
    print(tulipe.get_info())
    tulipe.bloom()

    print(oak.get_info())
    oak.produce_shade()
    print(pine.get_info())
    pine.produce_shade()

    print(tomato.get_info())
    print(tomato.get_nutri())
    print(carrot.get_info())
    print(carrot.get_nutri())
