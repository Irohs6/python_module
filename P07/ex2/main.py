#!/usr/bin/env python3
"""Exercise 2: Ability System - Demonstration script."""

from ex2.EliteCard import EliteCard


def main() -> None:
    """Demonstrate the Ability System with multiple interfaces."""
    try:
        print("=== DataDeck Ability System ===\n")

        from ex0.Card import Card
        from ex2.Combatable import Combatable
        from ex2.Magical import Magical

        interfaces = {
            "Card": Card,
            "Combatable": Combatable,
            "Magical": Magical,
        }

        print("EliteCard capabilities:")
        for name, cls in interfaces.items():
            methods = [
                m
                for m, v in cls.__dict__.items()
                if not m.startswith("_") and callable(v)
            ]
            print(f"- {name}: {methods}")

        warrior = EliteCard("Arcane Warrior", 6, "Legendary", 5, 3, 8)

        print(f"\nPlaying {warrior.name} (Elite Card):")
        warrior.play({"mana": 2})

        print("\nCombat phase:")
        attack_result = warrior.attack("Enemy")
        print(f"Attack result: {attack_result}")

        defense_result = warrior.defend(5)
        print(f"Defense result: {defense_result}")

        print("\nMagic phase:")
        spell_result = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
        print(f"Spell cast: {spell_result}")

        mana_result = warrior.channel_mana(3)
        print(f"Mana channel: {mana_result}")

        print("\nMultiple interface implementation successful!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
