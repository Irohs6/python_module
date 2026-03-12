#!/usr/bin/env python3

from ex0.Card import Card


class ArtifactCard(Card):
    """An artifact card that provides permanent game modifications."""

    def __init__(
        self, name: str, cost: int, rarity: str,
        durability: int, effect: str
    ) -> None:
        """Initialize an artifact card with durability and effect."""
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability < 0:
            raise ValueError("durability must be a positive integer")
        self.durability = durability
        self.effect = effect
        self.is_active = True

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
                    'effect': f'Permanent: {self.effect}'
                }
        }

    def get_card_info(self) -> dict:
        """Return artifact card info including durability and effect."""
        info = super().get_card_info()
        info['type'] = 'Artifact'
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info

    def activate_ability(self) -> dict:
        """Activate the artifact's ongoing ability."""
        if not self.is_active or self.durability <= 0:
            return {
                'artifact': self.name,
                'activated': False,
                'reason': 'Artifact is destroyed'
            }
        self.durability -= 1
        if self.durability == 0:
            self.is_active = False
        return {
            'artifact': self.name,
            'activated': True,
            'effect': self.effect,
            'durability_remaining': self.durability
        }
