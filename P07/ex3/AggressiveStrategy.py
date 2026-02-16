#!/usr/bin/env python3

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Aggressive strategy: prioritize damage and low-cost cards."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute an aggressive turn: play low-cost cards first."""
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        available_mana = 5

        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost
                info = card.get_card_info()
                if info.get('type') == 'Creature':
                    damage_dealt += info.get('attack', 0)
                elif info.get('type') == 'Spell':
                    damage_dealt += card.cost

        return {
            'strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets by threat level (highest first)."""
        return sorted(
            available_targets,
            key=lambda t: t.get('attack', 0),
            reverse=True
        )
