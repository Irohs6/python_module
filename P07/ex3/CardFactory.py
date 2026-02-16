#!/usr/bin/env python3


from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory for creating different types of cards."""

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        """Create a creature card with combat abilities."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        """Create a spell card with magical abilities."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        """Create an artifact card with unique effects."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck with a mix of card types."""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Return supported card types."""
        pass
