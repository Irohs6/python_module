#!/usr/bin/env python3

class Plant:
    def __init__(self, name:str, height:int):
        self.name = name.capitalize()
        self.height = height
        self.grow_count = 0

    def grow(self):
        self.height += 1
        self.grow_count += 1
        print(f"{self.name} grew 1cm.")

    def get_info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name:str, height:int, color:str):
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def bloom(self):
        self.blooming = False

    def get_info(self):
        state = "blooming" if self.blooming else "not blooming"
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers ({state})"

class PrizePlant(FloweringPlant):
    def __init__(self, name, height, color, score:int):
        super().__init__(name, height, color)
        self.score = score

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.score}"
    

class GardenManager:
    def __init__(self, owner: str, plants: list[Plant] = None):
        self.owner = owner.capitalize()
        if plants is None:
            plants = []
        self.plants = plants

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        return f"Added {plant.name} to {self.owner}'s garden"

    def help_grow(self):
        print(f"{self.owner} is helping all plants grow ...")
        for plant in self.plants:
            plant.grow()
    
    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print(f"PLants in garden")
        for plant in self.plants:
            print(f"{plant.get_info()}")
        print(f"Plant added: {len.plants}, Total growth {self.GardenStat.total_growth} cm")
        print(f"PLant types: {self.GardenStat.count_type}")

    class GardenStat():

        @staticmethod
        def total_growth(plants):
            total_grow = 0
            for plant in plants:
                total_grow = total_grow + plant.grow_count
            return total_grow
        
        def count_type(plants):
            nb_plant = 0
            nb_flower_plant = 0
            nb_prize_plant = 0
            for plant in plants:
                if isinstance(plant, PrizePlant):
                    nb_prize_plant += 1
                elif isinstance(plant, FloweringPlant):
                    nb_flower_plant += 1
                elif isinstance(plant, Plant):
                    nb_plant += 1
            return (f"{nb_flower_plant}, {nb_prize_plant}, {nb_plant}")





if __name__ == "__main__":
    garden = GardenManager("Alice")
    rose = FloweringPlant("rose", 20, "red")
    sunflower = PrizePlant("sunflower", 50, "yellow", 10)

    print(garden.add_plant(rose))     
    print(garden.add_plant(sunflower)) 
    garden.report()


