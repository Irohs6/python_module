#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.Card import Card


class Combatable(ABC):
    """Mixin class to add combat capabilities to a card."""

    @abstractmethod
    def attack(self, target: Card) -> dict:
        """Attack a target, dealing damage equal to attack value."""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """Defend against an incoming attack, reducing health."""
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """Return current combat stats of the card."""
        pass
