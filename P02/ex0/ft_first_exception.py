#!/usr/bin/env python3

def check_temperature(temp_str):
    """Check if a temperature is appropriate for plants.

    Args:
        temp_str: String representing a temperature value

    Returns:
        None: Prints the verification result
    """
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp}' is not a valid number")
    else:
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")

    tests = ["25", "abc", "100", "-50"]

    for t in tests:
        print(f"Testing temperature: {t}")
        check_temperature(t)

    print("All tests completed - program didn't crash!")
