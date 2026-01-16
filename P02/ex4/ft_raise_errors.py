#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Validate plant health parameters.

    Args:
        plant_name: Name of the plant
        water_level: Water level (1-10)
        sunlight_hours: Sunlight hours (2-12)

    Returns:
        str: Success message if all parameters are valid

    Raises:
        ValueError: If any parameter is invalid
    """
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test plant health validation with various inputs."""
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 4, 5))
    except ValueError as e:
        print(e)

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 5, 6))
    except ValueError as e:
        print(e)

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 5))
    except ValueError as e:
        print(e)

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0))
    except ValueError as e:
        print(e)

    print("All error raising tests completed")


if __name__ == "__main__":
    test_plant_checks()
