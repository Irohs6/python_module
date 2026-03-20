

from typing import Any, Callable


def mage_counter() -> Callable:
    counter: int = 0

    def counter_():
        nonlocal counter
        counter += 1
        return counter
    return counter_


def spell_accumulator(initial_power: int) -> Callable:

    def accumualte_power(add: int):

        nonlocal initial_power
        initial_power += add
        return initial_power

    return accumualte_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def apply_enchantement(item_name: str):
        return enchantment_type + chr(32) + item_name
    return apply_enchantement


def memory_vault() -> dict[str, callable]:
    vault: dict[Any, Any] = {}

    def store(key: Any, value: Any):
        if key not in vault.keys():
            vault[key] = value
        else:
            raise KeyError

        def recall(key: Any):
            vault.get(key, None)
            return {
                'store': store,
                'recall': recall
            }
