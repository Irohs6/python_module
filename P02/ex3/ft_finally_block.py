#!/usr/bin/env python3

def water_plant(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception
            print(f"Watering {plant} ")
    except Exception:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plant(("tomato", "letuce", "carrots"))
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plant(("tomato", None, "carrots"))
    print("\nCleanup always happens, even with errors!")
