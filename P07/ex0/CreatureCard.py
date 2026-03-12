#!/usr/bin/env python3
from .Card import Card


class CreatureCard(Card):
    """A creature card with attack and health attributes."""

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(attack, int) or attack < 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health < 0:
            raise ValueError("health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """Play the creature card onto the battlefield."""
        if not isinstance(game_state, dict):
            raise ValueError("game_state must be a dictionary")
        if not self.is_playable(game_state.get('mana', 0)):
            return {
                'is_playable': False,
                'result':
                    {
                        'card': self.name,
                        'required_mana': self.cost,
                        'available_mana': game_state.get('mana', 0)
                    }
            }
        return {
            'is_playable': True,
            'result':
                {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'
                }
        }

    def get_card_info(self) -> dict:
        """Return creature card info including attack and health."""

        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target: Card | str) -> dict:
        """Attack a target, dealing damage equal to attack value."""

        target_name = (
            target.name if isinstance(target, Card) else str(target)
        )
        combat_resolved = (True if isinstance(target, CreatureCard)
                           and target.health <= self.attack else False)
        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack,
            'combat_resolved': combat_resolved
        }
