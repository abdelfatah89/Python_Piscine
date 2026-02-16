def validate_ingredients(ingredients: str) -> str:
    valid_list = ["air", "earth", "water", "fire"]
    for item in valid_list:
        if item.lower() in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
