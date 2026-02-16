#!/usr/bin/env python3
"""Demonstration of Abstract Factory + Strategy Pattern."""

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """Demonstrate the game engine with factory and strategy."""
    print("=== DataDeck Game Engine ===\n")

    # Configure
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    # Show available types
    types = factory.get_supported_types()
    print(f"\nAvailable types: {types}")

    # Simulate turn
    print("\nSimulating aggressive turn...")
    hand = [
        factory.create_creature('dragon'),
        factory.create_creature('goblin'),
        factory.create_spell('lightning'),
    ]
    hand_display = [f"{c.name} ({c.cost})" for c in hand]
    print(f"Hand: {hand_display}")

    result = strategy.execute_turn(hand, [])
    print("\nTurn execution:")
    print(f"Strategy: {result['strategy']}")
    actions = {
        'cards_played': result['cards_played'],
        'mana_used': result['mana_used'],
        'targets_attacked': result['targets_attacked'],
        'damage_dealt': result['damage_dealt'],
    }
    print(f"Actions: {actions}")

    # Engine simulation
    engine.simulate_turn()
    report = engine.get_engine_status()
    print(f"\nGame Report: {report}")

    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
