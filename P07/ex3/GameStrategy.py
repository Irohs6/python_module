#!/usr/bin/env python3

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract base class for game strategies."""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute a turn based on the current hand and battlefield."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize targets based on the strategy."""
        pass
