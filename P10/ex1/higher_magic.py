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
    return f"Heal {target}!"


def power_spell(power: int)-> int:
    return (power)


def main():
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    result1, result2 = combined_spell('Dragon')
    print(f"Combined spell result: {result1}, {result2}\n")

    print("Testing power amplifier...")
    amplified_spell = power_amplifier(power_spell, 3)
    print(f"Original: {power_spell(10)}, Amplified: {amplified_spell(10)}\n")

    def is_enemy(target: str) -> bool:
        return target in ["Goblin", "Orc"]

    print("Testing conditional spell...")
    conditional_spell = conditional_caster(is_enemy, fireball)
    print(conditional_spell("Goblin"))
    print(conditional_spell("Villager"), '\n')

    print("Testing spell sequence...")
    sequence_spell = spell_sequence([fireball, heal])
    for result in sequence_spell("Dragon"):
        print(result)


if __name__ == "__main__":
    main()
