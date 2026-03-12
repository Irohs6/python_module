#!/usr/bin/env python3

import random
from typing import Optional

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    """A deck management class that handles any card type."""

    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """Add a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a card by name. Returns True if found and removed."""
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """Shuffle the deck randomly."""
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Draw the top card from the deck."""
        if not self.cards:
            return None
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """Return statistics about the deck composition."""
        creatures = sum(
            1 for card in self.cards if isinstance(card, CreatureCard)
        )
        spells = sum(1 for card in self.cards if isinstance(card, SpellCard))
        artifacts = sum(
            1 for card in self.cards if isinstance(card, ArtifactCard)
        )
        total = len(self.cards)
        avg_cost = (
            round(sum(card.cost for card in self.cards) / total, 1)
            if total
            else 0.0
        )
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
