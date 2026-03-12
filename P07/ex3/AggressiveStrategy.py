#!/usr/bin/env python3

from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Aggressive strategy: prioritize damage and low-cost cards."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute an aggressive turn: play low-cost cards first."""
        sorted_hand = sorted(hand, key=lambda card: card.cost)

        cards_played = []
        mana_used = 0
        damage_dealt = 0
        available_mana = 10

        for card in sorted_hand:
            if card.cost <= available_mana:

                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost

                info = card.get_card_info()

                if info.get("type") == "Creature":
                    damage_dealt += card.attack

                elif info.get("type") == "Spell":
                    damage_dealt += card.cost

        # Determine targets: prioritize battlefield threats, else rush player
        if battlefield:
            prioritized = self.prioritize_targets(battlefield)
            targets_attacked = [
                target.get("name", str(target))
                if isinstance(target, dict) else target.name
                for target in prioritized
            ]
        else:
            targets_attacked = ["Enemy Player"]

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return self.__class__.__name__

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets by threat level (highest first)."""
        return sorted(
            available_targets, key=lambda target:
            getattr(target, "attack", 0) if not isinstance(target, dict)
            else target.get("attack", 0), reverse=True
        )
