

def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]

    for valid in valid_ingredients:
        if valid in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
