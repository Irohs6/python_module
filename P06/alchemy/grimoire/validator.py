def validate_ingredients(ingredients: str) -> str:
    """
    Validate the ingredients of a spell.

    Args:
        ingredients: String containing the ingredients

    Returns:
        "[ingredients] - VALID" or "[ingredients] - INVALID"
    """
    valid_ingredients = ["fire", "water", "earth", "air"]

    for valid in valid_ingredients:
        if valid in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
