#!/usr/bin/env python3


class Plant:
    """Basic plant with name and height, supporting growth."""
    def __init__(self, name: str, height: int):
        """Initialize a plant with a name and height in cm."""
        self.name = name.capitalize()
        self.height = height
        self.grow_count = 0

    def grow(self):
        """Increase height by 1cm and record the growth event."""
        self.height += 1
        self.grow_count += 1
        print(f"{self.name} grew 1cm.")

    def get_info(self):
        """Return a one-line summary of the plant height."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that produces flowers with a given color."""
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        """Return info string including color and blooming state."""
        state = "blooming"
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers ({state})"


class PrizeFlower(FloweringPlant):
    """A flowering plant with an additional prize score."""
    def __init__(self, name, height, color, score: int):
        super().__init__(name, height, color)
        self.score = score

    def get_info(self):
        """Return info string including prize points."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.score}"


class GardenManager:
    """Manage a collection of plants owned by a person."""
    def __init__(self, owner: str, plants: list[Plant] = None):
        """Initialize a garden manager.

        Args:
            owner: Owner's name.
            plants: Optional initial list of plants.
        """
        self.owner = owner.capitalize()
        if plants is None:
            plants = []
        self.plants = plants

    def add_plant(self, plant: Plant):
        """Add a plant to the garden and return a confirmation."""
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def help_grow(self):
        """Trigger a growth step for all plants in the garden."""
        print(f"{self.owner} is helping all plants grow ...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        """Print a summary report for the current garden state."""
        added = len(self.plants)
        growth = self.GardenStat.total_growth(self.plants)
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            print(f"- {plant.get_info()}")

        print(f"\nPlant added: {added}, Total growth: {growth}cm")
        print(f"Plant types: {self.GardenStat.count_type(self.plants)}")

    @staticmethod
    def validate_height(value: int) -> bool:
        """Return True if the height value is non-negative."""
        return value >= 0

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        """Create a list of garden managers for the provided owners."""
        return [cls(owner) for owner in owners]

    class GardenStat():
        """Utility functions for analyzing collections of plants."""

        @staticmethod
        def total_growth(plants):
            """Sum the number of recorded growth events across plants."""
            total_grow = 0

            for plant in plants:
                total_grow = total_grow + plant.grow_count
            return total_grow

        @staticmethod
        def total_score(plants):
            """Sum prize scores across plants that have one."""
            total_score = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    total_score = total_score + plant.score
            return total_score

        @staticmethod
        def count_type(plants):
            """Count the number of plants by type in a readable string."""
            nb_plant = 0
            nb_flower_plant = 0
            nb_prize_plant = 0

            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    nb_prize_plant += 1
                elif isinstance(plant, FloweringPlant):
                    nb_flower_plant += 1
                elif isinstance(plant, Plant):
                    nb_plant += 1
            return (
                f"{nb_plant} regular, "
                f"{nb_flower_plant} flowering, "
                f"{nb_prize_plant} prize flowers"
                )


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("rose", 25, "red")
    sunflower = PrizeFlower("sunflower", 50, "yellow", 10)

    print(alice.add_plant(oak))
    print(alice.add_plant(rose))
    print(alice.add_plant(sunflower))
    print("\n")

    alice.help_grow()
    print("\n")
    alice.report()
    print("\n")

    print("Height validation test:", GardenManager.validate_height(10))

    print(f"Garden scores "
          f"- Alice: {alice.GardenStat.total_score(alice.plants)},"
          f" Bob: {bob.GardenStat.total_score(bob.plants)}")

    print(f"Total gardens managed: {len(gardens)}")
