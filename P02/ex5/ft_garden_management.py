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


class HealthError(GardenError):
    """Plant health-related error."""

    pass


class Plant:
    """Represent a basic plant with growth tracking."""

    def __init__(
        self, name: str, height: int, water_level: int = 5,
            sunlight_hours: int = 6):
        """Initialize a plant.

        Args:
            name: Plant name
            height: Initial height in cm
            water_level: Water level (default 5)
            sunlight_hours: Daily sunlight hours (default 6)
        """
        self.name = name
        self.height = height
        self.water_level = water_level
        self.sunlight = sunlight_hours
        self.grow_count = 0

    def grow(self) -> None:
        """Increase plant height and growth count."""
        self.height += 1
        self.grow_count += 1
        print(f"{self.name} grew 1cm.")

    def get_info(self) -> str:
        """Get plant information string.

        Returns:
            str: Formatted plant information
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Represent a flowering plant with color."""

    def __init__(
        self,
        name: str,
        height: int,
        water_level: int,
        color: str,
        sunlight_hours: int = 6,
    ) -> None:
        """Initialize a flowering plant.

        Args:
            name: Plant name
            height: Initial height in cm
            water_level: Water level
            color: Flower color
            sunlight_hours: Daily sunlight hours (default 6)
        """
        super().__init__(name, height, water_level, sunlight_hours)
        self.color = color
        self.blooming = True

    def get_info(self) -> str:
        """Get flowering plant information with color.

        Returns:
            str: Formatted plant info with flower details
        """
        state = "blooming"
        base_info = super().get_info()
        return f"{base_info}, {self.color} flowers ({state})"


class PrizeFlower(FloweringPlant):
    """Represent a prize-winning flowering plant."""

    def __init__(
        self, name: str, height: int, water_level: int, color: str, score: int,
            sunlight_hours: int = 6) -> None:
        """Initialize a prize flower.

        Args:
            name: Plant name
            height: Initial height in cm
            water_level: Water level
            color: Flower color
            score: Prize score
            sunlight_hours: Daily sunlight hours (default 6)
        """
        super().__init__(name, height, water_level, color, sunlight_hours)
        self.score = score

    def get_info(self) -> str:
        """Get prize flower information with score.

        Returns:
            str: Formatted info with prize points
        """
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.score}"


class GardenManager:
    """Manage a garden with plants and operations."""

    def __init__(self, owner: str, water_tank: int = 100,
                 plants: list[Plant] = None) -> None:
        """Initialize garden manager.

        Args:
            owner: Garden owner name
            water_tank: Water tank capacity (default 100)
            plants: Initial plant list (default None)
        """
        self.owner = owner
        self.water_tank = water_tank
        if plants is None:
            plants = []
        self.plants = plants

    def add_plant(self, plant: Plant) -> str | PlantError:
        """Add a plant to the garden.

        Args:
            plant: Plant to add

        Returns:
            str: Success message or error message

        Raises:
            PlantError: If plant name is empty
        """
        try:
            if not plant.name:
                raise PlantError("Error adding plant:" " Plant name cannot"
                                 " be empty!")
            self.plants.append(plant)
            return f"Added {plant.name} successfully"
        except PlantError as e:
            return e

    def help_grow(self) -> None:
        """Help all plants in the garden grow."""
        print(f"{self.owner} is helping all plants grow ...")
        for plant in self.plants:
            plant.grow()

    def report(self) -> None:
        """Generate and print garden report."""
        added = len(self.plants)
        growth = self.GardenStat.total_growth(self.plants)
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden")
        for plant in self.plants:
            print(f"{plant.get_info()}")
        print(f"Plant added: {added}, Total growth: {growth}cm")
        print(f"Plant types: {self.GardenStat.count_type(self.plants)}")

    def water_plant(self) -> None:
        """Water all plants with cleanup guarantee.

        Raises:
            WaterError: If water tank is depleted
        """
        try:
            if self.water_tank < 5:
                raise WaterError("Not enough water in tank")
            print("Watering plants...")
            print("Opening watering system")
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Error: Cannot water None" " "
                                     "- invalid plant!")
                print(f"Watering {plant.name} - success")
                if self.water_tank < 5:
                    raise WaterError("Not enough water in tank")
                self.water_tank -= 5
        except WaterError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)\n")

    @staticmethod
    def check_plant_health(plant: Plant) -> str:
        """Check if plant health parameters are valid.

        Args:
            plant: Plant to check

        Returns:
            str: Health status message

        Raises:
            HealthError: If any parameter is invalid
        """
        if not plant.name:
            raise HealthError("Error: Plant name cannot be empty!")
        if plant.water_level < 1:
            raise HealthError(
                f"Error: Water level {plant.water_level}" " is too low (min 1)"
            )
        if plant.water_level > 10:
            raise HealthError(
                f"Error checking {plant.name}: Water level"
                f" {plant.water_level} is too high (max 10)"
            )
        if plant.sunlight < 2:
            raise HealthError(
                f"Error: Sunlight hours {plant.sunlight}" " is too low (min 2)"
            )
        if plant.sunlight > 12:
            raise HealthError(
                f"Error: Sunlight hours {plant.sunlight}" ""
                " is too high (max 12)"
            )
        return (
            f"{plant.name}: healthy (water: {plant.water_level},"
            f" sun: {plant.sunlight})"
        )

    @staticmethod
    def validate_height(value: int) -> bool:
        """Validate if height value is non-negative.

        Args:
            value: Height value to validate

        Returns:
            bool: True if valid
        """
        return value >= 0

    @classmethod
    def create_garden_network(cls, owners: list[str]
                              ) -> list["GardenManager"]:
        """Create multiple gardens for different owners.

        Args:
            owners: List of owner names

        Returns:
            list: List of GardenManager instances
        """
        return [cls(owner) for owner in owners]

    class GardenStat:
        """Garden statistics calculation utilities."""

        @staticmethod
        def total_growth(plants: list[Plant]) -> int:
            """Calculate total growth of all plants.

            Args:
                plants: List of plants

            Returns:
                int: Total growth in cm
            """
            total_grow = 0
            for plant in plants:
                total_grow = total_grow + plant.grow_count
            return total_grow

        @staticmethod
        def count_type(plants: list[Plant]) -> str:
            """Count different types of plants.

            Args:
                plants: List of plants

            Returns:
                str: Formatted count of plant types
            """
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


def test_garden_management() -> None:
    """Test garden management system with error handling and recovery."""
    print("=== Garden Management System ===\n")

    # Create garden with low water to demonstrate recovery
    alice = GardenManager("Alice", 15)

    # Test 1: Adding plants
    print("Adding plants to garden...")
    tomato = Plant("tomato", 100)
    lettuce = FloweringPlant("lettuce", 25, 15, "red")
    invalid_plant = Plant("", 50)

    print(alice.add_plant(tomato))
    print(alice.add_plant(lettuce))
    print(alice.add_plant(invalid_plant))
    print()
    # Test 2: Watering plants (with cleanup)
    alice.water_plant()

    # Test 3: Check plant health
    print("Checking plant health...")
    for plant in alice.plants:
        try:
            status = alice.check_plant_health(plant)
            print(status)
        except HealthError as e:
            print(e)
    print()
    # Test 4: Error recovery demonstration
    print("Testing error recovery...")
    alice.water_tank = 0  # Force water shortage
    alice.water_plant()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
