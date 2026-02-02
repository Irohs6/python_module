#!/usr/bin/env python3


class Plant:
    """Base plant with name, height, and age."""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a base plant.

        Args:
            name: Plant name.
            height: Height in centimeters.
            age: Age in days.
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self):
        """Return a one-line summary of the plant."""
        return (f"{self.name}: {self.height}cm {self.age} days old")


class Flower(Plant):
    """A flowering plant with a color attribute."""
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a message indicating the plant is blooming."""
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self):
        """Return detailed information including color."""
        return (
            f"{self.name} (Flower): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """A tree with an additional trunk diameter attribute."""
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.diam = trunk_diameter

    def produce_shade(self):
        """Print an estimate of shade area produced by the tree."""
        print(f"{self.name} provides {self.diam * 2} square meters of shade\n")

    def get_info(self):
        """Return detailed information including trunk diameter."""
        return (
            f"{self.name} (Tree): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.diam} cm diameter"
            )


class Vegetable(Plant):
    """An edible plant with harvest season and nutrition info."""
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
        """Return a sentence describing nutritional value."""
        return (
            f"{self.name} is rich in {self.nutri_val}\n"
        )

    def get_info(self):
        """Return detailed information including harvest season."""
        return (
            f"{self.name} (Vegetable): "
            f"{self.height}cm, "
            f"{self.age} days, "
            f"{self.season} harvest"
            )


if __name__ == "__main__":
    rose = Flower("rose", 25, 30, "red")
    tulipe = Flower("Tulipe", 30, 15, "yellow")

    oak = Tree("oak", 300, 100, 75)
    pine = Tree("pin", 400, 80, 50)

    tomato = Vegetable("tomato", 15, 25, "summer", "Vitamin C")
    carrot = Vegetable("carrot", 10, 5, "summer", "Vitamin A")

    print(" === Garden Plant Types === \n")
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
