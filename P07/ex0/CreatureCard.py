#!/usr/bin/env python3
from .Card import Card


class CreatureCard(Card):
    """A creature card with attack and health attributes."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        attack: int, health: int
    ) -> None:
        """Initialize a creature card."""
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("health must be a positive integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Play the creature card onto the battlefield."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> dict:
        """Return creature card info including attack and health."""
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target: object) -> dict:
        """Attack a target, dealing damage equal to attack value."""
        target_name = (
            target.name if hasattr(target, 'name') else str(target)
        )
        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
