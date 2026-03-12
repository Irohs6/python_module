
from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Carte Elite - Implémente 3 interfaces!
    - Card: Comportement de base
    - Combatable: Capacités de combat
    - Magical: Capacités magiques
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defense: int, mana_pool: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.defense_power = defense
        self.mana_pool = mana_pool
        self.current_health = 10

    # Implémentation de Card

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
                    'effect': 'Elite card summoned to battlefield with '
                    'combat and magic abilities'
                }
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': 'Elite',
            'attack': self.attack_power,
            'defense': self.defense_power,
            'mana_pool': self.mana_pool
        })
        return info

    # Implémentation de Combatable

    def attack(self, target: Card | str) -> dict:
        """Attack a target, dealing damage."""
        target_name = target.name if isinstance(target, Card) else str(target)
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(incoming_damage, self.defense_power)
        taken = incoming_damage - blocked
        self.current_health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.current_health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "defense": self.defense_power,
            "health": self.current_health
        }

    # Implémentation de Magical

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(spell_name) % 5 + 1
        if self.mana_pool >= mana_cost:
            self.mana_pool -= mana_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": mana_cost
            }
        return {"error": "Not enough mana"}

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool,
            "spellcasting_available": self.mana_pool > 0
        }
