#!/usr/bin/env python3


class SecurePlant:
    """Plant with private attributes and validated updates.

    Attributes are stored privately and can be updated via setter
    methods that perform basic validation.
    """
    def __init__(self, name: str, height: int, age: int):
        """Initialize a secure plant with name, height, and age.

        Args:
            name: Plant name.
            height: Initial height in centimeters.
            age: Initial age in days.
        """
        self.name = name.capitalize()
        self.__height = height
        self.__age = age

    def get_height(self):
        """Return the current height in centimeters."""
        return self.height

    def set_height(self, height):
        """Set the height if valid; log rejection otherwise.

        Args:
            height: New height in centimeters (must be non-negative).
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def get_age(self):
        """Return the current age in days."""
        return self.age

    def set_age(self, new_age):
        """Set the age if valid; log rejection otherwise.

        Args:
            new_age: New age in days (must be non-negative).
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")

    def get_info(self):
        """Return a compact description of the plant's current state."""
        return (f"{self.name} ({self.__height}cm, {self.__age} days)")

    def grow(self):
        """Increase height and age by one unit each (cm/day)."""
        self.__height = self.__height + 1
        self.__age = self.__age + 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("rose", 15, 25)
    print("Created:", rose.name)
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-5)
    rose.set_age(-5)

    print("\n")

    print(f"Curent plant: {rose.get_info()}")
