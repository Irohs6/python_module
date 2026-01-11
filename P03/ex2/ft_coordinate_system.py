#!/usr/bin/env python3

import sys
import math


def parse_coordinate(args):
    """Parse command line arguments to extract coord."""
    print(f'Parsing coordinates: "{args}"')
    parts = args.split(",")
    if len(parts) != 3:
        print(f"Parsing invalid coordinates: '{args}'")
        print("Error parsing coordinates: expected exactly 3 values (x,y,z)")
        return None
    coords = []
    for part in parts:
        try:
            coords.append(int(part))
        except ValueError as e:
            print(f"Parsing invalid coordinates: '{args}'")
            print(f"Error parsing coordinates: {e}")
            print(f"Error details- Type: {type(e).__name__}, Args: {e.args}")
            return None
    return tuple(coords)


def calcul_distance(positions_one, position_two):
    x1, y1, z1 = positions_one
    x2, y2, z2 = position_two
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return math.sqrt(dx*dx + dy*dy + dz*dz)


def main():
    print("=== Game Coordinate System ===\n")

    if len(sys.argv) == 2:
        pos_one = parse_coordinate(sys.argv[1])
        origin = (0, 0, 0)

        if not pos_one:
            return
        distance = calcul_distance(pos_one, origin)
        print(f"Distance between {pos_one} and {origin}: {distance:.2f}\n")

        print("Unpacking demonstration:")
        x, y, z = pos_one
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}\n")
        return

    if len(sys.argv) == 3:
        pos_one = parse_coordinate(sys.argv[1])
        pos_two = parse_coordinate(sys.argv[2])
        if not pos_one or not pos_two:
            return
        distance = calcul_distance(pos_one, pos_two)
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
