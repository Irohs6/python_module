#!/usr/bin/env python3

from ex0.Card import Card


class SpellCard(Card):
    """A spell card that produces instant magical effects."""

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        """Initialize a spell card with an effect type."""
        super().__init__(name, cost, rarity)
        valid_types = ('damage', 'heal', 'buff', 'debuff')
        if effect_type not in valid_types:
            raise ValueError(
                f"effect_type must be one of {valid_types}"
            )
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Play the spell card, applying its instant effect."""
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
        else:
            effects = {
                'damage': f'Deal {self.cost} damage to target',
                'heal': f'Restore {self.cost} health to target',
                'buff': f'Buff target with +{self.cost} stats',
                'debuff': f'Debuff target with -{self.cost} stats'
            }
            return {
                'is_playable': True,
                'result': {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': effects.get(self.effect_type, 'Unknown effect')
                }
            }

    def get_card_info(self) -> dict:
        """Return spell card info including effect type."""

        info = super().get_card_info()
        info['type'] = 'Spell'
        info['effect_type'] = self.effect_type
        return info

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell effect on given targets."""
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets_affected': len(targets),
            'targets': [
                t.name if hasattr(t, 'name') else str(t)
                for t in targets
            ],
            'resolved': True
        }
