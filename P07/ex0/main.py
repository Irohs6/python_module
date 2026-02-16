#!/usr/bin/env python3
"""Exercise 0: Card Foundation - Demonstration script."""

from ex0.CreatureCard import CreatureCard


def main() -> None:
    """Demonstrate the Card Foundation with abstract base classes."""
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    result = dragon.play({'mana': 6})
    print(f"Play result: {result}")

    goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
    print(f"\nFire Dragon attacks {goblin.name}:")
    attack_result = dragon.attack_target(goblin)
    print(f"Attack result: {attack_result}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
