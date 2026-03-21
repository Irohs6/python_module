from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs) -> tuple:
        return spell1(*args, **kwargs), spell2(*args, **kwargs)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list:
        return [spell(*args, **kwargs) for spell in spells]

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
