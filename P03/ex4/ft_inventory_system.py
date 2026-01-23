#!/usr/bin/env python3
"""
Exercise 4: Inventory Master
Demonstrates dictionary usage for game inventory management.
"""

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parse command line arguments in format 'item:quantity'.

    Converts arguments like 'sword:1', 'potion:5' into a dictionary
    mapping item names to their quantities.

    Args:
        args: List of strings in format 'item:quantity'.

    Returns:
        dict[str, int]: Dictionary mapping item names to quantities.
    """
    inventory: dict[str, int] = {}

    for arg in args:
        try:
            if ":" not in arg:
                print(f"Warning: '{arg}' invalid format, expected "
                      f"'item: quantity'")
                continue

            item: str
            qty_str: str
            item, qty_str = arg.split(":", 1)
            quantity: int = int(qty_str)

            if quantity < 0:
                print(f"Warning: negative quantity for '{item}', ignored")
                continue

            inventory[item] = quantity

        except ValueError:
            print(f"Warning: '{arg}' has invalid quantity, ignored")

    return inventory


def calculate_stats(inventory: dict[str, int]) -> dict:
    """Calculate inventory statistics.

    Args:
        inventory: Dictionary mapping item names to quantities.

    Returns:
        dict: Statistics including total, unique count, most/least abundant.
    """
    total_items: int = sum(inventory.values())
    unique_types: int = len(inventory.keys())

    most_item: str = max(inventory, key=inventory.get)
    least_item: str = min(inventory, key=inventory.get)

    return {
        "total": total_items,
        "unique": unique_types,
        "most": (most_item, inventory[most_item]),
        "least": (least_item, inventory[least_item]),
    }


def categorize_items(inventory: dict[str, int]) -> dict[str, dict[str, int]]:
    """Categorize items by abundance level.

    Categories:
    - Abundant: 4+ units
    - Moderate: 2-3 units
    - Scarce: 1 unit

    Args:
        inventory: Dictionary mapping item names to quantities.

    Returns:
        dict: Nested dictionary with categories as keys.
    """
    categories: dict[str, dict[str, int]] = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {},
    }

    for item, qty in inventory.items():
        if qty >= 4:
            categories["Abundant"][item] = qty
        elif qty >= 2:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty

    return categories


def get_restock_suggestions(inventory: dict[str, int]) -> list[str]:
    """Get list of items that need restocking (quantity = 1).

    Args:
        inventory: Dictionary mapping item names to quantities.

    Returns:
        list[str]: List of item names with quantity of 1.
    """
    return [item for item, qty in inventory.items() if qty <= 1]


def calculate_percentages(inventory: dict[str, int]) -> dict[str, float]:
    """Calculate percentage of each item in total inventory.

    Args:
        inventory: Dictionary mapping item names to quantities.

    Returns:
        dict[str, float]: Dictionary mapping items to their percentages.
    """
    total: int = sum(inventory.values())
    return {item: (qty / total * 100) for item, qty in inventory.items()}


def print_inventory_report(inventory: dict[str, int]) -> None:
    """Display complete inventory analysis report.

    Args:
        inventory: Dictionary mapping item names to quantities.
    """
    stats: dict = calculate_stats(inventory)
    categories: dict[str, dict[str, int]] = categorize_items(inventory)
    restock: list[str] = get_restock_suggestions(inventory)
    percentages: dict[str, float] = calculate_percentages(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {stats['total']}")
    print(f"Unique item types: {stats['unique']}\n")

    print("=== Current Inventory ===")
    sorted_inv: list[tuple[str, int]] = sorted(
        inventory.items(), key=lambda x: x[1], reverse=True
    )

    for item, qty in sorted_inv:
        unit: str = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percentages[item]:.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {stats['most'][0]} ({stats['most'][1]} units)")

    least_unit: str = "unit" if stats["least"][1] == 1 else "units"
    print(f"Least abundant: {stats['least'][0]} ({stats['least'][1]} "
          f"{least_unit})")

    print("\n=== Item Categories ===")
    for category, items in categories.items():
        if items:
            print(f"{category}: {items}")

    print("\n=== Management Suggestions ===")
    if restock:
        print(f"Restock needed: {restock}")
    else:
        print("No items need restocking")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup- 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    """Main function to process inventory from command line arguments."""
    args: list[str] = sys.argv[1:]

    if not args:
        print("=== Inventory System Analysis ===")
        print(
            "No items provided. Usage: python3 ft_inventory_system.py "
            "item1:qty1 item2:qty2 ..."
        )
        sys.exit(0)

    inventory: dict[str, int] = parse_inventory(args)

    if not inventory:
        print("No valid items found!")
        sys.exit(0)

    print_inventory_report(inventory)


if __name__ == "__main__":
    main()
