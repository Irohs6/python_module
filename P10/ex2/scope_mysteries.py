

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
        vault[key] = value

    def recall(key: Any):
        return vault.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    for i in range(3):
        print(f"Call {i}: {counter()}")

    print("\nTesting sepll acumulator...")
    accumulator = spell_accumulator(10)
    print(accumulator(1))
    print(accumulator(1), '\n')

    print("Testing enchantment factory...")
    enchantment = enchantment_factory('fire')
    print(enchantment("sword"), '\n')

    print("Testing memory vault...")
    memory = memory_vault()
    print(memory['store']('lapin', 5), memory['recall']('lapin'))


if __name__ == "__main__":
    main()
