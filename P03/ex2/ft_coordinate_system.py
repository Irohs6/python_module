#!/usr/bin/env python3

import sys
import math


def parse_coordinate(args: list[str]) -> tuple[int, ...] | None:
    """Parse command line arguments to extract 3D coordinates.

    Converts a string in format 'x,y,z' into a tuple of three integers
    representing a 3D position in game space.

    Args:
        args: String containing coordinates in format 'x,y,z'
              where x, y, z are integers.

    Returns:
        tuple[int, int, int]: A tuple containing (x, y, z) coordinates
                              if parsing succeeds.
        None: If the string format is invalid or values cannot be
              converted to integers."""

    print(f'Parsing coordinates: "{args}"')
    parts: list[str] = args.split(",")
    if len(parts) != 3:
        print(f"Parsing invalid coordinates: '{args}'")
        print("Error parsing coordinates: expected exactly 3 values (x,y,z)")
        return None
    coords: list[int] = []
    for part in parts:
        try:
            coords.append(int(part))
        except ValueError as e:
            print(f"Parsing invalid coordinates: '{args}'")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details- Type: {type(e).__name__}, Args: {e.args}")
            return None
    return tuple(coords)


def calcul_distance(
    positions_one: tuple[int, ...],
        position_two: tuple[int, ...]) -> float:
    """Calculate the 3D Euclidean distance between two points.

    Uses the 3D distance formula:
    distance = sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)

    This is the extension of the Pythagorean theorem to 3D space.

    Args:
        positions_one: First 3D coordinate as tuple (x1, y1, z1).
        position_two: Second 3D coordinate as tuple (x2, y2, z2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    x1, y1, z1 = positions_one
    x2, y2, z2 = position_two
    dx: int = x2 - x1
    dy: int = y2 - y1
    dz: int = z2 - z1
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def main():
    """Main function for the 3D coordinate system demonstration.

    Processes command line arguments to:
    - Calculate distance from a point to origin (1 argument)
    - Calculate distance between two points (2 arguments)
    - Display usage information (no arguments)

    Command line usage:
        python3 ft_coordinate_system.py x,y,z
        python3 ft_coordinate_system.py x1,y1,z1 x2,y2,z2

    Also demonstrates tuple unpacking by extracting x, y, z values
    from parsed coordinates.
    """
    print("=== Game Coordinate System ===\n")

    if len(sys.argv) == 2:
        pos_one: tuple[int, int, int] | None = parse_coordinate(sys.argv[1])
        origin: tuple[int, int, int] = (0, 0, 0)
        if not pos_one:
            return
        print(f"Parsed position: {pos_one}")
        distance: float = calcul_distance(pos_one, origin)
        print(f"Distance between {origin} and {pos_one}: {distance:.2f}\n")

        print("Unpacking demonstration:")
        x: int
        y: int
        z: int
        x, y, z = pos_one
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}\n")
        return

    if len(sys.argv) == 3:
        pos_one: tuple[int, int, int] | None = parse_coordinate(sys.argv[1])
        pos_two: tuple[int, int, int] | None = parse_coordinate(sys.argv[2])
        if not pos_one or not pos_two:
            return
        distance: float = calcul_distance(pos_one, pos_two)
        print(f"Distance between {pos_one} and {pos_two}: {distance:.2f}\n")

        print("Unpacking demonstration:")

        x, y, z = pos_one
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}\n")
        return

    print("Usage:")
    print(" python3 ft_coordinate_system.py x,y,z")
    print(" python3 ft_coordinate_system.py x1,y1,z1 x2,y2,z2")


if __name__ == "__main__":
    main()
