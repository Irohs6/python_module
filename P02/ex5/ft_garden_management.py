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
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.grow_count = 0

    def grow(self):
        self.height += 1
        self.grow_count += 1
        print(f"{self.name} grew 1cm.")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def get_info(self):
        state = "blooming"
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers ({state})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, score: int):
        super().__init__(name, height, color)
        self.score = score

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.score}"


class GardenManager:
    def __init__(self, owner: str, plants: list[Plant] = None):
        self.owner = owner
        if plants is None:
            plants = []
        self.plants = plants

    def add_plant(self, plant: Plant):
        if not plant.name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def help_grow(self):
        print(f"{self.owner} is helping all plants grow ...")
        for plant in self.plants:
            plant.grow()

    def report(self):
        added = len(self.plants)
        growth = self.GardenStat.total_growth(self.plants)
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden")
        for plant in self.plants:
            print(f"{plant.get_info()}")
        print(f"Plant added: {added}, Total growth: {growth}cm")
        print(f"Plant types: {self.GardenStat.count_type(self.plants)}")

    @staticmethod
    def validate_height(value: int) -> bool:
        return value >= 0

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        return [cls(owner) for owner in owners]

    class GardenStat():

        @staticmethod
        def total_growth(plants):
            total_grow = 0
            for plant in plants:
                total_grow = total_grow + plant.grow_count
            return total_grow

        @staticmethod
        def count_type(plants):
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
    print("=== Garden Management System Demo ===")

    # Création d’un réseau de jardins
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    alice = gardens[0]
    bob = gardens[1]

    # Plantes d’Alice
    oak = Plant(None, 100)
    rose = FloweringPlant("rose", 25, "red")
    sunflower = PrizeFlower("sunflower", 50, "yellow", 10)

    print(alice.add_plant(oak))
    print(alice.add_plant(rose))
    print(alice.add_plant(sunflower))

    # Croissance
    alice.help_grow()

    # Rapport Alice
    alice.report()

    # Test de validation statique
    print("Height validation test:", GardenManager.validate_height(10))

    # Score des jardins (exemple simple)
    print("Garden scores")
    print(f"- Alice: {alice.GardenStat.total_growth(alice.plants) * 10}")
    print(f"- Bob: {bob.GardenStat.total_growth(bob.plants) * 10}")

    print(f"Total gardens managed: {len(gardens)}")
