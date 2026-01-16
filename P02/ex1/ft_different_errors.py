#!/usr/bin/env python3

def test_error_type():
    """Test different common Python error types.

    Demonstrates handling of ValueError, ZeroDivisionError,
    FileNotFoundError and KeyError.
    """
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

        print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

        print("Testing FileNotFoundError...")
    try:
        open("file.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

        print("Testing KeyError...")
    try:
        test: str = {"rose": 1}
        print(test["tulipe"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

        print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def garden_operation():
    """Demonstrate handling of different error types in garden context."""
    print("=== Garden Error Types Demo ===")
    test_error_type()
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operation()
