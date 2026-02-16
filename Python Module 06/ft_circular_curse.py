print("\n=== Circular Curse Breaking ===\n")

from alchemy.grimoire.validator import validate_ingredients
print("Testing ingredient validation:")
print(f"validate_ingredients('fire air'): "
      f"{validate_ingredients('fire air')}")
print(f"validate_ingredients('dragon scales'): "
      f"{validate_ingredients('dragon scales')}\n")

from alchemy.grimoire.spellbook import record_spell
print("Testing spell recording with validation:")
print(f"record_spell('Fireball', 'fire air'): "
      f"{record_spell('Fireball', 'fire air')}")
print(f"record_spell('Dark magic', 'shadow'): "
      f"{record_spell('Dark magic', 'shadow')}\n")

print(f"record_spell('Lightning', 'air'): "
      f"{record_spell('Lightning', 'air')}\n")

print("Circular dependency curse avoided using late imports!")
print("All spells processed safely!")