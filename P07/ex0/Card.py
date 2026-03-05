#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract base class defining the universal card blueprint."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """Initialize a card with name, cost, and rarity."""
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("cost must be a positive integer")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Play this card, applying its effect to the game state."""
        pass

    def get_card_info(self) -> dict:
        """Return a dictionary with the card's information."""
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with the available mana."""
        return available_mana >= self.cost
