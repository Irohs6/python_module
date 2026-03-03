from typing import Callable


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    result = validate_ingredients(ingredients)
    if result == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"


def record_spell_dependency_injection(spell_name: str, ingredients: str,
                                      validate_ingredients: Callable) -> str:
    result = validate_ingredients(ingredients)
    if result == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
