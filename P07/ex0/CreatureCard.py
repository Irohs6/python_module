#!/usr/bin/env python3
from .Card import Card


class CreatureCard(Card):
    def __init__(self, name, cost, rarity, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.set_attack(attack)
        self.set_health(health)

    def set_attack(self, attack):
        if not isinstance(attack, int):
            raise ValueError(f"{attack} positive interger required")
        if attack < 0:
            raise ValueError(f"Error {attack}  < 0")
        else:
            self.__attack = attack

    def get_attack(self):
        return self.__attack

    def set_health(self, health):
        if not isinstance(health, int):
            raise ValueError(f"{health} positive interger required")
        if health < 0:
            raise ValueError(f"Error {health}  < 0")
        else:
            self.__health = health

    def get_health(self):
        return self.__health

    def is_playable(self, avaiable_mana: int) -> bool:
        if self.cost < avaiable_mana:
            return False
        else:
            return True

    def play(self, game_state: dict) -> dict:
        if not isinstance(game_state, dict):
            raise AttributeError(f"{game_state} is not a dict")
        else:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name if hasattr(target, 'name') else str(target),
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self):
        info: dict = super().get_card_info()
        info["attack"] = self.get_attack()
        info["health"] = self.get_health()
        return info
