from alchemy.potions import strength_potion

print("\n=== Import Transmutation Mastery ===\n")

import alchemy.elements
print("Method 1 - Full module import:")
print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}\n")

from alchemy.elements import create_water
print("Method 2 - Specific function import:")
print(f"create_water(): {create_water()}\n")

from alchemy.potions import healing_potion as heal
print("Method 3 - Aliased import:")
print(f"heal(): {heal()}\n")

from alchemy.elements import create_fire, create_earth
from alchemy.potions import strength_potion
print("Method 4 - Multiple imports:")
print(f"create_earth(): {create_earth()}")
print(f"create_fire(): {create_fire()}")
print(f"strength_potion(): {strength_potion()}\n")

print("All import transmutation methods mastered!")
