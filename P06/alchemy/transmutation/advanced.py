from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create the philosopher's stone using relative imports."""
    lead_to_gold_result = lead_to_gold()
    heal_result = healing_potion()
    return (
        f"Philosopher’s stone created using {lead_to_gold_result}"
        f" and {heal_result}"
    )


def elixir_of_life() -> str:
    """Create the elixir of life for eternal youth."""
    return "Elixir of life: eternal youth achieved!"
