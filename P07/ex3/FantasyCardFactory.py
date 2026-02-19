#!/usr/bin/env python3
"""Concrete fantasy-themed card factory."""

import random

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Factory that creates fantasy-themed cards."""

    CREATURES = {
        "dragon": ("Fire Dragon", 5, "Legendary", 7, 5),
        "goblin": ("Goblin Warrior", 2, "Common", 3, 2),
    }

    SPELLS = {
        "fireball": ("Fireball", 4, "Rare", "damage"),
        "lightning": ("Lightning Bolt", 3, "Rare", "damage"),
        "heal": ("Healing Light", 2, "Common", "heal"),
    }

    ARTIFACTS = {
        "mana_ring": ("Mana Ring", 2, "Common", 5, "+1 mana per turn"),
    }

    # ---- Creature ----

    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> CreatureCard:
        """Create a fantasy creature card."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key in self.CREATURES:
                name, cost, rarity, attack, health = self.CREATURES[key]
                return CreatureCard(name, cost, rarity, attack, health)

        elif isinstance(name_or_power, int):
            name, cost, rarity, _, health = random.choice(
                list(self.CREATURES.values())
            )
            attack = name_or_power
            return CreatureCard(name, cost, rarity, attack, health)

        name, cost, rarity, attack, health = random.choice(
            list(self.CREATURES.values())
        )
        return CreatureCard(name, cost, rarity, attack, health)

    # ---- Spell ----

    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> SpellCard:
        """Create a fantasy spell card."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key in self.SPELLS:
                name, cost, rarity, effect_type = self.SPELLS[key]
                return SpellCard(name, cost, rarity, effect_type)

        elif isinstance(name_or_power, int):
            name, _, rarity, effect_type = random.choice(
                list(self.SPELLS.values())
            )
            cost = name_or_power
            return SpellCard(name, cost, rarity, effect_type)

        name, cost, rarity, effect_type = random.choice(
            list(self.SPELLS.values())
        )
        return SpellCard(name, cost, rarity, effect_type)

    # ---- Artifact ----

    def create_artifact(
        self, name_or_power: str | int | None = None
    ) -> ArtifactCard:
        """Create a fantasy artifact card."""
        if isinstance(name_or_power, str):
            key = name_or_power.lower()
            if key in self.ARTIFACTS:
                name, cost, rarity, durability, effect = self.ARTIFACTS[key]
                return ArtifactCard(name, cost, rarity, durability, effect)

        elif isinstance(name_or_power, int):
            name, cost, rarity, _, effect = random.choice(
                list(self.ARTIFACTS.values())
            )
            durability = name_or_power
            return ArtifactCard(name, cost, rarity, durability, effect)

        name, cost, rarity, durability, effect = random.choice(
            list(self.ARTIFACTS.values())
        )
        return ArtifactCard(name, cost, rarity, durability, effect)

    # ---- Deck ----

    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck with a mix of card types."""
        deck: dict[str, list] = {
            "creatures": [],
            "spells": [],
            "artifacts": [],
        }

        creators = [
            ("creatures", self.create_creature),
            ("spells", self.create_spell),
            ("artifacts", self.create_artifact),
        ]

        for _ in range(size):
            key, creator = random.choice(creators)
            deck[key].append(creator())

        return deck

    # ---- Supported types ----
    def get_supported_types(self) -> dict:
        """Return supported card types and their options."""
        return {
            "creatures": list(self.CREATURES.keys()),
            "spells": list(self.SPELLS.keys()),
            "artifacts": list(self.ARTIFACTS.keys()),
        }
