def record_spell(spell_name: str, ingredients: str) -> str:
    """
    Record a spell after validating its ingredients.

    Uses a late import to avoid circular dependency.

    Args:
        spell_name: Name of the spell
        ingredients: Ingredients of the spell

    Returns:
        Message indicating whether the spell was recorded or rejected
    """
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if result == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
