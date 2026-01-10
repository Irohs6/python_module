#!/usr/bin/env python3

class GardenError(Exception):
    """General garden-related error."""
    pass


class PlantError(GardenError):
    """Plant-related error."""
    pass


class WaterError(GardenError):
    """Watering-related error."""
    pass


class Plant:
    """Represent a simple plant with a water level."""
    def __init__(self, name, water_level=2):
        self.name = name
        self.water_level = water_level

    def water(self, amount):
        """Add water to the plant.

        Args:
            amount: Amount of water to add

        Raises:
            WaterError: If amount is not positive
        """
        if amount <= 0:
            raise WaterError("Water amount must be positive.")
        self.water_level += amount

    def check(self):
        """Check if plant has sufficient water.

        Returns:
            bool: True if plant is healthy

        Raises:
            PlantError: If plant is wilting
        """
        if self.water_level < 3:
            raise PlantError(f"{self.name} is wilting!")
        return True


def demo():
    """Demonstrate custom garden errors."""
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
