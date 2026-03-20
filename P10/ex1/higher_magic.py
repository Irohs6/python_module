from typing import Any, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if callable(spell1) and callable(spell2):
        def combined(target: str) -> tuple:
            if isinstance(target, str):
                return spell1(target), spell2(target)
    else:
        raise TypeError("Both arguments must be callable")

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("Base spell must be callable")
    if not isinstance(multiplier, int):
        raise TypeError("Multiplier must be an integer")

    def amplified(target: str) -> Any:
        if isinstance(target, str):
            return base_spell(target) * multiplier
        else:
            raise TypeError("Target must be a string")

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition):
        raise TypeError("Condition must be callable")
    if not callable(spell):
        raise TypeError("Spell must be callable")

    def caster(target: str) -> Any:
        if isinstance(target, str):
            if condition(target):
                return spell(target)
            else:
                return "Spell fizzled"
        else:
            raise TypeError("Target must be a string")

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise TypeError("All elements in spells must be callable")

    def sequence(target: str) -> list:
        if isinstance(target, str):
            return [spell(target) for spell in spells]
        else:
            raise TypeError("Target must be a string")

    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}!"


def heal(target: str) -> str:
    return f"Heal restores 30 health to {target}!"


def main():
    combined_spell = spell_combiner(fireball, heal)
    print(combined_spell("Goblin"))

    amplified_spell = power_amplifier(fireball, 3)
    print(amplified_spell("Orc"))

    def is_enemy(target: str) -> bool:
        return target in ["Goblin", "Orc"]

    conditional_spell = conditional_caster(is_enemy, fireball)
    print(conditional_spell("Goblin"))
    print(conditional_spell("Villager"))

    sequence_spell = spell_sequence([fireball, heal])
    print(sequence_spell("Dragon"))


if __name__ == "__main__":
    main()
