#!/usr/bin/env python3

class GardenError(Exception):
    """Erreur générale liée au jardin."""
    pass


class PlantError(GardenError):
    """Erreur liée à une plante."""
    pass


class WaterError(GardenError):
    """Erreur liée à l'arrosage."""
    pass


class Plant:
    """Représente une plante simple avec un niveau d'eau."""
    def __init__(self, name, water_level=2):
        self.name = name
        self.water_level = water_level

    def water(self, amount):
        if amount <= 0:
            raise WaterError("Water amount must be positive.")
        self.water_level += amount

    def check(self):
        if self.water_level < 3:
            raise PlantError(f"{self.name} is wilting!")
        return True


def demo():
    print("=== Custom Garden Errors Demo ===")

    plant = Plant("Tomato", water_level=1)

    print("Testing PlantError...")
    try:
        plant.check()
    except PlantError as e:
        print("Caught PlantError:", e)

    print("Testing WaterError...")
    try:
        plant.water(-5)
    except WaterError as e:
        print("Caught WaterError:", e)

    print("Testing catching all garden errors...")
    try:
        plant.check()
    except GardenError as e:
        print("Caught a garden error:", e)

    print("All custom error types work correctly!")


if __name__ == "__main__":
    demo()
