#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None:
    """Check if a temperature is appropriate for plants.
    Args:
        temp_str: String representing a temperature value
    Returns:
        None: Prints the verification result
    """
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature_input() -> None:
    temp_str: str = input("Enter a temperature")
    check_temperature(temp_str)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")

    test_temperature_input()

    print("All tests completed - program didn't crash!")
