def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    res = validate_ingredients(ingredients)
    if "INVALID" in res:
        return f"Spell rejected: {spell_name} ({res})"
    else:
        return f"Spell recorded: {spell_name} ({res})"