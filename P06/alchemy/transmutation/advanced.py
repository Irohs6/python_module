def philosophers_stone():
    from .basic import lead_to_gold
    from ..potions import healing_potion
    lead_to_gold_result = lead_to_gold()
    heal_result = healing_potion()
    return (f"Philosopher’s stone created using {lead_to_gold_result}"
            f" and {heal_result}")


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
