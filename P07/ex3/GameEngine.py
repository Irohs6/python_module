#!/usr/bin/env python3
"""Game engine orchestrator."""

from typing import Optional

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Orchestrates card creation and strategy execution."""

    def __init__(self) -> None:
        """Initialize the game engine."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.hand: list = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Configure the engine with a factory and strategy."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """Simulate a game turn using factory and strategy."""
        if not self.factory or not self.strategy:
            return {'error': 'Engine not configured'}

        if not self.hand:
            self.hand = [
                self.factory.create_creature('dragon'),
                self.factory.create_creature('goblin'),
                self.factory.create_spell('lightning'),
            ]
            self.cards_created += len(self.hand)

        result = self.strategy.execute_turn(self.hand, [])
        self.turns_simulated += 1
        self.total_damage += result.get('damage_dealt', 0)
        self.hand = []
        return result

    def get_engine_status(self) -> dict:
        """Return current engine status."""
        strategy_name = (
            self.strategy.get_strategy_name()
            if self.strategy else 'None'
        )
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strategy_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
