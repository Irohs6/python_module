#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name.capitalize()
        self.cost = cost
        self.rarity = rarity.capitalize()

    @abstractmethod
    def play(self, game_stats: dict) -> dict:
        pass

    @abstractmethod
    def is_playable(self, avaiable_mana: int) -> bool:
        pass

    def get_card_info(self) -> dict:
        return ({
            "Name": self.name,
            "Cost": self.cost,
            "Rarity": self.rarity
            })
