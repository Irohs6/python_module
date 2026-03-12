#!/usr/bin/env python3
"""Exercise 1: Deck Builder - Demonstration script."""

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    """Demonstrate the Deck Builder system."""
    try:
        print("=== DataDeck Deck Builder ===\n")

        deck = Deck()

        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        bolt = SpellCard("Lightning Bolt", 3, "Rare", "damage")
        crystal = ArtifactCard("Mana Crystal", 2, "Common",
                               5, "+1 mana per turn")

        print("Building deck with different card types...")
        deck.add_card(dragon)
        deck.add_card(bolt)
        deck.add_card(crystal)

        stats = deck.get_deck_stats()
        print(f"Deck stats: {stats}")

        deck.shuffle()

        print("\nDrawing and playing cards:\n")
        game_state = {"mana": 10}

        while True:
            card = deck.draw_card()
            if card is None:
                break
            info = card.get_card_info()
            card_type = info.get("type", "Unknown")
            print(f"Drew: {card.name} ({card_type})")
            result = card.play(game_state)
            print(f"Play result: {result['result']}\n")

        print(
            "Polymorphism in action: "
            "Same interface, different card behaviors!"
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
