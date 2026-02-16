#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Dict, List


class Magical(ABC):
    """Interface pour les entités magiques"""

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: List) -> Dict:
        """Lance un sort"""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        """Canalise du mana"""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        """Retourne les stats magiques"""
        pass
