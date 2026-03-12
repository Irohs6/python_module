#!/usr/bin/env python3

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        atk: int,
        health: int,
        base_rating: int = 1000,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.atk = atk
        self.health = health
        self.wins = 0
        self.losses = 0
        self._base_rating = base_rating
        self._rating = base_rating

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

    def attack(self, target) -> dict:
        damage = self.atk
        if hasattr(target, "defend"):
            if hasattr(target, "health"):
                target.defend(damage)
            return {
                "damage_dealt": damage,
                "target_remaining_health": target.health,
            }
        else:
            return {
                "damage_dealt": damage,
                "target_remaining_health": None,
            }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        return {
            "damage_taken": incoming_damage,
            "remaining_health": self.health,
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.atk, "health": self.health}

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self._rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self._rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating(),
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}",
            "interfaces": ["Card", "Combatable", "Rankable"],
        }
