#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    """Water plants with guaranteed cleanup.

    Args:
        plant_list: Tuple of plant names to water

    Note:
        Cleanup always happens via finally block
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError
            print(f"Watering {plant} ")
    except ValueError:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    water_plants(("tomato", "lettuce", "carrots"))
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(("tomato", None, "carrots"))


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
