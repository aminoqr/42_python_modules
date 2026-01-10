#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_name, plant_status, water_level):
    if plant_status == "wilting":
        raise PlantError(f"The {plant_name} plant is wilting!")
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


print("=== Custom Garden Errors Demo ===")
print()
print("Testing PlantError...")
try:
    check_plant("tomato", "wilting", 11)
except PlantError as e:
    print(f"Caught PlantError: {e}")
print()
print("Testing WaterError...")
try:
    check_plant("tomato", "not wilting", 5)
except WaterError as e:
    print(f"Caught WaterError: {e}")
print()

print("Testing catching all garden errors...")
try:
    check_plant("tomato", "wilting", 15)
except GardenError as e:
    print(f"Caught a garden error: {e}")

try:
    check_plant("tomato", "healthy", 4)
except GardenError as e:
    print(f"Caught a garden error: {e}")
print()
print("All custom error types work correctly!")
